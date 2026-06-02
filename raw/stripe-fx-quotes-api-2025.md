<!-- Source URL: https://docs.stripe.com/payments/custom/localize-prices/fx-quotes-api -->
<!-- Fetched: 2026-04-21 -->

# Enable currency conversion using the FX Quotes API

Learn how to set the currencies to localize, exchange rates, and the fees to pass along to your customers.

Use the [FX Quotes API](https://docs.stripe.com/api/fx_quotes.md) to enable the following currency conversion capabilities:

- Current exchange rates: The current exchange rate that Stripe uses for any given currency pair.
- Extended exchange rate quotes: The rate quote (5 minute, 1 hour, or 24 hours) to use to reduce uncertainty from foreign exchange fluctuations.
- Foreign exchange fee information: The details for the Stripe foreign exchange (FX) fees for your transactions, which can help with estimating settlement amounts before payment costs.

Displaying prices in a customer’s local currency can help improve conversion rates and payment authorization rates. To convert currencies, you must account for:

- The appropriate foreign currency amounts to display before checkout.
- The current exchange rates and FX fees for transactions.
- The amount of money credited to your Stripe balance in your currency.
- The frequency of exchange rate changes and when to update localized prices.

## Terms of use

Stripe doesn’t support the FX Quotes API for certain MCCs. Use the form at the bottom of this page to request access.

By using the FX Quotes API, you agree to the following [Terms of Service](https://www.stripe.com/legal/fxquotes):

- The FX Quotes API is currently offered as a _preview service_. This means Stripe offers the service “as is” and disclaims all expressed or implied warranties and guarantees around this service. You’re relying on a preview service at your own risk and Stripe isn’t liable for losses, damages, or costs arising that relate to the accuracy of the preview service.
- The FX Quotes API might provide you with a quote for a specific currency pair that’s valid for a period of time in the future. This is called an Extended Rate Quote. This quote isn’t an offer to enter into foreign exchange, and we can withdraw it at any time.
- Use of the FX Quotes API and Extended Rate Quotes must be used as part of a commercial transaction of goods and services you sell on Stripe.
- Extended Rate Quotes can help you manage general uncertainty in foreign exchange (FX) rates. You’re not permitted to selectively use Extended Rate Quotes in certain situations but not others. For example, you cannot only use Extended Rate Quotes in instances where the market FX rate is less favorable than the Extended Rate Quote.
- Stripe might add or remove supported currencies from the FX Quotes API at any time, without notice.

## Use the FX Quotes API

To access this preview feature, use a [preview API version](https://docs.stripe.com/sdks/versioning.md#public-preview-release-channel) (for example, `2025-07-30.preview`) with a beta SDK.

#### Use Stripe's SDK

Below is a sample for Ruby. You can run the equivalent command for [all SDKs](https://docs.stripe.com/sdks.md) in other languages.

```bash
gem install stripe -v 14.0.0-beta.1
```

```ruby
require 'stripe'
# Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>', stripe_version: '2025-07-30.preview')
```

#### Call the API directly

```curl
curl https://api.stripe.com/v1/fx_quotes \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2025-03-31.preview" \
  -d to_currency=gbp \
  -d "from_currencies[]=eur" \
  -d lock_duration=day
```

## Set the optimal localized price

Use the rates from the FX Quotes API to set your localized prices for other countries, based on the price you charge customers in your home country. When finalizing your localized prices, consider local market pricing and whether you want to round prices to the nearest whole number.

If you want to receive the same amount, regardless of your customer’s payment currency, you can pass the Stripe FX fee to the customer.

For example, you’re a US-based business that sells your 100 USD product in France. To calculate the equivalent price in EUR, use the `exchange_rate` parameter to pass the FX fee to the customer. If you don’t want to pass on this fee, you can use the `base_rate` parameter.

The following example response shows a quote created to convert prices presented in the local currency (EUR) to your settlement currency (USD).

```json
{
  "id": "fxq_1R6BWhL05bA97JHQELB5EROs",
  "object": "fx_quote",
  "created": 1742824731,
  "lock_duration": "five_minutes",
  "lock_expires_at": 1742825031,
  "lock_status": "active",
  "to_currency": "usd",
  "rates": {
    "eur": {
      "exchange_rate": 1.06053,
      "rate_details": {
        "base_rate": 1.08295,
        "duration_premium": 0.0007,
        "fx_fee_rate": 0.02,
        "reference_rate": 1.0827,
        "reference_rate_provider": "ecb"
      }
    }
  },
  "usage": {
    "payment": {
      "destination": null,
      "on_behalf_of": null
    },
    "transfer": null,
    "type": "payment"
  }
}
```

Using the above example:

- To pass on the FX fee to the customer: Divide the product price (100 USD) by the exchange rate (1.06053) to calculate the price for your customers in France, inclusive of the FX fee: 94.29 EUR.
- To avoid passing on the FX fee: Divide the product price (100 USD) by the base rate (1.08295) to calculate the price for your customers in France, excluding the FX fee: 92.34 EUR.

Cross-border transactions also carry an international payment method fee, depending on the geography and payment method. For more details, see the Stripe [pricing page](https://stripe.com/pricing).

## Quote durations and rate changes

If you’re interested in a longer quote `lock_duration`, contact us using the form at the bottom of this page.

```suggestion
Use the FX Quotes API to set a duration for how long an exchange rate is valid. Transactions are converted at the quoted exchange rate as long as you use the rate before it expires (`lock_expires_at`).
```

You can choose from the following time periods for `lock_duration`:

- `five_minutes`
- `hour`
- `day`
- `none`

When you set the `lock_duration` to 5 minutes, 1 hour, or 1 day, the `duration_premium` field includes the [fee charged for the extended rate quote](https://docs.stripe.com/payments/currencies/localize-prices/fx-quotes-api.md#pricing). When you set the `lock_duration` to `none`, the FX Quotes API provides exchange rate information for the current live Stripe exchange rate.

To determine the appropriate lock duration, consider the refresh rate for local prices and how long a Checkout Session lasts.

Fluctuations in the currency market can affect our ability to honor a given quote. If an exchange rate exceeds the rate threshold for payments or transfers, the extended rate quote is invalidated and the `lock_status` changes to `expired`.

If you use an expired quote for a `PaymentIntent` or `Transfer`, you receive one of the following error codes: [payment_intent_fx_quote_invalid](https://docs.stripe.com/error-codes.md#payment-intent-fx-quote-invalid) or [transfers_fx_quote_invalid](https://docs.stripe.com/error-codes.md#transfers-fx-quote-invalid). You can use these error codes to [handle expired quotes](https://docs.stripe.com/payments/currencies/localize-prices/fx-quotes-api.md#webhook-integration).

## Use locked exchange rates to localize prices

The following code example shows how to request an extended rate quote if you’re a UK-based business that localizes prices for US customers, and you want to receive 100 GBP, regardless of changes to the exchange rate. Set the `lock_duration` to `hour`.

```curl
curl https://api.stripe.com/v1/fx_quotes \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2025-03-31.preview" \
  -d to_currency=gbp \
  -d "from_currencies[]=usd" \
  -d lock_duration=day
```

> #### European Central Bank reference rates
>
> You can display the [supported](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html) European Central Bank exchange rates as a reference using the [FX Quotes API](https://docs.stripe.com/api/fx_quotes/object.md#fx_quote_object-rates-%3Cfrom_currency%3E.rate_details-reference_rate_provider).

If the exchange rate for USD is 0.8, divide your price (100 GBP) by the exchange rate (0.8) to calculate your localized price: 125 USD. Because this exchange rate is locked for the next hour, you can show 125 USD to your US customers on your site and payment page.

You can pass your US price of 125 USD into the Payment Intents API to make the payment using the `fx_quote` parameter.

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2025-03-31.preview" \
  -d amount=125 \
  -d currency=usd \
  -d fx_quote=fxq_1QBck4FTKRd55CNDdboZYz9g
```

### Handle minor units

All API requests expect `amount` values in the currency’s _minor unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)). Use the rates provided by the [FX Quotes API](https://docs.stripe.com/api/fx_quotes.md), and convert the resulting amount into Stripe [minor units](https://docs.stripe.com/currencies.md#minor-units). Learn more about [zero-decimal currencies](https://docs.stripe.com/currencies.md#zero-decimal).

> #### Disputes and refunds
>
> Stripe converts [disputed or refunded payments](https://docs.stripe.com/payments/currencies/localize-prices.md#conversions-disputes-refunds) to the presentment currency at the current exchange rate, instead of at the previous rate.

## Handle expired quotes

Stripe sends an `fx_quote.expired` webhook when a quote expires or becomes invalid because of significant rate drifts. Attaching an expired `FX Quote` object to a `PaymentIntent` or `Transfer` returns a `400` status code. To update localized prices, you can subscribe to the `fx_quote.expired` webhook and create a new extended rate quote with the `FX Quote` object.

### Mid-market rate fallback

We use the mid-market rate in cases where an extended rate quote expires or becomes unusable because of significant mid-market rate changes. This applies to some [non-card payment methods](https://stripe.com/guides/payment-methods-guide#2-choosing-the-right-payment-methods-for-your-business) that require more than 24 hours to process payments.

## Pricing

We don’t charge for extended rate quotes with a lock duration of `none`. When `lock_duration` is set to `five_minutes`, `hour`, or `day`, Stripe charges a fee to cover the risk and cost incurred. You can see this fee in the `duration_premium` field and it’s added to the `base_rate` to calculate the `exchange_rate`.

The exact fee depends on the `lock_duration`, and the currency pair used for the currency conversion. Refer to the table below to calculate the fee for an extended rate quote. If you’re converting from a currency in Group 2 to a currency in Group 1 (or the other way around), the fee listed for Group 2 applies. For example, a USD-KRW currency pair with a 1-hour duration has a 0.15% fee because KRW is in Group 2. If both currencies are in the same group, the fee for that group applies.

The FX Quote API only supports locking the currencies in the following two groups:

| Group                                                                                                                                                                                                                                                                                                                                                                                                                                      | 5 minutes | 1 hour | 24 hours |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- | ------ | -------- |
| **Group 1:** aed, aud, awg, bbd, bhd, bmd, bsd, cad, chf, dkk, eur, gbp, hkd, idr, inr, jod, jpy, kwd, myr, nzd, omr, pab, ron, sar, sek, sgd, thb, usd, xcd, yer                                                                                                                                                                                                                                                                          | 0.07%     | 0.10%  | 0.20%    |
| **Group 2:** afn, all, amd, ang, aoa, azn, bam, bdt, bif, bnd, bob, brl, bwp, bzd, clp, cny, cop, crc, cve, czk, djf, dop, dzd, fkp, gel, gip, gmd, gnf, gtq, gyd, hnl, htg, huf, ils, isk, jmd, kes, kgs, khr, krw, kyd, kzt, lkr, lrd, mad, mdl, mga, mkd, mnt, mop, mur, mvr, mxn, mzn, nad, nok, npr, pen, php, pkr, pln, pyg, qar, rsd, rwf, shp, std, tjs, tnd, try, ttd, twd, tzs, uah, ugx, uyu, uzs, vnd, xaf, xof, xpf, zar, zmw | 0.12%     | 0.15%  | 0.30%    |

## Available in preview

The FX Quotes API is currently available in the following countries:

- AT
- BE
- BG
- CA
- CH
- CY
- CZ
- DE
- DK
- EE
- ES
- FI
- FR
- GB
- GI
- GR
- HR
- HU
- IE
- IT
- LT
- LU
- LV
- MT
- NL
- NO
- PL
- PT
- RO
- SE
- SI
- SK
- US
