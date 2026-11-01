---
title: "Adyen Authentication webhooks v1 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/acs-webhook/latest/overview"
raw_files:
  - "adyen/api-explorer/acs-webhook/latest/overview/2026-09-15.md"
tags: [adyen, issuing, authentication, webhooks, acs]
---

## Overview

This 2026-09-15 API Explorer snapshot is the **Authentication webhooks v1** endpoint catalog. It says Adyen sends webhooks for cardholder-authentication events and lists two POST routes. This catalog does not define an individual event payload, receiver response, challenge decision, timing, or payment result. [[adyen]] [[adyen-issuing]] [[adyen-webhooks]]

## Key takeaways

- `balancePlatform.authentication.created` is listed with the summary “Cardholder authenticated”; `balancePlatform.authentication.relayed` is listed with “Out-of-band authentication requested” (raw lines 9–15). These are endpoint summaries, not schemas or guarantees about a particular authentication outcome.
- No request-field requiredness, event identifier, response body/status, acceptance deadline, retry, ordering, signature, or final authorization rule appears in this overview. Follow the individual endpoint references and Issuing authentication guidance before implementing a challenge or interpreting an outcome (full raw lines 1–15).

## Detail locators

- Catalog identity and purpose: raw lines 5–7.
- Both POST route names and their summaries: raw lines 9–15.

## Related

- [[adyen-issuing]] — issuer-side cardholder authentication and reciprocal catalog route.
- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-authenticate-cardholders]] — separate detailed Issuing OOB challenge guidance; its response and timing rules are not stated by this catalog.

## Raw Sources

- [[raw/adyen/api-explorer/acs-webhook/latest/overview/2026-09-15|Authentication webhooks v1 catalog capture]]
