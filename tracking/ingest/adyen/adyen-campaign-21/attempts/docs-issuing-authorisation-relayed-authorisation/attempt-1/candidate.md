---
title: "Adyen Issuing: Use relayed authorisation"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/authorisation/relayed-authorisation"
raw_files:
  - "adyen/docs/issuing/authorisation/relayed-authorisation/2026-09-15.md"
tags: [adyen, issuing, relayed-authorisation, webhooks, fallback]
---

## Overview

This Adyen Issuing guide describes the platform's real-time approval or refusal decision through a relayed-authorisation webhook. When Adyen receives a payment authorisation request, it sends transaction data, including transaction-rule and validation-check information, to the platform's configured server. The server replies with its decision; Adyen applies configured fallback logic if the response does not arrive or is invalid. This is a 2026-09-15 capture of a page marked last modified 2023-09-12. The page documents decision handling for [[adyen-issuing]], not a successful card payment, capture, or settlement.

## Key takeaways

- The guide says each relayed webhook allows up to **2000 ms** for an approval or refusal reply (raw lines 21–26, 80–82, 258–263). Its `Decision on error` settings separately select automatic approval or decline for connection errors/timeouts and invalid responses (raw lines 73–76). The companion [[source-adyen-docs-issuing-validation-checks]] raw instead says `relayedAuthorisationStip` stand-in processing is triggered after **1500 ms** without a response (raw validation-checks lines 158–168). These two snapshots do not explain the timing difference; do not equate the values or silently choose one as a universal operational deadline.
- To receive webhooks, the platform exposes a JSON-capable HTTPS endpoint on port 443, 8443, or 8843 that can handle basic authentication (raw lines 34–40). Customer Area configuration requires the **Manage relayed authorisation configuration** user role. It sets the URL, certificate validation level, basic-auth credentials, HMAC key, and error decisions; the guide warns that the generated HMAC key must be saved securely because it cannot be copied later (raw lines 42–78).
- Adyen sends an HTTP POST for a payment attempt. The prose says a processed decision uses HTTP 200 and a response-body `status` of `Authorised` or `Refused`, with optional `metadata`; 4xx and 5xx indicate the server could not process the request and cause fallback (raw lines 80–95). The approval/refusal JSON examples instead nest `status` inside `authorisationDecision` and add `reference` (raw lines 226–255). The prose/example response-shape difference remains unresolved here; verify the API contract before implementing.
- The sample incoming webhook shows account holder, balance account, payment instrument, merchant, amount, transaction-rule and validation data; its prefilled `authorisationDecision.status: Authorised` is example data and does not replace the platform's reply or prove a final outcome (raw lines 97–224). For refusal reasons or other validation outcomes, use the corresponding validation guide.
- For firewall allowlisting, the page recommends the `out.adyen.com` domain or regularly resolving it; it says Adyen does not provide a stable IP list and hard-coded addresses risk disruption (raw lines 265–274).

## Detail locators

- `How it works` and 2000 ms fallback options: raw lines 19–32.
- `Expose a webhook endpoint` and `Configure the relayed authorisation webhook`: raw lines 34–78, including required role, authentication, HMAC, and decision-on-error settings.
- `Respond to the webhook`: raw lines 80–95 for HTTP outcome semantics; incoming example at 97–224; approve/decline response examples at 226–255.
- `Fallback` and domain/IP guidance: raw lines 258–274.
- Timing contrast: independently read [[raw/adyen/docs/issuing/validation-checks/2026-09-15|validation-checks raw]] lines 158–168, retained as related evidence rather than part of this page's `raw_files`.

## Related

- [[adyen]] — provider context.
- [[adyen-issuing]] — Issuing concept.
- [[source-adyen-docs-issuing-validation-checks]] — validation results and 1500 ms stand-in statement; compare with this page's 2000 ms language.

## Raw Sources

- [[raw/adyen/docs/issuing/authorisation/relayed-authorisation/2026-09-15|Adyen relayed authorisation, captured 2026-09-15]]
