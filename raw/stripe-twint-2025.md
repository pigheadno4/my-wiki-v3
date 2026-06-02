<!-- Source URL: https://docs.stripe.com/payments/twint -->
<!-- Fetched: 2026-05-03 -->

# TWINT payments

Learn about TWINT, a popular payment method in Switzerland.

TWINT is a payment method used in Switzerland that allows customers to [authenticate and approve](https://docs.stripe.com/payments/payment-methods.md#customer-actions) payments using an approved TWINT mobile app.

You get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

#### Payment method properties

- **Customer locations**

  Switzerland

- **Presentment currency**

  CHF

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Bank redirects

- **Recurring payments**

  Yes

- **Payout timing**

  [Standard payout timing](https://docs.stripe.com/payouts.md#payout-speed) applies

- **Connect support**

  [Yes](https://docs.stripe.com/payments/twint.md#connect)

- **Dispute support**

  [Yes](https://docs.stripe.com/payments/twint.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/twint.md#refunds)

- **Maximum Amount**

  5000.00 CHF

#### Business locations

Stripe accounts in the following countries can accept TWINT payments:

- AT
- BE
- BG
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
- IS
- IT
- LI
- LT
- LU
- LV
- MC
- MT
- NL
- NO
- PL
- PT
- RO
- SE
- SI
- SK
- SM

#### Product support

- Elements1
- Checkout
- Payment Links
- Connect
- Subscriptions
- Invoicing

1Express Checkout Element doesn’t support TWINT.

## Payment flows

Customers pay with TWINT by using one of the following methods:

- **Mobile**: Customers follow a mobile redirect from your website or mobile app to a TWINT app, where they authorize the payment, then return to your website or mobile app.

- **Desktop**: Customers scan a QR code you present on your website using a TWINT app, which allows them to authorize the payment.

## Get started

You don’t have to integrate TWINT and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable TWINT. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add TWINT from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)

If you prefer to manually list payment methods, learn how to [manually configure TWINT as a payment method](https://docs.stripe.com/payments/twint/accept-a-payment.md).

## Comply with TWINT merchant onboarding requirements

> Make sure you comply with the following TWINT requirements *before* requesting access to Twint as a payment method in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) or through the [capabilities API](https://docs.stripe.com/api/capabilities.md).

- Businesses must have a functional website that is reachable and isn’t password protected or in a “coming soon” state.
- The business website must contain the following information visible in the legal notice, terms of service or terms and conditions:
  - Company name and legal form (for sole proprietorships, the full first and last name of the business owner).
  - Full business address, including street, house number, postal code, and city.
  - Contact details, including at least one of an email address or a telephone number.
- Switzerland must be available as a shipping destination for businesses selling physical goods, and you must display prices in CHF (Swiss Francs), at the latest during the checkout process.

> You can use [Adaptive Pricing](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md) to automate currency displays without having to explicitly price your products in CHF.

The TWINT payments capability stays in a `pending` state until the compliance with the TWINT onboarding requirements is verified. Contact [Stripe support](https://support.stripe.com/contact) you’re unsure about your TWINT payments capability status.

## Termination rights

In addition to the termination and suspension rights included in the [Stripe Services Agreement](https://stripe.com/legal/ssa), TWINT has the right to suspend or terminate your use of TWINT, such as for breach of the requirements listed above that aren’t promptly remedied.

## Refunds

You can refund TWINT charges up to 180 days after the payment completes. Refunds usually take a few minutes to complete. TWINT supports full and partial refunds. You can also issue multiple partial refunds up to the amount of the original charge.

## Disputes

Buyers can dispute TWINT transactions by filing a complaint with their bank. TWINT disputes are rare, with 25-50 disputes recorded for every 1,000,000 transactions.

## Billing

[Stripe Billing](https://stripe.com/billing) supports TWINT payments for both [invoices](https://docs.stripe.com/invoicing/payment-methods.md) and [subscriptions](https://docs.stripe.com/billing/subscriptions/twint.md).

## Connect

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with TWINT to process payments on behalf of a connected account. Connect users can use TWINT with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

### Enable TWINT for connected accounts that use the Stripe Dashboard

Connected accounts that use the Stripe Dashboard can enable TWINT in their [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard. To check which accounts have enabled TWINT, use the `capabilities` hash in our [accounts webhooks or APIs](https://docs.stripe.com/api/accounts/object.md#account_object-capabilities-twint_payments) to see if the `twint_payments` capability is set to `active`.

### Enable TWINT for connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe

Follow the instructions to [enable payment methods for your connected accounts](https://docs.stripe.com/connect/account-capabilities.md). The name of your connected account is the name customers see during checkout and in the TWINT app.
