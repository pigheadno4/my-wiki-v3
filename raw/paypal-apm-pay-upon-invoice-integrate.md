---
title: Integrate Pay upon Invoice
slug: /docs/checkout/apm/pay-upon-invoice/integrate-pui-merchant/
createTime: "2024-10-24T04:38:12.060Z"
updateTime: "2025-05-14T12:22:09.506Z"
---

# Integrate Pay upon Invoice

## Know before you code

- Request approval to enable Pay upon Invoice by visiting these Sandbox and Live links: - Sandbox - [https://www.sandbox.paypal.com/bizsignup/entry?country.x=DE&product=payment_methods&capabilities=PAY_UPON_INVOICE](https://www.sandbox.paypal.com/bizsignup/entry?country.x=DE&product=payment_methods&capabilities=PAY_UPON_INVOICE)
- Live - [https://www.paypal.com/bizsignup/entry?country.x=DE&product=payment_methods&capabilities=PAY_UPON_INVOICE](https://www.paypal.com/bizsignup/entry?country.x=DE&product=payment_methods&capabilities=PAY_UPON_INVOICE)

- Make sure you're [subscribed to the following webhook events](https:/docs/checkout/apm/reference/subscribe-to-webhooks/) : - The PAYMENT.CAPTURE.COMPLETED webhook event indicates a successful order capture.
- The PAYMENT.CAPTURE.DENIED and CHECKOUT.PAYMENT-APPROVAL.REVERSED webhook events indicate a failed order capture.

- Make sure your preference for receiving payments in your PayPal business or merchant account is set to accept and convert to the currency in your account. In your profile, select **Account Settings** &gt; **Payment preferences** &gt; **Block payments** and click **Update** to mark this preference.
- You can use only intent=CAPTURE in [Create order](https:/docs/api/orders/v2/#orders_create) to process payments using Pay upon Invoice.
- Request that buyers provide their birth date to process payments using Pay upon Invoice.
- You are legally obligated to display the messages to the buyer as described in the [Error codes and error messages](#error-codes-and-error-messages) section.
- Use Postman to explore and test PayPal APIs.

## 1. Offer Pay upon Invoice on your checkout page

Create the user interface to offer Pay upon Invoice and collect the buyer's information.

On your Pay upon Invoice checkout page, you'll need to complete the following:

- **Required.** Integrate with the [FraudNet JavaScript library](https:/docs/checkout/apm/pay-upon-invoice/fraudnet/) to allow Ratepay to complete their buyer credit and risk checks.
- **Required.** Present the following legal text to the buyer in English or German in one of the following ways:

A. Integrate with the PUI Legal Component:

#### **`Code`**

```javascript
  <script src="https://www.paypal.com/sdk/js?client-id=test&components=legal"></script>
<div id="paypal-legal-container"></div>
<script>
  paypal
    .Legal({
      fundingSource: paypal.Legal.FUNDING.PAY_UPON_INVOICE,
    })
    .render("#paypal-legal-container");
</script>

```

B. Copy and paste the below text directly.

### English

By clicking on the button, you agree to the[terms of payment](https://www.ratepay.com/legal-payment-terms)and[performance of a risk check](https://www.ratepay.com/legal-payment-dataprivacy)from the payment partner, Ratepay. You also agree to PayPal’s[privacy statement](https://www.paypal.com/us/webapps/mpp/ua/privacy-full). If your request to purchase upon invoice is accepted, the purchase price claim will be assigned to Ratepay, and you may only pay Ratepay, not the merchant.
,### German
Mit Klicken auf den Button akzeptieren Sie die[Ratepay Zahlungsbedingungen](https://www.ratepay.com/legal-payment-terms)und erklären sich mit der Durchführung einer[Risikoprüfung durch Ratepay](https://www.ratepay.com/legal-payment-dataprivacy), unseren Partner, einverstanden. Sie akzeptieren auch PayPals[Datenschutzerklärung](https://www.paypal.com/de/webapps/mpp/ua/privacy-full?locale.x=de_DE). Falls Ihre Transaktion per Kauf auf Rechnung erfolgreich abgewickelt werden kann, wird der Kaufpreis an Ratepay abgetreten und Sie dürfen nur an Ratepay überweisen, nicht an den Händler.

## 2. Create an order

Create an order with Pay upon Invoice as the payment source. Use the buyer information you captured from your user interface to create an order with Pay upon Invoice as the payment source.

#### Sample request

API endpoint used: [Create order](https:/docs/api/orders/v2/#orders_create)

#### **`Code`**

```javascript
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <Access-Token>" \
-H "PayPal-Request-Id: 7b92603e-77ed-4896-8e78-5dea2050476a" \
-d '{
  "intent": "CAPTURE",
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "purchase_units": [
    {
      "amount": {
        "currency_code": "EUR",
        "value": "100.00",
        "breakdown": {
          "item_total": {
            "currency_code": "EUR",
            "value": "81.00"
          },
          "tax_total": {
            "currency_code": "EUR",
            "value": "19.00"
          }
        }
      },
      "shipping": {
        "name": {
          "full_name": "John Doe"
        },
        "address": {
          "address_line_1": "Taunusanlage 12",
          "admin_area_2": "FRANKFURT AM MAIN",
          "postal_code": "60325",
          "country_code": "DE"
        }
      },
      "items": [
        {
          "name": "Air Jordan Shoe",
          "category": "PHYSICAL_GOODS",
          "unit_amount": {
            "currency_code": "EUR",
            "value": "81.00"
          },
          "tax": {
            "currency_code": "EUR",
            "value": "19.00"
          },
          "tax_rate": "19.00",
          "quantity": "1"
        }
      ],
      "invoice_id": "MERCHANT_INVOICE_ID",
      "custom_id": "MERCHANT_CUSTOM_ID"
    }
  ],
  "payment_source": {
    "pay_upon_invoice": {
      "name": {
        "given_name": "John",
        "surname": "Doe"
      },
      "email": "buyer@example.com",
      "birth_date": "1990-01-01",
      "phone": {
        "national_number": "6912345678",
        "country_code": "49"
      },
      "billing_address": {
        "address_line_1": "Schönhauser Allee 84",
        "admin_area_2": "Berlin",
        "postal_code": "10439",
        "country_code": "DE"
      },
      "experience_context": {
        "locale": "en-DE",
        "brand_name": "EXAMPLE INC",
        "logo_url": "https://example.com/logoUrl.svg",
        "customer_service_instructions": [
          "Customer service phone is +49 6912345678."
        ]
      }
    }
  }
}'
```

### Modify the code

After you copy the code in the sample request, modify the following:

- Access-Token - Your [access token](https:/api/rest/authentication) .
- intent - This parameter must be set to CAPTURE as shown in this sample code.
- purchase_units: amount - Pass the amount of the order and the currency code.
- purchase_units: items - Pass the name, category, unit amount, tax amount and tax rate of various items in the order. Please note: only items from the category PHYSICAL_GOODS are permissible for Pay Upon Invoice. If items that do not belong in this category are wrongfully tagged as such, the transaction can be reversed.
- purchase_units: shipping - Pass the optional shipping name and address.
- payment_source - Specify the following: - pay_upon_invoice as the payment_source and include the country_code .
- Account holder's name on name field.
- Account holder's email on email field.
- Account holder's date of birth on birth_date field.
- Account holder's phone number on phone field.
- Account holder's billing address on billing_address field.
- experience_context - Specify preferred language, brand name, logo, and customer service instructions to be presented on Ratepay's payment instruction email sent to the buyer. Currently, you can use only German as the preferred language ( locale = de-DE ).

- processing_instruction - Set this value to ORDER_COMPLETE_ON_PAYMENT_APPROVAL as shown in this sample code.
- invoice_id - Pass the optional invoice number that identifies the order in your system. This order ID shows up in the payment instruction email that Ratepay sends to the buyer. We recommend that you pass this value to help Ratepay communicate with the buyer. If your request doesn't pass a value for invoice_id , Ratepay's payment instruction email shows the id value of the PayPal checkout order resource.
- Optional: Change or add other parameters in the [Create order request body](https:/docs/api/orders/v2/#orders_create) to create an order that reflects the actual order details.

### Step result

A successful request results in the following:

- A return status code of HTTP 201 Created .
- A JSON response body that contains the order ID. You'll use the order ID in the next step.

This indicates that Ratepay performed the buyer risk assessment successfully and approved the payment.

When the status returns PENDING_APPROVAL , display a message to the buyer that indicates checkout is complete. In the [next step](#3-listen-to-webhooks) , listen to the webhooks to get the result of the order capture, so you can notify the buyer offline of a successful or failed transaction.

### Sample response

#### **`Test`**

```javascript
{
  "id": "5O190127TN364715T",
  "status": "PENDING_APPROVAL",
  "payment_source": {
    "pay_upon_invoice": {
      "birth_date": "1990-01-01",
      "name": {
        "given_name": "John",
        "surname": "Doe"
      },
      "email": "buyer@example.com",
      "phone": {
        "national_number": "6912345678",
        "country_code": "49"
      },
      "billing_address": {
        "address_line_1": "Schönhauser Allee 84",
        "admin_area_2": "Berlin",
        "postal_code": "10439",
        "country_code": "DE"
      }
    }
  },
  "links": [
    {
      "href": "https://api-m.paypal.com/v2/checkout/orders/5O190127TN364715T",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```

## 3. Listen to webhooks

Listen to the following webhooks to get the result of order capture:

- The PAYMENT.CAPTURE.COMPLETED webhook event indicates a successful order capture.
- The PAYMENT.CAPTURE.DENIED and CHECKOUT.PAYMENT-APPROVAL.REVERSED webhook events indicate a failed order capture.

Getting the result might be delayed by a few moments.

#### Sample PAYMENT.CAPTURE.COMPLETED webhook

#### **`Code`**

```javascript
{
  "id": "WH-6WA12701B00483532-15737896PW730511B",
  "event_version": "1.0",
  "create_time": "2021-03-19T08:07:57.563Z",
  "resource_type": "capture",
  "resource_version": "2.0",
  "event_type": "PAYMENT.CAPTURE.COMPLETED",
  "summary": "Payment completed for EUR 1.0 EUR",
  "resource": {
    "id": "84745544P6340640G",
    "status": "COMPLETED",
    "amount": {
      "value": "100.00",
      "currency_code": "EUR"
    },
    "seller_receivable_breakdown": {
      "paypal_fee": {
        "value": "3.00",
        "currency_code": "EUR"
      },
      "gross_amount": {
        "value": "100.00",
        "currency_code": "EUR"
      },
      "net_amount": {
        "value": "97.00",
        "currency_code": "EUR"
      }
    },
    "custom_id": "MERCHANT_CUSTOM_ID",
    "invoice_id": "MERCHANT_INVOICE_ID",
    "seller_protection": {
      "status": "NOT_ELIGIBLE"
    },
    "supplementary_data": {
      "related_ids": {
        "order_id": "5O190127TN364715T"
      }
    },
    "update_time": "2021-03-19T08:07:40Z",
    "create_time": "2021-03-19T08:06:45Z",
    "final_capture": true,
    "links": [
      {
        "method": "GET",
        "rel": "self",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/826413372K501814R"
      },
      {
        "method": "POST",
        "rel": "refund",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/826413372K501814R/refund"
      },
      {
        "method": "GET",
        "rel": "up",
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T"
      }
    ]
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-6WA12701B00483532-15737896PW730511B",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-6WA12701B00483532-15737896PW730511B/resend",
      "rel": "resend",
      "method": "POST"
    }
  ]
}
```

Make sure the order ID from [Step 2](#2-create-an-order) matches resource.supplementary_data.related_ids.order_id parameter in the webhook payload.

### Sample PAYMENT.CAPTURE.DENIED webhook

#### **`Code`**

```javascript
{
  "id": "WH-11M70257FM3776948-8B478027S4286991F",
  "event_version": "1.0",
  "create_time": "2021-03-19T08:17:29.782Z",
  "resource_type": "capture",
  "resource_version": "2.0",
  "event_type": "PAYMENT.CAPTURE.DENIED",
  "summary": "Payment denied for EUR 100.0 EUR",
  "resource": {
    "id": "826413372K501814R",
    "status": "DECLINED",
    "amount": {
      "value": "100.00",
      "currency_code": "EUR"
    },
    "seller_receivable_breakdown": {
      "gross_amount": {
        "value": "100.00",
        "currency_code": "EUR"
      },
      "net_amount": {
        "value": "100.00",
        "currency_code": "EUR"
      }
    },
    "custom_id": "MERCHANT_CUSTOM_ID",
    "invoice_id": "MERCHANT_INVOICE_ID",
    "seller_protection": {
      "status": "NOT_ELIGIBLE"
    },
    "supplementary_data": {
      "related_ids": {
        "order_id": "5O190127TN364715T"
      }
    },
    "update_time": "2021-03-19T08:17:12Z",
    "create_time": "2021-03-19T08:16:01Z",
    "final_capture": true,
    "links": [
      {
        "method": "GET",
        "rel": "self",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/826413372K501814R"
      },
      {
        "method": "POST",
        "rel": "refund",
        "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/826413372K501814R/refund"
      },
      {
        "method": "GET",
        "rel": "up",
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T"
      }
    ]
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-11M70257FM3776948-8B478027S4286991F",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-11M70257FM3776948-8B478027S4286991F/resend",
      "rel": "resend",
      "method": "POST"
    }
  ]
}
```

Make sure the order ID from [Step 2](#2-create-an-order) matches the resource.supplementary_data.related_ids.order_id parameter in the webhook payload.

#### **`Code`**

```javascript
{
  "id": "WH-COC11055RA711503B-4YM959094A144403T",
  "create_time": "2021-03-19T08:17:29.782Z",
  "event_type": "CHECKOUT.PAYMENT-APPROVAL.REVERSED",
  "summary": "A payment has been reversed after approval.",
  "resource": {
    "order_id": "5O190127TN364715T",
    "purchase_units": [
      {
        "custom_id": "MERCHANT_CUSTOM_ID",
        "invoice_id": "MERCHANT_INVOICE_ID"
      }
    ],
    "payment_source": {
      "pay_upon_invoice": {
        "birth_date": "1990-01-01",
        "name": {
          "given_name": "John",
          "surname": "Doe"
        },
        "email": "buyer@example.com",
        "phone": {
          "national_number": "6912345678",
          "country_code": "49"
        },
        "billing_address": {
          "address_line_1": "Schönhauser Allee 84",
          "admin_area_2": "Berlin",
          "postal_code": "10439",
          "country_code": "DE"
        }
      }
    }
  },
  "event_version": "1.0"
}
```

Make sure the order ID from [Step 2](#2-create-an-order) matches the resource.order_id parameter in the webhook payload.

Alternatively, if your app misses the webhook needed to capture the order, you can get the order capture result by sending a GET call to the [Show order details](/docs/api/orders/v2/#orders_get) endpoint of the Orders v2 API.

**Important:** Exercise caution when polling for order capture results using the [Show order details](/docs/api/orders/v2/#orders_get) endpoint. PayPal enforces rate limits on API requests.

#### Sample Request

#### **`Code`**

```javascript
curl -v -X GET https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer <Access-Token>"
```

#### Sample Response

#### **`Code`**

```javascript
{
  "id": "5O190127TN364715T",
  "intent": "CAPTURE",
  "status": "COMPLETED",
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "payment_source": {
    "pay_upon_invoice": {
      "birth_date": "1990-01-01",
      "name": {
        "given_name": "John",
        "surname": "Doe"
      },
      "email": "buyer@example.com",
      "phone": {
        "national_number": "6912345678",
        "country_code": "49"
      },
      "billing_address": {
        "address_line_1": "Schönhauser Allee 84",
        "admin_area_2": "Berlin",
        "postal_code": "10439",
        "country_code": "DE"
      },
      "payment_reference": "b8a1525dlYzu6Mn62umI",
      "deposit_bank_details": {
        "bic": "DEUTDEFFXXX",
        "bank_name": "Deutsche Bank",
        "iban": "DE89370400440532013000",
        "account_holder_name": "Paypal - Ratepay GmbH - Test Bank Account"
      }
    }
  },
  "purchase_units": [
    {
      "invoice_id": "MERCHANT_INVOICE_ID",
      "custom_id": "MERCHANT_CUSTOM_ID",
      "amount": {
        "currency_code": "EUR",
        "value": "100.00",
        "breakdown": {
          "item_total": {
            "currency_code": "EUR",
            "value": "81.00"
          },
          "tax_total": {
            "currency_code": "EUR",
            "value": "19.00"
          }
        }
      },
      "shipping": {
        "name": {
          "full_name": "John Doe"
        },
        "address": {
          "address_line_1": "Taunusanlage 12",
          "admin_area_2": "FRANKFURT AM MAIN",
          "postal_code": "60325",
          "country_code": "DE"
        }
      },
      "items": [
        {
          "name": "Air Jordan Shoe",
          "category": "PHYSICAL_GOODS",
          "unit_amount": {
            "currency_code": "EUR",
            "value": "100.00"
          },
          "tax": {
            "currency_code": "EUR",
            "value": "19.00"
          },
          "tax_rate": "19.00",
          "quantity": "1"
        }
      ],
      "payments": {
        "captures": [
          {
            "id": "826413372K501814R",
            "status": "COMPLETED",
            "amount": {
              "currency_code": "EUR",
              "value": "100.00"
            },
            "final_capture": true,
            "seller_protection": {
              "status": "NOT_ELIGIBLE"
            },
            "seller_receivable_breakdown": {
              "gross_amount": {
                "currency_code": "EUR",
                "value": "100.00"
              },
              "paypal_fee": {
                "currency_code": "EUR",
                "value": "3.00"
              },
              "net_amount": {
                "currency_code": "EUR",
                "value": "97.00"
              }
            },
            "invoice_id": "MERCHANT_INVOICE_ID",
            "custom_id": "MERCHANT_CUSTOM_ID",
            "links": [
              {
                "href": "https://api-m.paypal.com/v2/payments/captures/3C679366HH908993F",
                "rel": "self",
                "method": "GET"
              },
              {
                "href": "https://api-m.paypal.com/v2/checkout/orders/5O190127TN364715T",
                "rel": "up",
                "method": "GET"
              },
              {
                "href": "https://api-m.paypal.com/v2/payments/captures/3C679366HH908993F/refund",
                "rel": "refund",
                "method": "POST"
              }
            ],
            "create_time": "2021-03-19T08:16:01Z",
            "update_time": "2021-03-19T08:17:12Z"
          }
        ]
      }
    }
  ],
  "links": [
    {
      "href": "https://api-m.paypal.com/v2/checkout/orders/5O190127TN364715T",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```

### Step result

A successful request returns the HTTP 200 OK status code with a JSON response body that returns a COMPLETED status.

A successfully captured order has the following:

- The order status as COMPLETED , which means the order was captured successfully.
- A capture with COMPLETED status is included in the purchase_units[0].payments.captures[0] response parameter. The up HATEOAS link indicates the order associated with this capture.
- The payment reference is included in the payment_source.pay_upon_invoice.payment_reference response parameter. The buyer needs to enter this value in the reason for transfer (dt. Verwendungszweck) during the bank transfer.

## 4. Notify Buyer of success

Notify the buyer of the successful transaction offline and send the instructions to pay the invoice. Obtain these instructions on a per transaction basis from the Orders API [show order details](https:/docs/api/orders/v2/#orders_get) endpoint. The payment reference is included in the payment_source.pay_upon_invoice.payment_reference response parameter. The buyer must enter this value in the reason for transfer (dt. Verwendungszweck) during the bank transfer. The deposit bank information is included in the payment_source.pay_upon_invoice.deposit_bank_details response parameter.

### Sample Request

#### **`Code`**

```javascript
curl -v -X GET https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer <Access-Token>"
```

### Sample Response

#### **`Code`**

```javascript
{
  "id": "5O190127TN364715T",
  "intent": "CAPTURE",
  "status": "COMPLETED",
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "payment_source": {
    "pay_upon_invoice": {
      "birth_date": "1990-01-01",
      "name": {
        "given_name": "John",
        "surname": "Doe"
      },
      "email": "buyer@example.com",
      "phone": {
        "national_number": "6912345678",
        "country_code": "49"
      },
      "billing_address": {
        "address_line_1": "Schönhauser Allee 84",
        "admin_area_2": "Berlin",
        "postal_code": "10439",
        "country_code": "DE"
      },
      "payment_reference": "b8a1525dlYzu6Mn62umI",
      "deposit_bank_details": {
        "bic": "DEUTDEFFXXX",
        "bank_name": "Deutsche Bank",
        "iban": "DE89370400440532013000",
        "account_holder_name": "Paypal - Ratepay GmbH - Test Bank Account"
      }
    }
  },
  "purchase_units": [
    {
      "invoice_id": "MERCHANT_INVOICE_ID",
      "custom_id": "MERCHANT_CUSTOM_ID",
      "amount": {
        "currency_code": "EUR",
        "value": "100.00",
        "breakdown": {
          "item_total": {
            "currency_code": "EUR",
            "value": "81.00"
          },
          "tax_total": {
            "currency_code": "EUR",
            "value": "19.00"
          }
        }
      },
      "shipping": {
        "name": {
          "full_name": "John Doe"
        },
        "address": {
          "address_line_1": "Taunusanlage 12",
          "admin_area_2": "FRANKFURT AM MAIN",
          "postal_code": "60325",
          "country_code": "DE"
        }
      },
      "items": [
        {
          "name": "Air Jordan Shoe",
          "category": "PHYSICAL_GOODS",
          "unit_amount": {
            "currency_code": "EUR",
            "value": "100.00"
          },
          "tax": {
            "currency_code": "EUR",
            "value": "19.00"
          },
          "tax_rate": "19.00",
          "quantity": "1"
        }
      ],
      "payments": {
        "captures": [
          {
            "id": "826413372K501814R",
            "status": "COMPLETED",
            "amount": {
              "currency_code": "EUR",
              "value": "100.00"
            },
            "final_capture": true,
            "seller_protection": {
              "status": "NOT_ELIGIBLE"
            },
            "seller_receivable_breakdown": {
              "gross_amount": {
                "currency_code": "EUR",
                "value": "100.00"
              },
              "paypal_fee": {
                "currency_code": "EUR",
                "value": "3.00"
              },
              "net_amount": {
                "currency_code": "EUR",
                "value": "97.00"
              }
            },
            "invoice_id": "MERCHANT_INVOICE_ID",
            "custom_id": "MERCHANT_CUSTOM_ID",
            "links": [
              {
                "href": "https://api-m.paypal.com/v2/payments/captures/3C679366HH908993F",
                "rel": "self",
                "method": "GET"
              },
              {
                "href": "https://api-m.paypal.com/v2/checkout/orders/5O190127TN364715T",
                "rel": "up",
                "method": "GET"
              },
              {
                "href": "https://api-m.paypal.com/v2/payments/captures/3C679366HH908993F/refund",
                "rel": "refund",
                "method": "POST"
              }
            ],
            "create_time": "2021-03-19T08:16:01Z",
            "update_time": "2021-03-19T08:17:12Z"
          }
        ]
      }
    }
  ],
  "links": [
    {
      "href": "https://api-m.paypal.com/v2/checkout/orders/5O190127TN364715T",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```

### Step result

A successful request returns the HTTP 200 OK status code with a JSON response body that returns a COMPLETED status.

A successfully captured order has the following:

- The order status as COMPLETED , which means the order was captured successfully.
- A capture with COMPLETED status is present in the response parameter purchase_units[0].payments.captures[0] . The up HATEOAS link indicates the order associated with this capture.
- The deposit bank information is present in the payment_source.pay_upon_invoice.deposit_bank_details response parameter.

Send an invoice to the buyer and include the payment instructions as received on a per transaction basis pointing out that payment must be made to Ratepay.

## Display the appropriate error message to the buyer

If [Step 1](#1-offer-pay-upon-invoice-on-your-checkout-page) is unsuccessful, it returns the HTTP 422 UNPROCESSABLE_ENTITY status code with a JSON response body that contains an error code in the issue parameter.

### Sample request

#### **`Code`**

```javascript
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <Access-Token>" \
-H "PayPal-Request-Id: 7b92603e-77ed-4896-8e78-5dea2050476a" \
-d '{
  "intent": "CAPTURE",
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "purchase_units": [
    {
      "amount": {
        "currency_code": "EUR",
        "value": "100.00",
        "breakdown": {
          "item_total": {
            "currency_code": "EUR",
            "value": "81.00"
          },
          "tax_total": {
            "currency_code": "EUR",
            "value": "19.00"
          }
        }
      },
      "shipping": {
        "name": {
          "full_name": "John Doe"
        },
        "address": {
          "address_line_1": "Taunusanlage 12",
          "admin_area_2": "FRANKFURT AM MAIN",
          "postal_code": "60325",
          "country_code": "DE"
        }
      },
      "items": [
        {
          "name": "Air Jordan Shoe",
          "category": "PHYSICAL_GOODS",
          "unit_amount": {
            "currency_code": "EUR",
            "value": "81.00"
          },
          "tax": {
            "currency_code": "EUR",
            "value": "19.00"
          },
          "tax_rate": "19.00",
          "quantity": "1"
        }
      ],
      "invoice_id": "MERCHANT_INVOICE_ID",
      "custom_id": "MERCHANT_CUSTOM_ID"
    }
  ],
  "payment_source": {
    "pay_upon_invoice": {
      "name": {
        "given_name": "John",
        "surname": "Doe"
      },
      "email": "payment_source_info_cannot_be_verified@example.com",
      "birth_date": "1990-01-01",
      "phone": {
        "national_number": "6912345678",
        "country_code": "49"
      },
      "billing_address": {
        "address_line_1": "Schönhauser Allee 84",
        "admin_area_2": "Berlin",
        "postal_code": "10439",
        "country_code": "DE"
      },
      "experience_context": {
        "locale": "en-DE",
        "brand_name": "EXAMPLE INC",
        "logo_url": "https://example.com/logoUrl.svg",
        "customer_service_instructions": [
          "Customer service phone is +49 6912345678."
        ]
      }
    }
  }
}'
```

### Step result

An unsuccessful request results in the following:

- A return status code of HTTP 422 Unprocessable Entity .
- A JSON response body that contains an error code in the issue parameter and the error description in the description parameter.

#### Sample response

#### **`Code`**

```javascript
{
  "name": "UNPROCESSABLE_ENTITY",
  "details": [
    {
      "issue": "PAYMENT_SOURCE_INFO_CANNOT_BE_VERIFIED",
      "description": "The combination of the payment_source name, billing address, shipping name and shipping address could not be verified. Please correct this information and try again by creating a new order."
    }
  ],
  "message": "The requested action could not be performed, semantically incorrect, or failed business validation.",
  "debug_id": "82c4e721e5c58",
  "links": [
    {
      "href": "https://developer.paypal.com/api/orders/v2/#error-PAYMENT_SOURCE_INFO_CANNOT_BE_VERIFIED",
      "rel": "information_link",
      "method": "GET"
    }
  ]
}
```

#### Duplicate orders

When a duplicate order is detected, the Orders API declines the order and returns the following error code and description:

Error code: PUI_DUPLICATE_ORDER Error description: A Pay Upon Invoice (Rechnungskauf) order with the same payload has already been successfully processed in the last few seconds. To process a new order, please try again in a few seconds.

### Error codes and error messages

Ratepay mandates that you display these error messages to the buyer for the following error codes:

| Error code                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Error message (English)                                                                                                                                                                                                                                                                                                                  | Error message (German)                                                                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [](#payment_source_info_cannot_be_verifiedthe-combination-of-your-name-and-address-could-not-be-validated.-please-correct-your-data-and-try-again.-you-can-find-further-information-in-the-ratepay-data-privacy-statement-or-you-can-contact-ratepay-using-this-contact-form.die-kombination-aus-ihrem-namen-und-ihrer-anschrift-konnte-nicht-validiert-werden.-bitte-korrigieren-sie-ihre-daten-und-versuchen-sie-es-erneut.-weitere-informationen-finden-sie-in-den-ratepay-datenschutzbestimmungen-oder-nutzen-sie-das-ratepay-kontaktformular.)PAYMENT_SOURCE_INFO_CANNOT_BE_VERIFIED | The combination of your name and address could not be validated. Please correct your data and try again. You can find further information in the[Ratepay Data Privacy Statement](https://www.ratepay.com/en/ratepay-data-privacy-statement/)or you can contact Ratepay using this[contact form](https://www.ratepay.com/en/contact/).    | Die Kombination aus Ihrem Namen und Ihrer Anschrift konnte nicht validiert werden. Bitte korrigieren Sie Ihre Daten und versuchen Sie es erneut. Weitere Informationen finden Sie in den Ratepay[Datenschutzbestimmungen](https://www.ratepay.com/legal-payment-dataprivacy/?lang=de)oder nutzen Sie das Ratepay[Kontaktformular](https://www.ratepay.com/kontakt/). |
| [](#payment_source_declined_by_processorit-is-not-possible-to-use-the-selected-payment-method.-this-decision-is-based-on-automated-data-processing.-you-can-find-further-information-in-the-ratepay-data-privacy-statement-or-you-can-contact-ratepay-using-this-contact-form.die-gewählte-zahlungsart-kann-nicht-genutzt-werden.-diese-entscheidung-basiert-auf-einem-automatisierten-datenverarbeitungsverfahren.-weitere-informationen-finden-sie-in-den-ratepay-datenschutzbestimmungen-oder-nutzen-sie-das-ratepay-kontaktformular.)PAYMENT_SOURCE_DECLINED_BY_PROCESSOR             | It is not possible to use the selected payment method. This decision is based on automated data processing. You can find further information in the[Ratepay Data Privacy Statement](https://www.ratepay.com/en/ratepay-data-privacy-statement/)or you can contact Ratepay using this[contact form](https://www.ratepay.com/en/contact/). | Die gewählte Zahlungsart kann nicht genutzt werden. Diese Entscheidung basiert auf einem automatisierten Datenverarbeitungsverfahren. Weitere Informationen finden Sie in den Ratepay[Datenschutzbestimmungen](https://www.ratepay.com/legal-payment-dataprivacy/?lang=de)oder nutzen Sie das Ratepay[Kontaktformular](https://www.ratepay.com/kontakt/).            |

## Test your integration

Use these buyer email addresses to simulate the failure scenarios in the PayPal sandbox environment.

| Error code                                                                                                                          | Buyer email                                        |
| ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| [](#payment_source_info_cannot_be_verifiedpayment_source_info_cannot_be_verified@example.com)PAYMENT_SOURCE_INFO_CANNOT_BE_VERIFIED | payment_source_info_cannot_be_verified@example.com |
| [](#payment_source_declined_by_processorpayment_source_declined_by_processor@example.com)PAYMENT_SOURCE_DECLINED_BY_PROCESSOR       | payment_source_declined_by_processor@example.com   |
| [](#payment_source_cannot_be_usedpayment_source_cannot_be_used@example.com)PAYMENT_SOURCE_CANNOT_BE_USED                            | payment_source_cannot_be_used@example.com          |
| [](#billing_address_invalidbilling_address_invalid@example.com)BILLING_ADDRESS_INVALID                                              | billing_address_invalid@example.com                |
| [](#shipping_address_invalidshipping_address_invalid@example.com)SHIPPING_ADDRESS_INVALID                                           | shipping_address_invalid@example.com               |

Any buyer email not listed in the table will simulate a successful scenario on PayPal sandbox environment.
