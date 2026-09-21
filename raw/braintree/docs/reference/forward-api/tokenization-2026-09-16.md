<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/forward-api/tokenization -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Tokenization
slug: /docs/reference/forward-api/tokenization/
createTime: '2025-04-01T23:38:14.622Z'
updateTime: '2025-04-01T23:38:14.669Z'
---



# Tokenization


**AVAILABILITY**
 **Use of the production** [Forward API](/braintree/docs/reference/forward-api/overview/) is subject to eligibility.

  Contact your Account Manager for more information or [submit an inquiry to our Business Development team](https://www.braintreepayments.com/products/braintree-extend#contact).

 




## Example - Discover TPAN


### bash
```bash

curl https://forwarding.sandbox.braintreegateway.com/ \
  -H "Content-Type: application/json" \
  -X POST \
  -u "\${BRAINTREE_PUBLIC_KEY}:\${BRAINTREE_PRIVATE_KEY}" \
  -d '{
    "merchant_id": "'"$BRAINTREE_MERCHANT_ID"'",
    "payment_method_nonce": "fake-valid-nonce",
    "debug_transformations": true,
    "tokenize_on_forward": true,
    "url": "https://httpbin.org/post",
    "method": "POST",
    "config": {
      "name": "inline_example_debug",
      "methods": ["POST"],
      "url": "^https://httpbin\\.org/post$",
      "request_format": {"/body": "json"},
      "types": ["NetworkTokenizedCard"],
      "transformations": [{
        "path": "/body/number",
        "value": "$number"
      },
      {"path": "/body/cvv", "value": "$cvv"}]
    }
  }'

```
Returns:


### json
```json

{"number":"6011000991300009","cvv:":"123"}
# cvv will be three random digits

```

## Example - Mastercard TPAN


### bash
```bash

curl https://forwarding.sandbox.braintreegateway.com/ \
  -H "Content-Type: application/json" \
  -X POST \
  -u "\${BRAINTREE_PUBLIC_KEY}:\${BRAINTREE_PRIVATE_KEY}" \
  -d '{
    "merchant_id": "'"$BRAINTREE_MERCHANT_ID"'",
    "payment_method_nonce": "fake-valid-nonce",
    "debug_transformations": true,
    "tokenize_on_forward": true,
    "url": "https://httpbin.org/post",
    "tsp": {"currency_code": "EUR"},
    "method": "POST",
    "config": {
      "name": "inline_example_debug",
      "methods": ["POST"],
      "url": "^https://httpbin\\.org/post$",
      "request_format": {"/body": "json"},
      "types": ["NetworkTokenizedCard"],
      "transformations": [{
        "path": "/body/number",
        "value": "$number"
      },
      {"path": "/body/cvv", "value": "$cvv"}]
    }
  }'

```
Returns:


### json
```json

{"number":"5555555555554444","cvv":"123"}
# cvv will be three random digits

```

#### Additional parameters


## AVS and CVV

Authorizations against a Discover TPAN require the generated CVV unless the [expire_at](#tsp.expire_at) option was set; failing to provide it will result in a decline.   The TPAN does not have an associated postal code, and any postal code provided during an authorization will result in an AVS response of [M (matches)](/braintree/docs/reference/general/processor-responses/avs-cvv-responses#avs).


## Errors

If tokenization is attempted on an unsupported or invalid payment instrument, the Forward API will return an [error response](/braintree/docs/reference/forward-api/tokenization-errors).

