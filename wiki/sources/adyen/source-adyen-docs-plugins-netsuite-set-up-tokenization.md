---
title: "Set up tokenization in NetSuite"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/netsuite/set-up-tokenization"
raw_files:
  - "adyen/docs/plugins/netsuite/set-up-tokenization/2026-09-15.md"
tags: [adyen, netsuite, tokenization, recurring-payments]
---

## Overview

Adyen's NetSuite tokenization setup guide (page metadata last modified 2023-11-20; captured 2026-09-15) describes the Payment Instruments prerequisite, Adyen payment-processing-profile fields, Customer Area additional data, token import, transaction overrides, and recurring-contract notifications. It describes configuration and token records for later recurring use; it does not establish a particular merchant's consent, token validity, payment authorization, or future payment success. Route through [[adyen-netsuite]] for the integration scope.

## Key takeaways

- NetSuite **Payment Instruments** must be enabled for tokenization; the page warns this changes its UI and fields. Pay by Link tokenization additionally requires its custom preferences. The guide then calls for editing the Adyen payment processing profile in NetSuite and selecting additional response data in the merchant-account Customer Area (raw lines 19–35, 61–78).
- The profile separates card tokenization from recurring model choice (`CardOnFile`, `UnscheduledCardOnFile`, or `Subscription`, sent with the payment request). Pay by Link tokenization is separately enabled, and making a PBL token the shopper's default works only when PBL tokenization is checked. Replacing card details with a token applies only when **PAYMENT CARD TOKENIZATION** is **Yes**. Card and general token payment-method instances are distinct (raw lines 36–59).
- Existing token import uses a Customer Record's **Financial → Payment Instruments** entry with **General Token** or **Payment Card Token**, a matching Adyen token payment method, token value, and Adyen token family. For a token created outside NetSuite, add the Adyen Shopper Reference; without it, NetSuite uses the shopper's internal ID, and the page warns Adyen invalidates an existing token that does not match that reference. The shopper reference is entered under the Customer Record's **Classification** tab (raw lines 80–105).
- For an individual credit-card transaction, **ADYEN PAYMENT CARD TOKENIZATION OVERRIDE** can choose Yes, No, or blank to inherit the profile setting; the recurring-processing-model override likewise inherits when blank. These are transaction-level options, not permission for an arbitrary future charge (raw lines 111–124).
- Token notifications require configured webhooks and the **RECURRING_CONTRACT** event code. Once enabled, the page says NetSuite creates general tokens for non-card payment details upon receiving that webhook; general-token notifications exclude card-token notifications. Card-token notifications are viewed on the transaction, while a token's creation can be checked in the Customer Record payment instrument (raw lines 126–156).
- The **Manually create tokens** section ends after an incomplete sentence, “To tokenize payment details of your shoppers after they have completed a payment”; it supplies no complete manual procedure. Do not infer steps or a resulting token from this fragment (raw lines 107–109).

## Detail locators

- Payment Instruments and Pay by Link prerequisites: raw lines 19–27.
- Profile card/PBL/recurring choices and payment-method instances: raw lines 29–59.
- Customer Area additional data selections: raw lines 61–78.
- Import fields and shopper-reference invalidation warning: raw lines 80–105.
- Incomplete manual-token section and transaction overrides: raw lines 107–124.
- Webhook setup, general-versus-card notification paths and token inspection: raw lines 126–156.

## Related

- [[adyen-netsuite]] — NetSuite integration concept and source route.
- [[adyen]] — Adyen provider page.

## Raw Sources

- [[raw/adyen/docs/plugins/netsuite/set-up-tokenization/2026-09-15|NetSuite tokenization setup, captured 2026-09-15]]
