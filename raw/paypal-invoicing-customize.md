---
title: Customize Invoicing
slug: /docs/invoicing/customize/
createTime: "2024-05-13T20:13:05.554Z"
updateTime: "2026-01-07T08:13:47.882Z"
---

# Customize Invoicing

The Invoicing REST API supports search, refunds, templates, reminders, and more.

This page describes a few ways you can customize an invoice. Refer to the [Invoicing API reference](/docs/api/invoicing/v2/#invoices) to see everything you can do with the Invoicing API.

You can also [make test calls to the Invoicing API with the PayPal API Executor](https://www.paypal.com/apex/product-profile/invoicing_v2/) .

## Create QR code

When a buyer uses a mobile device to scan the QR code, they're redirected to the PayPal mobile payment flow to view the invoice and pay online with PayPal or another payment type.

###

### 1. Create codes

To generate a QR code, first [create and send an invoice](https://developer.paypal.com/docs/multiparty/invoicing/integrate/) .

If you don't want PayPal to email the invoice notification to your buyer when you create it, because you want to send a QR code, set send_to_recipient in the Send invoice request to false . This parameter updates the invoice status to UNPAID and does not send the email notification.

Copy the invoice ID returned when you create the invoice.

To create a QR code for your invoice, copy the following code and modify it.

#### Sample request

API endpoint used: [Generate QR code](/docs/api/invoicing/v2/#invoices_generate-qr-code)

#### **`Sample request`**

```javascript
curl -v -X POST https://api-m.sandbox.paypal.com/v2/invoicing/invoices/{INVOICE-ID}/generate-qr-code \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'PayPal-Partner-Attribution-Id: BN-CODE' \
  -H 'PayPal-Auth-Assertion: AUTH-ASSERTION-JWT'
```

#### **`Sample response`**

```curl
--2e4a1c93-9ec0-448b-8c6e-c2a691240f2f
      Content-Disposition: form-data; name="image"
      Content-Type: application/json \

      iVBORw0KGgoAAAANSUhEUgAAAJYAAACWAQAAAAAUekxPAAAByElEQVR42u2WsW30MAyFabhQ51tAgNdQp5XsBXy+BeyV1GkNAVrA7lQIYp4ucf4L/kZMEaSIoeorKPGRjzTxf1+mP/ZTLBCFQcUz6ckQWRGLnMIt9YX6M3ERstXER4oPlxcTBjELM9OiEO8bjNmPzPpLvDbGKR4UOsdfcmti0C9u5v28aNrEaqkWmzsX7q+1bGJhIT5dPAweoq87Ghk/fB4ATCZLi4zFHZ1CiKQHG08WMSRBM0KquDv9oX0rYzTLptAyXNSnfo0sTHbcXf/g0PlYhOzuIl40WGgQL+0bWTwsbybUuiV96dfIYKwKnsHGVcZ4rxKOT09ffdrKYEeaCNnToGq7SRgkD7NHPFpovO5oZHGjEXU7kZAPJGN59nRzz3i2LzIWJpNvrDumwaL+Isargpt1lzAYxkPG4GZC3SD8Vu0lYjV1ZLDZfE/0oX0r48NgFMFVsGbPQnaynr2GOdiNu4yhSfui4qryQp++bGRcx4nDREE2YZExJJHvKJqBhPHfbmxidd4XUxfFZONqZQz7DXN3JS5EN5Yy3mzdrpPRk5WyPGFHeZSuP1nGEKnzYcCOsjgiVvdbUXlm/E287rwW9ve/9ovYG2Y/Iq/A3o7lAAAAAElFTkSuQmCC
      --2e4a1c93-9ec0-448b-8c6e-c2a691240f2f--
```

#### Modify code

After you copy the code in the sample request, modify the following:

- Change ACCESS-TOKEN to your [access token](https://developer.paypal.com/docs/multiparty/get-started/#exchange-your-api-credentials-for-an-access-token) .
- Change BN-CODE to your [PayPal Attribution ID](https://developer.paypal.com/api/rest/requests/#paypal-partner-attribution-id) to receive revenue attribution. To find your BN code, see [Code and Credential Reference](https://developer.paypal.com/docs/multiparty/create-account/#link-bncode) .
- Change AUTH-ASSERTION-JWT to your [PayPal-Auth-Assertion](https://developer.paypal.com/api/rest/requests/#link-paypalauthassertion) token.
- Change INVOICE-ID to the invoice ID that was returned when you created the invoice.

#### Step result

A successful response results in:

- A return status code of HTTP 200 OK .
- A JSON response body that shows the QR code as an encoded Base64 image, such as:

#### 2. Test QR code

To test your QR code, complete these steps:

- Use your preferred programming language or online tool to decode the Base64-encoded value to an image.
- Scan the QR code to open the invoice.

## Add tips

To include a field that enables the customer to add a tip as a flat amount or percent of the total due, set the [allow_tip](https://developer.paypal.com/docs/api/invoicing/v2/#definition-configuration) parameter to true .

**info**
**Note:** If the customer adds a tip, it shows up on the invoice and in the payment notification email.

## Enable partial and minimum due payments

To enable the customer to make a partial payment, set the [allow_partial_payment](https://developer.paypal.com/docs/api/invoicing/v2/#definition-partial_payment) parameter to true .

When you enable a partial payment, you can also set the [minimum_amount_due](https://developer.paypal.com/docs/api/invoicing/v2/#definition-partial_payment) parameter to the minimum amount due value.

## Next

[Test and go live with your Invoicing integration](/docs/invoicing/test-and-go-live/)
