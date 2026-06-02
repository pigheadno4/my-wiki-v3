<!-- Source URL: https://docs.stripe.com/payments/sequra -->
<!-- Fetched: 2026-05-06 -->

# SeQura payments

Offer customers the ability to pay when they want while getting paid instantly.

[SeQura](https://www.sequra.com/) allows customers in Southern Europe the ability to pay in 3 interest-free or up to 12 installments total.

#### Payment method properties

- **Customer locations**

  EU

- **Presentment currencies**

  EUR

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

  [ Yes ](https://docs.stripe.com/payments/sequra.md#disputed-payments)

- **Manual capture support**

  [ Yes ](https://docs.stripe.com/payments/sequra/accept-a-payment.md)

- **Refunds / Partial refunds**

  [ Yes ](https://docs.stripe.com/payments/sequra.md#refunds) / [ Yes ](https://docs.stripe.com/payments/sequra.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept SeQura payments that settle in a [supported currency](https://docs.stripe.com/payments/sequra.md#supported-currencies).

- ES

#### Product support

- Payment Links
- Checkout1
- Elements2

1Not supported when using Checkout in subscription mode or setup mode.

2Express Checkout Element doesn’t support SeQura.

## Payment flow

Below is a demonstration of the SeQura payment flow from your checkout page:
![](https://d37ugbyn3rpeym.cloudfront.net/videos/sequra_checkout_demo.mp4)

## Get started

You don’t have to integrate SeQura and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable SeQura. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add SeQura from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)

If your integration requires manually listing payment methods, learn how to [ configure SeQura](https://docs.stripe.com/payments/sequra/accept-a-payment.md).

## Payment options

The minimum charge limit is 29,00 EUR or the equivalent for other supported currencies.

## Prohibited and restricted business categories

In addition to the categories of goods or services sold and businesses [restricted from using Stripe overall](https://stripe.com/restricted-businesses), the following categories are prohibited from using SeQura:

- A/C, Refrigeration Repair
- Accounting/Bookkeeping Services
- Advertising Services
- Agricultural Cooperative
- Airlines, Air Carriers
- Airports, Flying Fields
- Ambulance Services
- Architectural/Surveying Services
- Automobile Associations
- Bail and Bond Payments
- Bakeries
- Bands, Orchestras
- Barber and Beauty Shops
- Betting/Casino Gambling
- Billiard/Pool Establishments
- Boat Dealers
- Boat Rentals and Leases
- Books, Periodicals, and Newspapers
- Bowling Alleys
- Business/Secretarial Schools
- Buying/Shopping Services
- Cable, Satellite, and Other Pay Television and Radio
- Candy, Nut, and Confectionery Stores
- Car Rental Agencies
- Car Washes
- Car and Truck Dealers (New & Used)
- Car and Truck Dealers (Used Only)
- Carpentry Services
- Carpet/Upholstery Cleaning
- Caterers
- Charitable and Social Service Organizations - Fundraising
- Chemicals and Allied Products (Not Elsewhere Classified)
- Child Care Services
- Chiropodists, Podiatrists
- Chiropractors
- Cigar Stores and Stands
- Civic, Social, Fraternal Associations
- Cleaning and Maintenance
- Clothing Rental
- Colleges, Universities
- Commercial Equipment (Not Elsewhere Classified)
- Commercial Footwear
- Commercial Photography, Art and Graphics
- Commuter Transport, Ferries
- Computer Network Services
- Computer Programming
- Computer Repair
- Concrete Work Services
- Construction Materials (Not Elsewhere Classified)
- Consulting, Public Relations
- Correspondence Schools
- Counseling Services
- Country Clubs
- Courier Services
- Court Costs
- Credit Reporting Agencies
- Dairy Products Stores
- Dance Hall, Studios, Schools
- Dentists, Orthodontists
- Detective Agencies
- Digital Goods Media – Books, Movies, Music
- Digital Goods – Applications (Excludes Games)
- Digital Goods – Games
- Digital Goods – Large Digital Goods Merchant
- Adult Content and Services
- Direct Marketing - Insurance Services
- Direct Marketing - Other
- Direct Marketing - Outbound Telemarketing
- Direct Marketing - Subscription
- Direct Marketing - Travel
- Doctors
- Door-To-Door Sales
- Drinking Places
- Drugs, Drug Proprietaries, and Druggist Sundries
- Dry Cleaners
- Eating Places, Restaurants
- Electric Vehicle Charging
- Electrical Parts and Equipment
- Electrical Services
- Electronics Repair Shops
- Elementary, Secondary Schools
- Employment/Temp Agencies
- Equipment Rental
- Exterminating Services
- Fast Food Restaurants
- Financial Institutions
- Fines - Government Administrative Entities
- Freezer and Locker Meat Provisioners
- Fuel Dealers (Non Automotive)
- Funeral Services, Crematories
- Furniture Repair, Refinishing
- General Services
- Government Licensed On-line Casinos (On-Line Gambling)
- Government Services (Not Elsewhere Classified)
- Government-Licensed Horse/Dog Racing
- Government-Owned Lotteries (Non-US region)
- Government-Owned Lotteries (US Region only)
- Grocery Stores, Supermarkets
- Heating, Plumbing, A/C
- Hospitals
- Hotels, Motels, and Resorts
- Industrial Supplies (Not Elsewhere Classified)
- Information Retrieval Services
- Insurance Underwriting, Premiums
- Intra-Company Purchases
- Landscaping Services
- Laundries
- Laundry, Cleaning Services
- Legal Services, Attorneys
- Marinas, Service and Supplies
- Marketplaces
- Masonry, Stonework, and Plaster
- Massage Parlors
- Medical Services
- Medical and Dental Labs
- Medical, Dental, Ophthalmic, and Hospital Equipment and Supplies
- Membership Organizations
- Metal Service Centers
- Miscellaneous Business Services
- Miscellaneous Food Stores
- Miscellaneous General Services
- Miscellaneous Publishing and Printing
- Miscellaneous Recreation Services
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
- Nondurable Goods (Not Elsewhere Classified)
- Nursing/Personal Care
- Office and Commercial Furniture
- Opticians, Eyeglasses
- Optometrists, Ophthalmologist
- Osteopaths
- Package Stores-Beer, Wine, and Liquor
- Paints, Varnishes, and Supplies
- Parking Lots, Garages
- Pawn Shops
- Petroleum and Petroleum Products
- Photo Developing
- Photographic, Photocopy, Microfilm Equipment, and Supplies
- Picture/Video Production
- Piece Goods, Notions, and Other Dry Goods
- Plumbing, Heating Equipment, and Supplies
- Political Organizations
- Precious Stones and Metals, Watches and Jewelry
- Professional Services
- Public Warehousing and Storage
- Quick Copy, Repro, and Blueprint
- Railroads
- Real Estate Agents and Managers - Rentals
- Recreational Vehicle Rentals
- Religious Organizations
- Roofing/Siding, Sheet Metal
- Secretarial Support Services
- Security Brokers/Dealers
- Shoe Repair/Hat Cleaning
- Small Appliance Repair
- Snowmobile Dealers
- Special Trade Services
- Specialty Cleaning
- Sporting/Recreation Camps
- Sports Clubs/Fields
- Stationery, Office Supplies, Printing and Writing Paper
- TUI Travel - Germany
- Tailors, Alterations
- Tax Preparation Services
- Taxicabs/Limousines
- Telecommunication Equipment and Telephone Sales
- Telecommunication Services
- Telegraph Services
- Testing Laboratories
- Theatrical Ticket Agencies
- Timeshares
- Tolls/Bridge Fees
- Towing Services
- Trailer Parks, Campgrounds
- Travel Agencies, Tour Operators
- Truck/Utility Trailer Rentals
- Typesetting, Plate Making, and Related Services
- Typewriter Stores
- Miscellaneous Business Services
- Utilities
- Video Amusement Game Supplies
- Video Game Arcades
- Video Tape Rental Stores
- Vocational/Trade Schools
- Watch/Jewelry Repair
- Welding Repair
- Other categories at the discretion of SeQura

## Disputes

SeQura has a claims process that allows transaction disputes. Customers can open disputes for cases of suspected fraud, double payments, or a difference between an order and a transaction amount.

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to receive [webhooks](https://docs.stripe.com/webhooks.md))

Stripe holds back the disputed amount from your balance until SeQura resolves the dispute.

We request that you upload compelling evidence proving that you fulfilled the purchase order [using the Stripe Dashboard](https://docs.stripe.com/disputes/responding.md#respond). This evidence can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or proof of receipt
- Record of refund (for purchase you’ve already refunded)

To handle disputes programmatically, [respond to disputes using the API](https://docs.stripe.com/disputes/api.md).

This information helps SeQura determine if a dispute is valid. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 12 calendar days. If SeQura resolves the dispute with you winning, we return the disputed amount to your Stripe balance. If SeQura rules in favor of the customer, the disputed amount stays with the customer.

## Refunds

SeQura supports full and partial refunds.

- The refund period is up to 180 days after the purchase.
- Refunds for SeQura payments are asynchronous and take up to 5 minutes to complete.

Stripe notifies you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. If a refund fails (the `Refund` object’s status transitions to `failed`), then we return the amount to your Stripe balance, and you must arrange an alternative way of providing your customer with a refund.

## Supported currencies

You can create SeQura payments in the currencies that map to your country. The default local currency for SeQura is `eur`.

- eur: ES
