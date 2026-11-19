<!-- Source URL: https://docs.stripe.com/payments/klarna/supplementary-purchase-data -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Klarna supplementary purchase data

Learn how to provide Klarna-specific supplementary data for various industry verticals.

> #### Available with preview header
> 
> You can use this public preview feature by including the version header `2025-11-17.preview` or a later preview version header in your API request.

Supplementary purchase data adds context to a transaction to improve payment outcomes and customer support. Use it to send industry-specific details for verticals such as events, transportation, marketplaces, and insurance.

## When to use supplementary purchase data

Use supplementary purchase data if you operate in a supported vertical and want to improve your payment outcomes with Klarna.

The supplementary data shared with Klarna supports these use cases:

- **Post-purchase transparency**: Provide detailed transaction breakdowns for your customers in the Klarna app, streamline disputes and returns, and reduce support requests.
- **Higher acceptance rates**: Historical data informs underwriting and can increase approvals for legitimate transactions.
- **Enhanced fraud assessment**: Detailed transaction insights support more effective fraud investigations, especially in high-risk segments.
- **Risk exposure monitoring**: Transaction data supports continuous monitoring and timely mitigation.
- **Enhanced solution offerings**: Based on historical behavior, Klarna can develop enhanced solutions for incentives and actions that benefit you and your customers.

### Limitations

Keep these limits in mind:

- **No fee changes**: Passing supplementary purchase data doesn’t impact the fees you pay for Klarna transactions. Your pricing remains the same whether or not you provide this data.
- **No validation feedback**: Stripe and Klarna accept well-formed supplementary purchase data but don’t provide feedback on whether the specific data you send qualifies for improved outcomes.

### Measure impact

Track your Klarna authorization rates over time in your payment analytics. After you implement supplementary purchase data, you might see more successful authorizations, though the impact varies based on your transaction patterns and the data you provide.

## Availability

Supplementary purchase data is available exclusively for Klarna payments and supports the following industry verticals:

- Events (concerts, festivals, sports, conferences)
- Insurance (standalone insurance policies)
- Vouchers (gift cards, discount codes)
- Train transportation
- Bus transportation
- Ferry transportation
- Organized trips and tours
- Marketplace sellers

> #### Travel and entertainment verticals
> 
> For lodging, car rentals, and air transportation with Klarna payments, see the [travel and entertainment industry metadata documentation](https://docs.stripe.com/industry-metadata.md). Those verticals are shared with card payments, while the verticals on this page are Klarna-exclusive.

## Send supplementary purchase data 

You send Klarna-specific supplementary purchase data through the `payment_method_options.klarna.supplementary_purchase_data` parameter when you [create](https://docs.stripe.com/api/payment_intents/create.md), [update](https://docs.stripe.com/api/payment_intents/update.md), or [confirm](https://docs.stripe.com/api/payment_intents/confirm.md) a PaymentIntent.

The `supplementary_purchase_data` hash contains an array of hashes for each vertical. Klarna processes all entries in these arrays for risk assessment. You can send multiple verticals in a single request.

### Example: Create a PaymentIntent with voucher data

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=10000 \
  -d currency=eur \
  -d "automatic_payment_methods[enabled]=true" \
  -d "payment_method_options[klarna][supplementary_purchase_data][vouchers][0][voucher_name]=Holiday Gift Card"
```

### Example: Create a PaymentIntent with multiple verticals

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=15000 \
  -d currency=eur \
  -d "automatic_payment_methods[enabled]=true" \
  -d "payment_method_options[klarna][supplementary_purchase_data][vouchers][0][voucher_name]=Gift Card" \
  -d "payment_method_options[klarna][supplementary_purchase_data][insurances][0][insurance_type]=cancelation" \
  -d "payment_method_options[klarna][supplementary_purchase_data][insurances][0][price]=2000" \
  -d "payment_method_options[klarna][supplementary_purchase_data][insurances][0][currency]=EUR"
```

## Vertical data formats 

The following tabs describe the hashes for the supported verticals:

#### Insurance

Insurance data is sent through the `payment_method_options.klarna.supplementary_purchase_data.insurances` parameter. Each element in the array represents an individual insurance policy purchased as the primary product (not as an add-on to another service).

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-insurances) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with insurance data

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=5000 \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]=true" \
  -d "payment_method_options[klarna][supplementary_purchase_data][insurances][0][insurance_type]=medical" \
  -d "payment_method_options[klarna][supplementary_purchase_data][insurances][0][insurance_company_name]=Global Medical Insurance" \
  -d "payment_method_options[klarna][supplementary_purchase_data][insurances][0][price]=5000" \
  -d "payment_method_options[klarna][supplementary_purchase_data][insurances][0][currency]=USD"
