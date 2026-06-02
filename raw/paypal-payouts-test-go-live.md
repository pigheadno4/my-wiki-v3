<!-- Source URL: https://developer.paypal.com/docs/payouts/standard/integrate-api/test-go-live/ -->
<!-- Fetched: 2026-04-16 -->

---
title: Test and Go Live
slug: /docs/payouts/standard/integrate-api/test-go-live/
updateTime: "2022-05-19T07:02:27.000Z"
---

# Test and Go Live

You can run negative tests on your integration to manage the responses you give to your customers.

## Know before you code

- Before you trigger a simulation, you'll need to you need to get an access token.
- Use Postman to explore and test PayPal APIs.

## Simulation methods

To trigger a simulation for the Payouts API, use a JSON pointer in the request payload or use a path parameter in the request URI.

### Use a JSON pointer in the request payload

| Trigger | Test value | Simulated response |
| --- | --- | --- |
| items[0]/note | ERRPYO002 | SENDER_EMAIL_UNCONFIRMED |

JSON pointer request:

```curl
curl -X POST https://api-m.sandbox.paypal.com/v1/payments/payouts \
  -H "content-type: application/json" \
  -H "Authorization: Bearer <Access-Token>" \
  -d '{
  "sender_batch_header":
  {
    "sender_batch_id": "1524086406556",
    "email_subject": "This email is related to simulation"
  },
  "items": [
  {
    "recipient_type": "EMAIL",
    "receiver": "payouts-simulator-receiver@paypal.com",
    "note": "ERRPYO002",
    "sender_item_id": "15240864065560",
    "amount":
    {
      "currency": "USD",
      "value": "1.00"
    }
  }]
}'
```

JSON pointer response:

```json
{
  "name": "SENDER_EMAIL_UNCONFIRMED",
  "message": "Authorization error occurred",
  "debug_id": "ca787bdf80d7a",
  "information_link": "https://developer.paypal.com/docs/api/payments.payouts-batch/v1/#errors"
}
```

### Use a path parameter in the request URI

| Trigger | Test value | Simulated response |
| --- | --- | --- |
| /v1/payments/payouts | ERRPYO015 | CLOSED_MARKET |

Path parameter request:

```curl
curl -X GET https://api-m.sandbox.paypal.com/v1/payments/payouts/ERRPYO015 \
  -H "content-type: application/json" \
  -H "Authorization: Bearer <Access-Token>"
```

Path parameter response:

```json
{
  "batch_header":
  {
    "payout_batch_id": "DQCP2UAJCBMNY",
    "batch_status": "SUCCESS",
    "time_created": "2017-08-21T11:22:33Z",
    "time_completed": "2017-08-21T11:22:54Z",
    "sender_batch_header":
    {
      "email_subject": "user test case"
    },
    "amount":
    {
      "currency": "USD",
      "value": "190.0"
    },
    "fees":
    {
      "currency": "USD",
      "value": "0.0"
    }
  },
  "items": [
  {
    "payout_item_id": "RWD4Y3H9VV8BA",
    "transaction_status": "FAILED",
    "payout_item_fee":
    {
      "currency": "USD",
      "value": "0.0"
    },
    "payout_batch_id": "DQCP2UAJCBMNY",
    "payout_item":
    {
      "recipient_type": "EMAIL",
      "amount":
      {
        "currency": "USD",
        "value": "190.0"
      },
      "note": "payout to  receiver",
      "receiver": "receiver@example.com",
      "sender_item_id": "MSI-2727"
    },
    "time_processed": "2017-08-21T11:22:44Z",
    "errors":
    {
      "name": "CLOSED_MARKET",
      "message": "Market closed and transaction is between 2 different countries",
      "information_link": "https://developer.paypal.com/docs/api/payments.payouts-batch/v1/#errors",
      "details": []
    },
    "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/payments/payouts-item/RWD4Y3H9VV8BA",
      "rel": "item",
      "method": "GET",
      "encType": "application/json"
    }]
  }],
  "links": [
  {
    "href": "https://api-m.sandbox.paypal.com/v1/payments/payouts/DQCP2UAJCBMNY",
    "rel": "self",
    "method": "GET",
    "encType": "application/json"
  }]
}
```

## Test values

Use the listed test values to trigger positive and negative responses for these payouts actions:

- Create payout
- Show payout details
- Cancel payout item
- Show payout item details
- Batch processing

