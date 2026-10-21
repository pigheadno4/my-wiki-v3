---
title: "Adyen Marketplace-path multi pay-in allocation of third-party payments"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/multi-pay-in/payments"
raw_files:
  - "adyen/docs/marketplaces/multi-pay-in/payments/2026-09-15.md"
tags: [adyen, marketplaces, platforms, multi-pay-in, payments, split-payments, reconciliation]
---

## Overview

This Marketplace-path guide describes moving proceeds of payments **processed by third-party pay-in partners** from an Adyen-held multi pay-in balance account into user and platform balance accounts. It is an allocation of already collected partner proceeds, not an Adyen-acquired shopper payment or external bank payout. The page does not establish the partner's payment result, a particular seller or merchant of record, legal fund ownership, or any completed transfer. See [[adyen]] and [[adyen-platforms]]. Keep this pinned Marketplace URL distinct from the analogous Platforms-path source.

## Key takeaways

- The guide requires Checkout API credentials and subscription to Transfer and/or Transaction webhooks. It says each individual payment must be allocated to balance accounts within 24 hours of settlement in the multi pay-in account, framing that as a financial-regulation limitation. It provides no account-specific eligibility or region list.
- Submit POST `/payments` **for each individual third-party payment**, identifying the source multi pay-in account with `additionalData.BalancePlatform.balanceAccount`, setting `paymentMethod.type=multi_payin` and `additionalData.tokenDataType=MultiPayIn`, and supplying amount, merchant account, reference and `splits`. The request reference returns as `merchantReference`. The example is Checkout v72 TEST and returns `resultCode: Authorised`; that response alone does not establish balance booking, settlement or payout.
- A `BalanceAccount` split targets a user's or platform's `balanceAccountId`; `Commission` books platform commission to the liable balance account and does not require `account`. Fee-booking types include `AdyenMarkup`, `AdyenCommission`, `PaymentFee` and `AdyenFees`. The split reference is required for `BalanceAccount` and supports refunds and reconciliation. Distinguish the source multi pay-in account from destination user and platform liable accounts.
- Adyen recommends explicit fee split instructions. If no fee-booking instructions are included, **all transaction fees default to the platform's liable balance account**. Its USD 400 example allocates USD 396 to the user and USD 4 commission to the liable account, with associated fees also charged to liable; these are example amounts, not a fee rate or actual booked result.
- Track the separate legs: outgoing `internal/internalTransfer` debit of the multi pay-in account; incoming `platformPayment/capture/BalanceAccount` user credit; incoming `Commission` credit to liable; and outgoing fee capture from the chosen or default liable account. Transfer events move through `received` and `authorised` to `booked` for source debit or `captured` for credit/fee legs, followed by transaction webhooks. Check account, direction, type, references and transaction ID for each leg; one event does not prove all legs.
- Two TEST examples conflict internally: the user's captured-credit payload names balance-account suffix `00002`, while the request, earlier credit events and booked transaction name `00001`; the commission booked-transaction sample has amount `-400` despite the positive commission-credit narrative and transfer examples. Use actual event identifiers and signs for reconciliation rather than resolving these from sample data. The Balance Platform Accounting Report excerpt spans multi pay-in, liable and user accounts but is illustrative. Only after funds settle in the user's balance account does the page route to configured scheduled or on-demand payout; it shows no bank-credit outcome.

## Detail locators

- Multi pay-in purpose, prerequisites and 24-hour per-payment limitation: raw lines 15–36. Request fields, split targets/types, fee default and USD 400 example: lines 38–75. TEST Checkout v72 request, SDK-version examples, and `Authorised` response: lines 77–424.
- Webhook taxonomy and separate movement legs: lines 426–450; outgoing multi pay-in debit and booked transaction: 453–729; user credit: 731–1035; commission credit: 1037–1358; fee debit: 1360–1665. Example account-ID and commission-sign conflicts: lines 107–108, 765–769, 914–920, 1024–1029, and 1319–1355.
- Balance Platform Accounting Report excerpt and its status/reference/currency/date columns: lines 1667–1686. Post-settlement payout route and refund next-step link: lines 1688–1696.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — modern balance-platform and Marketplace model.
- [[source-adyen-docs-platforms-multi-pay-in-payments]] — separately pinned Platforms-path guide.
- [[source-adyen-docs-platforms-multi-pay-in]] — service overview and partner proceeds flow.
- [[source-adyen-docs-platforms-multi-pay-in-receive-funds]] — incoming partner payout into the multi pay-in account, before per-payment allocation.
- [[adyen-platform-internal-transfers]] — distinct internal balance-account transfer context.

## Related raw API references

- The raw page links to Checkout `/payments`, Transfer and Transaction webhook API references, Balance Platform Accounting Report and payout/refund guides; those linked pages need separate authority for detailed current behavior.

## Raw Sources

- [[raw/adyen/docs/marketplaces/multi-pay-in/payments/2026-09-15|Adyen Docs: Allocate third-party payments (2026-09-15 snapshot)]]
