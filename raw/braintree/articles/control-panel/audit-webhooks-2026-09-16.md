<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/audit-webhooks -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Audit Webhooks
slug: /articles/control-panel/audit-webhooks/
createTime: '2025-04-01T23:10:42.267Z'
updateTime: '2025-04-01T23:10:42.293Z'
---



**AVAILABILITY**
 **Audit Webhooks are currently only available to select partners.**

 

Audit Webhooks are a specialized system of automated notifications indicating that an authentication event has occurred in your gateway. Rather than requiring you to pull information via our API, webhooks push information to your designated destination when important events occur.

Webhooks allow you to develop a workflow for how your server responds to the information provided in a notification (e.g. setting up your server to send an email to any customers whose subscriptions have expired).

For general information on Braintree webhooks, refer to [Create webhooks](/braintree/articles/control-panel/webhooks).


## API


### Notifications

Braintree::WebhookNotification::Kind::IpRestrictionsChanged Braintree::WebhookNotification::Kind::TokenizationKeyCreated Braintree::WebhookNotification::Kind::TokenizationKeyDestroyed Braintree::WebhookNotification::Kind::ApiKeyCreated Braintree::WebhookNotification::Kind::ApiKeyDestroyed Braintree::WebhookNotification::Kind::TwoFactorChanged

The following table describes the conditions that trigger each kind of webhook.

| Notification Type | Description |
| --- | --- |
| ip_restrictions_changed | IP restrictions have been changed. |
| tokenization_key_created | A tokenization key has been created. |
| tokenization_key_destroyed | A tokenization key has been destroyed. |
| api_key_created | An API key has been created. |
| api_key_destroyed | An API key has been destroyed. |
| two_factor_changed | A user has changed two factor authentication. |


## Login


### Notifications

Braintree::WebhookNotification::Kind::UserPasswordReset Braintree::WebhookNotification::Kind::UserLogin Braintree::WebhookNotification::Kind::UserSsoLogin Braintree::WebhookNotification::Kind::UserLoginFailed

The following table describes the conditions that trigger each kind of webhook.

| Notification Type | Description |
| --- | --- |
| user_password_reset | A password has been reset for a user. |
| user_login | A user has successfully logged into the Control Panel. |
| user_sso_login | A user has successfully logged into the Control Panel through SSO. |
| user_locked_out | A user has been locked out of the Control Panel. |


## AuthZ


### Notifications

Braintree::WebhookNotification::Kind::RoleCreated Braintree::WebhookNotification::Kind::RoleChanged Braintree::WebhookNotification::Kind::RoleAssigned Braintree::WebhookNotification::Kind::RoleUnassigned Braintree::WebhookNotification::Kind::UserSuspensionChanged

The following table describes the conditions that trigger each kind of webhook.

| Notification Type | Description |
| --- | --- |
| role_created | A role has been created. |
| role_changed | A role's rights have been changed. |
| role_assigned | A role has been assigned to a user. |
| role_unassigned | A role has been unassigned from a user. |
| user_suspension_changed | A user suspension status has changed. |


## OAuth


### Notifications

Braintree::WebhookNotification::Kind::OAuthAccessGranted Braintree::WebhookNotification::Kind::OAuthApplicationCreated Braintree::WebhookNotification::Kind::OAuthApplicationChanged

The following table describes the conditions that trigger each kind of webhook.

| Notification Type | Description |
| --- | --- |
| oauth_access_granted | A connected merchant has granted API access. |
| oauth_application_created | A connected merchant has created an OAuth application. |
| oauth_application_changed | A connected merchant has made changes to an OAuth application. |


## Fraud Protection


### Notifications

Braintree::WebhookNotification::Kind::AvsRulesChanged Braintree::WebhookNotification::Kind::CvvRulesChanged Braintree::WebhookNotification::Kind::RiskThresholdCreated Braintree::WebhookNotification::Kind::RiskThresholdDeleted Braintree::WebhookNotification::Kind::RiskThresholdChanged Braintree::WebhookNotification::Kind::PremiumFraudProtectionChanged

The following table describes the conditions that trigger each kind of webhook.

| Notification Type | Description |
| --- | --- |
| avs_rules_changed | The AVS rules have been changed. |
| cvv_rules_changed | The CVV rules have been changed. |
| risk_threshold_created | A risk threshold rule has been created. |
| risk_threshold_deleted | A risk threshold rule has been deleted. |
| risk_threshold_changed | A risk threshold rule has been changed. |
| premium_fraud_protection_changed | Premium fraud protection has been changed. |


## Shared Attributes

| Notification Type | Description |
| --- | --- |
| kind (enum) | The kind of webhook notification. |
| timestamp (string) | The UTC time at which the webhook was triggered. |

