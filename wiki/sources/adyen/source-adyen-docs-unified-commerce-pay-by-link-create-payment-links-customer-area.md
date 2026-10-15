---
title: "Adyen payment links through Customer Area"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/pay-by-link/create-payment-links/customer-area"
raw_files:
  - "adyen/docs/unified-commerce/pay-by-link/create-payment-links/customer-area/2026-09-15.md"
tags: [adyen, unified-commerce, pay-by-link, customer-area, hosted-checkout]
---

## Overview

This 2026-09-15 Adyen webpage snapshot explains how an authorized merchant user creates a Pay by Link payment link in Customer Area, sends it to a shopper, and checks payment updates. Link creation in Customer Area requires no development work and supports most configured payment methods except buy now, pay later methods. The link takes the shopper to an Adyen-hosted payment form; creating, sending, or opening a link is not evidence of an authorized, captured, or finally successful payment. Optional server webhooks require development work.

> [!warning] Contradiction
> The supported-methods matrix captured 2026-09-15 marks Affirm, Alma, and Atome in the Customer Area column, while the Customer Area creation guide says these links exclude buy now, pay later methods. The difference is unresolved in these snapshots; verify applicable method, account, and product conditions before claiming Customer Area availability. [[source-adyen-docs-unified-commerce-pay-by-link-supported-payment-methods]]

## Key takeaways

- The user needs the **Pay by Link Interface** role to create links; **Change payment methods** is needed to customize shown methods, and **Merchant admin** or **Pay by Link Settings** is needed to customize themes. Before creation, the guide calls for Pay by Link terms, supported methods on the merchant account, and creation settings. See `Requirements` and `Customize the payment page`.
- In Customer Area, the user switches to a merchant account, opens **Payments > Payment links**, enters the configured form details, creates the link, and copies/sends it to the shopper. Fields and requiredness depend on creation settings. The form includes merchant reference, amount, shopper country/region, theme, optional/configured shopper reference and link type. The default is single use; the configured validity defaults to 24 hours and can be at most 70 days from link creation. If enabled, an email service can send the link or a successful-and-completed payment confirmation. See `1. Create a payment link` and `2. Send the payment link to your shopper`.
- After payment, Customer Area **Payments > Payment list** shows the result. Email updates can be configured, and optional webhooks can send updates to a server. In the link list, **Completed** means the payment was authorized; manual capture may still be required. **Payment pending** means the final result is unknown. Reusable links show only **Active** or **Expired**, never Completed. Link details are kept for three months, while the Customer Area link list displays links created within the last 90 days. See `3. Get updates about the payment` and `View payment links in your Customer Area`.
- Shopper reference must not contain personally identifiable information such as name or email. Shopper details are masked by default in the link list/details, and unmasking requires the **Merchant view PII** role. The guide requires shopper consent before tokenization; Customer Area link creation supports saving details for recurring payments, while saving for later one-off payments is directed to the Pay by Link API. See `1. Create a payment link`, `View payment links in your Customer Area`, and `Tokenize payment details`.
- The user can manually expire a link through Customer Area. Method visibility/order and payment-page theme have role and account-level settings. The `Test and go live` section lists testing, live-account configuration, live payment-method request, and live terms steps; the snapshot alone does not establish live readiness.

## Detail locators

- `Requirements`: account/user-role matrix, optional webhook setup, terms, supported-method and creation-settings links.
- `1. Create a payment link`: form field table, setting-dependent requiredness, single-use/reusable choice, 70-day maximum, and optional email-service actions.
- `View payment links in your Customer Area`: status definitions, reusable-link exception, 90-day list window, and masked shopper data.
- `Customize the payment page` and `Test and go live`: method ordering, themes, role gates, and live preparation.

## Related

- [[adyen]]
- [[adyen-unified-commerce]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/unified-commerce/pay-by-link/create-payment-links/customer-area/2026-09-15|Adyen Customer Area payment-link guide, 2026-09-15 snapshot]]
