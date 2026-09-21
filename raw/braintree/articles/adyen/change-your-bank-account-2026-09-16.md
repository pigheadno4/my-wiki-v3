<!-- Source URL: https://developer.paypal.com/braintree/articles/adyen/change-your-bank-account -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Change Your Bank Account
slug: /articles/adyen/change-your-bank-account/
createTime: '2025-04-01T23:34:19.142Z'
updateTime: '2025-04-01T23:34:19.156Z'
---


Change Your Bank AccountAs a part of your original application, you provided bank information for a checking account associated with your business. All settled transactions paid out to this bank account according to the [settlement and funding timeline](/braintree/articles/adyen/transactions/settlement-funding-timeline).


## Updating bank account information

If you'd like to change your business bank account information, upload a recent bank statement for your new account using our [Business Uploads Tool](/braintree/articles/guides/account-information#securely-upload-business-documents) in the Control Panel.


**NOTE**
 Screenshots of an online banking profile will not be accepted.

 

Make sure that the provided document includes all of the following details:


- Account holder’s name (must match the DBA or legal name of business)
- Account currency
- Bank insignia
- IBAN
- BIC/SWIFT Code

Our Support team will review the uploaded bank statement and follow up with the [authorized signer](#authorized-signer) of your account.


**NOTE**
 The account submitted must be a business checking account domiciled in the same country as your business. Savings, deposit-only, and prepaid debit accounts will not be accepted.

 


### Authorized signer

The authorized signer for your Braintree account is the only person who can request access or make changes to sensitive account information, such as transaction details, bank account information, or statement descriptors. This individual and their associated authorized email address were determined during the application process.

Authorized signers are not the same as the Account Admin [user role](/braintree/articles/control-panel/users-roles/managing-users-roles) in the Control Panel, and can't be managed via the Control Panel; to change your authorized signer or add additional signers, [Contact us](/braintree/help/updateBusinessDetails).


**NOTE**
 If an authorized signer calls in to request information about their account, they will need to answer specific security questions to confirm their identity.

 


## Multi-currency settlement

You can associate one checking account with each of the settlement currencies set up for your Braintree account. While we will deposit funds into your bank accounts in the associated settlement currency, Adyen will debit fees in the base currency established with your original application (either GBP or EUR).

