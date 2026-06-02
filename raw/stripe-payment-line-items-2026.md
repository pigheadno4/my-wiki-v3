<!-- Source URL: https://docs.stripe.com/payments/payment-line-items -->
<!-- Fetched: 2026-05-11 -->

# Payment line items

Send additional transaction metadata across supported Payment Method Types to access cost savings, facilitate payment reconciliation, and improve auth rates.

Payment line items is a feature in the Payment Intents API that provides benefits for cards and _local payment methods_ (Payment methods used in specific countries or regions, such as bank transfers, vouchers, and digital wallets. Examples include Pix (Brazil, bank transfers), Konbini (Japan, vouchers), and WeChat Pay (China, digital wallet)) processing.

- **Cost savings for eligible commercial cards for _IC+ users_ (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs):** By passing payment line items, you can participate in the Level 2/Level 3/Product 3 (L2/L3) program that major card networks administer. For eligible commercial cards, passing line item data can provide interchange fee savings.
- **Facilitate reconciliation:** Passing line item data can also facilitate reconciliation for your customers. For example, if you primarily serve government customers, it will aid the customer in reconciling a purchase against what shows up on their statement.
- **Improved authorization rates:** Payment methods like Klarna and PayPal use line item data in their underwriting models, potentially allowing them to approve more credit based payment options when line items data is passed.

## Feature restrictions

Payment line items have the following restrictions across supported payment method types:

