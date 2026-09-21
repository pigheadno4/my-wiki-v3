<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/vault/card-verification -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Card Verification
slug: /articles/control-panel/vault/card-verification/
createTime: '2025-04-02T01:26:54.717Z'
updateTime: '2026-05-28T13:42:02.387Z'
---



# Card Verification


**AVAILABILITY**
 Our card verification feature only works with credit and debit card payment methods.

 

Card verification is a strong first-line defense against potentially fraudulent cards. It ensures that the credit card number provided is associated with a valid, open account and can be stored in the Vault and charged successfully. We can verify the following fields with the customer’s bank:


- Card number
- Card expiration date
- Street address and postal code
- CVV

If card verification is enabled, the gateway will verify that credit cards are valid and pass any of your configured [AVS and CVV rules](/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules) before they are stored in the Vault. Cards that are not valid will not be stored in the Vault.

Braintree strongly recommends verifying all cards before they are stored in your Vault by [enabling card verification](#enabling-card-verification) for your entire account in the Control Panel.


## How it works

The Braintree gateway verifies credit cards by running either a $0 or $1 authorization and then automatically voiding it. For most processors and card brands, transactions are initially tried with a $0 authorization. If $0 authorizations are not supported, a $1 authorization will be performed automatically.

In any instance where a $1 authorization returns a successful result, we immediately follow up with an automatic [void request](/braintree/articles/control-panel/transactions/refunds-voids-credits#voids) to ensure that the transaction does not settle and that it disappears from the cardholder's statement as soon as possible.


**NOTE**
 Some banks don't recognize void requests immediately. It's possible that after the void is issued, your customer will still see the pending charge. If this happens, have your customer call their bank; the bank should be able to see the void request and update your customer's bank statement accordingly.

 


## Enabling card verification

To enable card verification for all cards as they are entered into the Vault:


- Log into the[Control Panel](https://www.braintreegateway.com/login).
- Click on the gear icon in the top right corner.
- Click**Processing**from the drop-down menu.
- Scroll to the**Vaulting**section.
- Next to**Card Verification**, click the toggle to turn it on.


**NOTIFICATION**
For information about verifying cards for Apple Pay transactions, see [Enabling Apple Pay card verification](/docs/guides/apple-pay/server-side/ruby#apple-pay-verification) .



If enabled, the gateway will verify that credit cards are valid and that they pass configured [AVS/CVV rules](/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules) before they are stored in the Vault. Cards that are not valid will not be stored in the Vault.


**NOTE**
 You can also choose to verify cards individually if you prefer. [Learn more about card verification in our developer docs.](/braintree/docs/guides/credit-cards/server-side#card-verification) For Apple Pay transactions, see [these instructions](https://developer.paypal.com/braintree/docs/guides/apple-pay/server-side/ruby/?mode=preview#one-time-requests) instead.

 


## Retrying all failed $0 verifications

Certain banks using Visa and Mastercard do not accept $0 as a valid transaction amount. These banks typically respond with a specific decline code that tells us that we should retry the authorization with an amount of $1, which we do automatically. However, in cases where we're sent a generic decline code, the authorization is not retried by default.


**NOTE**
 If Apple Pay card verification fails, you must retry verification manually. For more information about card verification for Apple Pay transactions, see [Apple Pay card verification](https://developer.paypal.com/braintree/docs/guides/apple-pay/server-side/ruby/?mode=preview#apple-pay-card-verification).

 

To attempt to avoid rejecting otherwise valid cards, you can opt to retry all failed $0 authorizations as $1 authorizations, regardless of the processor decline response.

To enable this feature:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Processing**from the drop-down menu
- Scroll to the**Vaulting**section
- Next to**Card Verification – Retry All Failed $0**, click the toggle to turn it on


**NOTE**
 You can enable **Retry All Failed $0** verifications even if you disable **Card Verification** by requesting individual card verifications using the API. [Learn more in our developer docs.](/braintree/docs/guides/credit-cards/server-side#card-verification)

 


## Verifying vaulted cards



 Due to PCI compliance restrictions, we never store your customer’s CVV. You’ll need to collect this from them again before re-verifying a card through the Control Panel or API.

 

To re-verify a card that is already stored in a Vault record:


- Log into the[Control Panel](https://www.braintreegateway.com/login).
- Select**Vault**in the navigation bar.
- Scroll to the**Customer Search**section.
- Define your desired parameters, and select**Search**.
- Select the link in theTokencolumn of the record you want to re-verify.
- Select the**Edit**button at the top of the page.
- Select theVerify cardbox at the bottom of the**Payment Method Details**section.
- Enter the card's CVV.
- Select the**Save**button.

The verification result appears on the next page, along with the CVV and AVS Responses.

You also can perform e-verification through the API. [Learn more in our developer docs.](/braintree/docs/reference/request/payment-method/update#card-verification)

