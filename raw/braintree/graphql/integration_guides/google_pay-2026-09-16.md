<!-- Source URL: https://developer.paypal.com/braintree/graphql/integration_guides/google_pay -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Google Pay
slug: /graphql/integration_guides/google_pay/
createTime: '2025-01-16T11:26:39.986Z'
updateTime: '2025-05-01T01:25:32.786Z'
---



# Google Pay

Google Pay provides both in-app and web purchasing experiences for customers with supported Android devices. It allows customers to pay with cards and PayPal accounts stored in their Google account, in addition to those stored in Google Pay.

For more details on compatibility and availability, see our [Google Pay support article](/braintree/articles/guides/payment-methods/google-pay).


## Creating transactions


### Using Credit Cards

For the purpose of making transactions, a Google Pay card is treated just like a standard credit card with a few noted differences.

You can create a Google Pay transaction using the [chargePaymentMethod](/braintree/graphql/reference/#Mutation--chargePaymentMethod) mutation while suppling an amount and paymentMethodId.

### Mutation
```graphql
mutation ChargePaymentMethod($input: ChargePaymentMethodInput!) {
  chargePaymentMethod(input: $input) {
    transaction {
      id
      legacyId
      status
      paymentMethodSnapshot {
        ... on CreditCardDetails {
          origin {
            type
            details {
              ... on GooglePayOriginDetails {
                googleTransactionId
                bin
              }
            }
          }
        }
      }
    }
  }
}

```


### Variables
```json
{
  "input": {
    "paymentMethodId": "id_of_payment_method",
    "transaction": { "amount": "1.00" }
  }
}

```

### Response
```json
{
  "data": {
    "chargePaymentMethod": {
      "transaction": {
        "id": "id_of_transaction",
        "legacyId": "legacy_id_of_transaction",
        "status": "SUBMITTED_FOR_SETTLEMENT",
        "paymentMethodSnapshot": {
          "origin": {
            "type": "GOOGLE_PAY",
            "details": {
              "googleTransactionId": "id_of_google_transaction",
              "bin": "bank_identification_number"
            }
          }
        }
      }
    }
  },
  "extensions": { "requestId": "a-uuid-for-the-request" }
}

```
Notice the origin field in the response. The type clearly spells out that it's a Google Pay transaction. You are also able to pass device data under [riskData](/braintree/graphql/reference/#Input--RiskDataInput) for added fraud analysis information just like a in standard credit card charge.


### Using PayPal with Google Pay

Using PayPal on Google Pay will create a PayPal rather than a Google Pay transaction. PayPal transactions using Google Pay can be done the same as credit card transactions on Google Pay using the chargePaymentMethod mutation. The PayPal payment method will be noted with a Google Pay origin, and the transaction will have FacilitatorDetails.OAuthApplication.name set to Google.

### Mutation
```graphql
mutation ChargePaymentMethod($input: ChargePaymentMethodInput!) {
  chargePaymentMethod(input: $input) {
    transaction {
      id
      status
      paymentMethodSnapshot {
        __typename
        ... on PayPalTransactionDetails {
          origin {
            details {
              __typename
            }
          }
        }
      }
      facilitatorDetails {
        oauthApplication {
          name
        }
      }
    }
  }
}

```


### Variables
```json
{
  "input": {
    "paymentMethodId": "id_of_google_pay_paypal_payment_method",
    "transaction": { "amount": "1.00" }
  }
}

```

### Response
```json
{
  "data": {
    "chargePaymentMethod": {
      "transaction": {
        "id": "id_of_transaction",
        "status": "SETTLING",
        "paymentMethodSnapshot": {
          "__typename": "PayPalTransactionDetails",
          "origin": { "details": { "__typename": "GooglePayOriginDetails" } }
        },
        "facilitatorDetails": { "oauthApplication": { "name": "Google" } }
      }
    }
  },
  "extensions": { "requestId": "a-uuid-for-the-request" }
}

```
The merchant account used at transaction time must accept PayPal transactions.Creating a transaction with a PayPal account through Google Pay is effectively the same as creating a transaction from your PayPal integration, they have the same [settlement rules and options that typical PayPal transactions have](/braintree/docs/guides/paypal/server-side/#settlement).

For certain account setups, it is recommended that merchants collect and pass billing address information when storing payment methods and/or creating transactions. Passing billing address details (postal code at minimum) can help increase the likelihood of a successful authorization. To learn more about your specific account setup,[contact us](/braintree/help?issue=TransactionProcessingQuestion).
## Vaulting Google Pay

Google Pay cards can only be saved to your Vault for specific use cases; see the [support article for details](/braintree/articles/guides/payment-methods/google-pay/#recurring-billing-and-vaulting).

Vaulting of PayPal accounts from Google Pay is currently not supported. This means the options passed in vaultPaymentMethodAfterTransacting while using [chargePaymentMethod](/braintree/graphql/reference/#Mutation--chargePaymentMethod) mutation are not supported when creating a transaction.

If your use case is supported, you can store a customer's Google Pay card in your Vault in one of the following ways:


- Using the[vaultPaymentMethod](/braintree/graphql/reference/#Mutation--vaultPaymentMethod)mutation
- IncludingvaultPaymentMethodAfterTransactingin the input for the[chargePaymentMethod](/braintree/graphql/guides/transactions/#creating-transactions)mutation

