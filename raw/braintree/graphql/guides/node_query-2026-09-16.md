<!-- Source URL: https://developer.paypal.com/braintree/graphql/guides/node_query -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Fetching Objects via the Node Query
slug: /graphql/guides/node_query/
createTime: '2025-01-16T11:25:36.363Z'
updateTime: '2025-04-30T10:46:56.891Z'
---



# Finding Objects with Node Query

In the GraphQL specification, the node query is a query that takes only an ID and returns the object corresponding to that ID. In a REST API, this is similar to a GET request that fetches an object by ID, but with an important difference: the node query does not require the type of that object to be specified.

An object type is fetchable by the node query as long as it implements the node interface and uses global IDs. A global ID specifies a given instance of a type uniquely across all objects of all types that implement node. This is how we are able to fetch an object in the node query without knowing its type.

You can see which types in our schema implement node by using the following introspection query:


### GraphQL,
```graphql
 __type(name: "Node") {
     possibleTypes {
         name description 
         } 
    } 
```
In our API, the following types implement the node interface:


- Transaction
- PaymentMethod
- Refund
- Customer
- Verification

In a REST API, you might expect to fetch a transaction with ID THE_TRANSACTION_ID by sending a GET request to an endpoint like /transactions/THE_TRANSACTION_ID. In a GraphQL API, this endpoint (and all other type-specific endpoints like it) are replaced by the node query. The equivalent query in GraphQL would be:


### GraphQL,
```graphql
 node(id: "THE_TRANSACTION_ID") { 
    ... on Transaction {
         status 
         } 
    } 
```
Note that the request expects a transaction fragment in the response. If you were fetching a refund, you would use a refund fragment:


### GraphQL,
```graphql
 node(id: "THE_REFUND_ID") {
    ... on Refund {
         status 
         } 
    } 
```
Say you have the ID of an object that may either be a refund or a transaction. You should include both type fragments:


### GraphQL,
```graphql
 node(id: "TRANSACTION_OR_REFUND_ID") {
     ... on Transaction { 
        status 
        } 
    ... on Refund {
         status 
         } 
    } 
```

## Fetching Transactions

After [creating a transaction](/braintree/graphql/guides/transactions#creating-transactions), you can save its ID to look up at a later time using the node query.


### GraphQL
```graphql
 node(id: "id_of_transaction") { 
    ... on Transaction { 
        status paymentMethod {
         id details { __typename 
         }
     } 
    } 
}
```

### Response
```json
{
  "data": {
    "node": {
      "status": "SUBMITTED_FOR_SETTLEMENT",
      "paymentMethod": {
        "id": "id_of_transaction",
        "details": {
          "__typename": "CreditCardTransactionDetails"
        }
      }
    }
  },
  "extensions": {
    "requestId": "cf78db46-a44d-4394-90f5-e5af86243517"
  }
}
```
