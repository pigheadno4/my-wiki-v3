---
title: "Braintree ACH Direct Debit Configuration"
type: source
date_ingested: 2026-10-08
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/ach/configuration"
raw_files:
  - "braintree/docs/guides/ach/configuration-2026-09-16.md"
tags: [braintree, ach, direct-debit, javascript-v3, configuration, sandbox]
---

## Overview

This fully read 2026-09-16 [[braintree]] website snapshot is an unversioned configuration notice for ACH Direct Debit. It limits the documented route to eligible merchants that can implement a custom client-side integration with JavaScript v3, excludes Drop-in UI, and directs merchants meeting those criteria to contact Braintree to request Sandbox enablement. The contact action is a request path, not evidence that an account is enabled. See [[braintree-payment-methods]] for the provider-wide payment-method route.

## Key takeaways

- The notice is specifically about ACH Direct Debit; it does not establish configuration or availability for other bank-payment methods.
- The page states two conditions for the documented route: merchant eligibility and the ability to implement a custom client-side integration using JavaScript v3. It separately says ACH Direct Debit is unavailable in Drop-in UI in this snapshot.
- For merchants meeting those criteria, the only setup action stated on this page is to contact Braintree to request ACH Direct Debit enablement in a Sandbox account. A request, contact response, or retained instruction is not proof that enablement occurred.
- The next-page link points to a JavaScript v3 client-side route, but that target was not read for this entry and supplies navigation only, not implementation or runtime evidence.

## Material boundaries

- This dated website snapshot is not proof of current availability, merchant eligibility, Sandbox or Production enablement, account configuration, exact SDK or GitHub implementation, successful payment execution, settlement, or funding.
- The page does not document configuration fields, bank-account collection, tokenization, verification, nonce handoff, server processing, transaction creation, webhooks, or lifecycle behavior. Use the applicable dedicated authorities for those procedures.
- The enablement sentence names a Sandbox account only. Do not infer a Production enablement process or result from this page.

## Detail locators

- Document identity and unversioned configuration route: raw frontmatter `title` and `slug`, lines 6-9.
- Eligible-merchant, custom JavaScript v3 integration and Drop-in UI exclusion: `**AVAILABILITY**`, raw lines 16-17.
- Contact request for Sandbox enablement: raw line 19.
- JavaScript v3 client-side next-page navigation: raw line 23; navigation only.

## Related

- [[braintree]]
- [[braintree-payment-methods]]
- [[source-braintree-docs-guides-ach-overview]]

## Related raw API references

- `/braintree/docs/guides/ach/client-side/javascript/v3/` - next-page navigation target named at raw line 23; not read or used as behavioral evidence for this entry.

## Raw Sources

- [[raw/braintree/docs/guides/ach/configuration-2026-09-16|Braintree ACH Direct Debit configuration notice (captured 2026-09-16)]]
