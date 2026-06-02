<!-- Source URL: https://docs.stripe.com/industry-metadata -->
<!-- Fetched: 2026-05-11 -->

# Industry metadata

Learn how to provide data specific to travel and entertainment purchases.

> #### Available with public preview header
>
> You can use this public preview feature by including the version header `2025-11-17.preview` or a later preview version header in your API request.

Use industry metadata in the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) to provide required industry-specific data for transactions in supported travel and entertainment industries.

Providing industry-specific data is required for certain merchant category codes to comply with card network requirements, and might improve authorization rates and risk assessment on Klarna transactions.

Implement industry metadata for card payments if your business operates under specific travel and entertainment merchant category codes (MCCs), such as car rental, lodging, travel agency, or airline codes listed in [Availability](https://docs.stripe.com/industry-metadata.md#availability)).

## Availability

Providing industry-specific data is only available to users of [PaymentIntents](https://docs.stripe.com/api/payment_intents.md) and is limited to the following Merchant Category Codes (MCCs).

- **Car Rental**: 3351-3441, 7512, 7513, 7519
- **Lodging**: 3501-3999, 7011
- **Travel Agency**: 4722
- **Flight**: 4511

You can submit industry metadata for payments with specific card brands (Visa, Mastercard, Amex, and Discover) and Klarna.

### Klarna-specific verticals

In addition to car rentals, lodging, and flights, Klarna supports additional industry-specific verticals that aren’t available for card payments, including:

- Events (concerts, festivals, sports, conferences)
- Insurance (standalone insurance policies)
- Train, bus, and ferry transportation
- Organized trips and tours
- Vouchers
- Marketplace sellers

Learn more about these Klarna-exclusive verticals in the [Klarna supplementary purchase data documentation](https://docs.stripe.com/payments/klarna/supplementary-purchase-data.md).

> #### Private preview for cards
>
> Industry Metadata is in private preview for card transactions and public preview only for Klarna. Additionally, card transactions don’t support passing cruise data.

## Send industry-specific data

You send industry-specific data through the `payment_details` parameter when you [create](https://docs.stripe.com/api/payment_intents/create.md), [update](https://docs.stripe.com/api/payment_intents/update.md), or [confirm](https://docs.stripe.com/api/payment_intents/confirm.md) a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).

The `payment_details` hash contains an array of hashes for each vertical (industry category): `car_rental_data`, `lodging_data`, and `flight_data`.

Each hash in these arrays represents an individual car rental, lodging stay, or flight ticket.

Refer to [Create a PaymentIntent](https://docs.stripe.com/industry-metadata.md#create-payment-intent-flight) to learn more about passing data.

> #### Array processing behavior
>
> Payment methods handle multiple bookings differently:
>
> - **Cards**: Only the _first entry_ in each array (`car_rental_data[0]`, `lodging_data[0]`, `flight_data[0]`) is sent to card networks. Additional entries are ignored and aren’t used for card network compliance.

- **Klarna**: _All entries_ in each array are processed and used in Klarna’s risk assessment and authorization decisions.
  > For card transactions with multiple bookings (such as multiple hotel stays or car rentals), create separate PaymentIntents for each booking to ensure all transaction data is properly sent to card networks.

This section is organized into three property categories for each vertical:

1. **General supported properties**: Base fields that all payment methods support. These fields define the core API structure.
1. **Additional supported properties for cards**: Extra fields that card networks use in addition to general properties. When processing card payments, use fields from both the “General” and “Cards” categories.
1. **Additional supported properties for Klarna**: Extra fields that Klarna uses in addition to the general properties. When processing Klarna payments, use fields from both the “General” and “Klarna” sections.

Cards and Klarna use different properties and validation rules. Properties sent to one payment method that aren’t supported are ignored.

The following tabs describe the `car_rental_data`, `lodging_data`, and `flight_data` hashes:

### General supported properties

The Stripe API supports the following properties, which all card and Klarna transactions use.

#### Car rental

The fields listed below are nested under `payment_details.car_rental_data`. See the [full code example](https://docs.stripe.com/industry-metadata.md#create-a-paymentintent) for how to structure your API request.

#### Required fields for car rentals

The following are the minimum required fields for all car rental transactions:

- `pickup.address.line1`
- `pickup.address.city`
- `pickup.address.postal_code`
- `pickup.address.country`
- `pickup.time`
- `drop_off.address.line1`
- `drop_off.address.city`
- `drop_off.address.postal_code`
- `drop_off.address.country`
- `drop_off.time`
- `total.amount`

These are additional fields that are required for card transactions:

- `pickup.address.state` (when applicable to the country)
- `drop_off.address.state` (when applicable to the country)
- `booking_number`
- `days_rented`
- `customer_service_phone_number`
- `renter_name`
- `vehicle.type`
- `vehicle.make`
- `vehicle.model`

| Property name          | Type   | Description                                                            | Format              |
| ---------------------- | ------ | ---------------------------------------------------------------------- | ------------------- |
| `pickup.address.line1` | String | First line of the car pickup address (street, PO Box, or company name) | - Required property |

- Alphanumeric
- Maximum length: 99 characters |
  | `pickup.address.postal_code` | String | Postal code of the car pickup address | - Required property
- Alphanumeric
- Maximum length: 10 characters |
  | `pickup.address.city` | String | City, district, suburb, town, or village of the car pickup address | - Required property
- Alphanumeric
- Maximum length: 99 characters |
  | `pickup.address.country` | String | Country code of the car pickup address | - Required property
- Must be a valid [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code |
  | `pickup.time` | Timestamp | Car pickup time | - Required property
- Seconds since the Unix epoch
- Must be between 2 years ago and 2 years from now |
  | `drop_off.address.line1` | String | First line of the car drop off address (street, PO Box, or company name) | - Required property
- Alphanumeric
- Maximum length: 99 characters |
  | `drop_off.address.postal_code` | String | Postal code of the car drop off address | - Required property
- Alphanumeric
- Maximum length: 10 characters |
  | `drop_off.address.city` | String | City, district, suburb, town, or village of the car drop off address | - Required property
- Alphanumeric
- Maximum length: 99 characters |
  | `drop_off.address.country` | String | Country code of the car drop off address | - Required property
- Must be a valid [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code |
  | `drop_off.time` | Timestamp | Car drop off time | - Required property
- Seconds since the Unix epoch
- Must be between 2 years ago and 2 years from now |
  | `total.amount` | Integer | Price of the overall car rental in the _smallest currency unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)) | - Required property
- Minimum: 0 |
  | `pickup.address.state` | String | State, county, province, or region of the car pickup address | - Required for cards
- Conditional validation1
- Alphanumeric
- Maximum length: 99 characters |
  | `drop_off.address.state` | String | State, county, province, or region of the car drop off address | - Required for cards
- Conditional validation2
- Alphanumeric
- Maximum length: 99 characters |
  | `pickup.address.line2` | String | Second line of the car pickup address (street, PO Box, or company name) | - Alphanumeric
- Maximum length: 99 characters |
  | `drop_off.address.line2` | String | Second line of the car drop off address (street, PO Box, or company name) | - Alphanumeric
- Maximum length: 99 characters |
  | `carrier_name` | String | Name of the car rental company | - Alphanumeric
- Maximum length: 255 characters |
  | `vehicle.vehicle_class` | String | Tier of rented vehicle | - One of `economy`, `premium_economy`, `business`, or `first_class` |
  | `affiliate.name` | String | Name of the affiliate that initiated the purchase | - Alphanumeric
- Maximum length: 255 characters |

1 `pickup.address.state` must be a valid state in `pickup.address.country` for card transactions

2 `drop_off.address.state` must be a valid state in `drop_off.address.country` for card transactions

#### Lodging

The fields listed below are nested under `payment_details.lodging_data`. See the [full code example](https://docs.stripe.com/industry-metadata.md#create-a-paymentintent) for how to structure your API request.

#### Required fields for lodging

The following are the minimum required fields for all lodging transactions:

- `checkin_at`
- `checkout_at`
- `total.amount`

These are additional fields required for card transactions:

- `booking_number`
- `fire_safety_act_compliance_indicator`
- `customer_service_phone_number`
- `accommodation.nights`
- `accommodation.daily_rate_amount`

| Property name | Type      | Description                    | Format              |
| ------------- | --------- | ------------------------------ | ------------------- |
| `checkin_at`  | Timestamp | Lodging check-in time and date | - Required property |

- Seconds since the Unix epoch
- Must be between 2 years ago and 2 years from now |
  | `checkout_at` | Timestamp | Lodging check-out time and date | - Required property
- Seconds since the Unix epoch
- Must be between 2 years ago and 2 years from now |
  | `total.amount` | Integer | Total lodging price excluding taxes and fees in the _smallest currency unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)) | - Required property
- Minimum: 0 |
  | `accommodation.accommodation_type` | String | Type of accommodation | - One of `room`, `apartment`, `house`, `cabana`, `villa`, `standard`, `suite`, or `penthouse` |
  | `affiliate.name` | String | Name of the affiliate that initiated the purchase | - Alphanumeric
- Maximum length: 255 characters |

#### Flight

The fields listed below are nested under `payment_details.flight_data`. See the [full code example](https://docs.stripe.com/industry-metadata.md#create-a-paymentintent) for how to structure your API request.

> #### Feature enablement required
>
> Flight data for card transactions is in private preview. Contact your account team or Stripe support to enable this feature.

#### Required fields for flights

The following are minimum required fields for all flight transactions:

- `segments[]` (array with at least one segment, each containing):
  - `segments[].service_class`
  - `segments[].carrier_code`
  - `segments[].departure.airport`
  - `segments[].departure.departs_at`
  - `segments[].arrival.airport`
- `total.amount`

These are additional fields required for card transactions:

- `segments[].carrier_name`
- `segments[].flight_number`
- `segments[].ticket_number`
- `segments[].arrival.arrives_at`

| Property name                                                       | Type   | Description                           | Format              |
| ------------------------------------------------------------------- | ------ | ------------------------------------- | ------------------- |
| `segments[].service_class`                                          | String | Class of service booked in the ticket | - Required property |
| - One of `economy`, `premium_economy`, `business`, or `first_class` |
| `segments[].carrier_code`                                           | String | Airline code for this travel segment  | - Required property |

- Exactly 2 characters: first character must be uppercase letter, second must be uppercase letter or digit
- Should be a valid [IATA airline code](https://en.wikipedia.org/wiki/Airline_codes) |
  | `segments[].departure.airport` | String | Airport code for the airport the flight departed from | - Required property
- Exactly 3 uppercase alphabetic characters
- Should be a valid [IATA airport code](https://en.wikipedia.org/wiki/IATA_airport_code) |
  | `segments[].departure.departs_at` | Timestamp | Ticket departure date | - Required property
- Seconds since the Unix Epoch
- Must be between 2 years ago and 2 years from now |
  | `segments[].arrival.airport` | String | Airport code for the airport the flight arrived at | - Required property
- Exactly 3 uppercase alphabetic characters
- Should be a valid [IATA airport code](https://en.wikipedia.org/wiki/IATA_airport_code) |
  | `total.amount` | Integer | Total ticket amount excluding taxes and fees in the _smallest currency unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)) | - Required property
- Minimum: 0 |
  | `passengers[].name` | String | Full name of a passenger on the ticket | - Conditionally required1
- Alphanumeric
- Maximum length: 198 characters |
  | `segments[].amount` | Integer | Total price of the travel segment in the _smallest currency unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)) | - Minimum: 0 |
  | `segments[].currency` | String | Currency of the segment price | - Must be a valid [ISO 4217 3-letter code](https://en.wikipedia.org/wiki/ISO_4217) |
  | `affiliate.name` | String | Name of the affiliate that initiated the purchase | - Alphanumeric
- Maximum length: 255 characters |

1 The `passengers` array is optional. `passengers[].name` is required for each passenger provided.

### Additional supported properties for cards

Cards support the general supported properties, and also use the following properties. Klarna won’t see these properties, and they won’t improve authorization rates or risk assessment for Klarna transactions.

#### Car rental

| Property name    | Type   | Description                                    | Format               |
| ---------------- | ------ | ---------------------------------------------- | -------------------- |
| `booking_number` | String | Booking confirmation number for the car rental | - Required for cards |

- Alphanumeric
- Maximum length: 255 characters |
  | `days_rented` | Integer | Number of days the car was rented | - Required for cards
- Minimum: 1
- Maximum: 999 |
  | `customer_service_phone_number` | String | Phone number for the car rental company’s customer service | - Required for cards
- Must be a valid phone number (numbers only), can also be all zeros (`0000000000`) in a sandbox
- Non-US phone numbers must begin with a plus symbol (`+`) |
  | `renter_name` | String | Name of the person renting the vehicle | - Required for cards
- Maximum length: 198 characters |
  | `vehicle.type` | String | Code indicating the vehicle’s class | - Required for cards
- One of `mini`, `subcompact`, `economy`, `compact`, `midsize`, `intermediate`, `standard`, `full_size`, `luxury`, `premium`, `minivan`, `twelve_passenger_van`, `moving_van`, `fifteen_passenger_van`, `cargo_van`, `twelve_foot_truck`, `twenty_foot_truck`, `twenty_four_foot_truck`, `twenty_six_foot_truck`, `moped`, `stretch`, `regular`, `unique`, `exotic`, `small_medium_truck`, `large_truck`, `small_suv`, `medium_suv`, `large_suv`, `exotic_suv`, `four_wheel_drive`, `special`, `taxi`, or `miscellaneous` |
  | `vehicle.make` | String | Brand of car that was rented | - Required for cards
- Alphanumeric
- Maximum length: 40 characters |
  | `vehicle.model` | String | Model of car that was rented | - Required for cards
- Alphanumeric
- Maximum length: 40 characters |
  | `distance.amount` | Integer | Distance traveled during the car rental period | - Conditionally required property 1
- Minimum: 0 |
  | `distance.unit` | String | Unit of distance for the distance traveled | - Conditionally required property 1
- One of `miles` or `kilometers` |
  | `no_show_indicator` | Boolean | Indicates if the customer failed to show up for their booking | - `true` or `false` |
  | `pickup.location_name` | String | Location where the car rental was picked up | - Alphanumeric
- Maximum length: 38 characters |
  | `drop_off.location_name` | String | Location where the car rental was dropped off | - Alphanumeric
- Maximum length: 38 characters |
  | `drivers[].driver_identification_number` | String | Driver’s license or ID number belonging to the authorized driver in the car rental agreement | - Alphanumeric
- Maximum length: 20 characters
- This personally identifiable property isn’t required |
  | `drivers[].driver_tax_number` | String | Tax identification number of the authorized driver in the car rental agreement | - Alphanumeric
- Maximum length: 20 characters
- This personally identifiable property isn’t required |
  | `total.rate_per_unit` | Integer | Rate charged for each unit of distance or time traveled | - Minimum: 0 |
  | `total.rate_unit` | String | Unit used to calculate the rate per unit traveled | - One of `miles`, `kilometers`, `days`, `weeks`, or `months` |
  | `total.tax.tax_exempt_indicator` | Boolean | Indicates if the car rental was tax-exempt or tax wasn’t collected | - `true` or `false` |
  | `total.tax.taxes[].rate` | Integer | Percentage used to calculate this tax amount | - Minimum: 0 |
  | `total.tax.taxes[].amount` | Integer | Amount of this tax charged for the car rental | - Minimum: 0 |
  | `total.tax.taxes[].type` | String | Type of tax applied to the car rental | - Alphanumeric
- Maximum length: 40 characters |
  | `total.extra_charges[].amount` | Integer | Amounts of extra charge incurred during the car rental | - Minimum: 0 |
  | `total.extra_charges[].type` | String | Types of extra charge incurred during the car rental | - One of `one_way_drop_off`, `regular_mileage`, `extra_mileage`, `late_charge`, `parking`, `towing`, `gps`, `phone`, `gas`, or `other` |
  | `total.discounts.maximum_free_miles_or_kilometers` | Integer | Number of free miles or kilometers allowed during the car rental | - Minimum: 0
- Maximum: 9999 |
  | `total.discounts.corporate_client_code` | String | Code assigned to a business entity used for corporate rates or discounts | - Alphanumeric
- Maximum length: 20 characters |
  | `total.discounts.coupon` | String | Coupon code used to discount the rate of the car rental agreement | - Maximum length: 25 characters |
  | `vehicle.vehicle_identification_number` | String | Registration number of the rented vehicle | - Alphanumeric
- Maximum length: 20 characters |
  | `vehicle.odometer` | Integer | Odometer reading when the car was first rented | - Minimum: 0 |
  | `affiliate.code` | String | Code of the affiliate that initiated the purchase | - Alphanumeric
- Maximum length: 20 characters |

1 The `distance` property is optional. `distance.amount` and `distance.unit` are required if distance is provided.

#### Lodging

| Property name    | Type   | Description                                             | Format               |
| ---------------- | ------ | ------------------------------------------------------- | -------------------- |
| `booking_number` | String | Booking confirmation number associated with the lodging | - Required for cards |

- Alphanumeric
- Maximum length: 255 characters |
  | `fire_safety_act_compliance_indicator` | Boolean | Indicates that the facility complies with hotel fire regulations such as the [Hotel and Motel Fire Safety Act of 1990](https://en.wikipedia.org/wiki/Hotel_and_Motel_Fire_Safety_Act_of_1990) | - Required for cards
- `true` or `false` |
  | `customer_service_phone_number` | String | Customer service phone number used to resolve cardholder questions and disputes | - Required for cards
- Must be a valid phone number (numbers only), can also be all zeros (`0000000000`) in a sandbox
- Non-US phone numbers must begin with a plus symbol (`+`) |
  | `accommodation.nights` | Integer | Number of nights the room was reserved | - Required for cards
- Minimum: 0
- Maximum: 999 |
  | `accommodation.daily_rate_amount` | Integer | Daily rate of the room at the lodging property, excluding taxes | - Required for cards
- Minimum: 0 |
  | `renter_name` | String | Name of the primary guest | - Alphanumeric
- Maximum length: 198 characters |
  | `renter_id_number` | String | Unique identification number assigned to the lodging guest | - Alphanumeric
- Maximum length: 25 characters |
  | `no_show_indicator` | Boolean | Indicates the customer failed to show up for their booking | - `true` or `false` |
  | `total.prepaid_amount` | Integer | Total amount the cardholder prepaid towards lodging expenses in the _smallest currency unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)) | - Minimum: 0 |
  | `total.cash_advances` | Integer | Total amount of cash received during the lodging stay in the _smallest currency unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)) | - Minimum: 0 |
  | `total.tax.tax_exempt_indicator` | Boolean | Indicates if the lodging was tax-exempt or if tax wasn’t collected | - `true` or `false` |
  | `total.tax.taxes[].rate` | Integer | Percentage used to calculate this tax amount | - Minimum: 0 |
  | `total.tax.taxes[].amount` | Integer | Amount of this tax charged for the lodging | - Minimum: 0 |
  | `total.tax.taxes[].type` | String | Type of tax applied to the lodging | - Alphanumeric
- Maximum length: 40 characters |
  | `total.extra_charges[].amount` | Integer | Total price of this extra charge in the _smallest currency unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)) | - Minimum: 0 |
  | `total.extra_charges[].type` | String | Type of extra charge applied | - One of `restaurant`, `mini_bar`, `gift_shop`, `phone`, `laundry`, or `other` |
  | `total.discounts.corporate_client_code` | String | Code assigned to a business entity to identify corporate rates and discounts | - Alphanumeric
- Maximum length: 20 characters |
  | `total.discounts.coupon` | String | Additional coupons or discounts applied to the lodging | - Alphanumeric
- Maximum length: 25 characters |
  | `host.property_phone_number` | String | Phone number of the lodging property | - Must be a valid phone number (numbers only), can also be all zeros (`0000000000`) in a sandbox
- Non-US phone numbers must begin with a plus symbol (`+`) |
  | `accommodation.rate_type` | String | Type of rate applied to the lodging stay | - Alphanumeric
- Maximum length: 20 characters |
  | `accommodation.smoking_indicator` | Boolean | Indicates whether the customer requested this room to be a smoking room | - `true` or `false` |
  | `accommodation.bed_type` | String | Size of the bed specified in the lodging reservation | - Alphanumeric
- Maximum length: 20 characters |
  | `affiliate.code` | String | Code of the travel agency that made the lodging reservation | - Alphanumeric
- Maximum length: 20 characters |

#### Flight

| Property name             | Type   | Description                         | Format               |
| ------------------------- | ------ | ----------------------------------- | -------------------- |
| `segments[].carrier_name` | String | Name of the airline for this ticket | - Required for cards |

- Alphanumeric
- Maximum length: 25 characters |
  | `segments[].flight_number` | String | Number assigned to the trip leg by the carrier | - Required for cards
- Alphanumeric
- Maximum length: 20 characters |
  | `segments[].ticket_number` | String | Number assigned to the ticket as supplied by the carrier | - Required for cards
- Alphanumeric
- Maximum length: 20 characters |
  | `segments[].arrival.arrives_at` | Timestamp | Ticket arrival date | - Required for cards
- Seconds since the Unix Epoch
- Must be between 2 years ago and 2 years from now |
  | `computerized_reservation_system` | String | Computerized reservation system used to make the reservation | - Conditional Validation1
- Maximum length: 4 characters |
  | `endorsements_and_restrictions` | String | Endorsements or restrictions on the airline ticket | - Alphanumeric
- Maximum length: 20 characters |
  | `transaction_type` | String | Transaction type code associated with the transaction | - One of `ticket_purchase`, `refund`, `exchange_ticket`, or `miscellaneous` |
  | `ticket_electronically_issued_indicator` | Boolean | Indicates if an electronic ticket was issued | - `true` or `false` |
  | `segments[].is_stop_over_indicator` | Boolean | Indicates if a stop over was allowed on this ticket | - `true` or `false` |
  | `segments[].fare_basis_code` | String | Code assigned to the ticket’s class based on the fare charged | - Alphanumeric
- Maximum length: 20 characters |
  | `segments[].exchange_ticket_number` | String | Original ticket number if this ticket replaced an old ticket number | - Alphanumeric
- Maximum length: 20 characters |
  | `segments[].tax_amount` | Integer | Amount of tax charged for the segment in the _smallest currency unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)) | - Minimum: 0 |
  | `segments[].fees` | Integer | Total fee amount for the segment in the _smallest currency unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)) | - Minimum: 0 |
  | `segments[].refundable` | Boolean | Indicates whether the segment is refundable | - `true` or `false` |
  | `total.credit_reason` | String | Reason for a credit to the ticket’s card holder | - One of `passenger_transport_ancillary_cancellation`, `ticket_and_ancillary_cancellation`, `ticket_cancellation`, `partial_ticket_refund`, or `other` |
  | `total.tax.taxes[].rate` | Integer | Percentage used to calculate this tax amount | - Minimum: 0 |
  | `total.tax.taxes[].amount` | Integer | Amount of this tax charged for the flight | - Minimum: 0 |
  | `total.tax.taxes[].type` | String | Type of tax applied to the flight | - Alphanumeric
