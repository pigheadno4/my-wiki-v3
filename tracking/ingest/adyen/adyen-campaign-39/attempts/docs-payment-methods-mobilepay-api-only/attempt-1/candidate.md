---
title: "Adyen MobilePay API-only integration guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mobilepay/api-only"
raw_files:
  - "adyen/docs/payment-methods/mobilepay/api-only/2026-09-15.md"
tags: [adyen, mobilepay, api-only, redirect, payouts]
---

## Overview

This 2026-09-15 Adyen guide adds MobilePay to an existing Web API-only Advanced integration. It covers method discovery, redirect handling, a payout-token extension, and qualified testing; the main integration guide owns the full checkout and result flow. This snapshot's discovery example and request snippets do not prove current availability, merchant enablement, a completed payment, or a payout. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Prerequisites are an existing Web API-only integration with handling for `action.type: redirect`, plus adding MobilePay in Customer Area. The custom payment form should include MobilePay in the method list; the form section says no shopper information needs to be collected there. For `/paymentMethods` discovery, the page lists `countryCode` DK or FI and `amount.currency` DKK or EUR, with FI/EUR in a TEST example and a MobilePay response example. The table does not establish every country/currency pairing or actual merchant availability.
- For an ordinary `/payments` call, the page says no MobilePay-specific parameters need to be added. Its "How it works" section nevertheless says the shopper enters details in the merchant-built form and the payment request includes additional item information, while the form section says no shopper data collection and the `/payments` section says no extra parameters. These statements should not be collapsed into a mandatory item-field or shopper-input rule. The "How it works" order-fulfillment step is an outline, not authorization or settlement evidence.
- For future payouts to MobilePay wallets, the page describes a separate `/payments` token-creation path: configure the recurring lifecycle webhook; send `telephoneNumber`, `shopperReference`, and `enablePayout: true`; on its webhook, save `storedPaymentMethodId` against `shopperReference`. A later POST `/transfers` puts that token in `counterparty.card.cardIdentification`. The payout feature is experimental and `/payments`-only. The example webhook uses `type: recurring.token.created` and `data.type: visa_mobilepay`; the example does not prove token creation or transfer success in an account.
- The page says ordinary MobilePay cannot be tested in the test environment and directs low-amount LIVE payments after a live Customer Area request, checking the `AUTHORISATION` webhook and live payment list. Separately, its experimental payout section gives a Vipps MobilePay test-app procedure to simulate a token-generating payment, process the recurring lifecycle webhook and send a Transfers API request. The page does not reconcile the payout test environment with its broad ordinary-payment test restriction; preserve both scopes. Authorization status is distinct from capture, settlement and payout completion.
- The `/payments` examples use empty currency and return URL placeholders. The curl example includes documentation hint markup as JSON property names and spells `enablePayOut`, while the token-creation prose says `enablePayout`; most language examples omit the shopper reference and payout flag. These snippets are not validated copy-ready requests. The TEST examples do not override the stated ordinary LIVE testing instruction.

## Detail locators

- Scope, prerequisites, form and conflicting how-it-works statements: pinned raw lines 15–42.
- `/paymentMethods` discovery table and FI/EUR TEST example: pinned raw lines 44–83.
- Ordinary `/payments` no-extra-parameter statement and incomplete request snippets: pinned raw lines 85–271.
- Token fields, recurring webhook example and later transfer: pinned raw lines 273–305.
- LIVE ordinary-payment testing and experimental payout test-app procedure: pinned raw lines 307–340.

## Related

- [[adyen-online-payments]] — main concept and Web API-only integration architecture
- [[source-adyen-docs-payment-methods-mobilepay]] — method overview; separate authority for method-level eligibility and payout scope

## Raw Sources

- [[raw/adyen/docs/payment-methods/mobilepay/api-only/2026-09-15|MobilePay API-only guide, 2026-09-15]]
