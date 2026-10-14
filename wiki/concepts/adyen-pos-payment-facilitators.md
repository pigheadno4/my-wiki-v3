---
title: "Adyen POS payment facilitators"
type: concept
category: technology
tags: [adyen, point-of-sale, payment-facilitators, sub-merchants, merchant-of-record]
---

## Definition

For an in-person transaction facilitated by a payment facilitator, Adyen's 2026-09-15 POS guide says the **sub-merchant is considered Merchant of Record** and card schemes require sub-merchant data with each transaction. Adyen adds some data automatically; the facilitator supplies the remainder. This statement is scoped to the guide's facilitated POS transactions and does not define a general platform contract or settlement model.

## Sub-merchant data paths

The guide covers Terminal API payment terminals and Mobile solutions, plus standalone terminals. A sub-merchant's store can hold `subMerchantData` through Management API. Standalone terminals must use this store route. Integrated terminals can use store configuration, per-request Terminal API fields, or both; request fields override store data when both are present. Request-supplied fields belong to Terminal API payment and referenced/unreferenced refund requests. Non-Terminal-API modifications use data from the initial payment. The source distinguishes store-configured `subMerchantData.id` (15-character maximum) from Terminal API `subMerchantId` (19-character maximum); details and requiredness stay in the source.

## Evidence boundary

This dated guide does not establish current scheme/account eligibility, successful transmission of a specific payload, authorization, capture or settlement. Its Terminal API response example does not echo the submitted sub-merchant data. It does not describe the facilitator's funds flow, payee account, split, payout or liability terms; those require separate contractual and provider evidence.

## Related

- [[adyen-pos-store-management]] — Management API store identity and configuration.
- [[adyen-terminal-api]] — Terminal API payment and refund messages.

## Sources

- [[source-adyen-docs-point-of-sale-payment-facilitators]] — 2026-09-15 Adyen POS payment-facilitator guide for Merchant-of-Record statement, store versus request-supplied sub-merchant data, precedence and scope.
