# docs-payment-methods-mb-way retrieval checks

## Q1 — identity and scope
Query: What is MB WAY in this Adyen overview, and what can the snapshot establish?
Expected: A Portugal MB WAY/Multibanco solution overview captured 2026-09-15, with a PT/EUR direct-wallet capability row. Adyen integration does not require a separate Multibanco contract according to this source. The snapshot does not establish current merchant eligibility or a successful live transaction. Route: [[wiki/index]] → [[wiki/adyen-index]] → [[wiki/concepts/adyen-online-payments]] → [[wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way]] → [[raw/adyen/docs/payment-methods/mb-way/2026-09-15]]. Canonical stem: `/payment-methods/mb-way`. Verify raw lines 15–34.

## Q2 — shopper journey, capabilities and limit
Query: How do Web and App2App MB WAY journeys differ, and which capability/limit qualifications are stated?
Expected: Web shopper enters mobile number then confirms an app notification; mobile App2App redirects to MB WAY app for authorization with no phone-number entry. Matrix marks PT/EUR direct wallet, refunds/partial/multiple partial refunds available, recurring/separate/partial/multiple partial capture and chargebacks unavailable. Default EUR 1,000 daily cumulative user limit can be raised in MB WAY app to EUR 5,000; do not describe it as a per-transaction cap. Follow platform guides for implementation. Route: [[wiki/index]] → [[wiki/adyen-index]] → [[wiki/concepts/adyen-online-payments]] → [[wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way]] → [[raw/adyen/docs/payment-methods/mb-way/2026-09-15]]. Canonical stem: `/payment-methods/mb-way`. Verify raw lines 23–36 and route list lines 38–86.
