---
title: "Adyen Network Tokenization"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/network-tokenization"
raw_files:
  - "adyen/docs/online-payments/network-tokenization/2026-09-15.md"
tags: [adyen, network-tokenization, cards, recurring-payments, co-badged-cards]
---

## Overview

This Adyen guide describes network tokenization for online card payments. It defines a card-network token as a 16-digit alternative to the PAN that is unique to a shopper-and-merchant combination, and distinguishes that network token from Adyen tokenization, in which Adyen returns a stored-payment token for later payments. The snapshot presents two implementation choices: Adyen manages the card-scheme network tokens and automatically substitutes them during payment processing, or the merchant supplies and manages existing network tokens.

## Key takeaways

- Network tokenization requires an online card-payment integration, the Checkout webservice and Merchant Recurring API credential roles, and Standard webhooks. The guide limits it to payments acquired by Adyen and says it cannot be used with external acquirer connections.
- In the Adyen-managed option, the merchant keeps its regular card-payment flow while Adyen swaps card details or a `storedPaymentMethodId` for a network token before forwarding the payment for authorization. This option can be combined with Adyen tokenization.
- In the merchant-managed option, the merchant sends a network token obtained from a card network. The guide says this option cannot be combined with Adyen tokenization. It requires an initial payment that returns a `networkTxReference`, which the merchant saves for subsequent payments.
- If an Adyen-managed network-token attempt fails, the guide says Adyen automatically retries without substituting a network token. Optional retry-attempt data can be enabled for the `/payments` response, and the same additional information is included in the `AUTHORISATION` webhook.
- Some US Visa, Mastercard, and Discover network tokens are co-badged with listed US Debit networks. Routing requires adding those US Debit payment methods to the merchant account; account routing priorities take precedence over Adyen's optimized routing, and an individual payment route can be selected with `paymentMethod.brand` after checking available brands through `/cardDetails`.

## Material qualifications and warnings

- Sharing network tokens across multiple merchant accounts requires contacting Adyen Support to enable the feature. Forwarding network tokens is separately routed to a PCI-compliant third party.
- The page claims benefits including maintained token validity after card-detail changes, higher authorization rates, and single-use cryptograms. These are documentation claims, not proof of current merchant eligibility, enablement, a particular transaction outcome, or a measured authorization-rate improvement.
- Under `## Let Adyen manage network tokens`, the opening sentence says, "To manage network tokens yourself" and directs the reader to Support for enablement. The heading and sentence disagree, so this snapshot does not unambiguously establish which option needs that enablement step.
- The merchant-managed section says subsequent payments use the saved `networkTxReference`. Its subscription/automatic-top-up table maps that value to `paymentMethod.networkPaymentReference`, but the subsequent one-off table omits that field while requiring cryptogram fields again. Confirm the current request contract rather than inferring the missing one-off field from the surrounding prose.

## Detail locators

- Definition and claimed benefits: opening text, raw lines 19-28.
- Integration, credential, webhook, and Adyen-acquirer requirements: `## Requirements`, raw lines 30-38.
- Difference from Adyen tokenization; Adyen-managed and merchant-managed compatibility boundaries: `## How it works`, raw lines 40-51.
- Cross-account sharing and forwarding navigation: `### Sharing network tokens` and `### Forward network tokens`, raw lines 53-59.
- US co-badged network-token routing, account setup, priorities, and per-payment route selection: `## Co-badged network tokens in the US`, raw lines 61-79.
- Adyen-managed flow, optional attempt/token data, automatic non-token retry, and `AUTHORISATION` webhook data: `## Let Adyen manage network tokens`, raw lines 81-192.
- Merchant-managed initial and subsequent payment flows, request fields, API-version qualification, `networkTxReference`, recurring-model matching, and the subsequent one-off field ambiguity: `## Manage network tokens yourself`, raw lines 194-429.
- Error-response shape and network-token error-code navigation: `## Troubleshooting`, raw lines 431-446.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-network-tokenization]]
- Distinct Adyen Vault-token concept: [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/online-payments/network-tokenization/2026-09-15|Adyen Network Tokenization documentation snapshot]] - complete collected guide covering network-token identity, implementation choices, requirements, routing, retry data, merchant-managed requests, and troubleshooting
