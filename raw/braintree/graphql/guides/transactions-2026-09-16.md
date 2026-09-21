<!-- Source URL: https://developer.paypal.com/braintree/graphql/guides/transactions -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Transactions
slug: /graphql/guides/transactions/
createTime: '2025-01-16T11:26:19.684Z'
updateTime: '2026-02-25T14:29:37.976Z'
---



# Transactions


## Creating Transactions

The GraphQL API currently supports two primary ways of creating transactions:


- The[chargePaymentMethod](/braintree/graphql/reference/#Mutation--chargePaymentMethod)mutation creates a transaction and captures funds immediately, beginning the[process](/braintree/articles/get-started/transaction-lifecycle)of actually[transferring money from the customer to your bank account](/braintree/articles/get-started/get-paid).
- [authorizePaymentMethod](/braintree/graphql/reference/#Mutation--authorizePaymentMethod)
- The[authorizePaymentMethod](/braintree/graphql/reference/#Mutation--authorizePaymentMethod)and[captureTransaction](/braintree/graphql/reference/#Mutation--captureTransaction)mutations create a transaction and capture funds separately.
- The[authorizePaymentMethod](/braintree/graphql/reference/#Mutation--authorizePaymentMethod)and[partialCaptureTransaction](/braintree/graphql/reference/#Mutation--partialCaptureTransaction)mutations create a transaction and capture the funds in multiple partial amounts. This is available for both PayPal and Venmo transactions.



Which you choose depends on your requirements. In most cases, you’ll want to submit a transaction for settlement at the same time that you authorize the payment by using [chargePaymentMethod](/braintree/graphql/reference/#Mutation--chargePaymentMethod).

However, there are some cases where you would want to create a transaction but not yet capture funds—for example, if you ship physical goods. In this case, you could use [authorizePaymentMethod](/braintree/graphql/reference/#Mutation--authorizePaymentMethod) at the time of the sale, which puts the money on hold against your customer's payment method, and then use [captureTransaction](/braintree/graphql/reference/#Mutation--captureTransaction) once the item has shipped.

For PayPal transactions, if you send physical goods to customers in multiple shipments, you can use [authorizePaymentMethod](/braintree/graphql/reference/#Mutation--authorizePaymentMethod) at the time of sale to create a parent authorization for the entire amount. As each shipment ships, you can capture that partial amount in a child transaction using [partialCaptureTransaction](/braintree/graphql/reference/#Mutation--partialCaptureTransaction) against the original authorization.


### Charging a Payment Method

In order to charge a payment method with [chargePaymentMethod](/braintree/graphql/reference/#Mutation--chargePaymentMethod), you'll need a payment method's ID, and information about the transaction you'd like to create using it.

If you charge a single-use payment method, this will consume it and you will no longer be able to look up, charge, or vault that payment method.

### Mutation
```graphql
mutation ExampleCharge($input: ChargePaymentMethodInput!) {
  chargePaymentMethod(input: $input) {
    transaction {
      id
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
      "amount": "11.23"
    }
  }
}
```
To plug this mutation into a curl request, compose the query and variables into a JSON-valid string and send it in the request body. For example:


### CURL
```graphql
curl -X POST https://payments.sandbox.braintree-api.com/graphql \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Basic BASE64_ENCODED(PUBLIC_KEY:PRIVATE_KEY)' \
  -H 'Braintree-Version: 2019-01-01' \
  -d '{
    "query": "mutation ExampleCharge($input: ChargePaymentMethodInput!) { chargePaymentMethod(input: $input) { transaction { id status } } }",
    "variables": {
      "input": {
        "paymentMethodId": "id_of_payment_method",
        "transaction": {
          "amount": "11.23"
        }
      }
    }
  }'
```
There are many more possible fields you can use in the input or request in the output; see the [API Explorer](/braintree/graphql/explorer) for more.

A successful charge results in a transaction with the [SUBMITTED_FOR_SETTLEMENT](/braintree/docs/reference/general/statuses#submitted-for-settlement) or [SETTLING](/braintree/docs/reference/general/statuses/#settling) status:


### Response
```json
{
  "data": {
    "transaction": {
      "id": "id_of_transaction",
      "status": "SUBMITTED_FOR_SETTLEMENT"
    }
  }
}
```

### Using Separate Authorization and Capture

If you require a [separate authorization step](/braintree/articles/get-started/transaction-lifecycle#authorized) before charging the payment method [to actually capture funds](/braintree/articles/get-started/transaction-lifecycle#submitted-for-settlement), the GraphQL API provides the [authorizePaymentMethod](/braintree/graphql/reference/#Mutation--authorizePaymentMethod) and [captureTransaction](/braintree/graphql/reference/#Mutation--captureTransaction) mutations.

### Mutation
```graphql
mutation ExampleAuth($input: AuthorizePaymentMethodInput!) {
  authorizePaymentMethod(input: $input) {
    transaction {
      id
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
      "amount": "11.23"
    }
  }
}
```
A successful authorization results in a transaction with the [AUTHORIZED](/braintree/docs/reference/general/statuses#authorized) status:


### Response
```json
{
  "data": {
    "transaction": {
      "id": "id_of_authorized_transaction",
      "status": "AUTHORIZED"
    }
  }
}
```
Once you have authorized your payment method and are ready to capture funds, you should use the [captureTransaction](/braintree/graphql/reference/#Mutation--captureTransaction) mutation. This mutation only requires the ID of the transaction that you'd like to capture.

You have a [limited number of days to capture a transaction once it has been authorized](/braintree/docs/reference/general/statuses#authorization-expired).

### Mutation
```graphql
mutation ExampleCapture($input: CaptureTransactionInput!) {
  captureTransaction(input: $input) {
    transaction {
      id
      status
    }
  }
}

```


### Variables
```json
{
  "input": {
    "transactionId": "id_of_authorized_transaction"
  }
}
```
A successful charge results in a transaction with the [SUBMITTED_FOR_SETTLEMENT](/braintree/docs/reference/general/statuses#submitted-for-settlement) status:


### Response
```json
{
  "data": {
    "transaction": {
      "id": "id_of_authorized_transaction",
      "status": "SUBMITTED_FOR_SETTLEMENT"
    }
  }
}
```

### Using Multiple Partial Capture

This mutation is available for PayPal transactions.

To capture a transaction in multiple parts:


- Authorize the entire order amount with either of the[authorizePaymentMethod](/braintree/graphql/reference/#Mutation--authorizePaymentMethod)or[authorizePayPalAccount](/braintree/graphql/reference/#Mutation--authorizePayPalAccount)mutations.
- Make a separate call to the[partialCaptureTransaction](/braintree/graphql/reference/#Mutation--partialCaptureTransaction)mutation for each amount you want to capture separately. In each call, specify the ID of the parent authorized transaction and the amount you wish to capture.

Once you have authorized the payment method as outlined in [Using Separate Authorization and Capture](#using-separate-authorization-and-capture), you can partially capture funds with the [partialCaptureTransaction](/braintree/graphql/reference/#Mutation--partialCaptureTransaction) mutation. This mutation requires the amount you want to collect as well as the ID of the authorized transaction.

### Mutation
```graphql
mutation ExamplePartialCapture($input: PartialCaptureTransactionInput!) {
  partialCaptureTransaction(input: $input) {
    capture {
      id
      status
    }
  }
}

```


### Variables
```json
{
  "input": {
    "transactionId": "id_of_authorized_transaction",
    "transaction": {
      "amount": "5.45"
    }
  }
}
```
The mutation is successful if the resulting partial capture transaction is in the [SETTLING](/braintree/docs/reference/general/statuses#settling), [SUBMITTED_FOR_SETTLEMENT](/braintree/docs/reference/general/statuses#submitted-for-settlement), or [SETTLED](/braintree/docs/reference/general/statuses#settled) state. The parent transaction will have a status of [SETTLEMENT_PENDING](/braintree/docs/reference/general/statuses#settlement-pending).


### Response
```json
{
  "data": {
    "capture": {
      "id": "id_of_child_transaction",
      "status": "SETTLING"
    }
  }
}
```
For more information about the lifecycle of partial capture transactions, see our full guide on [multiple partial capture](/braintree/docs/reference/request/transaction/submit-for-partial-settlement/ruby).

After charging a payment method, you may want to store the ID of the resulting transaction in your database for future reference, either for presenting back in the UI at a later time, or for your own internal book-keeping, analysis, or reporting requirements. You can retrieve this transaction by its ID using the [node query](/braintree/graphql/guides/node_query).


### Transaction Statuses

Even if the [chargePaymentMethod](/braintree/graphql/reference/#Mutation--chargePaymentMethod) or [authorizePaymentMethod](/braintree/graphql/reference/#Mutation--authorizePaymentMethod) mutation doesn't return any errors, the transaction may not have been created successfully. For instance, the customer's card-issuing bank may have declined the authorization, or your fraud protection settings may have blocked it. In this case, the [Transaction](/braintree/graphql/reference/#Object--Transaction) will have a failure status, such as Processor Declined or Gateway Rejected, and further information on what caused the failure. You can then use this to decide how to handle the failure and how to report it back to your customer.

A successful transaction will be updated over time as funds are debited from the customer and sent to you. As money moves, the transaction passes through multiple states in the payment lifecycle, most typically from Authorized to Submitted for Settlement, to Settling, to Settled. For detailed information on what these statuses mean, see [the Transaction Lifecycle](/braintree/articles/get-started/transaction-lifecycle).

Using the [complete list of transaction statuses and their meanings](/braintree/docs/reference/general/statuses#transaction), you can check the [status](/braintree/graphql/reference/#Enum--PaymentStatus) of a transaction to determine if it was successful or unsuccessful and why, and if successful, what will happen to the transaction next. [This simplified status diagram](https://paypalobjects.com/btdevdoc/braintree/img/developers/flow_processing-workflow.png) shows what happens to a transaction if it succeeds or fails various validations.


### Error Handling

Unsuccessful transactions are a normal part of transaction processing and should not be considered exceptional. If an error occurs, you will either not receive a transaction object on the payload, or you will receive only a partial object.

Here's an example of an error on a transaction.


### JSON
```json
{
  "data": {
    "chargePaymentMethod": null
  },
  "errors": [
    {
      "message": "Amount must be greater than zero.",
      "path": [
        "chargePaymentMethod"
      ],
      "extensions": {
        "errorType": "user_error",
        "errorClass": "VALIDATION",
        "legacyCode": "81531",
        "inputPath": [
          "input",
          "transaction",
          "amount"
        ]
      }
    }
  ],
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
See more details on handling errors in [Making API Calls](/braintree/graphql/guides/making_api_calls#errors).


## Reversing or Refunding a Transaction

Once you've charged a payment method, you might want to cancel the transaction or refund the customer their money later. We will provide instructions here for the various ways you can "undo" a charge.

To attempt to completely reverse a transaction, regardless of its present settlement status, you may use the [reverseTransaction](/braintree/graphql/reference/#Mutation--reverseTransaction) mutation. When using this mutation, we will either void the transaction or issue a refund for the full amount of the transaction.

**Voiding** the transaction cancels it, preventing funds from being debited from the customer's account. A **refund** occurs when you have received or are in the process of receiving funds from a transaction already, and you would like to debit the full or partial amount of money from your own account to send back to the customer.


### Reversing a Transaction

To reverse a transaction, you only need the ID of the Transaction. Depending on the settlement status at the time of the attempted reversal, the result of the reverseTransaction mutation will either be a Transaction updated to the VOIDED status, or a new Refund linked to the original transaction. If you are interested in only partially refunding a transaction or wish to provide an orderId, use the refundTransaction mutation directly instead.

### Mutation
```graphql
mutation ExampleReverse($input: ReverseTransactionInput!) {
  reverseTransaction(input: $input) {
    reversal {
      ... on Transaction {
        id
        status
        statusHistory {
          status
          terminal
        }
      }
      ... on Refund {
        id
        amount {
          value
        }
        orderId
        status
        refundedTransaction {
          id
          amount {
            value
          }
          orderId
          status
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
    "transactionId": "TRANSACTION_ID"
  }
}
```

### Response
```json
{
  "data": {
    "reverseTransaction": {
      "reversal": {
        "id": "TRANSACTION_ID",
        "status": "VOIDED",
        "statusHistory": [
          {
            "status": "VOIDED",
            "terminal": "true"
          },
          {
            "status": "SUBMITTED_FOR_SETTLEMENT",
            "terminal": "false"
          },
          {
            "status": "AUTHORIZED",
            "terminal": "false"
          }
        ]
      }
    }
  }
}
```
or


### Response
```json
{
  "data": {
    "reverseTransaction": {
      "reversal": {
        "id": "REFUND_ID",
        "amount": {
          "value": "10.00"
        },
        "orderId": "original-charge-order-id-123",
        "status": "SUBMITTED_FOR_SETTLEMENT",
        "refundedTransaction": {
          "id": "TRANSACTION_ID",
          "amount": {
            "value": "10.00"
          },
          "orderId": "original-charge-order-id-123",
          "status": "SETTLED"
        }
      }
    }
  }
}
```

### Refunding a Transaction

If you already know the transaction has been SETTLED, or you want to partially refund it, or you need to provide a refund order ID, you can use the refundTransaction mutation.

You'll need the ID for the Transaction that needs to be refunded. It must meet the following criteria to be refundable:


- in either theSETTLINGorSETTLEDstatus
- has not already been fully refunded

By default, refundTransaction will fully refund a transaction. You can pass in an amount less than the original amount in order to partially refund it. You can also optionally specify an orderId to give the refund its own unique order ID, instead of the default behavior, which is inheriting the order ID from the original transaction.

### Mutation
```graphql
mutation ExampleRefund($input: RefundTransactionInput!) {
  refundTransaction(input: $input) {
    refund {
      id
      amount {
        value
      }
      orderId
      status
      refundedTransaction {
        id
        amount {
          value
        }
        orderId
        status
      }
    }
  }
}

```


### Variables
```json
{
  "input": {
    "transactionId": "SETTLED_TRANSACTION_ID",
    "refund": {
      "amount": "7.00",
      "orderId": "refund-order-id-456"
    }
  }
}
```
A successful refund results in a new Refund object:


### Response
```json
{
  "data": {
    "refundTransction": {
      "refund": {
        "id": "REFUND_ID",
        "amount": {
          "value": "7.00"
        },
        "orderId": "refund-order-id-456",
        "status": "SUBMITTED_FOR_SETTLEMENT",
        "refundedTransaction": {
          "id": "TRANSACTION_ID",
          "amount": {
            "value": "10.00"
          },
          "orderId": "original-charge-order-id-123",
          "status": "SETTLED"
        }
      }
    }
  }
}
```
Or, a refund can fail because the original transaction wasn't ready to refund or had already been refunded. For example:


### JSON
```json
{
  "data": null,
  "errors": [
    {
      "message": "Transaction has already been completely refunded.",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "refundTransaction"
      ],
      "extensions": {
        "errorType": "user_error",
        "errorClass": "VALIDATION",
        "legacyCode": "91512",
        "inputPath": [
          "input",
          "transactionId"
        ]
      }
    }
  ]
}
```

### Voiding a Transaction

Use [voidTransaction](https://developer.paypal.com/braintree/graphql/reference/#Mutation--voidTransaction) to cancel a transaction before it is settled. If a payment has been authorized or submitted for settlement but has not yet completed settlement, you can void it to stop the capture of funds. The money is never transferred to the merchant, and no refund is needed because the transaction was not completed.


#### Sample request


### Response
```json
mutation VoidTransaction($input: VoidTransactionInput!) {
  voidTransaction(input: $input) {
    transaction {
      id
      status
      amount {
        value
        currencyCode
      }
    }
    clientMutationId
    errors {
      field
      message
      code
    }
  }
}
```

#### Variables


### Response
```json
{
  "input": {
    "transactionId": "dHJhbnNhY3Rpb25faWQ=",
    "clientMutationId": "void-transaction-123"
  }
}
```

#### Sample responses


##### Success


### Response
```json
{
  "data": {
    "voidTransaction": {
      "transaction": {
        "id": "dHJhbnNhY3Rpb25faWQ=",
        "status": "VOIDED",
        "amount": {
          "value": "100.00",
          "currencyCode": "USD"
        }
      },
      "clientMutationId": "void-transaction-123",
      "errors": []
    }
  }
}
```

#### Error scenarios


##### Invalid transaction ID


### Response
```json
{
  "data": {
    "voidTransaction": {
      "transaction": null,
      "clientMutationId": "void-transaction-123",
      "errors": [
        {
          "field": "transactionId",
          "message": "Invalid transaction ID provided",
          "code": "INVALID_INPUT_FOR_VOID_TRANSACTION_MUTATION"
        }
      ]
    }
  }
}

```

##### Transaction Not Found


### Response
```json
{
  "data": {
    "voidTransaction": {
      "transaction": null,
      "clientMutationId": "void-transaction-123",
      "errors": [
        {
          "field": "transactionId",
          "message": "Transaction not found",
          "code": "TRANSACTION_NOT_FOUND"
        }
      ]
    }
  }
}
```

##### Transaction Cannot Be Voided


### Response
```json
{
  "data": {
    "voidTransaction": {
      "transaction": null,
      "clientMutationId": "void-transaction-123",
      "errors": [
        {
          "field": "transactionId",
          "message": "Transaction cannot be voided in its current state",
          "code": "TRANSACTION_CANNOT_BE_VOIDED"
        }
      ]
    }
  }
}
```

##### Authorization Error


### Response
```json
{
  "errors": [
    {
      "message": "Unauthorized access",
      "extensions": {
        "code": "UNAUTHORIZED"
      }
    }
  ]
}
```

### Reversing Refunds

If you want to reverse a previously issued refund, you can use the [reverseRefund](/braintree/graphql/reference/#Mutation--reverseRefund) mutation:

### Mutation
```graphql
mutation ReverseRefund($input: ReverseRefundInput!) {
  reverseRefund(input: $input) {
    refund {
      id
      createdAt
      amount {
        value
        currencyCode
      }
      status
      source
      refundedTransaction {
        id
      }
    }
  }
}

```


### Variables
```json
{
  "input": {
    "refundId": "id_of_refund"
  }
}
```

### Response
```json
{
  "data": {
    "reverseRefund": {
      "refund": {
        "id": "id_of_refund",
        "createdAt": "created_at_date",
        "amount": {
          "value": "10.00",
          "currencyCode": "USD"
        },
        "status": "VOIDED",
        "source": "API",
        "refundedTransaction": {
          "id": "id_of_refunded_transaction"
        }
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
| Mutation | Function | When to Use |
| --- | --- | --- |
| voidTransaction | Voids a transaction if it’s notSETTLED. | If you already know the transaction has**NOT**beenSETTLED. |
| refundTransaction | Refunds a transaction if it’sSETTLED. | If you already know the transaction has beenSETTLED, or you want to partially refund it, or you need to provide a refund order ID. |
| reverseTransaction | Refunds a transaction if it’sSETTLED, OR Voids a transaction if it’s notSETTLED. | When you’re not sure about the transaction status. |


### Detached Refunds

If you need to create a [detached refund](/braintree/articles/control-panel/transactions/refunds-voids-credits#detached-credits) (unassociated with any previous Braintree payment), you can do so using the [refundCreditCard](/braintree/graphql/reference/#Mutation--refundCreditCard) and [refundUsBankAccount](/braintree/graphql/reference/#Mutation--refundUsBankAccount) mutations:

### Mutation
```graphql
mutation ($input: RefundCreditCardInput!) {
  refundCreditCard(input: $input) {
    clientMutationId
    refund {
      id
      status
      amount {
        value
      }
      orderId
      merchantAccountId
      source
      refundedTransaction {
        id
      }
      paymentMethod {
        id
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
    "refund": {
      "amount": "10.00"
    }
  }
}
```

### Response
```json
{
  "data": {
    "refundCreditCardInput": {
      "clientMutationId": "id_of_client_mutation",
      "refund": {
        "id": "id_of_refund",
        "status": "SUBMITTED_FOR_SETTLEMENT",
        "amount": {
          "value": "10.00"
        },
        "orderId": "id_of_order",
        "merchantAccountId": "id_of_merchant_account",
        "source": "API",
        "refundedTransaction": {
          "id": "id_of_refunded_transaction"
        },
        "paymentMethod": {
          "id": "id_of_payment_method"
        }
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

## Searching For Transactions

There are two ways to query for specific information on transactions:


- [Using the search query](#search-query)
- [Fetching the transaction by its ID using a node query](#node-query)


### Search Query

The following is an example of using the [search](/braintree/graphql/reference/#Query--search) query to find transactions that fit certain criteria:


- The fields available to search on are on the[TransactionSearchInput](/braintree/graphql/reference/#Input--TransactionSearchInput)object
- The fields available on the returned transactions are on the[TransactionConnection](/braintree/graphql/reference/#Object--TransactionConnection)object.

### Query
```graphql
query ($input: TransactionSearchInput!) {
  search {
    transactions(input: $input) {
      edges {
        node {
          id
          status
          amount {
            value
            currencyCode
          }
          merchantId
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
      "is": "id_of_transaction"
    },
    "status": {
      "is": "status_of_transaction"
    },
    "amount": {
      "value": {
        "is": "value_of_transaction"
      }
    }
  }
}
```

### Response
```json
{
  "data": {
    "search": {
      "transactions": {
        "edges": [
          {
            "node": {
              "id": "id_of_transaction",
              "status": "status_of_transaction",
              "amount": {
                "value": "value_of_transaction",
                "currencyCode": "currency_code_of_transaction"
              },
              "merchantId": "id_of_merchant"
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

### Node Query

You can also use a [node query](/braintree/graphql/guides/node_query/) to perform a GET request to retrieve a transaction by its ID:


### GraphQL
```graphql
 node(id: "id_of_transaction") { ... on Transaction
    { 
      status paymentMethod 
    { 
      id details 
    {
      __typename }
    }
  }
} 
```

### Response
```json
{
  "data": {
    "node": {
      "status": "status_of_transaction",
      "paymentMethod": {
        "id": "id_of_transaction",
        "details": {
          "__typename": "type_name_of_transaction"
        }
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
