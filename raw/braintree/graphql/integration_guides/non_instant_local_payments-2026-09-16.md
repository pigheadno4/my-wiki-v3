<!-- Source URL: https://developer.paypal.com/braintree/graphql/integration_guides/non_instant_local_payments -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Non-Instant Local Payments
slug: /graphql/integration_guides/non_instant_local_payments/
createTime: '2025-01-16T11:27:05.289Z'
updateTime: '2025-05-01T21:37:04.690Z'
---



# Non-Instant Local Payment Methods


## Requirements


- In order to use this API, you must have[created and linked](/braintree/articles/guides/payment-methods/paypal/setup-guide)your PayPal account with login credentials to the Braintree control panel.

The PayPal account must be set up to transact in the same currency of the targeted funding source. OXXO: Mexican pesos (MXN), Boleto Bancário: Brazilean real (BRL), and Multibanco: European Union euro (EUR). Failure to do so will result in a[validation error](https://developer.paypal.com/docs/api/orders/v2/#error-PAYEE_COUNTRY_NOT_SUPPORTED_FOR_PAYMENT_SOURCE).
- This API is available for all merchants to test in sandbox. For production usage, your account must be enabled to use this feature. Please contact[Braintree Support](/braintree/help)for further assistance.


## Creating Non-Instant Local Payment Contexts

To create a non-instant [local payment context](/braintree/articles/guides/payment-methods/local-payment-methods#payment-contexts), you will specify all relevant transaction information for that payment scheme.

Braintree currently supports the following non-instant payment schemes:


- Multibanco
- OXXO
- Trustly


## Fetching Non-Instant Local Payment Contexts

See [Fetching Local Payment Contexts](/braintree/graphql/integration_guides/local_payment_contexts/#fetching-local-payment-contexts) page.


## Capturing Non-Instant Transactions

There is no capture call for non-instant transactions; Braintree will associate a transaction on behalf of the merchant once we receive confirmation that the voucher has been paid.

Use the approval url from the mutation response to display a modal in which you can simulate a successful payment, an expired payment, or an unapproved payment.
- Successful payment: a webhook will be sent to the merchant in 2-3 minutes and the payment context will update to show an associated transaction in a settled state.
- Expired payment: a webhook will be sent to the merchant in 2-3 minutes and the payment context will be expired.
- Unapproved payment: the payment context will be expired.


## Multibanco

**Required fields**


- amount- the amount of the order.
- payerInfo/givenName- the given name of the buyer.
- payerInfo/surname- the given surname of the buyer.
- type- this must beMULTIBANCO.

**Optional fields**


- orderId- this will be a merchant-generated identifier for the order.

**Ignored fields**


- expiryDate- this value is not overridable; the value is alwaystoday + 7 days.

### Mutation
```graphql
mutation CreateNonInstantLocalPaymentContext(
  $input: CreateNonInstantLocalPaymentContextInput!
) {
  createNonInstantLocalPaymentContext(input: $input) {
    paymentContext {
      id
      type
      paymentId
      approvalUrl
      merchantAccountId
      createdAt
      transactedAt
      approvedAt
      amount {
        value
        currencyCode
      }
    }
  }
}

```


### Variables,
```json
{
  "input": {
    "paymentContext": {
      "amount": { "value": 1.23, "currencyCode": "EUR" },
      "type": "MULTIBANCO",
      "countryCode": "PT",
      "returnUrl": "https://example.com/return",
      "cancelUrl": "https://example.com/cancel",
      "merchantAccountId": "a_merchant_account_id",
      "payerInfo": {
        "givenName": "John",
        "surname": "Doe"
      }
    }
  }
}

```

### Response
```json
{
  "data": {
    "createNonInstantLocalPaymentContext": {
      "paymentContext": {
        "id": "a_payment_context_id",
        "type": "multibanco",
        "paymentId": "a_payment_id",
        "approvalUrl": "https://example.com/approval",
        "merchantAccountId": "a_merchant_account_id",
        "createdAt": "2021-07-28",
        "transactedAt": "2021-07-28",
        "approvedAt": "2021-07-28",
        "amount": { "value": 1.23, "currencyIsoCode": "EUR" }
      }
    },
    "extensions": { "requestId": "abc-123-def-456" }
  }
}

```

## OXXO

**Required fields**


- amount- the amount of the order.
- payerInfo/billingAddress- the billing address of the buyer.
- payerInfo/givenName- the given name of the buyer.
- payerInfo/surname- the given surname of the buyer.
- type- this must beOXXO.

**Optional fields**


- expiryDate- ifexpiryDateis omitted, it will default totoday + 3 days.
- orderId- this will be a merchant-generated identifier for the order.

### Mutation
```graphql
mutation CreateNonInstantLocalPaymentContext(
  $input: CreateNonInstantLocalPaymentContextInput!
) {
  createNonInstantLocalPaymentContext(input: $input) {
    paymentContext {
      id
      type
      paymentId
      approvalUrl
      merchantAccountId
      createdAt
      transactedAt
      approvedAt
      amount {
        value
        currencyCode
      }
    }
  }
}

```


### Variables,
```json
{
  "input": {
    "paymentContext": {
      "amount": { "value": 1.23, "currencyCode": "MXN" },
      "type": "OXXO",
      "countryCode": "MX",
      "returnUrl": "https://example.com/return",
      "cancelUrl": "https://example.com/cancel",
      "merchantAccountId": "a_merchant_account_id",
      "payerInfo": {
        "givenName": "John",
        "surname": "Doe",
        "email": "john.doe@example.com"
      }
    }
  }
}

```

### Response
```json
{
  "data": {
    "createNonInstantLocalPaymentContext": {
      "paymentContext": {
        "id": "a_payment_context_id",
        "type": "oxxo",
        "paymentId": "a_payment_id",
        "approvalUrl": "https://example.com/approval",
        "merchantAccountId": "a_merchant_account_id",
        "createdAt": "2021-07-28",
        "transactedAt": "2021-07-28",
        "approvedAt": "2021-07-28",
        "amount": { "value": 1.23, "currencyIsoCode": "MXN" }
      }
    },
    "extensions": { "requestId": "abc-123-def-456" }
  }
}

```

## Trustly

**Required fields**


- amount- the amount of the order.
- payerInfo/phoneNumber- the phone number of the buyer.
- type- this must beTRUSTLY.

**Optional fields**


- orderId- this will be a merchant-generated identifier for the order.

**Ignored fields**


- expiryDate- this value is not overridable; the value is alwaystoday + 7 days.

### Mutation
```graphql
mutation CreateNonInstantLocalPaymentContext(
  $input: CreateNonInstantLocalPaymentContextInput!
) {
  createNonInstantLocalPaymentContext(input: $input) {
    paymentContext {
      id
      type
      paymentId
      approvalUrl
      merchantAccountId
      createdAt
      transactedAt
      approvedAt
      amount {
        value
        currencyCode
      }
    }
  }
}

```


### Variables,
```json
{
  "input": {
    "paymentContext": {
      "amount": { "value": 10.22, "currencyCode": "EUR" },
      "type": "TRUSTLY",
      "countryCode": "DE",
      "returnUrl": "https://example.com/return",
      "cancelUrl": "https://example.com/cancel",
      "merchantAccountId": "a_merchant_account_id",
      "payerInfo": {
        "phoneNumber": "487238725269"
      }
    }
  }
}

```

### Response
```json
{
  "data": {
    "createNonInstantLocalPaymentContext": {
      "paymentContext": {
        "id": "a_payment_context_id",
        "type": "trustly",
        "paymentId": "a_payment_id",
        "approvalUrl": "https://example.com/approval",
        "merchantAccountId": "a_merchant_account_id",
        "createdAt": "2021-07-28",
        "transactedAt": "2021-07-28",
        "approvedAt": "2021-07-28",
        "amount": { "value": 10.22, "currencyIsoCode": "EUR" }
      }
    },
    "extensions": { "requestId": "abc-123-def-456" }
  }
}

```

## Error Samples

[General API error documentation](/braintree/graphql/guides/making_api_calls/#understanding-responses)


### JSON
```json
{
  "errors": [
    {
      "message": "Presentment currency code USD is invalid for funding source oxxo",
      "locations": [{ "line": 2, "column": 3 }],
      "path": ["createNonInstantLocalPaymentContext"],
      "extensions": {
        "errorClass": "VALIDATION",
        "errorType": "user_error",
        "inputPath": ["input", "paymentContext"]
      }
    }
  ],
  "data": { "createNonInstantLocalPaymentContext": null },
  "extensions": { "requestId": "abc-123-def-456" }
}

```

### JSON
```json
{
  "errors": [
    {
      "message": "The requested action could not be performed, semantically incorrect, or failed business validation.",
      "locations": [{ "line": 2, "column": 3 }],
      "path": ["createNonInstantLocalPaymentContext"],
      "extensions": {
        "errorClass": "VALIDATION",
        "errorType": "user_error",
        "inputPath": ["input", "paymentContext"]
      }
    }
  ],
  "data": { "createNonInstantLocalPaymentContext": null },
  "extensions": { "requestId": "abc-123-def-456" }
}

```
