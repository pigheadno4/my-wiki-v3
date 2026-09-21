<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/setup-guide -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Setup Guide
slug: /articles/guides/payment-methods/paypal/setup-guide/
createTime: '2025-04-01T23:38:34.767Z'
updateTime: '2025-04-01T23:38:34.785Z'
---



# Setup Guide

Once you have confirmed that your merchant account is [eligible to accept PayPal transactions](/braintree/articles/guides/payment-methods/paypal/overview#availability), you must complete the following steps to add this payment method to your Braintree integration:


- Sign up for a free, verified PayPal Business Account
- Enter your PayPal credentials in the Braintree Control Panel
- Add PayPal as a payment method using our[PayPal guide in the developer docs](/braintree/docs/guides/paypal/overview)


## Required steps


### Sign up for a PayPal Business Account

In order to use PayPal with Braintree, you'll need a PayPal Business Account. You can either sign up for a new account on [PayPal's website](https://www.paypal.com/webapps/mpp/referral/paypal-business-account), or upgrade an existing [PayPal Premier account](https://www.paypal.com/cgi-bin/webscr?cmd=p/gen/personal_vs_business-outside) by completing the following steps:


- Go to the[Settings page](https://www.paypal.com/myaccount/settings/)in your PayPal account
- Click**Upgrade to a Business account**
- Enter your business information and follow the remaining prompts


**NOTE**
 After setting up your new PayPal Business Account, you will need to verify specific personal information, such as your bank account details. Navigate to your profile in the [PayPal console](https://www.paypal.com/login) and follow the prompts to complete the verification process. If you are having trouble, [contact PayPal support](#contacting-paypal-support).

 


### Enter your PayPal credentials in the Braintree Control Panel

You must enter your PayPal Business Account credentials in the Braintree Control Panel to enable this payment method in production. You can only link one PayPal account to your Braintree gateway. To complete your PayPal setup:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Processing**from the drop-down menu
- Scroll to the**Payment Methods**section
- Next to**PayPal**, click the toggle to access the**Accept PayPal**options page
- Click the**Log In with PayPal**button
- Enter your PayPal login credentials and click**Log In**
- Click the**Submit**button


**NOTE**
 If your Braintree account was recently approved, you may not see the option to enter PayPal login credentials in the Control Panel. It can take a few business days for your account to be fully set up and for this option to become available. [Contact us](/braintree/help/acceptPaymentTypes) for more information.

 


#### REST API app

Once you have successfully linked your PayPal Business Account to your Braintree Control Panel, you may notice that a REST API app has been created in your [PayPal Apps Control Panel](https://developer.paypal.com/developer/applications). This app allows Braintree to interact with the PayPal API on your behalf; without it, you will be unable to process PayPal transactions through your Braintree account. We recommend that you do not delete the REST API app at any time.


## Recommended setup options


### Managing disputes in the Braintree Control Panel

To keep your transaction management in a centralized location, we recommend enabling PayPal disputes in your Braintree Control Panel. [Learn more in our PayPal disputes support article.](/braintree/articles/guides/payment-methods/paypal/disputes#setup)


### Settlement Withdrawal

To keep funding as simple as possible, we recommend that you enable Settlement Withdrawal on your account by [contacting PayPal](#contacting-paypal-support). [Read more about Settlement Withdrawal, funding, and reconciliation.](/braintree/articles/guides/payment-methods/paypal/funding-reconciliation)


### eCheck payments

An eCheck, or electronic check, is a payment sent directly from your customer's bank account. **Braintree does not support these transactions at this time**. If your PayPal Business Account allows for eCheck payment attempts, attempted eCheck authorizations may be successful, but the associated transactions will be automatically [voided](/braintree/articles/control-panel/transactions/refunds-voids-credits#voids).

To provide a better experience for your customers, we recommend blocking eCheck payments before the authorization. You can do so by [adjusting your payment receiving preferences](https://www.paypal.com/selfhelp/article/FAQ2406/1) within your PayPal account settings.


### Foreign currencies

To accept PayPal payments in multiple currencies, you must first complete the following steps:


- Confirm that you have a Braintree merchant account for each currency you'd like to accept –[contact us](/braintree/help/acceptCurrencies)if you need assistance
- Set up your PayPal account to allow payments in foreign currencies –[learn more in PayPal's developer docs](https://developer.paypal.com/api/nvp-soap/paypal-payments-standard/admin/setup-account/#handle-multiple-currencies)

Once you're set up, you will [specify a Braintree merchant account](/braintree/docs/reference/request/transaction/sale/ruby#specify-merchant-account-id) when processing PayPal transactions in order to present different currencies to your customers.


#### Avoiding conversion and cross border fees

You can [adjust your payment receiving preferences](https://developer.paypal.com/api/nvp-soap/paypal-payments-standard/admin/setup-account/#accept-or-deny-cross-currency-payments) to block all payments in foreign currencies. While doing so will allow you to avoid additional fees, it will also prevent you from selling to customers who don't use your account currency.


**IMPORTANT**
 Depending on your account setup, PayPal may assess conversion and cross border fees when processing transaction in foreign currencies. If you had previously adjusted your payment receiving preferences, check the toggle setting on your PayPal Business Account to make sure that it reflects how you wish to handle payments in foreign currencies.

 


## Contacting PayPal support

Many account changes can be made directly in your PayPal console (e.g. your funding bank account), but you may need to call to request certain setup options (e.g. Settlement Withdrawal). For the fastest service via phone, it’s best to log into your [PayPal account](https://www.paypal.com/login), click **Contact Us**, and then click **Call us**. This will give you a passcode, which you can provide to PayPal to immediately verify your identity when you call. Passcodes expire in 60 minutes.

To send an email instead, log into your [PayPal account](https://www.paypal.com/login), click **Contact Us**, and then click **Email us**.

