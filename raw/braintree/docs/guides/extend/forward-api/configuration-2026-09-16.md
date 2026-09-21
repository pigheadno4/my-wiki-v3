<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/extend/forward-api/configuration -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Configuration
slug: /docs/guides/extend/forward-api/configuration/
createTime: '2025-04-02T00:37:24.000Z'
updateTime: '2025-04-02T00:37:24.056Z'
---



# Configuration

**AVAILABILITY**
 **Use of the production**  [**Forward API**](/braintree/docs/reference/forward-api/overview/)  **is subject to eligibility.**   Contact your Account Manager for more information or [submit an inquiry to our Business Development team](https://www.braintreepayments.com/products/braintree-extend#contact).

 The Forward API is configured using JSON from two sources:


- The[incoming forward request](#incoming-forward-request)
- A[config](#configs)


## Incoming Forward Request

The [incoming forward request](/braintree/docs/reference/forward-api/forward) is simply the body of the incoming request to the Forward API. It is specified in JSON, and contains information like your merchant ID, the nonce or token of the outgoing payment method, and the URL of the outgoing request.

You can find more information about the params of an incoming forward request on the [reference page](/braintree/docs/reference/forward-api/forward).


## Configs

[Configs](/braintree/docs/reference/forward-api/config/) specify the format, structure, and transformations that are applied to a request before being sent to the destination.     In sandbox, you can specify a config inline on the request using the config key. In production, we will review and import each of your configs which you can reference by [name](/braintree/docs/reference/forward-api/forward#name) on the incoming request.     Let's take a look at an example request using the config key: 
### bash
```bash
curl https://forwarding.sandbox.braintreegateway.com/ \
  -H "Content-Type: application/json" \
  -X POST \
  -u "${BRAINTREE_PUBLIC_KEY}:${BRAINTREE_PRIVATE_KEY}" \
  -d '{
    "merchant_id": "'"$BRAINTREE_MERCHANT_ID"'",
    "payment_method_nonce": "fake-valid-nonce",
    "url": "https://httpbin.org/post",
    "method": "POST",
    "config": {
      "name": "inline_example",
      "methods": ["POST"],
      "url": "^https://httpbin\.org/post$",
      "request_format": {"/body": "urlencode"},
      "types": ["CreditCard"],
      "transformations": [{
        "path": "/body/card[number]",
        "value": "$number"
      }]
    }
  }'
```
 Returns: 
### JSON
```json
{
    "status": 200, // (httpbin.org status code)
    "headers": (headers from httpbin.org),
    "body": (raw body from httpbin.org),
    "request-time": (in milliseconds)
}
```
 This config describes how to post data to a sample destination ( [httpbin.org](http://httpbin.org) ). When you use this config, the $number placeholder will be replaced with credit card data from the Vault.     For more details about the parameters that the Forward API accepts in a config, see the [config reference](/braintree/docs/reference/forward-api/config/).     When name is provided on a request instead of config, the Forward API will check to see if a stored config exists with that name and use it in place of the config key. In sandbox, we provide all merchants with a named config, braintree, that creates transactions in the Braintree sandbox. 
### bash
```bash
# sample usage of the 'braintree' config
curl https://forwarding.sandbox.braintreegateway.com/ \
  -H "Content-Type: application/json" \
  -X POST \
  -u "${BRAINTREE_PUBLIC_KEY}:${BRAINTREE_PRIVATE_KEY}" \
  -d '{
    "merchant_id": "'"$BRAINTREE_MERCHANT_ID"'",
    "payment_method_nonce": "fake-valid-nonce",
    "name": "braintree",
    "url": "https://sandbox.braintreegateway.com/merchants/'$BRAINTREE_MERCHANT_ID'/transactions",
    "method": "POST",
    "data": {"public_key": "'"$BRAINTREE_PUBLIC_KEY"'", "amount": "1.00"},
    "sensitive_data": {"private_key": "'"$BRAINTREE_PRIVATE_KEY"'"}
  }'
```


## Debug Transformations

One handy way to test the Forward API without actually performing a request is to use [debug_transformations](/braintree/docs/reference/forward-api/forward#debug_transformations). Debug transformations tell the Forward API to not make an outgoing request, and instead respond with the information it would have sent. In sandbox, set [debug_transformations](/braintree/docs/reference/forward-api/forward#debug_transformations) to true to use this feature: 
### bash
```bash
curl https://forwarding.sandbox.braintreegateway.com/ \
    -H "Content-Type: application/json" \
    -X POST \
    -u "$\{BRAINTREE_PUBLIC_KEY}:$\{BRAINTREE_PRIVATE_KEY}" \
    -d '{
        "merchant_id": "'$BRAINTREE_MERCHANT_ID'",
        "payment_method_nonce": "fake-valid-nonce",
        "debug_transformations": true,
        "url": "https://httpbin.org/post",
        "method": "POST",
        "config": {
            "name": "inline_example_debug",
            "methods": ["POST"],
            "url": "^https://httpbin\\.org/post$",
            "request_format": {"/body": "json"},
            "types": ["CreditCard"],
            "transformations": [{
                "path": "/body/card/number",
                "value": "$number"
            }]
        }
    }'
```
 Returns: 
### JSON
```json
{
    "card": {
        "number": "4012888888881881"
    }
}
```
 If you use [Postman](https://www.postman.com/), a helpful tool for working with APIs, we have published a Postman collection to help get you started.      [Download it here](/braintree/files/forward_api.postman_collection.json)     and import it into Postman.


## Test Nonces

In case you do not have a valid payment_method_nonce handy, we provide a number of [test nonces](/braintree/docs/reference/general/testing#payment-method-nonces) you can use in a Forward API request.


## Transformations

Transformations are a powerful way of controlling the output of the forward API. You saw above how to inject card information into the request. [Read on](/braintree/docs/guides/extend/forward-api/transformations) to learn how to format, encode, and encrypt parts of the request using transformations.



[Next Page:Transformations→](/braintree/docs/guides/extend/forward-api/transformations)

