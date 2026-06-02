<!-- Source URL: https://docs.paypal.ai/growth/payouts/send/api -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Payouts API

You can use this pattern to send payouts to multiple recipients with a single API call.

<Tip>You can send payouts to PayPal accounts and Venmo users.</Tip>

**Useful resource**: <a href="https://www.paypal.com/apex/product-profile/payouts/getAccessToken" target="_blank" rel="noopener noreferrer">PayPal API Executor</a>

## Important information

Ensure to review the following information before you send payouts.

### Rate-limiting guideline

PayPal does not have a published rate-limiting policy. To ensure site security and stability for merchants, we might temporarily apply rate limiting if we see unusual or abusive traffic. We hold the rate limit until we know the traffic is safe. For Payouts API, we allow 400 POST requests per minute. If you get an HTTP `429 Unprocessable Entity - RATE_LIMIT_REACHED` message, you have exceeded the rate limit. If this affects your integration, contact <a href="https://www.paypal-techsupport.com/s/?language=en_US" target="_blank" rel="noopener noreferrer">Merchant Technical Support</a>.

You can <a href="#use-webhooks">use webhooks</a> for status updates instead of repeated API calls through <a href="#poll-for-updates">polling</a> and reuse <a href="#1-generate-access-token">OAuth 2.0 access tokens</a> (till their expiry time) to avoid unnecessary requests.

### Payouts SDK

You can use the PayPal Payouts SDK as an alternative to direct API integration. The SDK provides methods for authentication, request construction, and error handling in multiple programming languages. For more information, see <a href="/growth/payouts/reference/payouts-sdk" target="_blank" rel="noopener noreferrer">Payouts SDK</a>.

## End-to-end workflow

![Payouts API end-to-end workflow diagram](assets/paypal-payouts-api-flow.png)

## Prerequisites

- Complete all mandatory steps to <a href="/growth/payouts/set-up#set-up-sandbox-account-for-payouts-api-integration" target="_blank" rel="noopener noreferrer">get started</a>.
- Ensure your <a href="/growth/payouts/set-up#set-up-live-account" target="_blank" rel="noopener noreferrer">PayPal business account is set up</a>.
- Ensure to <a href="/growth/payouts/set-up#fund-your-account" target="_blank" rel="noopener noreferrer">fund your business account</a>.

## Send payouts

You can use the procedures in this section to send payouts using the Payouts API.

### 1. Create payout batch

Use a <a href="https://docs.paypal.ai/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a POST call to the `/v1/payments/payouts` endpoint.

<Tip>You can use the `PayPal-Request-Id` header parameter to <a href="/growth/payouts/customize/customize-payouts-api-integration#implement-idempotency" target="_blank" rel="noopener noreferrer">implement idempotency</a>.</Tip>

Include the following parameters:

