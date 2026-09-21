<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/account-information -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Updating Account Information
slug: /articles/guides/account-information/
createTime: '2025-04-01T22:19:52.091Z'
updateTime: '2026-06-15T15:32:04.840Z'
---



# Updating Account Information


## Control Panel login credentials

Anyone can reset their password by clicking the **Forgot** link on the [sign-in page](https://www.braintreegateway.com/login). Alternatively, users with the Manage Users permission can [change passwords and make other changes to users](/braintree/articles/control-panel/users-roles/managing-users-roles#editing-users) in the Control Panel.

If you would like to [update the email address](/braintree/articles/control-panel/users-roles/managing-users-roles#editing-users) associated with your Control Panel user, click on your user icon in the top right corner, and click **My User** from the drop-down menu. You must have access to the original email account in order to confirm the update. If you no longer have access to the original email account, you should [create a new user](/braintree/articles/control-panel/users-roles/managing-users-roles#creating-users).


## Securely upload business documents

In some situations, we may ask you to provide us with sensitive information or documentation (e.g. if you request to update your bank account information, we'll ask you to provide specific bank documentation). Account Administrators and users with the Business Management [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-upload-business-documents) can upload all requested documents in the Control Panel.

You can upload documents by following these steps:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Business**from the drop-down menu
- Click the**Documents**tab
- Next to**Business Uploads**, click the**Upload Business Documents**button
- Select the reason for uploading your document from the drop-down menu
- In theNotesfield, enter your case number and/or the Support representative's name that you’ve been in contact with
- Click the**Continue to Add Documents**button
- Click the**Add Document**button and select the file you'd like to upload
- Click the**Finish & Send Documents**button

After you complete these steps, the appropriate team will be notified and will follow up with you.


**NOTE**
 The Business Uploads tool can accept PNG, JPG, PDF, CSV, XLS, XLSL, and XLSX files. Password-protected documents are not supported and will cause an upload error.

 


## Bank account information

We partner with different banks to provide merchant account services to businesses around the globe. Those partners have different requirements for account changes, based in part on local regulations. You can find a list of the documents required in your region within the bank specific support articles you received at the time of your onboarding. If you are unsure of your account setup, [contact us](/braintree/help?issue=changeBankAccount) for more information on what you'll need to provide.

If you are located in the United States, you can submit a bank account change request directly from the [Control Panel](https://www.braintreegateway.com/login).As part of the request, you will be asked to provide supporting documentation for your new account.

If you are located outside the United States, [contact us](https://developer.paypal.com/braintree/help/changeBankAccount) for information about the documentation and approvals required to process your request.


**NOTE**
 The account submitted must be a business checking account. Savings, deposit-only, and prepaid debit accounts will not be accepted.

 


### Viewing your bank account information

Merchants using Braintree Direct that are located in the US and EU can view the bank account associated with their merchant accounts in the Control Panel. This is the bank account that we send funds – or disbursements – to. To view your disbursements account:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Business**from the drop-down menu
- Scroll down to the**Merchant Accounts**section
- Under theBank Accountcolumn for the account of your choice, click the**View**link

The Disbursement Bank Account page has both the routing number and the last four digits of the bank account associated with the selected merchant account.


**NOTE**
 Users can only access the Disbursement Bank Account page if the merchant account they are trying to view is included in their role permissions. If you need to view an account that is not included, have your account admin [edit your user](/braintree/articles/control-panel/users-roles/managing-users-roles#editing-users) to include that merchant account.

 


## Other types of updates

Only the [**authorized signer**](#authorized-signer) on your account can request to access or update specific account details. If anyone other than the authorized signer reaches out regarding these details, we will require the authorized signer to [Contact us](/braintree/help/updateBusinessDetails) via their associated email address with permission to proceed.

The following account details cannot be changed without written consent from your authorized signer:


- Legal name
- DBA (Doing Business As)
- Contact information
- Product or website changes
- Control Panel time zone
- [Statement descriptor](/braintree/articles/control-panel/transactions/descriptors)


### Authorized signer

The authorized signer for your Braintree account is the only person who can request access or make changes to sensitive account information, such as transaction details, bank account information, or statement descriptors. This individual and their associated authorized email address were determined during the application process.

Authorized signers are not the same as the Account Admin [user role](/braintree/articles/control-panel/users-roles/managing-users-roles) in the Control Panel, and can't be managed via the Control Panel; to change your authorized signer or add additional signers, [Contact us](/braintree/help/updateBusinessDetails).


**NOTE**
 If an authorized signer calls in to request information about their account, they will need to answer specific security questions to confirm their identity.

 


### VAT registration number


#### What is a UK VAT registration number?

A UK VAT registration number is a unique nine-digit code issued by HMRC, the UK Tax Authority, to any business which is registered to pay UK VAT. As per current UK VAT legislation, businesses need in principle to VAT register as soon as they have a turnover in the last 12 months exceeding a certain threshold (GBP 90K – situation on 1 September 2024).


#### When do I need to provide my UK VAT registration number to Braintree/PayPal?

We require you to provide us with the (new) UK VAT registration number of your business immediately:


- In case you are a business established and VAT registered in UK
- In case your UK business was previously not VAT registered but now obtained a UK VAT registration number
- In case the UK VAT registration number of your business has changed

