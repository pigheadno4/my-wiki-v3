---
title: "Manage bank account details | Adyen Payout Service"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts/manage-bank-details"
raw_files:
  - "adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/manage-bank-details/2026-09-15.md"
tags: [adyen, payout-service, bank-details, tokenization, third-party-payouts]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] **Payout Service** guide describes tokenizing a third-party counterparty's bank details so a merchant can refer to them in later bank-payout requests. A token is a reference to the bank details, not proof that the bank account is valid, that a payout has been made or that a beneficiary received funds. See [[adyen-payouts]] for this Transfers API payout route and [[adyen-tokenization]] for the token family. [Raw: lines 15–23, 34–35, 519–565]

## Key takeaways

- Before this flow, the guide calls for a Payout Service integration, **Checkout API for tokenization**, a company `ws@Company.[YourCompanyAccount]` API credential with **Checkout encrypted cardholder data** role, a webhook receiver, and Adyen-contact enablement. That named role is the page's prerequisite despite the bank-details subject; it does not by itself establish PCI scope or actual credential assignment. [Raw: lines 25–37]
- The captured local-tokenized detail scope is IBAN/SEPA Direct Debit, UK Local/BACS and US Local/ACH. **Local account details cannot be used for cross-border transfers**; the guide says to use a cross-border-capable identification format such as NumberAndBic. Token creation **does not validate the bank account**, so invalid details can cause a later payout to fail. The list is dated provider guidance, not proof of current regional enablement. [Raw: lines 34–52]
- To store details, the documented server request is Checkout API `POST /payments` with `amount.value: 0`, applicable currency, bank-detail `paymentMethod` (`sepadirectdebit`, `ukLocal` or `usLocal`), billing address, `enablePayOut: true`, merchant account, `recurringProcessingModel: Subscription`, payment reference, return URL, bank-holder `shopperReference` and `storePaymentMethod: true`. This is a **zero-auth tokenization setup**, not a funds payout; the example is a TEST-environment SEPA request. [Raw: lines 54–112]
- The page says a token is created **after successful payment authorization**. Retrieve `storedPaymentMethodId` from `additionalData.tokenization.storedPaymentMethodId` in the successful authorization response or from `recurring.token.created`; store it together with `additionalData.tokenization.shopperReference`. Both values are needed for the later bank-payout request, whose own child guide controls transfer submission and outcome. A zero amount or the sample `Authorised` response does not establish bank verification, payout booking or bank receipt. [Raw: lines 519–571]

## Detail locators

- Payout-token purpose and feature/credential/webhook requirements: raw lines 19–37.
- Cross-border restriction, no account validation and dated local-format scope: raw lines 34–52.
- Zero-auth Checkout `POST /payments` request fields and TEST example: raw lines 54–112.
- Language-specific illustrative library requests: raw lines 114–517.
- Authorization-gated token location and required token/holder pair: raw lines 519–565.
- Separate payout-request route: raw lines 567–571.

## Related

- [[adyen-payouts]] — Payout Service route and legacy Payout API distinction
- [[adyen-tokenization]] — token family context
- [[source-adyen-docs-payouts-payout-service-pay-out-to-bank-accounts]] — third-party bank payout route, currencies and priorities
- [[source-adyen-docs-payouts-payout-service-pay-out-to-bank-accounts-bank-payout-request]] — payout request and transfer outcome child guide

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/manage-bank-details/2026-09-15|Pinned Payout Service manage-bank-details guide]]
