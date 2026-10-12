---
title: "Adyen Verify HMAC Signatures"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/webhooks/secure-webhooks/verify-hmac-signatures"
raw_files:
  - "adyen/docs/development-resources/webhooks/secure-webhooks/verify-hmac-signatures/2026-09-15.md"
tags: [adyen, webhooks, hmac, security, integrity]
---

## Overview

This [[adyen]] documentation page explains how to enable and verify HMAC signatures for webhook types that support them. It distinguishes the payload-field signature used by Standard webhooks from the request-header signature used by some non-standard webhooks, and documents Adyen library and custom-verifier routes.

## Key takeaways

- Adyen strongly recommends HMAC verification for webhooks that support it. The page describes a successful comparison as evidence that the signed event came from Adyen and was not modified in transit; this security check does not establish the event's business outcome or that the receiver processed it successfully.
- A secret HMAC key is linked to one webhook endpoint, so multiple receiving endpoints require separate keys. Moving from test to live also requires generating a new key. Enablement is conditional on the option being available for the webhook.
- Standard webhooks place `hmacSignature` in `additionalData`. For a custom Standard-webhook verifier, the page specifies an ordered, colon-delimited payload from eight event values, empty strings for empty fields, UTF-8 payload bytes, binary decoding of the hexadecimal key, HMAC-SHA256, Base64 encoding, and comparison with the received signature.
- Some non-standard webhooks instead put `hmacsignature` and `protocol` in request headers. Their verifier signs the request body exactly as received without deserializing it, using HMAC-SHA256 and the binary key, then Base64-encodes and compares the result. Do not apply the Standard webhook's selected-field construction to this header-signature path.
- After generating a replacement key, propagation can take time. The receiver should temporarily continue accepting events signed with the previous key.

> [!warning] Scope and evidence boundary
> The page is an unversioned documentation snapshot and applies HMAC only where the webhook supports it. It does not prove current account or webhook-type eligibility, successful configuration or delivery, replay protection, endpoint processing, or any payment or resource outcome. Preserve the Standard `additionalData` versus non-standard header-signature distinction when implementing verification.

## Detail locators

- Security purpose, supported-webhook qualification, and library-versus-custom routes: `# Verify HMAC signatures`, lines 17-24.
- Endpoint-specific keys, test-to-live key separation, enablement steps, and signature-location distinction: `## Enable HMAC signatures`, lines 26-45.
- Replacement-key propagation and previous-key overlap: `### Changing your HMAC key`, lines 63-67.
- Packaged validator library routes: `## Verify using our libraries`, lines 69-78; language examples continue through line 186.
- Standard-webhook custom payload construction, encoding, HMAC-SHA256 calculation, and comparison: `## Verify using your own solution`, lines 188-235.
- Worked Standard-webhook key and event example: `### Example`, lines 237-276.
- Non-standard header fields, untouched request-body requirement, calculation, and comparison: `## Verify HMAC keys returned in the header`, lines 278-296; Java and Python examples continue through line 398.

## Related

- Company: [[adyen]]
- Concept: [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/development-resources/webhooks/secure-webhooks/verify-hmac-signatures/2026-09-15|Adyen Verify HMAC signatures]] - complete collected guide to endpoint and environment key scope, Standard payload-field verification, non-standard header verification, encoding, comparison, library routes, and key rotation
