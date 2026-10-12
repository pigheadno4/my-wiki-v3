---
title: "Adyen Docs: Forward payment details"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/tokenization/forward-payment-details"
raw_files:
  - "adyen/docs/online-payments/tokenization/forward-payment-details/2026-09-15.md"
tags: [adyen, tokenization, network-tokens, card-details, forwarding]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] webpage describes server-side Checkout `/forward` requests that send card details or network tokens to a PCI-compliant third party, such as another PSP. The merchant specifies the destination and placeholder-based request; Adyen substitutes the payment details, calls the third-party API on the merchant's behalf, and returns that party's response as a string. This is a forwarding route related to [[adyen-tokenization|Adyen tokenization]] and [[adyen-network-tokenization|network tokenization]], not proof of a third-party payment's success.

## Key takeaways

- The documented setup calls for an online-payments integration using Checkout API v70 or later, Checkout webservice and Merchant Recurring credential roles, Recurring tokens life cycle events webhooks, and contacting Adyen Support to enable card-detail or network-token forwarding. For live use, the endpoint region must match the Adyen token vault's storage region. The destination must be PCI compliant.
- Card-detail forwarding covers an existing Adyen token, an existing token with CVC, or non-tokenized encrypted or unencrypted card details sent to the third party for its own tokenization. The non-tokenized route can optionally store the same card with Adyen via `options.tokenize`; sending unencrypted card details is conditioned on full PCI compliance. The field list and request examples are in the raw sections below.
- Network-token forwarding requires an Adyen token for the same payment details and a conditional request body that falls back to the Adyen-stored card details if the network token is unavailable. The guide says a network token cannot be forwarded together with card details that have not yet been tokenized by Adyen. Its scenario table distinguishes forwarding a network token with a network transaction reference and cryptogram, a network token alone, and the Adyen-token fallback.
- The `/forward` result includes the HTTP status Adyen received from the third party and passes the third-party response body as an unmodified string. Adyen-side errors and third-party no-response or timeout cases are separate diagnostic paths; a returned third-party status must be interpreted under that party's contract.
- `options.dryRun` is described only for the test environment and masks sensitive information in the returned populated request. Several illustrative request/response snippets have incomplete JSON punctuation, so their structure should be checked against the current API reference before implementation.

## Detail locators

- **Scope and prerequisites** — opening description and `## Requirements`, raw lines 15-35; includes the PCI-compliant destination, Checkout API version, credential roles, webhook, Support enablement, Adyen token prerequisite for network forwarding, and live-region condition.
- **Request ownership and response route** — `## How it works`, raw lines 37-46.
- **Card-detail modes and request fields** — `## Forward card details`, raw lines 48-97; token, token plus CVC, non-tokenized details, destination parameters, `options.tokenize`, and test-only `options.dryRun`. Examples and the Adyen/third-party exchange follow at raw lines 98-258.
- **Network-token constraints and fallback** — `## Forward network tokens`, raw lines 260-323; option fields, conditional body and scenarios. Request and forwarding examples follow at raw lines 324-477.
- **Result and errors** — `## Handle the result`, raw lines 478-530; third-party status/body, conditional `storedPaymentMethodId`, separate Adyen and third-party error descriptions.
- **Placeholder map** — `## Placeholder reference`, raw lines 532-561.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-tokenization]]
- Related concept: [[adyen-network-tokenization]]

## Raw Sources

- [[raw/adyen/docs/online-payments/tokenization/forward-payment-details/2026-09-15|Adyen Docs — Forward payment details (2026-09-15)]]
