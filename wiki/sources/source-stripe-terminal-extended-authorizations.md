---
title: "Stripe Terminal: Extended Authorizations"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/features/extended-authorizations"
raw_files:
  - "stripe-terminal-features-extended-authorizations-2026-11-07.md"
  - "stripe-terminal-extended-authorizations-2025.md"
tags: [stripe, stripe-terminal, extended-authorization, payment-intents, card-present]
---

## Summary

The May and November 2026 [[stripe]] Terminal guides describe extending the capture window for a successfully authorized, confirmed card-present PaymentIntent. They describe a typical baseline of 48 hours, or five days for Visa, and extensions of up to 30 days depending on card brand and merchant category. A hotel might authorize at check-in and capture at check-out.

## Request and Capture

- **Eligibility**. Visa, Mastercard, American Express, and Discover have the card-brand and merchant-category scopes below. Single-message methods such as Interac and eftpos are excluded. Stripe advises Connect users to set the MCC for each connected account to match its business.
- **Creation**. At PaymentIntent creation, set `payment_method_options.card_present.request_extended_authorization` to `true` and `capture_method` to `manual`. Confirmation attempts to initiate payment.
- **Deadline**. After confirmation, read `payment_method_details.card_present.capture_before` on the Charge for the payment's exact deadline. Network rules can change. If capture misses that deadline, the authorization expires, the hold is released, and the PaymentIntent transitions to `canceled`.

## SDK and Server Examples

> [!warning] iOS and Android SDK 6.0.0
> November documents that `captureMethod` defaults to automatic-asynchronous on iOS and Android SDK 6.0.0. SDK-side PaymentIntent creation must explicitly select manual capture for extended authorization. The retained Swift and Kotlin webpage examples omit this setter. The separately captured [[source-github-stripe-terminal-ios|iOS SDK]] and [[source-github-stripe-terminal-android|Android SDK]] examples explicitly select manual. The November React Native example adds `captureMethod: 'manual'` and gives no React Native version threshold.

The May Node create example passes `payment_method_types: ['card_present']`. The November cURL example sends `allowed_payment_method_types[]=card_present`. Both request extended authorization and manual capture. The [[stripe-payment-intents|PaymentIntent concept]] records the separate `stripe@23.0.0` request boundary. The webpage examples alone leave cross-version compatibility unresolved.

## Validity Window by Card Brand and MCC

| Card brand | Eligible merchant categories | Extended window |
| --- | --- | --- |
| Visa | Hotel, lodging, vehicle rental, and cruise line | Nominal 30 days. The exact window is 29 days 18 hours for clearing. |
| Visa | Aircraft, bicycle (including electric scooters), boat, clothing and costume, DVD and video, equipment and tool, furniture, motor home, and motorcycle rentals, plus trailer parks and campgrounds | Nominal 10 days. The exact window is 9 days 18 hours for clearing. |
| Mastercard (excludes Maestro and Cirrus) | All merchant categories | 30 days |
| American Express | Lodging and vehicle rental | 30 days, with capture due by the end of the customer's stay or rental |
| Discover | Airline, bus charter or tour, car rental, cruise line, local or suburban commuter, passenger transportation including ferries, hotel, lodging, and passenger railway | 30 days |

## See Also

- [[stripe-terminal-extended-authorizations]] — Terminal extended authorization concept
- [[stripe-terminal-incremental-authorizations]] — related capability for increasing the authorized amount

## Raw Sources

- [[raw/stripe-terminal-features-extended-authorizations-2026-11-07|2026-11-07 Terminal extended authorizations guide]]
- [[raw/stripe-terminal-extended-authorizations-2025|2026-05-01 Terminal extended authorizations guide]]
