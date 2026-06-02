<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/sca-payment-indicators/ -->
<!-- Fetched: 2026-04-13 -->

---
title: SCA payment indicators
slug: /docs/checkout/advanced/customize/sca-payment-indicators/
createTime: '2024-08-15T07:30:48.343Z'
updateTime: '2024-12-03T23:42:08.630Z'
---


# SCA payment indicators
If you process payments that require Strong Customer Authentication (SCA), you need to provide additional context about the transaction with payment indicators. The payment indicators ensure that buyer authentication, card on file, and other factors are appropriately handled. Pass these payment indicators to avoid rejected transactions.

To provide additional transaction context, include stored_payment_source in your create order request.

## Know before you code
Required integration: Expanded Checkout integration

## Add request parameter
Update the POST v2/checkout/orders request body to include stored_credential.

### Sample request
API endpoint used: Create order

```bash
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <Access-Token>" \
-H "PayPal-Partner-Attribution-Id: <BN-Code>" \
-d '{
  "intent": "CAPTURE",
  "purchase_units": [{
    "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
    "amount": {
      "currency_code": "USD",
      "value": "100.00"
    }
  }],
  "payment_source": {
    "card": {
      "number": "4111111111111111",
      "expiry": "2020-02",
      "name": "John Doe",
      "billing_address": {
        "address_line_1": "2211 N First Street",
        "address_line_2": "17.3.160",
        "admin_area_1": "CA",
        "admin_area_2": "San Jose",
        "postal_code": "95131",
        "country_code": "US"
      },
      "stored_credential": {
        "payment_initiator": "MERCHANT",
        "payment_type": "RECURRING",
        "usage": "SUBSEQUENT",
        "previous_transaction_reference": "53963906K75832009"
      }
    }
  }
}'
```

### Modify the code
Copy the code snippet and modify the values for stored_credential as follows:

**payment_initiator** (Required)

| Value | Description |
| --- | --- |
| CUSTOMER | Customer initiates the payment. |
| MERCHANT | Merchant initiates the transaction and the merchant has established consent to charge the buyer. |

**payment_type** (Required)

| Value | Description |
| --- | --- |
| UNSCHEDULED | Payments that the merchant initiates and are not on a specified schedule. For example, this includes preauthorized transactions where the merchant can charge the buyer once a balance falls within a specified range. These transactions are also referred to as top-up. |
| RECURRING | Merchant initiates a payment as part of a series of recurring payments. The payment amounts can be variable and are on a fixed time interval. |
| ONE_TIME | Default when no stored_credential is sent. |

**usage**

| Value | Description |
| --- | --- |
| FIRST | Save card information or payment token to use in subsequent transactions. Collect consent from the buyer that you intend to save their payment information. |
| SUBSEQUENT | Card information or payment token was previously saved and is used in the transaction. |
| DERIVED | The value of FIRST or SUBSEQUENT is determined based on the data available. |

**previous_transaction_reference**
Transaction ID previously used to charge the payer. Shows payment processors that you have established a contract with the payer.

**previous_network_transaction_reference**

| Value | Description |
| --- | --- |
| previous_network_transactionID | Transaction ID from a non-PayPal payment processor that you have previously used to process the payment. |
| network | Transaction ID from a non-PayPal payment processor that you have previously used to process the payment. |

**network_transaction_reference**
Reference values used by the card network to identify a transaction.

| Value | Description |
| --- | --- |
| ID (Required) | Transaction reference ID returned by the scheme. |
| NETWORK (Required) | Name of the card network through which the transaction was routed. |
| DATE | The date that the transaction was authorized by the scheme. |

### Step result
A successful request results in the following:

- A return status code of HTTP 201 Created.
- A JSON response body that contains the processor response.

## Use cases
You can use these common scenarios to determine how you'll update your integration.

### One time transaction
| Scenario | Payment initiator | Payment type | Usage |
| --- | --- | --- | --- |
| Single payment. Payer doesn't intend to make another purchase or save their card. | CUSTOMER | ONE_TIME | DERIVED |
| Single payment. Payer saves their card details for a future single payment. | CUSTOMER | ONE_TIME | FIRST |
| Single payment. Payer uses a previously-saved card to complete the transaction. | CUSTOMER | ONE_TIME | SUBSEQUENT |

### Recurring plan or subscription
| Scenario | Payment initiator | Payment type | Usage |
| --- | --- | --- | --- |
| Initial transaction to sign up for the recurring charges. Payer hasn't saved their card. | CUSTOMER | RECURRING | FIRST |
| Initial transaction to sign up for the recurring charges. Payer has already saved their card. | CUSTOMER | RECURRING | SUBSEQUENT |
| Subsequent payments as part of a recurring plan. | MERCHANT | RECURRING | SUBSEQUENT |
| Initial customer-initiated transaction wasn't processed with PayPal. Merchant processes recurring charge with PayPal. | MERCHANT | RECURRING | SUBSEQUENT |

### Unscheduled payment
| Scenario | Payment initiator | Payment type | Usage |
| --- | --- | --- | --- |
| Initial transaction to sign up for an unscheduled payment. Payer has not saved their card. | CUSTOMER | UNSCHEDULED | FIRST |
| Initial transaction to sign up for an unscheduled payment. Payer has already saved their card. | CUSTOMER | UNSCHEDULED | SUBSEQUENT |
| Subsequent payments as part of the unscheduled contract. | MERCHANT | UNSCHEDULED | SUBSEQUENT |
| Initial payer-initiated transaction wasn't processed with PayPal. Merchant processes unscheduled charge with PayPal. | MERCHANT | UNSCHEDULED | SUBSEQUENT |
