---
title: "Braintree Masterpass Configuration"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/masterpass/configuration"
raw_files:
  - "braintree/docs/guides/masterpass/configuration-2026-09-16.md"
tags: [braintree, masterpass, secure-remote-commerce, configuration, historical-snapshot]
---

## Overview

This collected unversioned [[braintree|Braintree]] configuration page is a historical retrieval route for the transition from Masterpass to Secure Remote Commerce (SRC). It tells prior Masterpass users to integrate with SRC and records access, SDK-generation and account-enablement qualifications for [[braintree-payment-methods]]; it does not establish a currently supported or executable migration path.

## Key takeaways

- The page says Masterpass was replaced by SRC and directs prior Masterpass users to integrate with SRC.
- It describes SRC as a limited release for eligible merchants, says the API is subject to change, names Android v2, iOS v4 and JavaScript v3 Client SDK generations, and routes access requests to Braintree. These are captured page statements, not present merchant eligibility or exact current SDK/package requirements.
- Masterpass is not automatically enabled in either Sandbox or Production accounts; the page tells interested merchants to contact Braintree. This is an enablement condition, not proof that either environment is enabled or that a transaction succeeds.

> [!warning] Historical replacement and support-status conflict
> The assigned page directs former Masterpass users to SRC and calls SRC a current limited release, but the separately retained 2026-09-16 SRC authority says Visa Click to Pay/SRC would no longer be supported after January 20, 2026 and that later attempts risk decline. [[source-braintree-payment-methods-secure-remote-commerce]] Preserve both statements: the snapshot does not identify a safe current successor or prove present Masterpass or SRC availability.

## Evidence boundaries

This short configuration webpage contains no client-side or server-side implementation procedure. It is website snapshot evidence, not exact SDK/package or GitHub implementation history, merchant-account enablement, current eligibility, environment behavior, or payment-execution proof.

## Detail locators

- Masterpass replacement and instruction to integrate with SRC: opening `**AVAILABILITY**`, raw line 18.
- SRC limited-release, eligible-merchant, API-change, Client SDK generation and access-request statements: opening `**AVAILABILITY**`, raw line 18.
- Nonautomatic Sandbox and Production enablement plus contact route: `## Email us`, raw lines 21-24.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Retained SRC authority: [[source-braintree-payment-methods-secure-remote-commerce]]

## Related raw API references

- [[raw/braintree/docs/guides/masterpass/overview-2026-09-16|Braintree Masterpass overview]] - navigation only; not read as evidence for this entry
- [[raw/braintree/docs/guides/masterpass/client-side/javascript/v3-2026-09-16|Braintree Masterpass client-side JavaScript v3 guide]] - navigation only; not read as evidence for this entry
- [[raw/braintree/docs/guides/masterpass/server-side/node-2026-09-16|Braintree Masterpass server-side Node.js guide]] - navigation only; not read as evidence for this entry

## Raw Sources

- [[raw/braintree/docs/guides/masterpass/configuration-2026-09-16|Braintree Masterpass configuration]] - complete collected page covering the Masterpass-to-SRC direction, SRC access and Client SDK-generation qualifications, and nonautomatic Sandbox or Production enablement
