---
title: "Adyen Salesforce Composable Storefront payment-method setup"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/composable-storefront/set-up-payment-methods"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/set-up-payment-methods/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, composable-storefront, payment-methods, express-checkout]
---

## Overview

Adyen's Salesforce **Composable Storefront** package guide configures payment methods for the Retail React App and Salesforce Business Manager. It is scoped to the Composable Storefront integration, not an SFRA cartridge. It describes setup and version-qualified UI paths; it does not establish that a method is currently eligible for a merchant or that a payment, order, refund or settlement completed.

## Key takeaways

- First add desired methods in Adyen Customer Area, then in Salesforce Business Manager enable `AdyenComponent` and `CREDIT_CARD` under **Merchant tools > Ordering > Payment Methods** and set **Payment Processor** to `Adyen_Component` for both. The guide says most enabled Customer Area methods then appear without extra configuration, while its named methods need additional steps. The page does not specify Business Manager or Customer Area user roles, API credentials or webhook roles; follow the linked installation/account guides for those prerequisites.
- **Apple Pay:** the package uses Adyen's Apple Pay certificate path. Web pages with Apple Pay require HTTPS and a valid SSL certificate; add Apple Pay in the test Customer Area with website URLs, and `http://localhost` cannot be used for testing. Live domain-association-variable instructions differ between package v1.2.0 and v2.0.0+. Apple Pay express is shown on cart/mini-cart in earlier tabs; the earlier blanket product-detail restriction is superseded by a separate **v4.2.0+** tab permitting product-detail launch with `isExpressPdp` and product `id`/`quantity`. That component does not handle product-detail quantity or variant changes. Use the matching version tab, not another tab's code.
- **Click to Pay** starts at package v4.1.0 and needs a Content Security Policy allowing listed Visa/Mastercard domains for script, image, frame and connect sources; merchant display name is optional. This is a browser-resource configuration step, not confirmation of method eligibility or transaction success.
- **Card installments** start at v4.3.0 for regular card payments, not Apple Pay, Google Pay or PayPal express. The test Customer Area must enable each merchant-account/card-scheme/country combination; otherwise `/payments` can reject even a valid storefront value. The guide restricts country/currency combinations to BR/BRL, MX/MXN and JP/JPY with different value rules. The PWA package gates the `installments` field server-side using the country in `locale` and removes it for other countries. The selected count is saved as `c_cardInstallments` on the Salesforce payment instrument after a successful payment and displayed on confirmation when present; configuration alone does not prove that outcome.
- **PayPal express** starts at v4.2.0 for cart or product detail; product detail requires product `id`, `price` and `quantity` to create a temporary basket and cannot handle quantity/variant changes there. An optional review page must retrieve payment data and call `submitPaymentDetails()` on shopper confirmation; the sample callbacks and redirect code are examples, not an order or payment guarantee.
- **Google Pay:** after test Customer Area enablement, the standard flow needs no additional page-specific setup; live setup requires a Google Merchant ID and registered storefront origins. Google Pay express starts at v4.3.0, requires applicable Salesforce shipping methods and a Google Pay-supported country from `locale.id`, and supports cart or product detail with different basket inputs. Its product-detail flow creates a temporary basket and does not handle quantity/variant changes; unsupported browsers/devices silently do not mount the component.

## Detail locators

- `## Requirements` / `## Enable Adyen as your payment processor` — Composable integration scope, Customer Area enablement first, Business Manager IDs and processor mapping.
- `## Apple Pay` through `### Go live` — HTTPS/certificate/test-domain conditions; Apple Pay express tabs for v1.2.0, v2.0.0+, v4.0.0+, v4.2.0+; product-detail limit and version-specific domain association.
- `## Click to Pay` — v4.1.0+ and CSP directives/domains.
- `## Credit card installments` — v4.3.0+, Customer Area gate, country/currency/value table, locale-based server filtering, configuration and conditional order-display field.
- `## PayPal express` — v4.2.0+, cart/PDP product inputs and optional review-page handoff.
- `## Google Pay` — standard test/live setup and v4.3.0+ express shipping, locale, basket, browser and product-detail conditions.

## Related

- Company: [[adyen]]
- Salesforce Commerce Cloud integration concept: [[adyen-salesforce-commerce-cloud]]

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/set-up-payment-methods/2026-09-15|2026-09-15 Composable Storefront payment-method setup]]
