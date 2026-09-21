<!-- Source URL: https://developer.paypal.com/braintree/graphql/guides/collecting_payment_information -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Collecting Payment Information
slug: /graphql/guides/collecting_payment_information/
createTime: '2025-01-16T11:26:36.828Z'
updateTime: '2025-04-28T13:29:41.622Z'
---



# How to Collect Payment Information


## The Client-Side Integration

When a customer makes a purchase on your app or website, they will first need to enter their payment information. Payment methods come in many varieties, and we support a lot of them — from credit and debit cards, to [PayPal](/braintree/docs/guides/paypal/overview) and [Venmo](/braintree/docs/guides/venmo/overview) accounts, to [Apple Pay](/braintree/docs/guides/apple-pay/overview), [Google Pay](/braintree/docs/guides/google-pay/overview), and [more](/braintree/articles/get-started/payment-methods).

Because payment data is highly sensitive, we offer SDK integrations that shield you from having to store, or even pass through, any of it. Our SDK will send payment data directly from the client to our servers, store it temporarily, and return a unique identifier in string form back to the client. In our SDK documentation, this string is called a "nonce" and it represents a temporary payment method [*](#terminology-note). In terms of the GraphQL API, this string is the ID of a single-use PaymentMethod. Send the string to your payment integration with our GraphQL API in order to charge or vault the payment method.

To get started, see our client SDK guides, offered for [JavaScript](/braintree/docs/guides/client-sdk/setup/javascript/v3), [iOS](/braintree/docs/guides/client-sdk/setup/ios/v6), or [Android](/braintree/docs/guides/client-sdk/setup/android/v4).


## Requesting a Client Token

In order to set up and configure a client-side integration, you need to provide it with a [form of authorization](/braintree/docs/guides/authorization/overview). One option is a client token, which can be obtained with the GraphQL API.

### Mutation
```graphql
mutation {
  createClientToken {
    clientToken
  }
}

```



You can also pass in an optional merchant account ID:

### Mutation
```graphql
mutation ExampleClientToken($input: CreateClientTokenInput) {
  createClientToken(input: $input) {
    clientToken
  }
}

```


### Variables
```json
{
  "input": {
    "clientToken": {
      "merchantAccountId": "MERCHANT_ACCOUNT_ID"
    }
  }
}
```



## Use the Client Token to Get a Payment Method

Use it in your client-side integration to collect customer payment information. For example, if your customer is checking out via a website:

JavaScriptbraintree.dropin.create( { authorization: 'CLIENT_TOKEN_FROM_GRAPHQL_MUTATION', container: '#id-of-dropin-container-on-your-page' }, function(createErr, instance) { varForSubmitButton.addEventListener('click', function() { instance.requestPaymentMethod(function(err, payload) { // submit payload.nonce to your server // where it can be used as a payment method ID }); }); }
);


## Use the Payment Method

Send the resulting nonce string from the payment method to your server, where you can use the GraphQL API to charge the payment method or store it in your Vault for future use.


#### Terminology Note

Nonce is a cryptographic term that stands for " n once," a one-time-use code.

The process of getting a nonce (or anything analogous) is called tokenization, because you're exchanging information for a token that references, but does not contain, that information.

In the GraphQL API, when you tokenize a payment method, you get back a GraphQL PaymentMethod type with an ID used to reference it (replacing the nonce) that does not expose any sensitive payment data.

