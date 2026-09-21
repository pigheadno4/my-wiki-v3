<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/recurring-billing/email-notifications -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Email Notifications
slug: /articles/guides/recurring-billing/email-notifications/
createTime: '2025-04-02T02:25:44.971Z'
updateTime: '2026-01-20T15:06:49.527Z'
---



# Email Notifications


**NOTE**
 If you want to send email receipts to your customers for every successful sale transaction or refund, see [Email Receipts](/braintree/articles/control-panel/transactions/email-receipts) instead.

 

We can send email notifications to your customers for the following recurring billing events:


- **First Decline**: Sent after the first unsuccessful attempt to charge a customer on a recurring billing cycle
- **First Retry**: Sent after an[automatic attempt](/braintree/articles/guides/recurring-billing/recurring-advanced-settings#automatic-retries)to charge a customer if the initial transaction was unsuccessful
- **Second Retry**: Sent after the next attempt to charge a customer if the first retry was unsuccessful
- **Past Due**: Sent x days after the first decline. You can define x when you configure the**Send options**for your notifications.

We will only send email notifications to your customers for events that leave a subscription in the **Past Due** state. For example, if your account's [retry logic](/braintree/articles/guides/recurring-billing/recurring-advanced-settings#setting-up-retry-logic) is set to cancel subscriptions after the second retry, your customer will only receive a **First Decline** and a **First Retry** email notification - we will not send a **Second Retry** email or any automatic notification when the subscription has been canceled.


## Configuring email notifications

Have the authorized signer on your account contact Support to request activation of this feature. After receiving confirmation from Support, enable email receipts in the Control Panel:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Subscriptions**in the navigation bar
- Click the**Email Notifications**tab
- Click the**Create An Email Notification**button
- Select the recurring billing plan and any[additional options](#configuration-options)
- Click the**Create**button


### Configuration options

On the New Recurring Email Notification page, you can personalize your notification emails by configuring the following fields:


- Sender Email Address: The address customers will see in theFrom:field of your outbound notifications


**NOTE**
 If you want to include a Sender Name in this field, use this format: First Last [&lt;address@example.com&gt;](mailto:&lt;address@example.com&gt;)

 

Subject The text that customers will see in the subject line of your outbound notifications

Body The text that will appear in the body of the email; must be written as plain text

Send options The recurring billing events that will trigger emails to your customers


#### Authorized signer

The authorized signer for your Braintree account is the only person who can request access or make changes to sensitive account information, such as transaction details, bank account information, or statement descriptors. This individual and their associated authorized email address were determined during the application process.

Authorized signers are not the same as the Account Admin [user role](/braintree/articles/control-panel/users-roles/managing-users-roles) in the Control Panel, and can't be managed via the Control Panel; to change your authorized signer or add additional signers, [contact us](/braintree/help/updateBusinessDetails).


**NOTE**
 If an authorized signer calls in to request information about their account, they will need to answer specific security questions to confirm their identity.

 

