---
title: "Braintree PayPal Testing and Go Live (iOS v7)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/testing-go-live/ios/v7"
raw_files:
  - "braintree/docs/guides/paypal/testing-go-live/ios/v7-2026-09-16.md"
tags: [braintree, paypal, ios, ios-v7, testing, sandbox, production, app-switch]
---

## Overview

This 2026-09-16 Braintree website snapshot is the PayPal Testing and Go Live guide routed under iOS v7. It distinguishes mocked from linked PayPal sandbox testing, documents an eligibility-qualified PayPal App Switch test path with browser-session fallback, and separates the production server credential/environment change from the unchanged iOS client-token configuration. It is Braintree-hosted website guidance for this route, not evidence for sibling platforms or versions, current availability or account eligibility, a standalone direct PayPal integration, exact-SHA SDK behavior, or successful payment, settlement, or funding.

## Key takeaways

- Mocked testing uses Braintree sandbox credentials and test values to check client- and server-side configuration and simulated responses, but it does not send data to a PayPal sandbox account or provide end-to-end testing. Linked testing requires separate setup, connects the Braintree and PayPal sandbox accounts, returns data to both, and is the route described for fuller functionality such as reporting and email receipts.
- The page warns not to use the merchant's PayPal business account as the customer account in linked testing or production because the transaction will decline. It also notes that linking a PayPal sandbox account can cause some fake nonces to stop working.
- For App Switch, after `tokenize` the SDK attempts to open the PayPal app only when it is installed and the user is eligible; otherwise it falls back to `ASWebAuthenticationSession`. The production-app test path is limited to US developers and requires the sign-in email to match `userAuthenticationEmail`; the separate sandbox-app path requires Firebase access and is presented for teams inside or outside the US.
- The sandbox build overrides an installed production PayPal app, so the page directs testers to delete existing PayPal apps first. It also warns that selecting **Complete Transaction** after returning to the merchant app can charge a real card linked to the test account. System errors, app-launch failure, activity-feed updates, and non-App-Switch screens are listed as unavailable sandbox-app test cases.
- Sandbox artifacts do not transfer to production. Production merchant ID and public/private API keys are environment- and user-specific and must be kept in server-side configuration. The page recommends using credentials for a dedicated API user with Account Admin permissions and an email address not tied to one employee, rather than an individual user's credentials, because deleting or suspending that individual can break the Braintree connection and cause failed transactions. The iOS client needs no production configuration change because it receives a client token from the server. Production checks use real payment methods, limited low-value sales submitted for settlement, and can debit the payment method and incur fees; the described bank-deposit confirmation is an instructed check, not proof that any deposit occurred.

> [!warning] Unresolved App Switch scope
> This website snapshot documents testing App Switch with both the PayPal production app and a PayPal sandbox app. The independently retained exact-SHA iOS SDK concept records source comments that call the optional v7 app-switch API beta and production-only. Preserve both source-qualified statements; this page does not establish which scope is current or reconcile the website and implementation evidence.

## Detail locators

- Mocked versus linked sandbox behavior and the business-account decline warning: raw lines 16-37.
- Linked PayPal sandbox account, app, credential, Control Panel, and fake-nonce setup: raw lines 42-89.
- App Switch eligibility, `ASWebAuthenticationSession` fallback, production-app prerequisites, email match, and post-transaction checks: raw lines 92-132.
- Sandbox-app prerequisites, destructive app replacement, Firebase installation, certificate trust, and verification: raw lines 134-182.
- Sandbox-app FAQ, real-card charge warning, demo settings, supported use cases, and unavailable cases: raw lines 185-256.
- Sandbox/production isolation, API-user guidance, credential scope, production account recreation, server examples, and unchanged client-token configuration: raw lines 259-375.
- Limited production sales, settlement/deposit check, real-payment-method requirement, debits, and fees: raw lines 378-382.

## Related

- Company: [[braintree]]
- Concepts: [[braintree-ios-sdk]], [[paypal-braintree-integration]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/testing-go-live/ios/v7-2026-09-16|Braintree PayPal Testing and Go Live — iOS v7 (2026-09-16)]]
