<!-- Source URL: https://docs.stripe.com/payments/quickstart-checkout-sessions -->
<!-- Fetched: 2026-04-20 -->

# Build a payments page

Create a payments page with prebuilt UIs using the Checkout Sessions API.

## Accept payments on your website

Accept one-time and subscription payments from more than 100 local payment methods.

## Two Checkout UI Options

You can use two different payment UIs with the Checkout Sessions API:

- **Checkout page** — Customers enter their payment details in a fully-featured payment page, either embedded on your site or via a redirect to a Stripe-hosted page.

![Checkout hosted page](assets/checkout-hosted-hover.6ee5a154986ffc216c034a47b7b0d65e.png)

- **Checkout elements** — Build a fully customized payment page using elements.

![Checkout elements](assets/checkout-elements-hover.28148f5be39600e85ef4784ab9e873e7.png)

![Card brand choice full page](assets/checkout-card-brand-choice-full-page.9cf891dfb55abcdc9ae9046ea15bc054.png)

## Comparison: Checkout Page vs Checkout Elements

| | PAGE (Recommended) | ELEMENTS |
| --- | --- | --- |
| API | Checkout Sessions | Checkout Sessions |
| Feature list | Out of the box UI support for Billing, Tax, Adaptive Pricing, Stripe Managed Payments, Link, Dynamic payment methods, Surcharging, Split-tender | Out of the box UI support for Adaptive Pricing, Link, Dynamic payment methods |
| Order summary | Includes full order summary with subtotals (tax and shipping costs), cross-sells & upsells, free trials, discounts and promo codes | No order summary |
| Ongoing maintenance required | No | Yes |
| Hosting | Hosted or Embedded | Embedded only |
| Complexity | Low | Most (highest) |
| Customization | 15 configurable settings via brand settings | Full CSS customization via the Appearance API |

## Customize Checkout

- Customize the look and feel — appearance and behavior of the checkout flow
- Collect additional information — shipping details and other customer information
- Collect taxes — for one-time payments in Stripe Checkout
- Dynamically update checkout — make updates while your customer checks out
- Extend checkout with custom components — add custom components to payment form
- Add trials, discounts, and upsells — promotions, trials, discounts, optional items

## Change When and How You Collect Payment

- Set up subscriptions — recurring payments for your customers
- Set up future payments — save customer payment details to charge later
- Save payment details during payment — accept a payment and save details for future purchases
- Let customers pay in their local currency — Adaptive Pricing

## Manage Your Business

- Manage your product catalog — handle inventory and fulfillment with Checkout
- Migrate payment methods to the Dashboard — migrate management of payment methods
- After the payment — customize the post-payment checkout process

## Sample Projects

- One-time payments: Web, Mobile web
- Subscriptions: Web, Mobile web, Stripe Billing
