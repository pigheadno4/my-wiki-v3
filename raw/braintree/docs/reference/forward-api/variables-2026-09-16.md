<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/forward-api/variables -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Variables
slug: /docs/reference/forward-api/variables/
createTime: '2025-04-02T02:05:52.756Z'
updateTime: '2025-04-02T02:05:53.094Z'
---



# Variables


**AVAILABILITY**
 **Use of the production** [Forward API](/braintree/docs/reference/forward-api/overview/) is subject to eligibility. 

 Contact your Account Manager for more information or [submit an inquiry to our Business Development team](https://www.braintreepayments.com/products/braintree-extend#contact) .

Most strings evaluate to themselves, but strings beginning with $ perform either variable lookups or template lookups.



Global variable lookups are of the form $variable_name. When they are evaluated they return the result of looking up the named variable. Global variables may come from a couple different sources (in increasing order of precedence): the Forward API itself, anything specified in data of the forwarding request, and anything specified in the sensitive_data section of the forwarding request. If the same variable name appears in different sources, the variable from the source with the highest level of precedence will be chosen.



Template lookups are of the form $/section/nested_section/etc Template lookups allow transformations to reference part of the partially constructed request (the template). When template lookups are evaluated the relevant section of the template is fetched, serialized accoring to the rules in request_format, and returned as a string.



There are also local variable lookups, which are of the form $/var/name. They are references to a special section of the template ( var ) which is not serialized and which may not be provided by either the config or the forwarding request.



To define a local variable, write to the var section just as you would any other part of the template:


### json
```json
{"path": "/var/aes-nonce", "value": ["aes-gcm-nonce"]}
```
To use that variable, just refer to it by its path:
### json
```json
{"path": "/body/aes-nonce", "value": ["hex", "$/var/aes-nonce"]}
```
When using an Apple Pay card, you do not have access to the underlying card information. The card number will be the DPAN, and the expiration date will correspond to the DPAN, not the underlying card.


### Variable suffixes

When [forwarding multiple payment methods](/braintree/docs/guides/extend/forward-api/examples#forwarding-multiple-payment-methods), variables for each payment method are bound based on their token's position in the array of [payment_method_tokens](/braintree/docs/reference/forward-api/forward#payment_method_tokens), 1-indexed. Unsuffixed variables reference the first payment method: $variable and $variable_1 have the same value.



When forwarding both a[payment method and a payment method nonce](/braintree/docs/guides/extend/forward-api/examples#cvv-with-vaulted-card-data), the nonce's variables are_2suffixed.


### Available Global Variables