```

#### Vouchers

Voucher data is sent through the `payment_method_options.klarna.supplementary_purchase_data.vouchers` parameter. Each element in the array represents an individual voucher, such as a gift card or discount code.

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-vouchers) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with voucher data

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=10000 \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]=true" \
  -d "payment_method_options[klarna][supplementary_purchase_data][vouchers][0][voucher_name]=Holiday Gift Card 2025" \
  -d "payment_method_options[klarna][supplementary_purchase_data][vouchers][0][voucher_type]=gift_card" \
  -d "payment_method_options[klarna][supplementary_purchase_data][vouchers][0][voucher_company]=Retail Store Inc" \
  -d "payment_method_options[klarna][supplementary_purchase_data][vouchers][0][starts_at]=1735689600" \
  -d "payment_method_options[klarna][supplementary_purchase_data][vouchers][0][ends_at]=1767225600" \
  -d "payment_method_options[klarna][supplementary_purchase_data][vouchers][0][affiliate_name]=Partner Retailer"
```

#### Events

Event data is sent through the `payment_method_options.klarna.supplementary_purchase_data.event_reservation_details` parameter. Each element in the array represents an individual event ticket or reservation.

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-event_reservation_details) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with event data

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=15000 \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]=true" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][event_name]=Summer Music Festival 2025" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][event_company_name]=Stripe Example Entertainment" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][event_type]=festival" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][starts_at]=1751328000" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][ends_at]=1751414400" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][venue_name]=Central Park" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][access_controlled_venue]=true" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][address][street_address]=Central Park West" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][address][city]=New York" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][address][region]=NY" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][address][postal_code]=10024" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][address][country]=US" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][affiliate_name]=Ticketvendor" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][insurances][0][insurance_type]=cancelation" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][insurances][0][insurance_company_name]=Event Insurance Co" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][insurances][0][price]=2000" \
  -d "payment_method_options[klarna][supplementary_purchase_data][event_reservation_details][0][insurances][0][currency]=USD"
```

#### Train

Train reservation data is sent through the `payment_method_options.klarna.supplementary_purchase_data.train_reservation_details` parameter. Each element in the array represents an individual train ticket or reservation.

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-train_reservation_details) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with train data

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=8500 \
  -d currency=eur \
  -d "automatic_payment_methods[enabled]=true" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][carrier_name]=Eurotrains" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][ticket_class]=business" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][price]=8500" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][currency]=EUR" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][departure][departure_location]=Paris Gare du Nord" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][departure][departs_at]=1751324400" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][departure][address][street_address]=18 Rue de Dunkerque" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][departure][address][city]=Paris" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][departure][address][postal_code]=75010" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][departure][address][country]=FR" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][arrival][arrival_location]=London St Pancras International" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][arrival][address][street_address]=Pancras Road" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][arrival][address][city]=London" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][arrival][address][postal_code]=N1C 4QP" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][arrival][address][country]=GB" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][passengers][0][given_name]=Jane" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][passengers][0][family_name]=Smith" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][insurances][0][insurance_type]=cancelation" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][insurances][0][insurance_company_name]=Travel Insurance Ltd" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][insurances][0][price]=1500" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][insurances][0][currency]=EUR" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][affiliate_name]=Rail Travel Partners"
```

#### Bus

