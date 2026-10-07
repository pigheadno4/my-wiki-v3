---
title: "Braintree Drop-in Example Integrations"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/start/example-integrations-drop-in/using-the-examples"
raw_files:
  - "braintree/docs/start/example-integrations-drop-in/using-the-examples-2026-09-16.md"
tags: [braintree, drop-in, examples, sandbox, testing]
---

## Overview

This 2026-09-16 snapshot of Braintree's Using the Examples page routes developers to GitHub example repositories for the server-side languages listed on the page. The examples use [[braintree-web-drop-in|Braintree Web Drop-in]] for the client-side integration and are described as end-to-end examples intended to run locally or on Heroku.

This is example and navigation evidence, not proof of exact SDK or package versions, current support status, a runnable environment, or successful payment processing.

## Key takeaways

- The page lists Java (Spring), .NET (ASP.NET), Node.js (Express), PHP, PHP (Slim), Python (Flask), and Ruby (Rails) example repositories.
- Running an example requires a Braintree Sandbox account plus a Merchant ID, public key, and private key; local setup is delegated to each repository's README.
- After an example is running, the page routes test-card transactions to Braintree's testing reference. PayPal testing additionally requires linking a PayPal Sandbox account to the Braintree Sandbox account before using the Sandbox PayPal flow in Drop-in.
- The snapshot warns that Drop-in deprecation begins October 1, 2026, with no new features, improvements, or bug fixes after that date; it says payment processing remains supported until October 1, 2027, when the SDK becomes unsupported and processing may be suspended at any time. It directs migration to the Braintree Android, iOS, or JavaScript SDK. These dates are source-specific snapshot claims, conflict with the September milestones retained in exact-version repository evidence, and do not establish current SDK or support status.

## Detail locators

- Drop-in lifecycle warning and migration routes: raw lines 17-22.
- Example repository list: raw lines 29-38.
- Local/Heroku scope, Sandbox credentials, and README setup route: raw lines 41-52.
- Test-card route: raw lines 55-62.
- Linked PayPal Sandbox setup and Sandbox login flow: raw lines 65-67.

## Related

- [[braintree-web-drop-in]] - prebuilt web checkout UI and source-qualified lifecycle boundary
- [[braintree]] - provider overview

## Raw Sources

- [[raw/braintree/docs/start/example-integrations-drop-in/using-the-examples-2026-09-16|Braintree Using the Examples (2026-09-16 snapshot)]]
