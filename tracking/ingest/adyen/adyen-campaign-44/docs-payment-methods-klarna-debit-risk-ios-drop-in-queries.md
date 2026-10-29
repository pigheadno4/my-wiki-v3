# Klarna Debit Risk iOS Drop-in retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-klarna-debit-risk-ios-drop-in`
**Full pinned raw:** `raw/adyen/docs/payment-methods/klarna-debit-risk/ios-drop-in/2026-09-15.md`
**Verified locators:** `# Klarna Debit Risk iOS Drop-in`, lines 15–23; `## Sessions flow Drop-in`, lines 25–46; `## Advanced flow Drop-in`, lines 1059–1081; `## Test and go live`, lines 1049–1057 and 2084–2092.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-klarna-debit-risk-ios-drop-in.md` → pinned raw.
**Answer boundary:** This is a Debit Risk add-on to existing iOS Drop-in Sessions or Advanced flow, separate from Klarna financing products. The guide does not prove current merchant eligibility, approved debit, capture or settlement; the overview covers country/currency and non-settlement risk.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** Sessions requirements lines 29–46, recurring premise/token table lines 50–79, token-created webhook line 429, shopper-absent rule lines 431–437, SEPA examples lines 443–768; Advanced redirect prerequisite lines 1063–1069, corresponding recurring/token evidence lines 1085–1114 and 1464–1497.
**Answer boundary:** Base Sessions needs Checkout API v68+ and Customer Area addition; Advanced needs existing redirect handling and Customer Area addition. Recurring is through SEPA Direct Debit, with explicit permission strongly recommended; follow-up token payments are shopper-absent Subscription or UnscheduledCardOnFile. The token-creation table calls for countryCode and Ecommerce, but its example omits countryCode and uses ContAuth (compare lines 71/76 with 89–104; repeated at 1106/1111 and 1125–1139). Several examples stringify storePaymentMethod. Verify the applicable API shape before reuse.
