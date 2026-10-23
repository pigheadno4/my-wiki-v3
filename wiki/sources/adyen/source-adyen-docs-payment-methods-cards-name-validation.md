---
title: "Adyen cardholder name validation"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/name-validation"
raw_files:
  - "adyen/docs/payment-methods/cards/name-validation/2026-09-15.md"
tags: [adyen, cards, name-validation, online-payments]
---

## Overview

This Adyen guide (last-modified metadata 2022-08-09; captured 2026-09-15) describes requesting a Visa or Mastercard cardholder-name comparison against issuer records during a **zero-value authorization** in the **Advanced online-payments flow**, Checkout API **v69 or later**. It presents fraud, KYC and payout reliability as potential uses, not proof of identity, regulatory compliance, a paid authorization, capture, settlement, or payout. A fee applies to each transaction where name validation is performed. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The stated requirements are an API key on a credential with the Checkout webservice role, issuer readiness, a zero-value authorization, and Visa or Mastercard payments in the United States, United Kingdom, or Europe. This dated scope does not establish current issuer or merchant eligibility. (raw lines 27–36)
- Send `/payments` with `amount.value: 0`, card details (`paymentMethod.type: scheme`), the cardholder name, and `paymentValidations.name.status: requested`. The guide specifies encrypted card fields, with unencrypted fields only for a fully PCI-compliant integration. `shopperName.firstName` and `lastName` are preferred; if omitted, Adyen falls back to `paymentMethod.holderName`, deriving the first name up to its first space or period. Apple Pay and Google Pay do not return the shopper name for this flow; the merchant must collect a checkout-entered name and pass it to `/payments`. (raw lines 47–54, 60–71, 490–494)
- The synchronous response's `paymentValidations.name.status` can be `performed`, `notPerformed`, or `notSupported`. The guide says unsupported issuer validation has no validation charge. Visa returns a raw status; Mastercard does not. A separate `result` supplies `match`, `partialMatch`, or `noMatch`; Visa has full/first/middle/last-name fields, Mastercard full name only. The schemes maintain the full-name combination logic, which Adyen says is opaque to it. A merchant must decide what to do with the result, for example separately authorize a payment or seek additional verification. (raw lines 49–56, 503–529)
- Example response `resultCode: Authorised` is paired with `amount.value: 0`; it illustrates the zero-value check, not movement of purchase or payout funds. Test names and the `NotPerformed`/`NotSupported` reference triggers are test fixtures, not live controls. (raw lines 537–590, 592–653)

## Example qualifications and conflicts

- The curl, Node, Python and Ruby examples include `paymentValidations.name.status: requested`; the Java, PHP, C#, Go and TypeScript request snippets omit `paymentValidations` even though the prose says to include it. Those snippets alone are incomplete for requesting validation. (raw lines 49, 69, 79–108, 142–151, 193–205, 249–260, 278–306, 345–356, 371–399, 413–440, 477–487)
- The Visa test row for “John Peter Smith” shows raw `fullName: 01` together with Adyen `fullName: partialMatch`, while the outcome mapping labels Visa raw `01` as `match`. Treat that row as an unresolved example inconsistency, not a dependable mapping rule. (raw lines 525–529, 618–624)
- The guide says additional `paymentValidations` types are being developed; this is future-facing guidance, not evidence that those types are supported in this snapshot. (raw line 56)

## Detail locators

- Requirements and flow: raw lines 27–56.
- Request fields, wallet-name handling and language examples: raw lines 60–489.
- Holder-name fallback and response status/outcomes: raw lines 490–529.
- Illustrative responses and test scenarios: raw lines 531–653.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/name-validation/2026-09-15|Adyen name validation guide, 2026-09-15 snapshot]]
