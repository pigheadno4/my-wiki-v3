<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/transactions/transaction-issues -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Transaction Issues
slug: /articles/control-panel/transactions/transaction-issues/
createTime: '2025-04-02T00:28:35.292Z'
updateTime: '2025-04-02T00:28:35.307Z'
---



# Transaction Issues

Outside of standard [processor declines](/braintree/articles/control-panel/transactions/declines) and [gateway rejections](/braintree/articles/control-panel/transactions/gateway-rejections), additional unexpected issues can occasionally prevent transactions from processing smoothly. Known as transaction issues, these rare occurrences are generally a result of something more complex than a normal declined or rejected transaction.


## Notifications

You may also opt to deliver these notifications via webhook alongside the emails. To receive Transaction Issue Notifications via webhook, first follow the instructions [here](https://developer.paypal.com/braintree/docs/reference/general/webhooks/overview) to ensure the Users receiving the webhook notifications have the proper permissions and a destination URL is prepared and ready for receipt. Then, follow the instructions as further detailed [here](https://developer.paypal.com/braintree/docs/guides/webhooks/create/ruby) to create a webhook


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Select the gear icon in the top right corner
- Select**API**from the drop-down menu
- Select the the**Webhooks tab**
- Select the**Create New Webhook**button
- Provide your[destination URL](https://developer.paypal.com/braintree/docs/guides/webhooks/create/ruby#destination-url)and make your[notification selections](https://developer.paypal.com/braintree/docs/guides/webhooks/create/ruby#notification-kinds)
- Select**Create Webhook**button

You have two options for designating who will receive transaction issue notification – adding a User Recipient or an Email Recipient.

**User Recipients** : This field allows you to send notifications to existing users in the Control Panel. These recipients will receive notifications for the transactions their [role](/braintree/articles/control-panel/users-roles/managing-users-roles) has access to.

**Email Recipients** : This field allows you to send notifications to any email address, regardless of whether the email is associated with a user in the Control Panel. This can be particularly helpful if you use internal distribution lists to monitor transaction issues (e.g. [transaction_issues@yourcompany.com](mailto:/transaction_issues@yourcompany.com) ). Emails entered in this field will receive all transaction issue notifications, even if the address corresponds to a Control Panel user with limited permissions.

