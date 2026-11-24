---
title: "Stripe Terminal: Collect On-Screen Inputs"
type: concept
category: technology
tags: [stripe, stripe-terminal, collect-inputs, forms, signature, reader-display]
---

## Definition

The 2026-05-01 Stripe Terminal guide lists Stripe Reader S700/S710 and BBPOS WisePOS E for on-screen input forms. It documents six input types with customizable text and optional toggles. Forms can be displayed before payment, after payment, or outside a payment cycle.

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
- The JavaScript, iOS, Android, and React Native SDK variants document up to five inputs per call, collected in sequence.
- Can be displayed before payment, after payment, or outside any payment cycle
- iOS: requires SDK 4.4.0+; Android: requires SDK 4.3.0+
- The 2026-05-01 guide documents offline input collection on a capable smart reader for iOS, Android, and React Native.

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
- Server-driven collection times out after two minutes without a touch and reports the failure in a `terminal.reader.action_failed` webhook.

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
| Toggle | Server-driven documents `enabled` and `disabled`. SDKs also document `skipped` |

## Signature Images

- For server-driven collection, Stripe stores the signature file for seven days.
- Download the file through the Files API and store it if it is needed beyond seven days.
- The merchant is responsible for complying with laws governing collection, use, storage and disclosure of signatures.

## Legal Compliance

The feature includes a strong legal notice: the merchant is fully responsible for:
- Obtaining all necessary consents, authorizations, and permissions
- Ensuring the legal validity and enforceability of contracts or notices that use input collected by the reader or output displayed on it

## Simulated Testing

The May guide's JavaScript, iOS, and Android simulator sections list these scenarios:
- Successful collection (all inputs)
- Successful collection (skipping all non-required inputs)
- Failed collection (timeout)

Hard-coded values are returned per input type when simulating success.

## Sources

- [[source-stripe-terminal-collect-inputs]] — integration guide captured 2026-05-01, with the 2026-11-07 platform variant index linked for navigation.
