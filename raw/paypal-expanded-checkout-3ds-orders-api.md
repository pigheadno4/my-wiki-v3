<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/api/ -->
<!-- Fetched: 2026-04-13 -->

Online / Checkout / Expanded / Customize / 3D Secure / 3D Secure: Orders API

# 3D Secure: Orders API

Enable 3D Secure for advanced credit and debit cards. This integration uses Orders API.

> **Info:** PayPal handles 3D Secure authentication for standard payment integrations. No changes are required for standard integrations.

## Know before you code

### If you are based in Europe, you may be subject to PSD2

- Include 3D Secure as part of your integration.
- Pass the cardholder's billing address as part of the transaction processing.

Use the following code to request either `SCA_ALWAYS` or `SCA_WHEN_REQUIRED` as a verification attribute for the `card` object.

- `SCA_ALWAYS` triggers 3D Secure for every transaction, regardless of SCA requirements.
- `SCA_WHEN_REQUIRED` returns a 3D Secure contingency when it is a mandate in the region where you operate. This is the **default** when neither parameter is explicitly passed.

### Include a contingency for 3D Secure

```json
{
  "method": "POST",
  "path": "v2/checkout/orders/5O190127TN364715T/authorize",
  "headers": {
    "PayPal-Request-Id": "7b92603e-77ed-4896-8e78-5dea2050476a",
    "Authorization": "Bearer <Access-Token>"
  },
  "body": {
    "payment_source": {
      "card": {
        "number": "4111111111111111",
        "expiry": "2010-02",
        "name": "John Doe",
        "billing_address": {
          "address_line_1": "2211 N First Street",
          "address_line_2": "17.3.160",
          "admin_area_1": "CA",
          "admin_area_2": "San Jose",
          "postal_code": "95131",
          "country_code": "US"
        },
        "attributes": {
          "verification": {
            "method": "SCA_WHEN_REQUIRED"
          }
        }
      }
    }
  }
}
```

### Step result

| Request type | Result |
| ------------ | ------ |
| Single-step payment request | HTTP 201 Created |
| Multi-step payment request | HTTP 422 Unprocessable Entity |
| Confirm order request | HTTP 200 OK |

## Launch authentication flow with HATEOAS link

The merchant needs to redirect the payer back to PayPal to complete 3D Secure authentication.

To trigger the authentication:
1. Redirect the buyer to the `"rel": "payer-action"` HATEOAS link returned as part of the response before authorizing or capturing the order.
2. Append `redirect_uri` to the payer-action URL so that PayPal returns the payer to the merchant's checkout page after 3D Secure authentication.

### Sample payer-action URL

```
https://example.com/webapp/myshop?action=verify&flow=3ds&cart_id=ORDER-ID&redirect_uri=MERCHANT-LANDING-PAGE
```

- The issuing bank verifies authentication.
- Device data is collected, and JavaScript is posted directly to the issuing bank.

### 3DS request (check authentication result)

```bash
GET v2/checkout/orders/5O190127TN364715T?fields=payment_source
Authorization: Bearer <Access-Token>
```

### 3DS response

```json
{
  "payment_source": {
    "card": {
      "type": "CREDIT",
      "brand": "VISA",
      "last_digits": "1111",
      "authentication_result": {
        "liability_shift": "POSSIBLE",
        "three_d_secure": {
          "enrollment_status": "Y",
          "authentication_status": "Y"
        }
      }
    }
  }
}
```

## Proceed with the transaction

### Single-step API request

After the 3D Secure contingency is thrown during the **create order** response, and the contingency is resolved by the buyer, invoke the authorize order and capture order endpoints with an **empty payload** to complete the transaction.

### Multi-step API request

After the 3D Secure contingency is thrown during the **authorize order** or **capture order** response, and the contingency is resolved by the buyer, invoke the authorize order and capture order endpoints again with an **empty payload** to complete the transaction.

## See also

- **Response parameters** — Learn more about handling 3D Secure responses.
- **Test scenarios** — Simulate 3D Secure scenarios and responses.
