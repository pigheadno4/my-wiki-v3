---
title: "Adyen Adobe Commerce headless Express checkout"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/headless-integration/express-checkout"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/headless-integration/express-checkout/2026-09-15.md"
tags: [adyen, adobe-commerce, headless, express-checkout]
---

## Overview

This 2024-modified Adyen webpage explains the separate **Adobe Commerce express checkout module** for a **headless** Adobe Commerce integration. It describes Apple Pay, Google Pay and PayPal buttons on product detail, cart and mini-cart pages, using Adyen Web Components for the shopper UI and Adobe Commerce APIs for the quote, shipping, order and payment flow. It does not document standard storefront behavior or establish live merchant/payment-method eligibility. See [[adyen]] and [[adyen-magento2]]; the retained [[source-github-adyen-magento2]] is separate package- and commit-qualified plugin evidence.

## Key takeaways

- Prerequisites in this guide are a headless Adobe Commerce plugin integration, Web Components integrations for the chosen express methods, the express checkout module and the selected methods' express-checkout implementation. REST uses use-case-specific endpoints. GraphQL uses Adobe Commerce's `/graphql` endpoint and **requires Adyen plugin v8.2.0 or later**; this page does not pin the express module's own version.
- The quote lifecycle differs by surface. Cart/mini-cart has a cart-created quote; product detail requires manual quote initialization and later cart activation before placing the order. The initialization tables say passing an existing real cart ID disables that cart; the GraphQL activation mutation for logged-in users disables other real carts. The page says the plugin reactivates a disabled real cart after payment completes, while a shopper who abandons a product-detail flow needs the manually initialized quote cancelled through the documented event/API route. Treat cart IDs and quote activation/cancellation as stateful operations.
- Shipping-address and method changes update the Adobe Commerce quote; if shipping changes the total, update both the quote and payment Component to the final amount. The REST/GraphQL steps split logged-in and guest cart identifiers. Apple Pay and Google Pay supply shopper details only after authorization, so the guide uses temporary dummy values for shipping information and calls for updating it when details arrive.
- PayPal alone needs initial `paymentData` and the full `response.action` passed to the Component to open the lightbox. Shipping-address or method changes require updating the PayPal order; the documented updated amount has an ISO currency code and **minor-unit** value, and later updates reuse returned `paymentData`. For delivery-method lightboxes, the description is required by PayPal; the page recommends meaningful fallback logic when Title/Label are absent, without making its sample fallback order a universal rule.
- Order placement uses Adobe Commerce REST payment-information endpoints or GraphQL `placeAdyenOrder`, followed by the standard headless payment-status check. A Component event, example request body, success-page redirect instruction or local test instruction is not evidence of a completed live order, authorization, capture or settlement. This page states no special Customer Area role or tokenization contract.

## Detail locators

- Scope, methods, prerequisites and REST/GraphQL version boundary: pinned raw lines 15–51.
- Surface-specific quote setup, existing-cart disablement and IDs: pinned raw lines 53–131.
- Component shipping collection and PayPal lightbox initialization/action handoff: pinned raw lines 133–246.
- Shipping selection, temporary values and final amount synchronization: pinned raw lines 248–303.
- Cart activation, order submission and payment-outcome check: pinned raw lines 305–409.
- Abandoned quote cancellation and PayPal updateOrder with minor-unit amount/paymentData: pinned raw lines 411–541.
- Method-specific test routes: pinned raw lines 543–549.

## Related

- [[adyen-magento2]] — Adobe Commerce plugin concept; versioned repository evidence remains separately qualified.
- [[source-github-adyen-magento2]] — distinct `adyen/module-payment` snapshot, not a version pin for this express module.

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/headless-integration/express-checkout/2026-09-15|Adyen headless Express checkout guide, captured 2026-09-15]]
