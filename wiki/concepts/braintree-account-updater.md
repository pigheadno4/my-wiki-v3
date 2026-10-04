---
title: "Braintree Account Updater"
type: concept
category: technology
tags: [braintree, account-updater, vault, cards, recurring-billing]
---

## Braintree Account Updater

Braintree Account Updater is an optional Braintree Direct feature that requests updated account numbers and/or expiration dates from participating issuers for supported vaulted cards and applies returned changes to the Vault. The collected guide limits merchant eligibility to businesses based in the US or transacting primarily with US customers, says pricing varies by pricing model, and states that the feature is not enabled by default. Issuer participation remains a separate card-level condition, so a supported card brand does not guarantee an update. [[source-braintree-articles-guides-account-updater]]

## Operating boundaries

The collected guide lists vaulted Visa, Mastercard and Discover credit cards, excludes prepaid cards and cards processed through Apple Pay or Google Pay, and documents an initial request followed by rolling request criteria. A Vault containing more than 2 million payment methods receives the guide's narrower initial expired-card scope. Next Day Card Refresh depends on configured retry logic; exact thresholds, transaction-activity conditions and decline codes remain in the source's verified raw locators. [[source-braintree-articles-guides-account-updater]]

Reporting exposes successful and unsuccessful or action-required outcomes through payment-method history, a Control Panel report and a daily-report webhook. For `Call customer - account closed`, `Call customer for updates`, `Call issuer for updates` or `Do not retry`, Braintree says it will not resend the card until the payment method is manually updated in the Control Panel or through the API. An update request is not proof of issuer participation, a successful Vault change or a successful later payment. [[source-braintree-articles-guides-account-updater]]

## Sources

- [[source-braintree-articles-guides-account-updater]] - unversioned Braintree guide to Account Updater eligibility, issuer-dependent Vault update requests, rolling criteria, retry dependency, reporting and terminal no-resend outcomes
- [[source-braintree-control-panel-reporting-expiring-cards]] - separate Control Panel report for identifying expired or soon-to-expire Vault cards; report visibility is not an update request
- [[source-braintree-webhooks-account-updater-node]] - feature-restricted Node.js reference for the Account Updater daily-report webhook