Note: Test values are case sensitive.

### Create payout

#### Positive response test values

Use the JSON pointer method to simulate this response at POST v1/payments/payouts/.

| Trigger | Test value | Simulated response |
| --- | --- | --- |
| items[0]/note | POSPYO001 | PAYLOAD WITH 201 RESPONSE CODE |
| items[0]/note | POSPYO003 | PAYLOAD WITH 201 RESPONSE CODE FOR VENMO RECEIVER |

#### Negative response test values

Use the JSON pointer method to simulate these error responses at POST v1/payments/payouts.

| Trigger | Test value | Simulated response |
| --- | --- | --- |
| items[0]/note | ERRPYO001 | SENDER_RESTRICTED |
| items[0]/note | ERRPYO002 | SENDER_EMAIL_UNCONFIRMED |
| items[0]/note | ERRPYO003 | AUTHORIZATION_ERROR |
| items[0]/note | ERRPYO005 | INSUFFICIENT_FUNDS |
| items[0]/note | ERRPYO006 | INTERNAL_ERROR |
| items[0]/note | ERRPYO010 | VALIDATION_ERROR |
| items[0]/note | ERRPYO011 | REQUIRED_SCOPE_MISSING |
| items[0]/note | ERRPYO012 | SENDER_LOCKED |
| items[0]/sender_batch_id | ERRPYO013 | VALIDATION_ERROR FOR VENMO NOTE MISSING |
| items[0]/note | ERRPYO014 | USER_BUSINESS_ERROR |
| items[0]/note | ERRPYO035 | RATE_LIMIT_VALIDATION |
| items[0]/note | ERRPYO036 | REQUEST_TIMEOUT_EXCEEDED |
| items[0]/note | ERRPYO037 | SYNC_MODE_NOT_APPLICABLE |
| items[0]/note | ERRPYO038 | NON_HOLDING_CURRENCY |
| items[0]/note | ERRPYO039 | PREVIOUS_REQUEST_IN_PROGRESS |
| items[0]/note | ERRPYO040 | CIP_NOT_VERIFIED |

### Show payout details

#### Positive response test values

Use the path parameter in the request URI method to simulate this response at GET v1/payments/payouts.

| Trigger or test value | Simulated response |
| --- | --- |
| /v1/payments/payouts/POSPYO002 | PAYLOAD WITH 200 RESPONSE CODE |

#### Negative response test values

Use the path parameter in the request URI method to simulate these error responses at GET v1/payments/payouts.

| Trigger or test value | Simulated response |
| --- | --- |
| /v1/payments/payouts/ERRPYOB005 | ACCOUNT_RESTRICTED |
| /v1/payments/payouts/ERRPYOB006 | ACCOUNT_UNCONFIRMED_EMAIL |
| /v1/payments/payouts/ERRPYOB007 | APPROVER_DENIED |
| /v1/payments/payouts/ERRPYOB008 | GAMER_FAILED_COUNTRY_OF_RESIDENCE_CHECK |
| /v1/payments/payouts/ERRPYOB009 | GAMER_FAILED_FUNDING_SOURCE_CHECK |
| /v1/payments/payouts/ERRPYOB010 | GAMING_INVALID_PAYMENT_FLOW |
| /v1/payments/payouts/ERRPYOB011 | NON_HOLDING_CURRENCY |
| /v1/payments/payouts/ERRPYOB012 | PENDING_RECIPIENT_NON_HOLDING_CURRENCY_PAYMENT_PREFERENCE |
| /v1/payments/payouts/ERRPYOB013 | SENDER_STATE_RESTRICTED |
| /v1/payments/payouts/ERRPYOB014 | SPENDING_LIMIT_EXCEEDED |
| /v1/payments/payouts/ERRPYOB015 | TRANSACTION_DECLINED_BY_TRAVEL_RULE |
| /v1/payments/payouts/ERRPYO015 | CLOSED_MARKET |
| /v1/payments/payouts/ERRPYO016 | CURRENCY_COMPLIANCE |
| /v1/payments/payouts/ERRPYO017 | CURRENCY_NOT_SUPPORTED_FOR_RECEIVER |
| /v1/payments/payouts/ERRPYO018 | DUPLICATE_ITEM |
| /v1/payments/payouts/ERRPYO019 | RECEIVER_ACCOUNT_LOCKED |
| /v1/payments/payouts/ERRPYO020 | RECEIVER_COUNTRY_NOT_ALLOWED |
| /v1/payments/payouts/ERRPYO021 | RECEIVER_UNCONFIRMED |
| /v1/payments/payouts/ERRPYO022 | RECEIVER_UNREGISTERED |
| /v1/payments/payouts/ERRPYO023 | RECEIVER_YOUTH_ACCOUNT |
| /v1/payments/payouts/ERRPYO024 | RECEIVING_LIMIT_EXCEEDED |
| /v1/payments/payouts/ERRPYO025 | REGULATORY_BLOCKED |
| /v1/payments/payouts/ERRPYO026 | REGULATORY_PENDING |
| /v1/payments/payouts/ERRPYO027 | RISK_DECLINE |
| /v1/payments/payouts/ERRPYO028 | SELF_PAY_NOT_ALLOWED |
| /v1/payments/payouts/ERRPYO029 | TRANSACTION_LIMIT_EXCEEDED |
| /v1/payments/payouts/ERRPYO030 | UNDEFINED |
| /v1/payments/payouts/ERRPYO031 | ZERO_AMOUNT |
| /v1/payments/payouts/ERRPYO032 | INVALID_RESOURCE_ID |
| /v1/payments/payouts/ERRPYO033 | INTERNAL_ERROR |
| /v1/payments/payouts/ERRPYO034 | INVALID_EMAIL |
| /v1/payments/payouts/ERRPYO060 | RECEIVER_ACCOUNT_LIMITATION |

