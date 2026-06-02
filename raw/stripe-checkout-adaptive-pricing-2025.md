<!-- Source: Stripe Checkout — Adaptive Pricing -->
<!-- Fetched: 2026-04-20 -->

# Adaptive Pricing

Learn about using Adaptive Pricing to allow customers to pay in their local currency.

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/localize-prices/adaptive-pricing?payment-ui=stripe-hosted.

Adaptive Pricing lets your customers pay in their local currency in more than [150 countries](https://docs.stripe.com/payments/checkout/localize-prices/adaptive-pricing.md#supported-currencies). With Adaptive Pricing, Stripe uses machine learning to determine the most relevant presentment currency, then automatically calculates the localized price and handles all currency conversion.

Use Adaptive Pricing to:

- Display pricing in local currencies based on location
- Calculate prices in real time using an exchange rate guaranteed for 24 hours
- Unlock payment methods that require local currency
- Facilitate compliance when presenting supported currencies

#### Integration effort

Complexity: 1/5

#### Fees

View information on [fees and our FAQ](https://support.stripe.com/questions/adaptive-pricing).

## Enable Adaptive Pricing in the Dashboard [Dashboard]

Adaptive Pricing is always enabled for Payment Links. Manage Adaptive Pricing for Checkout in your [payment settings](https://dashboard.stripe.com/settings/adaptive-pricing) in the Dashboard. You can enable Adaptive Pricing in a sandbox and live mode. Disabling Adaptive Pricing doesn’t affect Checkout Sessions that have already been converted or active subscriptions paid in customers’ local currencies.

## Configure local payment methods [Dashboard]

Adaptive Pricing can increase the usage of local payment methods by ensuring customers have the option to pay in their local currency and with payment methods most relevant to them. As an example, 70% of all e-commerce transactions in the Netherlands use iDEAL, but it only works with EUR. You can configure which payment methods you accept in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) if you use dynamic payment methods. Adaptive Pricing provides access to the following payment methods that require presenting in local currency:

- Amazon Pay
- Bancontact
- BLIK
- EPS
- iDEAL
- Link
- P24
- Pix
- South Korean cards
- MB WAY
- Naver Pay
- Kakao Pay
- PAYCO
- PayPal
- Revolut Pay
- Samsung Pay
- TWINT
- Wechat Pay
- Klarna (EU+UK only)
- UPI

> For cross-border subscriptions, Adaptive Pricing supports only card payments, Link, Apple Pay, and Google Pay.

## Event destinations and reporting [Server-side]

The Checkout Session and the underlying `PaymentIntent` objects reflect what your customer paid in your integration currency and amount, which is the currency you specified for your prices.

If a customer pays in their local currency, the [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) and [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event contains a `presentment_details` hash that includes the `presentment_amount` and `presentment_currency`.

#### JSON

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  "type": "checkout.session.completed",
  "data": {
    "object": {
      "id": "{{SESSION_ID}}",
      "object": "checkout.session",
      "currency": "usd",
      "amount_total": 1000,
      "amount_subtotal": 1000,
      "presentment_details": {
        "presentment_amount": 1370,
        "presentment_currency": "cad"
      }
    }
  }
}
```

When a recurring subscription invoice is paid in the local currency, the [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event for each `PaymentIntent` associated with the invoice contains a `presentment_details` hash that includes the `presentment_amount` and `presentment_currency`.

#### JSON

```json
{
  "id": "{{PAYMENT_INTENT_ID}}",
  "object": "payment_intent",
  "currency": "usd",
  "amount": 1000,
  "presentment_details": {
    "presentment_amount": 1370,
    "presentment_currency": "cad"
  }
}
```

When a recurring subscription is created in the local currency, the [customer.subscription.created](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.created) event contains a `presentment_details` hash that includes the `presentment_currency`, which reflects the local currency that will be used for off-session payments.

## Testing

To test local currency presentment for Checkout and Payment Links, pass in a location-formatted customer email that includes a suffix in a `+location_XX` format in the local part of the email. `XX` must be a valid [two-letter ISO country code](https://www.nationsonline.org/oneworld/country_code_list.htm).

For example, to test currency presentment for a customer in France, pass in an email like `test+location_FR@example.com`.

When you visit the URL for a Checkout Session or Payment Link created with a location-formatted email, you see the same currency as a customer does in the specified country.

### Testing Checkout

When you create a Checkout Session, pass the location-formatted email as [customer_email](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-customer_email) to simulate Checkout from a particular country.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "payment",
  return_url: "https://example.com/return",
  customer_email: "test+location_FR@example.com",
});
```

You can also create a new customer and specify an email for them that contains the `+location_XX` suffix. Stripe test cards work as usual.

### Testing Payment Links

For Payment Links, pass the location-formatted email as the `prefilled_email` [URL parameter](https://docs.stripe.com/payment-links/customize.md#customize-checkout-with-url-parameters) to test currency presentment for customers in different countries.

## Restrictions

Adaptive Pricing isn’t available for businesses using Elements with the Payment Intents API.

Adaptive Pricing isn’t supported for Indian businesses.

Additionally, Adaptive Pricing requires the [currency for your prices](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-currency) to be one of your settlement currencies. Prices automatically convert during checkout. This applies to [prices](https://docs.stripe.com/products-prices/manage-prices.md#prices-create) you create and reference with a price ID and prices you create inline with [price_data](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-price_data) when you create a Checkout Session.

If you process payments through a platform, we require your platform’s integration currency to be the settlement currency of the merchant of record on the charge.

Adaptive Pricing doesn’t apply for Checkout Sessions that:

- Contain prices where the customer’s local currency is already defined in the price’s [currency_options](https://docs.stripe.com/payments/checkout/localize-prices/manual-currency-prices.md). For example, if a price has `currency_options` for EUR and GBP, Adaptive Pricing won’t convert to EUR or GBP, but it can still convert to other currencies like CAD or JPY.
- Use [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-capture_method) as `manual`.
- Use [custom amounts](https://docs.stripe.com/payments/checkout/pay-what-you-want.md).

Checkout Sessions that aren’t supported by Adaptive Pricing present prices in the original currency that you’ve set your prices in.

## Supported currencies

Businesses in supported regions can automatically convert prices to the local currencies of their customers in the following markets:

### North America

- AG
- AW
- BS
- BB
- BZ
- BM
- CA
- KY
- CR
- DM
- DO
- GD
- GT
- HT
- HN
- MX
- JM
- PA
- KN
- LC
- VC
- TT
- US

### South America

- BR
- BO
- CO
- CL
- FK
- GY
- PY
- PE
- UY

### Europe

- AL
- AD
- AT
- BE
- BA
- HR
- CY
- CZ
- DK
- EE
- FI
- FR
- DE
- GI
- GR
- HU
- IS
- IE
- IT
- LV
- LT
- LU
- MT
- MC
- MD
- ME
- NL
- MK
- NO
- PL
- PT
- RO
- SM
- RS
- SK
- SI
- ES
- SE
- CH
- UA
- GB
- VA

### Asia

- AF
- AM
- AZ
- BD
- BN
- KH
- CN
- GE
- HK
- IN
- ID
- IL
- JP
- KZ
- KG
- MO
- MY
- MV
- MN
- NP
- PK
- PH
- QA
- SA
- SG
- KR
- LK
- TW
- TJ
- TH
- TR
- AE
- UZ
- VN
- YE

### Oceania

- AU
- PF
- NC
- NZ
- WF

### Africa

- AO
- DZ
- BJ
- BW
- BF
- BI
- CM
- CV
- CF
- TD
- CI
- DJ
- GQ
- GA
- GM
- GN
- GW
- KE
- LR
- MG
- ML
- MU
- MA
- MZ
- NA
- NE
- CG
- RW
- SH
- ST
- SN
- ZA
- TZ
- TG
- UG
- ZM

## Pricing

- You pay 0%
- Your customers pay 2–4%

You don’t directly pay any additional Stripe fees for Adaptive Pricing, as all such fees are paid for by your customers. The Stripe-provided exchange rate you present to your customers includes a 2–4% conversion fee, increasing their purchase price by a corresponding amount. Stripe determines the fee, which varies for the purposes of increasing customer conversion. Your customer doesn’t pay this fee if they choose to pay in your integration currency, but their bank’s exchange rate and fees might apply. For detailed information about current Stripe fees, see our [pricing page](https://stripe.com/pricing).

## Exchange rate

Stripe uses the mid-market exchange rate and applies a fee to guarantee the rate through settlement.

Learn more about how Stripe handles [currency conversions](https://docs.stripe.com/currencies.md) and [Adaptive Pricing fees](https://support.stripe.com/questions/adaptive-pricing#:~:text=Adaptive%20Pricing%20is%20a%20Checkout,latest%20Stripe%2Dprovided%20exchange%20rates).

## Refunds

You can issue a refund in your integration currency, and Stripe refunds your customer in the currency they used to make the payment. The refund uses the same exchange rate as the original transaction, so there are no extra costs for you, and your customer gets back the exact amount they paid.

Learn more about how Stripe helps you manage [refunds](https://docs.stripe.com/refunds.md).

# Embedded page

> This is a Embedded page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/localize-prices/adaptive-pricing?payment-ui=embedded-form.

Adaptive Pricing lets your customers pay in their local currency in more than [150 countries](https://docs.stripe.com/payments/checkout/localize-prices/adaptive-pricing.md#supported-currencies). With Adaptive Pricing, Stripe uses machine learning to determine the most relevant presentment currency, then automatically calculates the localized price and handles all currency conversion.

Use Adaptive Pricing to:

- Display pricing in local currencies based on location
- Calculate prices in real time using an exchange rate guaranteed for 24 hours
- Unlock payment methods that require local currency
- Facilitate compliance when presenting supported currencies

#### Integration effort

Complexity: 1/5

#### Fees

View information on [fees and our FAQ](https://support.stripe.com/questions/adaptive-pricing).

## Enable Adaptive Pricing in the Dashboard [Dashboard]

Manage Adaptive Pricing for Checkout in your [payment settings](https://dashboard.stripe.com/settings/adaptive-pricing) in the Dashboard. You can enable Adaptive Pricing in a sandbox and live mode. Disabling Adaptive Pricing doesn’t affect Checkout Sessions that have already been converted or active subscriptions paid in customers’ local currencies.

## Configure local payment methods [Dashboard]

Adaptive Pricing can increase the usage of local payment methods by ensuring customers have the option to pay in their local currency and with payment methods most relevant to them. As an example, 70% of all e-commerce transactions in the Netherlands use iDEAL, but it only works with EUR. You can configure which payment methods you accept in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) if you use dynamic payment methods. Adaptive Pricing provides access to the following payment methods that require presenting in local currency:

- Amazon Pay
- Bancontact
- BLIK
- EPS
- iDEAL
- Link
- P24
- Pix
- South Korean cards
- MB WAY
- Naver Pay
- Kakao Pay
- PAYCO
- PayPal
- Revolut Pay
- Samsung Pay
- TWINT
- Wechat Pay
- Klarna (EU+UK only)
- UPI

> For cross-border subscriptions, Adaptive Pricing supports only card payments, Link, Apple Pay, and Google Pay.

## Event destinations and reporting [Server-side]

The Checkout Session and the underlying `PaymentIntent` objects reflect what your customer paid in your integration currency and amount, which is the currency you specified for your prices.

If a customer pays in their local currency, the [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) and [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event contains a `presentment_details` hash that includes the `presentment_amount` and `presentment_currency`.

#### JSON

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  "type": "checkout.session.completed",
  "data": {
    "object": {
      "id": "{{SESSION_ID}}",
      "object": "checkout.session",
      "currency": "usd",
      "amount_total": 1000,
      "amount_subtotal": 1000,
      "presentment_details": {
        "presentment_amount": 1370,
        "presentment_currency": "cad"
      }
    }
  }
}
```

When a recurring subscription invoice is paid in the local currency, the [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event for each `PaymentIntent` associated with the invoice contains a `presentment_details` hash that includes the `presentment_amount` and `presentment_currency`.

#### JSON

```json
{
  "id": "{{PAYMENT_INTENT_ID}}",
  "object": "payment_intent",
  "currency": "usd",
  "amount": 1000,
  "presentment_details": {
    "presentment_amount": 1370,
    "presentment_currency": "cad"
  }
}
```

When a recurring subscription is created in the local currency, the [customer.subscription.created](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.created) event contains a `presentment_details` hash that includes the `presentment_currency`, which reflects the local currency that will be used for off-session payments.

## Testing

To test local currency presentment, pass in a location-formatted customer email that includes a suffix in a `+location_XX` format in the local part of the email. `XX` must be a valid [two-letter ISO country code](https://www.nationsonline.org/oneworld/country_code_list.htm).

For example, to test currency presentment for a customer in France, pass in an email like `test+location_FR@example.com`. A Checkout Session created with a location-formatted email displays the same currency as the specified country.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "payment",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
  customer_email: "test+location_FR@example.com",
});
```

You can also create a new customer and specify an email for them that contains the `+location_XX` suffix. Stripe test cards work as usual.

## Restrictions

Adaptive Pricing isn’t available for businesses using Elements with the Payment Intents API.

Adaptive Pricing isn’t supported for Indian businesses.

Additionally, Adaptive Pricing requires the [currency for your prices](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-currency) to be one of your settlement currencies. Prices automatically convert during checkout. This applies to [prices](https://docs.stripe.com/products-prices/manage-prices.md#prices-create) you create and reference with a price ID and prices you create inline with [price_data](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-price_data) when you create a Checkout Session.

If you process payments through a platform, we require your platform’s integration currency to be the settlement currency of the merchant of record on the charge.

Adaptive Pricing doesn’t apply for Checkout Sessions that:

- Contain prices where the customer’s local currency is already defined in the price’s [currency_options](https://docs.stripe.com/payments/checkout/localize-prices/manual-currency-prices.md). For example, if a price has `currency_options` for EUR and GBP, Adaptive Pricing won’t convert to EUR or GBP, but it can still convert to other currencies like CAD or JPY.
- Use [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-capture_method) as `manual`.
- Use [custom amounts](https://docs.stripe.com/payments/checkout/pay-what-you-want.md).

Checkout Sessions that aren’t supported by Adaptive Pricing present prices in the original currency that you’ve set your prices in.

## Supported currencies

Businesses in supported regions can automatically convert prices to the local currencies of their customers in the following markets:

### North America

- AG
- AW
- BS
- BB
- BZ
- BM
- CA
- KY
- CR
- DM
- DO
- GD
- GT
- HT
- HN
- MX
- JM
- PA
- KN
- LC
- VC
- TT
- US

### South America

- BR
- BO
- CO
- CL
- FK
- GY
- PY
- PE
- UY

### Europe

- AL
- AD
- AT
- BE
- BA
- HR
- CY
- CZ
- DK
- EE
- FI
- FR
- DE
- GI
- GR
- HU
- IS
- IE
- IT
- LV
- LT
- LU
- MT
- MC
- MD
- ME
- NL
- MK
- NO
- PL
- PT
- RO
- SM
- RS
- SK
- SI
- ES
- SE
- CH
- UA
- GB
- VA

### Asia

- AF
- AM
- AZ
- BD
- BN
- KH
- CN
- GE
- HK
- IN
- ID
- IL
- JP
- KZ
- KG
- MO
- MY
- MV
- MN
- NP
- PK
- PH
- QA
- SA
- SG
- KR
- LK
- TW
- TJ
- TH
- TR
- AE
- UZ
- VN
- YE

### Oceania

- AU
- PF
- NC
- NZ
- WF

### Africa

- AO
- DZ
- BJ
- BW
- BF
- BI
- CM
- CV
- CF
- TD
- CI
- DJ
- GQ
- GA
- GM
- GN
- GW
- KE
- LR
- MG
- ML
- MU
- MA
- MZ
- NA
- NE
- CG
- RW
- SH
- ST
- SN
- ZA
- TZ
- TG
- UG
- ZM

## Pricing

- You pay 0%
- Your customers pay 2–4%

You don’t directly pay any additional Stripe fees for Adaptive Pricing, as all such fees are paid for by your customers. The Stripe-provided exchange rate you present to your customers includes a 2–4% conversion fee, increasing their purchase price by a corresponding amount. Stripe determines the fee, which varies for the purposes of increasing customer conversion. Your customer doesn’t pay this fee if they choose to pay in your integration currency, but their bank’s exchange rate and fees might apply. For detailed information about current Stripe fees, see our [pricing page](https://stripe.com/pricing).

## Exchange rate

Stripe uses the mid-market exchange rate and applies a fee to guarantee the rate through settlement.

Learn more about how Stripe handles [currency conversions](https://docs.stripe.com/currencies.md) and [Adaptive Pricing fees](https://support.stripe.com/questions/adaptive-pricing#:~:text=Adaptive%20Pricing%20is%20a%20Checkout,latest%20Stripe%2Dprovided%20exchange%20rates).

## Refunds

You can issue a refund in your integration currency, and Stripe refunds your customer in the currency they used to make the payment. The refund uses the same exchange rate as the original transaction, so there are no extra costs for you, and your customer gets back the exact amount they paid.

Learn more about how Stripe helps you manage [refunds](https://docs.stripe.com/refunds.md).

## See also

- [Adaptive Pricing FAQ](https://support.stripe.com/questions/adaptive-pricing)
