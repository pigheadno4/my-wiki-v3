---
title: "Adyen Payout Service account structure and fund flow"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/account-structure-resources"
raw_files:
  - "adyen/docs/payouts/payout-service/account-structure-resources/2026-09-15.md"
tags: [adyen, payouts, payout-service, account-structure, balance-platform]
---

## Overview

This 2026-09-15 [[adyen]] Payout Service guide explains **payouts combined with payment processing for the merchant's own business**. Adyen company and merchant accounts handle that business's payments; a linked balance platform manages the merchant's balance account and related account-holder, legal-entity and verified bank-account transfer-instrument resources. In the guide's example, shopper payments process through one of the business's merchant accounts, settle into its balance account, and remain there until a later payout request to its own instrument or a third-party bank account/card. This is an illustrative merchant funding model, not a general allocation of platform-user or liable balances in [[adyen-platforms]]. [[adyen-payouts]]

## Key takeaways

- The company account represents the business entity and contains one or more merchant accounts; merchant accounts process its payments and configure methods/currencies. For payouts with payments, the merchant account links to a balance platform. The Management API is named for managing company/merchant resources. See raw lines 25–42.
- Adyen says its contact sets up balance-platform resources: a balance account holding funds available for payouts, an account holder specifying permitted actions and linked to **one legal entity**, and a transfer instrument representing **the business's verified bank account**. The contact also sets up the legal entity with business information for verification. The text allows multiple balance accounts, although it says one suffices for most use cases. See raw lines 44–56.
- The OnlineStoreLLC example has one company account, three country-organized merchant accounts, one EU balance platform with one account holder and balance account, plus a legal entity with a verified bank-account instrument. These counts and regions are examples, not required topology or proof of live eligibility. See raw lines 58–81.
- In that example, a shopper payment is processed in a merchant account, then **settled** into the business's balance account. Only **after settlement** does the page route to `POST /transfers` for payout to its transfer instrument or to a third-party bank account or card. Requesting a transfer is distinct from its booking, beneficiary credit or bank/card receipt. See raw lines 83–103.

## Detail locators

- **Company/merchant accounts and linked balance platform:** raw lines 25–46.
- **Balance account, account holder, instrument and legal entity:** raw lines 48–56.
- **Illustrative multi-merchant resource topology:** raw lines 58–81.
- **Payment settlement to balance and subsequent payout destinations:** raw lines 83–103.

## Related

- [[adyen-payouts]]
- [[adyen-platforms]]
- [[source-adyen-docs-payouts-payout-service-payout-lifecycle]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/account-structure-resources/2026-09-15|Adyen Payout Service account structure — collected 2026-09-15]]