|                         | Cards L2/L3 program                                                                                                                                                                                   | Klarna                                                                                                                               | PayPal                                                                                                                                      |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Geographic availability | Supported for US domestic transactions (US users accepting US issued cards, excluding US territories), and intra-EU transactions (EU businesses accepting EU cards).                                  | Klarna is a global payment method. For business location support, see [Klarna payments](https://docs.stripe.com/payments/klarna.md). | Available for customers in all locations. For business location support, see [PayPal payments](https://docs.stripe.com/payments/paypal.md). |
| Card networks           | Only supported for Visa, Mastercard, and American Express (cost savings requires direct agreement with American Express)                                                                              | Not applicable                                                                                                                       | Not applicable                                                                                                                              |
| Number of line items    | Currently supports 200 line items. (American Express Specification restricts us to send them only the first 4 line items.)                                                                            | Same as cards                                                                                                                        | Same as cards                                                                                                                               |
| Feature compatibility   | Both _automatic capture_ (Automatically capture funds when a charge is authorized) and _manual capture_ (Manually capture funds separately from an authorization) modes work with payment line items. |

[Flexible payment scenarios](https://docs.stripe.com/payments/flexible-payments.md) except [partial authorization](https://docs.stripe.com/payments/partial-authorization.md) and decrement authorization [work with payment line items](https://docs.stripe.com/payments/payment-line-items/flexible-payment-scenarios.md) for payments where you’re passing in line items. | Both _automatic capture_ (Automatically capture funds when a charge is authorized) and _manual capture_ (Manually capture funds separately from an authorization) modes work with payment line items. | Both _automatic capture_ (Automatically capture funds when a charge is authorized) and _manual capture_ (Manually capture funds separately from an authorization) modes work with payment line items. |
| Industry specific metadata | You can’t send line items alongside industry specific metadata such as car rental/lodging, and airlines | Klarna supports industry specific metadata with Extra Merchant Data (private preview). | Same as cards |
| APIs | Available for payments made through the [PaymentIntents API](https://docs.stripe.com/payments/payment-intents.md). | Same as cards | Same as cards |

## Cards L2 and L3 Rates Eligibility

> #### Visa CEDP Program
>
> To learn more about Visa’s Commercial Enhanced Data Program (CEDP), which replaces their U.S. Level 2/3 interchange programs, including information about its network fees, see the [CEDP Support article](<https://support.stripe.com/questions/understand-the-visa-commercial-enhanced-data-program-(cedp)>).

See [Industry to MCC codes](https://docs.stripe.com/payments/payment-line-items.md#industry-to-mcc-codes) to see what MCC your business might fall under.

Stripe API doesn’t reject line items that don’t meet the network MCC and/or tax requirements, but these transactions don’t qualify for the corresponding Level 2/3 savings.

| Cards L2/L3 Rates Eligibility | Level 2                                                     | Level 3/Product 3                                |
| ----------------------------- | ----------------------------------------------------------- | ------------------------------------------------ |
| Card types                    | Only Business, Purchasing, and Corporate cards are eligible | Only Purchasing and Corporate cards are eligible |
| MCCs                          | Users with the following MCCs aren’t eligible for Level 2:  |

- For **Mastercard**: 5812, 3501-3999, 7011, 3351-3500, 7512, 7513, 7519, 3000-3299, 4511, 4112
- For **Visa**: 5812, 5814, 3501-4010, 3351-3500, 7512, 7513, 3000-3299, 4511, 4411, 4112, 4722, 5962, 5966, and 5967 | Users with the following MCCs aren’t eligible for Level 3/Product 3:
- For **Mastercard**: 5812, 3501-3999, 7011, 3351-3500, 7512, 7513, 7519, 3000-3299, 4511, 4112, 8398, 4468, 5499, 5541, 5542, 5983
- For **Visa**: 5812, 5814, 3501-4010, 3351-3500, 7512, 7513, 3000-3299, 4511, 4411, 4112, 4722, 5962, 5966, and 5967 |
  | Sales tax requirement | - For **Mastercard**: sales tax must be between 0.1% and 30%, unless the business is using one of the following MCCs - 4468, 5541, 5542, 5499, 5983, 7511, 9752, 4111, 4131, 4215, 4784, 8211, 8220, 8398, 8661, 9211, 9222, 9311, 9399, or 9402
- For **Visa**: sales tax must be between 0.1% and 22% unless the business is using one of the following MCCs - 4468, 5499, 5541, 5542, or 5983 | Not required for Level 3/Product 3 rates. 0 is acceptable if no sales tax is collected but an accurate value must be reported. |

The following fields are required in order to receive L2 or L3 rates.

#### Payment Intents API

| Cards L2 or L3 Rates Eligibility   | Level 2                   | Level 3/Product 3 |
| ---------------------------------- | ------------------------- | ----------------- |
| Minimum Field Requirements         | - tax[total_tax_amount]   |
| - payment_details[order_reference] | - line_item[product_name] |

- line_item[unit_cost]
- line_item[quantity]
- line_item[tax][total_tax_amount]
- line_item[product_code]
- line_item[unit_of_measure]
- payment_details[order_reference] |

#### Checkout Sessions API

| Cards L2 or L3 Rates Eligibility | Level 2                                                                   | Level 3                                                                                                                      |
| -------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Minimum Field Requirements       | - N/A, Checkout populates the tax and order reference based on line items | - [line_item[quantity]](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-quantity) |

- [line_item[price][unit_amount]](https://docs.stripe.com/api/prices/object.md#price_object-unit_amount)
- [line_item[price][product]](https://docs.stripe.com/api/prices/object.md#price_object-product)
- [line_item[price][product][name]](https://docs.stripe.com/api/products/object.md#product_object-name)
- [line_item[price][product][unit_label]](https://docs.stripe.com/api/products/object.md#product_object-unit_label) |

## Field Requirements

All the fields mentioned below are passed within the [amount_details](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-amount_details) or [payment_details](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_details) parameters. Refer to [Sample request (Level 2 data)](https://docs.stripe.com/payments/payment-line-items.md#sample-request-level-2-data) to learn about passing data.

“Required field” indicates a field is required to pass Stripe validations when any line item data is populated. “Required for L2 or L3” indicates a field is required to receive network L2/L3 rates.

### General supported fields

| Field Name              | Type   | Description                        | Format           |
| ----------------------- | ------ | ---------------------------------- | ---------------- |
| line_item[product_name] | string | The product name of the line item. | - Required field |

- Required for L3
- Max length 1024 chars (Cards truncates to 26 alphanumeric characters and Paypal truncates to 127 characters) |
  | line_item[unit_cost] | integer | The unit cost of the line item represented in the [smallest currency unit](https://docs.stripe.com/currencies.md#zero-decimal) | - Required field
- Required for L3
- Value must be >= 0 |
  | line_item[quantity] | integer | The quantity of items. | - Required field
- Required for L3
- Value must be > 0 |
  | line_item[tax][total_tax_amount] | integer | The total amount of tax on a single line item represented in the [smallest currency unit](https://docs.stripe.com/currencies.md#zero-decimal) | - Required for L3
- Value must be >= 0
- Conditional validation 1 |
  | line_item[product_code] | string | The product code of the line item, such as an SKU | - Required for L3
- Max length 12 chars |
  | line_item[unit_of_measure] | string | A unit of measure for the line item, such as gallons, feet, meters, generic measurements (such as each), and so on | - Required for L3
- Max length 12 chars
- Alphanumeric |
  | payment_details[order_reference] | string | A unique value assigned by the business to identify the transaction. | - Required for L3
- Required for L2
- For card networks: truncated to 25 alphanumeric characters, excluding spaces
- For Klarna: truncated to 255 characters and visible to customers when they view the order in the Klarna app |
  | tax[total_tax_amount] | integer | The total amount of tax on the transaction represented in the [smallest currency unit](https://docs.stripe.com/currencies.md#zero-decimal) | - Required for L2
- Value must be >= 0
- Conditional validation 1 |
  | payment_details[customer_reference] | string | A unique value to identify the customer. This field is available only for card payments | - Before we send this string to a card network, we truncate it to 25 alphanumeric characters, excluding spaces |
  | shipping[to_postal_code] | string | If a physical good is being shipped, the postal code of where it’s being shipped to | - Max length 10 chars
- Alphanumeric, hyphens are allowed |
  | shipping[from_postal_code] | string | If a physical good is being shipped, the postal code of where it’s being shipped from | - Max length 10 chars
- Alphanumeric, hyphens are allowed |
  | shipping[amount] | integer | If a physical good is being shipped, the cost of shipping represented in the [smallest currency unit](https://docs.stripe.com/currencies.md#zero-decimal) | - Value must be >= 0 |
  | discount_amount | integer | The total discount applied on the transaction represented in the [smallest currency unit](https://docs.stripe.com/currencies.md#zero-decimal) | - Value must be > 0
- Conditional validation 2 |
  | line_item[discount_amount] | integer | The discount applied on this line item represented in the [smallest currency unit](https://docs.stripe.com/currencies.md#zero-decimal) | - Value must be > 0
- Conditional validation 2 |

1 `tax[total_tax_amount]` and `line_item[tax][total_tax_amount]` are mutually exclusive. You can only specify one or the other.

2 `discount_amount` and `line_item[discount_amount]` are mutually exclusive. You can only specify one or the other.

### Additional Cards supported fields

Cards supports the preceding general fields, and also supports:

| Field Name                                              | Type   | Description                                                                                                                                                                                                                                                        | Format                                                                     |
| ------------------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| line_item[payment_method_options][card][commodity_code] | string | Identifier that categorizes the items being purchased using a standardized commodity scheme, such as (but not limited to): [UNSPSC](https://www.undp.org/unspsc), [NAICS](https://www.census.gov/naics/), [NAPCS](https://www.census.gov/naics/napcs/), and so on. | Max length 12 chars. Value must be alphanumeric characters without spaces. |

### Additional Klarna supported fields

Klarna supports the preceding general fields, and also supports:

| Field Name                                                                            | Type   | Description                                                                                                                                           | Format               |
| ------------------------------------------------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| line_item[payment_method_options][klarna][product_url]                                | string | Valid http or https URL of the product                                                                                                                | Max 4096 characters. |
| line_item[payment_method_options][klarna][image_url]                                  | string | Valid http or https URL of the image                                                                                                                  | Max 4096 characters. |
| amount_details[line_items][0][payment_method_options][klarna][reference]              | string | Unique reference for this line item to correlate it with your system’s internal records. The field is displayed in the Klarna Consumer App if passed. | Max 255 characters.  |
| amount_details[line_items][0][payment_method_options][klarna][subscription_reference] | string | Arbitrary identifier of your choosing to describe a subscription. Used in select Klarna recurring integrations. This isn’t visible to customers.      | Max 255 characters.  |

> For Klarna transactions, total amount is implicitly derived from the formula `(unit_cost * quantity) - discount_amount + tax.total_tax_amount`. There is no explicit field to pass the amount.

### Additional PayPal supported fields

Paypal supports the preceding general fields, and also supports:

| Field Name                                             | Type   | Description                                                                                                        | Format                                  |
| ------------------------------------------------------ | ------ | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------- |
| line_item[payment_method_options][paypal][description] | string | Description of the line item.                                                                                      | Max 127 characters                      |
| line_item[payment_method_options][paypal][category]    | enum   | Type of the line item.                                                                                             | digital_goods, physical_goods, donation |
| line_item[payment_method_options][paypal][sold_by]     | string | The Stripe account ID of the connected account that sells the item. Leave blank if you aren’t a connected account. | Max 127 characters                      |

## Cards-specific line items for L2 and L3 rates

Pass in required data for eligible cards to qualify for L2/L3 network programs

- Level 2: sales tax charged on transactions
- Level 3/Product 3: line item level breakdown such as product code, quantity, unit cost

#### Level 2

### Sample request (Level 2 data)

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 4600,
  currency: "usd",
  payment_method_types: ["card"],
  payment_details: {
    customer_reference: "customer_reference",
    order_reference: "order_reference",
  },
  amount_details: {
    tax: {
      total_tax_amount: 500,
    },
  },
});
```

### Sample response (Level 2 data)

```json
{
  "id": "pi_3OoMm5BLxXjrKOiR3LRyi610",
  "amount": 4600,
  "currency": "usd""amount_details": {
    "tax": {
      "total_tax_amount": 500
    },
  },
  "status": "requires_payment_method"
}

```

#### Level 3/Product 3

### Sample request (Level 3 and Product 3 data)

> Line items aren’t included by default in the API response. To return line items, [expand](https://docs.stripe.com/expand.md#includable-properties) `amount_details.line_items`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 4100,
  currency: "usd",
  payment_method_types: ["card"],
  payment_details: {
    customer_reference: "customer_reference",
    order_reference: "order_reference",
  },
  amount_details: {
    shipping: {
      from_postal_code: "94110",
      to_postal_code: "94117",
      amount: 100,
    },
    line_items: [
      {
        product_code: "SKU001",
        product_name: "Product 001",
        unit_cost: 2000,
        quantity: 1,
        tax: {
          total_tax_amount: 100,
        },
        unit_of_measure: "feet",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
      {
        product_code: "SKU002",
        product_name: "Product 002",
        unit_cost: 1800,
        quantity: 1,
        tax: {
          total_tax_amount: 100,
        },
        unit_of_measure: "gallons",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
    ],
  },
  expand: ["amount_details.line_items"],
});
```

### Sample response (Level 3 and Product 3 data)

```json
{
  "id": "pi_3OoMm5BLxXjrKOiR3LRyi610",
  "amount": 4100,
  "currency": "usd""amount_details": {
    "shipping": {
      "from_postal_code": "94110",
      "to_postal_code": "94117",
      "amount": 100
    },
    "line_items": {
      "object": "list",
      "url": "/v1/payment_intents/pi_3OoMm5BLxXjrKOiR3LRyi610/amount_details_line_items",
      "has_more": false,
      "data": [{
          "_id": "li_123",
          "product_code": "SKU001",
          "product_name": "Product 001",
          "unit_cost": 2000,
          "quantity": 1,
          "tax": {
            "total_tax_amount": 100
          },
          "unit_of_measure": "feet",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123",
            }
          }
        },
        {
          "_id": "li_456",
          "product_code": "SKU002",
          "product_name": "Product 002",
          "unit_cost": 1800,
          "quantity": 1,
          "tax": {
            "total_tax_amount": 100
          },
          "unit_of_measure": "gallons",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123",
            }
          }
        }
      ]
    }
  },
  "status": "requires_payment_method"
}
```

## PaymentIntent Operations

You can pass line items during both confirmation and capture.

### Set line items during Confirmation

You can set line items during confirmation regardless of the [capture_method](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-capture_method) you choose. If you pass line items during confirmation, then capture separately, you don’t need to pass line items again.

#### Create and confirm together

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 4100,
  currency: "usd",
  payment_method_types: ["card"],
  payment_method: "pm_card_visa",
  payment_details: {
    customer_reference: "customer_reference",
    order_reference: "order_reference",
  },
  amount_details: {
    shipping: {
      from_postal_code: "94110",
      to_postal_code: "94117",
      amount: 100,
    },
    line_items: [
      {
        product_code: "SKU001",
        product_name: "Product 001",
        unit_cost: 2000,
        quantity: 1,
        tax: {
          total_tax_amount: 100,
        },
        unit_of_measure: "feet",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
      {
        product_code: "SKU002",
        product_name: "Product 002",
        unit_cost: 1800,
        quantity: 1,
        tax: {
          total_tax_amount: 100,
        },
        unit_of_measure: "gallons",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
    ],
  },
  confirm: true,
});
```

#### Create and confirm separately

Call the `/confirm` endpoint after your PaymentIntent has been created.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.confirm("pi_xxxxxxxx");
```

### Set line items during Capture

If you don’t specify line items during confirmation, you can pass them during capture.

> Not supported when using PayPal

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 4100,
  currency: "usd",
  payment_method_types: ["card", "paypal"],
  payment_details: {
    customer_reference: "customer_reference",
    order_reference: "order_reference",
  },
  amount_details: {
    shipping: {
      from_postal_code: "94110",
      to_postal_code: "94117",
      amount: 100,
    },
    line_items: [
      {
        product_code: "SKU001",
        product_name: "Product 001",
        unit_cost: 2000,
        quantity: 1,
        tax: {
          total_tax_amount: 100,
        },
        unit_of_measure: "feet",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
      {
        product_code: "SKU002",
        product_name: "Product 002",
        unit_cost: 1800,
        quantity: 1,
        tax: {
          total_tax_amount: 100,
        },
        unit_of_measure: "gallons",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
    ],
  },
  confirm: true,
  capture_method: "manual",
});
```

Pass in an updated `amount_details` hash during Capture if needed.

#### Capture the already persisted amount details

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture("pi_xxxxxxxx");
```

#### Update amount details during capture

Capture the PaymentIntent with updated `amount_details`. You can change the line items and pass in an updated amount equal to the cost of the line items.

```curl
curl https://api.stripe.com/v1/payment_intents/pi_xxxxxxxx/capture \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount_to_capture=4100 \
  -d "payment_details[customer_reference]=customer_reference" \
  -d "payment_details[order_reference]=order_reference" \
  -d "amount_details[shipping][from_postal_code]=94110" \
  -d "amount_details[shipping][to_postal_code]=94117" \
  -d "amount_details[shipping][amount]=100" \
  -d "amount_details[line_items][0][product_code]=SKU001" \
  -d "amount_details[line_items][0][product_name]=Product 003" \
  -d "amount_details[line_items][0][unit_cost]=1500" \
  -d "amount_details[line_items][0][quantity]=1" \
  -d "amount_details[line_items][0][tax][total_tax_amount]=500" \
  -d "amount_details[line_items][1][product_code]=SKU002" \
  -d "amount_details[line_items][1][product_name]=Product 002" \
  -d "amount_details[line_items][1][unit_cost]=1500" \
  -d "amount_details[line_items][1][quantity]=1" \
  -d "amount_details[line_items][1][tax][total_tax_amount]=500"
```

## Payment Method Specific line items

Pass in additional payment method types on a per-line-item basis all in one place. You can pass in data related to payment methods you might not be confirming with as well, as long as the parameter is supported. This can simplify your integration, without requiring engineering effort to add and remove payment method specific fields for each payment method.

> Line items aren’t included by default in the API response. To return line items, [expand](https://docs.stripe.com/expand.md#includable-properties) `amount_details.line_items`

### Sample request (with Payment Method Specific line items)

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=4000 \
  -d currency=usd \
  -d "payment_method_types[0]=card" \
  -d "payment_method_types[1]=paypal" \
  -d "payment_method_types[2]=klarna" \
  -d "payment_details[customer_reference]=customer_reference" \
  -d "payment_details[order_reference]=order_reference" \
  -d "amount_details[shipping][from_postal_code]=94110" \
  -d "amount_details[shipping][to_postal_code]=94117" \
  -d "amount_details[shipping][amount]=100" \
  -d "amount_details[line_items][0][product_code]=SKU001" \
  -d "amount_details[line_items][0][product_name]=Product 001" \
  -d "amount_details[line_items][0][unit_cost]=2000" \
  -d "amount_details[line_items][0][discount_amount]=100" \
  -d "amount_details[line_items][0][quantity]=1" \
  -d "amount_details[line_items][0][tax][total_tax_amount]=100" \
  -d "amount_details[line_items][0][unit_of_measure]=feet" \
  -d "amount_details[line_items][0][payment_method_options][card][commodity_code]=123123" \
  --data-urlencode "amount_details[line_items][0][payment_method_options][klarna][image_url]=https://www.example.com/image.jpg" \
  --data-urlencode "amount_details[line_items][0][payment_method_options][klarna][product_url]=https://www.example.com/product" \
  -d "amount_details[line_items][0][payment_method_options][paypal][description]=This is a sample product description unique to PayPal for SKU001" \
  -d "amount_details[line_items][0][payment_method_options][paypal][category]=digital_goods" \
  -d "amount_details[line_items][1][product_code]=SKU002" \
  -d "amount_details[line_items][1][product_name]=Product 002" \
  -d "amount_details[line_items][1][unit_cost]=1800" \
  -d "amount_details[line_items][1][quantity]=1" \
  -d "amount_details[line_items][1][tax][total_tax_amount]=100" \
  -d "amount_details[line_items][1][unit_of_measure]=gallons" \
  -d "amount_details[line_items][1][payment_method_options][card][commodity_code]=123123" \
  --data-urlencode "amount_details[line_items][1][payment_method_options][klarna][image_url]=https://www.example.com/image.jpg" \
  --data-urlencode "amount_details[line_items][1][payment_method_options][klarna][product_url]=https://www.example.com/product" \
  -d "amount_details[line_items][1][payment_method_options][paypal][description]=This is a sample product description unique to PayPal for SKU002" \
  -d "amount_details[line_items][1][payment_method_options][paypal][category]=physical_goods" \
  -d "expand[0]=amount_details.line_items"
```

### Sample response (with Payment Method Specific line items)

```json
{
  "id": "pi_3OoMm5BLxXjrKOiR3LRyi610",
  "amount": 4000,
  "currency": "usd"
  "amount_details": {
    "shipping": {
      "from_postal_code": "94110",
      "to_postal_code": "94117",
      "amount": 100
    },
    "line_items": {
      "object": "list",
      "url": "/v1/payment_intents/pi_3OoMm5BLxXjrKOiR3LRyi610/amount_details_line_items",
      "has_more": false,
      "data": [{
          "_id": "li_123",
          "product_code": "SKU001",
          "product_name": "Product 001",
          "unit_cost": 2000,
          "quantity": 1,
          "discount_amount": 100,
          "tax": {
            "total_tax_amount": 100
          },"unit_of_measure": "feet",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123",
            },
            "klarna": {
              "image_url": "https://www.example.com/image.jpg",
              "product_url": "https://www.example.com/product"
            },
            "paypal": {
              "description": "This is a sample product description unique to PayPal for SKU001",
              "category": digital_goods,
            }
          }
        },
        {
          "_id": "li_456",
          "product_code": "SKU002",
          "product_name": "Product 002",
          "unit_cost": 1800,
          "quantity": 1,
          "tax": {
            "total_tax_amount": 100
          },"unit_of_measure": "gallons",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123",
            },
            "klarna": {
              "image_url": "https://www.example.com/image.jpg",
              "product_url": "https://www.example.com/product"
            },
            "paypal": {
              "description": "This is a sample product description unique to PayPal for SKU001",
              "category": physical_goods,
            }
          }
        }
      ]
    }
  },
  "status": "requires_payment_method"
}
```

## Using top-level discount or tax

The following example shows passing the top-level `discount_amount` and `tax` without line item level `tax` and `discount_amount`.

### Sample request (top-level discount or tax)

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=2500 \
  -d currency=usd \
  -d "payment_method_types[0]=card" \
  -d "payment_method_types[1]=paypal" \
  -d "payment_method_types[2]=klarna" \
  -d "payment_details[customer_reference]=customer_reference" \
  -d "payment_details[order_reference]=order_reference" \
  -d "amount_details[shipping][from_postal_code]=94110" \
  -d "amount_details[shipping][to_postal_code]=94117" \
  -d "amount_details[shipping][amount]=100" \
  -d "amount_details[discount_amount]=100" \
  -d "amount_details[tax][total_tax_amount]=500" \
  -d "amount_details[line_items][0][product_code]=SKU001" \
  -d "amount_details[line_items][0][product_name]=Product 001" \
  -d "amount_details[line_items][0][quantity]=1" \
  -d "amount_details[line_items][0][unit_cost]=2000" \
  --data-urlencode "amount_details[line_items][0][payment_method_options][klarna][image_url]=https://www.example.com/image.jpg" \
  --data-urlencode "amount_details[line_items][0][payment_method_options][klarna][product_url]=https://www.example.com/product" \
  -d "amount_details[line_items][0][payment_method_options][paypal][description]=This is a sample product description unique to PayPal for SKU001" \
  -d "amount_details[line_items][0][payment_method_options][paypal][category]=digital_goods" \
  -d "expand[0]=amount_details.line_items"
```

### Sample response (top-level discount or tax)

```json
{
  "id": "pi_3R0p2JCvDOElLqwO0mlHFrzv",
  "amount": 2500,
  "amount_capturable": 0,
  "amount_received": 2500,
  "payment_details": {
    "customer_reference": "customer_reference",
    "order_reference": "order_reference"
  },
  "amount_details": {"discount_amount": 100,
    "shipping": {
      "amount": 100,
      "from_postal_code": "94110",
      "to_postal_code": "94117"
    },"tax": {
      "total_tax_amount": 500
    },
    "line_items": {
      "object": "list",
      "data": [
        {
          "id": "uli_RueKif6jOR65uG",
          "object": "amount_details_line_item",
          "discount_amount": null,
          "payment_method_options": {
            "klarna": {
              "image_url": "https://www.example.com/image.jpg",
              "product_url": "https://www.example.com/product"
            },
            "paypal": {
              "category": "digital_goods",
              "description": "This is a sample product description unique to PayPal for SKU001"
            }
          },
          "product_code": "SKU001",
          "product_name": "Product 001",
          "quantity": 1,
          "tax": null,
          "unit_cost": 2000
        }
      ],
      "has_more": false,
      "url": "/v1/payment_intents/pi_3R0p2JCvDOElLqwO0mlHFrzv/amount_details_line_items"
    }
  }
  ...
}

```

## Loosen arithmetic validation

By default, Stripe validates that your line item data adds up correctly. When the sum of line items doesn’t match the total amount, Stripe returns a 400 error so you can correct discrepancies before processing the payment.

Opt out of strict validation on a per-request basis by setting [enforce_arithmetic_validation](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-amount_details-enforce_arithmetic_validation) to false. When you do this:

- The request proceeds even if line item amounts don’t match the total.
- Stripe returns validation error details in the [amount_details.error](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_details-error) field in the response.
- For card payments, Stripe doesn’t send line item data with arithmetic errors to card networks, preventing the transaction from qualifying for L2/L3 interchange savings.

### Sample request

The following is a sample request when arithmetic validation isn’t enforced:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  payment_method_types: ["card"],
  amount_details: {
    enforce_arithmetic_validation: false,
    tax: {
      total_tax_amount: 500,
    },
    line_items: [
      {
        product_code: "SKU001",
        product_name: "Product 001",
        unit_cost: 2000,
        quantity: 2,
      },
    ],
  },
  expand: ["amount_details.line_items"],
});
```

### Sample response

The following is a sample response when arithmetic validation isn’t enforced:

```json
{
  "id": "pi_3Spjgy2QCQbYXizB0HMvTu0w",
  "object": "payment_intent",
  "amount": 5000,
  "amount_details": {
    "error": {
      "code": "amount_details_amount_mismatch",
      "message": "The total value of `amount_details` (4500) does not match the `amount` (5000). Make sure that the total value of `line_items` matches the amount to charge, taking into account any discounts, tax, and shipping. See https://docs.stripe.com/payments/payment-line-items"
    },
    "line_items": {
      "object": "list",
      "data": [
        {
          "id": "uli_TnKLbGmvsdUYdN",
          "object": "payment_intent_amount_details_line_item",
          "discount_amount": null,
          "payment_method_options": null,
          "product_code": "SKU001",
          "product_name": "Product 001",
          "quantity": 2,
          "tax": null,
          "unit_cost": 2000,
          "unit_of_measure": null
        }
      ],
      "has_more": false,
      "url": "/v1/payment_intents/pi_3Spjgy2QCQbYXizB0HMvTu0w/amount_details_line_items"
    },
    "tax": {
      "total_tax_amount": 500
    },
    "tip": {}
  },
  "status": "requires_payment_method"
}
```

## Industry to MCC codes

| Category                          | Description                             |
| --------------------------------- | --------------------------------------- |
| Food & Beverage                   | - **5812**: Restaurants (not fast food) |
| - **5814**: Fast Food Restaurants |
| Hospitality & Travel              | - **3000-3299**: Airlines               |

- **3501-3999, 7011**: Hotels & Lodging
- **3351-3500**: Car Rental Agencies
- **4722**: Travel Agencies and Tour Operators
- **7512**: Automobile Rental Agency
- **7513**: Truck Rental and Leasing
- **7519**: Motor Home and Recreational Vehicle Rental
- **4411**: Cruise Lines
- **4112**: Passenger Railways
- **4111**: Local and Suburban Commuter Transit
- **4215**: Courier Services
- **4784**: Bridge and Road Fees
- **4468**: Marinas, Marine Service
- **5983**: Fuel Dealers |
  | Retail & E-Commerce | - **5962**: Direct Marketing—Travel
- **5966**: Direct Marketing—Outbound Telemarketing
- **5967**: Direct Marketing—Other |
  | Utilities & Miscellaneous | - **8398**: Charitable and Social Service Organizations
- **9752**: U.K. Petrol Stations, Electronic Hot File
- **9211**: Court Costs, including Alimony and Child Support
- **9311**: Tax Payments
- **9222**: Fines
- **9402**: Postal Services – Government Only and other similar services
- **9399**: Government Services (Not Elsewhere Classified) and other similar services
- **8661**: Religious Organizations
- **8211**: Schools and Educational Institutions
- **8220**: Colleges, Universities |

## Flexible payment scenarios

You can use payment line items with [complex payments](https://docs.stripe.com/payments/payment-line-items/flexible-payment-scenarios.md) such as multicaptures and overcaptures.
