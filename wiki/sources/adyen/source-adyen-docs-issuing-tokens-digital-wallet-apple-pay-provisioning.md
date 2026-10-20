---
title: "Adyen Issuing Apple Pay in-app and Wallet provisioning"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/tokens-digital-wallet/apple-pay-provisioning"
raw_files:
  - "adyen/docs/issuing/tokens-digital-wallet/apple-pay-provisioning/2026-09-15.md"
tags: [adyen, issuing, apple-pay, digital-wallet, network-tokens]
---

## Overview

This Adyen Issuing-path guide, last modified 2023-03-28 and captured 2026-09-15, describes use of the Adyen Apple Pay Provisioning SDK to add an Adyen-issued payment card to Apple Wallet from an issuer's iOS app or directly from Apple Wallet. The page labels itself a work in progress and says APIs, documentation and processes may change (raw lines 15–23). [[adyen]] [[adyen-issuing]]

## Key takeaways

- For an issuer with an iOS app, the guide says to implement its in-app flow; it also says to support direct Apple Wallet provisioning through a Wallet extension and Authentication UI extension (raw lines 39–43, 135–182). These are instructions in this dated guide, not evidence of current Apple or Adyen program approval.
- The listed SDK environment is iOS target 13.4+, Xcode 14+ and Swift 5.7+. Before provisioning a specified `paymentInstrument`, the issuer's server GETs `/paymentInstruments/{id}/networkTokenActivationData` with the Bank Issuing PaymentInstrument Network Token Activation Data role, then sends returned `sdkInput` to the app (raw lines 31–37, 55–74). The cURL example uses the test Balance Platform host (raw lines 65–70).
- In-app, `ProvisioningService.canAddCard()` controls whether to show the button; `canAddCardDetails()` checks a particular device. On selection, `start()` invokes the SDK; its delegate sends `sdkOutput` to the back end, which POSTs it to Adyen and returns `sdkInput`. The completion delegate includes both a pass and an error, so invocation or callback alone does not prove that a card was added (raw lines 76–130).
- For direct Wallet provisioning, `ExtensionProvisioningService` reports status and card passes, generates the pass request, and uses a delegate/back-end POST of `sdkOutput` to return `sdkInput` for the network-token provisioning step. The raw specifies separate 100 ms status and 20 s pass-entry time limits with a fresh activation-data GET if exceeded (raw lines 197–270, 272–348, 350–447). It does not show a completed live provisioning outcome.

## Detail locators

- SDK download and installation pointer: raw lines 25–29. In-app sequence, eligibility, delegate and completion callback: raw lines 39–130.
- Wallet and Authentication UI extension classes, identifiers and protocol setup: raw lines 135–182. Multi-instrument `sdkInput`, status and unavailable-service fallback: raw lines 211–270.
- iPhone versus Watch pass-entry methods and card-art delegate: raw lines 272–348. Request generation and `provision(paymentInstrumentId, sdkOutput)` callback/POST: raw lines 350–447.

## Related

- [[adyen-issuing]] — issuing-program and `paymentInstrument` context.

## Raw Sources

- [[raw/adyen/docs/issuing/tokens-digital-wallet/apple-pay-provisioning/2026-09-15|Adyen Apple Pay provisioning guide, captured 2026-09-15]]
