---
title: "Braintree Control Panel Log In with PayPal"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/users-roles/log-in-with-paypal"
raw_files:
  - "braintree/articles/control-panel/users-roles/log-in-with-paypal-2026-09-16.md"
tags: [braintree, control-panel, authentication, paypal, users, account-security]
---

## Overview

This collected Braintree article documents an account-login option that lets a user with an established PayPal account use PayPal credentials to access the Braintree Sandbox or Production Control Panel. It is a credential convenience for two separate accounts: it neither links the PayPal and Braintree accounts nor configures PayPal payment acceptance through the Braintree gateway.

## Key takeaways

- An existing Braintree user enables the option from **My User**, confirms the current Braintree user password, authenticates with PayPal and agrees to the change. After enablement, the user's Braintree credentials are no longer valid; disabling the option switches the user back by confirming the Braintree username and setting a new password.
- Existing Braintree-user two-factor authentication settings do not transfer to the PayPal login. The page directs a user who wants 2FA after switching to set up a PayPal Security Key.
- The article separately states that a user with **User Management** permission can suspend or delete users. Suspension can be reversed, deletion is permanent, and changing a user whose API credentials are used by an integration can break the Braintree connection and cause failed transactions; the page recommends a dedicated API user for integration keys.

## Evidence boundary

> [!warning] Login is not PayPal payment integration
> Log In with PayPal changes how a user authenticates to the Braintree Control Panel. The collected page explicitly says that it does not link the PayPal and Braintree accounts and does not enable PayPal as a Braintree gateway payment method. Payment acceptance requires separate PayPal configuration. Treat the 2026-09-16 snapshot as collected account-access evidence, not proof of current support or payment eligibility.

## Detail locators

- PayPal-credential login, Sandbox and Production destinations, and separate-account boundary: `# Log In with PayPal > ## Log In with PayPal`, line 19.
- Separate PayPal-payment-method setup boundary: note under `## Log In with PayPal`, lines 22-23.
- Existing-account enablement steps and Braintree-credential invalidation: `### Enabling Log In with PayPal on an existing account`, lines 28-47.
- Non-transfer of Braintree-user 2FA and the PayPal Security Key route: `### Two-Factor Authentication with Log In with PayPal`, lines 52-54.
- Disablement route and new-password requirements: `### Disabling Log In with PayPal`, lines 57-74.
- Suspend/delete permission, reversibility and API-credential integration warning: `## Deleting or suspending users`, lines 77-91.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/guides/payment-methods/paypal/setup-guide-2026-09-16|Braintree PayPal payment-method setup guide]] - unread navigation-only route linked for separately configuring PayPal payment acceptance; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/users-roles/log-in-with-paypal-2026-09-16|Braintree Control Panel Log In with PayPal]] - complete collected article covering PayPal-credential login, account separation, credential and 2FA transitions, disablement and the user-administration warning
