---
title: "Braintree Hosted Fields Events (JavaScript v3)"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/hosted-fields/events/javascript/v3"
raw_files:
  - "braintree/docs/guides/hosted-fields/events/javascript/v3-2026-09-16.md"
tags: [braintree, javascript-sdk, hosted-fields, events, form-validation]
---

## Overview

This Braintree JavaScript v3 guide explains how a merchant page can listen for Hosted Fields events and update its UI from field state. It also routes readers to `getState` for on-demand field inspection; the guide's Hosted Fields reference links target version 3.92.1.

## Key takeaways

- Register an event listener with the Hosted Fields `on` function in the `create` callback, then use the emitted event object to inspect fields and update the merchant-controlled UI.
- The event set covers focus, blur, transitions between empty and non-empty states, card-type changes, validity changes, and customer input-submission requests. Use the event table in the raw guide for the exact triggers.
- `cardTypeChange` is emitted only from changes in the card-number field. The worked example changes the CVV label and placeholder when exactly one possible card type remains, and falls back to `CVV` otherwise.
- When event-driven handling is unnecessary, `getState` returns the form state. The example checks `isValid` for every provided field before proceeding toward tokenization; this is field-validity and UI-flow state, not evidence that tokenization or a payment succeeded.
- The guide is scoped to JavaScript v3, while its Hosted Fields API reference links are pinned to `braintree-web` 3.92.1. Do not project those linked reference details onto unspecified SDK versions.

## Detail locators

- Event names and trigger descriptions: `# Events` > event table, lines 20-28.
- Listener setup and the `cardTypeChange` CVV-label example: `# Events` > `### Callback`, lines 30-55; Promise equivalent at lines 59-85.
- On-demand state inspection before form submission: `# Events`, lines 86-87; Callback example at lines 88-108 and Promise example at lines 110-130.
- Version-qualified Hosted Fields reference route: `# Events`, line 133.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-sdk]]
- Related source: [[source-braintree-credit-cards-client-javascript-v3]]

## Raw Sources

- [[raw/braintree/docs/guides/hosted-fields/events/javascript/v3-2026-09-16|Braintree JavaScript v3 Hosted Fields events guide]] - complete guide covering event-driven UI updates and on-demand field-state inspection