- Maximum length: 40 characters |
  | `total.extra_charges[].amount` | Integer | Price of this extra charge in the _smallest currency unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)) | - Minimum: 0 |
  | `total.extra_charges[].type` | String | Type of extra charge applied to the ticket | - One of `additional_fees`, `exchange_fee`, `ancillary_service_charges` |
  | `total.discounts.corporate_client_code` | String | Code assigned to a business entity to identify corporate rates and discounts | - Alphanumeric
- Maximum length: 20 characters |
  | `affiliate.code` | String | Unique code to identify the affiliate partner issuing the ticket | - Alphanumeric
- Maximum length: 20 characters |
  | `affiliate.travel_authorization_code` | String | Code provided by the carrier authorizing the affiliate to issue tickets | - Alphanumeric
- Maximum length: 64 characters |

1 For German transactions: `computerized_reservation_system` should contain spaces or one of `STRT` for Start, `PARS` for TWA, `DATS` for Delta, `SABR` for Sabre, `DALA` for Covia-Apollo, `BLAN` for Dr. Blank, `DERD` for DER, or `TUID` for TUI

### Additional Klarna supported properties

Klarna supports the general supported properties, and also uses the following properties. The card networks won’t see these properties and they won’t impact compliance with card network requirements for card transactions.

#### Car rental

