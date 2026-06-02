<!-- Source: Stripe Checkout — Display yearly prices in monthly terms -->
<!-- Fetched: 2026-04-20 -->

# Display yearly prices in monthly terms

Help customers compare prices by displaying yearly prices in monthly terms.

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/yearly-price-display?payment-ui=stripe-hosted.

You can display annually billed prices as their per month cost equivalent across Checkout, Payment Links, [pricing tables](https://docs.stripe.com/payments/checkout/pricing-table.md), and [buy buttons](https://docs.stripe.com/payment-links/buy-button.md). You can manage pricing display in your [Checkout and Payment Links settings](https://dashboard.stripe.com/settings/checkout).

## Checkout and Payment Links

When you have pricing set to display `per month`, Checkout shows a label with the equivalent monthly rate below the yearly total. If the yearly price is an [upsell](https://docs.stripe.com/payments/checkout/upsells.md) from a monthly price and has a lower equivalent monthly rate, the old price displays with a strikethrough.
![A yearly recurring price with a monthly terms description in Checkout](assets/stripe-checkout-yearly-price-upsell.png)

## Pricing table

When you have pricing set to display `per month`, the pricing table displays the equivalent monthly rate of eligible yearly prices followed by the total annual amount.
![A pricing table with yearly prices displayed in monthly terms](assets/stripe-checkout-yearly-price-table.png)

## Buy button

When you have pricing set to display `per month`, the buy button displays the equivalent monthly rate of eligible yearly prices followed by the total annual amount.
![A buy button with a yearly price displayed in monthly terms](assets/stripe-checkout-yearly-price-buy-button.png)

## Restrictions

Customers, sessions, and pricing tables with any of the following features aren’t eligible to display `per month`:

- A combination of recurring and one-time prices
- Prices with recurring intervals that aren’t billed annually
- Prices with free trials or [billing cycle anchors](https://docs.stripe.com/payments/checkout/billing-cycle.md)
- [Usage-based pricing](https://docs.stripe.com/products-prices/pricing-models.md#usage-based-pricing)

# Embedded page

> This is a Embedded page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/yearly-price-display?payment-ui=embedded-form.

You can display annually billed prices as their per month cost equivalent across Checkout, Payment Links, [pricing tables](https://docs.stripe.com/payments/checkout/pricing-table.md), and [buy buttons](https://docs.stripe.com/payment-links/buy-button.md). You can manage pricing display in your [Checkout and Payment Links settings](https://dashboard.stripe.com/settings/checkout).

## Checkout and Payment Links

When you have pricing set to display `per month`, Checkout shows a label with the equivalent monthly rate below the yearly total. If the yearly price is an [upsell](https://docs.stripe.com/payments/checkout/upsells.md) from a monthly price and has a lower equivalent monthly rate, the old price displays with a strikethrough.
![A yearly recurring price with a monthly terms description in Checkout](assets/stripe-checkout-yearly-price-upsell.png)

## Pricing table

When you have pricing set to display `per month`, the pricing table displays the equivalent monthly rate of eligible yearly prices followed by the total annual amount.
![A pricing table with yearly prices displayed in monthly terms](assets/stripe-checkout-yearly-price-table.png)

## Buy button

When you have pricing set to display `per month`, the buy button displays the equivalent monthly rate of eligible yearly prices followed by the total annual amount.
![A buy button with a yearly price displayed in monthly terms](assets/stripe-checkout-yearly-price-buy-button.png)

## Restrictions

Customers, sessions, and pricing tables with any of the following features aren’t eligible to display `per month`:

- A combination of recurring and one-time prices
- Prices with recurring intervals that aren’t billed annually
- Prices with free trials or [billing cycle anchors](https://docs.stripe.com/payments/checkout/billing-cycle.md)
- [Usage-based pricing](https://docs.stripe.com/products-prices/pricing-models.md#usage-based-pricing)
