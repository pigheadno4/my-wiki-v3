<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/apple-pay/testing-go-live -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Testing and Go Live
slug: /docs/guides/apple-pay/testing-go-live/
createTime: '2025-04-01T21:49:14.848Z'
updateTime: '2025-07-16T16:04:05.661Z'
---



# Testing and Go Live

In order to test the entire Apple Pay user flow, use a[device that supports Apple Pay](https://support.apple.com/en-us/HT208531). To test Apple Pay on the web, use the Safari or Chrome browser.

In the sandbox environment, Braintree accepts[Apple Pay Sandbox test cards](https://developer.apple.com/apple-pay/sandbox-testing)from the device. Using these test cards requires that your device is signed into an[iCloud sandbox tester account](https://help.apple.com/app-store-connect/#/dev8b997bee1). Please note that the Braintree sandbox environment returns a payment method nonce with dummy data ("Jane Doe"), even when decryption is successful. You can simulate server behaviors by using[test amounts on your transactions](/braintree/docs/reference/general/testing#transaction-amounts)and[test nonces](/braintree/docs/reference/general/testing#payment-method-nonces).

In our production environment, the payment data is decrypted with an Apple Pay certificate that is securely stored on our servers. You should expect to see the same device account number (DPAN) in Wallet (formerly Passbook) and in the Braintree Control Panel.

If Apple Pay tokenization fails during development, it is likely caused by a certificate mismatch. You can determine which certificate was used for encryption based on thePKPaymentToken(payment.token.paymentDataheader.publicKeyHashfield) on iOS orApplePayPaymentToken(payment.token.paymentDataheader.publicKeyHashfield) on the web.
## Go live


- Run a few real transactions to ensure that you are able to process Apple Pay for all[supported card types](/braintree/articles/guides/payment-methods/apple-pay#availability).
- Apple Pay requires coordination from acquiring banks, issuing banks, and card networks. Please email us if your live transactions are declined.