| Property name    | Type   | Description                                                    | Format                    |
| ---------------- | ------ | -------------------------------------------------------------- | ------------------------- |
| `drivers[].name` | String | Full name of the authorized driver in the car rental agreement | - Conditionally required1 |

- Alphanumeric
- Maximum length: 198 characters |
  | `drivers[].date_of_birth.day` | Integer | Date of birth of the authorized driver in the car rental agreement | - Conditionally required2
- Minimum: 1
- Maximum: 31
- `date_of_birth` must be a valid date in the past |
  | `drivers[].date_of_birth.month` | Integer | Date of birth of the authorized driver in the car rental agreement | - Conditionally required2
- Minimum: 1
- Maximum: 12
- `date_of_birth` must be a valid date in the past |
  | `drivers[].date_of_birth.year` | Integer | Date of birth of the authorized driver in the car rental agreement | - Conditionally required2
- Minimum: 1901
- `date_of_birth` must be a valid date in the past |
  | `carrier_name` | String | Name of the car rental company | - Alphanumeric
- Maximum length: 255 characters |
  | `total.currency` | String | Currency of the price of the overall car rental | - Must be a valid [ISO 4217 3-letter code](https://en.wikipedia.org/wiki/ISO_4217) |
  | `insurances[].insurance_type` | String | Type of insurance coverage provided for the car rental | - Conditionally required3
- One of `liability_supplement`, `loss_damage_waiver`, `partial_damage_waiver`, `personal_accident`, `personal_effects`, or `other` |
  | `insurances[].amount` | Integer | Price of the insurance provided for the car rental in the _smallest currency unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)) | - Conditionally required3
