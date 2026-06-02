<!-- Source URL: https://docs.stripe.com/payments/kriya -->
<!-- Fetched: 2026-05-06 -->

# Kriya payments

Offer businesses flexible payment terms while getting paid instantly.

[Kriya](https://www.kriya.co/) provides flexible payment terms for businesses to buy what they need now and pay for it later.

#### Payment method properties

- **Customer locations**

  UK

- **Presentment currencies**

  GBP

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Buy Now, Pay Later

- **Recurring payments**

  No

- **Payout timing**

  Standard

- **Connect support**

  No

- **Dispute support**

  [ Yes ](https://docs.stripe.com/payments/kriya.md#disputed-payments)

- **Manual capture support**

  [ Yes ](https://docs.stripe.com/payments/kriya/accept-a-payment.md)

- **Refunds / Partial refunds**

  [ Yes ](https://docs.stripe.com/payments/kriya.md#refunds) / [ Yes ](https://docs.stripe.com/payments/kriya.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept Kriya payments that settle in a [supported currency](https://docs.stripe.com/payments/kriya.md#supported-currencies).

- GB

#### Product support

- Payment Links
- Checkout1
- Elements2

1Not supported when using Checkout in subscription mode or setup mode.

2Express Checkout Element doesn’t support Kriya.

## Payment flow

Below is a demonstration of the Kriya payment flow from your checkout page:
![](https://d37ugbyn3rpeym.cloudfront.net/videos/kriya_checkout_demo.mp4)

## Get started

You don’t have to integrate Kriya and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Kriya. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Kriya from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)

If your integration requires manually listing payment methods, learn how to [ configure Kriya](https://docs.stripe.com/payments/kriya/accept-a-payment.md).

## Prohibited and restricted business categories

In addition to the categories of goods or services sold and businesses [restricted from using Stripe overall](https://stripe.com/restricted-businesses), the following categories are prohibited from using Kriya:

- Advertising Services
- Airlines, Air Carriers
- Betting/Casino Gambling
- Car Rental Agencies
- Charitable and Social Service Organizations - Fundraising
- Cigar Stores and Stands
- Civic, Social, Fraternal Associations
- Country Clubs
- Courier Services
- Cruise Lines
- Adult Content and Services
- Direct Marketing - Other
- Direct Marketing - Outbound Telemarketing
- Drug Stores and Pharmacies
- Drugs, Drug Proprietaries, and Druggist Sundries
- Financial Institutions
- Government Licensed On-line Casinos (On-Line Gambling)
- Government-Licensed Horse/Dog Racing
- Government-Owned Lotteries (US Region only)
- Heating, Plumbing, A/C
- Hotels, Motels, and Resorts
- Insurance Underwriting, Premiums
- Massage Parlors
- Membership Organizations
- Miscellaneous General Services
- Cryptocurrency exchanges and wallets
- Non-FI, Stored Value Card Purchase/Load
- Pawn Shops
- Petroleum and Petroleum Products
- Political Organizations
- Religious Organizations
- Security Brokers/Dealers
- Special Trade Services
- Sporting/Recreation Camps
- TUI Travel - Germany
- Timeshares
- Trailer Parks, Campgrounds
- Travel Agencies, Tour Operators
- Video Amusement Game Supplies
- Video Game Arcades
- Other categories at the discretion of Kriya

## Disputes

Kriya has a claims process that allows transaction disputes. Customers can open disputes for cases of suspected fraud, double payments, or a difference between an order and a transaction amount.

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to receive [webhooks](https://docs.stripe.com/webhooks.md))

Stripe holds back the disputed amount from your balance until Kriya resolves the dispute.

We request that you upload compelling evidence proving that you fulfilled the purchase order [using the Stripe Dashboard](https://docs.stripe.com/disputes/responding.md#respond). This evidence can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or proof of receipt
- Record of refund (for purchase you’ve already refunded)

To handle disputes programmatically, [respond to disputes using the API](https://docs.stripe.com/disputes/api.md).

This information helps Kriya determine if a dispute is valid. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 12 calendar days. If Kriya resolves the dispute with you winning, we return the disputed amount to your Stripe balance. If Kriya rules in favor of the customer, the disputed amount stays with the customer.

## Refunds

Kriya supports full and partial refunds.

- The refund period is up to 180 days after the purchase.
- Refunds for Kriya payments are asynchronous and take up to 5 minutes to complete.

Stripe notifies you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. If a refund fails (the `Refund` object’s status transitions to `failed`), then we return the amount to your Stripe balance, and you must arrange an alternative way of providing your customer with a refund.

## Supported currencies

You can create Kriya payments in the currencies that map to your country. The default local currency for Kriya is `gbp`.

- gbp: GB
