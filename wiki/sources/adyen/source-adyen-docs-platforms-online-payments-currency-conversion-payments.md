---
title: "Adyen Platforms: convert the currency of an online payment"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/currency-conversion/payments"
raw_files:
  - "adyen/docs/platforms/online-payments/currency-conversion/payments/2026-09-15.md"
tags: [adyen, platforms, online-payments, currency-conversion, foreign-exchange]
---

## Overview

This 2026-09-15 Adyen for Platforms overview describes a limited-availability pilot for an online payment in which the customer pays in a processing currency and the platform's user is credited in a different settlement currency. The platform fixes the goods or services price in one of those currencies, calculates the amount in the other, and sends both amounts in a `POST /payments` request. This overview routes to separate fixed-settlement and fixed-processing procedures; it does not itself specify rate-calculation fields, split instructions, fees, refund handling or actual booking evidence. See [[adyen]], [[adyen-platforms]] and [[adyen-currencies-and-fx]].

## Key takeaways

- **Pilot scope:** The page says currency conversion is in pilot, and its processes and documentation may change. It describes the processing currency as the one in which the customer pays and the settlement currency as the one in which the user wants to be paid. A dated description does not prove current availability, account eligibility, a specific currency pair, rate or completed funds movement.
- **Choose which amount is fixed:** If the goods price is fixed in settlement currency, the user's amount stays fixed and the customer's processing-currency amount is calculated. If fixed in processing currency, the customer's amount stays fixed and the user's settlement-currency amount is calculated. The overview says to use the prevailing exchange rate of the day for the other amount, without supplying a quote, formula or markup terms.
- **Common sequence:** The user sells goods or services to a customer; the platform determines the other currency amount and submits `POST /payments` specifying both currency amounts. The page describes Adyen debiting the customer and crediting the user in their respective currencies when it receives the request. It is not an observed authorization, capture, booking, payout or merchant-of-record determination.
- **Detailed routes:** Consult [[source-adyen-docs-platforms-online-payments-currency-conversion-payments-fix-settlement-currency]] or [[source-adyen-docs-platforms-online-payments-currency-conversion-payments-fix-processing-currency]] for the chosen fixed-price path, including its own prerequisites and consequences. This overview does not establish those procedures for every account or payment method.

## Detail locators

- Pilot warning and processing-versus-settlement roles: raw lines 15–26. Common sale, calculation and `/payments` sequence: lines 28–33. Choice of fixed currency and prevailing-rate statement: lines 35–39. Links to the two detailed paths and which party's amount stays fixed: lines 41–51.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform and user context.
- [[adyen-currencies-and-fx]] — provider currency and FX context.
- [[source-adyen-docs-platforms-online-payments-currency-conversion-payments-fix-settlement-currency]] — fixed user settlement amount procedure.
- [[source-adyen-docs-platforms-online-payments-currency-conversion-payments-fix-processing-currency]] — fixed customer processing amount procedure.

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/currency-conversion/payments/2026-09-15|Adyen Docs: Convert the currency of a payment (2026-09-15 snapshot; pilot)]]
