---
title: "Adyen Riverty Web Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/riverty/web-component"
raw_files:
  - "adyen/docs/payment-methods/riverty/web-component/2026-09-15.md"
tags: [adyen, riverty, web, components, redirect, invoice]
---

## Overview

This captured guide adds Riverty to existing Web Components Sessions and Advanced integrations. It covers request fields, optional profile tracking, Component setup, mandatory manual capture, partial modifications and checkout consent. It is a documentation snapshot, not proof of account eligibility, an executed payment or a completed capture/refund. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and pricing:** Sessions requires Web Components plus Checkout API v68 or later and redirect handling; Advanced requires Web Components plus additional `action.type=redirect` handling. Both require Riverty added in Customer Area. Activating Riverty defaults to standard pricing; contact an account manager before activation to verify Enterprise-pricing eligibility if relevant. The guide imports `Riverty` from Adyen Web and initializes `new Riverty(checkout, ...).mount(...)`; it says no additional Riverty configuration parameters are needed.
- **Request conditions:** Sessions `/sessions` marks shopper first/last name, telephone, email, billing and delivery addresses, and `lineItems` required; DOB and shopper IP are unmarked. The line item needs quantity, description and ID. For DACH operation, VAT must not be null for the stated VAT reclaim process. The guide says B2B is not supported and using a business name as shopper name may cause rejection. Advanced `/payments` instead marks telephone and delivery address unrequired; send delivery address only if address or delivery person differs, with delivery first/last name even if that person is the shopper. It warns a first-time shopper may be rejected when delivery and billing differ, and in that case says to send billing address only with delivery there. Advanced method types listed are `riverty`, `riverty_account`, `sepadirectdebit_riverty`, and `riverty_installments`, with `paymentMethod.subtype=redirect`; IBAN is required only for the Secure Direct Debit type. The overview limits split installments to DE/AT/NL, so the method-type list is not a country-wide entitlement.
- **Availability and profile tracking:** Advanced `/paymentMethods` lists country values AT, BE, DE, NL, CH and currency values EUR, CHF without explicit country/currency pairing. Profile tracking is **recommended** for Austria, Germany and Switzerland to improve acceptance, not required for all payments. Riverty's implementation support must provide `profileTrackingShopId` before implementing it. The script yields a profile ID, which the guide says to encrypt and send in `deviceFingerprint`.
- **Fingerprint field warning:** the Advanced flow prose says top-level `deviceFingerprint`, and its curl example shows that top-level field, while the parameter table labels it `paymentMethod.deviceFingerprint`. This snapshot does not resolve the field path; do not treat the example as an authoritative correction. Its `RedirectShopper` response is an additional redirect action, not completed payment.
- **Capture and modifications:** All Riverty payments need manual capture after shipment, even when other methods capture automatically. Capture triggers the shopper invoice and payment schedule; authorization expires if not captured within **30 days**, unless Support extends the period and confirms the change. Partial capture sends amount and matching `lineItems`; if sums differ, Adyen adds a dummy line item. Manually cancel remaining authorized balance. Multiple partial captures need Support setup and create an invoice per capture. Uncaptured payments can be cancelled; captured payments must be refunded to return funds. Partial refund uses amount, item data and `capturePspReference` to select the capture; absent that reference, the **last** capture is chosen automatically, possibly incorrectly. Full capture/refund does not need line items. The examples show `status=received`, which is receipt of a modification request, not final success.
- **Go-live and sample warnings:** Riverty requires Terms & Conditions and data-protection guidelines shown for shopper approval before payment. Several curl samples omit a shell continuation after `-X POST`; the partial-capture URL is printed `https: //...`, so these samples are not ready-to-run commands.

## Detail locators

- Raw `## Sessions flow Component`, lines 25–56: prerequisites, pricing, required fields, B2B/VAT conditions. Raw lines 130–162: import, configuration and Component.
- Raw `## Advanced flow Component`, lines 365–405: prerequisites, flow, profile tracking. Raw `## Get Riverty as an available payment method`, lines 409–437: value lists and `riverty` availability example. Raw `## Add additional parameters to your /payments request`, lines 488–527: method variants, delivery risk, IBAN and fingerprint path mismatch.
- Raw `## Capture the payment`, lines 166–270 and 603–707: manual capture, 30-day expiry, partial capture, cancellation and examples. Raw `## Refunds and cancellations`, lines 274–355 and 709–790: refund fields, capture selection and received response.
- Raw `### Go-live requirements`, lines 361–363 and 796–798: consent requirement. [[source-adyen-docs-payment-methods-riverty]]: product scope and split-installment geography.

## Related

- [[source-adyen-docs-payment-methods-riverty]] — method overview and product limits
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/riverty/web-component/2026-09-15|Riverty Web Component guide, captured 2026-09-15]]
