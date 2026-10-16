# Fixed retrieval checks — docs-plugins-mirakl-onboard-sellers

## Q1 — Purpose, scope, and what not to infer

**Query:** What does the Mirakl onboarding page cover, and what does it not prove?

**Answer:** It describes seller-to-legal-entity submission, Hosted Onboarding Page access/security and KYC status synchronization for the Adyen Mirakl connector. A seller's separate shops in different currencies each require separate legal-entity onboarding. It does not prove an individual seller completed KYC, gained payout eligibility, received funds or became the merchant of record; linked payment/payout pages own those separate flows. The page was last modified and captured 2026-09-15. Evidence: raw lines 11, 15–21, 23–73, 96–108. Canonical route: [[adyen-index]] → [[adyen-mirakl]] → ## Sources → [[source-adyen-docs-plugins-mirakl-onboard-sellers]] → [[raw/adyen/docs/plugins/mirakl/onboard-sellers/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** What inputs and sequence does seller onboarding require, and how should KYC and bank-data signals be interpreted?

**Answer:** The seller supplies email and legal business name in the country/region's required format; address and bank components have the stated when-provided conditions, with US/Canada State/Province conditional. The connector sends `/legalEntities`, creates an HOP link on the next sync, and the seller answers security questions before Adyen HOP KYC for the account holder and any shareholders. The connector syncs status to Mirakl and sends pass/fail notifications; the listed verification statuses include awaiting data, awaiting verification and failed. Phone numbers require + plus country code. Mirakl Bank name/BIC are mandatory there, whereas HOP asks for IBAN; HOP entry can produce dummy Mirakl bank-name/BIC values, so the page recommends Mirakl bank entry first. None of these signals alone establishes final approval, payout permission or a receiving-bank credit. Evidence: raw lines 25–94. Canonical route: [[adyen-index]] → [[adyen-mirakl]] → ## Sources → [[source-adyen-docs-plugins-mirakl-onboard-sellers]] → [[raw/adyen/docs/plugins/mirakl/onboard-sellers/2026-09-15]].
