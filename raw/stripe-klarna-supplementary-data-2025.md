<!-- Source URL: https://docs.stripe.com/payments/klarna/supplementary-purchase-data -->
<!-- Fetched: 2026-05-06 -->

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

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "eur",
  payment_method_types: ["klarna"],
  payment_method_options: {
    klarna: {
      supplementary_purchase_data: {
        vouchers: [
          {
            voucher_name: "Holiday Gift Card",
          },
        ],
      },
    },
  },
});
```

### Example: Create a PaymentIntent with multiple verticals

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 15000,
  currency: "eur",
  payment_method_types: ["klarna"],
  payment_method_options: {
    klarna: {
      supplementary_purchase_data: {
        vouchers: [
          {
            voucher_name: "Gift Card",
          },
        ],
        insurances: [
          {
            insurance_type: "cancelation",
            price: 2000,
            currency: "EUR",
          },
        ],
      },
    },
  },
});
```

## Vertical data formats

The following tabs describe the hashes for the supported verticals:

#### Insurance

Insurance data is sent through the `payment_method_options.klarna.supplementary_purchase_data.insurances` parameter. Each element in the array represents an individual insurance policy purchased as the primary product (not as an add-on to another service).

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-insurances) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with insurance data

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  payment_method_types: ["klarna"],
  payment_method_options: {
    klarna: {
      supplementary_purchase_data: {
        insurances: [
          {
            insurance_type: "medical",
            insurance_company_name: "Global Medical Insurance",
            price: 5000,
            currency: "USD",
          },
        ],
      },
    },
  },
});
```

#### Vouchers

Voucher data is sent through the `payment_method_options.klarna.supplementary_purchase_data.vouchers` parameter. Each element in the array represents an individual voucher, such as a gift card or discount code.

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-vouchers) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with voucher data

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "usd",
  payment_method_types: ["klarna"],
  payment_method_options: {
    klarna: {
      supplementary_purchase_data: {
        vouchers: [
          {
            voucher_name: "Holiday Gift Card 2025",
            voucher_type: "gift_card",
            voucher_company: "Retail Store Inc",
            starts_at: 1735689600,
            ends_at: 1767225600,
            affiliate_name: "Partner Retailer",
          },
        ],
      },
    },
  },
});
```

#### Events

Event data is sent through the `payment_method_options.klarna.supplementary_purchase_data.event_reservation_details` parameter. Each element in the array represents an individual event ticket or reservation.

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-event_reservation_details) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with event data

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 15000,
  currency: "usd",
  payment_method_types: ["klarna"],
  payment_method_options: {
    klarna: {
      supplementary_purchase_data: {
        event_reservation_details: [
          {
            event_name: "Summer Music Festival 2025",
            event_company_name: "Stripe Example Entertainment",
            event_type: "festival",
            starts_at: 1751328000,
            ends_at: 1751414400,
            venue_name: "Central Park",
            access_controlled_venue: true,
            address: {
              street_address: "Central Park West",
              city: "New York",
              region: "NY",
              postal_code: "10024",
              country: "US",
            },
            affiliate_name: "Ticketvendor",
            insurances: [
              {
                insurance_type: "cancelation",
                insurance_company_name: "Event Insurance Co",
                price: 2000,
                currency: "USD",
              },
            ],
          },
        ],
      },
    },
  },
});
```

#### Train

Train reservation data is sent through the `payment_method_options.klarna.supplementary_purchase_data.train_reservation_details` parameter. Each element in the array represents an individual train ticket or reservation.

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-train_reservation_details) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with train data

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 8500,
  currency: "eur",
  payment_method_types: ["klarna"],
  payment_method_options: {
    klarna: {
      supplementary_purchase_data: {
        train_reservation_details: [
          {
            carrier_name: "Eurotrains",
            ticket_class: "business",
            price: 8500,
            currency: "EUR",
            departure: {
              departure_location: "Paris Gare du Nord",
              departs_at: 1751324400,
              address: {
                street_address: "18 Rue de Dunkerque",
                city: "Paris",
                postal_code: "75010",
                country: "FR",
              },
            },
            arrival: {
              arrival_location: "London St Pancras International",
              address: {
                street_address: "Pancras Road",
                city: "London",
                postal_code: "N1C 4QP",
                country: "GB",
              },
            },
            passengers: [
              {
                given_name: "Jane",
                family_name: "Smith",
              },
            ],
            insurances: [
              {
                insurance_type: "cancelation",
                insurance_company_name: "Travel Insurance Ltd",
                price: 1500,
                currency: "EUR",
              },
            ],
            affiliate_name: "Rail Travel Partners",
          },
        ],
      },
    },
  },
});
```

