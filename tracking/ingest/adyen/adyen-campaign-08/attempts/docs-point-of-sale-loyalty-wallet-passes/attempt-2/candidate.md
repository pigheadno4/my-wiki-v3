---
title: "Adyen POS Apple Wallet loyalty passes"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/loyalty/wallet-passes"
raw_files:
  - "adyen/docs/point-of-sale/loyalty/wallet-passes/2026-09-15.md"
tags: [adyen, point-of-sale, loyalty, apple-wallet, nfc, terminal-api]
---

## Overview

Adyen's wallet-passes guide describes using a merchant's NFC loyalty pass in Apple Wallet during a Terminal API payment-terminal transaction. The pass identifies the shopper's loyalty account for a merchant-run program; it is separate from the shopper's credit/debit card, payment token, PAN, and payment authorization. The guide gives post-payment recognition and pre-payment redeem flows, plus pass-server and Customer Area setup. This 2026-09-15 snapshot does not prove current wallet, terminal, merchant or regional eligibility, pass issuance, or a successful payment. [[adyen]] [[adyen-pos-loyalty]] [[adyen-terminal-api]]

## Key takeaways

- The page requires a Terminal API integration with a payment terminal. Its dated support table lists Verifone Engage software **1.64+** and Castles Android software **1.105+**, says **only Apple Wallet passes** are supported, and says an Apple agreement is needed to present Apple Wallet passes. It does not state Google Wallet pass support. See `## Requirements`.
- In the **payment flow**, the merchant makes a payment request and checks the payment response's `LoyaltyResult` for its pass's `LoyaltyAccountID.LoyaltyID`, then looks up and updates the shopper in its pass server/loyalty program, for example to accrue points. The loyalty ID is a pass identifier; the payment-flow response example separately shows card payment data but does not display an alias. The guide's following prose says to use the returned card alias as well as the loyalty ID, and a separate double-tap example shows an alias in `AdditionalResponse`. Absence of `LoyaltyResult` is described as no merchant pass in that wallet, not as a failed payment. See `### Tab: Payment flow` and `## Use the payment flow`.
- **Redeem flows** start with Terminal API card acquisition, check the merchant pass before payment, and can apply points or a discount to the final payment amount. In **single tap**, acquisition includes an amount and polls both pass and wallet payment-method details; the final amount must be no more than that acquisition amount, and Adyen Support must enable single tap to avoid another presentation when the amount changes. For an existing pass in **single tap**, the payment response does not repeat the loyalty details; in **double tap**, it includes `LoyaltyResult` with the same loyalty details. Double-tap acquisition can omit an unknown amount and polls pass details only; the shopper presents a payment method again and can use a different one. See `## Transaction flow options` and `## Use the redeem flow`.
- In redeem, retain `POIData.POITransactionID.TimeStamp` and `TransactionID` from the card-acquisition response and pass them as `PaymentData.CardAcquisitionReference` in the payment request. `LoyaltyAccount` in the acquisition response contains the pass ID and protocol brand, while the payment request carries the final amount. These are distinct from card account details and `PaymentInstrumentData`. See `### Get the shopper's pass details` and `### Case 1: The shopper has your pass`.
- The merchant or a third-party service runs a pass server with an enrollment/add-pass URL of at most **60 characters including scheme** and ties the pass to its POS and loyalty program. Pass creation yields a pass type ID and private key. Customer Area configuration selects the account level and flow, pass name/type ID, protocol, optional add-pass URL, and private-key slot. Adyen says its backend protects/encrypts the key; the terminal uses it to decrypt the NFC message and return the unique pass ID. These credentials and pass identifiers should not be treated as payment credentials. See `## Create NFC wallet passes` and `## Configure passes in your Customer Area`.
- The guide's on-the-spot enrollment and pass issue path is stated for **Verifone Engage** terminals. If the shopper lacks a pass, the merchant checks existing enrollment or asks whether to enroll; if the shopper declines, the flow ends with payment and no `LoyaltyResult`. For consented enrollment, the merchant creates a loyalty/pass-server profile and sends `LoyaltyData.LoyaltyAccountID` in the payment request. `LoyaltyID` is either only the pass number when the URL is configured in Customer Area or the URL plus pass number when it is not. Optional `SaleToAcquirerData.shopperReference` is case-sensitive, at least three characters, and must omit PII such as name/email. See `## Shopper enrollment` and `### Case 2: The shopper does not have your pass`.
- For an individual transaction, a Base64-encoded `VASModeOverride` JSON object in `SaleData.SaleToPOIData` can select pass-and-payment, pass-or-payment, pass-only or payment-only collection in a card-acquisition or payment request. The raw lists exact mode values; it does not make this override an account-wide configuration change. See `## Overriding the configured flow`.

## Detail locators

- `## Requirements` and `## Transaction flow options`: dated platform/model/software limits, Apple agreement, payment versus single-/double-tap behavior and amount/Support conditions.
- `## Create NFC wallet passes` and `## Configure passes in your Customer Area`: pass server, 60-character enrollment URL, Apple pass type ID, protocol and private-key setup.
- `## Use the payment flow`: Terminal API payment-response `LoyaltyResult` fields and merchant-side loyalty-account update.
- `## Use the redeem flow`: card-acquisition `LoyaltyAccount`, `POITransactionID` handoff, final `CardAcquisitionReference`, existing-pass and newly-issued-pass cases, `LoyaltyData` and shopper-reference privacy rule.
- `## Overriding the configured flow`: per-request `VASModeOverride` values and Base64 placement.

## Related

- [[adyen-pos-loyalty]] — in-person loyalty routes.
- [[adyen-terminal-api]] — Terminal API payment and card-acquisition messages.
- [[adyen-payment-terminals]] — physical terminal hardware context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/loyalty/wallet-passes/2026-09-15|Adyen wallet passes guide, fetched 2026-09-15]]
