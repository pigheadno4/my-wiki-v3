---
title: Test and go live with Subscriptions
slug: /docs/subscriptions/test-subscriptions/
createTime: "2024-08-15T08:02:56.807Z"
updateTime: "2025-05-09T15:55:47.656Z"
---

# Test and go live with Subscriptions

You can run negative tests on your integration to manage the responses you give to your customers.

## Know before you code

- Before you trigger a simulation, you'll need to you need to [get an access token](/api/rest/authentication/) .
- Use Postman to explore and test PayPal APIs.

## Test flow

Test a transaction to see the subscription created in the merchant account.

### Test the transaction as a buyer

- Select the PayPal button on the page.

- Use the sandbox personal login information from the Developer Dashboard to log in and simulate the buyer making a purchase.

- In the Checkout window, notice the purchase amount in the upper right corner. USD is the default currency. You can customize the PayPal JavaScript SDK with different [currency codes](/sdk/js/configuration/) .

  **Availability:** The JavaScript SDK onShippingChange , onShippingAddressChange , and onShippingOptionsChange functions are not compatible with Subscriptions.

- Select the pull-down arrow next to the purchase amount. The subscription details are available for the buyer to review. It should appear similar to the following image: ![Screenshot,of,subscription,details,in,checkout](assets/paypal-subscriptions-details.png)

- Complete the flow.

### Confirm funds move from the buyer account

- Use the sandbox personal account you used to complete the purchase to log in to [https://www.sandbox.paypal.com/myaccount/autopay/connect/](https://www.sandbox.paypal.com/myaccount/autopay/connect/) . This URL takes you to the automatic payments page in the sandbox personal account.
- Confirm the subscription appears in the active automatic payment list. Select the active automatic payment to see the details of the subscription.
- Log out of the account.

### Confirm funds move to the merchant account

- Use the sandbox business account information from the Developer Dashboard to log in to [https://www.sandbox.paypal.com/billing/subscriptions](https://www.sandbox.paypal.com/billing/subscriptions) . This URL takes you to the subscriptions management page in the sandbox business account.
- Confirm the subscription made by the test buyer appears on the **Subscriptions** tab. Select the subscription to see the details of the subscription.
- Log out of the account.

## Simulation methods

To trigger a simulation for the Subscriptions API, you can use either a [JSON pointer in the request payload](#use-a-json-pointer-in-the-request-payload) or a [path parameter in the request URI](#use-a-path-parameter-in-the-request-uri) .

### Use a JSON pointer in the request payload

| Trigger | Test value | Simulated error response |
| ------- | ---------- | ------------------------ |
| plan_id | ERRSUB033  | NOT_AUTHORIZED           |

#### Request

curl -X POST \
 https://api-m.sandbox.paypal.com/v1/billing/subscriptions \
 -H 'Authorization: Bearer &lt;Access Token&gt;'
-d '{
"plan_id": "ERRSUB033",
"start_time": "2020-02-06T15:00:00Z",
"quantity": "1",
"shipping_amount": {
"currency_code": "USD",
"value": "12.00"
},
"subscriber": {
"name": {
"given_name": "John",
"surname": "Doe"
},
"email_address": "customer@example.com",
"shipping_address": {
"name": {
"full_name": "John Doe"
},
"address": {
"address_line_1": "2211 N First Street",
"address_line_2": "Building 17",
"admin_area_2": "San Jose",
"admin_area_1": "CA",
"postal_code": "95131",
"country_code": "US"
}
}
},
"application_context": {
"brand_name": "Walmart Inc",
"locale": "en-US",
"shipping_preference": "SET_PROVIDED_ADDRESS",
"user_action": "SUBSCRIBE_NOW",
"payment_method": {
"payer_selected": "PAYPAL_CREDIT",
"payee_preferred": "IMMEDIATE_PAYMENT_REQUIRED"
},
"return_url": "http://zoho.com/returnUrl",
"cancel_url": "http://zoho.com/cancelUrl"
}
}'#### Response
{
"name": "NOT_AUTHORIZED",
"debugId": "b1d1f06c7246c",
"message": "Authorization failed due to insufficient permissions.",
"details": [
{
"issue": "PERMISSION_DENIED",
"description": "You do not have permission to access or perform operations on this resource."
}
],
"links": [
{
"href": "https://developer.paypal.com/docs/api/v1/billing/subscriptions#PERMISSION_DENIED",
"rel": "information_link",
"method": "GET"
}
]
}### Use a path parameter in the request URI
| Trigger or test value | Simulated error response |
| --- | --- |
| v1/billing/subscriptions/ERRSUB068/activate | RESOURCE_NOT_FOUND |

#### Request

curl -X GET \
 https://api-m.sandbox.paypal.com/v1/billing/subscriptions/ERRSUB068/activate \
 -H 'Authorization: Bearer &lt;Access Token&gt;' \
 -H 'Content-Type: application/json' \
 -d '{
"reason": "Reactivating the subscription"
}
}'#### Response
{
"name": "RESOURCE_NOT_FOUND",
"message": "The specified resource does not exist.",
"debug_id": "c2d1f06c7246c",
"details": [
{
"issue": "INVALID_RESOURCE_ID",
 "description": "Requested resource ID was not found",
"value": "I-TT452GLLEP1G"
}
],
"links": [
{
"href": "https://developer.paypal.com/docs/api/v1/billing/subscriptions#RESOURCE_NOT_FOUND,
"rel": "information_link"
}
]
}## Test values
Use the following test values to trigger positive and negative responses for these subscriptions actions:

