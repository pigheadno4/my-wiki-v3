---
title: "Adaptive Pricing — Elements Integration Guide"
type: source
date_ingested: 2026-04-21
date_updated: 2026-11-15
original_format: webpage
canonical_url: https://docs.stripe.com/payments/custom/localize-prices/adaptive-pricing
raw_files:
  - "stripe-payments-custom-localize-prices-adaptive-pricing-2026-11-07.md"
  - "stripe-adaptive-pricing-elements-2025.md"
tags: [stripe, adaptive-pricing, checkout-sessions, currency-selector, localization, elements, local-payment-methods]
---

## Summary

[[stripe]]'s April and November 2026 guides describe Adaptive Pricing for Checkout Sessions with Elements: Stripe chooses a relevant presentment currency, calculates a localized price, and handles conversion. The November guide says Stripe uses machine learning; April said it inferred currency from public IP. The wording change does not establish whether IP can still be an input. This is a Checkout Sessions API path, not a Payment Intents API integration. The guide says the feature reaches customers in more than 150 countries; that is not account-specific eligibility. See [[stripe-adaptive-pricing]] and [[stripe-currency-selector-element]].

## Enablement and price display

- The November guide separates **client readiness** (`adaptivePricing: { allowed: true }` in `stripe.initCheckoutElementsSdk` or `CheckoutElementsProvider` options) from **Checkout Session enablement** (`adaptive_pricing.enabled` per Session or Adaptive Pricing settings in the Dashboard). Both are required for the eligible Elements flow. The integration or price currency must be one of the merchant's settlement currencies; on a platform it must be a settlement currency of the merchant of record. Dashboard enablement alone, a client flag alone, or a successfully created Session does not establish local-currency presentment.
- The guide says merchants using Adaptive Pricing with Elements **must render** the Currency Selector Element, and separately says they are responsible for applicable price-localization laws. In HTML/JS, create and mount it with `checkout.createCurrencySelectorElement()`; in React mount `CurrencySelectorElement` within `CheckoutElementsProvider`. If `currencyOptions` is empty, a mounted selector displays nothing. The November troubleshooting checklist says to check client readiness, merchant-of-record settlement eligibility, cross-border customer status, and the supported currency pair. Its checklist calls `adaptivePricing.allowed` a Checkout Session field, while its explicit code and configuration sections put that camel-case property in client options and use `adaptive_pricing.enabled` for the Session. Treat the checklist wording as an internal documentation inconsistency, not a third verified Session field.
- Keep line items, shipping, discounts, tax and totals formatted consistently in the selected currency. The Elements Session can contain localized formatted values, including `session.total.total.amount`; HTML/JS reads them with `checkout.loadActions()` and `actions.getSession()`. The November React example uses `useCheckoutElements()`; April used `useCheckout()`. These are capture-specific examples, not proof the old hook was deprecated or broken.
- For one-time payments, the November guide says the selector shows local and integration amounts. For subscriptions it does not show those amounts, so display the total elsewhere on the page. Its placement guidance favors the selector near the Payment Element or total, and above Express Checkout when used. Disabling Adaptive Pricing does not affect already-converted Sessions or active subscriptions already paid in local currency, according to the November guide.

## Eligibility, local methods, and limits

- The **April 2026 capture** said Adaptive Pricing was unsupported for Indian businesses. The **November 2026 capture** instead says it supports only Indian businesses that accept international payments. This is a substantive documentary change; it does not verify a particular Indian merchant's permission, settlement currency, or currency pair.
- The November guide lists **26** local-currency payment methods, versus 20 in April: Alipay, Amazon Pay, Bacs Debit, Bancontact, Bizum, BLIK, EPS, iDEAL, Link, P24, Pix, South Korean cards, MB WAY, Naver Pay, Kakao Pay, Pay by Bank, PAYCO, PayPal, Revolut Pay, Samsung Pay, Satispay, SEPA Debit, TWINT, WeChat Pay, Klarna (EU+UK only), and UPI. Alipay, Bacs Debit, Bizum, Pay by Bank, Satispay and SEPA Debit are the six added names. This is the page's list, not a guarantee of every method for every merchant or customer. For **cross-border subscriptions**, both captures limit Adaptive Pricing to cards, Link, Apple Pay and Google Pay.
- The November restriction section excludes Elements with the Payment Intents API and Checkout Sessions with `capture_method: manual`; it also skips conversion for a customer's local currency already provided in a Price's `currency_options`, while other currencies may still convert. Unsupported Sessions show the original price currency. The April guide additionally excluded custom amounts; November omits that bullet. Preserve the custom-amount exclusion as an April-only statement with unresolved November applicability, not evidence of new support.
- In the November guide, Stripe says it uses a 24-hour guaranteed rate and lists customer-paid conversion fees of 2–4% embedded in the presented exchange rate, with no direct additional merchant fee. Choosing the integration currency avoids that Adaptive Pricing fee, though bank exchange fees may apply. It says the merchant refunds in integration currency and the customer receives their original paid currency at the original exchange rate. These are dated guide statements, not a quote for a particular transaction.

## Session representation conflict

The November price-display section says the **Elements Session** can hold localized amounts while the **API Checkout Session** remains in integration currency with customer presentment under `presentment_details` (new raw line 38). Its testing section instead says, when local currency is possible, the **Checkout Session** object's `currency`, `payment_method_types`, and `amount_total` reflect the local currency and price (new raw line 203). The April capture has the same tension at old raw lines 39 and 180. These passages are not reconciled in the captures. Inspect the actual object and context before relying on either as an unconditional rule; a localized Elements Session and an API Checkout Session are different representations.

## Testing

The guide offers the Stripe.js testing assistant and a `customer_email` suffix `+location_XX` (for example, `test+location_FR@example.com`) on a Checkout Session with `ui_mode=elements` to simulate a customer location. April's example used the Node SDK; November's uses curl. A simulated location or changed Session field in a test is not proof of a merchant's live eligibility, payment-method availability, exchange quote, or successful payment.

## Related

- [[stripe-adaptive-pricing]] — broader Adaptive Pricing concept and dated feature bounds.
- [[stripe-currency-selector-element]] — selector UI and client/Session configuration distinction.
- [[source-stripe-adaptive-pricing]] — separately captured Adaptive Pricing source; do not use it to erase the dated contradictions on this Elements path.

## Raw Sources

- [[raw/stripe-payments-custom-localize-prices-adaptive-pricing-2026-11-07|stripe-payments-custom-localize-prices-adaptive-pricing-2026-11-07]] — November 2026 full Checkout Sessions/Elements guide.
- [[raw/stripe-adaptive-pricing-elements-2025|stripe-adaptive-pricing-elements-2025]] — April 2026 full guide; preserves prior India, hook, IP, testing and custom-amount wording.
