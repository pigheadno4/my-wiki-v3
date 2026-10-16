---
title: "Adyen Oracle Opera Integration"
type: concept
category: technology
tags: [adyen, oracle-opera, hospitality, opi, terminals, tokenization]
---

## Definition

Adyen's Oracle Opera hospitality integration connects OPI-compatible Opera workstations to Adyen payment terminals through Oracle Payment Interface 6.2. The 2021-modified guide captured 2026-09-15 describes on-premise, hosted and cloud setups, plus a separate merchant-account-enabled route for ecommerce OPI tokens. It does not define an exact Opera-version matrix or establish a merchant's live enablement. [[source-adyen-docs-plugins-oracle-opera]]

## Payment and token boundary

Opera's listed preauthorization is a temporary hold rather than a charge; top-up and release act on that hold, while Sales Completion and direct Sale/Purchase are the guide's charge paths. Void is limited to the same settlement day, and Reversal is described for interrupted or timed-out OPI transactions. Terminal token and bulk-token routes are listed for later top-ups, final settlement or migration scenarios. Ecommerce OPI-token retrieval first requires Support-enabled merchant-account settings; the guide instructs a Checkout `/payments` request with `additionalData.opi.includeTransToken=true` and `shopperReference=not_provided`, and returns `opi.transToken` in the response. That shopper-reference value is guide-specific, not a general stored-credential rule; the example `Authorised` response is not transaction proof.

## Scope and evidence boundary

This concept is for Oracle Opera hospitality/PMS and OPI. It does not import capabilities from a different Oracle retail product. A feature list, compatible-workstation statement or sample response does not verify terminal availability, token-migration safety, payment authorization, capture, refund or financial settlement for a particular guest.

## Sources

- [[source-adyen-docs-plugins-oracle-opera]] — Oracle Opera OPI 6.2 integration, hospitality transaction types, test-account enablement and ecommerce token route (2026-09-15 snapshot).

## Related

- [[adyen]]
- [[adyen-terminal-api]]
- [[adyen-tokenization]]
