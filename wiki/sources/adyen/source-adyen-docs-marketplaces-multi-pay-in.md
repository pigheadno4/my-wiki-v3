---
title: "Adyen Marketplaces multi pay-in overview"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/multi-pay-in"
raw_files:
  - "adyen/docs/marketplaces/multi-pay-in/2026-09-15.md"
tags: [adyen, marketplaces, platforms, multi-pay-in, third-party-payments]
---

## Overview

This 2026-09-15 Marketplace-path guide introduces Adyen **multi pay-in**, an Adyen for Platforms online-payment service that brings Adyen-acquired and third-party pay-in-partner volume into one balance-platform environment. Partner-acquired proceeds first arrive in a distinct multi pay-in account and are then allocated to user and platform liable balance accounts. The page describes a service flow, not a particular partner's enablement, processed payment, booked allocation or payout. [[adyen]] [[adyen-multi-pay-in]] [[adyen-platforms]] (raw lines 15–19, 36–38)

## Key takeaways

- **Prerequisites and limit:** The guide requires an Adyen for Platforms online-payments integration, Checkout API and Transfers API credentials, a subscription to Transfer or Transaction webhooks, and account-holder `sendToBalanceAccount` and `receiveFromBalanceAccount` capabilities. Multi pay-in does **not** support separate authorization and capture. These are requirements stated in the snapshot, not proof of live capability or availability. (raw lines 21–34)
- **Source account and allocation deadline:** On a multi pay-in request, Adyen says it creates a multi pay-in account within the balance platform as the payout account for the pay-in partner, separately for each partner. The guide describes the account as legally held by Adyen solely for users' benefit pending allocation. It says the platform must allocate funds received there to balance accounts within **24 hours** for a stated regulatory reason; this is the provider's dated requirement, not an independent conclusion about current law or a particular fund's ownership. (raw lines 36–50)
- **Payment allocation and default:** After funds reach that source account, the platform uses Checkout `POST /payments` for **each payment** and sends split instructions to allocate to a user's balance account and its own liable account. If the request omits splits, the guide says **all funds and fees** book to the platform's liable balance account. The illustrated flow separately shows third-party processing fees deducted by the partner, user sale credits, platform commission, Adyen fees and later payouts; it is not a completed-ledger example. (raw lines 52–77)
- **Customer refunds are partner-side:** For a partial or full third-party-payment refund, the guide says the process can vary by partner. Its general sequence has the pay-in partner return funds to the user's customer and withhold that refund from a later payout batch; the platform submits a Checkout `/payments/{paymentPspReference}/refunds` request to debit specified balance accounts and send the offset back to the multi pay-in account. Adyen-side deduction or offset alone does not prove the partner paid the customer. (raw lines 79–90)
- **Illustrative currency discrepancy:** The refund diagram text deducts **EUR 98.00** from the user and **EUR 2.00** from the liable account, but says the full refund amount moved to the multi pay-in account is **USD 100.00**. The page provides no conversion explanation there; do not infer a validated currency-consistent refund or exchange rate from that example. (raw lines 91–104)

## Detail locators

- Raw lines 21–34: integration, API/webhook, capability and separate-authorization/capture requirements.
- Raw lines 36–50: partner payout to Adyen-held multi pay-in account, one account per partner and 24-hour allocation wording.
- Raw lines 52–77: Checkout allocation, omitted-split liable-account fallback and example money-flow legs; lines 79–104: partner refund, platform balance deduction/offset and currency-conflicting illustration.
- Raw lines 106–126: separate receive-funds, internal top-up, payment-allocation and refund guides; follow those pages for operation-specific request/event rules.

## Related

- [[adyen-multi-pay-in]] — focused service concept.
- [[source-adyen-docs-platforms-multi-pay-in]] — parallel Platforms-path overview.
- [[source-adyen-docs-marketplaces-multi-pay-in-payments]] — detailed allocation route.
- [[source-adyen-docs-marketplaces-multi-pay-in-refunds]] — detailed refund route.

## Raw Sources

- [[raw/adyen/docs/marketplaces/multi-pay-in/2026-09-15|Marketplace multi pay-in overview, captured 2026-09-15]]
