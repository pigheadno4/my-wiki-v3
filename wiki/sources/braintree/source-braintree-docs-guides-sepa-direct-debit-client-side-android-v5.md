---
title: "Braintree SEPA Direct Debit Client-Side Implementation (Android v5)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/sepa-direct-debit/client-side/android/v5"
raw_files:
  - "braintree/docs/guides/sepa-direct-debit/client-side/android/v5-2026-09-16.md"
tags: [braintree, sepa, direct-debit, android, client-sdk, tokenization]
---

## Overview

This 2026-09-16 Braintree website snapshot is the Android v5-routed client-side implementation guide for SEPA Direct Debit. It covers collecting the customer's bank and customer information, creating and launching a SEPA payment-authorization request, handling the app return, and tokenizing the successful result into a nonce for a separate server-side transaction. The request example supplies a one-off mandate type, but the example is not proof of mandate acceptance, a debit, transaction success, settlement or funding.

The page limits SEPA Direct Debit to eligible merchants using a custom client-side integration, states Android v4.13+ availability, excludes Drop-in and directs qualifying merchants to request Sandbox or Production enablement. These are snapshot-scoped statements, not evidence of current SDK support, merchant eligibility or account enablement.

## Key takeaways

- The page's dependency example uses the Android SEPA Direct Debit module at `5.8.0`. Its separate availability notice says Android v4.13+, while this canonical route is Android v5; preserve those as page-scoped version statements rather than inferring support for another package version.
- The documented sequence constructs `SEPADirectDebitClient`, `SEPADirectDebitLauncher` and `SEPADirectDebitRequest`, calls `createPaymentAuthRequest()`, launches when required, handles the returned authorization result and then calls `tokenize()`. Required bank/customer fields and the complete request example remain in the raw locators.
- For a launched flow, the example stores the `SEPADirectDebitPendingRequest.Started` value and later supplies it to `handleReturnToApp`. It routes non-`singleTop` activity launch modes through `onResume` and `singleTop` through `onNewIntent`; a return can be success, no result or failure, so returning to the app is not itself success.
- A successful payment-authorization result is passed to `tokenize`. Tokenization can separately succeed, fail or be canceled; only the success branch sends the nonce string to the merchant server to create a transaction. A `LaunchNotRequired` payment-authorization response instead exposes a nonce for that same separate server action. Neither client branch proves server acceptance or payment outcome.

> [!warning] Snapshot, version and enablement boundary
> This is Android v5-routed website guidance collected on 2026-09-16, with a `5.8.0` dependency example and separate Android v4.13+ availability wording. It is not current package-support evidence, exact commit-qualified SDK behavior, merchant enablement, buyer or bank-account eligibility, or environment availability proof.

> [!warning] Return, mandate and payment boundary
> A started request, app return, payment-authorization result, one-off mandate-type example or nonce is not proof of accepted mandate terms, a successful debit or a final transaction. Preserve the result branches and the separate merchant-server transaction step.

## Detail locators

- Eligible-merchant, custom-integration, platform/version, Drop-in exclusion and account-enablement statements: `# Client-Side Implementation > AVAILABILITY`, raw lines 17-20.
- Android module dependency example at `5.8.0`: `## Get the SDK`, raw lines 25-41.
- Required bank-account and customer information: `## Collect information`, raw lines 44-59.
- Client, launcher, request, payment-authorization and tokenization sequence: `## Invoking the SEPA Direct Debit flow`, raw lines 61-64.
- Client authorization, return URL scheme and activity-launch-mode return handling: example at raw lines 66-116.
- Successful authorization tokenization, success/failure/cancel branches and server nonce handoff: example at raw lines 118-128.
- Request fields, billing-address example and one-off mandate-type example: raw lines 130-145.
- Ready-to-launch, pending-request storage, launch-not-required nonce and failure branches: raw lines 147-170.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Broader SEPA mandate and lifecycle route: [[source-braintree-docs-guides-sepa-direct-debit-overview]]
- JavaScript v3 client route: [[source-braintree-docs-guides-sepa-direct-debit-client-side-javascript-v3]]

## Related raw API references

The page links a server-side next step. That target was not read for this entry and is navigation only; it does not establish an exact server request, successful transaction, debit, settlement or funding.

## Raw Sources

- [[raw/braintree/docs/guides/sepa-direct-debit/client-side/android/v5-2026-09-16|Braintree SEPA Direct Debit client-side implementation for Android v5]] - complete collected page covering availability, SDK setup, customer-data collection, payment authorization, app-return handling and nonce tokenization