- Minimum: 0 |
  | `insurances[].currency` | String | Currency of the insurance provided for the car rental | - Must be a valid [ISO 4217 3-letter code](https://en.wikipedia.org/wiki/ISO_4217) |
  | `insurances[].insurance_company_name` | String | Name of the company providing insurance for the car rental | - Maximum length: 255 characters |

1 The `drivers` array is optional. The `drivers[].name` is required for each driver provided.

2 The `drivers[].date_of_birth` property is optional. `drivers[].date_of_birth.day`, `drivers[].date_of_birth.month`, and `drivers[].date_of_birth.year` are all required if `drivers[].date_of_birth` is provided.

3 The `insurances` array is optional. `insurances[].insurance_type` and `insurances[].amount` are required for each insurance provided.

#### Lodging

| Property name   | Type   | Description                     | Format                             |
| --------------- | ------ | ------------------------------- | ---------------------------------- |
| `guests[].name` | String | Full name of the lodging patron | - Conditionally required property1 |

- Alphanumeric
- Maximum length: 198 characters |
  | `host.address.line1` | String | First line of the lodging property address (street, PO Box, or company name) | - Conditionally required property2
- Alphanumeric
- Maximum length: 99 characters |
  | `host.address.postal_code` | String | Postal code of the lodging property address | - Conditionally required property2
- Alphanumeric
- Maximum length: 10 characters |
  | `host.address.city` | String | City, district, suburb, town, or village of the lodging property address | - Conditionally required property2
- Alphanumeric
- Maximum length: 99 characters |
  | `host.address.country` | String | Country code of the lodging property address | - Conditionally required property2
- Must be a valid [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code |
  | `total.currency` | String | Currency of the total lodging price | - Must be a valid [ISO 4217 3-letter code](https://en.wikipedia.org/wiki/ISO_4217) |
  | `host.name` | String | Name of the lodging property or host | - Alphanumeric
- Maximum length: 255 characters |
  | `host.host_reference` | String | Unique identifier assigned to the host providing the lodging | - Alphanumeric
- Maximum length: 255 characters |
  | `host.host_type` | String | Type of host providing the lodging | - One of `rental_agency`, `owner`, `hotel`, `hostel` |
  | `host.country_of_domicile` | String | The host’s country | - Must be a valid [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code |
  | `host.registered_at` | Timestamp | The host’s registration date | - Seconds since the Unix epoch
- Must be in the past |
  | `host.number_of_reservations` | Integer | Total number of reservations the host has | - Minimum: 0 |
  | `host.address.line2` | String | Second line of the lodging property address (street, PO Box, or company name) | - Alphanumeric
- Maximum length: 99 characters |
  | `host.address.state` | String | State, county, province, or region of the lodging property address | - Alphanumeric
- Maximum length: 99 characters |
  | `accommodation.number_of_rooms` | Integer | Number of rooms, cabanas, apartments, or similar units reserved | - Minimum: 1 |
  | `insurances[].insurance_type` | String | Type of insurance applied to the reservation | - Conditionally required property3
- One of `cancelation`, `bankruptcy`, `medical`, or `emergency` |
  | `insurances[].amount` | Integer | Price of the insurance in the _smallest currency unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)) | - Conditionally required property3
- Minimum: 0 |
  | `insurances[].currency` | String | Currency of the insurance provided for the car rental | - Must be a valid [ISO 4217 3-letter code](https://en.wikipedia.org/wiki/ISO_4217) |
  | `insurances[].insurance_company_name` | String | Name of the company providing insurance for the car rental | - Maximum length: 255 characters |

1 The `guests` array is optional. `guests[].name` is required for each guest provided.

2 The `host.address` property is optional. `host.address.line1`, `host.address.postal_code`, `host.address.city`, and `host.address.country` are all required if `host.address` is provided.

3 The `insurances` array is optional. `insurances[].insurance_type` and `insurances[].amount` are required for each insurance provided.

#### Flight

| Property name                                                              | Type    | Description                                                                                                                                                                                                                                                                                                            | Format                                                                             |
| -------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `booking_number`                                                           | String  | Booking confirmation number associated with the flight                                                                                                                                                                                                                                                                 | - Alphanumeric                                                                     |
| - Maximum length: 255 characters                                           |
| `segments[].departure.city`                                                | String  | Name of the city the flight departed from                                                                                                                                                                                                                                                                              | - Alphanumeric                                                                     |
| - Maximum length: 99 characters                                            |
| `segments[].departure.country`                                             | String  | Code for the country the flight departed from                                                                                                                                                                                                                                                                          | - Alphanumeric                                                                     |
| - [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)   |
| `segments[].arrival.city`                                                  | String  | Name of the city the flight arrived at                                                                                                                                                                                                                                                                                 | - Alphanumeric                                                                     |
| - Maximum length: 99 characters                                            |
| `segments[].arrival.country`                                               | String  | Code for the country the flight arrived at                                                                                                                                                                                                                                                                             | - Alphanumeric                                                                     |
| - [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)   |
| `total.currency`                                                           | String  | Currency of the total ticket amount                                                                                                                                                                                                                                                                                    | - Must be a valid [ISO 4217 3-letter code](https://en.wikipedia.org/wiki/ISO_4217) |
| `insurances[].insurance_type`                                              | String  | Type of insurance provided for the ticket                                                                                                                                                                                                                                                                              | - Conditionally required1                                                          |
| - One of `cancelation`, `bankruptcy`, `medical`, `baggage`, or `emergency` |
| `insurances[].amount`                                                      | Integer | Price of insurance in the _smallest currency unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)) | - Conditionally required1                                                          |
| - Minimum: 0                                                               |
| `insurances[].currency`                                                    | String  | Currency of the insurance price                                                                                                                                                                                                                                                                                        | - Must be a valid [ISO 4217 3-letter code](https://en.wikipedia.org/wiki/ISO_4217) |
| `insurances[].insurance_company_name`                                      | String  | Name of the company providing insurance for the ticket                                                                                                                                                                                                                                                                 | - Alphanumeric                                                                     |
| - Maximum length: 255 characters                                           |

1 The `insurances` array is optional. `insurances[].insurance_type` and `insurances[].amount` are required for each insurance provided.

> For certain properties, the lengths might be truncated to comply with various payment method requirements that accept different property sizes.

## Use PaymentIntents

Include `payment_details` data when you [create](https://docs.stripe.com/api/payment_intents/create.md), [update](https://docs.stripe.com/api/payment_intents/update.md), [confirm](https://docs.stripe.com/api/payment_intents/confirm.md), or [capture](https://docs.stripe.com/api/payment_intents/capture.md) a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).

The steps below highlight manual confirmation and capture to show how to update `payment_details` throughout the PaymentIntent lifecycle. You can provide `payment_details` for automatic confirmation or automatic capture use cases.

### Create a PaymentIntent

Create an unconfirmed and uncaptured [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) with `payment_details`. Use the [update](https://docs.stripe.com/api/payment_intents/update.md) method to update `payment_details` before confirming the PaymentIntent. All `payment_details` updates are a full hash replacement and must be valid for your payment method.

#### Car rental

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=200 \
  -d currency=usd \
  -d "payment_method_types[0]=card" \
  -d "payment_details[car_rental_data][0][booking_number]=BOOK123456" \
  -d "payment_details[car_rental_data][0][days_rented]=3" \
  --data-urlencode "payment_details[car_rental_data][0][customer_service_phone_number]=+18005551234" \
  -d "payment_details[car_rental_data][0][renter_name]=John Doe" \
  -d "payment_details[car_rental_data][0][no_show_indicator]=false" \
  -d "payment_details[car_rental_data][0][distance][amount]=150" \
  -d "payment_details[car_rental_data][0][distance][unit]=miles" \
  -d "payment_details[car_rental_data][0][drivers][0][name]=Jane Driver" \
  -d "payment_details[car_rental_data][0][drivers][0][driver_identification_number]=D12345678" \
  -d "payment_details[car_rental_data][0][drivers][0][driver_tax_number]=TN123456789" \
  -d "payment_details[car_rental_data][0][pickup][address][line1]=123 Main St" \
  -d "payment_details[car_rental_data][0][pickup][address][postal_code]=10001" \
  -d "payment_details[car_rental_data][0][pickup][address][city]=New York" \
  -d "payment_details[car_rental_data][0][pickup][address][country]=US" \
  -d "payment_details[car_rental_data][0][pickup][address][state]=NY" \
  -d "payment_details[car_rental_data][0][pickup][address][line2]=Apt 4B" \
  -d "payment_details[car_rental_data][0][pickup][time]=1768500000" \
  -d "payment_details[car_rental_data][0][pickup][location_name]=Downtown Garage" \
  -d "payment_details[car_rental_data][0][drop_off][address][line1]=456 Elm St" \
  -d "payment_details[car_rental_data][0][drop_off][address][postal_code]=02101" \
  -d "payment_details[car_rental_data][0][drop_off][address][city]=Boston" \
  -d "payment_details[car_rental_data][0][drop_off][address][country]=US" \
  -d "payment_details[car_rental_data][0][drop_off][address][state]=MA" \
  -d "payment_details[car_rental_data][0][drop_off][address][line2]=Suite 101" \
  -d "payment_details[car_rental_data][0][drop_off][time]=1768777200" \
  -d "payment_details[car_rental_data][0][drop_off][location_name]=Airport Terminal" \
  -d "payment_details[car_rental_data][0][total][amount]=30000" \
  -d "payment_details[car_rental_data][0][total][rate_per_unit]=1500" \
  -d "payment_details[car_rental_data][0][total][rate_unit]=days" \
  -d "payment_details[car_rental_data][0][total][tax][tax_exempt_indicator]=false" \
  -d "payment_details[car_rental_data][0][total][tax][taxes][0][rate]=10" \
  -d "payment_details[car_rental_data][0][total][tax][taxes][0][amount]=3000" \
  -d "payment_details[car_rental_data][0][total][tax][taxes][0][type]=Sales Tax" \
  -d "payment_details[car_rental_data][0][total][extra_charges][0][amount]=2000" \
  -d "payment_details[car_rental_data][0][total][extra_charges][0][type]=gps" \
  -d "payment_details[car_rental_data][0][total][discounts][maximum_free_miles_or_kilometers]=100" \
  -d "payment_details[car_rental_data][0][total][discounts][corporate_client_code]=CORP123" \
  -d "payment_details[car_rental_data][0][total][discounts][coupon]=SAVE20" \
  -d "payment_details[car_rental_data][0][insurances][0][insurance_type]=liability_supplement" \
  -d "payment_details[car_rental_data][0][insurances][0][amount]=1500" \
  -d "payment_details[car_rental_data][0][vehicle][vehicle_class]=premium_economy" \
  -d "payment_details[car_rental_data][0][vehicle][type]=compact" \
  -d "payment_details[car_rental_data][0][vehicle][make]=Toyota" \
  -d "payment_details[car_rental_data][0][vehicle][model]=Camry" \
  -d "payment_details[car_rental_data][0][vehicle][vehicle_identification_number]=1HGBH41JXMN109186" \
  -d "payment_details[car_rental_data][0][vehicle][odometer]=25000" \
  -d "payment_details[car_rental_data][0][affiliate][name]=Travel Partner" \
  -d "payment_details[car_rental_data][0][affiliate][code]=TP001"
```

#### Lodging

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=500 \
  -d currency=usd \
  -d "payment_method_types[0]=card" \
  -d "payment_details[lodging_data][0][checkin_at]=1771624800" \
  -d "payment_details[lodging_data][0][checkout_at]=1771869600" \
  -d "payment_details[lodging_data][0][booking_number]=HOTEL345678" \
  -d "payment_details[lodging_data][0][fire_safety_act_compliance_indicator]=true" \
  --data-urlencode "payment_details[lodging_data][0][customer_service_phone_number]=+12025551234" \
  -d "payment_details[lodging_data][0][renter_name]=Jane Smith" \
  -d "payment_details[lodging_data][0][renter_id_number]=ID123456789" \
  -d "payment_details[lodging_data][0][no_show_indicator]=false" \
  --data-urlencode "payment_details[lodging_data][0][host][property_phone_number]=+18005556789" \
  -d "payment_details[lodging_data][0][total][amount]=50000" \
  -d "payment_details[lodging_data][0][total][prepaid_amount]=25000" \
  -d "payment_details[lodging_data][0][total][cash_advances]=10000" \
  -d "payment_details[lodging_data][0][total][tax][tax_exempt_indicator]=false" \
  -d "payment_details[lodging_data][0][total][tax][taxes][0][rate]=10" \
  -d "payment_details[lodging_data][0][total][tax][taxes][0][amount]=5000" \
  -d "payment_details[lodging_data][0][total][tax][taxes][0][type]=City Tax" \
  -d "payment_details[lodging_data][0][total][extra_charges][0][amount]=3000" \
  -d "payment_details[lodging_data][0][total][extra_charges][0][type]=mini_bar" \
  -d "payment_details[lodging_data][0][total][discounts][corporate_client_code]=CORP456" \
  -d "payment_details[lodging_data][0][total][discounts][coupon]=WINTER10" \
  -d "payment_details[lodging_data][0][accommodation][accommodation_type]=suite" \
  -d "payment_details[lodging_data][0][accommodation][nights]=3" \
  -d "payment_details[lodging_data][0][accommodation][daily_rate_amount]=15000" \
  -d "payment_details[lodging_data][0][accommodation][rate_type]=Standard" \
  -d "payment_details[lodging_data][0][accommodation][smoking_indicator]=false" \
  -d "payment_details[lodging_data][0][accommodation][bed_type]=King" \
  -d "payment_details[lodging_data][0][affiliate][name]=Travel Network" \
  -d "payment_details[lodging_data][0][affiliate][code]=TN987"
```

#### Flight

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=200 \
  -d currency=usd \
  -d "payment_method_types[0]=card" \
  -d "payment_details[flight_data][0][computerized_reservation_system]=GDS1" \
  -d "payment_details[flight_data][0][endorsements_and_restrictions]=NONREF" \
  -d "payment_details[flight_data][0][transaction_type]=ticket_purchase" \
  -d "payment_details[flight_data][0][ticket_electronically_issued_indicator]=true" \
  -d "payment_details[flight_data][0][segments][0][service_class]=economy" \
  -d "payment_details[flight_data][0][segments][0][carrier_code]=AA" \
  -d "payment_details[flight_data][0][segments][0][departure][airport]=JFK" \
  -d "payment_details[flight_data][0][segments][0][departure][city]=New York" \
  -d "payment_details[flight_data][0][segments][0][departure][country]=US" \
  -d "payment_details[flight_data][0][segments][0][departure][departs_at]=1781535600" \
  -d "payment_details[flight_data][0][segments][0][arrival][airport]=LAX" \
  -d "payment_details[flight_data][0][segments][0][arrival][city]=Los Angeles" \
  -d "payment_details[flight_data][0][segments][0][arrival][country]=US" \
  -d "payment_details[flight_data][0][segments][0][arrival][arrives_at]=1781557200" \
  -d "payment_details[flight_data][0][segments][0][amount]=30000" \
  -d "payment_details[flight_data][0][segments][0][currency]=USD" \
  -d "payment_details[flight_data][0][segments][0][carrier_name]=American Airlines" \
  -d "payment_details[flight_data][0][segments][0][flight_number]=AA100" \
  -d "payment_details[flight_data][0][segments][0][ticket_number]=1234567890123" \
  -d "payment_details[flight_data][0][segments][0][is_stop_over_indicator]=false" \
  -d "payment_details[flight_data][0][segments][0][fare_basis_code]=Y" \
  --data-urlencode "payment_details[flight_data][0][segments][0][exchange_ticket_number]=N/A" \
  -d "payment_details[flight_data][0][segments][0][tax_amount]=2400" \
  -d "payment_details[flight_data][0][segments][0][fees]=1500" \
  -d "payment_details[flight_data][0][segments][0][refundable]=true" \
  -d "payment_details[flight_data][0][total][amount]=120000" \
  -d "payment_details[flight_data][0][total][tax][taxes][0][rate]=8" \
  -d "payment_details[flight_data][0][total][tax][taxes][0][amount]=9600" \
  -d "payment_details[flight_data][0][total][tax][taxes][0][type]=Sales Tax" \
  -d "payment_details[flight_data][0][total][extra_charges][0][amount]=1500" \
  -d "payment_details[flight_data][0][total][extra_charges][0][type]=additional_fees" \
  -d "payment_details[flight_data][0][total][discounts][corporate_client_code]=CORP789" \
  -d "payment_details[flight_data][0][passengers][0][name]=Alice Johnson" \
  -d "payment_details[flight_data][0][passengers][1][name]=Bob Brown" \
  -d "payment_details[flight_data][0][affiliate][name]=TravelNetwork" \
  -d "payment_details[flight_data][0][affiliate][code]=TN123" \
  -d "payment_details[flight_data][0][affiliate][travel_authorization_code]=AUTH5678"
```

### Confirm a PaymentIntent

You can update `payment_details` when confirming the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). All `payment_details` updates are a full hash replacement and must be valid for your payment method. See [sending industry-specific data](https://docs.stripe.com/industry-metadata.md#send-industry-specific-data) for more information on what each property represents.

#### Car rental

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_details[car_rental_data][0][booking_number]=BOOK123456" \
  -d "payment_details[car_rental_data][0][days_rented]=3" \
  --data-urlencode "payment_details[car_rental_data][0][customer_service_phone_number]=+18005551234" \
  -d "payment_details[car_rental_data][0][renter_name]=John Doe" \
  -d "payment_details[car_rental_data][0][no_show_indicator]=false" \
  -d "payment_details[car_rental_data][0][distance][amount]=150" \
  -d "payment_details[car_rental_data][0][distance][unit]=miles" \
  -d "payment_details[car_rental_data][0][drivers][0][name]=Jane Driver" \
  -d "payment_details[car_rental_data][0][drivers][0][driver_identification_number]=D12345678" \
  -d "payment_details[car_rental_data][0][drivers][0][driver_tax_number]=TN123456789" \
  -d "payment_details[car_rental_data][0][pickup][address][line1]=123 Main St" \
  -d "payment_details[car_rental_data][0][pickup][address][postal_code]=10001" \
  -d "payment_details[car_rental_data][0][pickup][address][city]=New York" \
  -d "payment_details[car_rental_data][0][pickup][address][country]=US" \
  -d "payment_details[car_rental_data][0][pickup][address][state]=NY" \
  -d "payment_details[car_rental_data][0][pickup][address][line2]=Apt 4B" \
  -d "payment_details[car_rental_data][0][pickup][time]=1768500000" \
  -d "payment_details[car_rental_data][0][pickup][location_name]=Downtown Garage" \
  -d "payment_details[car_rental_data][0][drop_off][address][line1]=456 Elm St" \
  -d "payment_details[car_rental_data][0][drop_off][address][postal_code]=02101" \
  -d "payment_details[car_rental_data][0][drop_off][address][city]=Boston" \
  -d "payment_details[car_rental_data][0][drop_off][address][country]=US" \
  -d "payment_details[car_rental_data][0][drop_off][address][state]=MA" \
  -d "payment_details[car_rental_data][0][drop_off][address][line2]=Suite 101" \
  -d "payment_details[car_rental_data][0][drop_off][time]=1768777200" \
  -d "payment_details[car_rental_data][0][drop_off][location_name]=Airport Terminal" \
  -d "payment_details[car_rental_data][0][total][amount]=30000" \
  -d "payment_details[car_rental_data][0][total][rate_per_unit]=1500" \
  -d "payment_details[car_rental_data][0][total][rate_unit]=days" \
  -d "payment_details[car_rental_data][0][total][tax][tax_exempt_indicator]=false" \
  -d "payment_details[car_rental_data][0][total][tax][taxes][0][rate]=10" \
  -d "payment_details[car_rental_data][0][total][tax][taxes][0][amount]=3000" \
  -d "payment_details[car_rental_data][0][total][tax][taxes][0][type]=Sales Tax" \
  -d "payment_details[car_rental_data][0][total][extra_charges][0][amount]=2000" \
  -d "payment_details[car_rental_data][0][total][extra_charges][0][type]=gps" \
  -d "payment_details[car_rental_data][0][total][discounts][maximum_free_miles_or_kilometers]=100" \
  -d "payment_details[car_rental_data][0][total][discounts][corporate_client_code]=CORP123" \
  -d "payment_details[car_rental_data][0][total][discounts][coupon]=SAVE20" \
  -d "payment_details[car_rental_data][0][insurances][0][insurance_type]=liability_supplement" \
  -d "payment_details[car_rental_data][0][insurances][0][amount]=1500" \
  -d "payment_details[car_rental_data][0][vehicle][vehicle_class]=premium_economy" \
  -d "payment_details[car_rental_data][0][vehicle][type]=compact" \
  -d "payment_details[car_rental_data][0][vehicle][make]=Toyota" \
  -d "payment_details[car_rental_data][0][vehicle][model]=Camry" \
  -d "payment_details[car_rental_data][0][vehicle][vehicle_identification_number]=1HGBH41JXMN109186" \
  -d "payment_details[car_rental_data][0][vehicle][odometer]=25000" \
  -d "payment_details[car_rental_data][0][affiliate][name]=Travel Partner" \
  -d "payment_details[car_rental_data][0][affiliate][code]=TP001"
```

#### Lodging

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_details[lodging_data][0][checkin_at]=1771624800" \
  -d "payment_details[lodging_data][0][checkout_at]=1771869600" \
  -d "payment_details[lodging_data][0][booking_number]=HOTEL345678" \
  -d "payment_details[lodging_data][0][fire_safety_act_compliance_indicator]=true" \
  --data-urlencode "payment_details[lodging_data][0][customer_service_phone_number]=+12025551234" \
  -d "payment_details[lodging_data][0][renter_name]=Jane Smith" \
  -d "payment_details[lodging_data][0][renter_id_number]=ID123456789" \
  -d "payment_details[lodging_data][0][no_show_indicator]=false" \
  --data-urlencode "payment_details[lodging_data][0][host][property_phone_number]=+18005556789" \
  -d "payment_details[lodging_data][0][total][amount]=50000" \
  -d "payment_details[lodging_data][0][total][prepaid_amount]=25000" \
  -d "payment_details[lodging_data][0][total][cash_advances]=10000" \
  -d "payment_details[lodging_data][0][total][tax][tax_exempt_indicator]=false" \
  -d "payment_details[lodging_data][0][total][tax][taxes][0][rate]=10" \
  -d "payment_details[lodging_data][0][total][tax][taxes][0][amount]=5000" \
  -d "payment_details[lodging_data][0][total][tax][taxes][0][type]=City Tax" \
  -d "payment_details[lodging_data][0][total][extra_charges][0][amount]=3000" \
  -d "payment_details[lodging_data][0][total][extra_charges][0][type]=mini_bar" \
  -d "payment_details[lodging_data][0][total][discounts][corporate_client_code]=CORP456" \
  -d "payment_details[lodging_data][0][total][discounts][coupon]=WINTER10" \
  -d "payment_details[lodging_data][0][accommodation][accommodation_type]=suite" \
  -d "payment_details[lodging_data][0][accommodation][nights]=3" \
  -d "payment_details[lodging_data][0][accommodation][daily_rate_amount]=15000" \
  -d "payment_details[lodging_data][0][accommodation][rate_type]=Standard" \
  -d "payment_details[lodging_data][0][accommodation][smoking_indicator]=false" \
  -d "payment_details[lodging_data][0][accommodation][bed_type]=King" \
  -d "payment_details[lodging_data][0][affiliate][name]=Travel Network" \
  -d "payment_details[lodging_data][0][affiliate][code]=TN987"
```

#### Flight

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_details[flight_data][0][computerized_reservation_system]=GDS1" \
  -d "payment_details[flight_data][0][endorsements_and_restrictions]=NONREF" \
  -d "payment_details[flight_data][0][transaction_type]=ticket_purchase" \
  -d "payment_details[flight_data][0][ticket_electronically_issued_indicator]=true" \
  -d "payment_details[flight_data][0][segments][0][service_class]=economy" \
  -d "payment_details[flight_data][0][segments][0][carrier_code]=AA" \
  -d "payment_details[flight_data][0][segments][0][departure][airport]=JFK" \
  -d "payment_details[flight_data][0][segments][0][departure][city]=New York" \
  -d "payment_details[flight_data][0][segments][0][departure][country]=US" \
  -d "payment_details[flight_data][0][segments][0][departure][departs_at]=1781535600" \
  -d "payment_details[flight_data][0][segments][0][arrival][airport]=LAX" \
  -d "payment_details[flight_data][0][segments][0][arrival][city]=Los Angeles" \
  -d "payment_details[flight_data][0][segments][0][arrival][country]=US" \
  -d "payment_details[flight_data][0][segments][0][arrival][arrives_at]=1781557200" \
  -d "payment_details[flight_data][0][segments][0][amount]=30000" \
  -d "payment_details[flight_data][0][segments][0][currency]=USD" \
  -d "payment_details[flight_data][0][segments][0][carrier_name]=American Airlines" \
  -d "payment_details[flight_data][0][segments][0][flight_number]=AA100" \
  -d "payment_details[flight_data][0][segments][0][ticket_number]=1234567890123" \
  -d "payment_details[flight_data][0][segments][0][is_stop_over_indicator]=false" \
  -d "payment_details[flight_data][0][segments][0][fare_basis_code]=Y" \
  --data-urlencode "payment_details[flight_data][0][segments][0][exchange_ticket_number]=N/A" \
  -d "payment_details[flight_data][0][segments][0][tax_amount]=2400" \
  -d "payment_details[flight_data][0][segments][0][fees]=1500" \
  -d "payment_details[flight_data][0][segments][0][refundable]=true" \
  -d "payment_details[flight_data][0][total][amount]=120000" \
  -d "payment_details[flight_data][0][total][tax][taxes][0][rate]=8" \
  -d "payment_details[flight_data][0][total][tax][taxes][0][amount]=9600" \
  -d "payment_details[flight_data][0][total][tax][taxes][0][type]=Sales Tax" \
  -d "payment_details[flight_data][0][total][extra_charges][0][amount]=1500" \
  -d "payment_details[flight_data][0][total][extra_charges][0][type]=additional_fees" \
  -d "payment_details[flight_data][0][total][discounts][corporate_client_code]=CORP789" \
  -d "payment_details[flight_data][0][passengers][0][name]=Alice Johnson" \
  -d "payment_details[flight_data][0][passengers][1][name]=Bob Brown" \
  -d "payment_details[flight_data][0][affiliate][name]=TravelNetwork" \
  -d "payment_details[flight_data][0][affiliate][code]=TN123" \
  -d "payment_details[flight_data][0][affiliate][travel_authorization_code]=AUTH5678"
```

### Capture a PaymentIntent

You can include and update `payment_details` when capturing the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). Make sure the data you provide is complete because `payment_details` can’t be modified after a PaymentIntent is captured. See [sending industry-specific data](https://docs.stripe.com/industry-metadata.md#send-industry-specific-data) for more information on what each property represents.

#### Car rental

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/capture \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_details[car_rental_data][0][booking_number]=BOOK123456" \
  -d "payment_details[car_rental_data][0][days_rented]=3" \
  --data-urlencode "payment_details[car_rental_data][0][customer_service_phone_number]=+18005551234" \
  -d "payment_details[car_rental_data][0][renter_name]=John Doe" \
  -d "payment_details[car_rental_data][0][no_show_indicator]=false" \
  -d "payment_details[car_rental_data][0][distance][amount]=150" \
  -d "payment_details[car_rental_data][0][distance][unit]=miles" \
  -d "payment_details[car_rental_data][0][drivers][0][name]=Jane Driver" \
  -d "payment_details[car_rental_data][0][drivers][0][driver_identification_number]=D12345678" \
  -d "payment_details[car_rental_data][0][drivers][0][driver_tax_number]=TN123456789" \
  -d "payment_details[car_rental_data][0][pickup][address][line1]=123 Main St" \
  -d "payment_details[car_rental_data][0][pickup][address][postal_code]=10001" \
  -d "payment_details[car_rental_data][0][pickup][address][city]=New York" \
  -d "payment_details[car_rental_data][0][pickup][address][country]=US" \
  -d "payment_details[car_rental_data][0][pickup][address][state]=NY" \
  -d "payment_details[car_rental_data][0][pickup][address][line2]=Apt 4B" \
  -d "payment_details[car_rental_data][0][pickup][time]=1768500000" \
  -d "payment_details[car_rental_data][0][pickup][location_name]=Downtown Garage" \
  -d "payment_details[car_rental_data][0][drop_off][address][line1]=456 Elm St" \
  -d "payment_details[car_rental_data][0][drop_off][address][postal_code]=02101" \
  -d "payment_details[car_rental_data][0][drop_off][address][city]=Boston" \
  -d "payment_details[car_rental_data][0][drop_off][address][country]=US" \
  -d "payment_details[car_rental_data][0][drop_off][address][state]=MA" \
  -d "payment_details[car_rental_data][0][drop_off][address][line2]=Suite 101" \
  -d "payment_details[car_rental_data][0][drop_off][time]=1768777200" \
  -d "payment_details[car_rental_data][0][drop_off][location_name]=Airport Terminal" \
  -d "payment_details[car_rental_data][0][total][amount]=30000" \
  -d "payment_details[car_rental_data][0][total][rate_per_unit]=1500" \
  -d "payment_details[car_rental_data][0][total][rate_unit]=days" \
  -d "payment_details[car_rental_data][0][total][tax][tax_exempt_indicator]=false" \
  -d "payment_details[car_rental_data][0][total][tax][taxes][0][rate]=10" \
  -d "payment_details[car_rental_data][0][total][tax][taxes][0][amount]=3000" \
  -d "payment_details[car_rental_data][0][total][tax][taxes][0][type]=Sales Tax" \
  -d "payment_details[car_rental_data][0][total][extra_charges][0][amount]=2000" \
  -d "payment_details[car_rental_data][0][total][extra_charges][0][type]=gps" \
  -d "payment_details[car_rental_data][0][total][discounts][maximum_free_miles_or_kilometers]=100" \
  -d "payment_details[car_rental_data][0][total][discounts][corporate_client_code]=CORP123" \
  -d "payment_details[car_rental_data][0][total][discounts][coupon]=SAVE20" \
  -d "payment_details[car_rental_data][0][insurances][0][insurance_type]=liability_supplement" \
  -d "payment_details[car_rental_data][0][insurances][0][amount]=1500" \
  -d "payment_details[car_rental_data][0][vehicle][vehicle_class]=premium_economy" \
  -d "payment_details[car_rental_data][0][vehicle][type]=compact" \
  -d "payment_details[car_rental_data][0][vehicle][make]=Toyota" \
  -d "payment_details[car_rental_data][0][vehicle][model]=Camry" \
  -d "payment_details[car_rental_data][0][vehicle][vehicle_identification_number]=1HGBH41JXMN109186" \
  -d "payment_details[car_rental_data][0][vehicle][odometer]=25000" \
  -d "payment_details[car_rental_data][0][affiliate][name]=Travel Partner" \
  -d "payment_details[car_rental_data][0][affiliate][code]=TP001"
```

#### Lodging

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/capture \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_details[lodging_data][0][checkin_at]=1771624800" \
  -d "payment_details[lodging_data][0][checkout_at]=1771869600" \
  -d "payment_details[lodging_data][0][booking_number]=HOTEL345678" \
  -d "payment_details[lodging_data][0][fire_safety_act_compliance_indicator]=true" \
  --data-urlencode "payment_details[lodging_data][0][customer_service_phone_number]=+12025551234" \
  -d "payment_details[lodging_data][0][renter_name]=Jane Smith" \
  -d "payment_details[lodging_data][0][renter_id_number]=ID123456789" \
  -d "payment_details[lodging_data][0][no_show_indicator]=false" \
  --data-urlencode "payment_details[lodging_data][0][host][property_phone_number]=+18005556789" \
  -d "payment_details[lodging_data][0][total][amount]=50000" \
  -d "payment_details[lodging_data][0][total][prepaid_amount]=25000" \
  -d "payment_details[lodging_data][0][total][cash_advances]=10000" \
  -d "payment_details[lodging_data][0][total][tax][tax_exempt_indicator]=false" \
  -d "payment_details[lodging_data][0][total][tax][taxes][0][rate]=10" \
  -d "payment_details[lodging_data][0][total][tax][taxes][0][amount]=5000" \
  -d "payment_details[lodging_data][0][total][tax][taxes][0][type]=City Tax" \
  -d "payment_details[lodging_data][0][total][extra_charges][0][amount]=3000" \
  -d "payment_details[lodging_data][0][total][extra_charges][0][type]=mini_bar" \
  -d "payment_details[lodging_data][0][total][discounts][corporate_client_code]=CORP456" \
  -d "payment_details[lodging_data][0][total][discounts][coupon]=WINTER10" \
  -d "payment_details[lodging_data][0][accommodation][accommodation_type]=suite" \
  -d "payment_details[lodging_data][0][accommodation][nights]=3" \
  -d "payment_details[lodging_data][0][accommodation][daily_rate_amount]=15000" \
  -d "payment_details[lodging_data][0][accommodation][rate_type]=Standard" \
  -d "payment_details[lodging_data][0][accommodation][smoking_indicator]=false" \
  -d "payment_details[lodging_data][0][accommodation][bed_type]=King" \
  -d "payment_details[lodging_data][0][affiliate][name]=Travel Network" \
  -d "payment_details[lodging_data][0][affiliate][code]=TN987"
```

#### Flight

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/capture \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_details[flight_data][0][computerized_reservation_system]=GDS1" \
  -d "payment_details[flight_data][0][endorsements_and_restrictions]=NONREF" \
  -d "payment_details[flight_data][0][transaction_type]=ticket_purchase" \
  -d "payment_details[flight_data][0][ticket_electronically_issued_indicator]=true" \
  -d "payment_details[flight_data][0][segments][0][service_class]=economy" \
  -d "payment_details[flight_data][0][segments][0][carrier_code]=AA" \
  -d "payment_details[flight_data][0][segments][0][departure][airport]=JFK" \
  -d "payment_details[flight_data][0][segments][0][departure][city]=New York" \
  -d "payment_details[flight_data][0][segments][0][departure][country]=US" \
  -d "payment_details[flight_data][0][segments][0][departure][departs_at]=1781535600" \
  -d "payment_details[flight_data][0][segments][0][arrival][airport]=LAX" \
  -d "payment_details[flight_data][0][segments][0][arrival][city]=Los Angeles" \
  -d "payment_details[flight_data][0][segments][0][arrival][country]=US" \
  -d "payment_details[flight_data][0][segments][0][arrival][arrives_at]=1781557200" \
  -d "payment_details[flight_data][0][segments][0][amount]=30000" \
  -d "payment_details[flight_data][0][segments][0][currency]=USD" \
  -d "payment_details[flight_data][0][segments][0][carrier_name]=American Airlines" \
  -d "payment_details[flight_data][0][segments][0][flight_number]=AA100" \
  -d "payment_details[flight_data][0][segments][0][ticket_number]=1234567890123" \
  -d "payment_details[flight_data][0][segments][0][is_stop_over_indicator]=false" \
  -d "payment_details[flight_data][0][segments][0][fare_basis_code]=Y" \
  --data-urlencode "payment_details[flight_data][0][segments][0][exchange_ticket_number]=N/A" \
  -d "payment_details[flight_data][0][segments][0][tax_amount]=2400" \
  -d "payment_details[flight_data][0][segments][0][fees]=1500" \
  -d "payment_details[flight_data][0][segments][0][refundable]=true" \
  -d "payment_details[flight_data][0][total][amount]=120000" \
  -d "payment_details[flight_data][0][total][tax][taxes][0][rate]=8" \
  -d "payment_details[flight_data][0][total][tax][taxes][0][amount]=9600" \
  -d "payment_details[flight_data][0][total][tax][taxes][0][type]=Sales Tax" \
  -d "payment_details[flight_data][0][total][extra_charges][0][amount]=1500" \
  -d "payment_details[flight_data][0][total][extra_charges][0][type]=additional_fees" \
  -d "payment_details[flight_data][0][total][discounts][corporate_client_code]=CORP789" \
  -d "payment_details[flight_data][0][passengers][0][name]=Alice Johnson" \
  -d "payment_details[flight_data][0][passengers][1][name]=Bob Brown" \
  -d "payment_details[flight_data][0][affiliate][name]=TravelNetwork" \
  -d "payment_details[flight_data][0][affiliate][code]=TN123" \
  -d "payment_details[flight_data][0][affiliate][travel_authorization_code]=AUTH5678"
```

### Multiple travel methods

You can also add multiple types of industry data to a single `payment_details` object to provide information about transactions involving several legs of travel. See [sending industry-specific data](https://docs.stripe.com/industry-metadata.md#send-industry-specific-data) for more information on what each property represents.

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=200 \
  -d currency=usd \
  -d "payment_method_types[0]=card" \
  -d "payment_details[car_rental_data][0][booking_number]=BOOK123456" \
  -d "payment_details[car_rental_data][0][days_rented]=3" \
  --data-urlencode "payment_details[car_rental_data][0][customer_service_phone_number]=+18005551234" \
  -d "payment_details[car_rental_data][0][renter_name]=John Doe" \
  -d "payment_details[car_rental_data][0][no_show_indicator]=false" \
  -d "payment_details[car_rental_data][0][distance][amount]=150" \
  -d "payment_details[car_rental_data][0][distance][unit]=miles" \
  -d "payment_details[car_rental_data][0][drivers][0][name]=Jane Driver" \
  -d "payment_details[car_rental_data][0][drivers][0][driver_identification_number]=D12345678" \
  -d "payment_details[car_rental_data][0][drivers][0][driver_tax_number]=TN123456789" \
  -d "payment_details[car_rental_data][0][pickup][address][line1]=123 Main St" \
  -d "payment_details[car_rental_data][0][pickup][address][postal_code]=10001" \
  -d "payment_details[car_rental_data][0][pickup][address][city]=New York" \
  -d "payment_details[car_rental_data][0][pickup][address][country]=US" \
  -d "payment_details[car_rental_data][0][pickup][address][state]=NY" \
  -d "payment_details[car_rental_data][0][pickup][address][line2]=Apt 4B" \
  -d "payment_details[car_rental_data][0][pickup][time]=1768500000" \
  -d "payment_details[car_rental_data][0][pickup][location_name]=Downtown Garage" \
  -d "payment_details[car_rental_data][0][drop_off][address][line1]=456 Elm St" \
  -d "payment_details[car_rental_data][0][drop_off][address][postal_code]=02101" \
  -d "payment_details[car_rental_data][0][drop_off][address][city]=Boston" \
  -d "payment_details[car_rental_data][0][drop_off][address][country]=US" \
  -d "payment_details[car_rental_data][0][drop_off][address][state]=MA" \
  -d "payment_details[car_rental_data][0][drop_off][address][line2]=Suite 101" \
  -d "payment_details[car_rental_data][0][drop_off][time]=1768777200" \
  -d "payment_details[car_rental_data][0][drop_off][location_name]=Airport Terminal" \
  -d "payment_details[car_rental_data][0][total][amount]=30000" \
  -d "payment_details[car_rental_data][0][total][rate_per_unit]=1500" \
  -d "payment_details[car_rental_data][0][total][rate_unit]=days" \
  -d "payment_details[car_rental_data][0][total][tax][tax_exempt_indicator]=false" \
  -d "payment_details[car_rental_data][0][total][tax][taxes][0][rate]=10" \
  -d "payment_details[car_rental_data][0][total][tax][taxes][0][amount]=3000" \
  -d "payment_details[car_rental_data][0][total][tax][taxes][0][type]=Sales Tax" \
  -d "payment_details[car_rental_data][0][total][extra_charges][0][amount]=2000" \
  -d "payment_details[car_rental_data][0][total][extra_charges][0][type]=gps" \
  -d "payment_details[car_rental_data][0][total][discounts][maximum_free_miles_or_kilometers]=100" \
  -d "payment_details[car_rental_data][0][total][discounts][corporate_client_code]=CORP123" \
  -d "payment_details[car_rental_data][0][total][discounts][coupon]=SAVE20" \
  -d "payment_details[car_rental_data][0][insurances][0][insurance_type]=liability_supplement" \
  -d "payment_details[car_rental_data][0][insurances][0][amount]=1500" \
  -d "payment_details[car_rental_data][0][vehicle][vehicle_class]=premium_economy" \
  -d "payment_details[car_rental_data][0][vehicle][type]=compact" \
  -d "payment_details[car_rental_data][0][vehicle][make]=Toyota" \
  -d "payment_details[car_rental_data][0][vehicle][model]=Camry" \
  -d "payment_details[car_rental_data][0][vehicle][vehicle_identification_number]=1HGBH41JXMN109186" \
  -d "payment_details[car_rental_data][0][vehicle][odometer]=25000" \
  -d "payment_details[car_rental_data][0][affiliate][name]=Travel Partner" \
  -d "payment_details[car_rental_data][0][affiliate][code]=TP001" \
  -d "payment_details[lodging_data][0][checkin_at]=1771624800" \
  -d "payment_details[lodging_data][0][checkout_at]=1771869600" \
  -d "payment_details[lodging_data][0][booking_number]=HOTEL345678" \
  -d "payment_details[lodging_data][0][fire_safety_act_compliance_indicator]=true" \
  --data-urlencode "payment_details[lodging_data][0][customer_service_phone_number]=+12025551234" \
  -d "payment_details[lodging_data][0][renter_name]=Jane Smith" \
  -d "payment_details[lodging_data][0][renter_id_number]=ID123456789" \
  -d "payment_details[lodging_data][0][no_show_indicator]=false" \
  --data-urlencode "payment_details[lodging_data][0][host][property_phone_number]=+18005556789" \
  -d "payment_details[lodging_data][0][total][amount]=50000" \
  -d "payment_details[lodging_data][0][total][prepaid_amount]=25000" \
  -d "payment_details[lodging_data][0][total][cash_advances]=10000" \
  -d "payment_details[lodging_data][0][total][tax][tax_exempt_indicator]=false" \
  -d "payment_details[lodging_data][0][total][tax][taxes][0][rate]=10" \
  -d "payment_details[lodging_data][0][total][tax][taxes][0][amount]=5000" \
  -d "payment_details[lodging_data][0][total][tax][taxes][0][type]=City Tax" \
  -d "payment_details[lodging_data][0][total][extra_charges][0][amount]=3000" \
  -d "payment_details[lodging_data][0][total][extra_charges][0][type]=mini_bar" \
  -d "payment_details[lodging_data][0][total][discounts][corporate_client_code]=CORP456" \
  -d "payment_details[lodging_data][0][total][discounts][coupon]=WINTER10" \
  -d "payment_details[lodging_data][0][accommodation][accommodation_type]=suite" \
  -d "payment_details[lodging_data][0][accommodation][nights]=3" \
  -d "payment_details[lodging_data][0][accommodation][daily_rate_amount]=15000" \
  -d "payment_details[lodging_data][0][accommodation][rate_type]=Standard" \
  -d "payment_details[lodging_data][0][accommodation][smoking_indicator]=false" \
  -d "payment_details[lodging_data][0][accommodation][bed_type]=King" \
  -d "payment_details[lodging_data][0][affiliate][name]=Travel Network" \
  -d "payment_details[lodging_data][0][affiliate][code]=TN987"
```

## Testing

Test that your integration works correctly for your customers. You can simulate API calls in a Stripe [Sandbox](https://docs.stripe.com/sandboxes.md) using a sandbox key. For additional information, see [Testing](https://docs.stripe.com/testing.md).

During testing, you can verify the following:

- Your industry metadata is properly formatted and accepted by the API
- Required fields are present for your payment method (cards or Klarna)
- The [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) successfully processes with your metadata

Sandbox testing verifies that your integration is technically correct, but doesn’t simulate card network interchange qualification decisions or Klarna’s authorization rates and risk assessment outcomes.
