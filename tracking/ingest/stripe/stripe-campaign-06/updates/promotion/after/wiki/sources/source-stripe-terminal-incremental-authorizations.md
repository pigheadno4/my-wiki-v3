---
title: "Stripe Terminal: Incremental Authorizations"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/features/incremental-authorizations"
raw_files:
  - "stripe-terminal-features-incremental-authorizations-2026-11-07.md"
  - "stripe-terminal-incremental-authorizations-2025.md"
tags: [stripe, stripe-terminal, incremental-authorization, payment-intents, card-present]
---

## Summary

The May 1 and November 7, 2026 guides describe raising the authorized amount on a confirmed, uncaptured Terminal PaymentIntent. The POS and reader must be fully online. Depending on the issuing bank, the cardholder may see the original pending hold rise or see each increment as a separate pending authorization. The captured total appears as one entry.

## Eligibility

- Both captures list Visa, Mastercard and American Express for all merchant categories and Discover for restricted categories. See the dated Availability table for the full Discover list.
- November adds **China UnionPay private preview** for car rental and automobile rental agencies, hotels, motels, resorts and steamship or cruise lines in select Asia-Pacific and European markets. The November raw lists the countries at lines 34–36 and directs merchants to Stripe Sales to request access. Account eligibility remains subject to access and transaction criteria.
- The maximum is ten incremental authorization attempts per payment, including declines.

## Setup and Confirmation

Create a card-present PaymentIntent with `capture_method` set to `manual` and `payment_method_options.card_present.request_incremental_authorization_support` set to `true`. The reader shows **Pre-authorization** in place of **Total**. Confirm through the client and check `payment_method_details.card_present.incremental_authorization_supported` on the latest Charge after successful confirmation. To adjust the amount before confirmation, use the PaymentIntent update method.

**SDK capture default.** The November guide says to set manual capture explicitly when creating a PaymentIntent with iOS or Android SDK 6.0.0 onward or React Native SDK `0.0.1-beta.34` onward because the capture method defaults to automatic-asynchronous. Its Swift and Kotlin creation snippets and Swift confirmation setup omit the manual setting. In React Native the creation and confirmation examples specify `captureMethod: 'manual'`, while the confirmation example omits the incremental authorization request flag. Use the documented creation prerequisites. See [[source-stripe-terminal-sdk-migration-guide]], [[source-github-stripe-terminal-ios]] and [[source-github-stripe-terminal-android]] for versioned evidence.

**Dated request examples.** The May server Node example uses `payment_method_types: ['card_present']`. November’s cURL create request uses `allowed_payment_method_types[]=card_present`. The separate November Create PaymentIntent reference describes `allowed_payment_method_types` as an optional input and `payment_method_types` as the returned compatible methods. For exact Node request-version distinctions, see [[stripe-payment-intents]]. The guide examples leave cross-version request compatibility unresolved.

**Dated React Native confirmation examples.** May passes the PaymentIntent ID to collect and uses ID-based `processPayment`. November passes the PaymentIntent object to collect and the collected intent to `confirmPaymentIntent`. See the respective raw sections. The snippets illustrate those captures’ calls.

## Increment and Capture on the Server

- Call `increment_authorization` with the higher **total** amount. Stripe attempts to authorize the **difference** from the currently authorized total. On success, the PaymentIntent records the updated amount. On `card_declined`, the previous authorization stays available for capture and companion field updates such as `application_fee_amount` are unsaved.
- Capture with `amount_to_capture` above the current authorization normally attempts an automatic increment. If that increment succeeds, the captured PaymentIntent reflects the updated total. If it is declined, Stripe returns `card_declined`, keeps the previous amount authorized, and discards accompanying field changes. Check for possible capture failures.
- **On-receipt tipping exception.** For eligible on-receipt overcapture, the above-authorization capture skips the automatic increment. The companion November guide scopes eligibility to US businesses with eligible card brands and merchant categories, requires checking `latest_charge` for `payment_method_details.card_present.overcapture_supported`, and documents an excess limit of 50% of the authorized amount or USD 50, whichever is greater. The blanket capture-success wording in the incremental guides belongs to the no-auto-increment exception, with payment eligibility, limits and failure checks still relevant. See [[source-stripe-terminal-on-receipt-tipping]].

## See Also

- [[stripe]] — company page
- [[stripe-terminal-incremental-authorizations]] — Terminal concept
- [[stripe-terminal-tipping]] — on-receipt tipping and overcapture
- [[stripe-incremental-authorization]] — separate non-Terminal flow

## Raw Sources

- [[raw/stripe-terminal-features-incremental-authorizations-2026-11-07|November 7, 2026 Terminal Incremental Authorizations guide]]
- [[stripe-terminal-incremental-authorizations-2025]] — May 1, 2026 verbatim webpage
