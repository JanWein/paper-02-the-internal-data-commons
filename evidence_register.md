# Current R2 addendum, 17 October 2026

| Claim | Evidence and scope | Location |
|:--|:--|:--|
| Branch score needs its actual-baseline constant | Direct expansion and constrained KKT proof; independently exact synthetic regression | Proposition 4, Appendix C, Section 8.5; code/reproduce_R2.py |
| Prior financing results preserved | Five scientific outputs match historical R1 hashes after rerun | results_R2/crossing_baseline_exact.json |
| Disconnected feasible sets | Not established; assertion withdrawn. Largest-point proof needs no interval assumption | Theorem 2 and Appendix E |
| Closest data-sharing mechanism | Primary PDF, arXiv:2107.08630v2, Sections 4-5, pp. 8-13, read in this revision | Section 2; https://arxiv.org/pdf/2107.08630 |
| Strict participation | Open fee upper bound; zero minimum rent precludes strict participation at nonnegative fee | Section 6 |

Retrieval log: direct versioned PDF request failed; unversioned arXiv PDF succeeded and its first page identifies v2, 20 July 2021. Read Assumptions 4.1-4.3, Propositions 4.1-4.2 and proof, and Assumptions 5.1-5.4, mixed-VCG definition, Proposition 5.1/proof, equation (31), and distorted variant. The manuscript distinguishes the source's welfare notions rather than assuming its instruments apply to our model. No external copies are redistributed. No comprehensive new literature census is claimed.

The preserved R1 ledger below records earlier sources and access limits; the current closest data-sharing comparison is the one above.

# Evidence and literature register: latest R1 revision

17 October 2026. This register supersedes the previous register, retained in `history/`. The manuscript is a completed theoretical article at its stated scope. No corporate observations, causal effects, author contacts, paid access, or external submissions occurred.

## Claims and access depth

| Manuscript claim | Primary basis | What was actually read or verified | Remaining boundary |
|:--|:--|:--|:--|
| Nonrival data can be inefficiently withheld | Jones and Tonetti (2020), author-hosted published PDF | Relevant model and discussion in initial run | Does not establish our internal support mechanism |
| Internal knowledge incentives are established | Cabrera-Cabrera (2002); Siemsen-Balasubramanian-Roth (2007) | Publisher abstracts, metadata; official INFORMS citation rechecked in R1 | No first-internal-incentives claim |
| Knowledge disclosure and downstream effort are distinct | d'Aspremont et al. (1998), author-hosted reprint | Model, assumptions, implementation theorem in initial run | Our contracting environment is narrower |
| Internal creation, sharing and technology already modeled | Jamm (2018), institutional working paper | Relevant model/technology sections in initial run | Preliminary working paper, later publication not verified |
| Transfer-price mechanism comparison | Dikolli-Vaysman (2006) | Publicly accessible article-in-press reprint, Sections 2-6 | We do not claim to have verified every supplementary proof |
| Club pricing and self-financing are established | Berglas-Pines (1981), publisher summary; Buchanan (1965), bibliographic record | Publisher states pricing/provision and surplus/deficit scope | Full club reprint unavailable; no detailed theorem imported |
| Cost uncertainty and restricted rent extraction already studied | Bierbrauer (2011), institutional working version 2010/01 | Introduction, institutional timing and alternative approval-rule comparison | Our frontier is restricted to a specific ledger class |
| Unpriced-opening loss, sequential score, reserve frontier | New manuscript Propositions 1-4 and Theorems 1-2 | Complete proofs in Appendices A-E | Model results, not verified global priority or firm prevalence |
| Two-margin interaction signs | Declared exact rational example | Executed fraction calculations in `results_R1/exact_interaction.json` | Existence on specified additive scales |
| Numerical implementation | Active-set solver plus independent optimization | Eight boundary/interior cases and exact financing roots | Checks algebra/software, not assumptions |

## Required bibliographic corrections and verifications

**Siemsen et al.** Official INFORMS citation: *Management Science* **53(10):1533-1550**, DOI **10.1287/mnsc.1070.0714**. The previous local bibliography already used issue 10; the R1 version confirms and retains it, rather than asserting that a nonexistent local issue-12 entry was changed. Source: https://pubsonline.informs.org/doi/10.1287/mnsc.1070.0714, citation and volume/issue sections.

