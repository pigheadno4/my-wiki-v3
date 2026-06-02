<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/acquirer-reference-number/ -->
<!-- Fetched: 2026-04-13 -->

Online / Checkout / Expanded / Customize / Track transactions using an acquirer reference number

# Track transactions using an acquirer reference number

The acquirer reference number (ARN) is a unique value assigned to a credit or debit card transaction after the card has been processed. The ARN tracks the transaction's movement, which helps card brands, card issuing banks, and processors locate the transaction and confirm its handling.

Customers can use the ARN to confirm that a refund was processed. If you provide your customer with the ARN, their bank can trace the transaction using this value. The ARN is passed as part of the response object.

Without an ARN, if a customer's card has been lost, stolen, or closed since the original transaction, the issuing bank can have trouble routing a refund to the customer's account. When this happens, the bank reroutes the money to the appropriate account, mails the customer a check, or returns the money to your merchant account.

## Know before you code

This integration requires an Expanded Checkout integration.

## Availability

- US, UK, Canada, Australia, and the EU.
- Credit and debit card purchases, including those made with digital wallets or mobile devices.

## How to retrieve the ARN

Make a GET call to retrieve a transaction's ARN. Available for orders, captures, and refunds. **Note:** After you capture a payment or refund a transaction, the ARN is available after a few days.

### Orders API

`GET /v2/checkout/orders/ORDER-ID?fields=payment_source`

The ARN appears nested in `purchase_units[].payments.captures[].network_transaction_reference.acquirer_reference_number` and `purchase_units[].payments.refunds[].acquirer_reference_number`.

```bash
GET v2/checkout/orders/ORDER-ID?fields=payment_source
Authorization: Bearer ACCESS-TOKEN
```

Sample response (abbreviated — shows ARN location):
```json
{
  "purchase_units": [{
    "payments": {
      "captures": [{
        "network_transaction_reference": {
          "id": "TRANSACTION-ID",
          "network": "VISA",
          "acquirer_reference_number": "ACQUIRER-REFERENCE-NUMBER"
        }
      }],
      "refunds": [{
        "acquirer_reference_number": "ACQUIRER-REFERENCE-NUMBER"
      }]
    }
  }]
}
```

### Refund API

`GET /v2/payments/refunds/REFUND-ID`

The ARN is at the top level: `acquirer_reference_number`.

```json
{
  "id": "REFUND-ID",
  "status": "COMPLETED",
  "acquirer_reference_number": "ACQUIRER-REFERENCE-NUMBER",
  "invoice_id": "INVOICE-123"
}
```

### Capture API

`GET /v2/payments/captures/CAPTURE-ID`

The ARN is nested in `network_transaction_reference.acquirer_reference_number`.

```json
{
  "id": "CAPTURE-ID",
  "status": "COMPLETED",
  "network_transaction_reference": {
    "id": "REFERENCE-ID",
    "network": "VISA",
    "acquirer_reference_number": "ACQUIRER-REFERENCE-NUMBER"
  },
  "processor_response": {
    "avs_code": "A",
    "cvv_code": "M",
    "response_code": "0000"
  }
}
```
