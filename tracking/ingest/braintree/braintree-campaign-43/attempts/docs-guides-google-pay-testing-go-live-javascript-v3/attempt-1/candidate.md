---
title: "Braintree Google Pay Testing and Go Live (JavaScript v3)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/google-pay/testing-go-live/javascript/v3"
raw_files:
  - "braintree/docs/guides/google-pay/testing-go-live/javascript/v3-2026-09-16.md"
tags: [braintree, google-pay, javascript-v3, sandbox, production, testing]
---

## Overview

This collected [[braintree]] guide at the Google Pay JavaScript v3 testing-and-go-live route describes an Android-device user-flow prerequisite, Sandbox nonce and transaction-display behavior, and the separate production enablement and Google merchant-registration steps. It is a website snapshot, not evidence of current browser support, merchant or buyer eligibility, account enablement, an exact `braintree-web` package or runtime behavior, successful payment execution, settlement, or funding.

## Key takeaways

- Testing the entire user flow on an Android device requires the user to have at least one card or PayPal account stored in Google Pay or the user's Google account. The page says a user without one can add a payment method to Google Pay during checkout. It also instructs merchants to test on the latest version of a supported browser, while routing the actual browser list to Google documentation.
- In Sandbox, the page says Google Pay returns valid testing nonces pointing to either a test virtual account number or a PayPal account. It routes simulation of server behavior to Braintree test amounts and test nonces; fixtures and returned nonces remain Sandbox evidence rather than live authorization or payment proof.
- Completed Sandbox transactions are described as appearing immediately in the Braintree gateway as Google Pay transactions, except PayPal-via-Google-Pay transactions appear as PayPal transactions. The page also says Sandbox `payer_email` will not match the PayPal account email added to Google Pay, whereas it will match in production. These are environment-qualified display and data statements, not a timing guarantee or evidence that an individual transaction completed.
- After integration testing, production requires Google Pay to be enabled in the Braintree Control Panel. The documented route is **Processing** → **Payment Methods** → the **Google Pay** toggle. A separate production step follows Google's documentation to register the domain and receive a merchant ID, which the page says to use when creating the payment data request.
- The production example supplies the Google merchant ID, selects Google's `PRODUCTION` environment, parses the returned payment data through the Braintree Google Pay instance, and comments that the resulting nonce should be sent to the merchant server. It is illustrative rather than package-qualified API or transaction proof, and the captured example has an unmatched extra closing parenthesis after `PaymentsClient(...)`.
- If Google Pay is active in the Control Panel but needs to be enabled for a specific merchant account, the page directs the merchant to contact Braintree. General Control Panel activation therefore does not establish merchant-account-specific enablement.

> [!warning] Sandbox, configuration, and sample code are not production proof
> Test nonces and Sandbox gateway display do not prove production eligibility, account or merchant-account enablement, authorization, payment completion, settlement, or funding. Production separately requires Control Panel activation, Google domain registration and a merchant ID; the displayed JavaScript also contains an unmatched extra closing parenthesis at raw line 59 and should not be treated as verified copy-ready code.

## Detail locators

- Android-device stored-method prerequisite, checkout-time addition option, and supported-browser testing instruction: `# Testing and Go Live`, lines 17-26.
- Sandbox nonce targets, test-amount/test-nonce navigation, gateway display distinction and environment-qualified `payer_email` behavior: `# Testing and Go Live`, line 28.
- Production Control Panel enablement sequence: `## Go live`, lines 31-40.
- Google domain registration, merchant ID acquisition and payment-data-request instruction: `## Go live`, lines 42-44.
- Illustrative merchant-ID request, `PRODUCTION` environment, parsing, server nonce handoff, error branch and unmatched closing parenthesis: `### Javascript`, lines 46-69.
- Specific-merchant-account enablement contact route: paragraph after `### Javascript`, line 71.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Payment-method context: [[source-braintree-payment-methods-google-pay]]

## Related raw API references

- [[raw/braintree/docs/reference/general/testing/node-2026-09-16|Braintree general transaction testing reference (Node.js route)]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/google-pay/configuration/javascript/v3-2026-09-16|Braintree Google Pay configuration guide for JavaScript v3]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/google-pay/testing-go-live/javascript/v3-2026-09-16|Braintree Google Pay Testing and Go Live for JavaScript v3]] - complete collected guide covering Android-device test prerequisites, Sandbox nonce and gateway behavior, and production enablement, domain-registration and merchant-ID steps