Bus reservation data is sent through the `payment_method_options.klarna.supplementary_purchase_data.bus_reservation_details` parameter. Each element in the array represents an individual bus ticket or reservation.

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-bus_reservation_details) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with bus data

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=4500 \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]=true" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][carrier_name]=Fastdog" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][ticket_class]=economy" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][price]=4500" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][currency]=USD" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][departure][departure_location]=New York Port Authority" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][departure][departs_at]=1751356800" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][departure][address][street_address]=625 8th Avenue" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][departure][address][city]=New York" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][departure][address][region]=NY" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][departure][address][postal_code]=10018" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][departure][address][country]=US" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][arrival][arrival_location]=Boston South Station" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][arrival][address][street_address]=700 Atlantic Avenue" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][arrival][address][city]=Boston" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][arrival][address][region]=MA" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][arrival][address][postal_code]=02110" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][arrival][address][country]=US" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][passengers][0][given_name]=John" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][passengers][0][family_name]=Doe" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][insurances][0][insurance_type]=cancelation" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][insurances][0][insurance_company_name]=Bus Travel Insurance" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][insurances][0][price]=500" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][insurances][0][currency]=USD" \
  -d "payment_method_options[klarna][supplementary_purchase_data][bus_reservation_details][0][affiliate_name]=Travel Booking Agency"
```

#### Ferry

Ferry reservation data is sent through the `payment_method_options.klarna.supplementary_purchase_data.ferry_reservation_details` parameter. Each element in the array represents an individual ferry ticket or reservation.

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-ferry_reservation_details) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with ferry data

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=6500 \
  -d currency=eur \
  -d "automatic_payment_methods[enabled]=true" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][carrier_name]=Ferry Line" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][ticket_class]=economy" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][price]=6500" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][currency]=EUR" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][departure][departure_location]=Dover Ferry Terminal" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][departure][departs_at]=1751389200" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][departure][address][street_address]=Eastern Docks" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][departure][address][city]=Dover" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][departure][address][postal_code]=CT17 9BU" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][departure][address][country]=GB" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][arrival][arrival_location]=Calais Ferry Terminal" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][arrival][address][street_address]=Port de Calais" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][arrival][address][city]=Calais" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][arrival][address][postal_code]=62100" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][arrival][address][country]=FR" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][passengers][0][given_name]=Alice" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][passengers][0][family_name]=Johnson" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][insurances][0][insurance_type]=cancelation" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][insurances][0][insurance_company_name]=Ferry Travel Insurance" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][insurances][0][price]=800" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][insurances][0][currency]=EUR" \
  -d "payment_method_options[klarna][supplementary_purchase_data][ferry_reservation_details][0][affiliate_name]=Channel Crossing Bookings"
```

#### Organized trips and tours

Organized trip reservation data is sent through the `payment_method_options.klarna.supplementary_purchase_data.round_trip_reservation_details` parameter. Each element in the array represents an individual trip ticket or reservation.

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-round_trip_reservation_details) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with organized trip data

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=12000 \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]=true" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][carrier_name]=Traintrak" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][ticket_class]=premium_economy" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][price]=12000" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][currency]=USD" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][departure][departure_location]=Chicago Union Station" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][departure][departs_at]=1751421600" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][departure][address][street_address]=225 S Canal St" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][departure][address][city]=Chicago" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][departure][address][region]=IL" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][departure][address][postal_code]=60606" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][departure][address][country]=US" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][arrival][arrival_location]=Los Angeles Union Station" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][arrival][address][street_address]=800 N Alameda St" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][arrival][address][city]=Los Angeles" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][arrival][address][region]=CA" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][arrival][address][postal_code]=90012" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][arrival][address][country]=US" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][passengers][0][given_name]=Michael" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][passengers][0][family_name]=Brown" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][insurances][0][insurance_type]=cancelation" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][insurances][0][insurance_company_name]=Travel Guard" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][insurances][0][price]=1200" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][insurances][0][currency]=USD" \
  -d "payment_method_options[klarna][supplementary_purchase_data][round_trip_reservation_details][0][affiliate_name]=Rail Pass America"
