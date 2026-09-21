<!-- Source URL: https://developer.paypal.com/braintree/graphql/integration_guides/local_payment_contexts -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Local Payment Contexts
slug: /graphql/integration_guides/local_payment_contexts/
createTime: '2025-01-16T11:26:07.075Z'
updateTime: '2025-05-01T21:49:56.203Z'
---



# Local Payment Contexts


## Requirements


- To use this API, be sure to[create and link](/braintree/articles/guides/payment-methods/paypal/setup-guide)your PayPal account with login credentials to the Braintree control panel.


## Fetching Local Payment Contexts

To retrieve info about a Local Payment Context, you need its global ID. If you have an ID in a legacy UUID format, convert it first to its global format with a GraphQL query. See [Convert Legacy Id Query](#convert-legacy-id-query).

### Query
```graphql
query Node($id: ID!) {
  node(id: $id) {
    ... on LocalPaymentContext {
      id
      legacyId
      type
      amount {
        value
        currencyIsoCode
      }
      approvalUrl
      merchantAccountId
      transactedAt
      approvedAt
      createdAt
      updatedAt
      expiredAt
      paymentId
      orderId
    }
  }
}

```

{ "id": "ABCDEFG" }
### Response
```json
{
  "data": {
    "node": {
      "id": "cGF5bWVudGNvbnRleHRfvnNjOTQyYzJnd21xYjM2bSMxNmU1ZmQ5YS02NmJiLTRpNDktOWVkYy0yYTY3OTQ2OWEzZjQ",
      "legacyId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "type": "MULTIBANCO",
      "amount": {
        "value": "1.00",
        "currencyIsoCode": "EUR"
      },
      "approvalUrl": "https://example.com/approval",
      "merchantAccountId": "a_merchant_account_id",
      "transactedAt": null,
      "approvedAt": null,
      "createdAt": "2022-10-27T19:08:56.253000Z",
      "updatedAt": "2022-10-27T19:08:56.253000Z",
      "expiredAt": null,
      "paymentId": "a_payment_id",
      "orderId": "order-id-190619"
    }
  },
  "extensions": {
    "requestId": "abc-123-def-456"
  }
}
```
Error example when entity is not found.


### JSON
```json
{
  "errors": [
    {
      "message": "An object with this ID was not found.",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "node"
      ],
      "extensions": {
        "errorClass": "NOT_FOUND",
        "errorType": "developer_error"
      }
    }
  ],
  "data": {
    "node": null
  },
  "extensions": {
    "requestId": "eaa66dfb-34b9-4527-b8ac-900931bebf35"
  }
}
```

## Convert Legacy Id Query

The legacy ID has a format of UUID. To convert it to a graphql_id, use the following query. For Local Payment Contexts IDs, specify PAYMENT_CONTEXT as a [LegacyIdType](/braintree/graphql/reference/#Enum--LegacyIdType) of input. For more information please refer to [legacy vs. graphql ids](/braintree/graphql/guides/migrating/#legacy-vs-graphql-ids) page.


### GraphQL,
```graphql
query GetId($legacyId: ID!, $type: LegacyIdType!) {
  idFromLegacyId(legacyId: $legacyId, type: $type)
}

```

### Variables,
```json
{
  "legacyId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "type": "PAYMENT_CONTEXT"
}
```

### Response
```json
{
  "data": {
    "idFromLegacyId": "dHJhbnNhY3Rpb25fdnN4NXB5Mw"
  },
  "extensions": {
    "requestId": "S9mAxXwoOWeQ8GOZCVTxriMrNmcSWUeAByLYcBTyt-4iHC4G_kOgjQ=="
  }
}
```