\*\*\*\* [Product](#product)

- [Create product](#create-product)
- [Get product](#get-product)
- [List products](#list-products)
- [Update product](#update-product)

\*\*\*\* [Plan](#plan)

- [Create plan](#create-plan)
- [Activate plan](#activate-plan)
- [Deactivate plan](#deactivate-plan)
- [Get plan](#get-plan)
- [List plans](#list-plans)
- [Update plan](#update-plan)
- [Change plan pricing](#change-plan-pricing)

\*\*\*\* [Subscription](#subscription)

- [Create subscription](#create-subscription)
- [Activate subscriptions](#activate-subscriptions)
- [Get subscription](#get-subscription)
- [Update subscription](#update-subscription)
- [Revise subscription](#revise-subscription)
- [Suspend subscription](#suspend-subscription)
- [Capture subscription](#capture-subscription)
- [Get subscription transaction](#get-subscription-transaction)
- [Cancel subscription](#cancel-subscription)

### Product

**Note:** Test values are case sensitive.

#### Create product

##### Negative response test values

Use the JSON pointer in the request payload to simulate the following error responses at POST /v1/catalogs/products .

| Trigger | Test value | Simulated error response |
| ------- | ---------- | ------------------------ |
| name    | ERRCAT001  | INTERNAL_SERVER_ERROR    |
| name    | ERRCAT002  | NOT_AUTHORIZED           |
| name    | ERRCAT003  | INVALID_REQUEST          |
| name    | ERRCAT004  | INVALID_REQUEST          |
| name    | ERRCAT005  | UNPROCESSABLE_ENTITY     |

#### Get product

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at GET /v1/catalogs/products/{test_value} .

| Trigger or test value           | Simulated error response |
| ------------------------------- | ------------------------ |
| /v1/catalogs/products/ERRCAT008 | INTERNAL_SERVER_ERROR    |
| /v1/catalogs/products/ERRCAT009 | NOT_AUTHORIZED           |
| /v1/catalogs/products/ERRCAT010 | RESOURCE_NOT_FOUND       |

#### List products

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at GET /v1/billing/plans/?&total_required={test_value} .

| Trigger or test value                          | Simulated error response |
| ---------------------------------------------- | ------------------------ |
| /v1/catalogs/products?total_required=ERRCAT006 | INTERNAL_SERVER_ERROR    |
| /v1/catalogs/products?total_required=ERRCAT007 | NOT_AUTHORIZED           |

#### Update product

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at PATCH /v1/catalog/products/{test_value} .

| Trigger or test value           | Simulated error response |
| ------------------------------- | ------------------------ |
| /v1/catalogs/products/ERRCAT011 | INTERNAL_SERVER_ERROR    |
| /v1/catalogs/products/ERRCAT012 | NOT_AUTHORIZED           |
| /v1/catalogs/products/ERRCAT013 | INVALID_REQUEST          |
| /v1/catalogs/products/ERRCAT014 | UNPROCESSABLE_ENTITY     |

### Plan

**Note:** Test values are case sensitive.

#### Create plan

##### Negative response test values

Use the JSON pointer in the request payload to simulate the following error responses at POST /v1/billing/plans/ .

| Trigger | Test value | Simulated error response |
| ------- | ---------- | ------------------------ |
| name    | ERRSUB001  | INTERNAL_SERVER_ERROR    |
| name    | ERRSUB002  | NOT_AUTHORIZED           |
| name    | ERRSUB003  | INVALID_REQUEST          |
| name    | ERRSUB004  | UNPROCESSABLE_ENTITY     |

#### Activate plan

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at POST/v1/billing/plans/{test_value}/activate .

| Trigger or test value                | Simulated error response |
| ------------------------------------ | ------------------------ |
| /v1/billing/plans/ERRSUB015/activate | INTERNAL_SERVER_ERROR    |
| /v1/billing/plans/ERRSUB016/activate | NOT_AUTHORIZED           |
| /v1/billing/plans/ERRSUB017/activate | RESOURCE_NOT_FOUND       |
| /v1/billing/plans/ERRSUB018/activate | UNPROCESSABLE_ENTITY     |

#### Deactivate plan

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at POST /v1/billing/plans/{test_value}/deactivate .

| Trigger or test value                  | Simulated error response |
| -------------------------------------- | ------------------------ |
| /v1/billing/plans/ERRSUB019/deactivate | INTERNAL_SERVER_ERROR    |
| /v1/billing/plans/ERRSUB020/deactivate | NOT_AUTHORIZED           |
| /v1/billing/plans/ERRSUB021/deactivate | RESOURCE_NOT_FOUND       |
| /v1/billing/plans/ERRSUB022/deactivate | UNPROCESSABLE_ENTITY     |

#### Get plan

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at GET /v1/billing/plans/{test_value} .

| Trigger or test value       | Simulated error response |
| --------------------------- | ------------------------ |
| /v1/billing/plans/ERRSUB008 | INTERNAL_SERVER_ERROR    |
| /v1/billing/plans/ERRSUB009 | NOT_AUTHORIZED           |
| /v1/billing/plans/ERRSUB009 | RESOURCE_NOT_FOUND       |

#### List plans

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at GET /v1/billing/plans/?page_size=3&page=1&total_required={test_value} .

| Trigger or test value                                         | Simulated error response |
| ------------------------------------------------------------- | ------------------------ |
| /v1/billing/plans?page_size=3&page=1&total_required=ERRSUB005 | INTERNAL_SERVER_ERROR    |
| /v1/billing/plans?page_size=3&page=1&total_required=ERRSUB006 | NOT_AUTHORIZED           |
| /v1/billing/plans?page_size=3&page=1&total_required=ERRSUB007 | INVALID_REQUEST          |

#### Update plan

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at PATCH /v1/billing/plans/{test_value} .

| Trigger or test value       | Simulated error response |
| --------------------------- | ------------------------ |
| /v1/billing/plans/ERRSUB011 | INTERNAL_SERVER_ERROR    |
| /v1/billing/plans/ERRSUB012 | NOT_AUTHORIZED           |
| /v1/billing/plans/ERRSUB013 | RESOURCE_NOT_FOUND       |
| /v1/billing/plans/ERRSUB014 | INVALID_REQUEST          |

#### Change plan pricing

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at POST /v1/billing/plans/{test_value}/update-pricing-schemes .

| Trigger or test value                              | Simulated error response |
| -------------------------------------------------- | ------------------------ |
| /v1/billing/plans/ERRSUB023/update-pricing-schemes | INTERNAL_SERVER_ERROR    |
| /v1/billing/plans/ERRSUB024/update-pricing-schemes | NOT_AUTHORIZED           |
| /v1/billing/plans/ERRSUB025/update-pricing-schemes | INVALID_REQUEST          |
| /v1/billing/plans/ERRSUB026/update-pricing-schemes | RESOURCE_NOT_FOUND       |
| /v1/billing/plans/ERRSUB027/update-pricing-schemes | UNPROCESSABLE_ENTITY     |
| /v1/billing/plans/ERRSUB028/update-pricing-schemes | UNPROCESSABLE_ENTITY     |
| /v1/billing/plans/ERRSUB029/update-pricing-schemes | UNPROCESSABLE_ENTITY     |
| /v1/billing/plans/ERRSUB030/update-pricing-schemes | UNPROCESSABLE_ENTITY     |
| /v1/billing/plans/ERRSUB031/update-pricing-schemes | UNPROCESSABLE_ENTITY     |

### Subscription

**Note:** Test values are case sensitive.

#### Create subscription

##### Negative response test values

Use the JSON pointer in the request payload to simulate the following error responses at POST /v1/billing/subscriptions .

| Trigger | Test value | Simulated error response |
| ------- | ---------- | ------------------------ |
| plan_id | ERRSUB032  | INTERNAL_SERVER_ERROR    |
| plan_id | ERRSUB033  | NOT_AUTHORIZED           |
| plan_id | ERRSUB034  | INVALID_REQUEST          |
| plan_id | ERRSUB035  | INVALID_REQUEST          |
| plan_id | ERRSUB036  | INVALID_REQUEST          |
| plan_id | ERRSUB037  | INVALID_REQUEST          |
| plan_id | ERRSUB038  | INVALID_REQUEST          |
| plan_id | ERRSUB039  | UNPROCESSABLE_ENTITY     |
| plan_id | ERRSUB040  | UNPROCESSABLE_ENTITY     |

#### Activate subscriptions

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at POST /v1/billing/subscriptions/{test_value}/activate .

| Trigger or test value                        | Simulated error response |
| -------------------------------------------- | ------------------------ |
| /v1/billing/subscriptions/ERRSUB066/activate | INTERNAL_SERVER_ERROR    |
| /v1/billing/subscriptions/ERRSUB067/activate | NOT_AUTHORIZED           |
| /v1/billing/subscriptions/ERRSUB068/activate | RESOURCE_NOT_FOUND       |
| /v1/billing/subscriptions/ERRSUB069/activate | UNPROCESSABLE_ENTITY     |
| /v1/billing/subscriptions/ERRSUB070/activate | UNPROCESSABLE_ENTITY     |

#### Get subscription

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at GET /v1/billing/subscriptions/{test_value} .

| Trigger or test value               | Simulated error response |
| ----------------------------------- | ------------------------ |
| /v1/billing/subscriptions/ERRSUB044 | INTERNAL_SERVER_ERROR    |
| /v1/billing/subscriptions/ERRSUB045 | NOT_AUTHORIZED           |
| /v1/billing/subscriptions/ERRSUB046 | RESOURCE_NOT_FOUND       |

#### Update subscription

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at PATCH /v1/billing/subscriptions/{test_value} .

| Trigger or test value               | Simulated error response |
| ----------------------------------- | ------------------------ |
| /v1/billing/subscriptions/ERRSUB047 | INTERNAL_SERVER_ERROR    |
| /v1/billing/subscriptions/ERRSUB048 | NOT_AUTHORIZED           |
| /v1/billing/subscriptions/ERRSUB049 | RESOURCE_NOT_FOUND       |
| /v1/billing/subscriptions/ERRSUB050 | INVALID_REQUEST          |
| /v1/billing/subscriptions/ERRSUB051 | UNPROCESSABLE_ENTITY     |
| /v1/billing/subscriptions/ERRSUB052 | UNPROCESSABLE_ENTITY     |

#### Revise subscription

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at POST /v1/billing/subscriptions/{test_value}/revise .

| Trigger or test value                      | Simulated error response |
| ------------------------------------------ | ------------------------ |
| /v1/billing/subscriptions/ERRSUB053/revise | INTERNAL_SERVER_ERROR    |
| /v1/billing/subscriptions/ERRSUB054/revise | NOT_AUTHORIZED           |
| /v1/billing/subscriptions/ERRSUB055/revise | INVALID_REQUEST          |
| /v1/billing/subscriptions/ERRSUB056/revise | UNPROCESSABLE_ENTITY     |

#### Suspend subscription

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at POST /v1/billing/subscriptions/{test_value}/suspend .

| Trigger or test value                       | Simulated error response |
| ------------------------------------------- | ------------------------ |
| /v1/billing/subscriptions/ERRSUB059/suspend | INTERNAL_SERVER_ERROR    |
| /v1/billing/subscriptions/ERRSUB060/suspend | NOT_AUTHORIZED           |
| /v1/billing/subscriptions/ERRSUB061/suspend | INVALID_REQUEST          |
| /v1/billing/subscriptions/ERRSUB062/suspend | UNPROCESSABLE_ENTITY     |

#### Capture subscription

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at POST /v1/billing/subscriptions/{test_value}/capture .

| Trigger or test value                       | Simulated error response |
| ------------------------------------------- | ------------------------ |
| /v1/billing/subscriptions/ERRSUB071/capture | INTERNAL_SERVER_ERROR    |
| /v1/billing/subscriptions/ERRSUB072/capture | NOT_AUTHORIZED           |
| /v1/billing/subscriptions/ERRSUB073/capture | RESOURCE_NOT_FOUND       |
| /v1/billing/subscriptions/ERRSUB074/capture | INVALID_REQUEST          |
| /v1/billing/subscriptions/ERRSUB075/capture | INVALID_REQUEST          |

#### Get subscription transaction

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at GET /v1/billing/subscriptions/{test_value}/transactions .

| Trigger or test value                            | Simulated error response |
| ------------------------------------------------ | ------------------------ |
| /v1/billing/subscriptions/ERRSUB076/transactions | INTERNAL_SERVER_ERROR    |
| /v1/billing/subscriptions/ERRSUB076/transactions | NOT_AUTHORIZED           |
| /v1/billing/subscriptions/ERRSUB076/transactions | RESOURCE_NOT_FOUND       |
| /v1/billing/subscriptions/ERRSUB076/transactions | INVALID_REQUEST          |

#### Cancel subscription

##### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at POST /v1/billing/subscriptions/{test_value}/cancel .

| Trigger or test value                      | Simulated error response |
| ------------------------------------------ | ------------------------ |
| /v1/billing/subscriptions/ERRSUB063/cancel | INTERNAL_SERVER_ERROR    |
| /v1/billing/subscriptions/ERRSUB064/cancel | NOT_AUTHORIZED           |
| /v1/billing/subscriptions/ERRSUB065/cancel | RESOURCE_NOT_FOUND       |

## Error handling

An error includes:

- The error name and description.
- A link to error-related documentation.
- A debug ID.
- Error details.

### API errors

| HTTP status code | Error name             | Message                                                                                             | Details                                                                                                                                                    |
| ---------------- | ---------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400              | INVALID_REQUEST        | Request is not well-formed, syntactically incorrect, or violates schema.                            | A required field is missing.                                                                                                                               |
| 401              | AUTHENTICATION_FAILURE | Authorization error occurred.                                                                       | Authorization error occurred. Check your credentials.                                                                                                      |
| 403              | NOT_AUTHORIZED         | Authorization failed due to insufficient permissions.                                               | You do not have permission to access or perform operations on this resource.                                                                               |
| 404              | RESOURCE_NOT_FOUND     | The specified resource does not exist.                                                              | Requested resource ID was not found.                                                                                                                       |
| 422              | UNPROCESSABLE_ENTITY   | The requested action could not be performed, semantically incorrect, or failed business validation. | Invalid plan status for activate action; plan status should be either inactive or created.                                                                 |
| 500              | INTERNAL_SERVER_ERROR  | An internal server error has occurred.                                                              | Resend the request at another time. If this error continues, contact[PayPal Merchant Technical Support](https://www.paypal-support.com/s/?language=en_US). |

### Sample error response

{
"name": "INVALID_REQUEST",
"message": "Request is not well-formed, syntactically incorrect, or violates schema",
"debug_id": "6u3y6fca61718",
"details": [{
"field": "/plan_id",
"issue": "MISSING_REQUIRED_PARAMETER",
"description": "A required field is missing.",
"location": "body"
}],
"links": [{
"href": "https://developer.paypal.com/docs/api/v2/payments/#INVALID_REQUEST",
"rel": "information_link",
"method": "GET"
}]
}## Go live

- Change the base URL for all your REST API calls from https://api-m.sandbox.paypal.com to https://api-m.paypal.com .
- Change the references to your sandbox API credentials to the live credentials. To get live API credentials, [create a live REST API](/docs/multiparty/get-started/#get-api-credentials) .
