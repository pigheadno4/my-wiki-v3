# Braintree Campaign 39 query audit — group B

## Shared checks

- **Identity PASS:** provider `braintree`; campaign `braintree-campaign-39`; read-only query audit of manifest positions 5–8 only. Objects are the four promoted source pages and their pinned raw files; action is answer verification only, with no repository write, ingest transition, catalog update, or state change.
- **Manifest/hash PASS:** the four raw SHA-256 values match `manifest.json`: identifying fraud `4a51421e…ba90b`, PCI compliance `9f7cf10b…f9b71`, compliance overview `33a25670…e41cb`, and NAB pricing/fees `12ad8907…75e8`.
- **Route/ownership PASS:** each canonical URL has one source owner. Existing routes are `[[index]]` → `[[braintree-index]]` → `[[braintree-fraud-tools]]` (identifying fraud) or `[[braintree-payment-platform]]` (the other three) → exact source → pinned raw. Direct aggregate source listings are deferred as instructed.
- **Full-read/gap-sweep PASS:** all four source pages and pinned raw files were read fully. A bounded filename/canonical-URL sweep found the exact three general pages and account-specific pricing siblings; no sibling or unread related page was needed to answer these exact-page questions. Linked BIN, void/refund, prohibited-transactions, network, PCI, and ecommerce pages remain navigation, not evidence here.

## Position 5 — `articles-risk-and-security-risk-factors-identifying-fraud` — PASS

**Route/page:** `[[index]]` → `[[braintree-index]]` → `[[braintree-fraud-tools]]` → `[[source-braintree-articles-risk-and-security-risk-factors-identifying-fraud]]` → `raw/braintree/articles/risk-and-security/risk-factors/identifying-fraud-2026-09-16.md`.

1. **Exact scope:** Braintree's collected general “Identifying Fraud” risk guide, fetched 2026-09-16 with page metadata dated 2025-04-01. It is a merchant-side checklist for assessing whether a transaction looks suspicious; it names no processor/account, region/jurisdiction, or exhaustive payment-method scope. Card/card-brand, BIN, prepaid, and gift-card examples do not make the indicators proof or a gateway decision. Raw: lines 1–9, 14–18, 60–71.
2. **Purpose/actions and limits:** Use customer-name/address/email, merchant-logged IP, and transaction-pattern indicators as investigation prompts. Merchant IP logging is a prerequisite for IP checks. If suspicious, withhold fulfillment while investigating, contact the customer, and verify contact data; if contact fails or fraud is confirmed, the page suggests void/refund to reduce chargeback likelihood, not guarantee prevention. The indicator lists are at lines 21–71; prerequisite at 45–57; conditional next steps at 76–80. The actual BIN and void/refund procedures are only linked at lines 64 and 80, not specified by this page.

## Position 6 — `articles-risk-and-security-compliance-pci-compliance` — PASS

**Route/page:** `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-articles-risk-and-security-compliance-pci-compliance]]` → `raw/braintree/articles/risk-and-security/compliance/pci-compliance-2026-09-16.md`.

1. **Exact scope:** Braintree's collected PCI DSS/SAQ guidance, fetched 2026-09-16 with page metadata dated 2025-04-01. The page says PCI DSS concerns any business handling, processing, or storing credit cards regardless of size/location, and contains a dated statement that assessments from 2024-03-31 must use PCI DSS 4.0. This is captured provider guidance, not current legal/card-network authority, a merchant assessment, certification, or proof of compliance. Raw: lines 1–9, 17–22.
2. **Purpose/actions and limits:** Complete an SAQ annually; the correct SAQ depends on PCI level and Braintree integration, and Braintree card-data handling does not satisfy the merchant's obligation. The page warns of possible fines/suspension for non-completion. Optional SecurityMetrics help requires approved Braintree application and an emailed Merchant Account Number; Braintree Direct levels 3/4 are described as no-cost, while levels 1/2 may incur SecurityMetrics enterprise fees. The number is not in Control Panel and an authorized signer must request it by email, not phone. Raw: SAQ/level lines 25–34; responsibility/consequences 37–43; assistance/fees 48–58; enrollment prerequisites/procedure 63–82; suspected-compromise escalation 85–86.

## Position 7 — `articles-risk-and-security-compliance-overview` — PASS

**Route/page:** `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-articles-risk-and-security-compliance-overview]]` → `raw/braintree/articles/risk-and-security/compliance/overview-2026-09-16.md`.

1. **Exact scope:** Braintree's collected general compliance orientation, fetched 2026-09-16 with page metadata dated 2025-04-01, for merchants accepting/storing payment methods. It assigns awareness of applicable rules and sanctions to the merchant; the US/international OFAC example is not a complete jurisdiction analysis. Card-brand restrictions vary by merchant location and Braintree integration. The BGN section is specifically for merchants with a BGN merchant account. Raw: lines 1–9, 14–25, 74–80.
2. **Purpose/actions and limits:** Follow applicable requirements and use the linked detailed routes; the page warns that noncompliance can lead to fines, holds, seizure, or legal action. For BGN, use an existing EUR merchant account from 2026-01-01 or contact Braintree/CSM; BGN conversion/rejection and dispute/reporting behavior are at lines 28–61. **Preserved gap:** the page says Braintree will suspend the BGN merchant account on 2025-12-15 (64–66), yet BGN-presented transactions are rejected only after 2025-12-31 23:59 CET (38–42); it does not explain behavior between those dates. PCI and ecommerce orientations are at 83–94. This snapshot is not present legal advice, certification, or account-transition proof.

## Position 8 — `articles-nab-pricing-fees` — PASS

**Route/page:** `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-articles-nab-pricing-fees]]` → `raw/braintree/articles/nab/pricing-fees-2026-09-16.md`.

1. **Exact scope:** Braintree-hosted NAB account/processor pricing snapshot, fetched 2026-09-16 with page metadata dated 2025-04-01. It covers account-selected blended and IC+ models, all-authorization per-transaction fees, multi-currency settlement/withdrawal, refunds, reporting, and dispute fees. It states no region or merchant eligibility and supplies no numeric model rate; AUD and named currencies do not authorize transfer to sibling routes. It is not current independent NAB policy or a merchant contract. Raw: lines 1–9, 17–31, 34–55.
2. **Purpose/actions and limits:** Determine the account's assigned pricing model and understand fee/refund/dispute treatment. The per-transaction fee covers verifications, failures, and refunds; refund returns differ for blended versus IC+ (58–71). Major-currency settlement and conversion are at 34–50, funding at 74–76, reporting at 79–81, and chargeback/pre-arbitration triggers at 84–86. **Preserved ambiguities:** the $20 AUD charge is described both for “that day's disbursement” (48) and per transfer/withdrawal (76); chargeback fees are said both to be deducted on the last business day (31) and debited as applicable throughout the month (86). The snapshot does not resolve either tension.

## Close

- **Approval:** PASS for all eight fixed answers / four assigned pages; query-audit group B is approvable as evidence-grounded.
- **Blockers:** none. No material retrieval failure; no extra authority or repository transition required.
- **Analysis end (UTC):** 2026-10-04T15:00:28Z
- **Handoff (UTC):** 2026-10-04T15:01:17Z