```

#### Marketplace sellers

Marketplace seller data is sent through the `payment_method_options.klarna.supplementary_purchase_data.marketplace_sellers` parameter. Each element in the array represents information about an individual seller in a marketplace transaction.

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-marketplace_sellers) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with marketplace seller data

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=25000 \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]=true" \
  -d "payment_method_options[klarna][supplementary_purchase_data][marketplace_sellers][0][marketplace_seller_reference]=seller_12345" \
  -d "payment_method_options[klarna][supplementary_purchase_data][marketplace_sellers][0][marketplace_seller_name]=Artisan Crafts Shop" \
  -d "payment_method_options[klarna][supplementary_purchase_data][marketplace_sellers][0][marketplace_seller_address][street_address]=123 Market Street" \
  -d "payment_method_options[klarna][supplementary_purchase_data][marketplace_sellers][0][marketplace_seller_address][city]=Portland" \
  -d "payment_method_options[klarna][supplementary_purchase_data][marketplace_sellers][0][marketplace_seller_address][region]=OR" \
  -d "payment_method_options[klarna][supplementary_purchase_data][marketplace_sellers][0][marketplace_seller_address][postal_code]=97204" \
  -d "payment_method_options[klarna][supplementary_purchase_data][marketplace_sellers][0][marketplace_seller_address][country]=US" \
  -d "payment_method_options[klarna][supplementary_purchase_data][marketplace_sellers][0][product_category]=handmade" \
  -d "payment_method_options[klarna][supplementary_purchase_data][marketplace_sellers][0][seller_registered_at]=1672531200" \
  -d "payment_method_options[klarna][supplementary_purchase_data][marketplace_sellers][0][seller_rating]=high" \
  -d "payment_method_options[klarna][supplementary_purchase_data][marketplace_sellers][0][number_of_transactions]=150" \
  -d "payment_method_options[klarna][supplementary_purchase_data][marketplace_sellers][0][volume_of_transactions]=3500000"
```

## Update and remove supplementary purchase data 

Use the [update](https://docs.stripe.com/api/payment_intents/update.md) or [confirm](https://docs.stripe.com/api/payment_intents/confirm.md) method to modify or remove supplementary purchase data.

### Full replacement of verticals

When you update a vertical’s array, the new data completely replaces the existing data for that vertical. For example, if a PaymentIntent has 2 vouchers and you send an update with 1 voucher, the result is 1 voucher (not 3).

Create a PaymentIntent with 2 vouchers:

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=10000 \
  -d currency=eur \
  -d "automatic_payment_methods[enabled]=true" \
  -d "payment_method_options[klarna][supplementary_purchase_data][vouchers][0][voucher_name]=First Voucher" \
  -d "payment_method_options[klarna][supplementary_purchase_data][vouchers][1][voucher_name]=Second Voucher"
```

Update the PaymentIntent with one voucher to replace the existing two vouchers:

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENTINTENT_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_method_options[klarna][supplementary_purchase_data][vouchers][0][voucher_name]=Replacement Voucher"
```

The PaymentIntent now has only one voucher.

### Preserve existing data

Verticals excluded in an update request remain unchanged. For example, you can add train data without affecting existing vouchers or insurances:

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENTINTENT_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][carrier_name]=Eurotrains" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][ticket_class]=business" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][price]=8500" \
  -d "payment_method_options[klarna][supplementary_purchase_data][train_reservation_details][0][currency]=EUR"
```

The PaymentIntent retains existing vouchers and insurances, and adds the train reservation.

### Unset a specific vertical

To unset all data for a specific vertical while preserving other verticals, set the vertical to an empty string. This removes the vertical from the PaymentIntent.

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENTINTENT_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_method_options[klarna][supplementary_purchase_data][insurances]="
```

### Unset all supplementary purchase data

To unset all supplementary purchase data from a PaymentIntent, set the entire `supplementary_purchase_data` parameter to an empty string:

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENTINTENT_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_method_options[klarna][supplementary_purchase_data]="
```

## Testing 

Test that your integration works correctly for your customers. Simulate API calls in a Stripe [Sandbox](https://docs.stripe.com/sandboxes.md) with a sandbox key. Attach a payment method using the [update](https://docs.stripe.com/api/payment_intents/update.md) method prior to confirming. For additional information, see [Testing](https://docs.stripe.com/testing.md).
