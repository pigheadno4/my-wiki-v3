# Fixed queries — PayTo Web Component

## Q1 — purpose and scope

**Query:** What does the captured PayTo Web Component page cover, and what does it not prove?

**Expected answer:** The source at canonical stem /payment-methods/payto/web-component is a 2026-09-15-captured Adyen PayTo add-on for an existing Web Components integration. It distinguishes Sessions and Advanced flows, one-time and subscription agreement setup, and later charges. Its AU/AUD examples and test emails do not prove current merchant enablement, bank consent, final payment success, or live operation. Verify full pinned raw at raw/adyen/docs/payment-methods/payto/web-component/2026-09-15.md, # Web Component lines 15–23 and ## Test and go live lines 294–306, 643–655. Route: wiki/index.md → wiki/adyen-index.md → wiki/concepts/adyen-online-payments.md → wiki/sources/adyen/source-adyen-docs-payment-methods-payto-web-component.md.

## Q2 — prerequisites and lifecycle

**Query:** For PayTo Web Components, which flow handles subsequent subscriptions, what is required first, and how is agreement acceptance distinguished from payment finality?

**Expected answer:** Both flows require existing Web Components integration, Checkout API v70+, and PayTo enabled in Customer Area; Advanced also handles await actions (pinned raw ## Sessions flow Component lines 25–51; ## Advanced flow Component lines 308–317). Sessions /sessions covers one-time and subscription setup plus first payment; subsequent subscription payments are routed only to Advanced /payments or API-only (lines 48–51, 221–224). A shopper's bank authorizes or declines the agreement (lines 217–219, 533–535); subsequent stored-token payment is limited by the accepted agreement and uses ContAuth (lines 537–546). Pending/Received examples are not final outcome proof; AUTHORISATION can be authorized or rejected, and OFFER_CLOSED and REFUND_FAILED describe distinct failure stages (lines 414–429, 573–596, 611–641). The page's recurringDetailReference, pspReference and recurring.token.created storedPaymentMethodId descriptions differ, so do not equate them without flow-specific payload evidence. Verify canonical stem /payment-methods/payto/web-component and full pinned raw raw/adyen/docs/payment-methods/payto/web-component/2026-09-15.md. Route: wiki/index.md → wiki/adyen-index.md → wiki/concepts/adyen-online-payments.md → wiki/sources/adyen/source-adyen-docs-payment-methods-payto-web-component.md.
