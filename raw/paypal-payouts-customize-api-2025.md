<!-- Source URL: https://docs.paypal.ai/growth/payouts/send-money/customize-payouts-api -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Customize Payouts API integration

You can use the procedures in this section to customize your Payouts API integration to support global payments, optimize API responses, and ensure reliable payout processing.

## Pay recipients in their local currency

You can pay recipients in any supported currency, even if your PayPal account does not hold a balance in that currency. To do this, set the `items.amount.currency` parameter in your <a href="/growth/payouts/send-money/use-payouts-api#1-create-payout-batch" target="_blank" rel="noopener noreferrer">payout request</a> to the appropriate <a href="/growth/payouts/reference/countries-supported-features#supported-currencies-for-automatic-conversion" target="_blank" rel="noopener noreferrer">currency code</a>. PayPal automatically converts currencies and applies relevant fees. This helps you reach recipients globally and simplify cross-border payments.

<Note>For more information about currency conversion, country exclusions, and restrictions, see <a href="/growth/payouts/reference/countries-supported-features#currency-conversion" target="_blank" rel="noopener noreferrer">Currency conversion</a>.</Note>

Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a GET call to the `/v1/payments/payouts/{ID}` endpoint.

**Path parameter**: `ID` is the `payout_batch_id` returned in the <a href="/growth/payouts/send-money/use-payouts-api#1-create-payout-batch" target="_blank" rel="noopener noreferrer">Create payout batch</a> response.

<CodeGroup>
  ```shell Sample request lines theme={null}
  curl -X GET https://api-m.sandbox.paypal.com/v1/payments/payouts/5UXD2E8A7EBQJ \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer ACCESS-TOKEN'
  ```

```json Sample response lines expandable theme={null}
{
  "total_items": 1,
  "total_pages": 1,
  "batch_header": {
    "payout_batch_id": "5UXD2E8A7EBQJ",
    "batch_status": "SUCCESS",
    "time_created": "2024-07-03T10:30:00Z",
    "time_completed": "2024-07-03T10:32:15Z",
    "sender_batch_header": {
      "sender_batch_id": "Payouts_2024_100001",
      "email_subject": "You have a payout!",
      "email_message": "Congratulations! You have received a payout."
    },
    "funding_source": "BALANCE",
    "amount": {
      "currency": "USD",
      "value": "108.50"
    },
    "fees": {
      "currency": "USD",
      "value": "1.95"
    }
  },
  "items": [
    {
      "payout_item_id": "9MYSR9GT8AEUG",
      "transaction_id": "2JE19762AW167960J",
      "activity_id": "3E158638XS0329103",
      "transaction_status": "SUCCESS",
      "payout_item_fee": {
        "currency": "USD",
        "value": "1.95"
      },
      "payout_batch_id": "5UXD2E8A7EBQJ",
      "payout_item": {
        "recipient_type": "EMAIL",
        "amount": {
          "currency": "EUR",
          "value": "100.00"
        },
        "note": "Thank you for your business!",
        "receiver": "recipient.europe@example.com",
        "sender_item_id": "EUR_PAYOUT_001"
      },
      "currency_conversion": {
        "from_amount": {
          "currency": "USD",
          "value": "108.50"
        },
        "to_amount": {
          "currency": "EUR",
          "value": "100.00"
        },
        "exchange_rate": "0.9217"
      },
      "time_processed": "2024-07-03T10:31:45Z"
    }
  ],
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/payments/payouts/5UXD2E8A7EBQJ",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `200 OK` response with the payout details, including currency conversion fee details for each payout item.

## Get specific payout details

When you <a href="/growth/payouts/send-money/use-payouts-api#poll-for-updates" target="_blank" rel="noopener noreferrer">track payouts status</a>, you can use the `fields` query parameter and customize the response to return only the information you need. This enables you to tailor the API output for summary reporting or reconciliation. Requesting specific fields reduces response size and improves performance.

Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a GET call to the `/v1/payments/payouts/{ID}?fields={FIELDS}` endpoint.

**Path parameter**: `ID` is the `payout_batch_id` returned in the <a href="/growth/payouts/send-money/use-payouts-api#1-create-payout-batch" target="_blank" rel="noopener noreferrer">Create payout batch</a> response.

**Query parameter**: `FIELDS` are the specific fields that you need in the response. For example, you can request only the `batch_header` for a summary.

<CodeGroup>
  ```shell Sample request lines theme={null}
  curl -v -X GET 'https://api-m.sandbox.paypal.com/v1/payments/payouts/NNX8XK9T3CGWN?fields=batch_header' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer ACCESS-TOKEN'
  ```

```json Sample response lines expandable theme={null}
{
  "batch_header": {
    "payout_batch_id": "NNX8XK9T3CGWN",
    "batch_status": "SUCCESS",
    "time_created": "2025-07-31T07:00:57Z",
    "time_completed": "2025-07-31T07:01:26Z",
    "sender_batch_header": {
      "sender_batch_id": "Payouts_1753945252",
      "email_subject": "You have a payout!",
      "email_message": "Congratulations! You have received a payout."
    },
    "funding_source": "BALANCE",
    "amount": {
      "currency": "USD",
      "value": "10.00"
    },
    "fees": {
      "currency": "USD",
      "value": "0.25"
    }
  },
  "items": [],
  "links": [
    {
      "href": "https://api.sandbox.paypal.com/v1/payments/payouts/NNX8XK9T3CGWN?page_size=1000&page=1",
      "rel": "self",
      "method": "GET",
      "encType": "application/json"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `200 OK` response with the requested details of the payout batch.

## Prevent duplicate requests

You can prevent the processing of duplicate batch payouts. To do this, in the <a href="/growth/payouts/send-money/use-payouts-api#1-create-payout-batch" target="_blank" rel="noopener noreferrer">create payout batch request</a>, use a unique `sender_batch_id` for each batch. If you reuse a `sender_batch_id` from the last 30 days, the API rejects the request and returns an error with a HATEOAS link to the original batch. When you retry a request after an HTTP 5xx error, use the same `sender_batch_id` as the original request to ensure PayPal processes only one batch, even if you submit multiple requests.

## Implement idempotency

You can retry a payout request multiple times and still ensure that it has the effect of only one successful request, through idempotency.

To implement idempotency:

- Include a unique, self-generated idempotency key as the `PayPal-Request-Id` header-parameter value for each payout request.
- Use the same idempotency key when you retry the request due to a network issue or HTTP 5xx server error.
- If the payout details already exist, PayPal returns the current state of the payout. This ensures you create only one payout for each unique key.

<Note>If PayPal receives two simultaneous requests with the same `PayPal-Request-Id` (idempotency key), PayPal processes only the first request. The second request fails with an error indicating the duplicate key. For more information, see <a href="/developer/how-to/api/make-api-requests#paypal-request-id" target="blank">PayPal-Request-Id</a>.</Note>