**Dikolli-Vaysman.** Official ScienceDirect record confirms DOI **10.1016/j.jacceco.2005.06.001**, *JAE* 41(1-2), **201-234**. Accessible article-in-press header has different page numbers; use final publisher pagination. Public reprint text was read beyond the abstract, resolving the earlier access limitation. No external reprint is redistributed.

Official record: https://www.sciencedirect.com/science/article/pii/S0165410106000085

Accessible primary article text: https://www.academia.edu/116922110/Information_Technology_Organizational_Design_and_Transfer_Pricing, reached from the public author profile's article link.

SSRN 887764 and the delivery URL returned 403 or errors. The companion proof-note record 887732 was found but not obtained. The accessible primary article supplied the actual model and mechanism comparison; appendix-level supplementary-proof equivalence was not claimed.

**Bierbrauer.** Published DOI **10.1016/j.jpubeco.2010.11.028**, *JPubE* 95(7-8):553-569. Institutional working version has the expanded title *An Incomplete Contracts Perspective on the Provision and Pricing of Excludable Public Goods*, revised April 2010: https://homepage.coll.mpg.de/pdf_dat/2010_01online.pdf. It was read as a working version, not mislabeled the final journal text.

**Berglas-Pines.** Published *JPubE* 15(2):141-162, DOI **10.1016/0047-2727(81)90030-X**. The publisher summary explicitly covers optimal prices and financing surplus/deficit. Direct full-text access failed; the Queen's WP 297 record says no downloadable version. This limits detailed priority assessment. Our generic pricing and financing ingredients are credited to the existing literature.

## R1 search and retrieval log

The following query groups were executed, with title variants and primary-source follow-up. The earlier run's detailed log is retained in the historical register. Search failure was never taken as evidence of originality.

1. `Dikolli Vaysman 2006 Information technology organizational design transfer pricing DOI pdf`; `Siemsen Balasubramanian Roth 2007 1533 1550 Management Science 53 10`; `public goods nonrival excludable congestion internal transfer pricing two part tariff investment budget balance`. Located official records, companion proofs, and congestion-financing comparators.
2. Exact-title searches for the Dikolli-Vaysman DOI, working-paper PDF, and `Complete Proofs to Theorems`. Verified final DOI against the publisher's indexed record. Direct publisher and SSRN opens failed.
3. Searches restricted to INSEAD, Duke, and public faculty profiles, plus title/date `June 2, 2005`. Duke timed out; an INSEAD result was a different paper citing the target and was not treated as the target. The public Baruch profile has inconsistent pagination, so the official publisher record takes precedence.
4. Opened the public author profile on Academia, followed its actual article and download links. Article text opened; download link failed. Read the original model, cost-based pricing, profit-sharing, reporting and bargaining sections, and the improving-IT and two-sided-coarse-information qualifications. This supports a mechanism comparison, not just an abstract comparison.
5. `Buchanan 1965 Economic Theory Clubs Economica 32 1 14 doi`; `Berglas 1976 Distribution Tastes Skills Provision Local Public Goods club congestion pricing financing`; `club nonrival congestion private information budget provision mechanism`. Located Berglas-Pines synthesis and self-financing literature.
6. Exact Berglas-Pines title/PDF search; `Incomplete contracts and excludable public goods authors 2011 self financing`. Publisher metadata and summary read. Direct club full text failed. Queen's WP record has no download. Bierbrauer's published record and institutional preprint located.
7. `site:coll.mpg.de Incomplete contracts and excludable public goods pdf`; same query for Cologne. Opened the actual MPI 2010/01 institutional PDF and examined the model's contracting restrictions and cost-uncertainty rationale.

No systematic database review, complete citation-network census, or definitive worldwide priority certification was completed. The closest comparison now includes club-good and procurement financing, not just data governance. That broader comparison constrains the contribution claim.

## Computation provenance

All economic primitives are declared in `code/reproduce_R1.py`. The main contribution is proved analytically. Numerical examples were selected to instantiate those results, not fitted to observations. Exact financing constraints use rational coefficients and isolate every boundary for one declared example. The default R1 command does not run the old synthetic exposure estimator or report it as validation of the organizational mechanism. Dependency versions and outputs are included.
