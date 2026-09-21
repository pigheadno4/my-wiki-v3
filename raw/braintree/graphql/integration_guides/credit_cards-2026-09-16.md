<!-- Source URL: https://developer.paypal.com/braintree/graphql/integration_guides/credit_cards -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Credit Card Integration Guide
slug: /graphql/integration_guides/credit_cards/
createTime: '2025-01-16T11:25:33.370Z'
updateTime: '2025-04-30T16:36:45.151Z'
---



# Credit Cards


## Creating simple transactions

Using [chargePaymentMethod](/braintree/graphql/reference/#Mutation--chargePaymentMethod) mutation is the simplest way to create a credit card transaction.

You can create a transaction with just an amount and a single-use payment method relayed from your client and immediately [submit for settlement](/braintree/articles/get-started/transaction-lifecycle/#submitted-for-settlement). You may see single-use payments methods referred to as a payment_method_nonce in your client. See [here](/braintree/graphql/guides/collecting_payment_information/#use-the-payment-method) for more information regarding this terminology difference.

### Mutation
```graphql
mutation ChargePaymentMethod($input: ChargePaymentMethodInput!) {
  chargePaymentMethod(input: $input) {
    transaction {
      status
      id
      legacyId
    }
  }
}

```


### Variables
```json
{
  "input": {
    "paymentMethodId": "id_of_payment_method",
    "transaction": {
      "amount": 15
    }
  }
}
```

### Response
```json
{
  "data": {
    "chargePaymentMethod": {
      "transaction": {
        "status": "SUBMITTED_FOR_SETTLEMENT",
        "id": "id_of_transaction",
        "legacyId": "legacy_id_of_transaction"
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
If you want to save a payment method for future transactions, you will need to save it to your Vault. If you want to save a payment method to your Vault upon a successful transaction, see the [vaultPaymentMethodAfterTransactingInput](/braintree/graphql/reference/#Input--VaultPaymentMethodAfterTransactingInput) field on [TransactionInput](/braintree/graphql/reference/#Input--TransactionInput). Follow the [Vaulting a Payment Method](/braintree/graphql/guides/payment_methods/#vaulting_the_payment_method) guide for step-by-step instructions on vaulting payment methods without an associated transaction.


## Creating advanced transactions

For more advanced use cases, like passing the billing address, tokenized CVV, or 3D Secure authentication, use the [chargeCreditCard](/braintree/graphql/reference/#Mutation--chargeCreditCard) mutation, which accepts additional inputs.

### Mutation
```graphql
mutation ChargeCreditCard($input: ChargeCreditCardInput!) {
  chargeCreditCard(input: $input) {
    transaction {
      id
      legacyId
      createdAt
      amount {
        value
        currencyCode
      }
      status
      billingAddress {
        addressLine1
        adminArea1
        adminArea2
        postalCode
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
    "options": {
      "billingAddress": {
        "addressLine1": "123 Main St",
        "adminArea1": "CA",
        "adminArea2": "San Jose",
        "postalCode": "95086"
      }
    },
    "transaction": {
      "amount": "1.00"
    }
  }
}
```

### Response
```json
{
  "data": {
    "chargeCreditCard": {
      "transaction": {
        "id": "id_of_transaction",
        "legacyId": "legacy_id_of_transaction",
        "createdAt": "date_time_of_transaction",
        "amount": {
          "value": "1.00",
          "currencyCode": "USD"
        },
        "status": "SUBMITTED_FOR_SETTLEMENT",
        "billingAddress": {
          "addressLine1": "123 Main St",
          "adminArea1": "CA",
          "adminArea2": "San Jose",
          "postalCode": "95086"
        }
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

### Card verification

When a payment method is a credit or debit card, you can use card verification to establish that the card data matches a valid, open account before storing or updating it in your Vault.

Braintree strongly recommends verifying all cards before they are stored in your Vault by [enabling card verification in the Control Panel](/braintree/articles/control-panel/vault/card-verification/#enabling-card-verification).

If you want to run a verification on a credit card already stored in your Vault, you can do so using the [verifyCreditCard](/braintree/graphql/reference/#Mutation--verifyCreditCard) mutation.

The gateway verifies cards by running a $0 or $1 authorization and then automatically voids it. If you'd like, you can specify a different amount via [CreditCardVerificationOptionsInput](/braintree/graphql/reference/#Input--CreditCardVerificationOptionsInput) for the authorization.

### Mutation
```graphql
mutation VerifyCreditCard($input: VerifyCreditCardInput!) {
  verifyCreditCard(input: $input) {
    verification {
      id
      legacyId
      status
      paymentMethodVerificationDetails {
        __typename
        ... on CreditCardVerificationDetails {
          amount {
            value
            currencyCode
          }
        }
      }
      processorResponse {
        legacyCode
        message
      }
    }
  }
}

```


### Variables
```json
{
  "input": {
    "paymentMethodId": "id_of_payment_method"
  }
}
```

### Response
```json
{
  "data": {
    "verifyCreditCard": {
      "verification": {
        "id": "id_of_verification",
        "legacyId": "legacy_id_of_verification",
        "status": "VERIFIED",
        "paymentMethodVerificationDetails": {
          "__typename": "CreditCardVerificationDetails",
          "amount": {
            "value": "0.00",
            "currencyCode": "USD"
          }
        },
        "processorResponse": {
          "legacyCode": "1000",
          "message": "Approved"
        }
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
If you use our Premium Fraud Management Tools, we strongly recommend passing[deviceData](/braintree/graphql/reference/#Input--RiskDataInput)each time you verify a card.
### Verification results

If verification is successful, the result will contain a [VerifyPaymentMethodPayload](/braintree/graphql/reference/#Object--VerifyPaymentMethodPayload) response object, which will contain a [VerificationDetails](/braintree/graphql/reference/#Union--VerificationDetails) response object.


### Response
```json
{
  "paymentMethodVerificationDetails": {
    "__typename": "CreditCardVerificationDetails",
    "amount": {
      "value": "1.25",
      "currencyCode": "USD"
    }
  }
}
```
Otherwise, you'll receive a [VerificationDetails](/braintree/graphql/reference/#Union--VerificationDetails) response object directly on a Customer or PaymentMethod result. This occurs when verification is run, and it returns with a status of PROCESSOR_DECLINED or GATEWAY_REJECTED


### Reasons for unsuccessful verification results

You can check the message and legacyCode of the [processorResponse](/braintree/graphql/reference/#Object--VerificationProcessorResponse) for the reason that verification was PROCESSOR_DECLINED. If the status is GATEWAY_REJECTED, you can check the [gatewayRejectionReason](/braintree/graphql/reference/#Enum--GatewayRejectionReason) field for the specific reason. [Learn more about gateway rejections](/braintree/articles/control-panel/transactions/gateway-rejections).


### Verify and Vault

If you need to verify a credit card and subsequently save it in your Vault, you can do both in a single request using [vaultCreditCard](/braintree/graphql/reference/#Mutation--vaultCreditCard) mutation. If the verification succeeds, the resulting multi-use payment method will be saved in your Vault, and the status attribute in the response will be set to VERIFIED.

### Mutation
```graphql
mutation VaultCreditCard($input: VaultCreditCardInput!) {
  vaultCreditCard(input: $input) {
    paymentMethod {
      id
      details {
        ... on CreditCardDetails {
          brandCode
          last4
        }
      }
    }
    verification {
      id
      legacyId
      status
      processorResponse {
        legacyCode
        message
      }
    }
  }
}

```


### Variables
```json
{
  "input": {
    "paymentMethodId": "id_of_payment_method"
  }
}
```

### Response
```json
{
  "data": {
    "vaultCreditCard": {
      "paymentMethod": {
        "id": "id_of_payment_method",
        "details": {
          "brandCode": "VISA",
          "last4": "1111"
        }
      },
      "verification": {
        "id": "id_of_verification",
        "legacyId": "legacy_id_of_verification",
        "status": "VERIFIED",
        "processorResponse": {
          "legacyCode": "1000",
          "message": "Approved"
        }
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

### Reasons for unsuccessful verification results

What you should check is the status of the response. If the status is VERIFIED, the verification was successful. If the status is PROCESSOR_DECLINED, it means the verification was unsuccessful based on the response from the processor. You can get more details under [processorResponse](/braintree/graphql/reference/#Object--VerificationProcessorResponse) in the response. You can check the [legacyCode](/braintree/docs/reference/general/processor-responses/authorization-responses) and [message](/braintree/docs/reference/general/processor-responses/authorization-responses) for the reason that a verification was declined. If status is GATEWAY_REJECTED, the gateway has rejected it because the payment method has failed one or more fraud checks. If the status is GATEWAY_REJECTED, you can check the [gatewayRejectionReason](/braintree/graphql/reference/#Enum--GatewayRejectionReason) in [GatewayRejectedEvent](/braintree/graphql/reference/#Object--GatewayRejectedEvent) for the specific reason. [Learn more about gateway rejections](/braintree/articles/control-panel/transactions/gateway-rejections).


### Update Billing Address

Updating a credit card's billing address can be done in multiple ways. See our [updating customer information support article](/braintree/articles/control-panel/vault/update/#billing-address) for more information. To update a credit card's billing address via the api you can use the [updateCreditCardBillingAddress](/braintree/graphql/reference/#Mutation--updateCreditCardBillingAddress) mutation. This mutation will set the new billing address for an existing multi-use credit card, and before updating, it will verify the card and new address.

### Mutation
```graphql
mutation UpdateCreditCardBillingAddress(
  $input: UpdateCreditCardBillingAddressInput!
) {
  updateCreditCardBillingAddress(input: $input) {
    billingAddress {
      addressLine1
      adminArea2
      adminArea1
    }
    verification {
      id
      legacyId
      status
    }
  }
}

```


### Variables
```json
{
  "input": {
    "paymentMethodId": "id_of_payment_method",
    "billingAddress": {
      "addressLine1": "123 Cantina",
      "adminArea2": "Mos Eisley",
      "adminArea1": "Tatooine"
    }
  }
}
```

### Response
```json
{
  "data": {
    "updateCreditCardBillingAddress": {
      "billingAddress": {
        "addressLine1": "123 Cantina",
        "adminArea2": "Mos Eisley",
        "adminArea1": "Tatooine"
      },
      "verification": {
        "id": "id_of_verification",
        "legacyId": "legacy_id_of_verification",
        "status": "VERIFIED"
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

### Authorize

If you need to authorize a credit card without submitting for settlement, you can use the [authorizeCreditCard](/braintree/graphql/reference/#Mutation--authorizeCreditCard) mutation. It will return a [TransactionPayload](/braintree/graphql/reference/#Object--TransactionPayload) object that will include transaction details. Check the status of the transaction to see if it was authorized. When [authorizing a credit card](/braintree/articles/control-panel/transactions/managing-authorizations) you will need to ensure you submit the transaction for settlement at a later time using the [captureTransaction](/braintree/graphql/reference/#Mutation--captureTransaction) mutation.

### Mutation
```graphql
mutation AuthorizeCreditCard($input: AuthorizeCreditCardInput!) {
  authorizeCreditCard(input: $input) {
    transaction {
      id
      legacyId
      status
    }
  }
}

```


### Variables
```json
{
  "input": {
    "paymentMethodId": "id_of_payment_method",
    "transaction": {
      "amount": "1.00"
    }
  }
}
```

### Response
```json
{
  "data": {
    "authorizeCreditCard": {
      "transaction": {
        "id": "id_of_payment_transaction",
        "legacyId": "legacy_id_of_transaction",
        "status": "AUTHORIZED"
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

### Creating a Detached Refund

Detached credits are disabled by default and generally violate card association rules. However, it may be appropriate to issue detached credits in some instances. For more information about detached credits, see the [detached credits](/braintree/articles/control-panel/transactions/refunds-voids-credits/#detached-credits) article. To issue detached credits, you can use the [refundCreditCard](/braintree/graphql/reference/#Mutation--refundCreditCard) mutation.

### Mutation
```graphql
mutation ($input: RefundCreditCardInput!) {
  refundCreditCard(input: $input) {
    refund {
      id
      status
      amount {
        value
      }
      orderId
      merchantAccountId
      source
    }
  }
}

```


### Variables
```json
{
  "input": {
    "paymentMethodId": "id_of_payment_method",
    "refund": {
      "amount": "10.00",
      "orderId": "id_of_order"
    }
  }
}
```

### Response
```json
{
  "data": {
    "refundCreditCard": {
      "refund": {
        "id": "id_of_refund",
        "status": "SUBMITTED_FOR_SETTLEMENT",
        "amount": {
          "value": "10.00"
        },
        "orderId": "id_of_order",
        "merchantAccountId": "id_of_merchant_account",
        "source": "API"
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
This mutation is disabled by default. To request that we temporarily enable detached credits, have the authorized signer on your Braintree gateway account[contact us](/braintree/help?issue=TransactionProcessingQuestion).
### Tokenization

The following mutation should only be used if you fall under the PCI SAQ-D compliance level. If you are unsure of your status, do**NOT**use this mutation.[Learn more about how to collect payment information](/braintree/graphql/guides/collecting_payment_information/)The [tokenizeCreditCard](/braintree/graphql/reference/#Mutation--tokenizeCreditCard) mutation will tokenize the credit card fields and return a payload for a single-use payment method.

### Mutation
```graphql
mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {
  tokenizeCreditCard(input: $input) {
    paymentMethod {
      id
      legacyId
      usage
      details {
        ... on CreditCardDetails {
          brandCode
          last4
          expirationMonth
          expirationYear
        }
      }
    }
  }
}

```


### GraphQL,
```graphql
{
  "input": {
    "creditCard": {
      "number": "4111111111111111",
      "expirationMonth": "12",
      "expirationYear": "2024"
    }
  }
}
```

### Response
```json
{
  "data": {
    "tokenizeCreditCard": {
      "paymentMethod": {
        "id": "id_of_payment_method",
        "legacyId": "legacy_id_of_payment_method",
        "usage": "SINGLE_USE",
        "details": {
          "brandCode": "VISA",
          "last4": "1111",
          "expirationMonth": "12",
          "expirationYear": "2024"
        }
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
Once you call the tokenizeCreditCard mutation, you can pass the resulting single-use payment method into various mutations such as chargePaymentMethod and [authorizePaymentMethod](/braintree/graphql/reference/#Mutation--authorizePaymentMethod).

