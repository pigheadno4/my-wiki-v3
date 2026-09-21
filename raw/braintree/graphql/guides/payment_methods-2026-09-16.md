<!-- Source URL: https://developer.paypal.com/braintree/graphql/guides/payment_methods -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Payment Methods
slug: /graphql/guides/payment_methods/
createTime: '2025-01-16T11:26:22.933Z'
updateTime: '2026-02-27T10:18:13.353Z'
---



# Payment Methods

A [PaymentMethod](/braintree/graphql/reference/#Object--PaymentMethod) represents transactable payment information such as credit card details or a customer's authorization to charge a PayPal or Venmo account. Payment methods belong to a [customer](/braintree/graphql/guides/customers), are securely stored in the Braintree Vault, and have an id attribute that you can store on your servers (with reduced PCI compliance burden) and later use to create [create transactions](/braintree/graphql/guides/transactions/#creating-transactions).


## Obtain A Single-Use Payment Method (Nonce)

Follow [this guide](/braintree/docs/start/hello-server#receive-a-payment-method-nonce-from-your-client) to obtain a payment method nonce from your client.

In this context, you can think of the payment method nonce string as a unique ID for a credit card, PayPal account, or any other payment method type that you've already sent to Braintree from your client-side integration. In the GraphQL API, this is represented by the [PaymentMethod](/braintree/graphql/reference/#Object--PaymentMethod) type, with its usage field containing a value of SINGLE_USE. The ID for this tokenized, single-use payment method information is the only thing you need to vault it.

For the remainder of this guide, we will refer to the payment method represented by the nonce as a "single-use payment method", and the nonce itself as its ID.


## Vaulting The Payment Method

Once you have a single-use payment method ID from your client, you can vault the underlying payment method. To do so, use the [vaultPaymentMethod](/braintree/graphql/reference/#Mutation--vaultPaymentMethod) mutation.

This mutation will automatically run a verification against payment methods that support them before storing them in the vault. The verification result is represented both at the top level as vaultPaymentMethod.verification, and on the payment method itself in vaultPaymentMethod.paymentMethod.verifications.

Note that the single-use payment method will be consumed if it is successfully vaulted. You will not be able to use it again. Instead, the mutation will return a new, multi-use payment method representing the same payment information. Use the ID returned by the [vaultPaymentMethod](/braintree/graphql/reference/#Mutation--vaultPaymentMethod) mutation to charge it.

### Mutation
```graphql
mutation ExampleVaultWithTypeFragment($input: VaultPaymentMethodInput!) {
  vaultPaymentMethod(input: $input) {
    paymentMethod {
      id
      usage
      details {
        __typename
        ... on CreditCardDetails {
          cardholderName
        }
        ... on PaypalAccountDetails {
          payer {
            email
          }
        }
        ... on VenmoAccountDetails {
          username
        }
        ... on UsBankAccountDetails {
          accountHolderName
        }
      }
    }
    verification {
      status
    }
  }
}

```


### Variables
```json
{
  "input": {
    "paymentMethodId": "id_of_single_use_payment_method"
  }
}
```

### CURL,
```bash
curl \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Basic BASE64_ENCODED(PUBLIC_KEY:PRIVATE_KEY)' \
  -H 'Braintree-Version: 2019-01-01' \
  -X POST https://payments.sandbox.braintree-api.com/graphql \
  -d '{
    "query": "mutation ExampleVaultSimple($input: VaultPaymentMethodInput!) { vaultPaymentMethod(input: $input) { paymentMethod { id usage details { __typename } } verification { status } } }",
    "variables": {
      "input": {
        "paymentMethodId": "id_of_single_use_payment_method"
      }
    }
  }'
```

### Response
```json
{
  "data": {
    "vaultPaymentMethod": {
      "paymentMethod": {
        "id": "id_of_multi_use_payment_method",
        "usage": "MULTI_USE",
        "details": {
          "__typename": "CreditCardDetails",
          "cardholderName": "Jane Q. Cardholder"
        }
      },
      "verification": {
        "status": "VERIFIED"
      }
    }
  }
}
```
or, if the payment method does not require a verification:


### Response
```json
{
  "data": {
    "vaultPaymentMethod": {
      "paymentMethod": {
        "id": "id_of_multi_use_payment_method",
        "usage": "MULTI_USE",
        "details": {
          "__typename": "PaypalAccountDetails",
          "payer": {
            "email": "emailfor@paypal.account"
          }
        }
      },
      "verification": null
    }
  }
}
```
See the [API Explorer](/braintree/graphql/explorer) for more possible payment method types and fields.

Braintree strongly recommends verifying all cards before they are stored in your Vault by[enabling card verification for your entire account](/braintree/articles/control-panel/vault/card-verification)in the Control Panel.


### Customers

If you want to group payment methods together in the Braintree API by individual customer, you can pass a customerId in the vault request. Once vaulted, a payment method cannot be transferred to a different customer, but the customer can be updated with new personal information. All payment methods belonging to a customer will be available on the paymentMethods connection field on the [Customer](/braintree/graphql/reference/#Object--Customer).

The default behavior when vaulting a payment method, without a customerId, is to create an empty customer associated with the newly-vaulted payment method. This can be ignored if unused, or updated later to hold relevant information.


### Error Handling

The only required parameter on input is paymentMethodId. Failing to supply this will result in an error.

If the vaulting mutation fails otherwise, it is most likely because:


- the[payment method verification failed](#payment-method-verification-failed)(for payment methods that require it)
- the[single-use payment method has already been consumed](#single-use-payment-method-is-consumed)
- the[single-use payment method has expired](#single-use-payment-method-has-expired)
- the[single-use payment method represents invalid payment information](#single-use-payment-method-represents-invalid-data)
- the[single-use payment method represents payment information that isn't vaultable](#single-use-payment-method-isnt-vaultable)

Depending on which error you receive, you will need to prompt your customer to re-enter or enter another payment method.


#### Payment Method Verification Failed

In order to mitigate fraudulent payment method usage, the [vaultPaymentMethod](/braintree/graphql/reference/#Mutation--vaultPaymentMethod) mutation will automatically run verifications against payment methods that support them (e.g. credit cards). You can control which merchant account to run the verification against using the verification.merchantAccountId input field.

If the verification fails or is declined, the payment method will not be stored in the vault. In this case, you will need to check the vaultPaymentMethod.verification response field to understand why the verification failed.

Here is an example response from a failed verification:


### JSON
```json
{
  "data": {
    "vaultPaymentMethod": {
      "paymentMethod": null,
      "verification": {
        "status": "PROCESSOR_DECLINED"
      }
    }
  },
  "errors": [
    {
      "message": "Payment method failed verification.",
      "path": [
        "vaultPaymentMethod",
        "paymentMethod"
      ],
      "extensions": {
        "errorClass": "VALIDATION",
        "inputPath": [
          "input",
          "paymentMethodId"
        ]
      }
    }
  ]
}
```
This response represents a GraphQL "partial failure", in which a failure to fetch one part of the response ( verifyCreditCard.paymentMethod ) doesn't affect the ability to fetch another ( verifyCreditCard.verification ). In this case, the errors entry is used to describe what happened to cause the verifyCreditCard.paymentMethod field to be null, while the data entry still contains useful information about the verification result in vaultPaymentMethod.verification.

There are certain cases where a single [vaultPaymentMethod](/braintree/graphql/reference/#Mutation--vaultPaymentMethod) request could result in multiple verifications (for example [$1 verification retries](/braintree/articles/control-panel/vault/card-verification#how-it-works) ). To fetch these results, refer to the vaultPaymentMethod.paymentMethod.verifications field, which returns all historical verifications run on the payment method. This field is represented as a paginated VerificationConnection, rather than a simple list. Read more about this type in our [Connections and Pagination](/braintree/graphql/guides/connections) guide.


#### Single-Use Payment Method is Consumed

The vaulting mutation could also fail if the paymentMethodId you provide has already been consumed. These IDs are single-use, so if you've already used it to create a transaction, for instance, you cannot vault it. Actions that consume a single-use payment method include charging, authorizing, capturing, and vaulting.


#### Single-Use Payment Method has Expired

Single-use payment methods expire after 3 hours. If it has been more than 3 hours since you [collected payment information](/braintree/graphql/guides/collecting_payment_information) to create a single-use payment method, you can no longer consume it.


#### Single-Use Payment Method Represents Invalid Data

When the payment information a single-use payment method represents is "not valid," the vaulting mutation will return a validation error.


#### Single-Use Payment Method Isn't Vaultable

In some cases, the single-use payment method represents payment information that is not vaultable. For example, when authorizing a PayPal account, the customer only grants permission to charge it once. In that case, you are not permitted to retain the information in your vault. Any calls to the vaulting mutation with such a single-use payment method will result in an error.


## Verify

Running a [Verification](/braintree/graphql/reference/#Object--Verification) checks whether a payment method has passed your fraud rules and the issuer has ensured it is associated with a valid account. When vaulting a credit card, by default, [vaultPaymentMethod](/braintree/graphql/reference/#Mutation--vaultPaymentMethod) will also verify that card before vaulting. If you need to verify a multi-use payment method, provide the [verifyPaymentMethod](/braintree/graphql/reference/#Mutation--verifyPaymentMethod) mutation with a payment method ID at the minimum.

### Mutation
```graphql
mutation VerifyPaymentMethod($input: VerifyPaymentMethodInput!) {
  verifyPaymentMethod(input: $input) {
    verification {
      id
      status
      merchantAccountId
      gatewayRejectionReason
      paymentMethod {
        id
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
    "verifyPaymentMethod": {
      "verification": {
        "id": "id_of_verification",
        "status": "VERIFIED",
        "merchantAccountId": "id_of_merchant_account",
        "gatewayRejectionReason": null,
        "paymentMethod": {
          "id": "id_of_payment_method"
        },
        "processorResponse": {
          "legacyCode": "legacy_code",
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

## Update

The GraphQL API supports updating specific properties on multi-use credit card payment methods. You can update the billing address, cardholder name, or expiration date using the following mutations:       [ updateCreditCardBillingAddress](https://developer.paypal.com/braintree/graphql/reference/#Mutation--updateCreditCardBillingAddress)

This mutation sets a new billing address for a multi-use credit card payment method. By default, this mutation will also verify the card with the latest billing address before updating.
### Mutation
```json
mutation UpdateCreditCardBillingAddress($input: UpdateCreditCardBillingAddressInput!) {
  updateCreditCardBillingAddress(input: $input) {
    billingAddress {
      addressLine1
      adminArea2
      adminArea1
    }
    paymentMethod {
      details {
        ... on CreditCardDetails {
          billingAddress {
            addressLine1
            adminArea2
            adminArea1
          }
        }
      }
    }
    verification {
      id
      status
      createdAt
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
      "paymentMethod": {
        "details": {
          "billingAddress": {
            "addressLine1": "123 Cantina",
            "adminArea2": "Mos Eisley",
            "adminArea1": "Tatooine"
          }
        }
      },
      "verification": {
        "id": "id_of_verification",
        "status": "VERIFIED",
        "createdAt": "2024-01-15T12:00:00Z"
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
[updateCreditCardCardholderName](https://developer.paypal.com/braintree/graphql/reference/#Mutation--updateCreditCardCardholderName) This mutation sets a new cardholder name for a multi-use credit card payment method. By default, this mutation will also verify the card with the new cardholder name before updating.
#### Mutation:


### Response
```json
mutation UpdateCreditCardCardholderName($input: UpdateCreditCardCardholderNameInput!) {
  updateCreditCardCardholderName(input: $input) {
    paymentMethod {
      details {
        ... on CreditCardDetails {
          cardholderName
        }
      }
    }
    verification {
      id
      status
      merchantAccountId
    }
  }
}
```

#### Variables:


### Response
```json
{
  "input": {
    "paymentMethodId": "id_of_payment_method",
    "cardholderName": "Han Solo"
  }
}
```

#### Response:


### Response
```json
{
  "data": {
    "updateCreditCardCardholderName": {
      "paymentMethod": {
        "details": {
          "cardholderName": "Han Solo"
        }
      },
      "verification": {
        "id": "id_of_verification",
        "status": "VERIFIED",
        "merchantAccountId": "your_merchant_account"
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
[updateCreditCardExpirationDate](https://developer.paypal.com/braintree/graphql/reference/#Mutation--updateCreditCardExpirationDate)Sets a new expiration date for a multi-use credit card payment method. By default, this mutation will also verify the card with the new expiration date before updating.


#### Mutation:

### Query
```graphql
mutation UpdateCreditCardExpirationDate(
  $input: UpdateCreditCardExpirationDateInput!
) {
  updateCreditCardExpirationDate(input: $input) {
    paymentMethod {
      details {
        ... on CreditCardDetails {
          expirationMonth
          expirationYear
        }
      }
    }
    verification {
      id
      status
      merchantAccountId
    }
  }
}

```


#### Variables:


### GraphQl
```json
{
  "input": {
    "paymentMethodId": "id_of_payment_method",
    "expirationMonth": "12",
    "expirationYear": "2030"
  }
}
```

#### Response:


### GraphQl
```json
{
  "data": {
    "updateCreditCardExpirationDate": {
      "paymentMethod": {
        "details": {
          "expirationMonth": "12",
          "expirationYear": "2030"
        }
      },
      "verification": {
        "id": "id_of_verification",
        "status": "VERIFIED",
        "merchantAccountId": "your_merchant_account"
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

## Skipping Verification

All three update mutations accept a verification input with a skip option if you want to update the credit card without performing a verification:


### GraphQl
```json
{
  "input": {
    "paymentMethodId": "id_of_payment_method",
    "cardholderName": "Han Solo",
    "verification": {
      "skip": true
    }
  }
}
```
When skip is set to true, the mutation will update the credit card property without verifying the card, and the verification field in the response will be null.


## Find

Use a [node query](/braintree/graphql/guides/node_query/) to fetch a payment method like as in a GET request:

### Query
```graphql
query PaymentMethod {
  node(id: "id_of_payment_method") {
    id
    ... on PaymentMethod {
      id
      legacyId
      usage
      createdAt
    }
  }
}

```


### Response
```json
{
  "data": {
    "node": {
      "id": "id_of_payment_method",
      "legacyId": "legacy_id_of_payment_method",
      "usage": "usage_of_payment_method",
      "createdAt": "created_at_date"
    },
    "extensions": {
      "requestId": "a-uuid-for-the-request"
    }
  }
}
```

## Search

Use the [search](/braintree/graphql/reference/#Query--search) query to search for a payment method using information on a [Customer](/braintree/graphql/reference/#Input--CustomerSearchInput) :

### Query
```graphql
query CustomerSearch($input: CustomerSearchInput!) {
  search {
    customers(input: $input) {
      edges {
        node {
          id
          paymentMethods {
            edges {
              node {
                id
                createdAt
                details {
                  ... on CreditCardDetails {
                    brandCode
                    last4
                    expirationMonth
                    expirationYear
                    cardholderName
                    uniqueNumberIdentifier
                  }
                }
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
    "id": {
      "is": "id_of_customer"
    }
  }
}
```

### Response
```json
{
  "data": {
    "search": {
      "customers": {
        "edges": [
          {
            "node": {
              "id": "id_of_customer",
              "paymentMethods": {
                "edges": [
                  {
                    "node": {
                      "id": "id_of_payment_method",
                      "createdAt": "created_at_date",
                      "details": {
                        "brandCode": "brand_code_of_credit_card",
                        "last4": "last_4_digits_of_an_account_number",
                        "expirationMonth": "MM",
                        "expirationYear": "YYYY",
                        "cardholderName": "name_of_cardholder",
                        "uniqueNumberIdentifier": null
                      }
                    }
                  }
                ]
              }
            }
          }
        ]
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
If the the customer can't be found, it will return an empty list of customers like so:


### Response
```json
{
  "data": {
    "search": {
      "customers": {
        "edges": []
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
The return value of this [search](/braintree/graphql/reference/#Query--search) query will be a [CustomerConnection](/braintree/graphql/reference/#Object--CustomerConnection).


## Delete

If your customer no longer wishes their payment method to be stored for future use, or you otherwise want to remove the multi-use payment method, use the [deletePaymentMethodFromVault](/braintree/graphql/reference/#Mutation--deletePaymentMethodFromVault) mutation. This is non-reversible; to store the same payment method again, you would need to obtain a new single-use payment method from the customer for it, and re-vault it, which would create a new multi-use payment method (with a new ID) representing the same underlying payment method.

### Mutation
```graphql
mutation DeletePaymentMethodFromVault(
  $input: DeletePaymentMethodFromVaultInput!
) {
  deletePaymentMethodFromVault(input: $input) {
    clientMutationId
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
    "deletePaymentMethodFromVault": {
      "clientMutationId": null
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
If the payment method can't be found, it will return an error stating "An object with this ID was not found."


### Deleting A Vaulted Venmo Account

If you use the [deletePaymentMethodFromVault](/braintree/graphql/reference/#Mutation--deletePaymentMethodFromVault) mutation to remove a multi-use Venmo payment method, it will also delete the Venmo customer's merchant connection within their Venmo app in "Connected Businesses". However, if your vault has duplicate Venmo payment methods for the same underlying customer Venmo account, the merchant connection will not be deleted until the last payment method is deleted.

Keep in mind that a Venmo customer can also delete a merchant connection from within their Venmo app at any time. This will automatically remove the Venmo payment method from your vault. You can be notified when this happens via the PaymentMethodRevokedByCustomer webhook; see the [Webhooks Guide](/braintree/docs/guides/webhooks/overview) for information on setting up webhooks outside of the GraphQL API.