#### Bus

Bus reservation data is sent through the `payment_method_options.klarna.supplementary_purchase_data.bus_reservation_details` parameter. Each element in the array represents an individual bus ticket or reservation.

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-bus_reservation_details) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with bus data

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 4500,
  currency: "usd",
  payment_method_types: ["klarna"],
  payment_method_options: {
    klarna: {
      supplementary_purchase_data: {
        bus_reservation_details: [
          {
            carrier_name: "Fastdog",
            ticket_class: "economy",
            price: 4500,
            currency: "USD",
            departure: {
              departure_location: "New York Port Authority",
              departs_at: 1751356800,
              address: {
                street_address: "625 8th Avenue",
                city: "New York",
                region: "NY",
                postal_code: "10018",
                country: "US",
              },
            },
            arrival: {
              arrival_location: "Boston South Station",
              address: {
                street_address: "700 Atlantic Avenue",
                city: "Boston",
                region: "MA",
                postal_code: "02110",
                country: "US",
              },
            },
            passengers: [
              {
                given_name: "John",
                family_name: "Doe",
              },
            ],
            insurances: [
              {
                insurance_type: "cancelation",
                insurance_company_name: "Bus Travel Insurance",
                price: 500,
                currency: "USD",
              },
            ],
            affiliate_name: "Travel Booking Agency",
          },
        ],
      },
    },
  },
});
```

#### Ferry

Ferry reservation data is sent through the `payment_method_options.klarna.supplementary_purchase_data.ferry_reservation_details` parameter. Each element in the array represents an individual ferry ticket or reservation.

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-ferry_reservation_details) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with ferry data

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 6500,
  currency: "eur",
  payment_method_types: ["klarna"],
  payment_method_options: {
    klarna: {
      supplementary_purchase_data: {
        ferry_reservation_details: [
          {
            carrier_name: "Ferry Line",
            ticket_class: "economy",
            price: 6500,
            currency: "EUR",
            departure: {
              departure_location: "Dover Ferry Terminal",
              departs_at: 1751389200,
              address: {
                street_address: "Eastern Docks",
                city: "Dover",
                postal_code: "CT17 9BU",
                country: "GB",
              },
            },
            arrival: {
              arrival_location: "Calais Ferry Terminal",
              address: {
                street_address: "Port de Calais",
                city: "Calais",
                postal_code: "62100",
                country: "FR",
              },
            },
            passengers: [
              {
                given_name: "Alice",
                family_name: "Johnson",
              },
            ],
            insurances: [
              {
                insurance_type: "cancelation",
                insurance_company_name: "Ferry Travel Insurance",
                price: 800,
                currency: "EUR",
              },
            ],
            affiliate_name: "Channel Crossing Bookings",
          },
        ],
      },
    },
  },
});
```

#### Organized trips and tours

