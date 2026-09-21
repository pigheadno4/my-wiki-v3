<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/extend/forward-api/tokenization-support -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Tokenization Support
slug: /docs/guides/extend/forward-api/tokenization-support/
createTime: '2025-04-01T22:51:39.054Z'
updateTime: '2025-04-01T22:51:39.098Z'
---



# Tokenization Support

**AVAILABILITY**
 **Use of the production**  [**Forward API**](/braintree/docs/reference/forward-api/overview/)  **is subject to eligibility.**   Contact your Account Manager for more information or [submit an inquiry to our Business Development team](https://www.braintreepayments.com/products/braintree-extend#contact).

 The Forward API currently supports Discover and Mastercard TPANs.     Discover TPANs are currently restricted to US-issued credit cards, PayPal accounts, and Venmo accounts.     Mastercard TPANs are currently restricted to credit cards issued in the European Union or United Kingdom and PayPal accounts.     In production, tokenization requires approval and linked PayPal credentials.


## Capabilities

|  | Discover TPAN | Mastercard TPAN |
| --- | --- | --- |
| **Region restrictions** | US only | European Union and United Kingdom |
| **Supports amount restrictions** | Yes, via[max_amount](/braintree/docs/reference/forward-api/tokenization#tsp-max_amount) | Yes, via[max_amount](/braintree/docs/reference/forward-api/tokenization#tsp-max_amount) |
| **Supports cryptogram-based authorizations** | No | No |
| **Supports CVV-based authorizations** | Yes, required for authorization unless[expire_at](/braintree/docs/reference/forward-api/tokenization#tsp-expire_at)is specified | Yes, required for authorization unless[expire_at](/braintree/docs/reference/forward-api/tokenization#tsp-expire_at)is specified |
| **Supports multiple authorizations** | Yes, if[expire_at](/braintree/docs/reference/forward-api/tokenization#tsp-expire_at)is specified | Yes, if[expire_at](/braintree/docs/reference/forward-api/tokenization#tsp-expire_at)is specified |
| **Supports PayPal** | Yes, currently only for channel-initiated billing agreements (CIBs) | Yes, currently only for channel-initiated billing agreements (CIBs) |
| **Supports TTL restrictions** | Yes, via[expire_at](/braintree/docs/reference/forward-api/tokenization#tsp-expire_at) | Yes, via[expire_at](/braintree/docs/reference/forward-api/tokenization#tsp-expire_at) |
| **Supports Venmo** | Yes | No |


## Usage

Configs using TPANs are nearly identical to CreditCard configs, with two key differences:


- "NetworkTokenizedCard"will be included among the[types](/braintree/docs/reference/forward-api/config/#types)
- $cvvwill be available as a[variable](/braintree/docs/reference/forward-api/variables)

Tokenization will be attempted automatically if a config supports the "NetworkTokenizedCard" type but not the payment method type of the specified payment_method_token or payment_method_nonce. If the config supports both, ["tokenize_on_forward"parameter](/braintree/docs/reference/forward-api/tokenization#tokenize_on_forward) can be set to true to send tokenized card information.     You can optionally pass [TSP Options](/braintree/docs/reference/forward-api/tokenization#tsp) when forwarding a specific payment method to a third party to limit what can be done with a TPAN. For example, if you passed max_amount as 10.00, and the third party tried to charge 900.00, the transaction would fail.


## Example - Discover TPAN

### bash
```bash
curl https://forwarding.sandbox.braintreegateway.com/ \
  -H "Content-Type: application/json" \
  -X POST \
  -u "${BRAINTREE_PUBLIC_KEY}:${BRAINTREE_PRIVATE_KEY}" \
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
      "url": "^https://httpbin\.org/post$",
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
### JSON
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
  -u "${BRAINTREE_PUBLIC_KEY}:${BRAINTREE_PRIVATE_KEY}" \
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
      "url": "^https://httpbin\.org/post$",
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
### JSON
```json
{"number":"5555555555554444","cvv":"123"}
# cvv will be three random digits
```


## See also


- [Tokenization Reference](/braintree/docs/reference/forward-api/tokenization)



[Next Page:Hyperwallet Integration→](/braintree/docs/guides/extend/forward-api/hyperwallet)

