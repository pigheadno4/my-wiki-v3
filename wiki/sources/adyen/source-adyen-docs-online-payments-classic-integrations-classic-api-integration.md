---
title: "Adyen Classic API integration"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/2026-09-15.md"
tags: [adyen, online-payments, classic-api, card-payments, authorization]
---

## Overview

This 2026-09-15 Adyen webpage explains the legacy Classic API integration for accepting card payments on a merchant website or mobile application by collecting shoppers' raw card data and sending it in a server-side Payment API `/authorise` request. It says the endpoint is inactive and no longer supported for new integrations. Adyen directs new integrations to Checkout API and existing integrations to contact Adyen about migration. The raw-card route presumes PCI compliance at Level 1 or 2; the page recommends Client-Side Encryption if the merchant wants to reduce PCI requirements. This is documentation for an existing Classic flow, not evidence that an account can start a new integration.

## Key takeaways

- After test-account setup, the page tells the merchant to obtain an API key or basic-authentication credentials for calls to Adyen. From the merchant server, the example sends merchant account, reference, minor-unit amount, and card information to `/authorise`. See `Requirements` and `Authorise request` in the raw snapshot.
- For a request that passes validation, Adyen describes risk analysis followed, depending on the outcome, by an authorization attempt and payment response. The response includes a unique PSP reference usable later for cancel/refund. The shown `Authorised` result is an example, not a promised outcome. See `Authorise response`. Authorization and its response are separate from the capture and webhook steps linked under `Next steps`.
- For co-badged cards in regions covered by the cited regulatory guidance, the shopper must be able to select a preferred brand, and a selected brand must be used to complete the payment. The page instructs the merchant to present supported brands and pass a shopper-selected brand as `selectedBrand` in `/authorise`. See `Requirements for co-badged cards`.

## Detail locators

- `Authorise request`: test-card route, exact request example, minor-unit example, and link to the PaymentRequest API reference for further required fields.
- `Authorise response`: conditional processing sequence, sample PSP reference/result, and link to possible PaymentResult codes and fields.
- `Next steps`: capture approved authorization when necessary to complete payment, and set up webhooks for confirmation of authorization or failure.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-pci-dss-compliance]]
- [[adyen-payment-capture]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/2026-09-15|Adyen Classic API integration, 2026-09-15 snapshot]]
