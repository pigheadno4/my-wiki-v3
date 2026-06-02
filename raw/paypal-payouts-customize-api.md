<!-- Source URL: https://developer.paypal.com/docs/payouts/standard/integrate-api/customize/ -->
<!-- Fetched: 2026-04-16 -->

---
title: Customize Integration
slug: /docs/payouts/standard/integrate-api/customize/
updateTime: "2021-12-15T03:27:59.000Z"
---

# Customize Integration

## Show payout details

To show details for all items in your payout, use the payout_batch_id from the Create a payout response. You can specify the optional fields query parameter to filter the fields that are returned in the response. This example specifies fields=batch_header, which tells the API to return only the batch_header in the response:

```curl
curl -v -X GET https://api-m.sandbox.paypal.com/v1/payments/payouts/12345678?fields=batch_header \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <Access-Token>"
```

The response shows only batch header information for the payout. The batch header information includes the payout batch ID, the batch status, and other information:

```json
{
  "batch_header": {
    "payout_batch_id": "12345678",
    "batch_status": "ACKNOWLEDGED",
    "time_created": "2014-01-27T10:17:00Z",
    "time_completed": "2014-01-27T11:17:39.00Z",
    "sender_payout_header": {
      "sender_batch_id": "2014021801",
      "email_subject": "You have a payout!"
    },
    "amount": {
      "value": "435.85",
      "currency": "USD"
    }
  }
}
```

## Error Handling

Each PayPal API call returns an HTTP status code. Some API calls also return JSON response bodies that include information about the resource including one or more contextual HATEOAS links. PayPal uses conventional HTTP response codes to indicate the success or failure of an API request. In general, these codes are as follows:

- 2xx codes indicate success.
- 4xx codes indicate an error that failed given the information provided, for example, a required parameter was omitted or a charge failed.
- 5xx codes indicate an error with PayPal's servers.

For more details on HTTP status codes and responses, see the API Responses section.

## Idempotent requests

Idempotency allows you to safely resend the same request multiple times without the action being carried out more than once.

This means that if you try to create a payout which, due to network downtime (5xx status codes), meant you did not get a response from our servers, you can safely retry the transaction using the same idempotency key without risk of repeating the payout.

If you change any values in the subsequent request to the unique-reference-id header from a request, the request will be duplicated.

You can retry idempotent calls that fail with network timeouts (HTTP 5xx codes) for as long as the server stores the ID. If a duplicate request is found with the same idempotency key, we return the latest state of the payout that was created as part of the first transaction.

To see examples of these requests, see the API requests page.

Note: If you send two simultaneous API requests with same PayPal-Request-Id header, we will process the first request and fail the second request.

## Duplicate payout requests

PayPal prevents duplicate batches from being processed. If you specify a sender_batch_id that was used in the last 30 days, the API rejects the request and returns an error message that indicates the duplicate sender_batch_id and includes a HATEOAS link to the original batch payout with the same sender_batch_id. If you receive an HTTP 5nn status code, you can safely retry the request with the same sender_batch_id. The API completes a payment only once for a specific sender_batch_id that is used within 30 days.

For more information on Payouts API error messages, see Payouts Error Messages.

## Send payments in a different currency

Send payments in certain currencies even if you don't maintain a balance in that currency. It's easy to view funding balances, see currency exchange rates, and monitor your payments.

Note: Before using the Payouts API to send payments in another currency, make sure you complete the Payouts integration.

To send a payment in a different currency with the Payouts API, set the currency parameter to the payment's currency code.

### Sample currency conversion request

This request calls for a 10 Euro payout.

```json
"recipient_type": "EMAIL", "amount": {
  "value": 10.00,
  "currency": "EUR"
},
  "receiver": "example@email.com",
  "note": "Thanks from Acme Inc ",
  "sender_item_id": "item1"
```

### Sample currency conversion response

PayPal automatically converts the payment in your PayPal balance to the currency specified.

```json
"funding_source": "BALANCE", "amount": {
  "currency": "EUR",
  "value": "10.00"
}, "fees": {
  "currency": "EUR",
  "value": "0.20"
}, "currency_conversion": {
  "from_amount": {
    "currency": "USD",
    "value": "11.43"
  },
  "to_amount": {
    "currency": "EUR",
    "value": "10.20"
  }
```

Note: See a list of country exclusions and restrictions for payouts currency conversion.
