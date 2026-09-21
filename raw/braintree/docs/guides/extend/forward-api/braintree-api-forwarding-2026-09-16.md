<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/extend/forward-api/braintree-api-forwarding -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Forwarding Braintree API Payment Tokens
slug: /docs/guides/extend/forward-api/braintree-api-forwarding/
createTime: '2025-04-02T01:09:14.071Z'
updateTime: '2025-04-02T01:09:14.096Z'
---



# Forwarding Braintree API Payment Tokens


**AVAILABILITY**
**Use of the production [Forward API](/braintree/docs/reference/forward-api/overview/) is subject to eligibility.** Contact your Account Manager for more information or [submit an inquiry to our Business Development team](https://www.braintreepayments.com/products/braintree-extend#contact) .

You may wish to forward payment tokens from the alternate Braintree API. If you have a token
returned from the Braintree API, you can forward it with thepayment_method_nonceparameter.
### bash
```bash
curl https://forwarding.sandbox.braintreegateway.com/ \
    -H "Content-Type: application/json" \
    -X POST \
    -u "$\{BRAINTREE_PUBLIC_KEY}:$\{BRAINTREE_PRIVATE_KEY}" \
    -d '{ 
        "merchant_id": "'"$BRAINTREE_MERCHANT_ID"'", 
        "method": "POST", 
        "payment_method_nonce": "tokencc_dp8wcw_wd4629_rqfkg2_qkwyz6_jq3", 
        "url": "https://httpbin.org/post", 
        "config": { 
            "name": "braintree-alternate-api-with-payment-token", 
            "methods": ["POST"], 
            "url": "^https://httpbin\\.org/post$", 
            "request_format": {"/body": "urlencode"}, 
            "types": ["CreditCard"], 
            "transformations": [{ 
                "path": "/body/card[number]", 
                "value": "$number" 
            }] 
        } 
    }'
```
If you have a payment method token backed by a payment method in the alternate Braintree API, you
can forward it with thepayment_method_tokenparameter as you would any other payment
method token.
### bash
```bash
curl https://forwarding.sandbox.braintreegateway.com/ \
  -H "Content-Type: application/json" \
  -X POST \
  -u "${BRAINTREE_PUBLIC_KEY}:${BRAINTREE_PRIVATE_KEY}" \
  -d '{
    "merchant_id": "'"$BRAINTREE_MERCHANT_ID"'",
    "method": "POST",
    "payment_method_token": "abc123",
    "url": "https://httpbin.org/post",
    "config": {
      "name": "braintree-alternate-api-with-payment-method-token",
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
