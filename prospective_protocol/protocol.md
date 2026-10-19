# Prospective supplement: status after R1

This unexecuted design predates the R1 admission and surplus-score mechanism. It is preserved as a measurement and interference protocol, not as a registration-ready test of the replacement theory. A future design must add a support-pricing/admission contrast and validate the incremental surplus score. No inference implementation or firm data is claimed. The completed theoretical article is separate.

# Proposed pre-analysis protocol

**The Internal Data Commons | 17 October 2026. Not registered and not executed.**

This document specifies a prospective partner study. No partner, approval, clusters, sample size, or data access has been secured. Choices marked provisional must be frozen before assignment. The mathematical examples and precision scenarios are synthetic.

## 1. Setting, population, and feasibility gates

Study one organization with repeated cross-unit reuse of existing operational data, decentralized operating budgets, and a credible central capacity reserve. Include source modules with a legitimate downstream opportunity, regardless of whether their producers volunteer. Define a module recipe and freeze its denominator during the baseline. Separately track new modules and changes in sensitivity. Never treat a refusal required by confidentiality as noncompliance.

The sampling frame is a baseline inventory of producer-owned sources and eligible consumer decision tasks. Twelve-month follow-up follows three baseline months; months 1-3 capture setup, months 4-12 capture ongoing maintenance. Track withdrawals, publication reversals after rewards, and service discontinuation. Twelve months need not cover lifetime costs or delayed risks. Report each period and the full-year net value; no short-run success claim can substitute for full follow-up. Extending follow-up is allowed only through a documented amendment before outcomes are examined by arm.

Go/no-go requirements: authorized internal research access; appropriate institutional and employee review; an auditable task inventory; reproducible link maps; reliable independent valuation for a meaningful subset of claims; common service definitions; a capacity reserve whose rules are credible; and adequate independent clusters and exposure support. No recruitment or contact was performed. If fewer than 40 independent ecosystems are feasible, treat the exercise as a feasibility study rather than a confirmatory interaction test. Even 40 clusters have poor precision for moderate effects.

## 2. Assignment and treatments

Map producers, consumers, dataset versions, decision tasks, and shared support personnel over baseline. Partition into ecosystem clusters to reduce, but not assume away, cross-cluster links. Freeze the graph before assignment. Publish a summary of the fraction of weighted edges crossing clusters without revealing confidential unit identities.

Assign each cluster independently to Z=(T,I) in {00,10,01,11}, each with probability .25. Independent rather than exactly balanced assignment simplifies marginal exposure interpretation; expected cell sizes are K/4 and realized sizes vary. A blocked, exactly balanced design may replace this only after recalculating all assignment and exposure probabilities and precision. The supplied balanced precision formulas are approximations to this design, not a completed power analysis of a real network.

T: install a standardized consumer adapter for one predeclared source/interface family. It reduces schema conversion and integration effort while leaving data definitions, mandatory quality thresholds, and access approval common across arms. Measure latency, failed conversions, and integration time as manipulation checks. Avoid silently adding catalog discovery, a new platform, and quality staffing in the same arm. Common baseline documentation is supplied in all arms; additional producer effort remains endogenous.

I: provide capped internal capacity credits for independently verified downstream value and sustained quality, using a preannounced conservative value schedule. No per-download reward. The schedule and monetary conversion into actual producer capacity are frozen before assignment. The center finances credits; recipients do not face marginal use charges. Track whether promised credits actually change producer resources. Caps and delayed payment mean the treatment is an encouragement with a nonlinear payoff, not an observed alpha shift of known magnitude.

All arms receive identical neutral measurement contact, safety review, and random audit probabilities. Auditors evaluate claims with treatment labels masked where feasible. Technical artifacts may reveal assignment, so record masking failures. Restrict cross-arm sharing of adapters only if operationally feasible; otherwise record exposure rather than pretending isolation. A shared central support desk is recorded as a network link.

## 3. Outcomes, estimands, and denominators

**Primary outcome:** annual organizational resource surplus allocated to cluster g, divided by its baseline eligible module count M_g>0. Count consumer benefits in the consumer owner's ledger, producer costs in the producer owner's ledger, and central costs through a frozen allocation key. Use M_g fixed before treatment. Clusters without eligible modules are not in this estimand's target population. Also report unnormalized totals and module-weighted estimates, which answer different questions.

Let Y_g(Z) be this outcome. Assignment vectors have known distribution P. Define the design-marginal mean

mu(z) = (1/K) sum_g E_{P_-g}[Y_g(z,Z_-g)].

