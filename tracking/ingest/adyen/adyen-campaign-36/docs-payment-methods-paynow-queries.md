# docs-payment-methods-paynow — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is a PayNow overview and channel chooser for Adyen online payments (source-adyen-docs-payment-methods-paynow; raw lines 15–17, 31–61). The source describes the wider Singapore network's SGD account/e-wallet transfers and enrollment identifiers, but explicitly restricts **Adyen's PayNow integration to QR-code payments** (raw lines 23–25). Its SG/SGD capability row and links do not establish current merchant eligibility, non-QR Adyen support, implementation details or an actual payment/refund outcome (raw lines 27–29, 31–68).

Q2. What is the central capability, prerequisites and warning?

The captured matrix identifies real-time `qrCode` flow for **SG/SGD**, marks refunds and partial refunds with checks, and marks recurring, multiple partial refunds, separate/partial/multiple partial captures and chargebacks with x (raw lines 27–29). The page routes to Web, iOS, Android, React Native and Flutter child guides, but specifies no API/SDK version, QR expiry, scan-to-payment lifecycle, webhook semantics or merchant setup on this overview (raw lines 31–61). Read those child guides for implementation; the generic 3D Secure/Capture “See also” links do not supersede the PayNow row (raw lines 63–68).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paynow]] → [[raw/adyen/docs/payment-methods/paynow/2026-09-15]].
