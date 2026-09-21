<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/forward-api/direct-tokenization -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Direct Tokenization
slug: /docs/reference/forward-api/direct-tokenization/
createTime: '2025-04-01T23:26:32.079Z'
updateTime: '2025-04-01T23:26:32.106Z'
---



# Direct Tokenization

**AVAILABILITY**
**Use of the production [Forward API](/braintree/docs/reference/forward-api/overview/) is subject to eligibility.** Contact your Account Manager for more information or [submit an inquiry to our Business Development team](https://www.braintreepayments.com/products/braintree-extend#contact).

 Direct tokenization utilizes the Forward API to generate a tokenized PAN for a payment instrument. ```syntax-inline
POST
```
 [https://forwarding.sandbox.braintreegateway.com/tsp](https://forwarding.sandbox.braintreegateway.com/tsp)  
**IMPORTANT**
You must be pre-approved to use this endpoint. If you are not approved, you will receive an error with a 403 status code when making requests to this endpoint. Keep in mind that the Payment Card Industry (PCI) views TPANs as PANs, which means they should be handled with the same care and compliance as credit card numbers.


#### Parameters

[device_data](#device_data)StringThe [device_data](/braintree/docs/guides/paypal/vault#collecting-device-data) parameter contains session identifiers ultimately used for Risk decisions. Provide the full string received from the Braintree client SDK.

[merchant_id](#merchant_id)String

RequiredThe unique identifier of the merchant whose Vault will be accessed.



[payment_method_nonce](#payment_method_nonce)StringThe [payment_method_nonce](/braintree/docs/guides/payment-method-nonces) of the payment instrument being tokenized.

[payment_method_token](#payment_method_token)StringThe [payment_method_token](/braintree/docs/reference/request/transaction/sale#payment_method_token) of the payment instrument being tokenized.

[tsp](#tsp)objectTokenization Service Provider options

[currency_code](#currency_code)StringThe currency code the max amount should apply to. Currently only enforced for Discover TPANs. Default USD.

[expire_at](#expire_at)StringIf provided, the tokenized PAN may be used any number of times untilexpire_at, an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date with optional time. This does not set $expiration_month and/or $expiration_year. Currently only enforced for Discover TPANs.

[max_amount](#max_amount)StringThe maximum amount the tokenized PAN can be charged. Currently only enforced for Discover TPANs.

[require_cryptogram](#require_cryptogram)booleanIf set totrue, a cryptogram will be returned instead of a dynamic CVV. Currently only compatible with Visa network tokens. Defaultfalse.




### Tokenization in the sandbox environment

When calling the TSP (Token Service Provider) in the sandbox environment, test values for number, cvv, expiration_month, and expiration_year will be returned.


## Example - Discover TPAN

### bash
```bash
curl https://forwarding.sandbox.braintreegateway.com/tsp   -H "Content-Type: application/json"   -X POST   -u "${BRAINTREE_PUBLIC_KEY}:${BRAINTREE_PRIVATE_KEY}"   -d '{
    "merchant_id": "'"$BRAINTREE_MERCHANT_ID"'",
    "payment_method_nonce": "fake-valid-nonce"
  }'

# Returns JSON object with cvv, expiration_month, expiration_year and number, eg
# {"expiration_year":"2036","expiration_month":"4","cvv":"939","number":"6011000991300009"}

```


## Example - Visa network token

### bash
```bash
curl https://forwarding.sandbox.braintreegateway.com/tsp   -H "Content-Type: application/json"   -X POST   -u "${BRAINTREE_PUBLIC_KEY}:${BRAINTREE_PRIVATE_KEY}"   -d '{
    "merchant_id": "'"$BRAINTREE_MERCHANT_ID"'",
    "payment_method_nonce": "fake-valid-visa-nonce",
    "tsp": {"require_cryptogram": true}
  }'

# Returns JSON object with cryptogram, expiration_month, expiration_year, number and network TRID, eg
# {"cryptogram":"AgAAAAAAALm1mmu9TqJGQAAAAAA=",
#  "expiration_year":"2036",
#  "expiration_month":"4",
#  "network_token_requestor_id":"40010036958",
#  "number":"4012000033330521"}
```

