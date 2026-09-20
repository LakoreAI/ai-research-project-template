"""Classification evaluation: accuracy, macro-F1, loss, and per-class report.

The single entry point is `evaluate(model, loader, device)`, which returns a
plain dict so the training loop can log it and the standalone evaluator can
save it as JSON. Add task-specific metrics here.
"""

from typing import Dict, Optional

import numpy as np
import torch
from sklearn.metrics import confusion_matrix, f1_score
from torch.utils.data import DataLoader

from src.modules.loss import ClassificationLoss
from src.modules.model import MLPClassifier


@torch.no_grad()
def evaluate(
    model: MLPClassifier,
    loader: DataLoader,
    device: torch.device,
    num_classes: Optional[int] = None,
    criterion: Optional[ClassificationLoss] = None,
) -> Dict[str, object]:
    """Returns {"accuracy", "f1", "loss", "per_class", "confusion"}.

    `accuracy` / `f1` are fractions in [0, 1]; `per_class` maps a class index
    to its accuracy; `confusion` is the raw (K, K) count matrix.
    """
    model.eval()
    criterion = criterion or ClassificationLoss().to(device)

    logits_all, labels_all = [], []
    losses = []
    for x, y in loader:
        x = x.float().to(device)
        y = y.reshape(-1).long().to(device)
        logits, _ = model(x)
        losses.append(criterion(logits, y).item())
        logits_all.append(logits.cpu())
        labels_all.append(y.cpu())

    if not logits_all:
        return {
            "accuracy": float("nan"),
            "f1": float("nan"),
            "loss": float("nan"),
            "per_class": {},
            "confusion": [],
        }

    logits = torch.cat(logits_all)
    labels = torch.cat(labels_all)
    preds = logits.argmax(dim=1)

    accuracy = (preds == labels).float().mean().item()
    f1 = float(f1_score(labels, preds, average="macro", zero_division=0))
    loss = float(np.mean(losses))

    k = num_classes or int(max(labels.max().item(), preds.max().item())) + 1
    conf = confusion_matrix(labels.numpy(), preds.numpy(), labels=list(range(k)))
    per_class = {}
    for c in range(k):
        support = int(conf[c].sum())
        per_class[c] = float(conf[c, c] / support) if support else float("nan")

    return {
        "accuracy": accuracy,
        "f1": f1,
        "loss": loss,
        "per_class": per_class,
        "confusion": conf.tolist(),
    }


def format_report(result: Dict[str, object]) -> str:
    lines = [
        f"accuracy={result['accuracy'] * 100:6.2f}  "
        f"macro-F1={result['f1'] * 100:6.2f}  "
        f"loss={result['loss']:.4f}"
    ]
    for cls, acc in sorted(result["per_class"].items()):
        lines.append(f"  class {cls:>3d}  acc={acc * 100:6.2f}")
    return "\n".join(lines)
