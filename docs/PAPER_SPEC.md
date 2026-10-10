# Paper Spec

## Venue & format
- **Template:** _IEEEtran conference | IEEEtran journal | ACM acmart | NeurIPS | LNCS_
- **Length:** _N pages excluding references (hard cap)._
- **Author block:** _name, affiliation, email._

## Paper type
_One of: empirical | theoretical | survey | position. This decides which sections are required._

## Thesis
- **Claim:** _one sentence, stated exactly as the paper should defend it._
- **Strength:** _what the paper must NOT overclaim (e.g. "applies to all computable agents,
  not AI specifically")._
- **Novelty:** _what is new vs. restated. If it is synthesis, say so in the paper._

## Section plan
_Ordered list. One line each: title + what it must establish._
1. Introduction: problem, thesis, contributions (3–5 bullets).
2. Related work: _closest 3–5 lines of work and the gap._
3. ...
N. Conclusion: no new claims.

## Content rules
- **Formal results:** _Definitions/theorems required? Full proofs or sketches?_
- **Examples:** _max K, only where a result is abstract; one per key result, not one per theorem._
- **Figures/tables:** _which ones, and their purpose. Tables over figures if space is tight._
- **Experiments:** _real numbers provided below, or none. Never invent results._

## Citations
- Use `thebibliography` (single-file) | `.bib` file.
- Cite only works you are confident exist, with correct venue and year.
- Anything uncertain: keep the claim, mark `% TODO: verify` in the source, and list it
  in the hand-off message. Never fabricate arXiv IDs, page numbers or DOIs.

## Style
- _Tone: formal, direct, no hype words ("revolutionary", "groundbreaking")._
- _Notation: define every symbol at first use; consistent macros._

## Output contract
- One self-contained `.tex` file that compiles with pdflatex twice, no errors,
  no overfull boxes > 5pt.
- Hand-off message: page count, list of `% TODO: verify` items, nothing else.

## Inputs
_Paste here: notes, results tables, figures, prior drafts, must-cite papers._