| <span style={{textAlign: 'left', display: 'block'}}>Parameter </span>                                                                                             | <span style={{textAlign: 'left', display: 'block'}}>Action</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sender_batch_header`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>object</span> | Use the `sender_batch_id` within this header to <a href="/growth/payouts/customize/customize-payouts-api-integration#prevent-duplicate-requests" target="_blank" rel="noopener noreferrer">prevent duplicate requests</a>.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `items.amount`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>object</span>        | To pay a recipient in their local currency, set the `currency` parameter to the <a href="/growth/payouts/reference/countries-supported-features#eligible-countries-and-their-feature-sets" target="_blank" rel="noopener noreferrer">local currency code</a>. PayPal converts the payment to the specified currency and applies conversion fees. When you <a href="#poll-for-updates" rel="noopener noreferrer">retrieve the payout details</a>, the response shows the funding source, payout amount, fees, and other currency conversion details. For a sample request and response for cross-currency payouts, see <a href="/growth/payouts/customize/customize-payouts-api-integration#pay-recipients-in-their-local-currency" target="_blank" rel="noopener noreferrer">Pay in local currency</a>.<br /><Note>Review <a href="/growth/payouts/reference/countries-supported-features#currency-conversion" target="_blank" rel="noopener noreferrer">country exclusions and restrictions</a> before sending cross-currency payouts.</Note> |
| `items.receiver`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>      | Pass the value that identifies the recipient. <br />For example, [user@example.com](mailto:user@example.com), +15555550123, @venmousername, PAYPALUSERID123                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `items.recipient_type`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                                                                   | For Venmo payouts, set the recipient type to `USER_HANDLE` and pass the handle in `items.receiver`. <br /><br />**Possible values**: `PHONE`, `EMAIL`, `USER_HANDLE`, `PAYPAL_ID`<br /><br />**Default value**: `EMAIL` <br /><Note>If you set the recipient type in `sender_batch_header`, all items use that type unless you override it per item.</Note>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `items.recipient_wallet`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                                                                 | Set the recipient wallet type. <br /><br />**Possible values**:<ul><li>**Venmo**: Set to `Venmo` to send a payout to a Venmo account. Use `PHONE`, `EMAIL`, or `USER_HANDLE` as the `recipient_type`. <Note>Venmo payouts are available only in the US. If the recipient does not have a Venmo account, they receive instructions to create one and claim the payout.</Note></li><li>**PayPal**: Set to `PayPal` to send a payout to a PayPal account. This is the default value.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

For information on all parameters, see <a href="https://docs.paypal.ai/reference/api/rest/payouts/create-batch-payout" target="_blank" rel="noopener noreferrer">API reference</a>.

<CodeGroup>
  ```shell Sample request lines expandable theme={null}
  curl -X POST https://api-m.sandbox.paypal.com/v1/payments/payouts \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer ACCESS-TOKEN' \
    -H 'PayPal-Request-Id: REQUEST-ID' \
    -d '{
      "sender_batch_header": {
        "sender_batch_id": "Batch-123",
        "email_subject": "You have a payout!"
      },
      "items": [
        {
          "recipient_type": "EMAIL",
          "amount": {
            "value": "10.00",
            "currency": "USD"
          },
          "receiver": "recipient@example.com",
          "note": "Thank you for your business!",
          "sender_item_id": "ITEM-ID-1"
        },
        {
          "recipient_type": "PHONE",
          "amount": {
            "value": "10.00",
            "currency": "USD"
          },
          "receiver": "+15555550123",
          "note": "Thanks for using Venmo!",
          "sender_item_id": "ITEM-ID-2"
        }
      ]
    }'
  ```

```json Sample response lines theme={null}
{
  "batch_header": {
    "payout_batch_id": "3TRXJ4Z8XJ8QY",
    "batch_status": "PENDING",
    "sender_batch_header": {
      "sender_batch_id": "Batch-123",
      "email_subject": "You have a payout!"
    }
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/payments/payouts/3TRXJ4Z8XJ8QY",
      "rel": "self",
      "method": "GET",
      "encType": "application/json"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `201 Created` response. The response includes the following parameters:

| <span style={{textAlign: 'left', display: 'block'}}>Parameter</span> | <span style={{textAlign: 'left', display: 'block'}}>Description</span>                                                | <span style={{textAlign: 'left', display: 'block'}}>Further action</span>                                                                                                                                                                |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `batch_header.payout_batch_id`                                       | Unique ID for the payout batch.                                                                                       | Use this ID to track or reference the batch in future API calls.                                                                                                                                                                         |
| `batch_header.batch_status`                                          | Status of the payout batch.<br /><br />**Possible values**: `SUCCESS`, `PENDING`, `PROCESSING`, `DENIED`, `CANCELED`. | PayPal may process the batch immediately or later. If the status is `PENDING`, check again later. <br /><br />To retry after a server error (such as HTTP `5xx`), send the request again with the same `sender_batch_id` within 30 days. |
| `batch_header.sender_batch_header`                                   | Metadata of the payout batch that the sender originally provided in the payout request.                               | You can use it to match the response with your original request parameters.                                                                                                                                                              |
| `links`                                                              | URLs to get batch or item status.                                                                                     | Use these URLs to check the status of the batch or individual items.                                                                                                                                                                     |

### 2. Track status

After placing the payouts request, you can code your app to track the payout status by [polling for updates](#poll-for-updates) or [using webhooks](#use-webhooks).

#### Poll for updates

Use a <a href="https://docs.paypal.ai/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a GET call to the `/v1/payments/payouts/{ID}` endpoint. <br />
**Path parameter**: `ID` is the `payout_batch_id` returned in the <a href="#1-create-payout-batch">Create payout batch</a> response.

<Tip>You can customize the request and choose which information to get in the response. See <a href="/growth/payouts/customize/customize-payouts-api-integration#get-specific-payout-details" target="_blank" rel="noopener noreferrer">Get specific payouts details</a>.</Tip>

<CodeGroup>
  ```shell Sample request lines  theme={null}
  curl -X GET https://api-m.sandbox.paypal.com/v1/payments/payouts/MJ77GF8MQ2TF6 \
    -H 'Authorization: Bearer ACCESS-TOKEN' \
    -H 'Content-Type: application/json'
  ```

```json Sample response lines expandable theme={null}
{
  "total_items": 3,
  "total_pages": 1,
  "batch_header": {
    "payout_batch_id": "MJ77GF8MQ2TF6",
    "batch_status": "SUCCESS",
    "time_created": "2023-04-10T20:16:44Z",
    "time_completed": "2023-04-10T20:16:45Z",
    "sender_batch_header": {
      "sender_batch_id": "Payouts_1681157804",
      "email_subject": "You have a payout!",
      "email_message": "You have received a payout! Thanks for using our service!"
    },
    "funding_source": "BALANCE",
    "amount": {
      "currency": "USD",
      "value": "60.00"
    },
    "fees": {
      "currency": "USD",
      "value": "0.50"
    }
  },
  "items": [
    {
      "payout_item_id": "CX64X3KPCVYLC",
      "transaction_id": "4XH44110EC095525K",
      "activity_id": "0KJ317812H109105P",
      "transaction_status": "UNCLAIMED",
      "payout_item_fee": {
        "currency": "USD",
        "value": "0.25"
      },
      "payout_batch_id": "MJ77GF8MQ2TF6",
      "payout_item": {
        "recipient_type": "EMAIL",
        "amount": {
          "currency": "USD",
          "value": "10.00"
        },
        "note": "Thanks for your patronage!",
        "receiver": "recipient@example.com",
        "sender_item_id": "201403140001",
        "recipient_wallet": "PAYPAL"
      },
      "time_processed": "2023-04-10T20:16:45Z",
      "links": [
        {
          "href": "https://api.sandbox.paypal.com/v1/payments/payouts-item/CX64X3KPCVYLC",
          "rel": "item",
          "method": "GET"
        }
      ]
    },
    {
      "payout_item_id": "S697W7QJMAEX4",
      "transaction_id": "0FY48488BY887313U",
      "transaction_status": "UNCLAIMED",
      "payout_item_fee": {
        "currency": "USD",
        "value": "0.25"
      },
      "payout_item": {
        "recipient_type": "PHONE",
        "amount": {
          "currency": "USD",
          "value": "20.00"
        },
        "note": "Thanks for your support!",
        "receiver": "15562941698",
        "sender_item_id": "201403140002",
        "recipient_wallet": "PAYPAL"
      },
      "time_processed": "2023-04-10T20:16:45Z"
    },
    {
      "payout_item_id": "J64P4FHTAY7UN",
      "transaction_status": "FAILED",
      "payout_item_fee": {
        "currency": "USD",
        "value": "0.00"
      },
      "payout_item": {
        "recipient_type": "PAYPAL_ID",
        "amount": {
          "currency": "USD",
          "value": "30.00"
        },
        "note": "Thanks for your patronage!",
        "receiver": "invalid@example.com",
        "sender_item_id": "201403140003",
        "recipient_wallet": "PAYPAL"
      },
      "errors": {
        "name": "RECEIVER_ACCOUNT_INVALID",
        "message": "Receiver's account is invalid."
      }
    }
  ],
  "links": [
    {
      "href": "https://api.sandbox.paypal.com/v1/payments/payouts/MJ77GF8MQ2TF6?page_size=1000&page=1",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `200 OK` response. The response includes the following parameters:

| <span style={{textAlign: 'left', display: 'block'}}>Parameter </span> | <span style={{textAlign: 'left', display: 'block'}}>Description </span>                                                                                                                                                                                                                                                                                                                                  | <span style={{textAlign: 'left', display: 'block'}}>Action </span>                                                                                                                                                                                                       |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `batch_header.batch_status`                                           | Status of the payout batch.<br /><br />**Possible values**:<br /><ul><li>`SUCCESS`: PayPal has processed and completed the payout batch.</li><li>`PENDING`: PayPal has queued the payout batch for processing.</li><li>`PROCESSING`: PayPal is processing the payout batch.</li><li>`DENIED`: PayPal has denied the payout requests.</li><li>`CANCELED`: PayPal has canceled the payout batch.</li></ul> | If the status is `PENDING` or `PROCESSING`, check again later. <br />If the status is `DENIED` or `CANCELED`, review the error message or reason and resubmit if needed. <Tip>For real-time updates about payout events, <a href="#use-webhooks">use webhooks</a>.</Tip> |
| `batch_header.sender_batch_header`                                    | Metadata of the payout batch that the sender originally provided in the payout request.                                                                                                                                                                                                                                                                                                                  | You can use it to match the response with your original request parameters.                                                                                                                                                                                              |
| `items`                                                               | Array of payout items with details for each item.                                                                                                                                                                                                                                                                                                                                                        | Use the `payout_item_id` to <a href="/growth/payouts/manage-payouts/track-payout-item-status" target="_blank" rel="noopener noreferrer">track the status of each payout item</a>.                                                                                        |
| `links`                                                               | URLs to get batch or item status.                                                                                                                                                                                                                                                                                                                                                                        | You can use them to poll for updates.                                                                                                                                                                                                                                    |

<Note>For information on all parameters, see <a href="/reference/api/rest/payouts/show-payout-batch-details" target="_blank" rel="noopener noreferrer">API reference</a>.</Note>

#### Use webhooks

Webhook events are external events that your app does not know about unless it receives event notifications. For example, a payout processed or completed is a webhook event. You can subscribe to such events and register a callback (listener) URL. When the event occurs, PayPal sends a notification to the registered callback URL. You can code your app to perform relevant actions based on the event notification it receives.

To handle webhook events:

1. Review the <a href="/reference/webhook-events/payouts-v1" target="_blank">list of webhook events for Payouts</a> and select the events for your app to subscribe.
2. Subscribe to the selected webhook events through one of the following means:
   - **PayPal developer account**: Log in to your account, go to <strong>App details</strong> page > <strong>Features</strong> > <strong>Webhooks</strong>, and subscribe to webhook events.
   - <a href="/reference/api/rest/webhooks/create-webhook" target="_blank">Webhooks management API</a>.
3. In your server-side app code, define a webhook handler that:
   - <a href="https://developer.paypal.com/api/rest/webhooks/rest/#link-subscribingalistenerurl" target="_blank">Listens to the webhook event</a>.
   - <a href="https://developer.paypal.com/api/rest/webhooks/#link-receivingthemessage" target="_blank">Confirms receipt of the webhook event to PayPal</a>.
   - <a href="https://developer.paypal.com/api/rest/webhooks/#link-verifyingthemessagereceived" target="_blank">Verifies the source of the event notification</a>.
   - Performs further actions based on event data.

For more information, see <a href="https://developer.paypal.com/api/rest/webhooks/" target="_blank">Webhooks overview</a> and <a href="https://developer.paypal.com/api/rest/webhooks/rest/" target="_blank">Webhooks integration guide</a>.

### 3. Handle errors

PayPal uses standard HTTP status codes to indicate the result of an API request:

- `2xx`: Success
- `4xx`: Incorrect request (for example, missing parameter)
- `5xx`: PayPal server error

When an API call returns an error, the response includes a JSON body with the error details and HATEOAS links to help you diagnose and resolve issues. In your app code, include the logic to review the error code, message, and related links to determine the cause. Implement actions based on the error processing.
For more information, see <a href="/developer/how-to/api/handling-api-responses" target="_blank">API responses</a>.

### 4. Test

Use the PayPal sandbox environment to ensure your integration works as expected and meets all business and technical requirements before you go live.

Testing your Payouts API integration involves:

- Testing end-to-end payouts flow to verify money movement from your business account to your personal account (in case of PayPal payouts) or out of your business account (in case of Venmo payouts).
- <a href="#test-api-calls%3A-use-test-values-and-simulate-responses">Testing API calls</a>.

#### Test API calls: use test values and simulate responses

To simulate Payouts API responses, inject <a href="/growth/payouts/reference/payouts-api-test-values" target="_blank" rel="noopener noreferrer">test values</a> in the [request payload](#sample-test-value-in-request-payload) or as a [path parameter in the request URL](#sample-test-value-as-path-parameter). These methods allow you to trigger specific error responses without creating actual payouts.

<Tabs>
  <Tab title="Sample - test value in request payload" id="requestpayload">
    | <span style={{textAlign: 'left', display: 'block'}}>Trigger</span> | <span style={{textAlign: 'left', display: 'block'}}>Test value</span> | <span style={{textAlign: 'left', display: 'block'}}>Simulated error response</span> |
    | ------------------------------------------------------------------ | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
    | items\[0]/note                                                     | ERRPYO002                                                             | `SENDER_EMAIL_UNCONFIRMED`                                                          |

    <CodeGroup>
      ```shell Sample request lines expandable theme={null}
      curl -X POST https://api-m.sandbox.paypal.com/v1/payments/payouts \
        -H 'Content-Type: application/json' \
        -H 'Authorization: Bearer ACCESS-TOKEN' \
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
            }
          ]
        }'
      ```

      ```json Sample response lines theme={null}
      {
        "name": "SENDER_EMAIL_UNCONFIRMED",
        "message": "Authorization error occurred",
        "debug_id": "ca787bdf80d7a",
        "information_link": "https://developer.paypal.com/docs/api/payments.payouts-batch/v1/#errors"
      }
      ```
    </CodeGroup>

  </Tab>

  <Tab title="Sample - test value as path parameter" id="pathparam">
    | <span style={{textAlign: 'left', display: 'block'}}>Path parameter</span> | <span style={{textAlign: 'left', display: 'block'}}>Test value</span> | <span style={{textAlign: 'left', display: 'block'}}>Simulated error response</span> |
    | ------------------------------------------------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
    | /v1/payments/payouts/                                                     | ERRPYO015                                                             | `CLOSED_MARKET`                                                                     |

    <CodeGroup>
      ```bash Sample request lines theme={null}
      curl -X GET https://api-m.sandbox.paypal.com/v1/payments/payouts/ERRPYO015 \
        -H 'Content-Type: application/json' \
        -H 'Authorization: Bearer ACCESS-TOKEN'
      ```

      ```json Sample response lines expandable theme={null}
      {
        "batch_header": {
          "payout_batch_id": "DQCP2UAJCBMNY",
          "batch_status": "SUCCESS",
          "time_created": "2017-08-21T11:22:33Z",
          "time_completed": "2017-08-21T11:22:54Z",
          "sender_batch_header": {
            "email_subject": "user test case"
          },
          "amount": {
            "currency": "USD",
            "value": "190.0"
          },
          "fees": {
            "currency": "USD",
            "value": "0.0"
          }
        },
        "items": [
          {
            "payout_item_id": "RWD4Y3H9VV8BA",
            "transaction_status": "FAILED",
            "errors": {
              "name": "CLOSED_MARKET",
              "message": "Payouts to this market are not supported.",
              "information_link": "https://developer.paypal.com/docs/api/payments.payouts-batch/v1/#errors",
              "details": []
            },
            "links": [
              {
                "href": "https://api-m.sandbox.paypal.com/v1/payments/payouts-item/RWD4Y3H9VV8BA",
                "rel": "item",
                "method": "GET",
                "encType": "application/json"
              }
            ]
          }
        ],
        "links": [
          {
            "href": "https://api-m.sandbox.paypal.com/v1/payments/payouts/DQCP2UAJCBMNY",
            "rel": "self",
            "method": "GET",
            "encType": "application/json"
          }
        ]
      }
      ```
    </CodeGroup>

  </Tab>
</Tabs>

### 5. Go live

1. <a href="/growth/payouts/set-up#set-up-live-account" target="_blank" rel="noopener noreferrer">Set up live account.</a>
2. <a href="https://developer.paypal.com/docs/api-basics/notifications/webhooks/" target="_blank" rel="noopener noreferrer">Set up webhooks</a> to get real-time notifications about payout events, such as completed or failed payouts.
3. <a href="https://developer.paypal.com/api/rest/production/" target="_blank" rel="noopener noreferrer">Go live with your app</a>.
