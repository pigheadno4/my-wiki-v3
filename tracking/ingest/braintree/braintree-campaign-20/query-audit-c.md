# Braintree C20 query audit — Group C

Scope: exactly the four fixed Group C questions for Fraud Protection Advanced and Fraud Protection. Both selected raws were read completely; no additional factual evidence was needed.

## `fraud-tools-premium-fraud-protection-advanced`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-fraud-protection-advanced]]`) → `wiki/concepts/braintree-fraud-protection-advanced.md` (`## Sources` → `[[source-braintree-fraud-tools-premium-fraud-protection-advanced]]`) → `wiki/sources/braintree/source-braintree-fraud-tools-premium-fraud-protection-advanced.md` (`raw_files` and `## Raw Sources`) → `raw/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced-2026-09-16.md`.

1. **Where is Fraud Protection Advanced documented?**
   - **Object/action match:** The named Braintree **Fraud Protection Advanced** premium fraud product and its card-transaction risk evaluation, not the distinct Fraud Protection product or another fraud, authentication or chargeback tool.
   - **Direct answer:** `source-braintree-fraud-tools-premium-fraud-protection-advanced.md` is the promoted retrieval entry and routes through the distinct Advanced concept to the complete collected **Fraud Protection Advanced** article at the exact raw path above.
   - **Exact raw locator:** embedded source URL at line 1; raw title/slug at lines 6–7; `# Fraud Protection Advanced`, lines 14–18.
   - **Verdict:** **PASS** — the live provider/concept route reaches the requested product page and its owned raw evidence.

2. **What purpose, setup, outcome and eligibility boundaries does this page itself state?**
   - **Object/action match:** Advanced product purpose, configuration/review setup, its own risk-decision outcomes and stated merchant eligibility; no sibling-product eligibility or decision states are imported.
   - **Direct answer:** The page describes Fraud Protection Advanced as machine-learning evaluation of card transactions using customer-device and transaction data, intended to produce fraud scores that help reject highly suspected fraud while reducing false-positive rejection. Its feature table says code changes are minimal, rules are merchant-created and customizable, detailed risk data and transaction review/webhooks are available, additional fees apply, and availability is limited to eligible Braintree Direct merchants using the “latest SDKs”; it names no SDK or version, so the snapshot does not prove current eligibility or enablement. Merchants can add Dashboard custom fields for filter conditions and designate suspicious payments for manual review by creating a filter labeled **Review**. For new transactions, **Approve** and **Review** are sent to the processor, **Decline** is gateway rejected, and **Not Evaluated** is sent to the processor by default; timeout beyond an internal decision threshold or an evaluation error yields **Not Evaluated**. Sending to the processor does not establish processor approval or settlement.
   - **Exact raw locator:** purpose and data scope at lines 14–18; feature/setup, eligibility and fee table at lines 26–35; custom-field setup at lines 53–84; review setup and action at lines 87–91; decision mapping and default risk filter at lines 104–115; **Not Evaluated** causes at lines 128–138.
   - **Verdict:** **PASS** — the source/raw pair answers each requested boundary while retaining the unspecified-SDK, page-scoped eligibility and downstream-outcome qualifications.

## `fraud-tools-premium-fraud-protection`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-fraud-protection]]`) → `wiki/concepts/braintree-fraud-protection.md` (`## Sources` → `[[source-braintree-fraud-tools-premium-fraud-protection]]`) → `wiki/sources/braintree/source-braintree-fraud-tools-premium-fraud-protection.md` (`raw_files` and `## Raw Sources`) → `raw/braintree/articles/guides/fraud-tools/premium/fraud-protection-2026-09-16.md`.

3. **Where is Fraud Protection documented?**
   - **Object/action match:** The product explicitly titled **Fraud Protection** and its card-transaction risk evaluation, not Fraud Protection Advanced or a generic label for Braintree fraud tooling.
   - **Direct answer:** `source-braintree-fraud-tools-premium-fraud-protection.md` is the promoted retrieval entry and routes through the distinct Fraud Protection concept to the complete collected **Fraud Protection** article at the exact raw path above.
   - **Exact raw locator:** embedded source URL at line 1; raw title/slug at lines 6–7; `# Fraud Protection`, lines 14–20.
   - **Verdict:** **PASS** — the live provider/concept route reaches the requested named product page and its owned raw evidence.

4. **What scope and qualifications does this page state, distinct from Advanced?**
   - **Object/action match:** The named Fraud Protection product’s own purpose, merchant-interface statement, new-transaction decision flow and diagnostic, bounded against Advanced-only eligibility and decision claims.
   - **Direct answer:** The page describes Fraud Protection as a Premium Fraud Management Tool that applies machine learning to customer-device and transaction data to score card transactions, helping merchants reject transactions highly suspected of fraud while avoiding over-blocking likely good transactions. It says merchants can view and tune fraud filters through a Fraud Protection merchant interface. For a new transaction it sends information to PayPal’s internal Fraud Protection service and uses adaptive rules and filters to decide **Approve** or **Decline**: **Approve** is sent to the processor and **Decline** is gateway rejected. The default Transaction Risk Filter rejects scores above its configured threshold, with 1000 described as riskiest and 0 as least risky. The page routes risk-decision lookup to Transaction Detail and says `Device Data Captured: True` indicates Premium Fraud Management Tools are functioning. It states no merchant-eligibility rule, exact SDK requirement, additional-fee claim, **Review** state or **Not Evaluated** state; those Advanced claims must not be imported. Sending an approved risk decision to the processor does not prove processor approval or settlement, and the 2026-09-16 snapshot does not prove current support or enablement.
   - **Exact raw locator:** named product purpose and merchant interface at lines 14–20; new-transaction analysis, **Approve**/**Decline** mapping and default score threshold at lines 23–32; Transaction Detail lookup at lines 34–42; device-data diagnostic at lines 45–46.
   - **Verdict:** **PASS** — the source/raw pair preserves this product’s narrower two-state decision evidence and does not inherit Advanced eligibility, fees, review or fallback states.

## Shared gap sweep, extra reads and reciprocal links

- **Pinned evidence:** Both selected raws were read from provenance through their final lines. SHA-256 values match the manifest: Advanced `c52e91bb4e601a6de281112cbcca22083e4ded3968acc799d03ae401a040c8c0`; Fraud Protection `fc8a03b9e860464800772384fc2cbb89372f491754afaf08ea12287f02806ab6`. Each raw line-1 URL also matches its manifest and promoted-source `canonical_url`.
- **Bounded gap sweep / extra full reads:** Filename and full-text searches surfaced the premium overview, custom-field and webhook material plus other fraud-tool and SDK pages. The two selected raws directly answer all four page-scoped questions; adjacent files remained navigation-only, so **no extra raw was read as factual evidence** and no sibling facts were imported.
- **Reciprocal links:** `wiki/index.md` links `braintree-index`; the provider index links both distinct concepts and both promoted sources; each concept links its matching source; each source links its matching concept and exact path-qualified raw through both `raw_files` and `## Raw Sources`. Fraud Protection also links Advanced only as a distinct product, not as factual authority.
- **Completeness:** 4/4 fixed questions contain one route/page context, object/action match, direct answer, exact raw locator and verdict. No retrieval repair or promotion is required.

**Group verdict: PASS (4/4).**
