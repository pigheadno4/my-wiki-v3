---
title: "Adyen Issuing: Wallet token authentication data"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/tokens-digital-wallet/authentication-data"
raw_files:
  - "adyen/docs/issuing/tokens-digital-wallet/authentication-data/2026-09-15.md"
tags: [adyen, issuing, digital-wallets, authentication, network-tokens]
---

## Overview

This Adyen Issuing guide, last modified 2023-03-17 and captured 2026-09-15, describes cardholder contact data used for OTP authentication when adding an Adyen-issued card to a digital wallet. The subject is wallet provisioning for an issued card, not a merchant checkout token or payment-authorization outcome. [[adyen-issuing]]

## Key takeaways

- The guide says Adyen must authenticate the cardholder before wallet use. Link a mobile phone number, email, or both to the card. During the described wallet-add flow, Adyen sends an OTP to the linked contact; if both are linked, the wallet prompts the cardholder to choose one. The page says the card is added after successful OTP validation. It does not provide a wallet-support list and directs readers to their Adyen contact for that list.
- Supply `card.authentication` on a card `paymentInstrument` create or update request. For phone, the example uses `number` and `type: mobile`; email is an alternative in the prose. The create example uses the Balance Platform API test host, a physical Mastercard card in NL and `status: inactive`; these are example values rather than universal requirements.
- The opening says to include authentication data when issuing a card, while later text explicitly allows adding the `authentication` object later or changing the phone number with PATCH `/paymentInstruments/{id}`. Read the creation-time wording together with the later update route. Neither sample establishes that a particular card was provisioned, that OTP delivery/validation succeeded, or that a transaction was authorized.

## Detail locators

- Purpose, OTP selection and wallet-support boundary: raw lines 19–31. Payload field description: raw line 35.
- Card-creation API and test-host example: raw lines 37–85; language-library examples and their shown versions: raw lines 87–601.
- Later authentication-data addition or phone change and PATCH example: raw lines 603–624; language-library examples: raw lines 626–898.

## Related

- [[adyen-issuing]] — Issuing card-program context.
- [[source-adyen-docs-issuing-network-tokens]] — Issuing network-token lifecycle overview.

## Raw Sources

- [[raw/adyen/docs/issuing/tokens-digital-wallet/authentication-data/2026-09-15|Wallet token authentication data — 2026-09-15 snapshot]]
