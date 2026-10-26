---
title: "Pay by Bank (US) Web Component integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pay-by-bank-us/web-component"
raw_files:
  - "adyen/docs/payment-methods/pay-by-bank-us/web-component/2026-09-15.md"
tags: [adyen, pay-by-bank-us, web, components, ach, capture, online-payments, tokenization]
---

## Overview

This Pay by Bank (US) Web Components add-on (metadata last modified 2019-09-06, captured 2026-09-15) covers existing Sessions and Advanced integrations, a `PayByBankUS` Component, country-code guidance, capture risk, recurring tokenization, TEST scenarios and a partner-registration gate for live use. **Authorization checks do not hold the shopper's bank funds**; capture can fail for insufficient funds even when initiated immediately. [[adyen]] [[adyen-online-payments]] [[adyen-payment-capture]]

## Key takeaways

- Both **Sessions** and **Advanced** requirements call for an existing Web Components integration at **v5.70.0 or later** and contacting Support to add Pay by Bank (US) in Customer Area. For v6 the named import is `PayByBankUS` and construction uses `new PayByBankUS(checkout)`; v5.x.x or earlier uses `checkout.create('paybybank_AIS_DD')`. The v6 import-guide link is labeled Components but contains `integration=Drop-in`; verify the Web Components base guide rather than using that link as an exact route. See raw lines 21–45 and 67–97.
- The `/sessions` table marks `countryCode` required while its description says only **US** is supported and US is the default when omitted. Preserve that table/description tension rather than asserting a universal requiredness rule. The `/payments` table marks `countryCode` optional, defaults to US, and **recommends** sending it for potential future non-US bank support; that future possibility is not current support. Both say country determines banks shown by the partner. See raw lines 47–65.
- The existing Components integration handles redirect and payment outcome; this page prescribes no additional method-specific redirect or outcome code. It does not give an authorization response example or make a return transition final-payment proof. See raw lines 99–105.
- Adyen **strongly recommends** capturing immediately: Plaid checks account balance and risk at authorization, but the issuing bank does not hold those funds. Balance can become insufficient before capture, and even immediate capture has this risk because ACH Direct Debit capture is asynchronous. This recommendation is not a guarantee of funds or settlement. See raw lines 107–113.
- The page says Pay by Bank (US) supports tokenization for recurring transactions and **strongly recommends** explicit shopper permission plus a clear schedule and amount to reduce chargeback risk. It delegates token creation, subsequent use and management to the general Tokenization guide rather than specifying a method-specific token request here. [[adyen-tokenization]] See raw lines 115–125.
- TEST can use amount scenarios (USD 3.53 approved, USD 27.53 a specified risk refusal), `custom_balances` for selectable balances, and `custom_chargeback_rXX` for an ACH return reason. The chargeback simulation first reports `Authorised`; its Chargeback stage starts after capture and settlement, with a `CHARGEBACK` webhook. TEST mimics live redirect but cannot simulate every refusal. These examples are simulator behavior, not live outcome guarantees. See raw lines 127–176.
- Live acceptance requires adding the method in live Customer Area **and** waiting for partner Plaid registration of the merchant account with participating banks. The page says registration takes up to one business week **from Plaid starting the process**, shoppers cannot connect during it, and a `paymentMethod.created` webhook announces when live acceptance can begin. This 2026-09-15 snapshot does not establish current registration or eligibility. See raw lines 178–182.

## Detail locators

- Sessions/Advanced version and Support prerequisites; v6/v5 Component setup: raw lines 21–45 and 67–97.
- Session versus payment country-code tables: raw lines 47–65.
- Redirect/outcome delegation and ACH capture risk: raw lines 99–113.
- Recurring tokenization and permission recommendation: raw lines 115–125.
- TEST payment and chargeback simulations: raw lines 127–176.
- Live Customer Area, Plaid registration and readiness webhook: raw lines 178–182.

## Related

- [[adyen-online-payments]] — Web Components integration context.
- [[adyen-payment-capture]] — asynchronous capture boundary.
- [[adyen-tokenization]] — linked general recurring-token workflow.
- [[source-adyen-docs-payment-methods-pay-by-bank-us]] — method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/pay-by-bank-us/web-component/2026-09-15|Pay by Bank US Web Component, captured 2026-09-15]]
