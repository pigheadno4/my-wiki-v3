---
title: Integrate API
slug: /docs/payouts/standard/integrate-api/
createTime: "2024-06-24T07:34:34.343Z"
updateTime: "2025-05-09T13:13:02.312Z"
---

# Integrate API

The Payouts API enables you to send payouts programmatically to your recipients. This page explains everything you need to know about making payouts using the Payouts API.

## How it works

When you initiate a payouts request, the Payouts API:

- Validates your request and processes the payouts.
- Sends you a status report.
- Notifies recipients that they have a payment.

## Know before you code

- Complete the steps in [Get started](/api/rest/) to get the following sandbox account information from the Developer Dashboard: - Your personal and business sandbox accounts
- Your access token

- [Request access to PayPal Payouts](https://www.paypal.com/payoutsweb/landing) .
- Set up your PayPal business account for Payouts: - [Confirm your identity](https://www.paypal.com/policy/flow/verifyCip)
- [Confirm your email](https://www.paypal.com/in/cshelp/article/how-do-i-confirm-my-email-address-help138)
- [Link your bank account](https://www.paypal.com/businessexp/money/addbank)
- Add enough money to cover your payout total, including [fees](https://www.paypal.com/us/webapps/mpp/merchant-fees#paypal-payouts)

- You can send up to 15,000 payments in one API call.
- This integration uses the [Payouts REST API](/docs/api/payments.payouts-batch/v1/) .
- Use Postman to explore and test PayPal APIs.

The sample request below creates a payout in USD for three recipients: two PayPal recipients and one Venmo recipient using the API endpoint [Create batch payout](/docs/api/payments.payouts-batch/v1/#payouts_post) .

#### **`Create a payout`**

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v1/payments/payouts \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <Access-Token>" \
  -d '{
  "sender_batch_header": {
    "sender_batch_id": "2014021801",
    "recipient_type": "EMAIL",
    "email_subject": "You have money!",
    "email_message": "You received a payment. Thanks for using our service!"
  },
  "items": [
    {
      "amount": {
        "value": "9.87",
        "currency": "USD"
      },
      "sender_item_id": "201403140001",
      "recipient_wallet": "PAYPAL",
      "receiver": "<receiver@example.com>"
    },
    {
      "amount": {
        "value": "112.34",
        "currency": "USD"
      },
      "sender_item_id": "201403140002",
      "recipient_wallet": "PAYPAL",
      "receiver": "<receiver2@example.com>"
    },
    {
      "recipient_type": "PHONE",
      "amount": {
        "value": "5.32",
        "currency": "USD"
      },
      "note": "Thanks for using our service!",
      "sender_item_id": "201403140003",
      "recipient_wallet": "PAYPAL",
      "receiver": "<408-234-1234>"
    }
  ]
}'
```

## Modify the code

Copy the code sample above and modify the following values:

- Change Access-Token to your [access token](/docs/multiparty/get-started/#exchange-your-api-credentials-for-an-access-token) .
- Change &lt;receiver@example.com&gt; and &lt;receiver2@example.com&gt; to sandbox account email addresses.
- Change &lt;408-234-1234&gt; to a sandbox account phone number.
- Optional: To send payments to Venmo recipients, set recipient_wallet to VENMO . Include a U.S. mobile number and a note in the payout item.
- Optional: To send a payout in a different currency, set the currency parameter to the payment's [currency code](/docs/business/develop/currency-codes/) . You'll need to make a separate API call for each currency type. PayPal can automatically exchange payments for [some currencies](/docs/payouts/standard/reference/currency-conversion/#automatic) , even when you don't hold a balance in that currency.

**info**
**Note**: Payout items default to the recipient_type in the sender_batch_header , unless an item has its own recipient_type . If there's no recipient_type in the sender_batch_header , each item must include its own recipient_type .

## Step result

A successful request returns:

- A return status code of HTTP 201 Created .
- A JSON response body with the payout_batch_id . Use the payout_batch_id in the [show payout batch details](/docs/api/payments.payouts-batch/v1/#payouts_get) endpoint to get a detailed record of each item in the payout.

**info**
**Tip** :You can log into your PayPal business account and see payout details on the **Activity** and **Reports** pages.

#### **`Sample code`**

```javascript
{
  "batch_header": {
    "payout_batch_id": "Y4JB5BNLE8Z88",
    "batch_status": "PENDING",
    "sender_batch_header": {
      "sender_batch_id": "2014021801",
      "recipient_type": "EMAIL",
      "email_subject": "You have money!",
      "email_message": "You received a payment. Thanks for using our service!"
    }
  },
  "links": [{
    "href": "https://api-m.sandbox.paypal.com/v1/payments/payouts/Y4JB5BNLE8Z88",
    "rel": "self",
    "method": "GET",
    "encType": "application/json"
  }]
}
```

## Error messages

For information on Payouts API error messages, see [Payouts Error Messages](/docs/api/payments.payouts-batch/v1/#errors) .

## Next

[Customize your integration](/docs/payouts/standard/integrate-api/customize)

## See also

- [PayPal API Executor](https://www.paypal.com/apex/product-profile/payouts/getAccessToken) —Make test calls to the Payouts API.
- [Payouts REST API](/docs/api/payments.payouts-batch/v1/)
