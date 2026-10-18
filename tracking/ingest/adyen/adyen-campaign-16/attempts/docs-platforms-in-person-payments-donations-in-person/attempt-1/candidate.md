---
title: "Adyen for Platforms in-person donations using Giving"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments/donations-in-person"
raw_files:
  - "adyen/docs/platforms/in-person-payments/donations-in-person/2026-09-15.md"
tags: [adyen, platforms, giving, donations, in-person-payments]
---

## Overview

This 2026-09-15 Adyen for Platforms guide describes how platform-model users can offer an in-store shopper a Giving donation to a nonprofit after a donation campaign is configured. A chosen donation is a separate transaction from the purchase. The guide says Adyen covers donation fees and transfers the full donation to the nonprofit; split amounts and fees may be specified on the original sale, not on the donation. This is a terminal or standalone in-person route, separate from the Platforms API-only online Giving flow. The described flow and sample outcomes do not establish current eligibility, a specific donation's success, settlement or nonprofit bank receipt.

## Key takeaways

- Scope is Adyen for Platforms merchants with a platform model using Terminal API payment terminals or a standalone solution. The terminal needs software v1.109 or later, with some terminals/features needing v1.110 or later. A configured account-holder donation campaign must be started for the selected nonprofit; after the next scheduled terminal reboot, eligible payment flows can show its donation options. The guide points to separate supported-terminal, method, region/currency and campaign-management pages; those linked lists must be checked for a concrete rollout. A terminal does not prompt for a donation after a gift-card payment. The page does not establish Tap to Pay Mobile support or a merchant-of-record identity.
- Implement the Adyen Giving merchant webhook to obtain each donation's outcome. Its `DONATION` event has `success` and `originalReference`; the latter associates the donation with the original transaction. A webhook can support email or mobile notice if the platform or user has the shopper's contact details. The sample `success: true` notification is illustrative, not proof that a live donation or transfer completed.
- A shopper donation receipt from the full donation transaction response is available only for the two-step Terminal API interaction flow. Send a `TransactionStatusRequest` with receipt reprint, `DocumentQualifier` and a `MessageReference` for `SaleID: AdyenGiving`; using the original response's `adyen_giving_service_id` identifies a specific donation, while omitting `ServiceID` retrieves the latest donation on that terminal. `RepeatedMessageResponse.PaymentReceipt` supplies receipt data. A receipt-generation route is distinct from donation outcome confirmation; identify the intended donation before sending a shopper receipt.
- The campaign logo is an optional terminal standby-screen customization with model-specific dimensions and file-size limits. The guide does not use it as an eligibility or outcome signal.

## Detail locators

- `Requirements` — platform model, Terminal API/standalone scope, v1.109 and possible v1.110 gate, Giving merchant webhook, supported terminal/method/region/currency navigation, gift-card exception and campaign prerequisite (raw lines 27–37).
- `How it works` — nonprofit selection, account-holder campaign setup/start, optional logo, receipt or notification methods, and display after scheduled reboot (lines 39–55).
- `(Optional) Configure a logo` — terminal standby logo settings and model-specific file dimensions/size table (lines 57–79).
- `(Optional) Get the two-step donation response` — `TransactionStatusRequest` header, receipt-reprint qualifiers, `AdyenGiving` message reference, specific versus latest donation lookup, and `RepeatedMessageResponse.PaymentReceipt` (lines 82–186).
- `Giving webhook` — `DONATION`, `success`, `originalReference`, contact-detail condition and test-mode example (lines 266–305).

## Related

- Company: [[adyen]]
- Concepts: [[adyen-giving]], [[adyen-platforms]]
- Related sources: [[source-adyen-docs-platforms-donations-create-manage-campaigns]], [[source-adyen-docs-platforms-online-payments-donations-online]]

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/donations-in-person/2026-09-15|2026-09-15 Platforms in-person Giving guide]]
