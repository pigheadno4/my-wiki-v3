<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/users-roles/role-permissions -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Role Permissions
slug: /articles/control-panel/users-roles/role-permissions/
createTime: '2025-04-02T00:34:58.359Z'
updateTime: '2025-04-02T00:34:58.395Z'
---



# Role Permissions

When you [create a role](/braintree/articles/control-panel/users-roles/managing-users-roles#creating-and-editing-roles) in the Control Panel, you will select the **Rights Granted** to users assigned that role. These rights are also known as role permissions.

Role permissions are divided into categories. You can assign a role all of the rights within a category or select specific rights from multiple categories.


**NOTE**
 For security, the **Account Admin** role is required to assign users the Manage Roles and Manage Users permissions.

 


## Rights Granted

| **Permission** | **Category** | **Rights Granted** |
| --- | --- | --- |
| Create Sales | Transactions | User can[create transactions](/braintree/articles/control-panel/transactions/create)using new or vaulted payment methods. User can[clone existing transactions](/braintree/articles/control-panel/transactions/clone)if the Submit Sales for Settlement role permission is also enabled. |
| Credit Previous Transactions (Refunds) | Transactions | User can[issue refunds](/braintree/articles/control-panel/transactions/refunds-voids-credits#refunds)for `Settling` or `Settled` transactions. |
| Submit Sales for Settlement | Transactions | User can manually[create new transactions](/braintree/articles/control-panel/transactions/create)and[submit for settlement](/braintree/articles/get-started/transaction-lifecycle#submitted-for-settlement)any `Authorized` transactions. |
| Manage Escrow | Transactions | Users with a Braintree Marketplace account can decide when to release funds that have been held in[escrow](/braintree/articles/guides/braintree-marketplace/processing#escrow). |
| Void Transactions | Transactions | User can[void transactions](/braintree/articles/control-panel/transactions/refunds-voids-credits#voids)that are `Authorized` or `Submitted for Settlement`. |
| Download Transactions with Masked Payment Data | Transactions | User can[run transaction searches via the API](/braintree/docs/reference/request/transaction/search)and[download reports](/braintree/articles/control-panel/reporting/overview)from the Control Panel. |
| Manage Customers and Payment Methods (Add/Edit/Delete) | Customer Management | User can[create new customers in the Vault](/braintree/articles/control-panel/vault/create),[update vaulted customer information](/braintree/articles/control-panel/vault/update),[verify vaulted credit cards](/braintree/articles/control-panel/vault/card-verification#verifying-cards-already-stored),[run customer searches via the API](/braintree/docs/reference/request/customer/search), and[generate a client token via the API](/braintree/docs/start/hello-server/ruby#generate-a-client-token). |
| Download Vault Records with Masked Payment Data | Customer Management | User can[run customer searches via the API](/braintree/docs/reference/request/customer/search)and[export vault records](/braintree/articles/control-panel/vault/overview#exporting-vault-records)from the Control Panel. |
| Create, Run, and Download Reports | Reporting | User can create, run, and download various reports via the[Control Panel](/braintree/articles/control-panel/reporting/overview). This permission does not grant the user access to statements. |
| View Dashboard Graphs | Reporting | User can view the graphs on the main[Dashboard](/braintree/articles/control-panel/overview#dashboard)of the Control Panel. |
| Add/Edit Processing Options | Processing and Security Options | User can make changes within the Processing Options page in the Control Panel, including enabling specific payment methods. This permission also allows users to view[merchant account IDs](/braintree/articles/control-panel/important-gateway-credentials#merchant-account-id). |
| Edit IP Restrictions | Processing and Security Options | User can restrict which IP addresses can take certain actions via the API.[Learn more about allowlisting.](/braintree/articles/risk-and-security/allowlisting) |
| Enable/Disable Premium Fraud Management Tools | Fraud Tools | Users can enable and disable the[Premium Fraud Management Tools](/braintree/articles/guides/fraud-tools/premium/overview)and have access to the[Fraud Protection/Fraud Protection Advanced](/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced)dashboard when Fraud Protection/Fraud Protection Advanced is enabled. |
| View Premium Fraud Management Tools | Fraud Tools | Users can view the[Premium Fraud Management Tools](/braintree/articles/guides/fraud-tools/premium/overview)and have access to the[Fraud Protection/Fraud Protection Advanced](/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced)dashboard when Fraud Protection/Fraud Protection Advanced is enabled. |
| View and Edit Basic Fraud Tools | Fraud Tools | User can view and make changes to the[Basic Fraud Tools](/braintree/articles/guides/fraud-tools/basic/overview)enabled for your account. |
| Edit Filters | Fraud Protection Advanced Dashboard | If you are using[Fraud Protection Advanced (FPA)](/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced), user can edit filters. |
| Make Decisions on Review | Fraud Protection Advanced Dashboard | If you are using[Fraud Protection Advanced (FPA)](/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced), user can make decisions on review. |
| Edit Custom Fields | Fraud Protection Advanced Dashboard | If you are using[Fraud Protection Advanced (FPA)](/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced), user can edit custom fields. |
| Edit Block and Allow List | Fraud Protection Advanced Dashboard | If you are using[Fraud Protection Advanced (FPA)](/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced), user can edit the Block and Allow List |
| Manage Users (Add/Edit/Delete/Reset Password) | User Management | User can create new users, edit existing users, and reset passwords for users logging into the Control Panel.[Learn more.](/braintree/articles/control-panel/users-roles/managing-users-roles) |
| Manage Roles (Add/Edit/Delete) | User Management | User can create new roles, assign and edit role permissions, and delete roles from the Control Panel.[Learn more.](/braintree/articles/control-panel/users-roles/managing-users-roles) |
| Manage Plans, Addons and Discounts (Add/Edit/Delete) | Recurring Billing | User can create new recurring billing plans, edit existing plans, and delete plans from the Control Panel.[Learn more.](/braintree/articles/guides/recurring-billing/plans) |
| Manage Subscriptions (Add/Edit/Delete) | Recurring Billing | User can create new, edit existing, and cancel active subscriptions.[Learn more.](/braintree/articles/guides/recurring-billing/subscriptions) |
| Manage Recurring Email Notifications (Add/Edit/Delete) | Recurring Billing | User can configure email notifications for recurring billing events.[Learn more.](/braintree/articles/guides/recurring-billing/email-notifications) |
| Download Subscription Records | Recurring Billing | User can[run subscription searches via the API](/braintree/docs/reference/request/subscription/search),[search subscriptions](/braintree/articles/guides/recurring-billing/subscriptions#searching-for-subscriptions)in the Control Panel, and download search results as a CSV file. |
| View Modifications | Recurring Billing | User can view but not add, edit, or delete recurring billing add-ons and discounts.[Learn more.](/braintree/articles/guides/recurring-billing/add-ons-discounts) |
| View Subscription Plans | Recurring Billing | User can view but not add, edit, or delete recurring billing plans.[Learn more.](/braintree/articles/guides/recurring-billing/plans) |
| View Subscriptions | Recurring Billing | User can view but not add, edit or delete recurring billing subscriptions.[Learn more.](/braintree/articles/guides/recurring-billing/subscriptions) |
| Search Subscriptions | Recurring Billing | User can[run subscription searches via the API](/braintree/docs/reference/request/subscription/search)and[search subscriptions](/braintree/articles/guides/recurring-billing/subscriptions#searching-for-subscriptions)in the Control Panel. |
| View, manage and contest disputes | Dispute Management | User can view, manage, and[dispute chargebacks](/braintree/articles/risk-and-security/chargebacks-retrievals/disputing-chargebacks). |
| Manage Webhooks (Add/Edit/Delete) | Webhooks | User can create and manage webhooks within the Control Panel.[Learn more.](/braintree/articles/control-panel/webhooks) |
| View Agreements | My Account | User can view your account’s Agreements within the Control Panel. |
| View Statements | Statements | User can view[statements](/braintree/articles/control-panel/reporting/overview#statements)for your account within the Control Panel. Statement availability, timing, and delivery method will vary depending on your account setup. |
| Manage Merchant Accounts | Merchant Accounts | Users in the sandbox can[create new test merchant accounts](/braintree/articles/get-started/try-it-out#testing-currencies). In production, users with a Braintree Marketplace account can onboard sub-merchants and manage sub-merchant accounts.[Learn more.](/braintree/articles/guides/braintree-marketplace/onboarding) |
| Upload business documents | Business Management | User can[securely upload business documents](/braintree/articles/guides/account-information#securely-upload-business-documents)to the Control Panel. |
| Forward Payment Methods with the Forward API | Forward API | Allows API usage of the[Forward API](/braintree/docs/reference/forward-api/overview/). This permission is available to all merchants in sandbox and approved merchants in production. This permission is not included on the Account Admin role. |
| Manage OAuth Applications (Add/Edit/Disable) | OAuth Applications | User can create and manage your OAuth application in the Control Panel. This permission is only available for those merchants participating in the[Braintree Auth](/braintree/docs/guides/braintree-auth/overview)and[OAuth](/braintree/docs/guides/extend/oauth/overview)betas. |
| View Connected OAuth Applications | Connected OAuth Applications | User can view the ecommerce platforms and merchant service providers connected to your OAuth application. This permission is only available for those merchants participating in the[Braintree Auth](/braintree/docs/guides/braintree-auth/overview)and[OAuth](/braintree/docs/guides/extend/oauth/overview)betas. |
| Manage Connected OAuth Applications (Authorize/Deauthorize) | Connected OAuth Applications | User can manage the ecommerce platforms and merchant service providers connected to your OAuth application. User can consent to any scopes requested by any OAuth application, including scopes that correspond to rights that the user does not have. This permission is only available for those merchants participating in the[Braintree Auth](/braintree/docs/guides/braintree-auth/overview)and[OAuth](/braintree/docs/guides/extend/oauth/overview)betas. |
| View Address | Read-Only Access | User can view address information associated to customers and payment methods. |
| View Customers | Read-Only Access | User can view customers. |
| View Merchant Accounts | Read-Only Access | User can view your[merchant accounts.](/braintree/articles/get-started/overview#merchant-account) |
| View Payment Methods | Read-Only Access | User can view (masked) payment method details.[Learn more.](/braintree/articles/get-started/payment-methods) |
| View Transactions | Read-Only Access | User can view transaction details.[Learn more.](/braintree/articles/get-started/transaction-lifecycle) |
| View Verifications | Read-Only Access | User can view card verification details.[Learn more.](/braintree/articles/control-panel/vault/card-verification) |
| Download Files | Read-Only Access | User can download[reporting](/braintree/articles/control-panel/reporting/overview)files and[search](/braintree/articles/control-panel/search)results. |
| Search Customers | Search | User can[search your Braintree Vault.](/braintree/articles/control-panel/search#vault) |
| Search Transactions | Search | User can[search your transaction history.](/braintree/articles/control-panel/search#transactions) |
| Search Verifications | Search | User can[search your card verifications.](/braintree/articles/control-panel/search#verifications) |

