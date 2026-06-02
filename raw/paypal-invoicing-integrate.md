---
title: Integrate invoicing
slug: /docs/invoicing/integrate/
createTime: "2024-05-15T17:52:06.969Z"
updateTime: "2026-04-07T14:58:08.437Z"
---

# Integrate invoicing

PayPal Invoicing API helps you create, update, send, and manage invoices programmatically from your backend systems.
This quick start is for developers who want a minimal, end-to-end example in a sandbox account and need to see the core create-and-send flow with as little setup as possible. You’ll use the PayPal Invoicing REST API to create a draft invoice in your sandbox account, send it to a test customer, and verify that the invoice appears in your sandbox business account. ## Prerequisites

- [PayPal business account](https://www.paypal.com/business/open-business-account?_ga=2.49411041.673139926.1760916697-1259758161.1760473483) with Invoicing enabled.
- Obtain your sandbox credentials and access token. Refer to [Get Started with PayPal REST APIs](https://developer.paypal.com/api/rest/) for more information.
- (Optional) Use a test email you can access, not your PayPal business email.
  For the complete API reference, including full schema definitions and interactive examples, see the [Invoicing API Reference](https://developer.paypal.com/docs/api/invoicing/v2/) .
  ​

## What you’ll build

After completing this quick start, you will have:- Created a draft invoice in your sandbox account

- Sent the invoice to a sandbox customer email address
- Confirmed the invoice status has changed to UNPAID ​

## Flow summary

- Your server sends a POST request to create a draft invoice.
- PayPal creates the invoice resource and returns an invoice ID.
- Your server sends a POST request to send the invoice.
- PayPal delivers the invoice to the recipient and updates the status.
- You verify the invoice appears as UNPAID in your sandbox account.

Open the dashboard, then create or select an app. Copy the Client ID and Secret. Use these credentials to generate an access token, and include that token in the Authorization header for every request.

**Note:** Replace CLIENT_ID and CLIENT_SECRET with your sandbox app credentials from the dashboard.

#### **`quick start, step 1, invoicing`**

```curl
curl -X POST https://api-m.sandbox.paypal.com/v1/oauth2/token \
  -H "Accept: application/json" \
  -H "Accept-Language: en_US" \
  -u "YOUR_CLIENT_ID:YOUR_CLIENT_SECRET" \
  -d "grant_type=client_credentials"
```

#### Expected result

- A successful token request returns the status 200 OK .
- Copy the access_token value from the response body. You'll use this value in Steps 2 and 3.

Create a draft invoice in a single API call. The invoice is not visible to your customer yet. This step generates the invoice with all required details, such as customer, items, and amount, before sending to the customer. The invoice workflow is:**Draft**→**Sent**→**Viewed**→**Paid**(or**Cancelled**/**Overdue**).

This example creates a draft invoice. Save the returned `id`, then call the send invoice endpoint when you're ready to request payment.

**Note:** Replace ACCESS_TOKEN with your token from Step 1, and replace customer@example.com with your sandbox personal account email.

#### **`Sample request`**

```curl
curl -X POST https://api-m.sandbox.paypal.com/v2/invoicing/invoices \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "detail": {
      "currency_code": "USD",
      "note": "Thanks for your business"
    },
    "invoicer": {
      "name": {
        "given_name": "Jane",
        "surname": "Doe"
      }
    },
    "primary_recipients": [
      {
        "billing_info": {
          "email_address": "customer@example.com"
        }
      }
    ],
    "items": [
      {
        "name": "Website design",
        "quantity": "1",
        "unit_amount": {
          "currency_code": "USD",
          "value": "500.00"
        }
      }
    ]
  }'
```

#### Expected result

- A successful request returns the status 201 Created .
- The response body contains an href link with your invoice ID ( INV2-XXXX-XXXX-XXXX-XXXX ).
- The invoice appears in your sandbox account with Draft status.
- The invoice is not yet visible to the customer.

In your sandbox account, send the draft invoice you created in the previous step. This moves the invoice fromDRAFTtoSENTstatus, and PayPal sends a secure payment link in the email to your customer. Use theidfrom step 2 and pass it as theinvoice_idpath parameter. To change details in the sent invoice, update the specific details using thePUTmethod, andsend_to_recipient: trueto notify the customer.

**Note:** After you send an invoice, you can’t delete it. You can only cancel it to mark it as no longer active.

#### **`Sample request`**

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/invoicing/invoices/{invoice_id}/send \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "send_to_recipient": true,
    "send_to_invoicer": true
  }'
```

#### Expected result

- A successful request returns the status 200 OK .
- The invoice status changes to UNPAID in your sandbox account.
- PayPal sends the invoice to the customer email address provided in Step 2.
- The customer receives a payment link to pay through PayPal's hosted payment page.

## Verify it works

You should see:- Invoice appears in your sandbox PayPal business account under **Invoicing** .

- Invoice status shows as UNPAID .
- The customer email address you provided has received a payment notification.
- The invoice ID returned in Step 2 matches the invoice visible in the dashboard.

## Next steps

### Customize your integration

Learn more about customizing your invoicing integration
