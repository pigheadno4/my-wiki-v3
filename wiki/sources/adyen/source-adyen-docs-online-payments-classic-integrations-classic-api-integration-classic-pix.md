---
title: "Adyen Pix for existing Classic API integrations"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/classic-pix"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/classic-pix/2026-09-15.md"
tags: [adyen, pix, classic-api, brazil, asynchronous-payments]
---

## Overview

This [[adyen]] guide explains how an existing older Classic API `/authorise` integration can offer Pix, Brazil's instant bank-transfer method. The shopper uses a bank or wallet app to scan or paste QR data; funds move from the shopper account to Adyen and are transferred daily to the merchant bank account. The page directs Checkout API integrations to a separate Pix guide. It says the merchant needs a local entity in Brazil, and its capability table specifies Brazil and BRL. Use [[adyen-online-payments]] for the provider integration context.

## Key takeaways

- Existing Classic merchants first add Pix in the test Customer Area, display it in the payment form, and collect shopper name and CPF/CNPJ. The server sends `/authorise` with `selectedBrand=pix` and the purchase amount; the guide says to send both `shopperName` and `socialSecurityNumber` so the shopper can identify the payment. The detailed request fields and example are at the raw locator below.
- The `/authorise` response gives `resultCode=Received`, a PSP reference, and QR contents/link in `additionalData`. Presenting a QR code means the payment is pending, not paid. After the shopper confirms in a participating bank or wallet app, the payment result arrives asynchronously in a webhook; the sample shows an `AUTHORISATION` event with `success=true`. Treat that sample as an example, not proof for another transaction.
- The payment's `additionalData.pix.expirationDate` defaults to 24 hours and has a five-day maximum in this snapshot. Pix checks funding, timing, fraud/regulatory, and account conditions before approval; Adyen or the acquirer can also reject for fraud concerns or Pix technical issues. The table says recurring, partial refunds, separate captures, and chargebacks are unavailable in this guide; full refunds are described within 90 days after payment.
- The shopper can change the paid amount in the bank or wallet app. Match webhook `additionalData.pix.originalAmountValue` against `amount.value`; on mismatch, Adyen recommends canceling and refunding. This reconciliation check matters even when the QR amount was generated correctly.
- Test Customer Area promotion of a pending offer to sale simulates payment and supports reconciliation testing. Live Pix acceptance requires a separate request in the live Customer Area; the test simulation does not establish live eligibility or a real paid outcome.

## Detail locators

- **Classic versus Checkout scope, Pix flow, money movement, country/currency and feature limits:** raw lines 15–44.
- **Test setup, shopper fields, Classic `/authorise` request and expiry:** raw lines 46–86; request example at lines 88–114.
- **Pending QR response and display fields:** raw lines 116–134 and `## Present the QR code or QR code data`, lines 151–159.
- **Approval checks, asynchronous webhook result, and amount reconciliation:** `### Transaction conditions` and `## Payment result`, lines 136–236.
- **Refund window, test promotion, and live request:** `## Refunds` and `## Test and go live`, lines 238–255.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/classic-pix/2026-09-15|Adyen Classic Pix guide — collected 2026-09-15]]
