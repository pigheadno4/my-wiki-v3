<!-- Source URL: https://docs.stripe.com/payments/sunbit -->
<!-- Fetched: 2026-05-06 -->

# Sunbit payments

Offer customers the ability to pay in 3, 6, 12, 18 (or more) monthly installments while getting paid instantly.

[Sunbit](https://sunbit.com/) is a buy now, pay later payment method available in the US that gives your customers the flexibility to choose the number of monthly installments they want to use for payment. When customers select Sunbit as their payment method, Stripe redirects them to Sunbit’s website, where they can choose between 3, 6, 12, or 18-month flexible payment plans to complete their purchase. You get paid up front. Sunbit handles the customer’s payments and collections.

#### Payment method properties

- **Customer locations**

  US

- **Presentment currencies**

  USD

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Buy Now, Pay Later

- **Recurring payments**

  No

- **Payout timing**

  Standard

- **Connect support**

  Yes

- **Dispute support**

  [ Yes ](https://docs.stripe.com/payments/sunbit.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [ Yes ](https://docs.stripe.com/payments/sunbit.md#refunds) / [ Yes ](https://docs.stripe.com/payments/sunbit.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept Sunbit payments that settle in a [supported currency](https://docs.stripe.com/payments/sunbit.md#supported-currencies).

- US

#### Product support

- Connect
- Payment Links
- [Checkout](https://docs.stripe.com/payments/sunbit/accept-a-payment.md?payment-ui=checkout)1
- [Elements](https://docs.stripe.com/payments/sunbit/accept-a-payment.md?payment-ui=elements&api-integration=checkout)2

1Not supported when using Checkout in [subscription mode or setup mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode).

2Express Checkout Element doesn’t support Sunbit.

## Payment flow

Below is a demonstration of the Sunbit payment flow from your checkout page:
![](https://d37ugbyn3rpeym.cloudfront.net/videos/sunbit_demo.mp4)

## Get started

You don’t have to integrate Sunbit and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Sunbit. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Sunbit from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)

If your integration requires manually listing payment methods, learn how to [ configure Sunbit](https://docs.stripe.com/payments/sunbit/accept-a-payment.md).

## Payment options

The minimum charge limit is 60.00 USD or the equivalent for other supported currencies.

The maximum charge limit is 19,999.99 USD or the equivalent for other supported currencies.

## Prohibited and restricted business categories

In addition to the categories of goods or services sold and businesses [restricted from using Stripe overall](https://stripe.com/restricted-businesses), the following categories are prohibited from using Sunbit:

- Accounting/Bookkeeping Services
- Advertising Services
- Agricultural Cooperative
- Airlines, Air Carriers
- Airports, Flying Fields
- Ambulance Services
- Amusement Parks/Carnivals
- Antique Reproductions
- Antique Shops
- Aquariums
- Architectural/Surveying Services
- Art Dealers and Galleries
- Artists Supply and Craft Shops
- Automated Fuel Dispensers
- Automobile Associations
- Bail and Bond Payments
- Bakeries
- Bands, Orchestras
- Betting/Casino Gambling
- Billiard/Pool Establishments
- Boat Rentals and Leases
- Book Stores
- Books, Periodicals, and Newspapers
- Bowling Alleys
- Bus Lines
- Business/Secretarial Schools
- Buying/Shopping Services
- Cable, Satellite, and Other Pay Television and Radio
- Camera and Photographic Supply Stores
- Candy, Nut, and Confectionery Stores
- Car Rental Agencies
- Car Washes
- Caterers
- Charitable and Social Service Organizations - Fundraising
- Chemicals and Allied Products (Not Elsewhere Classified)
- Child Care Services
- Childrens and Infants Wear Stores
- Cigar Stores and Stands
- Civic, Social, Fraternal Associations
- Clothing Rental
- Colleges, Universities
- Commercial Equipment (Not Elsewhere Classified)
- Commercial Footwear
- Commercial Photography, Art and Graphics
- Commuter Transport, Ferries
- Computer Network Services
- Computer Programming
- Computer Repair
- Computers, Peripherals, and Software
- Construction Materials (Not Elsewhere Classified)
- Consulting, Public Relations
- Correspondence Schools
- Courier Services
- Court Costs
- Credit Reporting Agencies
- Cruise Lines
- Dairy Products Stores
- Dance Hall, Studios, Schools
- Department Stores
- Detective Agencies
- Digital Goods Media – Books, Movies, Music
- Digital Goods – Applications (Excludes Games)
- Digital Goods – Games
- Digital Goods – Large Digital Goods Merchant
- Direct Marketing - Catalog Merchant
- Direct Marketing - Combination Catalog and Retail Merchant
- Adult Content and Services
- Direct Marketing - Insurance Services
- Direct Marketing - Other
- Direct Marketing - Outbound Telemarketing
- Direct Marketing - Subscription
- Direct Marketing - Travel
- Discount Stores
- Door-To-Door Sales
- Drinking Places
- Drug Stores and Pharmacies
- Drugs, Drug Proprietaries, and Druggist Sundries
- Dry Cleaners
- Durable Goods (Not Elsewhere Classified)
- Duty Free Stores
- Eating Places, Restaurants
- Educational Services
- Electric Razor Stores
- Electric Vehicle Charging
- Electrical Parts and Equipment
- Electronics Stores
- Elementary, Secondary Schools
- Emergency Services (GCAS)
- Employment/Temp Agencies
- Equipment Rental
- Family Clothing Stores
- Fast Food Restaurants
- Financial Institutions
- Fines - Government Administrative Entities
- Florists
- Florists Supplies, Nursery Stock, and Flowers
- Freezer and Locker Meat Provisioners
- Fuel Dealers (Non Automotive)
- Funeral Services, Crematories
- Furriers and Fur Shops
- Gift, Card, Novelty, and Souvenir Shops
- Glassware, Crystal Stores
- Golf Courses - Public
- Government Licensed On-line Casinos (On-Line Gambling)
- Government Services (Not Elsewhere Classified)
- Government-Licensed Horse/Dog Racing
- Government-Owned Lotteries (Non-US region)
- Government-Owned Lotteries (US Region only)
- Grocery Stores, Supermarkets
- Hobby, Toy, and Game Shops
- Hotels, Motels, and Resorts
- Industrial Supplies (Not Elsewhere Classified)
- Information Retrieval Services
- Insurance Underwriting, Premiums
- Intra-Company Purchases
- Jewelry Stores, Watches, Clocks, and Silverware Stores
- Laundries
- Luggage and Leather Goods Stores
- Lumber, Building Materials Stores
- Marketplaces
- Masonry, Stonework, and Plaster
- Medical, Dental, Ophthalmic, and Hospital Equipment and Supplies
- Membership Organizations
- Mens and Boys Clothing and Accessories Stores
- Mens, Womens Clothing Stores
- Metal Service Centers
- Miscellaneous Apparel and Accessory Shops
- Miscellaneous Business Services
- Miscellaneous Food Stores
- Miscellaneous General Merchandise
- Miscellaneous Home Furnishing Specialty Stores
- Miscellaneous Publishing and Printing
- Miscellaneous Recreation Services
- Mobile Home Dealers
- Motion Picture Theaters
- Motor Freight Carriers and Trucking
- Music Stores-Musical Instruments, Pianos, and Sheet Music
- News Dealers and Newsstands
- Cryptocurrency exchanges and wallets
- Non-FI, Stored Value Card Purchase/Load
- Nondurable Goods (Not Elsewhere Classified)
- Office and Commercial Furniture
- Package Stores-Beer, Wine, and Liquor
- Paints, Varnishes, and Supplies
- Parking Lots, Garages
- Passenger Railways
- Pawn Shops
- Pet Shops, Pet Food, and Supplies
- Petroleum and Petroleum Products
- Photo Developing
- Photographic Studios
- Photographic, Photocopy, Microfilm Equipment, and Supplies
- Picture/Video Production
- Piece Goods, Notions, and Other Dry Goods
- Political Organizations
- Postal Services - Government Only
- Precious Stones and Metals, Watches and Jewelry
- Public Warehousing and Storage
- Quick Copy, Repro, and Blueprint
- Railroads
- Real Estate Agents and Managers - Rentals
- Record Stores
- Recreational Vehicle Rentals
- Religious Goods Stores
- Religious Organizations
- Secretarial Support Services
- Security Brokers/Dealers
- Service Stations
- Sewing, Needlework, Fabric, and Piece Goods Stores
- Shoe Repair/Hat Cleaning
- Shoe Stores
- Specialty Cleaning
- Sporting Goods Stores
- Sporting/Recreation Camps
- Sports Clubs/Fields
- Stamp and Coin Stores
- Stationery, Office Supplies, Printing and Writing Paper
- Stationery Stores, Office, and School Supply Stores
- TUI Travel - Germany
- Tailors, Alterations
- Tax Payments - Government Agencies
- Tax Preparation Services
- Taxicabs/Limousines
- Telecommunication Equipment and Telephone Sales
- Telecommunication Services
- Telegraph Services
- Tent and Awning Shops
- Testing Laboratories
- Theatrical Ticket Agencies
- Timeshares
- Tolls/Bridge Fees
- Tourist Attractions and Exhibits
- Trailer Parks, Campgrounds
- Transportation Services (Not Elsewhere Classified)
- Travel Agencies, Tour Operators
- Truck Stops
- Truck/Utility Trailer Rentals
- Typesetting, Plate Making, and Related Services
- Typewriter Stores
- Tent and Awning Shops
- Wig and Toupee Stores
- Variety Stores
- Utilities
- Video Amusement Game Supplies
- Video Game Arcades
- Video Tape Rental Stores
- Vocational/Trade Schools
- Watch/Jewelry Repair
- Welding Repair
- Wholesale Clubs
- Wig and Toupee Stores
- Used Merchandise and Secondhand Stores
- Other categories at the discretion of Sunbit

## Additional requirements

You acknowledge that:

- Sunbit (and/or its partner bank) decides if customers can use Sunbit for purchases and has the sole right to receive payment from Sunbit customers. Stripe acquires those purchases for you and settles the funds to you.
- Customers must complete their own applications and review all terms related to your goods and services and the use of Sunbit.
- You can’t impose fees or higher prices for Sunbit purchases (that is, no surcharging).
- The amount financed including any down payment entered on the customer application for Sunbit purchases must be equal to or less than the price of goods/services delivered/rendered to the customer.

## Disputes

Sunbit has a claims process that allows transaction disputes. Customers can open disputes for cases of suspected fraud, double payments, or a difference between an order and a transaction amount.

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to receive [webhooks](https://docs.stripe.com/webhooks.md))

Stripe holds back the disputed amount from your balance until Sunbit resolves the dispute.

We request that you upload compelling evidence proving that you fulfilled the purchase order [using the Stripe Dashboard](https://docs.stripe.com/disputes/responding.md#respond). This evidence can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or proof of receipt
- Record of refund (for purchase you’ve already refunded)

To handle disputes programmatically, [respond to disputes using the API](https://docs.stripe.com/disputes/api.md).

This information helps Sunbit determine if a dispute is valid. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 12 calendar days. If Sunbit resolves the dispute with you winning, we return the disputed amount to your Stripe balance. If Sunbit rules in favor of the customer, the disputed amount stays with the customer.

## Refunds

Sunbit supports full and partial refunds.

- The refund period is up to 180 days after the purchase.
- Refunds for Sunbit payments are asynchronous and take up to 5 minutes to complete.

Stripe notifies you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. If a refund fails (the `Refund` object’s status transitions to `failed`), then we return the amount to your Stripe balance, and you must arrange an alternative way of providing your customer with a refund.

## Connect

If you use *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), you must consider the following before you enable and use Sunbit.

### Request Sunbit capabilities for your connected accounts

Set the `sunbit_payments` capability to `active` on your platform account, and on any connected accounts you want to enable Sunbit for. You can also [request more account capabilities](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the default statement descriptor and the merchant name that appears on the customer’s banking application and confirmation emails.

| Charge type                                        | Descriptor taken from |
| -------------------------------------------------- | --------------------- |
| Direct                                             | Connected account     |
| Destination                                        | Platform              |
| Separate charge and transfer                       | Platform              |
| Destination (with `on_behalf_of`)                  | Connected account     |
| Separate charge and transfer (with `on_behalf_of`) | Connected account     |

To check or update your statement descriptor, go to your [account settings](https://docs.stripe.com/get-started/account/statement-descriptors.md). For Connect integrations, see [setting statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

## Supported currencies

You can create Sunbit payments in the currencies that map to your country. The default local currency for Sunbit is `usd`.

- usd: US
