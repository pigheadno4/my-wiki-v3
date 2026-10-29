# C44 Billie via Klarna retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-klarna-billie`

Full pinned raw path: `raw/adyen/docs/payment-methods/klarna/billie/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-klarna-billie]]` → `[[raw/adyen/docs/payment-methods/klarna/billie/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What is Billie via Klarna, and what does this page establish about availability?

**Answer path:** The source entry and raw lines 23–29 identify a B2B deferred-payment invoice product offered through Klarna, with redirect/widget flows and a no-recurring matrix cell. `## Requirements` lines 31–36 requires a preexisting platform-specific Klarna integration and adding Billie in test Customer Area. \"International\" and \"Multiple\" in the matrix are not a per-country/currency eligibility list; the DE/EUR TEST example does not prove a merchant's live approval or settlement. The child page lists "Redirect, Inline widget" and its widget section requires `paymentMethod.subtype: sdk` (lines 815–843), but the linked Klarna overview Billie (B2B) row lists only "Redirect" (`raw/adyen/docs/payment-methods/klarna/2026-09-15.md:36`). Preserve this contradiction; do not infer current inline-widget availability for a merchant.

## Q2 — central capability, prerequisites and warnings

**Query:** Which method/company fields and flow/result boundaries matter when using Billie?

**Answer path:** Raw `## Required fields` lines 38–51 requires `paymentMethod.type: klarna_b2b`, `shopperName`, `company.name`, and `company.registrationNumber` except for DE/AT. `## Payment request and response` lines 53–782 provides versioned TEST requests; the curl JSON has a trailing comma at line 69. `### Redirect to Billie` lines 791–813 returns `RedirectShopper` plus a redirect action. `### Inline widget` lines 815–843 requires subtype `sdk` and returns `Pending`, `paymentData` and client-token data for later `/payments/details`; neither is final payment or capture proof. For flow selection, note the contradiction: the child matrix lists "Redirect, Inline widget" (lines 27–29), whereas the overview Billie row lists only "Redirect" (`raw/adyen/docs/payment-methods/klarna/2026-09-15.md:36`); current merchant widget availability is unresolved. `## Test and go live` lines 845–873 gives sandbox and child-guide routes without live enablement evidence.
