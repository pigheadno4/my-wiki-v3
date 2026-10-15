---
title: "Pay by Link settings | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/pay-by-link/settings"
raw_files:
  - "adyen/docs/unified-commerce/pay-by-link/settings/2026-09-15.md"
tags: [adyen, pay-by-link, payment-links, customer-area, settings]
---

## Overview

This 2026-09-15 Adyen Docs snapshot covers **merchant Customer Area configuration** for Pay by Link creation options. The settings change which fields and choices are available when employees create payment links; this page does not itself create a link or establish a payment result. See [[adyen]] and [[adyen-unified-commerce]].

## Key takeaways

- Configuring these settings requires the **Merchant admin** or **Pay by Link Settings** user role. The guide uses the merchant account's **Payments > Payment link settings** page, with separate General and Creation tabs. These roles are Customer Area permissions; the page does not establish that a particular merchant account has Pay by Link enabled or which payment methods are available.
- General settings include a terms-and-conditions URL, email updates, credit-card settings, and whether to tokenize shopper payment details. The related [[source-adyen-docs-unified-commerce-pay-by-link]] overview gives the separate terms URL prerequisite before the first live payment link.
- Creation settings govern mandatory fields: available currencies, **link type** (how many times a link can be used to make a payment), and **link validity** (how long it can be used before expiry). The 48-hour/EUR/description/shopper-email configuration is an illustrative employee restriction, not a universal default. Configured expiry is not the same claim as the overview's three-month automatic link removal.
- Optional creation fields include store display, shopper reference, payment description, country/region, service date, and employee email delivery. The guide says to collect a shopper reference when tokenizing payment details for recurring payments; enabling the field does not itself prove consent or a token was created.
- Shopper-detail controls distinguish omission from asking the employee for mandatory or optional input, or asking the shopper for mandatory input on the payment link. The page says saved settings apply immediately, but it does not say previously created links are retroactively changed.

## Detail locators

- Purpose and required Customer Area roles: lines 15–31.
- Merchant-account navigation and General categories: `General settings`, lines 33–46.
- Creation controls and illustrative 48-hour example: `Creation settings`, lines 48–60.
- Currency, reuse count, and expiry meanings: `Mandatory fields`, lines 62–70.
- Optional fields, including shopper reference and email service: `Additional fields`, lines 72–83.
- Employee versus shopper personal-information choices and immediate save: `Shopper detail fields`, lines 85–96.

## Related

- [[adyen-unified-commerce]] — provider concept and Pay by Link routes.
- [[source-adyen-docs-unified-commerce-pay-by-link]] — overview with hosted page, live terms URL, and three-month removal boundary.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/pay-by-link/settings/2026-09-15|Pay by Link settings (2026-09-15)]]
