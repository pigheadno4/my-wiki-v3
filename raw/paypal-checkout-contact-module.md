---
title: Contact module
slug: /docs/checkout/standard/customize/contact-module/
createTime: '2025-01-03T21:41:51.688Z'
updateTime: '2025-04-07T16:18:56.019Z'
---

# Contact module

## Overview

The Contact Module helps buyers view and modify the email and phone number shared with merchants for a given order. It offers greater flexibility and control to buyers, particularly for gift orders where buyers need to specify alternative contact details.

### Key features

- **Merchant-controlled contact display**: Merchants choose if shoppers can see and edit their contact information during PayPal checkout.
- **Add contact information**: Buyers can add new email addresses and phone numbers during checkout.
- **Select existing contact information**: Buyers can select from a list of previously added email addresses and phone numbers.
- **Validation**: Input validation ensures the provided email addresses and phone numbers follow appropriate formats.
- **Merchant-provided data**: If the merchant supplies contact information, the information is displayed during the transaction. The merchant can decide whether the information is editable or not.
- **Profile contact integration**: Shows the primary email and phone number from the buyer's PayPal account by default.
- **Localized support**: Buyers from different countries can add and validate contact information according to regional standards.

### Buyer benefits

- **Personalization**: Allows buyers to customize contact details for each transaction.
- **Convenience**: Buyers don't need to update contact information outside the payment flow.

### Merchant benefits

- **Order fulfillment**: Provides merchants with precise and complete contact details for seamless communication.
- **Accuracy**: Ensures merchants receive accurate and current contact information.

## Availability

The Contact Module is currently **available in the US only**.

## Contact preferences

Merchants can set a contact preference to control what contact information buyers see when reviewing PayPal checkout.

PayPal supports three contact preference options:

- `NO_CONTACT_INFO`: **Default**. Buyers do not see any contact information during checkout.
- `UPDATE_CONTACT_INFO`: Buyers can see and edit their contact information.
- `RETAIN_CONTACT_INFO`: Buyers can see their contact information, but can't edit them.

## Manage buyer contact information

The Orders API manages contact information as part of the `purchase_units[].shipping` object in the `email_address` field and the `phone_number` object when an order is created.

Use buyer contact information from PayPal or the merchant site.

- **Upstream presentment**: Buyers begin PayPal checkout by selecting the button from the cart or product page. Buyers don't enter information on the merchant site.
- **Checkout presentment**: Buyers select the PayPal button when checking out on the merchant site after entering information. Merchants can pass buyer information to pre-fill fields at PayPal checkout.

## Hide contact information (NO_CONTACT_INFO)

This setting is default.

If a merchant prefers not to display contact information to buyers during checkout, the merchant can use `NO_CONTACT_INFO`, or omit `payment_source.paypal.experience_context.contact_preference`.

Even if the merchant provides contact information, PayPal will not display it to buyers if `NO_CONTACT_INFO` is enabled.

## Allow editing (UPDATE_CONTACT_INFO)

If a merchant wants to show editable contact information to buyers, the merchant uses `UPDATE_CONTACT_INFO`. After a buyer updates their details, the merchant sees the latest email and phone number. The merchant should use the latest information to communicate with their buyers.

`UPDATE_CONTACT_INFO` allows the buyer to edit both their phone number and email in PayPal. Individual edit preferences are not supported.

In the collapsed view, the Contact Module shows the primary email and phone number from the buyer's profile. If the merchant does not provide information, the PayPal profile information is used by default.

When expanded, the Contact Module displays:

- A dropdown to select from up to 5 previously used contact entries displayed in order of most recent use.
- Options to add new email addresses or phone numbers.
- Inline validation for newly added contact information.

### Buyer adds email

![Buyer flow for adding email during PayPal checkout.](assets/paypal-contact-module-add-email.png)

### Buyer selects phone number

![Buyer flow for selecting phone number during PayPal checkout.](assets/paypal-contact-module-select-phone.png)

### Pass UPDATE_CONTACT_INFO

In your call to the Orders API, set `payment_source.paypal.experience_context.contact_preference` to `UPDATE_CONTACT_INFO`.

If you pass information in `purchase_units[].shipping.email_address` and `purchase_units[].shipping.phone_number`, you see these values in the create order response and the get order API call after the buyer approves the transaction. This information is displayed and editable to the buyer during PayPal checkout.

