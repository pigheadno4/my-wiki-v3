<!-- Source URL: https://developer.paypal.com/braintree/graphql/guides/migrating -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Migrating from a Server SDK Integration
slug: /graphql/guides/migrating/
createTime: '2025-01-16T11:26:42.995Z'
updateTime: '2025-04-30T11:23:55.319Z'
---



# Migrating from a Server SDK Integration

The GraphQL API uses a different format for IDs than in previous Braintree APIs.

If you plan to migrate an existing [SDK integration](/braintree/docs/start/overview#key-concepts) to an integration with the GraphQL API, you will also need to migrate from using Braintree legacy IDs to using GraphQL IDs. This guide details a typical migration path to achieve this.


## Legacy vs. GraphQL IDs

Legacy IDs refer to the IDs currently accepted and returned by the Braintree SDKs. GraphQL IDs represent the same entities in the Braintree system, but include more information about the entity that make the GraphQL API more powerful. For example, instances of different domain objects may have the same legacy ID (e.g. a Transaction and a PaymentMethod may share an ID). GraphQL IDs are unique across all domains.

Types that implement the Node interface in the GraphQL API contain a legacyId field for the purposes of migrating from those legacy IDs to the GraphQL IDs. We also provide a query, idFromLegacyId, for translating a legacy ID to a GraphQL ID.


## Migrating an Integration to Use the Braintree GraphQL API


- Update your database schema to store an additional "GraphQL ID" field alongside any ID fields that you currently store from Braintree. For example, if you have atransactionstable with anidfield, you should add a column or field namedgraphql_id.
- Build your[Braintree GraphQL Integration](/braintree/graphql/guides/).
- When reading an ID from your database, prefer to read thegraphql_idinstead ofid.
- If thegraphql_idis not set in your database, translate youridto a GraphQL ID. You can either use theidFromLegacyIdquery to convert IDs, or read thegraphql_idfield on supported objects in the legacy SDK integration. Store this id asgraphql_idin your database, and use it when providingidin any GraphQL mutation or query.


- Always request both theidandlegacyIdin your API requests and dual-write these IDs in your local database. This will give you the flexibility to seamlessly switch back to your SDK integration, should the need arise.
- After you successfully launch your Braintree GraphQL API integration, you can back-fill your legacy IDs with GraphQL IDs using theidFromLegacyIdquery.
- Once your GraphQL integration is stable, you can stop requesting and writing thelegacyId. From now on, use only the GraphQL IDs from your new integration.


### Reading thegraphql_idField

The server-side SDKs include a graphql_id field on the [CreditCardVerification](/braintree/docs/reference/response/credit-card-verification#graphql_id), [Customer](/braintree/docs/reference/response/customer#graphql_id), [Dispute](/braintree/docs/reference/response/dispute#graphql_id), and [Transaction](/braintree/docs/reference/response/transaction#graphql_id) objects. This value is already translated and must not be translated using the idFromLegacyId query.


### Using theidFromLegacyIdQuery

The idFromLegacyId query takes a legacy ID and the object type and returns its GraphQL ID, for use in the GraphQL API.


### GraphQL
```graphql
query IdFromLegacyId($legacyId: ID!, $type: LegacyIdType!) {
  idFromLegacyId(legacyId: $legacyId, type: $type)
}

```

### Variables
```json
{
  "legacyId": "vsx5py3",
  "type": "TRANSACTION"
}
```

### Response
```json
{
  "data": { "idFromLegacyId": "dHJhbnNhY3Rpb25fdnN4NXB5Mw" },
  "extensions": {
    "requestId": "S9mAxXwoOWeQ8GOZCVTxriMrNmcSWUeAByLYcBTyt-4iHC4G_kOgjQ=="
  }
}

```



### GraphQL ID Format

In order to avoid interruptions in processing, it's best to make minimal assumptions about what GraphQL IDs will look like in the future. The format of the GraphQL ID is not a contract. While any given ID will never change, the new IDs may follow a different format in the future.

The length and format of these identifiers – including payment method tokens and transaction IDs – can change at any time, with or without advance notice. However, it is safe to assume that they will remain 1 to 256 characters (alphanumeric, dashes, and underscores).


## API concepts vs. SDK concepts

Some key terms and modeling differ between the API and SDKs.


### Nonces vs. single-use payment methods

The SDKs distinguish between nonces (single-use payment data collected from the client) and payment methods (vaulted payment data that may be re-used).

The API refers all payment data as a payment methods. Payment methods can be single-use (the equivalent of a nonce in the SDK) or multi-use (the equivalent of a vaulted payment method in the SDK). The usage field on a payment method indicates whether it is single- or multi-use.

| SDK | API |
| --- | --- |
| nonce | single-use payment method |
| payment method | multi-use payment method |


### Creating transactions

In the SDKs, the sale method authorizes a payment method and optionally captures the transaction via the submit_for_settlement flag. The API provides mutations to authorize or charge payment methods, which return transactions. It also provides mutations for capturing authorized transactions.

Here is an example of a sale transaction in the Ruby SDK:

Ruby SDK```language-ruby
result = gateway.transaction.sale( :amount =&gt; "10.00", :payment_method_nonce =&gt; nonce_from_the_client, :options =&gt; { :submit_for_settlement =&gt; true }
)
```

### GraphQL
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
    "paymentMethodId": "nonce_from_the_client",
    "transaction": { "amount": "10.00" }
  }
}

```



### Accepting payment data directly

Note this guidance is only relevant to merchants who are in PCI scope and handle raw payment details.

The SDKs allow raw credit card details as input to sale and vault requests. The API only accepts raw payment details via the tokenization mutations. To charge or vault credit card details directly, tokenize and then use the resulting payment method in a vault or charge mutation.

