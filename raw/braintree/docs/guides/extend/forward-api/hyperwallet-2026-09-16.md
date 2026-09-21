<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/extend/forward-api/hyperwallet -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Hyperwallet Integration
slug: /docs/guides/extend/forward-api/hyperwallet/
createTime: '2025-04-02T01:36:57.057Z'
updateTime: '2025-04-02T01:36:57.494Z'
---



# Hyperwallet Integration


**AVAILABILITY**
 **Use of the production** [**Forward API**](/braintree/docs/reference/forward-api/overview/) **is subject to eligibility.** Contact your Account Manager for more information or [submit an inquiry to our Business Development team](https://www.braintreepayments.com/products/braintree-extend#contact) .

Hyperwallet provides an [API](https://docs.hyperwallet.com/content/api/v4/overview/accessing-the-api) that you can use to interact with their service. The Forward API can be used to interact with the [Bank Card Create](https://docs.hyperwallet.com/content/api/v4/resources/bank-cards/create) and [Bank Card Update](https://docs.hyperwallet.com/content/api/v4/resources/bank-cards/update) parts of this API.


## Naming & Environment Alignment

| Braintree Env | Hyperwallet Env | Config Name |
| --- | --- | --- |
| Sandbox | Sandbox | hyperwallet_sandbox |
| Sandbox | UAT | hyperwallet_integration |
| Production | Production | hyperwallet_integration |


## Example


- Before running this request, create a[sandbox account](https://portal.hyperwallet.com/login)with Hyperwallet.
- Once you create a sandbox account, create a user by selecting the Tutorial tab and completing the first two steps. In the response to your create user request, you should see a "token" field with a value that starts withusr-.... This is the value you need to use forHYPERWALLET_USER_TOKEN. *You can see yourAPI Usernamein the Credentials tab, which is the value you need to provide as yourHYPERWALLET_USER.
- Finally, yourAPI Passwordstarts as the password for the account, but can be changed on the Credentials tab (note this does not change the account password). This is the value that you need to use forHYPERWALLET_PW.

Example create request (sandbox)




### bash
```bash
curl https://forwarding.sandbox.braintreegateway.com/ \
    -H "Content-Type: application/json" \
    -X POST \
    -u "${BRAINTREE_PUBLIC_KEY}:${BRAINTREE_PRIVATE_KEY}" \
    -d '{
        "merchant_id": "${BRAINTREE_MERCHANT_ID}",
        "payment_method_nonce": "fake-valid-nonce",
        "name": "hyperwallet_sandbox",
        "url": "https://api.sandbox.hyperwallet.com/rest/v4/users/${HYPERWALLET_USER_TOKEN}/bank-cards/",
        "method": "POST",
        "data": {
            "transferMethodCountry": "US",
            "transferMethodCurrency": "USD"
        },
        "sensitive_data": {
            "user": "${HYPERWALLET_USER}",
            "password": "${HYPERWALLET_PW}",
            "cvv": "123",
            "number": "4622943126011056"
        }
    }'
```
Response Body
### JSON
```json
{
    "token": "trm-62c28319-yyyy-4386-973d-cab385d9212a",
    "type": "BANK_CARD",
    "status": "ACTIVATED",
    "createdOn": "2022-10-07T17:30:40",
    "transferMethodCountry": "US",
    "transferMethodCurrency": "USD",
    "bankName": "INTL HDQTRS-CENTER OWNED",
    "cardType": "DEBIT",
    "cardNumber": "****1056",
    "cardBrand": "VISA",
    "dateOfExpiry": "2027-12",
    "userToken": "usr-69662d54-xxxx-48a3-922a-ec907fd58673",
    "processingTime": "30 minutes",
    "links": [
        {
            "params": {
                "rel": "self"
            },
            "href": "https://api.sandbox.hyperwallet.com/rest/v4/users/usr-69662d54-xxxx-48a3-922a-ec907fd58673/bank-cards/trm-62c28319-yyyy-4386-973d-cab385d9212a"
        }
    ]
}
```
Example update request


- TheHYPERWALLET_INST_TOKENis the token handed back from the create request. In the previous example, this wastrm-62c28319-yyyy-4386-973d-cab385d9212a.


### bash
```bash
curl https://forwarding.sandbox.braintreegateway.com/ \
    -H "Content-Type: application/json" \
    -X POST \
    -u "${BRAINTREE_PUBLIC_KEY}:${BRAINTREE_PRIVATE_KEY}" \
    -d '{
        "merchant_id": "${BRAINTREE_MERCHANT_ID}",
        "payment_method_nonce": "fake-valid-nonce",
        "name": "hyperwallet_sandbox",
        "url": "https://api.sandbox.hyperwallet.com/rest/v4/users/${HYPERWALLET_USER_TOKEN}/bank-cards/${HYPERWALLET_INST_TOKEN}",
        "method": "PUT",
        "sensitive_data": {
            "user": "${HYPERWALLET_USER}",
            "password": "${HYPERWALLET_PW}",
            "cvv": "123",
            "number": "4895142232120006"
        }
    }'
```

**NOTE**
For testing in sandbox, Hyperwallet only accepts a limited set of card numbers. As such, even though in a normal request the card number will come from the payment_method_nonce , for this example we are overwriting that with a literal using the number attribute of sensitive_data . To use the account number of the nonce, as in a normal request, omit the number attribute from sensitive_data .


**NOTE**
Test Values (cvv is 123 for all cards) 
- Working: 4895142232120006
- Working: 4622943126011056
- Error: 4147040070000692
- Flagged: 4622941000000013

 


## Common Issues

### JSON
```json
{
    "error": "Request URL does not match config URL regex",
    "message": {
        "config_regex": "^https://api.sandbox.hyperwallet.com/rest/v4/users/.*/bank-cards/.*$",
        "request_urls": [
            "https://api.sandbox.hyperwallet.com/rest/v4/users/usr-cedff10f-xxxx-42e5-bdf7-2f3abba7a817/bank-cards"
        ],
        "validation_error?": true
    },
    "request-uuid": "b6e56079-c93b-4efe-8ca5-6d4211097d4d"
}
```
 Make sure bank cards have a trailing slash, the correct version is being used, and the URL is appropriate to the environment. 
### JSON
```json
{
    "message ": "The bank account information provided is not configured for your program.",
    "code ": "EXTERNAL_ACCOUNT_TYPE_NOT_SUPPORTED "
}
```
 This error displays when "transferMethodCountry" is not US. 
### JSON
```json
{
    "message": "The request cannot be processed - Please contact our support team for the assistance.",
    "code": "VISADIRECT_ERROR_107"
}
```

Hyperwallet does not accept the traditional [test values](/braintree/docs/reference/general/testing#payment-method-nonces) Braintree has setup for **`payment_method_nonce`**. For sandbox, you can use the test values noted earlier in this document. For UAT, you need to work with your onboarding helper to receive nonce-tokens that represent vaulted debit cards that are then loaded by Forward API and sent to Hyperwallet.

[Next Page:Stripe→](/braintree/docs/guides/extend/forward-api/stripe)

