# Fixed retrieval checks — headless Adobe Commerce Express checkout

Q1. What integration does this guide cover, and what does its scope not prove?
- Expected: A separate express checkout module for headless Adobe Commerce, with Apple Pay, Google Pay and PayPal buttons on product, cart and mini-cart pages. It requires a headless plugin integration, selected-method Web Components and express setup. REST and GraphQL differ; GraphQL requires Adyen plugin v8.2.0+. This webpage does not pin the express module version, describe standard storefront checkout, establish merchant/method eligibility or prove live payment/order outcomes. Keep `adyen/module-payment@11.0.0` GitHub evidence separate.
- Raw locators: `raw/adyen/docs/plugins/adobe-commerce/headless-integration/express-checkout/2026-09-15.md:15-51`, `:543-549`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-plugins-adobe-commerce-headless-integration-express-checkout.md` → `[[adyen-magento2]]`.

Q2. What quote, shipping, PayPal and order steps carry material prerequisites or warnings?
- Expected: Cart/mini-cart uses a created quote; product detail initializes one and activates the cart before order placement. Existing real carts can be disabled, and abandoned manually initialized quotes need cancellation. Shipping changes must update quote and Component final amount; Apple/Google shopper details arrive after authorization, so temporary shipping values are updated later. PayPal lightbox needs initial paymentData and full action; shipping changes update the PayPal order with ISO currency/minor-unit amount and returned paymentData. Order placement uses REST payment-information or GraphQL placeAdyenOrder, then standard status check. Do not treat a Component event, sample request or success redirect as payment success; no special role/tokenization guarantee is stated.
- Raw locators: `raw/adyen/docs/plugins/adobe-commerce/headless-integration/express-checkout/2026-09-15.md:53-131`, `:151-187`, `:248-340`, `:349-448`, `:468-541`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-plugins-adobe-commerce-headless-integration-express-checkout.md` → `[[adyen-magento2]]`.
