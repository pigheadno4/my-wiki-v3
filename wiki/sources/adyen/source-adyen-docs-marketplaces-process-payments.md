---
title: "Adyen Marketplaces: Process online payments"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/process-payments"
raw_files:
  - "adyen/docs/marketplaces/process-payments/2026-09-15.md"
tags: [adyen, marketplaces, platforms, online-payments, split-payments]
---

## Overview

This 2023-modified, 2026-09-15-captured **Marketplaces / Adyen for Platforms** guide describes processing **online** payments on behalf of marketplace users and splitting payment funds between user balance accounts and the marketplace’s **liable balance account**, with fees/costs deducted as needed. It outlines a pay-in → balance-account booking/settlement → scheduled payout flow; its USD amounts and final payout arrows are illustrations, not evidence of a completed payment, capture, settled transfer or bank receipt. [[adyen-platforms]]

## Requirements and routing

- The guide requires an **online payments integration and checkout UI**, Checkout API and Transfers API credentials, standard-webhook handling, and an account holder’s `receiveFromPlatformPayments` capability in a **valid** state. Its setup row offers Checkout **Sessions** (one `/sessions` server call) or **Advanced** (`/paymentMethods`, `/payments`, `/payments/details`), recommending Sessions for most integrations. See [[raw/adyen/docs/marketplaces/process-payments/2026-09-15|raw lines 21–35]]. Possessing credentials or requesting a capability does not establish a successful payment or enabled allocation.
- If the holder lacks a **valid** `receiveFromPlatformPayments` capability, the funds cannot be allocated to that user balance account and the **full amount is booked to the liable balance account** (raw lines 32–33). Separately, if neither a split configuration profile nor an API request supplies split instructions, the **whole transaction amount and fees** go to the liable balance account (raw lines 37–41). These are distinct fallback conditions.
- The guide says individual payment, capture and refund requests on behalf of users need correct split instructions for user and liable balances, unless a split configuration profile supplies them. See [[raw/adyen/docs/marketplaces/process-payments/2026-09-15|raw lines 37–43]]. This overview does not specify profile-versus-request precedence; follow the linked split guide for operation-level behavior.

## Money-flow and status boundary

- The example starts with a **USD 400.00** customer payment, illustrates **USD 396.00** to a user balance account, **USD 4.00** commission to the liable balance account, and **USD 2.00** fee deducted from liable funds. It then depicts scheduled payout of **USD 396.00** to the user’s transfer instrument and **USD 2.00** to the marketplace transfer instrument. These are example allocations across different stages, not transaction evidence. See [[raw/adyen/docs/marketplaces/process-payments/2026-09-15|raw lines 51–69]].
- The page says Adyen settles processed funds according to split instructions and that balance-account settlement models define how sales funds move toward users’ transfer instruments. Payment processing, split booking, settlement, payout instruction and beneficiary-bank receipt are separate states. See [[raw/adyen/docs/marketplaces/process-payments/2026-09-15|raw lines 45–49, 51–69]].
- Its requirements table says to handle **standard webhooks** and subscribe to **any** of Transfer or Transaction webhooks (raw lines 30–31), while the later Webhooks section says to subscribe to **Transfer and Transaction webhooks** to track events/status (raw line 73). The two phrasings differ on subscription coverage; this page does not resolve whether one feed suffices for every event of interest.

## Detail locators

- Online-payment scope, credentials, webhooks, valid-capability and flow prerequisites: [[raw/adyen/docs/marketplaces/process-payments/2026-09-15|raw lines 15–35]].
- Split-instruction and invalid/missing-instruction liable fallbacks: [[raw/adyen/docs/marketplaces/process-payments/2026-09-15|raw lines 32–43]].
- Settlement and illustrative USD booking-to-payout sequence: [[raw/adyen/docs/marketplaces/process-payments/2026-09-15|raw lines 45–69]].
- Webhook coverage wording and split-at-authorization/capture routes: [[raw/adyen/docs/marketplaces/process-payments/2026-09-15|raw lines 71–90]].

## Related

- [[adyen-platforms]] — modern Platforms payments, balances and payouts.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/process-payments/2026-09-15|Marketplace process payments (captured 2026-09-15)]]
