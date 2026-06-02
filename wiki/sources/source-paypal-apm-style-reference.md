---
title: "Custom Style for Payment Fields (APM Reference)"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-style-reference.md"
tags: [paypal, apm, javascript-sdk, payment-fields, style, css, reference]
---

## Overview

CSS customization reference for `paypal.PaymentFields()` `style` object — variables and rules for APM payment field components.

Source URL: <https://developer.paypal.com/docs/checkout/apm/reference/style/>

Last updated: 2025-05-14

## Variables (11 documented)

| Variable | Purpose |
| --- | --- |
| `fontFamily` | Font family for payment fields text |
| `fontSizeBase` | Input/placeholder/dropdown text size |
| `fontSizeM` | Payment fields title description size |
| `textColor` | Title, input, dropdown text color |
| `colorTextPlaceholder` | Placeholder text color |
| `colorBackground` | Input/dropdown background color |
| `colorDanger` | Invalid field border + validation text color |
| `borderRadius` | Input/dropdown border radius |
| `borderWidth` | Input/dropdown border width |
| `borderFocusColor` | Focused field border color |
| `spacingUnit` | Distance between fields |

Additional variables in code example (not in table): `fontSizeSm`, `fontSizeLg`, `colorInfo`, `borderColor` — table may be incomplete.

## Rules (6 CSS selectors)

`.Input`, `.Input:hover`, `.Input:focus`, `.Input:active`, `.Input--invalid`, `.Label`

Standard CSS properties used (e.g., `color`, `boxShadow`).

## OXXO Reference

> [!info] `paypal.FUNDING.OXXO` in code example
> The style example uses `paypal.FUNDING.OXXO` — OXXO is a Mexican voucher payment method not seen in any other ingested document. May be an unlisted/undocumented APM or future addition.

## Raw Sources

- [[paypal-apm-style-reference]] — verbatim reference page

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview
- [[source-paypal-apm-js-sdk-reference]] — JS SDK reference (funding constants, button options)
