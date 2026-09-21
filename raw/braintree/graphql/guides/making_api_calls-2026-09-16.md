<!-- Source URL: https://developer.paypal.com/braintree/graphql/guides/making_api_calls -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Making API Calls
slug: /graphql/guides/making_api_calls/
createTime: '2025-01-16T11:27:00.154Z'
updateTime: '2026-03-11T10:23:36.689Z'
---



# Making API Calls

This guide covers how to make API calls by combining [basic GraphQL ideas](/braintree/graphql/guides/#basic-concepts) with [Braintree-specific API details](/braintree/graphql/guides/concepts/).

Because Braintree GraphQL requests are over HTTP, many examples in our guides use curl so you can start testing the API from the command line. We expect you will then pick the HTTP library of your choice for application development.

In the rest of the document, we use MUST, SHOULD, and MAY according to [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).


## Endpoints

All requests (queries and mutations) go to a single HTTP endpoint.

For the sandbox test environment:

https://payments.sandbox.braintree-api.com/graphqland the live production account:

https://payments.braintree-api.com/graphqlYou SHOULD use the [POST](https://tools.ietf.org/html/rfc7231#section-4.3.3) method for all requests.


### Important Security Requirement

The Braintree API returns data exactly as it is provided. It does not perform input validation, output encoding, or sanitization. You are responsible for properly encoding and securing any data retrieved from the API before using or displaying it in your application. Failing to do so may introduce security vulnerabilities.


#### Why Braintree does not encode or validate data

The Braintree API intentionally does not perform input validation or output encoding for several important reasons:


- **Data integrity**
We preserve your data exactly as you provide it. Any modification could corrupt legitimate business data.- **Application is context specific**
We cannot know how you'll use the data. The same character requires different encoding depending on where it is used. For example, &lt; must be encoded differently based on context:


- **JavaScript**requires\x3Cfor&lt;
- **URL**requires%3Cfor&lt;
- **JSON**requires\u003cfor&lt;

Encoding for one context makes the value incorrect for others. Because Braintree cannot determine how your application will use the data, it does not apply context-specific encoding.- **Your Application Controls the Execution Environment**
Only your application knows:


- Which framework is in use (Rails, React, PHP)
- Where data will be rendered (HTML, JSON API, PDF, email)
- Whether decoding is required before use
- What security controls are appropriate

For this reason, encoding and validation must be handled at the application layer.



#### Best practices


- **Never display data directly without encoding**— Use your framework's built-in encoding functions.
- **Choose the correct encoding for your context**— HTML, JavaScript, URL, etc.
- **Use parameterized queries**— Never concatenate data into SQL queries.
- **Validate URLs and file paths**— Don't trust user-provided URLs or paths.


## Request Requirements


### The Authorization Header

To use the API, you MUST have a [registered Braintree account](https://www.braintreepayments.com/sandbox) and include your credentials in the Authorization header. There are different types of credentials you can use to authorize depending on what you'd like to do. For instance, [client tokens](#client-tokens) and [tokenization keys](#tokenization-keys) are restricted to certain mutations and queries that generally don't involve money movement, such as tokenizing payment details. Other operations, such as vaulting and charging payment methods, require [API Key](#api-keys) authentication.


#### API Keys

This is the option many integrations use. After you [generate an API Key](https://articles.braintreepayments.com/control-panel/important-gateway-credentials#api-keys), you MUST Base64-encode it for GraphQL requests.

If your public key is v4ndq314c2s5c28r and your private key is 93b78bc88be90d93ac282e50ae569fdd, you can generate your Base64-encoded token like this:

echo -n "v4ndq314c2s5c28r:93b78bc88be90d93ac282e50ae569fdd" | base64which produces djRuZHEzMTRjMnM1YzI4cjo5M2I3OGJjODhiZTkwZDkzYWMyODJlNTBhZTU2OWZkZA==. The full header you present for authentication and authorization is:

Authorization: Basic djRuZHEzMTRjMnM1YzI4cjo5M2I3OGJjODhiZTkwZDkzYWMyODJlNTBhZTU2OWZkZA==
#### Tokenization Keys

A [tokenization key](/braintree/docs/guides/authorization/tokenization-key/) is a lightweight, reusable value that can authorize your client to tokenize payment methods. You can [view your tokenization keys in the Control Panel](/braintree/articles/control-panel/important-gateway-credentials#tokenization-keys). To authorize using a tokenization key, pass it in the Authorization header:

Authorization: Bearer YOUR_TOKENIZATION_KEY
#### Authorization Fingerprints

Another way to authenticate from your client is via an authorization fingerprint from a [client token](/braintree/docs/guides/authorization/client-token). A client token contains an authorization fingerprint, which is a signed [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token), and is generated on your server with a lifetime of 24 hours. To obtain an authorization fingerprint you must Base64 decode a client token, the decoded client token will contain an authorizationFingerprint value, which can then be passed in the Authorization header.

For instance, once you obtain a client token, it can be decoded:

echo -n YOUR_CLIENT_TOKEN | base64 -DThis will produce a JSON value, similar to this:


### Response
```json
{
  "version": "2",
  "environment": "sandbox",
  "authorizationFingerprint": "YOUR_AUTHORIZATION_FINGERPRINT"
}
```
Your client is responsible for obtaining an authorization fingerprint from your server and can pass it in the Authorization header:

Authorization: Bearer YOUR_AUTHORIZATION_FINGERPRINT
#### Braintree Auth

(This is currently in closed beta). To use [Braintree Auth](https://developers.braintreepayments.com/guides/braintree-auth/overview) credentials, you must obtain an access token via the [OAuth flow](https://developers.braintreepayments.com/guides/braintree-auth/oauth-flow/node#getting-an-access-token). When you have an access token, use it via the Authorization header:

Authorization: Bearer YOUR_ACCESS_TOKEN
### The Braintree-Version Header

You MUST provide a Braintree-Version header with a date in the format YYYY-MM-DD. We recommend using the date on which you begin integrating with the GraphQL API.

Braintree-Version: 2019-01-01
### The Content-Type Header

The content type of a query MUST be application/json.

Content-Type: application/json
### The Message Body

The message body MUST be a JSON object. It MUST contain a query key and MAY contain a variables key.

The value for query MUST be a single [JSON string](https://tools.ietf.org/html/rfc7159#section-7) containing a well-formed GraphQL document (query or mutation).

If you reference variables in your GraphQL document, the value for variables MUST be a JSON object containing the key/value pairs for each variable.


### Variables
```json
{
  "query": "a GraphQL document goes here that references $var1, $var2, and $var3",
  "variables": {
    "var1": 10,
    "var2": {
      "some": "data",
      "for": "var2"
    },
    "var3": [
      "a",
      "list",
      "of",
      "values"
    ]
  }
}
```

## Your First Request

The simplest request is ping. It is mainly useful to ensure you understand how to generate well-formed requests.

Here's the GraphQL query:



### Query
```graphql
query {
  ping
}

```

To send that to our API, it has to be wrapped in a JSON object with a query key:


### JSON
```json
{
  "query": "query { ping }"
}
```
And here's how it all fits together, using curl :

curl -H 'Authorization: Basic BASE64_ENCODED(PUBLIC_KEY:PRIVATE_KEY)' -H 'Braintree-Version: 2019-01-01' -H 'Content-Type: application/json' -X POST https://payments.sandbox.braintree-api.com/graphql -d '{"query": "query { ping }"}'You should receive this response:


### Response
```json
{
  "data": {
    "ping": "pong"
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

## A More Interesting Request

Here is a typical request body for the chargePaymentMethod mutation (Note: we have added newlines for readability but normally, [JSON strings](https://tools.ietf.org/html/rfc7159#section-7) MUST escape newlines):


### Request,Body
```json
{
  "query": "mutation chargePaymentMethod($input: ChargePaymentMethodInput!) { chargePaymentMethod(input: $input) { transaction { id status } } }",
  "variables": {
    "input": {
      "paymentMethodId": "PAYMENT_METHOD_ID",
      "transaction": {
        "amount": "11.23"
      }
    }
  }
}
```
Per standard GraphQL, the input key in the variables section binds to the $input variable defined by the mutation in the query section and should represent the ChargePaymentMethodInput type.


### Two Mutations In One Call

By using [GraphQL aliases](https://graphql.org/learn/queries/#aliases), we can make multiple charges in a single call to the API:


### Request,Body
```json
{
  "query": "mutation twoChargesAtOnce($tx1: ChargePaymentMethodInput!, $tx2: ChargePaymentMethodInput!) { firstTransaction: chargePaymentMethod(input: $tx1) { transaction { amount { value currencyIsoCode } } } secondTransaction: chargePaymentMethod(input: $tx2) { transaction { amount { value currencyIsoCode } } } }",
  "variables": {
    "tx1": {
      "paymentMethodId": "fake-valid-visa-nonce",
      "transaction": {
        "amount": "11.25"
      }
    },
    "tx2": {
      "paymentMethodId": "fake-valid-amex-nonce",
      "transaction": {
        "amount": "11.23"
      }
    }
  }
}
```

### Response
```json
{
  "data": {
    "firstTransaction": {
      "transaction": {
        "amount": {
          "value": "11.25",
          "currencyIsoCode": "USD"
        }
      }
    },
    "secondTransaction": {
      "transaction": {
        "amount": {
          "value": "11.23",
          "currencyIsoCode": "USD"
        }
      }
    }
  },
  "extensions": {
    "requestId": "TdTMiKZ1YBlBzSxLHSTEAQ1y3P3UbZCZue0NuDz4yLReE0_09dBOGg=="
  }
}
```

## Understanding Responses

A response from the GraphQL API will always return with HTTP status 200. The JSON body of the response explains whether an error occurred. Because you can send multiple queries and mutations in a single request, and because GraphQL includes the concept of a "partial success", the request may contain a mix of data and error messages. The body is always a JSON object and MAY include any of the three top-level keys: data, errors, and extensions.


### Data

A successful query MUST return a JSON object with a data key whose value is a JSON object with the data you requested. Each key in the data object will exactly match those specified in the query.


### Errors

Unlike a conventional REST API, GraphQL APIs do not rely on HTTP status codes to signal request outcomes. Our GraphQL API always return a JSON body with the 200 status code, even when there are errors.

If an error occurred, the response body MUST include a top-level errors array that describes the error or errors. For example, the response for charging a payment method with an invalid credit card number would be:


### Response
```json
{
  "data": {
    "chargePaymentMethod": null
  },
  "errors": [
    {
      "message": "Unknown or expired single-use payment method.",
      "locations": [
        {
          "line": 2,
          "column": 7
        }
      ],
      "path": [
        "chargePaymentMethod"
      ],
      "extensions": {
        "errorType": "user_error",
        "errorClass": "VALIDATION",
        "legacyCode": "91565",
        "inputPath": [
          "input",
          "paymentMethodId"
        ]
      }
    }
  ],
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
An element of the errors array [follows the GraphQL spec](https://graphql.github.io/graphql-spec/June2018/#sec-Errors) and will have the following values:


- message: The human-readable error message. This value is not intended to be parsed and may change at any time.
- locations: An array of{ "line": x, "column": y }objects that describe where the error was detected during parsing of the GraphQL query. This is typically only used by interactive viewers such as[GraphiQL](https://github.com/graphql/graphiql), including our[API Explorer](/braintree/graphql/explorer/).
- path: The GraphQL query or mutation causing the error.
- extensions: Additional information about the error including...
- errorType: A deprecated field, please refer to errorClass instead.
- errorClass: The classification of the error. Can be one of...
- AUTHENTICATION
- AUTHORIZATION
- INTERNAL
- UNSUPPORTED_CLIENT
- NOT_FOUND
- NOT_IMPLEMENTED
- RESOURCE_LIMIT
- SERVICE_AVAILABILITY
- VALIDATION


- legacyCode: A unique code identifying the error, which can be used to look it up[in our documentation](/braintree/docs/reference/general/validation-errors/all)
- inputPath: The input field responsible for the error.



Errors can manifest as GraphQL validation errors (e.g. provided a string for an integer field), Braintree validation errors (e.g. invalid credit card number), or errors reflecting upstream issues.

It is possible to have partially successful responses, where both a partially populated data object and errors are returned. If errors prevent a field in your query from resolving, the field in the data object will be returned with the value null and relevant errors will be in the error object.


### Extensions

The API response MUST contain an extensions object. This object contains at least a requestId entry that is unique to the request and useful to Braintree Support should you need help debugging a request.


## Timeouts

When using the GraphQL API, keep in mind that some requests (like creating transactions) can take longer than expected since they rely on communicating with a payment processor. We set a recommend setting a timeout of 60 seconds to accommodate for this. If you do not want to wait this long, you can set a custom timeout via the client you are using to form a request to the GraphQL API. However, if this timeout is less than 60 seconds, your client may trigger a timeout exception and you may not see the result of the request.

For example, let's say you set the timeout to 10 seconds, and you create a transaction request. If the request has not completed successfully at 10 seconds, your client will timeout. However, if the transaction then completes successfully at 19 seconds, the customer will be charged, but you will not receive any notification of this. You will need to search for the transaction to confirm if it was created and verify its status.


## Using GraphiQL

We've integrated the [GraphiQL](https://github.com/graphql/graphiql) project into our GraphQL documentation to allow you to explore the API in your browser using your sandbox API credentials. GraphiQL is a graphical interactive IDE for exploring and playing around with GraphQL APIs.

You can use it via the [API Explorer](/braintree/graphql/explorer) on this site, or with the desktop application, to interact with the API in real time.

To access the API, authenticate with your sandbox login credentials. From there, you can browse the schema documentation and live code queries and mutations. If you don't have a sandbox account, you can [create one](https://www.braintreepayments.com/sandbox) and it will be immediately available for use.

Rather than passing in a JSON-formatted string, as we show in the examples above, the GraphiQL explorer expects plain GraphQL queries and JSON-formatted variables to be entered in separate windows. Unless we are providing curl examples, we will follow this "plain" GraphQL formatting in our guides, so you can easily test-drive queries and mutations in GraphiQL. Just remember to use JSON-formatting when handling your own HTTP requests outside of GraphiQL.

