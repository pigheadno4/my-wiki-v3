---
title: "Stripe Terminal: Collect On-Screen Inputs"
type: concept
category: technology
tags: [stripe, stripe-terminal, collect-inputs, forms, signature, reader-display]
---

## Definition

Stripe Terminal smart readers (S700/S710, WisePOS E) can display prebuilt input forms and collect structured information from customers outside the payment flow. Supports 6 input types collected in sequence, with customizable text and optional toggles.

**Not available on**: M2, WisePad 3, Tap to Pay.

## Input Types

| Type | Use case |
| --- | --- |
| `signature` | Waivers, agreements |
| `selection` | Multiple-choice questions, receipt preference |
| `email` | Loyalty, marketing opt-in |
| `phone` | Customer identifier |
| `text` | Open-ended questionnaire |
| `numeric` | Numeric entry |

> Do not use `collect_inputs` for sensitive data (payment card info, health information, or data restricted by law).

## Integration

- **Server-driven**: `stripe.terminal.readers.collectInputs(readerId, { inputs: [...] })`
- **JS/iOS/Android/React Native**: `collectInputs(params)` on the Terminal SDK instance
- Up to **5 inputs per call**, collected in sequence
- Can be displayed before payment, after payment, or outside any payment cycle
- iOS: requires SDK 4.4.0+; Android: requires SDK 4.3.0+
- iOS and Android support collecting inputs while the reader is **offline**

## Customization

Each input supports:

- **`required`**: hides the Skip button; customer must respond
- **`custom_text`** (server-driven) / `title` + `description` (SDK): contextual text shown on screen
- Up to **4 toggles** per input: Boolean options, agreements, opt-ins

**Character limits:**

| Field | Max |
| --- | --- |
| `title` | 40 |
| `description` | 500 (selection), 100 (others) |
| `submit_button` | 30 |
| `skip_button` | 14 |
| Toggle `title` | 50 (25 if toggle has description) |
| Toggle `description` | 50 (25 if toggle has title) |

For `selection` inputs, choices can be styled `primary` (emphasized) or `secondary` (de-emphasized).

Use `\n` for line breaks within text fields.

## Customer Interaction

- Reader displays the first input; customer completes or skips (if optional) each in sequence
- After all inputs: reader shows a transitional state for **3 seconds**, then returns to splash screen if no subsequent request arrives
- Timeout: **2 minutes** of no touch → `terminal.reader.action_failed` webhook

## Receiving Input Data

**Server-driven**: Stripe sends `terminal.reader.action_succeeded` or `terminal.reader.action_failed` webhooks. Subscribe to both.

**SDK integrations**: data returned directly in the SDK callback/promise.

Returned values by type:

| Input type | Returned value |
| --- | --- |
| `signature` | File ID (SVG) — server-driven; SVG string — SDK |
| `selection` | Selected choice `text` + `id` |
| `phone` / `email` / `text` / `numeric` | Customer's input string |
| Skipped optional | `skipped: true` |
| Toggle | `"enabled"` / `"disabled"` / `"skipped"` |

## Signature Images

- Stored by Stripe for **7 days only**
- Download via Files API using your secret key; store externally if retention > 7 days
- Merchant is responsible for complying with laws governing collection, storage, and disclosure of signatures

## Legal Compliance

The feature includes a strong legal notice: the merchant is fully responsible for:
- Obtaining all necessary consents, authorizations, and permissions
- Ensuring the legal validity and enforceability of any contracts or notices created using collected inputs

## Simulated Testing

SDK simulated reader supports:
- Successful collection (all inputs)
- Successful collection (skipping all non-required inputs)
- Failed collection (timeout)

Hard-coded values are returned per input type when simulating success.

## Sources

- [[source-stripe-terminal-collect-inputs]] — primary source: input types, API, customization, webhooks, signature storage
