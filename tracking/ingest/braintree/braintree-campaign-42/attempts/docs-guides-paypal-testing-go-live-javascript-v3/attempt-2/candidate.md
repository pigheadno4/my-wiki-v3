---
title: "Braintree PayPal Testing and Go Live (JavaScript v3)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/testing-go-live/javascript/v3"
raw_files:
  - "braintree/docs/guides/paypal/testing-go-live/javascript/v3-2026-09-16.md"
tags: [braintree, paypal, javascript-v3, sandbox, production, testing]
---

## Overview

This collected Braintree guide at the JavaScript v3 PayPal route distinguishes mocked and linked PayPal Sandbox testing, then documents App Switch and dispute test procedures plus the separate move to Production. It is a website snapshot and does not establish a current `braintree-web` package version, merchant or buyer eligibility, successful payment execution, settlement, dispute synchronization, or funding.

## Key takeaways

- Mocked PayPal testing is the default. It uses Braintree Sandbox test values to simulate responses and can check client- and server-side configuration, but it is not end-to-end, sends no data to the PayPal Sandbox account, and does not work with the PayPal Checkout component of the JavaScript v3 SDK.
- Linked PayPal testing requires additional setup and connects the Braintree Sandbox account to a PayPal Sandbox account. The page says data returns to both Sandbox accounts and the route can exercise broader integration behavior such as transaction reporting and email receipts; these remain Sandbox results, not live-payment proof.
- Linking requires credentials for a PayPal business Sandbox account using the same country as the Braintree Sandbox account and an app under the same Sandbox developer account. After linking, some fake nonces may stop working. The page warns not to use the PayPal business account as the customer account for linked-flow or Production test payments because that produces declines.
- App Switch testing is conditioned on App Switch eligibility and a completed integration. The guide routes sandbox-app installation, browser-return and fallback scenarios, session restoration through the return URL, the iframe exclusion, and listed testable and untestable cases to the exact raw locators below. Setup or a browser/app return does not prove tokenization or payment completion.
- The page also provides a PayPal-dispute exercise for linked Sandbox accounts with an existing transaction, including Control Panel response steps and observed reporting fields. Those procedures and observations are snapshot-scoped test guidance, not a guarantee of dispute creation, timing, synchronization, or outcome for another account.
- Sandbox and Production accounts are isolated: created objects, processing options, recurring-billing settings, login information, merchant ID, and API keys do not transfer. The page separately says to contact PayPal support after integration completion to enable App Switch for Production traffic.
- Production setup uses Production credentials in server-side gateway configuration, recommends a dedicated API user rather than an individual user's credentials, and requires applicable account settings to be recreated. The page says the client needs no corresponding configuration update because it obtains its client token from the server.
- The Production check calls for only a few low-value sale transactions for intended payment-method types, submitted for settlement and followed through to bank deposit. It requires real payment methods; settled tests debit the associated method and incur fees, so the page says to use reasonable amounts and limit the number of transactions.

> [!warning] Sandbox and setup are not payment-lifecycle proof
> Mocked responses, linked-account data, App Switch setup, dispute exercises, and server configuration do not prove Production eligibility, tokenization, authorization, settlement, dispute synchronization, or funding. Production uses separate credentials and settings, and the prescribed live checks can move real funds and assess fees.

> [!warning] Malformed App Switch compatibility table
> The captured table at lines 139-148 has blank `Availability` cells and duplicated or concatenated browser-behavior text across other cells. Do not reconstruct missing support states or infer behavior from blank cells; rely only on the separately legible best-practice and test-case statements.

> [!warning] Unresolved dispute-identifier mapping
> Step 2 at lines 231-236 says the PayPal Case ID should match the Braintree Transaction ID, while lines 279-313 say the PayPal Case ID is mirrored by `Case Number` and identify `Transaction ID` as a separate transaction reference. This snapshot does not resolve which mapping is authoritative, so it does not establish one-to-one reconciliation from these fields alone.

## Detail locators

- Mocked versus linked PayPal Sandbox modes and their explicit boundaries: `# Testing and Go Live`, lines 16-31.
- PayPal business-account-as-customer decline warning: `# Testing and Go Live > IMPORTANT`, lines 36-37.
- Mocked-flow credential route and no-PayPal-Sandbox-data boundary: `## Mocked PayPal testing`, lines 42-46.
- Linked-account creation, same-country/developer-account conditions, credentials, fake-nonce warning, and Control Panel linking: `## Linked PayPal testing`, lines 49-87.
- App Switch eligibility, sandbox-app setup, compatibility/fallback table, return-URL guidance, iframe exclusion, and test-case boundaries: `## Testing App Switch`, lines 90-190.
- Linked-account and transaction prerequisites, dispute creation/response/escalation exercises, observations, reconciliation statement, and displayed report fields: `## Testing PayPal Disputes in the Braintree Sandbox`, lines 195-313.
- Sandbox/Production isolation and separate App Switch Production-enablement instruction: `## Go Live > IMPORTANT`, lines 316-322.
- Dedicated API-user recommendation, Production credentials, account-setting recreation, server configuration examples, and client-token boundary: `### Create an API user` through the paragraph after the Java example, lines 327-434.
- Low-value Production sales and real-method debit/fee warning: `## Test transactions in production`, lines 437-441.

## Related

- Company: [[braintree]]
- Main concept: [[paypal-braintree-integration]]
- Supporting administration concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/control-panel/important-gateway-credentials-2026-09-16|Braintree gateway-credentials article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16|Braintree users-and-roles article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/get-started/try-it-out-2026-09-16|Braintree Sandbox-versus-Production article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/payment-method-types-overview-2026-09-16|Braintree payment-method types overview]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/paypal/testing-go-live/javascript/v3-2026-09-16|Braintree PayPal Testing and Go Live for JavaScript v3]] - complete collected guide covering mocked and linked Sandbox approaches, App Switch and dispute test procedures, isolated Production setup, and limited real-payment Production checks
