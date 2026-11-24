---
title: "Stripe Terminal: Collect On-Screen Inputs"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/features/collect-inputs"
raw_files:
  - "stripe-terminal-collect-inputs-2025.md"
tags: [stripe, stripe-terminal, collect-inputs, forms, signature, reader-display, webhooks]
---

## Summary

The 2026-05-01 [[stripe]] Terminal guide describes displaying prebuilt forms and collecting customer responses with `collect_inputs` or `collectInputs`. It lists Stripe Reader S700/S710 and BBPOS WisePOS E. The 2026-11-07 capture indexes the Server-driven, JavaScript, iOS, Android, and React Native variants. The behavior below comes from the May guide.

## Key Details

**Input types**. `signature`, `selection`, `email`, `phone`, `text`, and `numeric`. Forms can appear before payment, after payment, or outside a payment cycle. Each of the four SDK variants documents up to five sequential inputs per call.

**Reader interaction**. The reader displays the first input. A required input hides Skip, while the customer may skip an optional input. After completion, the reader waits three seconds for a subsequent request before returning to the splash screen.

**Customization**. Set required inputs, customize the title, description and button text, and add up to four toggles per input. Selection inputs support `primary` and `secondary` choice styles.

**Character limits**. Title 40, description 500 for selection or 100 for other types, submit button 30, and skip button 14.

**Server-driven**. The merchant integration starts the reader action and subscribes to `terminal.reader.action_succeeded` and `terminal.reader.action_failed`. Two minutes without touching the reader screen causes a timeout reported as failure. Optional request metadata can correlate results. Retrieving the reader provides a fallback if the backend misses an event.

**SDK responses**. JavaScript and React Native return a promise. iOS and Android return results through a callback. Cancellation, timeout, or another collection failure returns an SDK error.

**Returned data**. Server-driven signatures return a file ID for a retrievable SVG. SDK signatures return SVG strings. Selection returns the choice’s `text` and `id`. Other inputs return the customer’s response string. Both paths flag a skipped optional input with `skipped: true`. The May guide lists `enabled` and `disabled` for server-driven toggles and additionally lists `skipped` for SDK toggles.

**Server-driven signature files**. Stripe stores the signature image for seven days. If needed longer, retrieve the file through the Files API and store it in accordance with applicable law.

**SDK minimums and offline collection**. The May guide gives iOS 4.4.0+ and Android 4.3.0+. It documents collecting inputs on a capable smart reader operating offline for iOS, Android and React Native.

**Data and merchant responsibilities**. Do not collect sensitive data, including payment card information or protected health information, or information restricted by law. The merchant is responsible for obtaining applicable consents and permissions, the legal validity and enforceability of contracts or notices created using collected inputs, and lawful collection, use, storage and disclosure of signatures.

## Related

- [[stripe-terminal-collect-inputs]] — collection flow and inputs
- [[stripe-terminal]] — Terminal integration overview

## Raw Sources

- [[raw/stripe-terminal-collect-inputs-2025|Stripe Terminal collect on-screen inputs guide captured 2026-05-01]] — five variant bodies

## Related raw API references

- [[raw/stripe-terminal-features-collect-inputs-2026-11-07|Stripe Terminal collect on-screen inputs platform variant index captured 2026-11-07]]