### Cancel payout item

#### Positive response test values

Use the path parameter in the request URI method to simulate this response at POST v1/payments/payouts-item/payouts_item_id/cancel.

| Trigger or test value | Simulated response |
| --- | --- |
| /v1/payments/payouts-item/POSPOI002/cancel | PAYLOAD WITH 200 RESPONSE CODE |

#### Negative response test values

Use the path parameter in the request URI method to simulate these error responses at POST v1/payments/payouts-item/payouts_item_id/cancel.

| Trigger or test value | Simulated response |
| --- | --- |
| /v1/payments/payouts-item/ERRPOI001/cancel | INVALID_RESOURCE_ID |
| /v1/payments/payouts-item/ERRPYO004/cancel | BATCH_NOT_COMPLETED |
| /v1/payments/payouts-item/ERRPYO007/cancel | ITEM_ALREADY_CANCELLED |
| /v1/payments/payouts-item/ERRPYO008/cancel | ITEM_CANCELLATION_FAILED |
| /v1/payments/payouts-item/ERRPYO009/cancel | ITEM_INCORRECT_STATUS |

### Show payout item details

#### Positive response test values

Use the path parameter in the request URI method to simulate this response at GET v1/payments/payouts-item/payouts_item_id.

| Trigger or test value | Simulated response |
| --- | --- |
| /v1/payments/payouts-item/POSPOI001 | PAYLOAD WITH 200 RESPONSE CODE |

#### Negative response test values

Use the path parameter in the request URI method to simulate these error responses at GET v1/payments/payouts-item/payouts_item_id.

