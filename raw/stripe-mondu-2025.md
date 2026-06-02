<!-- Source URL: https://docs.stripe.com/payments/mondu -->
<!-- Fetched: 2026-05-06 -->

# Mondu payments

Let your business customers pay in 30 days, while you get paid upfront.

[Mondu](https://www.mondu.ai/) is a European company offering innovative payment solutions for B2B commerce. It lets businesses and marketplaces offer their customers invoice payment with 30 days of net terms. Customers that select Mondu are redirected to Mondu’s site for a credit check, and return to your website to complete the order. You get paid immediately.

#### Payment method properties

- **Customer locations**

  EU, UK

- **Presentment currencies**

  EUR, CHF, GBP

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

  [ Yes ](https://docs.stripe.com/payments/mondu.md#disputed-payments)

- **Manual capture support**

  [ Yes ](https://docs.stripe.com/payments/mondu/accept-a-payment.md)

- **Refunds / Partial refunds**

  [ Yes ](https://docs.stripe.com/payments/mondu.md#refunds) / [ Yes ](https://docs.stripe.com/payments/mondu.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept Mondu payments that settle in a [supported currency](https://docs.stripe.com/payments/mondu.md#supported-currencies).

- AT
- BE
- CH
- DE
- DK
- ES
- FI
- FR
- GB
- IT
- NL
- NO
- PL
- SE

#### Product support

- Payment Links
- Checkout1
- Elements2

1Not supported when using Checkout in subscription mode or setup mode.

2Express Checkout Element doesn’t support Mondu.

## Payment flow

Below is a demonstration of the Mondu payment flow from your checkout page:
![](https://d37ugbyn3rpeym.cloudfront.net/videos/mondu_checkout_demo.mp4)

## Get started

You don’t have to integrate Mondu and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Mondu. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Mondu from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)

If your integration requires manually listing payment methods, learn how to [ configure Mondu](https://docs.stripe.com/payments/mondu/accept-a-payment.md).

## Payment options

The maximum charge limit is 19,999,99 EUR or the equivalent for other supported currencies.

## Prohibited and restricted business categories

In addition to the categories of goods or services sold and businesses [restricted from using Stripe overall](https://stripe.com/restricted-businesses), the following categories are prohibited from using Mondu:

- A/C, Refrigeration Repair
- Airlines, Air Carriers
- Airports, Flying Fields
- Ambulance Services
- Antique Reproductions
- Aquariums
- Auto Body Repair Shops
- Auto Paint Shops
- Automobile Associations
- Bail and Bond Payments
- Betting/Casino Gambling
- Billiard/Pool Establishments
- Boat Dealers
- Boat Rentals and Leases
- Bowling Alleys
- Bus Lines
- Buying/Shopping Services
- Cable, Satellite, and Other Pay Television and Radio
- Camera and Photographic Supply Stores
- Car Washes
- Car and Truck Dealers (Used Only)
- Carpet/Upholstery Cleaning
- Chemicals and Allied Products (Not Elsewhere Classified)
- Chiropodists, Podiatrists
- Cigar Stores and Stands
- Cleaning and Maintenance
- Clothing Rental
- Commuter Transport, Ferries
- Computer Network Services
- Concrete Work Services
- Courier Services
- Court Costs
- Credit Reporting Agencies
- Cruise Lines
- Detective Agencies
- Direct Marketing - Catalog Merchant
- Direct Marketing - Combination Catalog and Retail Merchant
- Adult Content and Services
- Direct Marketing - Insurance Services
- Direct Marketing - Subscription
- Direct Marketing - Travel
- Door-To-Door Sales
- Drug Stores and Pharmacies
- Drugs, Drug Proprietaries, and Druggist Sundries
- Electric Vehicle Charging
- Electrical Services
- Emergency Services (GCAS)
- Equipment Rental
- Exterminating Services
- Fines - Government Administrative Entities
- Fuel Dealers (Non Automotive)
- Funeral Services, Crematories
- Furriers and Fur Shops
- Gift, Card, Novelty, and Souvenir Shops
- Government Licensed On-line Casinos (On-Line Gambling)
- Government Services (Not Elsewhere Classified)
- Government-Licensed Horse/Dog Racing
- Government-Owned Lotteries (Non-US region)
- Government-Owned Lotteries (US Region only)
- Information Retrieval Services
- Intra-Company Purchases
- Landscaping Services
- Laundries
- Laundry, Cleaning Services
- Miscellaneous Auto Dealers
- Miscellaneous Repair Shops
- Mobile Home Dealers
- Motion Picture Theaters
- Motor Freight Carriers and Trucking
- Motor Homes Dealers
- Motor Vehicle Supplies and New Parts
- Motorcycle Shops and Dealers
- Motorcycle Shops, Dealers
- Cryptocurrency exchanges and wallets
- Non-FI, Stored Value Card Purchase/Load
- Nursing/Personal Care
- Opticians, Eyeglasses
- Optometrists, Ophthalmologist
- Orthopedic Goods - Prosthetic Devices
- Osteopaths
- Parking Lots, Garages
- Passenger Railways
- Pawn Shops
- Petroleum and Petroleum Products
- Photo Developing
- Political Organizations
- Quick Copy, Repro, and Blueprint
- Railroads
- Recreational Vehicle Rentals
- Religious Goods Stores
- Shoe Repair/Hat Cleaning
- Small Appliance Repair
- Snowmobile Dealers
- Sports Clubs/Fields
- Stamp and Coin Stores
- TUI Travel - Germany
- Tailors, Alterations
- Taxicabs/Limousines
- Telecommunication Services
- Telegraph Services
- Timeshares
- Tire Retreading and Repair
- Tolls/Bridge Fees
- Towing Services
- Trailer Parks, Campgrounds
- Truck/Utility Trailer Rentals
- Typesetting, Plate Making, and Related Services
- Utilities
- Video Game Arcades
- Video Tape Rental Stores
- Watch/Jewelry Repair
- Other categories at the discretion of Mondu

## Disputes

Mondu has a claims process that allows transaction disputes. Customers can open disputes for cases of suspected fraud, double payments, or a difference between an order and a transaction amount.

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to receive [webhooks](https://docs.stripe.com/webhooks.md))

Stripe holds back the disputed amount from your balance until Mondu resolves the dispute.

We request that you upload compelling evidence proving that you fulfilled the purchase order [using the Stripe Dashboard](https://docs.stripe.com/disputes/responding.md#respond). This evidence can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or proof of receipt
- Record of refund (for purchase you’ve already refunded)

To handle disputes programmatically, [respond to disputes using the API](https://docs.stripe.com/disputes/api.md).

This information helps Mondu determine if a dispute is valid. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 12 calendar days. If Mondu resolves the dispute with you winning, we return the disputed amount to your Stripe balance. If Mondu rules in favor of the customer, the disputed amount stays with the customer.

## Refunds

Mondu supports full and partial refunds.

- The refund period is up to 180 days after the purchase.
- Refunds for Mondu payments are asynchronous and take up to 5 minutes to complete.

Stripe notifies you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. If a refund fails (the `Refund` object’s status transitions to `failed`), then we return the amount to your Stripe balance, and you must arrange an alternative way of providing your customer with a refund.

## Supported currencies

You can create Mondu payments in the currencies that map to your country. The default local currency for Mondu is `eur`.

- eur: DE, NL, FR, FI, AT, IT, ES, BE, PL, NO, DK, SE, CH
- chf: CH
- gbp: GB
