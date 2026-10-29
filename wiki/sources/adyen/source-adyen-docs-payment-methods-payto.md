---
title: "Adyen PayTo payment method overview"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payto"
raw_files:
  - "adyen/docs/payment-methods/payto/2026-09-15.md"
tags: [adyen, payto, australia, mandate, account-to-account, online-payments]
---

## Overview

This 2026-09-15-captured Adyen overview describes **PayTo**, an Australian New Payments Platform account-to-account method for one-off and recurring bank-account payments. It explains merchant-method setup, bank agreement/mandate approval, initial and subsequent payment flows, limits, mandate management, refunds, and dispute handling. Bank approval of a mandate, an initial Pending response, and a successful payment webhook are distinct steps; this source is not evidence of current account eligibility or an executed transaction. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Method and captured capabilities:** The matrix labels PayTo **Real-time payments**, **Direct**, **AU**, and **AUD**. It checks recurring, full/partial/multiple partial refunds and chargebacks, while crossing separate/partial/multiple partial captures. These are captured overview indicators, not a merchant-specific entitlement or a full request contract. The chargeback check conflicts with the page's later assertion that no card-style chargeback process exists; keep both statements and verify the actual dispute route before relying on either label. [Raw: lines 23–27, 294–301]
- **Merchant setup and confirmation:** The page says to enable PayTo for a merchant account through Management API `POST /paymentMethodSettings` or live Customer Area. In the API table, `type: payto`, `payto.merchantName`, and `payto.payToPurpose` are required; `businessLineId` is required for a platform model and `storeIds` only for a specific store. Setup is asynchronous: configure a payment-method webhook and listen for `paymentMethod.created`. The prose says `status: success` means ready, but the shown success webhook has `enabled: false`. This is an unresolved example/prose conflict; do not infer the example demonstrates an enabled usable method. [Raw: lines 29–95]
- **First payment and one-off agreement:** The flow checks `/paymentMethods`, collects shopper account details and submits `/payments`; Adyen creates a bank agreement/mandate, the shopper sees Pending and approves in a banking app, and successful payment is confirmed by Adyen webhook. The first-payment diagram illustrates PayID or BSB, `shopperAccountIdentifier`, mandate and `storePaymentMethod: true`, an `await` action, then `AUTHORISATION` and `RECURRING_CONTRACT` webhooks. A separate one-off diagram shows a request without a mandate and an Adyen-generated single-use adhoc mandate with endDate day+1, exact amount and count 1. These are illustrated routes, not guarantees that every bank or shopper approves. [Raw: lines 97–185]
- **Stored payment visibility and models:** For later payments, use `shopperReference` in `/paymentMethods` and include the stored token in `/payments`. Show a token at shopper-initiated checkout only when `supportedRecurringProcessingModels` includes `CardOnFile`; tokens with only `Subscription` or `UnscheduledCardOnFile` belong to merchant-initiated use and should not be displayed there. The page maps Subscription to scheduled frequency, CardOnFile to customer-initiated adhoc, and UnscheduledCardOnFile to merchant-initiated adhoc. Subscription mandates require `count`; adhoc mandates may omit it. `recurringProcessingModel` must match `mandate.frequency`. The subsequent diagram again shows Pending before final `AUTHORISATION` webhook. [Raw: lines 187–249]
- **Variable bank limits:** The page says transaction limits differ among banks and account/verification policies. It gives examples of recurring limits often $1,000 per transaction but sometimes up to $25,000; one-off and CardOnFile examples often reach $25,000, while some banks set lower daily limits. These are source examples, not a universal cap or acceptance promise. [Raw: lines 253–261]
- **Mandate, refund and claim lifecycle:** A shopper can cancel a mandate in the banking app; the page says a `DISABLE_RECURRING` webhook follows and future payments fail. Terms cannot be modified in place; changing amount/frequency/end date requires cancelling and creating a new shopper-authorized mandate. Full and partial refunds are supported but cannot be reversed once processed. The disputes prose says there is no card-style chargeback clawback and describes a manual bank mandate-claim process, largely for missing authorization or payment under a suspended/cancelled mandate; this remains in tension with the matrix's chargeback check. [Raw: lines 263–301]
- **Notifications and errors:** Bank notifications can cover agreement creation, cancellation and payment; one-off agreement cancellation may generate an extra notification after it expires. For refusals, the page recommends enabling raw acquirer responses and links PayTo raw-response guidance. The Web, iOS, Android and API-only links are integration routes, not behavioral evidence for those child guides. [Raw: lines 303–339]

> [!WARNING] Setup and dispute statements conflict within the snapshot
> The setup text says `status: success` means PayTo is ready, yet its example has `enabled: false` (raw lines 70–85). The matrix checks chargebacks, yet later prose says no card-payment chargeback process exists and describes manual mandate claims (raw lines 25–27, 294–301). Preserve these as unresolved source tensions; neither warrants an enabled-account or dispute-entitlement conclusion.

## Detail locators

- Method identity, AU/AUD capability matrix and merchant setup: pinned raw lines 23–95.
- Initial, one-off and subsequent bank/mandate/payment sequences: pinned raw lines 97–228.
- Recurring model rules and variable bank limits: pinned raw lines 230–261.
- Cancellation, refunds, mandate claims, notifications and raw responses: pinned raw lines 263–313.
- Integration routes: pinned raw lines 315–339.

## Related

- [[adyen-online-payments]] — provider online-payment architecture and method routes.

## Raw Sources

- [[raw/adyen/docs/payment-methods/payto/2026-09-15|PayTo overview, captured 2026-09-15]]