| Trigger or test value | Simulated response |
| --- | --- |
| /v1/payments/payouts-item/ERRPYO041 | CLOSED_MARKET |
| /v1/payments/payouts-item/ERRPYO042 | CURRENCY_COMPLIANCE |
| /v1/payments/payouts-item/ERRPYO043 | CURRENCY_NOT_SUPPORTED_FOR_RECEIVER |
| /v1/payments/payouts-item/ERRPYO044 | RECEIVER_ACCOUNT_LOCKED |
| /v1/payments/payouts-item/ERRPYO045 | RECEIVER_COUNTRY_NOT_ALLOWED |
| /v1/payments/payouts-item/ERRPYO046 | RECEIVER_UNCONFIRMED |
| /v1/payments/payouts-item/ERRPYO047 | RECEIVER_UNREGISTERED |
| /v1/payments/payouts-item/ERRPYO048 | RECEIVER_YOUTH_ACCOUNT |
| /v1/payments/payouts-item/ERRPYO049 | RECEIVING_LIMIT_EXCEEDED |
| /v1/payments/payouts-item/ERRPYO050 | REGULATORY_BLOCKED |
| /v1/payments/payouts-item/ERRPYO051 | REGULATORY_PENDING |
| /v1/payments/payouts-item/ERRPYO052 | RISK_DECLINE |
| /v1/payments/payouts-item/ERRPYO053 | SELF_PAY_NOT_ALLOWED |
| /v1/payments/payouts-item/ERRPYO054 | TRANSACTION_LIMIT_EXCEEDED |
| /v1/payments/payouts-item/ERRPYO055 | UNDEFINED |
| /v1/payments/payouts-item/ERRPYO056 | ZERO_AMOUNT |
| /v1/payments/payouts-item/ERRPYO057 | INVALID_RESOURCE_ID |
| /v1/payments/payouts-item/ERRPYO058 | INTERNAL_ERROR |
| /v1/payments/payouts-item/ERRPYO059 | INVALID_EMAIL |
| /v1/payments/payouts-item/ERRPYO061 | RECEIVER_ACCOUNT_LIMITATION |
| /v1/payments/payouts-items/ERRPYOB016 | ACCOUNT_RESTRICTED |
| /v1/payments/payouts-items/ERRPYOB017 | ACCOUNT_UNCONFIRMED_EMAIL |
| /v1/payments/payouts-items/ERRPYOB018 | APPROVER_DENIED |
| /v1/payments/payouts-items/ERRPYOB019 | GAMER_FAILED_COUNTRY_OF_RESIDENCE_CHECK |
| /v1/payments/payouts-items/ERRPYOB020 | GAMER_FAILED_FUNDING_SOURCE_CHECK |
| /v1/payments/payouts-items/ERRPYOB021 | GAMING_INVALID_PAYMENT_FLOW |
| /v1/payments/payouts-items/ERRPYOB022 | NON_HOLDING_CURRENCY |
| /v1/payments/payouts-items/ERRPYOB023 | PENDING_RECIPIENT_NON_HOLDING_CURRENCY_PAYMENT_PREFERENCE |
| /v1/payments/payouts-items/ERRPYOB024 | SENDER_STATE_RESTRICTED |
| /v1/payments/payouts-items/ERRPYOB025 | SPENDING_LIMIT_EXCEEDED |
| /v1/payments/payouts-items/ERRPYOB026 | TRANSACTION_DECLINED_BY_TRAVEL_RULE |

### Batch processing

#### Batch status test values

Use the path parameter in the request URI method to simulate these error responses at GET v1/payments/payouts/payout_batch_id.

| Trigger or test value | Simulated response |
| --- | --- |
| /v1/payments/payouts/ERRPYOB001 | SUCCESS |
| /v1/payments/payouts/ERRPYOB002 | PENDING |
| /v1/payments/payouts/ERRPYOB003 | PROCESSING |
| /v1/payments/payouts/ERRPYOB004 | DENIED |

## Webhooks with failed payouts

Webhook resources don't contain error objects. If you receive a webhook for a failed payout and would like to understand why the payout failed, do a GET request on the object. For more details, see Webhook event names.

## Rate limiting

The rate limit number for Payouts API POST calls is 400.

PayPal's primary focus is site availability and security in support of merchants.

While we do not publish a rate limiting policy, we might temporarily rate limit if we identify traffic that appears to be abusive. We rate limit until we are confident that the activity is not problematic for PayPal, merchants, or customers.

To ensure maximum protection and site stability, we constantly evaluate traffic as it surges and subsides to adjust our policies. If you or your customers receive the HTTP 429 Unprocessable Entity - RATE_LIMIT_REACHED status code, too many requests were sent, and that might indicate anomalous traffic, so we rate limit to ensure site stability.

If this policy negatively affects your integration, contact Merchant Technical Support.

Tips to avoid rate limiting:

- Do not poll and instead use webhooks or IPN. To learn more, see Webhooks and Instant Payment Notification.
- Rather than generate an OAuth 2.0 access token for each transaction, cache tokens. See OAuth 2.0 authorization protocol.

## Go live with your integration

Deploying your code to the live environment takes only a few steps.

- Change the base URL for all your REST API calls from https://api-m.sandbox.paypal.com to https://api-m.paypal.com.
- Change the references to your sandbox API credentials to the live credentials. To get live API credentials, create a live REST API.
- Tip: Remember to change the sandbox client ID in the JavaScript SDK call in your HTML.
- If you created or updated pages on a website, move that code from the test environment to the live environment.
