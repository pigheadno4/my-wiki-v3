---
title: "Stripe Terminal: Collect On-Screen Inputs"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-collect-inputs-2025.md"
tags: [stripe, stripe-terminal, collect-inputs, forms, signature, reader-display, webhooks]
---

## Summary

Stripe Terminal smart readers (S700/S710, WisePOS E) can display prebuilt input forms and collect structured information from customers using `collectInputs` / `collect_inputs`. Not available on M2, WisePad 3, or Tap to Pay.

## Key Details

**6 input types**: `signature`, `selection`, `email`, `phone`, `text`, `numeric`. Up to 5 per call, collected in sequence. Can be used before payment, after payment, or outside a payment cycle.

**Customization**: each input supports `required` (hides Skip button), custom title/description/button text, and up to 4 toggles per input. Selection inputs support `primary`/`secondary` choice styles.

**Character limits**: title=40, description=500 (selection)/100 (others), submit_button=30, skip_button=14.

**Webhooks (server-driven)**: `terminal.reader.action_succeeded` and `terminal.reader.action_failed`. Timeout = 2 minutes of no touch on reader.

**Returned data**: signature = file ID (server-driven) or SVG string (SDK); selection = `text`+`id`; others = input string; skipped optional = `skipped: true`; toggle = `"enabled"`/`"disabled"`/`"skipped"`.

**Signature images**: stored by Stripe for **7 days only** — download and store externally if needed longer.

**SDK minimums**: iOS 4.4.0+, Android 4.3.0+. Both support collect inputs while offline.

**Legal**: merchant is fully responsible for obtaining required consents and ensuring legal validity of contracts/notices created from collected inputs.

## Raw Sources

- [[stripe-terminal-collect-inputs-2025]] — verbatim webpage content (5 SDK variants: server-driven, JS, iOS, Android, React Native)
