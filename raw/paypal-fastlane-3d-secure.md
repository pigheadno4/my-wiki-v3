<!-- Source URL: https://developer.paypal.com/docs/checkout/fastlane/3d-secure/ -->
<!-- Fetched: 2026-04-13 -->

---
title: 3D Secure for Fastlane
slug: /docs/checkout/fastlane/3d-secure/
createTime: '2025-11-20T13:53:57.053Z'
updateTime: '2025-12-04T16:27:50.237Z'
---


# 3D Secure for Fastlane

Use Fastlane's 3D Secure (3DS) to authenticate cardholders through card issuers. 3DS reduces fraud for supported cards and improves transaction performance. For more details, see [3D Secure authentication](https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/) .

Fastlane provides two options for performing 3DS:

- **Orders v2 API** : Run 3DS one time for each transaction when you integrate 3DS using the [3DS Orders v2 API](https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/api/) . If the customer closes the modal or fails authentication, the [Orders v2 API](https://developer.paypal.com/docs/api/orders/v2/) cannot issue a new challenge. Process the payment, request a new card, or complete another 3DS verification with the JavaScript SDK 3DS component.
- **PayPal JavaScript SDK 3DS component** : Use this component to complete 3DS verification. If you do not receive results, repeat 3DS verification, request a different card, or use Orders v2 to process the transaction.

 

## How it works
Follow these steps to make a 3DS call.

- Generate an access token.
- Render the checkout page to collect payment information.
- Verify the credit card amount.
- Authenticate the customer if required by the issuer or local regulations.

If authentication succeeds or is not required, process the payment with the returned payment token or save the payment method for future transactions.


Use PayPal's JavaScript SDK or perform a server-side call with the [Orders v2 API](https://developer.paypal.com/docs/api/orders/v2/) to support 3DS.

 

## Generate access token
Generate an access token to authenticatePayPal API requests.

 

### Request

#### **`Generate access token, request`**
```curl
curl -s -X POST "https://api-m.sandbox.paypal.com/v1/oauth2/token" \
 -u CLIENT_ID:CLIENT_SECRET \
 -H "Content-Type: application/x-www-form-urlencoded" \
 -d "grant_type=client_credentials" \
 -d "response_type=client_token" \
 -d "intent=sdk_init" \
 -d "domains[]=example.com,example2.com"
```
Modify the code

- Get your client ID and secret from your [Developer Dashboard](https://developer.paypal.com/dashboard/) .
- Copy the sample code. Replace CLIENT_ID with your client ID.
- Replace CLIENT_SECRET with your client secret.
- Replace example.com,example2.com with your domains.
- Provide the root domain name only.



**Note:** Do not use subdomains, wildcards, or protocols.




### Response

#### **`Generate access token, Response, /docs/checkout/fastlane/3d-secure/`**
```javascript
{
  "scope": "https://uri.paypal.com/services/invoicing https://uri.paypal.com/services/disputes/read-buyer https://uri.paypal.com/services/payments/realtimepayment https://uri.paypal.com/services/disputes/update-seller https://uri.paypal.com/services/payments/payment/authcapture openid https://uri.paypal.com/services/disputes/read-seller https://uri.paypal.com/services/payments/refund https://api-m.paypal.com/v1/vault/credit-card https://api-m.paypal.com/v1/payments/.* https://uri.paypal.com/payments/payouts https://api-m.paypal.com/v1/vault/credit-card/.* https://uri.paypal.com/services/subscriptions https://uri.paypal.com/services/applications/webhooks",
  "access_token": "<access_token>",
  "token_type": "Bearer",
  "app_id": "<APP-ID>",
  "expires_in": 31668,
  "nonce": "<NONCE_FROM_FASTLANE_INTEGRATION>"
}
```

Add the SDK script tag.


#### **`Initialize PayPal JavaScript SDK and Fastlane, script tag`**
```javascript
<script>
  src="https://www.paypal.com/sdk/js?client-id=<CLIENT_ID>>&components=buttons,fastlane,three-domain-secure"
  data-sdk-client-token="<SDK_CLIENT_TOKEN>"
</script>
```

Load the Fastlane component.


#### **`Load the  Fastlane component`**
```javascript
// instantiates the Fastlane module
const fastlane = await window.paypal.Fastlane({ }); 
// Convenience parameters for calling later on
const { identity,
  profile,
  FastlaneCardComponent,
  FastlaneWatermarkComponent,
 } = fastlane;
 fastlane.setLocale('en_us'); // Sets customer's country and language
```

Initialize 3DS after receiving the payment token and order amount.


#### **`Check 3DS eligibility`**
```javascript
// Check eligibility
const threeDomainSecureComponent = window.paypal.ThreeDomainSecureClient;
```

After you receive a payment token and the order amount, verify your eligibility.


#### **`Check 3DS eligibility, after you receive a payment token`**
```javascript
const threeDomainSecureParameters = {
  amount: '12.00',
  currency: 'USD',
  nonce: NONCE_FROM_FASTLANE_INTEGRATION,
  threeDSRequested: SCA_ALWAYS | SCA_WHEN_REQUIRED in the eligibility API request, otherwise defaults to SCA_WHEN_REQUIRED
  transactionContext: {
        experience_context: {
          brand_name: "YourBrandName",
          locale: "en-US",
          return_url: "https://example.com/returnUrl",
          cancel_url: "https://example.com/cancelUrl",
        },
        // Optional
        transaction_context: {
          soft_descriptor: "Card verification hold",
        },
      },
};
const isThreeDomainSecureEligible = await threeDomainSecureComponent.isEligible(
  threeDomainSecureParameters,
);
```

When the customer selects the submit button, trigger the authentication step and handle the result.


#### **`Customer attempts 3DS authentication`**
```javascript
const submitButton = document.getElementById("submit-button");
submitButton.addEventListener("click", async () => {
  if (isThreeDomainSecureEligible) {
    const {
      liabilityShift, // "no", "unknown", "possible"
      authenticationState, // "success", "cancelled", "errored"
      nonce, //Enriched nonce or the original nonce
    } = await threeDomainSecureComponent.show();
    if (authenticationState === "success") {
      // Check the liability shift and decide on continuing the transaction
    } else {
      // Cancelled or errored, merchant can choose to send the customer back to 3DS or submit a payment and or vault the payment token.
    }
  }
})
```
 

### Client-side response parameters
The JavaScript SDK returns the following parameters after authentication.

| Parameter | Value | Description | Action |
| liabilityShift | POSSIBLE | Liability might shift to issuer | Continue with authorization |
| liabilityShift | NO | Liability stays with merchant | Do not continue with authorization |
| liabilityShift | UNKNOWN | Authentication system unavailable | Do not continue, request cardholder retry |
| authenticationState | success | Customer successfully authenticated | No action needed |
| authenticationState | cancelled | Customer cancelled the authentication | No action needed |
| authenticationState | errored | Error occurred during authentication | No action needed |

Process the payment using the [Orders v2 API](https://developer.paypal.com/docs/api/orders/v2/) to validate the endrollmentStatus of the user.


After Fastlane generates a payment token and the customer places the order, call the [Orders v2 API](https://developer.paypal.com/docs/api/orders/v2/) to check 3DS eligibility.

Use the returned URL to redirect the customer for authentication. Use the following API call for single-step 3DS verification.


#### **`3DS with Orders v2 API`**
```curl
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders' \
 -H 'PayPal-Request-Id: UNIQUE_ID' \
 -H 'Authorization: Bearer PAYPAL_ACCESS_TOKEN' \
 -H 'Content-Type: application/json' \
 -H 'PayPal-Client-Metadata-Id: <CM_ID>' \
 -d '{
  "intent": "CAPTURE",
  "payment_source": {
    "card": {
      "single_use_token": "1h371660pr490622k", //paymentToken from the client
      "attributes": {
        "verification": {
          "method": "SCA_WHEN_REQUIRED"
        }
      }
    }
  },
  "experience_context": {
    "brand_name": "YourBrandName",
    "locale": "en-US",
    "return_url": "https://example.com/returnUrl",
    "cancel_url": "https://example.com/cancelUrl"
    },
    "transaction_context": {
      "soft_descriptor": "Card verification hold"
    },
  "purchase_units": [
    {
      "amount": {
        "currency_code": "USD",
        "value": "50.00",
        "breakdown": {
          "item_total": {
            "currency_code": "USD",
            "value": "40.00"
          },
          "shipping": {
            "currency_code": "USD",
            "value": "10.00"
          }
        }
      },
      "items": [
        {
          "name": "Coffee",
          "description": "1 lb Kona Island Beans",
          "sku": "sku03",
          "unit_amount": {
            "currency_code": "USD",
            "value": "40.00"
          },
          "quantity": "1",
          "category": "PHYSICAL_GOODS",
          "image_url": "https://example.com/static/images/items/1/kona_coffee_beans.jpg",
          "url": "https://example.com/items/1/kona_coffee_beans",
          "upc": {
            "type": "UPC-A",
            "code": "987654321015"
          }
        }
      ],
      "shipping": {
        "type": "SHIPPING",
        "name": {
          "full_name": "<FULL_NAME>"
        },
        "address": {
          "address_line_1": "123 Main St.",
          "admin_area_2": "Anytown",
          "admin_area_1": "CA", //must be sent in 2-letter format
          "postal_code": "12345",
          "country_code": "US"
        },
        "phone_number": {
          "country_code": "1",
          "national_number": "5555555555"
        }
      }
    }
  ]
}'
```
 

## Redirect customer for authentication
Redirect the buyer to the rel: payer-action HATEOAS link before authorizing or capturing the order. Add redirect_url as a query parameter, so PayPal returns the payer to your checkout page after authentication. The following is a sample URL: https://example.com/webapp/myshop?action=verify&flow=3ds&cart_id=ORDER-ID&redirect_uri=MERCHANT-LANDING-PAGE .


### Verify 3DS status
After the customer returns, check the verification status of the order by passing the order ID in a GET call to /v2/checkout/orders/{id} . A successful call returns an HTTP 200 response with the following content.


#### **`Request`**
```curl
curl -v -X GET https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER_ID \
-H 'Authorization: Bearer Bearer <Access-Token>'
```


#### **`Response`**
```javascript
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


## Server-side response parameters 
When using the [Orders v2 API](https://developer.paypal.com/docs/api/orders/v2/) , you receive comprehensive 3DS parameters on the server side.

 

## LiabilityShift
| Parameter | Value | Description | Action |
| LiabilityShift | POSSIBLE | Liability may shift to the issuer | Continue with authorization |
| LiabilityShift | NO | Liability stays with the merchant | Do not continue with authorization |
| LiabilityShift | UNKNOWN | Authentication system unavailable | Request cardholder retry |

 

## EnrollmentStatus
| Parameter | Value | Description | Action |
| EnrollmentStatus | Y | Card and bank ready for 3DS | Proceed with authentication |
| EnrollmentStatus | N | Not ready for 3DS | Do not proceed with authentication |
| EnrollmentStatus | U | System unavailable | Request cardholder retry |
| EnrollmentStatus | B | System bypassed authentication | Proceed with order |

 

## Authentication_Status
| Parameter | Value | Description | Action |
| Authentication_Status | Y | Successful authentication | No action needed |
| Authentication_Status | N | Failed authentication | No action needed |
| Authentication_Status | R | Rejected authentication | No action needed |
| Authentication_Status | A | Attempted authentication | No action needed |
| Authentication_Status | U | Unable to complete | No action needed |
| Authentication_Status | C | Challenge required | No action needed |

 

### Parameter availability
The [Orders v2 API](https://developer.paypal.com/docs/api/orders/v2/) provides all three parameters on the server side, LiabilityShift , EnrollmentStatus , and Authentication_Status . The JavaScript SDK provides only liabilityShift and authenticationState . It does not provide EnrollmentStatus .

| Parameter | Orders v2 API | JavaScript SDK |
| liabilityShift | Yes | Yes |
| enrollmentStatus | Yes | No |
| authenticationState | Yes | Yes |

 

## Complete the transaction
After 3DS authentication, you can complete the transaction using one of two methods: processing the payment or saving the payment method.

 

### Process payment
You can capture the payment using a single-step or multi-step API request.

- In a single-step flow, after the 3DS contingency is resolved during the [create order](https://developer.paypal.com/docs/api/orders/v2/#orders_create) response, call the [authorize order](https://developer.paypal.com/docs/api/orders/v2/#orders_authorize) and [capture order](https://developer.paypal.com/docs/api/orders/v2/#orders_capture) endpoints with empty payloads.
- In a multi-step flow, if the 3DS contingency occurs during an authorize order or capture order request, resolve the contingency, then call those endpoints again with empty payloads.

 

### Save payment method
To save the customer's payment method for future use after 3DS authentication, use the [Payment Method Tokens v3 API](https://developer.paypal.com/docs/api/payment-tokens/v3/) .

- To process the current payment and vault the payment method for future transactions, use the single payment with vault option.
- To save the payment method without processing an immediate payment, use the vault-only option.


After successful 3DS authentication, capture the authorized payment using the Orders v2 API [capture endpoint](https://developer.paypal.com/docs/api/orders/v2/#orders_capture) .


#### **`Capture request (Server-side)`**
```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/{order_id}/capture \
 -H 'Authorization: Bearer PAYPAL_ACCESS_TOKEN' \
 -H 'Content-Type: application/json' \
 -H 'PayPal-Request-Id: UNIQUE_REQUEST_ID'
```


#### **`Capture response`**
```javascript
{
  "id": "5O190127TN364715T",
  "status": "COMPLETED",
  "purchase_units": [{
    "payments": {
      "captures": [{
        "id": "3C679366HH908993F",
        "status": "COMPLETED",
        "amount": {
          "currency_code": "USD",
          "value": "100.00"
        },
        "seller_protection": {
          "status": "ELIGIBLE",
          "dispute_categories": [
            "ITEM_NOT_RECEIVED",
            "UNAUTHORIZED_TRANSACTION"
          ]
        },
        "final_capture": true,
        "disbursement_mode": "INSTANT",
        "create_time": "2018-04-01T21:20:49Z"
      }]
    }
  }]
}
```
 

### Handle capture status
Check the capture status in the response to determine next steps.

| Status | Description | Action |
| COMPLETED | Payment successfully captured | Fulfill the order and provide goods or services |
| DECLINED | Payment declined by issue | Notify the customer to use a different payment method |
| PENDING | Payment under review | Do not ship until the status isCOMPLETED |
| FAILED | Capture failed | Review the error details and retry if appropriate |

 

Ensure all fulfillment or follow-up actions align with the current status of the payment capture response from the [Orders v2 API](https://developer.paypal.com/docs/api/orders/v2/) .


The following code samples demonstrate how to initiate payment requests and manage payment methods using the [Orders v2 API](https://developer.paypal.com/docs/api/orders/v2/) and [Payment Method Tokens API](https://developer.paypal.com/docs/api/payment-tokens/v3/) .


#### **`Payment`**
```curl
curl -v -k -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
 -H 'PayPal-Request-Id: UNIQUE_ID' \
 -H 'Authorization: Bearer PAYPAL_ACCESS_TOKEN' \
 -H 'Content-Type: application/json' \
 -H 'PayPal-Client-Metadata-Id: YOUR_CMID' \
 -d '{
  "intent": "CAPTURE",
  "payment_source": {
    "card": {
      "single_use_token": "1h371660pr490622k" // Payment token from the client
    }
  },
  "purchase_units": [
    {
      "amount": {
        "currency_code": "USD",
        "value": "50.00",
        "breakdown": {
          "item_total": {
            "currency_code": "USD",
            "value": "40.00"
          },
          "shipping": {
            "currency_code": "USD",
            "value": "10.00"
          }
        }
      },
      "items": [
        {
          "name": "Coffee",
          "description": "1 pound of coffee beans",
          "sku": "sku03",
          "unit_amount": {
            "currency_code": "USD",
            "value": "40.00"
          },
          "quantity": "1",
          "category": "PHYSICAL_GOODS",
          "image_url": "https://example.com/static/images/items/1/coffee_beans.jpg",
          "url": "https://example.com/items/1/coffee_beans",
          "upc": {
            "type": "UPC-A",
            "code": "987654321015"
          }
        }
      ],
      "shipping": {
        "type": "SHIPPING",
        "name": {
          "full_name": "Firstname Lastname"
        },
        "address": {
          "address_line_1": "123 Main St.",
          "admin_area_2": "Anytown",
          "admin_area_1": "CA", // Must be sent in 2-letter format
          "postal_code": "12345",
          "country_code": "US"
        },
        "phone_number": {
          "country_code": "1",
          "national_number": "5555555555"
        }
      }
    }
  ]
}'
```


#### **`Save payment method`**
```curl
curl -v -k -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
 -H 'PayPal-Request-Id: UNIQUE_ID' \
 -H 'Authorization: Bearer PAYPAL_ACCESS_TOKEN' \
 -H 'Content-Type: application/json' \
 -H 'PayPal-Client-Metadata-Id: YOUR_CMID' \
 -d '{
  "intent": "CAPTURE",
  "payment_source": {
    "card": {
      "single_use_token": "1h371660pr490622k" // Payment token from the client
    }
  },
  "attributes": {
    "vault": {
      "store_in_vault": "ON_SUCCESS"
    }
},
  "purchase_units": [
    {
      "amount": {
        "currency_code": "USD",
        "value": "50.00",
        "breakdown": {
          "item_total": {
            "currency_code": "USD",
            "value": "40.00"
          },
          "shipping": {
            "currency_code": "USD",
            "value": "10.00"
          }
        }
      },
      "items": [
        {
          "name": "Coffee",
          "description": "1 pound of coffee beans",
          "sku": "sku03",
          "unit_amount": {
            "currency_code": "USD",
            "value": "40.00"
          },
          "quantity": "1",
          "category": "PHYSICAL_GOODS",
          "image_url": "https://example.com/static/images/items/1/coffee_beans.jpg",
          "url": "https://example.com/items/1/coffee_beans",
          "upc": {
            "type": "UPC-A",
            "code": "987654321015"
          }
        }
      ],
      "shipping": {
        "type": "SHIPPING",
        "name": {
          "full_name": "Firstname Lastname"
        },
        "address": {
          "address_line_1": "123 Main St.",
          "admin_area_2": "Anytown",
          "admin_area_1": "CA", // Must be sent in 2-letter format
          "postal_code": "12345",
          "country_code": "US"
        },
        "phone_number": {
          "country_code": "1",
          "national_number": "5555555555"
        }
      }
    }
  ]
}'
```


#### **`Vault`**
```curl
curl -v -k -X POST https://api-m.sandbox.paypal.com/v3/vault/payment-tokens \
 -H 'PayPal-Request-Id: UNIQUE_ID' \
 -H 'Authorization: Bearer PAYPAL_ACCESS_TOKEN' \
 -H 'Content-Type: application/json' \
 -H 'PayPal-Client-Metadata-Id: YOUR_CMID' \
 -d '{
  "payment_source": {
    "token": {
      "type": "NONCE",
      "id": "tokencc_bc_5k26jm_ffwg2n_tcvnhd_kkfth3_k74"
    }
  }
}'
```
 

## Sandbox testing
To trigger 3DS in Sandbox, add a valid BIN test card to your [Fastlane profile](http://fastlane.sandbox.paypal.com) .
Use the following recommended test card.

| Card network | Card number | Expiration date | CVV |
| Mastercard | 5186459910794125 | Any future date | 123 |