Organized trip reservation data is sent through the `payment_method_options.klarna.supplementary_purchase_data.round_trip_reservation_details` parameter. Each element in the array represents an individual trip ticket or reservation.

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-round_trip_reservation_details) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with organized trip data

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 12000,
  currency: "usd",
  payment_method_types: ["klarna"],
  payment_method_options: {
    klarna: {
      supplementary_purchase_data: {
        round_trip_reservation_details: [
          {
            carrier_name: "Traintrak",
            ticket_class: "premium_economy",
            price: 12000,
            currency: "USD",
            departure: {
              departure_location: "Chicago Union Station",
              departs_at: 1751421600,
              address: {
                street_address: "225 S Canal St",
                city: "Chicago",
                region: "IL",
                postal_code: "60606",
                country: "US",
              },
            },
            arrival: {
              arrival_location: "Los Angeles Union Station",
              address: {
                street_address: "800 N Alameda St",
                city: "Los Angeles",
                region: "CA",
                postal_code: "90012",
                country: "US",
              },
            },
            passengers: [
              {
                given_name: "Michael",
                family_name: "Brown",
              },
            ],
            insurances: [
              {
                insurance_type: "cancelation",
                insurance_company_name: "Travel Guard",
                price: 1200,
                currency: "USD",
              },
            ],
            affiliate_name: "Rail Pass America",
          },
        ],
      },
    },
  },
});
```

#### Marketplace sellers

Marketplace seller data is sent through the `payment_method_options.klarna.supplementary_purchase_data.marketplace_sellers` parameter. Each element in the array represents information about an individual seller in a marketplace transaction.

For the full list of fields and their formats, see the [API reference](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data-marketplace_sellers) (available with the `2025-11-17.preview` or later preview version header).

##### Example: Creating a PaymentIntent with marketplace seller data

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 25000,
  currency: "usd",
  payment_method_types: ["klarna"],
  payment_method_options: {
    klarna: {
      supplementary_purchase_data: {
        marketplace_sellers: [
          {
            marketplace_seller_reference: "seller_12345",
            marketplace_seller_name: "Artisan Crafts Shop",
            marketplace_seller_address: {
              street_address: "123 Market Street",
              city: "Portland",
              region: "OR",
              postal_code: "97204",
              country: "US",
            },
            product_category: "handmade",
            seller_registered_at: 1672531200,
            seller_rating: "high",
            number_of_transactions: 150,
            volume_of_transactions: 3500000,
          },
        ],
      },
    },
  },
});
```

## Update and remove supplementary purchase data

Use the [update](https://docs.stripe.com/api/payment_intents/update.md) or [confirm](https://docs.stripe.com/api/payment_intents/confirm.md) method to modify or remove supplementary purchase data.

### Full replacement of verticals

When you update a vertical’s array, the new data completely replaces the existing data for that vertical. For example, if a PaymentIntent has 2 vouchers and you send an update with 1 voucher, the result is 1 voucher (not 3).

Create a PaymentIntent with 2 vouchers:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "eur",
  payment_method_types: ["klarna"],
  payment_method_options: {
    klarna: {
      supplementary_purchase_data: {
        vouchers: [
          {
            voucher_name: "First Voucher",
          },
          {
            voucher_name: "Second Voucher",
          },
        ],
      },
    },
  },
});
```

Update the PaymentIntent with one voucher to replace the existing two vouchers:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.update(
  "{{PAYMENTINTENT_ID}}",
  {
    payment_method_options: {
      klarna: {
        supplementary_purchase_data: {
          vouchers: [
            {
              voucher_name: "Replacement Voucher",
            },
          ],
        },
      },
    },
  },
);
```

The PaymentIntent now has only one voucher.

### Preserve existing data

Verticals excluded in an update request remain unchanged. For example, you can add train data without affecting existing vouchers or insurances:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.update(
  "{{PAYMENTINTENT_ID}}",
  {
    payment_method_options: {
      klarna: {
        supplementary_purchase_data: {
          train_reservation_details: [
            {
              carrier_name: "Eurotrains",
              ticket_class: "business",
              price: 8500,
              currency: "EUR",
            },
          ],
        },
      },
    },
  },
);
```

The PaymentIntent retains existing vouchers and insurances, and adds the train reservation.

### Unset a specific vertical

To unset all data for a specific vertical while preserving other verticals, set the vertical to an empty string. This removes the vertical from the PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.update(
  "{{PAYMENTINTENT_ID}}",
  {
    payment_method_options: {
      klarna: {
        supplementary_purchase_data: {
          insurances: "",
        },
      },
    },
  },
);
```

### Unset all supplementary purchase data

To unset all supplementary purchase data from a PaymentIntent, set the entire `supplementary_purchase_data` parameter to an empty string:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.update(
  "{{PAYMENTINTENT_ID}}",
  {
    payment_method_options: {
      klarna: {
        supplementary_purchase_data: "",
      },
    },
  },
);
```

## Testing

Test that your integration works correctly for your customers. Simulate API calls in a Stripe [Sandbox](https://docs.stripe.com/sandboxes.md) with a sandbox key. Attach a payment method using the [update](https://docs.stripe.com/api/payment_intents/update.md) method prior to confirming. For additional information, see [Testing](https://docs.stripe.com/testing.md).