#### Create order with UPDATE_CONTACT_INFO

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H 'Content-Type: application/json' \
-H 'PayPal-Request-Id: REQUEST-ID' \
-H 'Authorization: Bearer ACCESS-TOKEN' \
-d '{
  "intent": "CAPTURE",
  "payment_source": {
    "paypal": {
      "experience_context": {
        "shipping_preference": "SET_PROVIDED_ADDRESS",
        "contact_preference": "UPDATE_CONTACT_INFO",
        "user_action": "PAY_NOW",
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
      }
    }
  },
  "purchase_units": [
    {
      "amount": {
        "currency_code": "USD",
        "value": "64.00"
      },
      "shipping": {
        "name": { "full_name": "Firstname Lastname" },
        "email_address": "customer@example.com",
        "phone_number": {
          "country_code": "1",
          "national_number": "5555555555"
        },
        "address": {
          "address_line_1": "123 Main St.",
          "admin_area_2": "Anytown",
          "admin_area_1": "CA",
          "postal_code": "12345",
          "country_code": "US"
        }
      }
    }
  ]
}'
```

#### Response

```json
{
  "id": "order-id",
  "intent": "CAPTURE",
  "status": "PAYER_ACTION_REQUIRED",
  "purchase_units": [{
    "amount": { "currency_code": "USD", "value": "64.00" },
    "payee": { "email_address": "merchant@example.com", "merchant_id": "CR87QHB7JKKK" },
    "shipping": {
      "name": { "full_name": "Firstname Lastname" },
      "email_address": "customer@example.com",
      "phone_number": { "country_code": "1", "national_number": "5555555555" },
      "address": {
        "address_line_1": "123 Main St.",
        "admin_area_2": "Anytown",
        "admin_area_1": "CA",
        "postal_code": "12345",
        "country_code": "US"
      }
    }
  }],
  "create_time": "2024-01-31T02:52:12Z",
  "links": [
    { "href": "https://www.api-m.paypal.com/v2/checkout/orders/order-id", "rel": "self", "method": "GET" },
    { "href": "https://www.paypal.com/checkoutnow?token=order-id", "rel": "payer-action", "method": "GET" }
  ]
}
```

### Retrieve buyer's latest contact information

When buyers edit their contact details and check out with PayPal, call the Orders API to retrieve the latest contact information.

#### Show order details

```curl
curl -v -X GET https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER-ID \
-H 'Authorization: Bearer ACCESS-TOKEN'
```

#### Response

```json
{
  "id": "ORDER-ID",
  "intent": "CAPTURE",
  "status": "APPROVED",
  "payment_source": {
    "paypal": {
      "email_address": "payer@example.com",
      "name": { "given_name": "Firstname", "surname": "Lastname" },
      "address": {
        "address_line_1": "123 Main St.",
        "admin_area_2": "Anytown",
        "admin_area_1": "CA",
        "postal_code": "12345",
        "country_code": "US"
      }
    }
  },
  "purchase_units": [{
    "reference_id": "default",
    "amount": { "currency_code": "USD", "value": "64.00" },
    "payee": { "email_address": "merchant@example.com", "merchant_id": "CR87QHB7JKKK" },
    "shipping": {
      "name": { "full_name": "Firstname Lastname" },
      "email_address": "customer_friend@example.com",
      "phone_number": { "country_code": "1", "national_number": "2222222222" },
      "address": {
        "address_line_1": "123 Main St.",
        "admin_area_2": "Anytown",
        "admin_area_1": "CA",
        "postal_code": "12345",
        "country_code": "US"
      }
    }
  }]
}
```

## Read-only contact display (RETAIN_CONTACT_INFO)

If a merchant wants to show contact information to buyers without allowing them to edit it, merchants use the `RETAIN_CONTACT_INFO` setting.

The merchant collects the buyer's email address and phone number on their website and includes them in the create order call using `purchase_units[].shipping.email_address` and `purchase_units[].shipping.phone_number`.

Set `payment_source.paypal.experience_context.contact_preference` to `RETAIN_CONTACT_INFO` in your Orders API request.

- If the merchant provides only one contact field (email or phone), PayPal assumes only that method is required to communicate with the buyer, and displays the one value.
- If `RETAIN_CONTACT_INFO` is set without passing any contact details, PayPal defaults to `NO_CONTACT_INFO` and hides all contact information from the buyer.

Buyers can view the contact information provided but cannot edit it. Only the values passed in the Orders API call are displayed.

#### Create order with RETAIN_CONTACT_INFO

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H 'Content-Type: application/json' \
-H 'PayPal-Request-Id: REQUEST-ID' \
-H 'Authorization: Bearer ACCESS-TOKEN' \
-d '{
  "intent": "CAPTURE",
  "payment_source": {
    "paypal": {
      "experience_context": {
        "shipping_preference": "SET_PROVIDED_ADDRESS",
        "contact_preference": "RETAIN_CONTACT_INFO",
        "user_action": "PAY_NOW",
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
      }
    }
  },
  "purchase_units": [
    {
      "amount": {
        "currency_code": "USD",
        "value": "64.00"
      },
      "shipping": {
        "name": { "full_name": "Firstname Lastname" },
        "email_address": "payer@example.com",
        "phone_number": {
          "country_code": "1",
          "national_number": "5555555555"
        },
        "type": "SHIPPING",
        "address": {
          "address_line_1": "123 Main St.",
          "admin_area_2": "Anytown",
          "admin_area_1": "CA",
          "postal_code": "12345",
          "country_code": "US"
        }
      }
    }
  ]
}'
```

#### Response

```json
{
  "id": "order-id",
  "intent": "CAPTURE",
  "status": "PAYER_ACTION_REQUIRED",
  "purchase_units": [{
    "amount": { "currency_code": "USD", "value": "64.00" },
    "payee": { "email_address": "merchant@example.com", "merchant_id": "CR87QHB7JKKK" },
    "shipping": {
      "name": { "full_name": "Firstname Lastname" },
      "email_address": "customer@example.com",
      "phone_number": { "country_code": "1", "national_number": "5555555555" },
      "address": {
        "address_line_1": "123 Main St.",
        "admin_area_2": "Anytown",
        "admin_area_1": "CA",
        "postal_code": "12345",
        "country_code": "US"
      }
    }
  }],
  "create_time": "2024-01-31T02:52:12Z",
  "links": [
    { "href": "https://www.api-m.paypal.com/v2/checkout/orders/order-id", "rel": "self", "method": "GET" },
    { "href": "https://www.paypal.com/checkoutnow?token=order-id", "rel": "payer-action", "method": "GET" }
  ]
}
```
