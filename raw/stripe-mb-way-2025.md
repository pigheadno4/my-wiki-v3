<!-- Source URL: https://docs.stripe.com/payments/mb-way -->
<!-- Fetched: 2026-05-07 -->

# MB WAY payments

Learn about MB WAY, a digital wallet payment method in Portugal.

MB WAY is a digital wallet payment method in Portugal. When paying with MB WAY, customers initiate payments using their phone number, and [authenticate and approve](https://docs.stripe.com/payments/payment-methods.md#customer-actions) them using their MB WAY app.

You get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) of whether the payment succeeded or failed.

> MB WAY supports international phone numbers, but the majority of customers use a Portuguese phone number starting with +351. You can test your integration in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) using [test phone numbers](https://docs.stripe.com/payments/mb-way/accept-a-payment.md#web-test-integration).

#### Payment method properties

- **Customer locations**

  Portugal

- **Presentment currency**

  EUR

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Wallet

- **Recurring payments**

  No

- **Payout timing**

  [Standard payout timing](https://docs.stripe.com/payouts.md#payout-speed) applies

- **Connect support**

  [Yes](https://docs.stripe.com/payments/mb-way.md#connect)

- **Dispute support**

  [Yes](https://docs.stripe.com/payments/mb-way.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  Yes / Yes

#### Business locations

Stripe accounts in the following countries can accept MB WAY payments:

- AT
- AU
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
- HK
- HR
- HU
- IE
- IT
- JP
- LI
- LT
- LU
- LV
- MT
- MX
- NL
- NO
- NZ
- PL
- PT
- RO
- SE
- SG
- SI
- SK
- US

#### Product support

- Connect
- Checkout1

- Payment Links
- Elements2

1Not supported when using Checkout in subscription mode, in setup mode, or when saving payment details during payment (`setup_future_usage`).2The Mobile Payment element doesn’t support MB WAY.

## Payment flows

Customers pay with MB WAY using a phone number linked to their MB WAY app. After providing their phone number, customers receive a push notification in their MB WAY app, authorize the payment, then return to your website.

Transaction amounts between 0.50 EUR and 5,000 EUR are supported on MB WAY. MB WAY users have a default daily cumulative limit of 1,000 EUR, which they can adjust up to 10,000 EUR in the MB WAY app.

Here’s a demo of the MB WAY payment process using your checkout page and the MB WAY app.
![](https://docs.stripecdn.com/6054002730f3bf541e64bb7c496657b5c391dea32622e9b69fe052dda2b1a4a3.mp4)

## Get started

Learn how to [configure MB WAY as a payment method](https://docs.stripe.com/payments/mb-way/accept-a-payment.md).

You don’t have to integrate MB WAY and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable MB WAY. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add MB WAY from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)

## Disputes

MB WAY has a claims process that allows transaction disputes. Customers can open disputes for cases of suspected fraud, double payments, or a difference between an order and a transaction amount.

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to receive [webhooks](https://docs.stripe.com/webhooks.md))

Stripe holds back the disputed amount from your balance until MB WAY resolves the dispute.

We request that you upload compelling evidence proving that you fulfilled the purchase order [using the Stripe Dashboard](https://docs.stripe.com/disputes/responding.md#respond). This evidence can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or proof of receipt
- Record of refund (for purchase you’ve already refunded)

To handle disputes programmatically, respond to disputes using the API.

This information helps MB WAY determine if a dispute is valid. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 7 calendar days. If MB WAY resolves the dispute with you winning, we return the disputed amount to your Stripe balance. If MB WAY rules in favor of the customer, the balance charge becomes permanent.

## Refunds

You can refund MB WAY charges up to 365 days after the payment completes. Refunds usually take a few minutes to complete. MB WAY supports full and partial refunds. You can also issue multiple partial refunds up to the amount of the original charge.

## Statement descriptors

Customized statement descriptors aren’t supported by MB WAY—the value specified in the [statement_descriptor](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-statement_descriptor) is ignored. Stripe’s company name (`Stripe Inc`) is shown on bank statements along with the transaction amount.

## Connect

A Connect platform can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with MB WAY to process connected account payments of all [charge types](https://docs.stripe.com/connect/charges.md).

### Connected accounts with full Stripe Dashboard access

Connected accounts with access to the full Stripe Dashboard, including Standard accounts, can enable MB WAY through their Dashboard. To check which accounts have enabled MB WAY, use the `capabilities` hash in the [accounts webhooks or APIs](https://docs.stripe.com/api/accounts/object.md#account_object-capabilities-mb_way_payments) to see if the `mb_way_payments` capability is set to `active`.

### Connected accounts without full Stripe Dashboard access

To onboard connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe, request the `mb_way_payments` capability using the [Capabilities API](https://docs.stripe.com/api/capabilities.md). For more details, follow the instructions to [enable payment methods for your connected accounts](https://docs.stripe.com/connect/account-capabilities.md).
