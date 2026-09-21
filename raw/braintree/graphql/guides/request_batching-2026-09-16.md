<!-- Source URL: https://developer.paypal.com/braintree/graphql/guides/request_batching -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: GraphQL Request Batching
slug: /graphql/guides/request_batching/
createTime: '2025-01-16T11:26:09.365Z'
updateTime: '2025-01-16T11:26:09.508Z'
---



# GraphQL Request Batching

We are working on an "extension" of GraphQL at Braintree to allow clients to execute a series of GraphQL queries in a single HTTP request, and optionally share variables between them. "Extension" is in quotes because this feature is intended to maintain full compliance with the GraphQL spec, which is intentionally vague around request/response transport format. We will go straight into examples here, but feel free to jump to [the end](#motivation) for more details on the motivation behind the feature.

Here is a basic example using the Ruby http gem:

```language-ruby
HTTP .basic_auth( user: "my_public_key", pass: "my_private_key" ) .headers( content_type: "application/vnd+braintree.graphql.batch.v0+json", braintree_version: "2020-05-06" ) .post( "https://payments.sandbox.braintree-api.com/graphql", json: [ { query: 'mutation Tokenize($input: TokenizeCreditCardInput!) { tokenizeCreditCard(input: $input) { paymentMethod { id @export(as: "tokenizedId") usage } } }', variables: { input: { creditCard: { number: "4111111111111111", expirationYear: "2020", expirationMonth: "12" } } } }, { query: 'mutation Vault($tokenizedId: ID!) { vaultPaymentMethod(input: {paymentMethodId: $tokenizedId}) { paymentMethod { id usage } } }' } ] )
```
At a high level, this example performs two GraphQL mutations in a single HTTP request to the Braintree API. The first mutation is tokenizeCreditCard, which exchanges credit card details for a single-use payment method, and the second is vaultPaymentMethod, which converts the single-use payment method from the previous step into a multi-use (vaulted) payment method. Let's break down the pieces.

.basic_auth(...) sets the authentication for the entire request. In this case, we use our public/private key pair.

.headers(...) is where things start to diverge from a typical GraphQL request. Specifically, notice the content_type header: application/vnd+braintree.graphql.batch.v0+json. This is a custom media type that is required in order to opt-in to this feature. Without it, we will assume you are trying to make a regular GraphQL request, and fail due to invalid syntax.

.post(...) sends the request to the Braintree Sandbox GraphQL URL, with a JSON request body represented as a Ruby array. Each object in this array corresponds to the GraphQL request payload you are used to: i.e. a query entry that contains the GraphQL query as a string, and an optional variables entry that contains a JSON object representing variables referenced by the query.

One thing you may notice is that the second query, vaultPaymentMethod declares a variable $tokenizedId: ID! which is not present in the variables object for that query. In fact, the second query doesn't specify any variables at all. The reason this works is because of the @export directive in the first query, which propagates variables to subsequent queries behind the scenes.

@export is a GraphQL [query directive](https://graphql.org/learn/queries/#directives) which accepts a single argument as of type String!. In this case, we've passed "tokenizedId" to indicate we want the result of the field id to be available as $tokenizedId to subsequent queries, provided they declare the variable first. For instance, the vaultPaymentMethod mutation declares the variable on its first line: mutation Vault($tokenizedId: ID!), and then references it with vaultPaymentMethod(input: {paymentMethodId: $tokenizedId}).


## Responses

Just as the request is a list of regular GraphQL request payloads, the response is a list of regular GraphQL response payloads, in the same order. For instance, if everything goes well, the above request would return something like this:

```language-json
[ { "data": { "tokenizeCreditCard": { "paymentMethod": { "id": "tokencc_ab_123abc_456def_789ghi_123abc_abc", "usage": "SINGLE_USE" } } }, "extensions": { "exportedVariables": { "tokenizedId": "tokencc_ab_123abc_456def_789ghi_123abc_abc" }, "requestId": "0c532285-b668-4e74-9c08-44577219835f" } }, { "data": { "vaultPaymentMethod": { "paymentMethod": { "id": "cGF5bWVudG1ldGhvZF9jY19hYmMxMjM0Cg==", "usage": "MULTI_USE" } } }, "extensions": { "exportedVariables": { "tokenizedId": "tokencc_ab_123abc_456def_789ghi_123abc_abc" }, "requestId": "0c532285-b668-4e74-9c08-44577219835f" } }
]
```
Each member of this list is a typical GraphQL response payload, which is a JSON object including data, extensions, and optionally errors. The data entry includes all the fields we selected in the corresponding query, in this case paymentMethod.id and paymentMethod.usage. The extensions entry includes the Braintree standard requestId (which is shared between all responses in the list), but also an entry called exportedVariables. This entry contains a snapshot of all variables exported since the beginning of the request until this particular query was resolved, and can be useful for debugging purposes.

Errors follow the same pattern as data. If a query in the list results in errors, those errors will be represented in the errors entry in the corresponding response payload. The important thing to note here is that, if an exported field can't be resolved due to errors, then it is never added to the exportedVariables object, and subsequent queries behave as if the variable was never passed. For instance, if we had passed an invalid expirationYear in the tokenizeCreditCard request, our response would look more like this:

```language-json
[ { "errors": [ { "message": "Expiration year is invalid", "locations": [{"line": 2, "column": 3}], "path": ["tokenizeCreditCard"], "extensions": { "errorClass": "VALIDATION", "legacyCode": "81713", "inputPath": ["input", "creditCard", "expirationYear"] } } ], "data": { "tokenizeCreditCard": null }, "extensions": { "exportedVariables": {}, "requestId": "0c532285-b668-4e74-9c08-44577219835f" } }, { "errors": [ { "message": "Variable 'tokenizedId' has coerced Null value for NonNull type 'ID!'", "locations": [{"line": 1, "column": 29}] } ], "extensions": { "exportedVariables": {}, "requestId": "0c532285-b668-4e74-9c08-44577219835f" } }
]
```
The first query failed with a VALIDATION class error, and consequently never got a chance to resolve the exported paymentMethod.id field. As a result, it was never added to the next query's variables object, causing the generic GraphQL failure Variable 'tokenizedId' has coerced Null value for NonNull type 'ID!'.


## When to use Request Batching

Request batching should only be used in specific scenarios, namely when you need to mix mutations and queries in a single request, and/or when you need to pass variables from one to the other. If you simply want to perform multiple independent mutations or queries in a single request, GraphQL already supports that. For instance, this is a valid query:

### Query
```graphql
query MultiQuery {
  ping
  viewer {
    id
  }
}

```

This will perform ping and viewer  in parallel. Similarly, the following is a valid mutation:

### Mutation
```graphql
mutation MultiMutation(
  $customerInput: CreateCustomerInput!
  $tokenizeInput: TokenizeCreditCardInput!
) {
  createCustomer(input: $customerInput) {
    customer {
      id
    }
  }
  tokenizeCreditCard(input: $tokenizeInput) {
    paymentMethod {
      id
    }
  }
}

```

This will perform createCustomer and tokenizeCreditCard  sequentially (top-level mutation fields always run sequentially).

In general, if your request batching can be replaced with standard GraphQL, you should prefer standard GraphQL.


## Prior Art

This form of request batching has already been popularized by some GraphQL server implementations, for instance [Hot Chocolate](https://chillicream.com/docs/hotchocolate/v10/execution-engine/batching) and [Sangria](https://sangria-graphql.github.io/learn/#batch-executor). Our implementation is slightly different in that it only returns a single response instead of streaming each query response separately. We may add support for streaming responses in the future.


## More Considerations and Limitations

This is a non-exhaustive list; it may change in future as we add functionality.


### All queries will be executed, even if there are errors.

As the previous errors example shows, all queries are executed even when previous queries have "failed". This is because GraphQL doesn't really have a binary representation of failure. Individual fields can contain errors, but that doesn't necessarily affect the rest of the query, and often you will be able to proceed with the data you did get. In future iterations of this feature, we may allow clients more flexibility in specifying how they want to proceed in the event of errors.


### All queries are executed sequentially.

While we do expect clients to see slight performance improvements from this feature due to less overall HTTP round-trips, the underlying queries will be executed sequentially. So every query you add to your list will introduce that much extra time to your overall response. For that reason, we have limited the number of queries you can send at the time of this writing to 5. All queries beyond this limit will return an error.


### Only scalar values can be exported.

This is actually a hard requirement due to the distinction between GraphQL input and output types. Even if we supported exporting a non-scalar field, it wouldn't be usable as input in subsequent queries.


### Exported variables are interoperable with passed-in variables.

There's nothing stopping you from referencing both exported variables and those in the variables object of your query. Just note that variables in the variables object will override exported ones in the event of a conflict.


### Exporting fields that are under a list node will only export the last value encountered.

We haven't decided how to support accumulating values into a list variable yet (although we're exploring some options). For now it will just override the exported variable for each result in the list, which is probably not what you want.


### Authentication applies to all queries.

The examples we used here conveniently all accept public/private key basic authentication. However, there may be cases where different query fields will expect different authentication, which is not currently supported. We are currently exploring some possible solutions for this.


## Motivation

One of our goals designing the Braintree GraphQL API has been to break down our existing API features into smaller, composable pieces. For instance, the Transaction.sale function in our client libraries accepts any combination of payment_method_token, payment_method_nonce, or raw payment method details. In addition, you can pass store_in_vault: true to indicate that you would like to persist the payment method after the transaction completes. This proliferation of options leads to ambiguity about things like parameter precedence, and makes it difficult for clients to understand the overall surface area of the endpoint.

In order to avoid this scenario in our GraphQL API, we have designed our schema to only expose the basic building blocks of these operations, allowing clients to compose them in whatever way fits their needs. After all, one of the core tenets of GraphQL is client flexibility. However, previously this placed a significant burden on clients to perform multiple HTTP requests for each of these operations, which involves separate response handling for each step. With request batching, clients now only have to handle a single HTTP response.

We will continue to add to this in the future, and would like to hear your feedback. Feel free to open an issue on our [GraphQL API repo](https://github.com/braintree/graphql-api/issues) if you have any questions.

