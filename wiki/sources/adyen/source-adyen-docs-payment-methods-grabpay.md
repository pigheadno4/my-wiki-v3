---
title: "Adyen GrabPay overview"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/grabpay"
raw_files:
  - "adyen/docs/payment-methods/grabpay/2026-09-15.md"
tags: [adyen, grabpay, wallets, online-payments, southeast-asia]
---

## Overview

This [[adyen]] overview describes GrabPay's shopper redirect and Wallet/PayLater options, a Wallets capability matrix, and integration-channel routes. It is a historical documentation snapshot captured 2026-09-15, not evidence of current merchant availability or a completed payment. See [[adyen-online-payments]] and raw lines 23–76.

## Key takeaways

- The described website/app flow redirects the shopper to GrabPay login. The shopper authenticates with a phone number and a Grab-sent one-time password, selects an option and confirms. The page describes shopper action; it does not establish a merchant-side final outcome, capture or settlement from the redirect or confirmation alone. See raw line 25.
- The page distinguishes **Wallet** (full amount immediately) from **PayLater** (the next month or four equal installments over three months). It says Adyen offers GrabPay Wallet in Malaysia, Singapore and the Philippines, and PayLater only in Malaysia and Singapore. This overview does not give PayLater-specific integration, eligibility or settlement mechanics. See raw lines 27–32.
- The capability table is explicitly a **Wallets** row, with **Redirect**, countries **MY, PH, SG**, and currencies **MYR, PHP, SGD**. It marks recurring, separate captures, partial captures, multiple partial captures and chargebacks unavailable; refunds, partial refunds and multiple partial refunds available. The country and currency lists do not themselves establish every country–currency pairing or a merchant's enablement; table marks do not prove that a refund was executed. Do not apply the Wallets row mechanically to PayLater. See raw lines 34–36.
- For a refund, the page requires a `reference` of at most 32 characters, using only alphanumeric characters, dashes and underscores. This is a request-field condition, not refund success proof. See raw line 38.
- The page links Web, iOS, Android and API-only guides, as well as Pay by Link and in-person pages. These are navigation routes, not child SDK/API versions, implementation steps or current support guarantees. See raw lines 40–76.

## Detail locators

- **Shopper redirect and login:** raw lines 23–25.
- **Wallet versus PayLater and geographic scope:** raw lines 27–32.
- **Wallets capability matrix and refund reference:** raw lines 34–38.
- **Integration channel links:** raw lines 40–76.

## Related

- [[adyen-online-payments]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/grabpay/web/2026-09-15|GrabPay Web chooser]] — linked channel route; child behavior separate.
- [[raw/adyen/docs/payment-methods/grabpay/ios/2026-09-15|GrabPay iOS chooser]] — linked channel route; child behavior separate.
- [[raw/adyen/docs/payment-methods/grabpay/android/2026-09-15|GrabPay Android chooser]] — linked channel route; child behavior separate.
- [[raw/adyen/docs/payment-methods/grabpay/api-only/2026-09-15|GrabPay API-only guide]] — linked merchant-built-UI route; request and outcome details separate.

## Raw Sources

- [[raw/adyen/docs/payment-methods/grabpay/2026-09-15|GrabPay overview — captured 2026-09-15]]