The **primary estimand** is Delta_own = mu(11)-mu(10)-mu(01)+mu(00), on the additive resource-value scale. The corresponding averaged main effects are secondary confirmatory estimands. This measures changing own treatment while averaging others at the trial saturation; it is not the whole-organization rollout effect. Under independent assignment, an unbiased estimator of mu(z) is K^-1 sum_g 1{Z_g=z}Y_g/.25. Unequal cluster size must not silently change its weighting.

**Exposure-specific effects:** fix G0 and define E_g=(U_g,D_g), where U_g indicates at least one upstream producer cluster assigned 11 and D_g indicates at least one downstream consumer cluster assigned 11. Isolated directions have exposure zero and are excluded from contrasts requiring positive exposure. This coarse mapping is a working assumption, not a fact. It excludes effects from technical-only and incentive-only neighbors unless they operate through the recorded combined indicator. Therefore report sensitivity using separate T and I weighted upstream/downstream exposure, and a broader shared-support graph. Do not present the coarse controlled contrast as causal if plausible omitted exposures change its interpretation.

Under exposure sufficiency Y_g(Z)=Y_g(Z_g,E_g), define direct(z,z';e) as the average Y_g(z,e)-Y_g(z',e) over a predeclared common-support population. Define spillover(e,e';z) analogously at fixed own assignment. Use joint probabilities pi_g(z,e)=Pr(Z_g=z,E_g=e), and the Horvitz-Thompson mean K_S^-1 sum_{g in S} 1{Z_g=z,E_g=e}Y_g/pi_g(z,e). Compute probabilities by exact enumeration where small, otherwise Monte Carlo with a fixed seed and numerical error bounds. Do not set rare empirical cells to zero or choose a support subset after seeing outcomes. Freeze S from the graph and assignment law, requiring pi>=.02 for each contrasted cell; this threshold is provisional and requires a feasibility calculation before registration.

**Total policy effect:** for a distribution P* of assignments, define V(P*)=sum_g E_{P*}[M_g Y_g(Z)] if Y is normalized; compare it with V(P0). Central costs enter once. Weighted exposure means can estimate policies whose exposure support is present and whose mapping is correct. Under independent four-arm assignment, every full vector has nonzero probability, so a universal-rollout mean is formally identifiable with a full-vector estimator. The all-11 probability is 4^-K, making that estimator practically useless for realistic K. We will not claim a precise universal effect from this factorial trial.

Optional expansion, conditional on enough ecosystems: group clusters into independently assigned superclusters with minimal outside links; randomize superclusters to 0%, 50%, and 100% combined-treatment saturation. Within 50% superclusters randomize eligibility. This identifies policy contrasts only under stated partial-interference or explicit cross-supercluster exposure assumptions and sufficient superclusters. It is a separate design amendment, not part of the current four-arm test. Never report its proposed contrasts as collected evidence.

## 4. Network schema and data dictionary

All identifiers are pseudonymous; only approved linkage custodians retain keys. Store timestamps, source system, missingness reasons, and versions for every record. Monetary fields use one preregistered price year and currency. No example record is an actual firm observation.

| Table / primary key | Essential fields | Unit and rule |
|:--|:--|:--|
| unit / unit_id | cluster_id, function, baseline budget, support pool | One organizational unit; baseline classification |
| module / module_id + version | producer_id, source_id, recipe, eligibility_date, sensitivity, baseline_status | One versioned reusable service; duplicates linked |
| link / module_id + consumer_id + task_id | baseline_expected_uses, weight, approval_scope, informal_link, shared_support | Directed eligible opportunity, including failed/informal uses |
| assignment / cluster_id | T, I, probability, random_seed, assignment_date, protocol_version | One randomized cluster |
| task / task_id + period | consumer_id, alternatives, baseline_loss, decision_rights, decision_rule, overlap_group | Unique downstream decision; eligibility is not use |
| use / module_id + task_id + period | operational_use, approval_id, version_used, evidence_uri, first_use_date | Validated use, not download count |
| effort / unit_id + activity_id + period | module_id, task_id, minutes, activity_type, loaded_rate, released_capacity | Producer/consumer work; activity types are mutually exclusive |
| quality / module_id + audit_id | sampled_probability, test, defect_severity, remediation, unresolved | Accuracy, completeness, freshness, definition fidelity separately |
| value / task_id + period | baseline_alternative, gross_gain, integration_cost, uncertainty_low/high, audit_status | Incremental task benefit; independently evaluated |
| allocation / overlap_group + period | total_allowed_gain, module_weights, unit_owner | Prevent benefit duplication; weights sum to one |
| support / ticket_id | unit_id, module_id, task_id, minutes, queue_delay, escalation | Support resource burden; linked to effort, not recounted |
| access / request_id | decision, reason, sensitivity, policy_version, wait_minutes | Valid restriction distinguished from obstruction |
| intervention / cost_id | central_owner, arm_eligibility, resource_type, amount, allocation_key | Real intervention cost; transfers separately flagged |
| credit / credit_id | producer_id, audited_value_category, awarded, realized_capacity, cap_binding | Internal transfer; excluded from resource-cost total |
| exposure / cluster_id + graph_version | upstream, downstream, support_exposure, pi, MC_error | Based on assignment and frozen graph, never adoption |

Data availability (inventory), information quality (audits), use (task evidence), rights (access and task authority), and outcomes (value ledger) are separate fields. Do not build a data-driven index using successful decisions as an input.

## 5. Cost allocation and welfare accounting

For each task, compare the realized workflow with the best feasible baseline alternative, including an internal substitute dataset. Value improvements relative to that alternative, not relative to doing nothing. Record gross benefit and integration cost separately. An independent evaluator validates time savings, reduced defects, and decision improvements. Freeze the conversion of released time into usable capacity, for example zero for unredeployed slack in a conservative cash view and a shadow wage in an economic-capacity view. Report both views; choose the capacity view as primary only after its valuation rules are validated before assignment.

Book each activity once: creation/documentation; scheduled maintenance; defect correction; consumer integration; producer support; compute; compliance; audit/administration. A support ticket whose minutes are in the effort table is a link to those minutes, not another cost row. Joint products use time recording where possible; otherwise use a fixed baseline allocation key and report alternative keys. Shared infrastructure costs include incremental capacity and a stated fixed-cost amortization scenario, not a chargeback duplicated as infrastructure expense.

A task benefit associated with multiple sources has one overlap-group cap. Allocate its incremental gain across source modules with weights fixed before treatment; report the task-level total independently. Do not count the same avoided duplicated work as both labor savings and improved decision value. The organization-wide ledger is the sum of producer and consumer entries plus central costs once; budget transfers reconcile to zero.

Legal restrictions are hard constraints. For permitted uses, include expected residual risk with an explicit scenario range; do not pretend rare losses are precisely estimated in twelve months. Harmful uses and defects reduce surplus. If rare-event valuations dominate the sign, label welfare inconclusive. No positive average gain can authorize a prohibited use.

## 6. Identification threats and missing outcomes

Selection: baseline inventory rather than volunteered publications defines eligibility. Report ITT including non-adopters and unpublished modules. Stratify or adjust using baseline opportunity, not realized attractiveness. A treatment-induced sensitivity change is an outcome and a documented constraint change; report a frozen-sensitivity analysis and the all-module ITT, not selective deletion.

Interference: retain informal collaborations and shared personnel in G0. Report cross-cluster exposure and graph alternatives. New links are mechanisms; never condition primary estimates on the realized network. Omitted global attention shocks can invalidate exposure-sufficiency claims; design-marginal own contrasts still average over trial assignments, but do not identify total spillovers.

Measurement: audit claims and a random sample of nonclaims in every arm. Nonclaims are not automatically zero benefit. Use audit-probability weights to estimate validated totals, report sampling uncertainty jointly with treatment uncertainty, and cross-check tickets with diaries and task evidence. Independently verify consumer counterfactuals to reduce collusion. A technical log proves access, not value.

Missingness: distinguish confirmed no use, observed use with unvalued gain, absent effort ledger, and withdrawn permission. Predeclare feasible bounds by task category from baseline and report worst-case treatment differences. Use imputation only as a secondary analysis under stated MAR assumptions with baseline predictors and assignment. No claim of positive welfare if reasonable missing-cost or missing-benefit bounds reverse its sign. Report differential ledger completion and audit refusal by arm. No replacement of dropped clusters after assignment.

Competing mechanisms: managerial attention, general training, more producer staff, or improved source quality can explain treatment effects. Common contact and audit schedules, recorded capacity redemption, adapter performance, and quality audits help distinguish these. These checks do not guarantee a causal mediation decomposition. No post-treatment adoption adjustment or causal mediation claim is primary.

## 7. Analysis, multiplicity, precision, and economically meaningful effects

Primary confirmatory test: two-sided interaction in additive annual net surplus with familywise alpha=.05. Main technical and incentive effects form a three-test family with the interaction, controlled by Holm. A prespecified adjusted estimator uses baseline surplus, opportunity count, and maintenance intensity, without changing the estimand. Unadjusted randomization estimates remain reported. Use the known assignment law; cluster or network dependence must be reflected in variance. Sharp-null randomization tests are exact for a global no-effect null, not automatically for a weak zero-interaction null with other effects. For weak contrasts use a design-based variance estimator, report conservative treatment of zero joint inclusion probabilities, and avoid claiming exact small-sample inference. A methods implementation and full network design simulation are prerequisites to field launch.

Secondary outcomes: validated cross-unit task uses; producer production and maintenance hours; support hours and queue delays; defects; avoided duplication; independently evaluated decision loss; invalid claims and duplicate products. Report them with confidence intervals and false-discovery-rate control within a declared exploratory family. These do not replace the primary welfare test.

Three prespecified moderator families use baseline values only: (i) benefit dispersion, measured as one minus the Herfindahl share of expected consumer benefit; (ii) maintenance intensity, scheduled annual hours per eligible module; (iii) interoperability, median baseline integration hours. Interact continuous centered baseline measures with the factorial interaction; apply Holm across these three tests. Do not claim that dispersion's sign follows from the scalar theory. Data sensitivity is a safety stratum and descriptive moderator, not a fourth confirmatory discovery test.

Economic thresholds: before assignment, the partner must set its annual incremental cost budget C and a minimum worthwhile net benefit delta_E in currency per baseline module, reflecting opportunity cost and accounting uncertainty. Report both a confidence interval for net value and the probability-free break-even accounting range. A standardized statistical effect cannot substitute for delta_E. The present document leaves C and delta_E explicitly unresolved because no partner economics were supplied; it is a complete prospective framework, not a registration-ready protocol.

For balanced K-cluster four-arm means, cluster-level SD sigma, and no interference variance inflation, SE(main)=2 sigma/sqrt(K) and SE(interaction)=4 sigma/sqrt(K). With 80% power, normal critical values 1.96+.842=2.802 give the synthetic MDEs below. The conservative first Holm threshold uses approximately 2.394+.842=3.236. Independent realized allocation, graph dependence, unequal size, skewed gains, and audited sampling can worsen precision. ANCOVA may improve precision if baseline predicts outcomes; no assumed gain is built in.

| Total clusters | Expected clusters per arm | Main MDE / sigma | Interaction MDE / sigma | Interaction MDE / sigma, conservative Holm |
|--:|--:|--:|--:|--:|
| 40 | 10 | .886 | 1.772 | 2.047 |
| 80 | 20 | .627 | 1.253 | 1.447 |
| 160 | 40 | .443 | .886 | 1.023 |
| 320 | 80 | .313 | .627 | .724 |

For planning with team-level observations m and ICC rho, a first approximation is DE=1+(m-1)rho, but the network design and cluster aggregate outcome require direct simulation rather than counting modules as independent teams. Use at least a baseline-based simulation grid over plausible effect sizes, cross-cluster interference, auditing rates, and missingness, with treatment-effect estimates held out during design changes. Such a partner-specific power analysis has not been completed here.

## 8. Mechanism tests and falsification

1. Technical first stage: integration hours and conversion failures fall. If access rises without validated value, inspect independent demand assessments and producer support rather than automatically diagnosing incentive failure.
2. Incentive first stage: announced credits produce realized producer capacity. Increased claims without audited benefits and sustained quality support gaming or metric substitution, not useful provision.
3. Underprovision falsification: in baseline high-opportunity, low-sensitivity modules, an exogenous producer credit that demonstrably raises maintained provision should generate additional validated downstream value exceeding its real costs. An upper confidence bound below the preregistered delta_E, or below zero net gain with adequate precision, rejects an economically material corrective effect for that population. It does not prove all silos efficient.
4. Low-demand counterexample: modules with baseline predicted downstream value below full cost should not become welfare-improving merely because they receive credits. A surge of such publications with no validated use contradicts a broad useful-underprovision narrative.
5. Negative-control quantities: downloads and repeated refresh events may rise while task-level value remains unchanged. Report both rather than retrospectively redefining valuable use.
6. Support mechanism: compare measured support curvature and consumer value growth with the region suggested by Proposition 2. A factorial interaction alone cannot recover elasticities or prove congestion mediation.

## 9. Candidate data and proposed empty outputs

Verified external resources: Census MOPS public tables, the official cognitive-testing paper describing 2015 data-use questions, and official restricted-use access guidance. Public aggregates are useful for motivation and measurement design but cannot identify the internal-network mechanism. Restricted access requires approval and Special Sworn Status; application costs and eligibility need checking. No access, estimate, or approval is asserted. A real partner's internal metadata, task ledger, access records, support tickets, and independent audits are essential and not currently available.

Planned empirical tables, all **NOT COLLECTED**: baseline opportunities and graph links by assigned arm; ITT welfare cell means; factorial interactions with intervals; exposure-specific means and support; task-level validation and missingness; maintenance and support costs; moderators; alternative risk and capacity valuations. Do not insert the synthetic examples from the manuscript into these tables. Any observed partner study would require a new data provenance record and dated protocol amendments.
