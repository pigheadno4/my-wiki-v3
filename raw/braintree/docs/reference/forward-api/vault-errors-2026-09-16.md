<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/forward-api/vault-errors -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Vault Errors
slug: /docs/reference/forward-api/vault-errors/
createTime: '2025-04-01T23:47:33.410Z'
updateTime: '2025-04-01T23:47:33.441Z'
---



# Vault Errors


**AVAILABILITY**
 **Use of the production** [Forward API](/braintree/docs/reference/forward-api/overview/) is subject to eligibility. 

 Contact your Account Manager for more information or [submit an inquiry to our Business Development team](https://www.braintreepayments.com/products/braintree-extend#contact) .

Vault errors are returned in the response body to your application. The body is a JSON structure with a format resembling this example:
### json
```json
{
    "error": "Vault error",
    "message": {
        "vault_error?": true,
        "vault_status": 404,
        "message": "payment_method_token not found"
    },
    "request-uuid": "a-unique-identifier-for-the-request"
}
```
Themessagemay include additional context from the[Braintree Vault.](/braintree/docs/guides/payment-methods)| Vault Status | Explanation | Additionalmessagecontent |
| --- | --- | --- |
| 401 | The provided API credentials are invalid or are sent from an IP violating the[IP allowlist](/braintree/articles/risk-and-security/allowlisting). | None |
| 403 | The provided API credentials lack the Forward API right.[Contact us](mailto:braintreeextend@braintreepayments.com)to confirm the user's API credentials have been allowlisted. | None |
| 404 | The provided[merchant_id](/braintree/docs/reference/forward-api/forward#merchant_id)is invalid. | None |
| 404 | The provided[payment_method_nonce](/braintree/docs/reference/forward-api/forward#payment_method_nonce)is invalid. | payment_method_nonce not found |
| 404 | The provided[payment_method_token](/braintree/docs/reference/forward-api/forward#payment_method_token)is invalid. | payment_method_token not found |
| 422 | The provided payment method does not have sufficient data, likely because it is malformed. | No payment data |
| 422 | The provided payment method cannot be used with the Forward API. | The provided payment method cannot be exported |
| 422 | Errors occurred with one or more payment methods or[cse_data](/braintree/docs/reference/forward-api/forward#cse_data)bindings. Inspect the object to see specific details. | messageis a JSON object |
| 422 | The provided[payment_method_nonce](/braintree/docs/reference/forward-api/forward#payment_method_nonce)must be retrieved via the Vault flow when you forward a PayPal account. | Pre-Approved Payment enabled PayPal account required for exporting. |

