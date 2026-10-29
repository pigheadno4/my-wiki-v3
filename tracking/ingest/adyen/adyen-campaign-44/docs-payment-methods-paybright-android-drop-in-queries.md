# C44 PayBright Android Drop-in retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-paybright-android-drop-in`

Full pinned raw path: `raw/adyen/docs/payment-methods/paybright/android-drop-in/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-paybright-android-drop-in]]` → `[[raw/adyen/docs/payment-methods/paybright/android-drop-in/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** Is this a current onboarding guide for a new PayBright Android merchant?

**Answer path:** The source entry and raw line 19 say Adyen will not accept new PayBright integrations following Affirm's acquisition. Raw `## Requirements` lines 29–34 scopes the guide to existing Advanced Android Drop-in. Later live-request instructions at lines 1000–1006 are subject to that restriction and provide no exception or approval proof. The Sessions `See also` URL at line 1010 is navigation, not a change to the Advanced requirement.

## Q2 — central capability, prerequisites and warnings

**Query:** How does PayBright Android Drop-in display, redirect and resolve a payment, and what capture/refund limits follow?

**Answer path:** Raw `## Show PayBright in your payment form` lines 36–46 uses CA/CAD `/paymentMethods` selection; `## Make a payment` lines 48–67 sends shopper/item data and Android return URL from server `/payments`. Versioned Java and Go `/payments` examples at lines 201 and 568 pass date-only `1970-07-10` to `OffsetDateTime.parse` and `time.Parse(time.RFC3339)` respectively, with Go discarding the parse error; they are not verified runnable birth-date code. Its redirect action is at lines 821–837. `## Handle the redirect` and `## Present the payment result` lines 839–891 use Drop-in return details and `/payments/details`, with AUTHORISATION webhook fallback when the shopper does not return. `## Capture the payment` lines 893–952 gives automatic default, first installment at capture, manual/delayed partial capture, remainder cancellation and Support-gated multiple capture. The `/capture` JSON at lines 925–948 has blank currency codes and a trailing comma at line 944, so it cannot be copied unchanged. `## Refunds and cancellations` lines 954–998 separates pre-capture cancellation from post-capture refund, but its labeled Checkout `/payments/{paymentPspReference}/refunds` route uses legacy-style `originalReference`/`modificationAmount`; the general [[source-adyen-docs-online-payments-refund]] guide's raw lines 56–76 requires the PSP reference in the path and `amount` in the body. Verify the endpoint-specific schema before adapting the captured PayBright sample; do not infer runtime success or failure. Result codes do not prove capture or settlement.
