---
title: "Braintree PayPal Testing and Go Live for Android v5"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/testing-go-live/android/v5"
raw_files:
  - "braintree/docs/guides/paypal/testing-go-live/android/v5-2026-09-16.md"
tags: [braintree, paypal, android, testing, sandbox, production]
---

## Overview

This Braintree-hosted Android v5 route is a snapshot guide to testing a Braintree PayPal integration and moving its server configuration to production. It distinguishes mocked Braintree-sandbox testing from a linked Braintree/PayPal sandbox path, describes eligibility-conditioned PayPal app switching with browser fallback, and separates sandbox state and credentials from production. It is not evidence of current account eligibility, a completed sandbox link, current SDK behavior, or a successful payment, settlement, or deposit. See [[braintree]] and [[braintree-android-sdk]].

## Key takeaways

- Mocked PayPal testing is the default Braintree sandbox path. The page says it simulates PayPal responses with Braintree test values and can check client/server configuration and responses, but it does not send data to a PayPal sandbox account or provide end-to-end testing. Linked PayPal testing instead requires additional setup and the API credentials of a PayPal sandbox test account; the page says the link returns data to both sandbox accounts and supports fuller integration testing.
- The linked flow must not use the PayPal business account as the paying customer account; the page warns that doing so causes declines in linked sandbox testing and production. After linking, some fake nonces may stop working. See the exact setup and warning locators below.
- After `PayPalLauncher().launch`, the page says the SDK attempts to switch to the PayPal app only when it is installed and the user meets eligibility requirements; otherwise it falls back to the default browser. App Switch testing additionally requires an eligible, completed integration. The captured use-case list is structurally ambiguous, so use its line-qualified raw text rather than treating it as an exhaustive or cleanly mapped behavior table.
- Sandbox and production are separate: processing options, recurring-billing settings, login details, merchant ID, and API keys do not transfer. The production transition uses production credentials in server-side code, recommends a dedicated non-employee API user with Account Admin permissions, and requires recreating applicable production account settings. The page says the client continues to obtain its client token from the server without a client-side configuration change.
- Production checks use real payment methods. The page recommends only a limited number of low-value sale transactions for each intended payment-method type, submitted for settlement and checked for bank deposit; any settled test debits the payment method and incurs fees. This is guidance, not proof of an individual transaction, settlement, fee, or deposit.

## Detail locators

- Testing-mode comparison and mocked-flow limits: `# Testing and Go Live`, raw lines 14–31; `## Mocked PayPal testing`, lines 44–48.
- Linked-account prerequisites, account-country condition, API credential fields, fake-nonce warning, and Braintree Control Panel link steps: `## Linked PayPal testing`, lines 51–93.
- PayPal app-switch installed-app and eligibility conditions plus browser fallback: raw line 93.
- App Switch purpose and prerequisites: `## Testing App Switch`, lines 96–103. Sandbox-app installation guidance and the warning that it may override an installed production app: `### Testing your integration using PayPal's sandbox`, lines 105–132.
- Captured App Switch use cases and exclusions: `### Four use cases available for testing`, lines 137–151; `### Use cases not available for testing`, lines 154–160. The first section's flattened bullets and wording do not establish a reliable one-to-one mapping of four named cases.
- Sandbox/production isolation: `## Go Live`, lines 163–168. Dedicated API-user guidance: `### Create an API user`, lines 172–178. Production credential fields and environment/user specificity: `### Get production credentials`, lines 179–188.
- Recreating production settings and changing server configuration: `### Update production account settings`, lines 191–193; `### Update live server configuration`, lines 196–279. Although this is an Android v5 route, that captured section contains Ruby, C#, Python, PHP, Node and Java server examples plus an out-of-place PayPal JS SDK migration sentence at line 263; those artifacts are not Android client behavior or a complete language-support matrix.
- Limited real-payment production checks, settlement/deposit check, fees and sandbox-value prohibition: `## Test transactions in production`, lines 282–286.

## Related

- [[braintree]]
- [[braintree-android-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/testing-go-live/android/v5-2026-09-16|Braintree PayPal Testing and Go Live — Android v5 (2026-09-16)]]
