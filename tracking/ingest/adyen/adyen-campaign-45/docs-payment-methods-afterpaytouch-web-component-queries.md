# Afterpay Web Component worker retrieval queries

## Q1 — Purpose and scope

**Query:** What does this Afterpay Web Component page add, and which integration flows does it cover?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-afterpaytouch-web-component.md` → `raw/adyen/docs/payment-methods/afterpaytouch/web-component/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/afterpaytouch/web-component`; full pinned raw `raw/adyen/docs/payment-methods/afterpaytouch/web-component/2026-09-15.md`, `# Afterpay Web Component` lines 15–23, `## Sessions flow Component` lines 25–36, and `## Advanced flow Component` lines 813–821. It is an add-on to existing Web Components flows; it does not establish a complete standalone integration, current merchant eligibility or a successful payment.

## Q2 — Capability, prerequisites and warnings

**Query:** Which request fields, redirect handling and capture constraints are specified for Sessions versus Advanced Afterpay Web Components?

**Expected route:** Same root → provider → `adyen-online-payments` → source → pinned raw route.

**Evidence locator:** Same canonical stem and full pinned raw path; Sessions fields/requirements lines 29–53, Redirect setup lines 739–767, Advanced fields and response lines 849–863 and 1578–1592, `## Capture the payment` lines 771–790 and 1594–1613, `## Test and go live` lines 792–811 and 1615–1634. Preserve Sessions Checkout API v68+, both flows' redirect setup, required shopper/address/line-item fields, Advanced `afterpaytouch`, automatic/manual capture, 13-day production and one-day test deadlines, cancellation/refund, and the multiple-partial-capture exception. The redirect response is not final payment success; the sandbox country list is not live availability. The initialization snippet's unquoted `afterpaytouch` should not be copied as valid JavaScript.
