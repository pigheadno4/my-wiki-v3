---
title: "Adyen Address Verification System (AVS) Checks"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/avs-checks"
raw_files:
  - "adyen/docs/risk-management/avs-checks/2026-09-15.md"
tags: [adyen, risk-management, avs, cards, fraud]
---

## Overview

This [[adyen]] guide explains Address Verification System (AVS) checks for card-not-present payments. With AVS enabled, the merchant sends the shopper's billing address in the authorization request and receives an Adyen AVS response indicating how it matches the card issuer's record. The guide covers an online-payments integration while also naming point-of-sale MOTO as a card-not-present use case; its separate POS response mapping is linked for that route. A match makes cardholder identity more likely in the guide's wording, not certain. See [[adyen-risk-management]].

## Key takeaways

- Setup requires an online-payments integration, enabled risk management, and a Customer Area user with a listed risk-settings role. AVS is supported for Visa, Mastercard, Discover, and American Express cards. The stated issuer support obligation applies in the US, Canada, UK, and Europe for Visa only; issuer support elsewhere is not assured. Merchant use of AVS is optional.
- AVS rules run **after authorization** and cannot be linked to Dynamic 3D Secure. The Adyen-provided AVS post-authorization rule can act on a mismatch; creating a custom post-authorization rule requires Protect premium features. Based on the result, the merchant can accept, make an exception, or cancel the transaction.
- For AVS, send the full `billingAddress` in the payment authorization request. The field table marks `country`, `city`, `street`, `houseNumberOrName`, and `postalCode` required when submitting that object; `stateOrProvince` is required for US or Canada shoppers. The page says an invalid country code rejects the transaction or request. Its special `ZZ` country guidance, address-line formatting, postal limits, and test fixtures are at the locators below.
- Adyen maps scheme/acquirer raw AVS responses to its own response codes; meanings and applicability vary by card scheme and acquirer. The test-environment Adyen AVS response is simulated because test payments do not pass through a live acquirer. The page says live responses include both raw acquirer and Adyen AVS codes, with Customer Area settings for exposing actual card/network response data.

## Detail locators

- **Requirements**, raw lines 22–33 — integration, risk setting, Customer Area roles, premium custom-rule boundary, post-authorization timing, card schemes, and issuer regions.
- **How does AVS work?**, raw lines 35–45 — billing-address comparison, mapped response, rule and merchant action, optional merchant use.
- **AVS in API requests**, raw lines 51–71 — `billingAddress` children and conditional requirements, invalid-country effect, `ZZ`, and non-guaranteed interchange note.
- **Test AVS results / Use AVS risk rules**, raw lines 73–86 — test-card setup, code selection, default post-authorization rule, and premium custom rule.
- **AVS responses and mapping**, raw lines 88–131 — Customer Area data settings, simulated versus live result, and scheme/acquirer-specific code table.

## Related

- [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/avs-checks/2026-09-15|Adyen AVS checks guide (2026-09-15 snapshot)]]
