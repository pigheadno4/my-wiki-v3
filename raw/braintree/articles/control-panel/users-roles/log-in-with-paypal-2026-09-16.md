<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/users-roles/log-in-with-paypal -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Log In with PayPal
slug: /articles/control-panel/users-roles/log-in-with-paypal/
createTime: '2025-04-01T23:03:07.732Z'
updateTime: '2025-04-01T23:03:07.752Z'
---



# Log In with PayPal


## Log In with PayPal

If you already have an established PayPal account, you can choose to use your PayPal username and password to log into the Braintree [sandbox](https://sandbox.braintreegateway.com/login) or [production](https://www.braintreegateway.com/login) environments. While this does not link your PayPal and Braintree accounts in any way, it does allow you the convenience of using only one set of login credentials for two separate accounts.


**NOTE**
 Enabling Log In with PayPal does not automatically set up your Braintree account to accept PayPal as a payment method. If you would like to accept PayPal via the Braintree gateway, you’ll need to [configure PayPal](/braintree/articles/guides/payment-methods/paypal/setup-guide) separately.

 


### Enabling Log In with PayPal on an existing account

If you already have Braintree user credentials and you would like to Log In with PayPal instead:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on your user icon in the top right corner
- Click**My User**from the drop-down menu
- Scroll to the**Log In with PayPal**section
- Click the**Enable**button
- Enter your Braintree user password when prompted
- Click the**Log In with PayPal**button
- Enter your PayPal user credentials in the PayPal pop up and click the**Log In**button
- Click the**Agree**button

You’ll receive an email confirming your switch to Log In with PayPal and letting you know your Braintree credentials are no longer active.


**NOTE**
 Once you’ve enabled Log In with PayPal on your account, your Braintree credentials will no longer be valid. If you would like to switch back, you can do so at any time by [disabling log in with PayPal](#disabling-log-in-with-paypal).

 


### Two-Factor Authentication with Log In with PayPal

If you have 2FA set up for your Braintree user and you switch to Log In with PayPal, your 2FA settings will not transfer. If you would like 2FA, you’ll need to set up a [PayPal Security Key](https://www.paypal.com/webapps/mpp/security/security-protections).


### Disabling Log In with PayPal

If you’d like to switch back to using your Braintree credentials, follow these steps:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on your user icon in the top right corner
- Click**My User**from the drop-down menu
- Scroll to the**Log In with PayPal**section
- Click the**Disable**button
- Confirm your Braintree username and enter a new password

New passwords must meet the following criteria:


- Must be at least 7 characters
- Must include at least 1 letter and 1 number
- Can't be one of the last 4 previously used passwords


## ​Deleting or suspending users

If you have User Management permissions, you can suspend or delete users. Suspended users can be reactivated; deleted users will be permanently removed.


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Team**from the drop-down menu
- Locate the user you'd like to make changes to
- Click either the**Suspend**or**Delete**link to the right of the user
- Click the**Yes**button to confirm your selection


**IMPORTANT**
 Be cautious when deleting or suspending users whose API credentials may be included in your integration – this could break your connection to Braintree and result in failed transactions. To avoid potential issues, we recommend [creating an API user](/braintree/docs/start/go-live#create-an-api-user) for the sole purpose of using their API keys for your integration.

 

