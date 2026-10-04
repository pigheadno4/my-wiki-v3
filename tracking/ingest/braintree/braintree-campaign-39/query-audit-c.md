# Braintree Campaign 39 query audit — group C

## Identity and shared checks

- Provider: `braintree`; campaign: `braintree-campaign-39`; manifest: `/Users/tengtao/Development/wiki-v2/tracking/ingest/braintree/braintree-campaign-39/manifest.json`.
- Assigned positions/jobs only: 9 `articles-risk-and-security-compliance-ecommerce-website-requirements`; 10 `articles-risk-and-security-chargebacks-retrievals-overview`; 11 `articles-risk-and-security-chargebacks-retrievals-reducing-chargebacks`; 12 `articles-risk-and-security-card-brand-monitoring-programs-overview`.
- PASS — provider/job/object/action: all four manifest jobs resolve to the exact expected source target, canonical URL, raw slug, and subject action (merchant disclosure requirements; chargeback/retrieval/pre-arbitration lifecycle; chargeback-reduction practices; card-brand monitoring-program overview).
- PASS — immutable evidence: the four local SHA-256 values match the manifest exactly: `f436f0d1adbf81ccced29cefbcc35f6950da4f916c65035da823901c66e41f14`, `3e15b55e7063da43b59687d5efbcbff3f8f3f8fd389cea11d2b924b4edea0390`, `8303c8be8650884025249cccc4e2fdb73a39abc2d40a897d51d027b35922e60f`, and `bfa09058bfccbba1c91ac37a966467bc16704efed173afa97ab2a4a69b365535`.
- PASS — retrieval/read: root `[[index]]` → `[[braintree-index]]` → existing main concept → promoted source → pinned raw works for every page. The four source pages and four pinned raws were read completely. Aggregate source catalogs remain deferred as instructed.
- PASS — bounded gap sweep: exact canonical URLs, topic filenames, related-raw navigation, and distinctive claims were searched. The assigned evidence answers all eight fixed questions; no extra raw was used as factual authority. These exact-page answers do not resolve or negate wider corpus conflicts.
- Analysis end UTC: `2026-10-04T15:01:58Z`.
- Handoff UTC: `2026-10-04T15:02:46Z`.

## Position 9 — Ecommerce Website Requirements

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-articles-risk-and-security-compliance-ecommerce-website-requirements]]` → `[[raw/braintree/articles/risk-and-security/compliance/ecommerce-website-requirements-2026-09-16]]`.

1. **PASS — scope.** This is Braintree-hosted merchant guidance for disclosures across websites, apps, invoices, and contracts, with requirements expressly varying by operating location, accepted card brands, and business model; it separately covers accepting PayPal through Braintree. It names no single jurisdiction or merchant-account/processor variant. Page metadata is created/updated 2025-04-01; the snapshot was fetched 2026-09-16. Raw locators: lines 1–10, 14–16, 86–92.
2. **PASS — purpose/actions and limits.** Merchants are directed to disclose contact information, pre-payment pricing, refund/cancellation policy (including a no-refund policy), privacy-data handling, and physical-goods delivery timing; mobile-only merchants must include or link these requirements, and PayPal-via-Braintree setup requires privacy-policy and terms links in the Control Panel. Custom-contract, members-only, nonprofit, and mobile qualifications are preserved; the terms-topic list is illustrative, not declared universally mandatory. Raw locators: lines 19–28, 31–39, 42–64, 67–83, 86–110.

## Position 10 — Chargebacks, Retrievals, and Pre-Arbitrations Overview

Route: `[[index]]` → `[[braintree-index]]` → `[[disputes]]` → `[[source-braintree-articles-risk-and-security-chargebacks-retrievals-overview]]` → `[[raw/braintree/articles/risk-and-security/chargebacks-retrievals/overview-2026-09-16]]`.

1. **PASS — scope.** This is a general Braintree payment-processor overview, not a bank-specific or universal card-network rule. Banking partner and merchant-account type qualify fund handling and fees. A body note is narrowly scoped to U.S. flat-rate merchants and says “as of August 27, 2025”; preserve the raw inconsistency that page metadata says updated 2025-08-19. The snapshot was fetched 2026-09-16. Raw locators: lines 1–10, 29–37, 45–47, 62–63.
2. **PASS — purpose/actions and limits.** The page defines chargeback, dispute, retrieval, and pre-arbitration; routes merchants through notification and accept/dispute choices; assigns case management to the merchant while Braintree facilitates; and routes exact fund/fee handling to bank-specific articles. Retrievals move no money and carry no fee in this article. Pre-arbitrations may be disputed but are said to rarely succeed without new, compelling evidence; the dated policy says Braintree auto-accepts under USD 1,000 for U.S. flat-rate merchants and permits representation above USD 1,000. Raw locators: lines 18–24, 27–47, 50–63.

## Position 11 — Reducing Chargebacks

Route: `[[index]]` → `[[braintree-index]]` → `[[disputes]]` → `[[source-braintree-articles-risk-and-security-chargebacks-retrievals-reducing-chargebacks]]` → `[[raw/braintree/articles/risk-and-security/chargebacks-retrievals/reducing-chargebacks-2026-09-16]]`.

1. **PASS — scope.** This is general Braintree merchant guidance, not a specific account, processor, payment method, region, jurisdiction, or current bank/card-network rule. Page metadata is created/updated 2025-04-02; the snapshot was fetched 2026-09-16. Raw locators: lines 1–10, 14–16.
2. **PASS — purpose/actions and limits.** The stated purpose is reducing frequency, not eliminating chargebacks. Actions cover collecting billing address/postal code/CVV; clear terms, contact details, and shipping timelines; opt-out and transparent pricing for trial-to-paid subscriptions; easy refunds with customer follow-up; recognizable descriptors; internal monitoring; CAPTCHA against carding; and routing to fraud tools. The page recommends not collecting payment information for a free trial rather than declaring a universal prohibition. Raw locators: lines 16, 19–41, 44–72.

## Position 12 — Card Brand Monitoring Programs Overview

Route: `[[index]]` → `[[braintree-index]]` → `[[disputes]]` → `[[source-braintree-articles-risk-and-security-card-brand-monitoring-programs-overview]]` → `[[raw/braintree/articles/risk-and-security/card-brand-monitoring-programs/overview-2026-09-16]]`.

1. **PASS — scope.** This is Braintree-hosted Visa/Mastercard chargeback- and fraud-monitoring guidance, with page metadata created/updated 2025-04-01 and snapshot fetch date 2026-09-16. Braintree notification is promised only when the merchant account is provided through Braintree. It is not current independent card-brand authority, enrollment proof, or transferable behavior for differently provided accounts. Raw locators: lines 1–10, 18–20, 42–46.
2. **PASS — purpose/actions and limits.** The page explains calendar-month threshold entry and card-brand-qualified exit; defines fraud ratio as monthly fraud amount divided by monthly settled-sales amount and dispute ratio as monthly opened-chargeback count divided by monthly settled-sales count; and excludes pre-arbitrations/second chargebacks and retrievals from that dispute-ratio calculation. It supplies no numeric thresholds and routes exact Visa/Mastercard program values to their separate articles. Merchants should minimize chargebacks/fraud and, for Braintree-provided accounts, use the Disputes-team notification/resource route. Raw locators: lines 16–18, 20–39, 42–46.

## Result, blockers, and approval

- Overall: **PASS — 8/8 fixed questions answered with raw locators; 4/4 routes and hashes verified.**
- Blockers: none.
- Approval: none required for this read-only audit handoff. Any repository correction, catalog transition, campaign close, commit, or push remains coordinator-owned and was not performed.
