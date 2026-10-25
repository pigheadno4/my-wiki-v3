# PAYCO iOS Component retrieval checks

**Q1. What is the page for, and what cannot be inferred?** It adds PayCo to existing iOS Components Sessions or Advanced flows through `InstantPaymentComponent` and method type `kcp_payco`. It does not prove merchant eligibility, a final payment result or live readiness. Raw locators: `raw/adyen/docs/payment-methods/payco/ios-component/2026-09-15.md:17-23,25-69,78-121`. Canonical stem: `https://docs.adyen.com/payment-methods/payco/ios-component`.

**Q2. What capability, prerequisites, and warnings matter?** Sessions requires Checkout API v68+, redirect handling and PayCo in Customer Area; Advanced requires its iOS Components flow, redirect handling and setup. Neither adds method-specific ordinary request or configuration fields. The Advanced prerequisite label links to Drop-in although surrounding route links are Components. The page says there are no specific test credentials and points to Support; it supplies no final outcome or live activation procedure. Raw locators: `raw/adyen/docs/payment-methods/payco/ios-component/2026-09-15.md:29-76,82-127`. Canonical stem: `https://docs.adyen.com/payment-methods/payco/ios-component`.

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-payco-ios-component]] → [[raw/adyen/docs/payment-methods/payco/ios-component/2026-09-15]].
