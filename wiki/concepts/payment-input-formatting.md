---
title: "Payment Input Formatting"
type: concept
category: technology
tags: [checkout, input-formatting, cards, browser-compatibility]
---

## Definition

Payment input formatting constrains and presents shopper-entered values while they type. A formatter can accept characters through a pattern, insert permanent separators, preserve the caret, normalize paste behavior, and expose an unformatted value for downstream use.

Formatting is not card-brand detection, primary-account-number validation, secure masking, tokenization, or payment processing. A correctly formatted value may still be invalid or unacceptable, and formatting code does not reduce the merchant's PCI obligations by itself.

## Pattern and Event Model

A pattern commonly combines input placeholders with automatically inserted characters such as spaces or punctuation. Implementations must account for selection ranges, backspace and forward-delete behavior, autofill, paste events, and input-method differences so separators do not displace the caret or duplicate input.

A paste callback can inspect the unformatted value before final formatting and select a different pattern. This supports presentation changes such as switching between card-number groupings, but the callback remains responsible for any brand or validity decision that drives the switch.

## Browser Compatibility

Browser and keyboard event behavior is not uniform. Formatters may need platform-specific strategies for iOS, Android Chrome, older WebViews, or legacy browsers, and may need to disable active formatting when a browser cannot preserve digits reliably. Browser-detection dependencies therefore form part of the runtime evidence boundary.

## Braintree Restricted Input

Braintree's `restricted-input@4.2.0` accepts alpha, digit, and wildcard placeholders, inserts permanent characters, maintains selection state, reformats pasted and autofilled values, and exposes `getUnformattedValue()`, `setPattern()`, and static `supportsFormatting()` APIs. Its strategy selection covers iOS, Android Chrome and ChromeOS, KitKat Chromium WebViews, IE9, and a base browser path.

The retained implementation disables formatting for detected Samsung browser cases because digits can be dropped. The exact classification depends on delegated `@braintree/browser-detection@^2.1.1` behavior, which is not contained in this repository snapshot.

## Related

- [[source-github-restricted-input]] - exact commit-qualified Braintree implementation and historical behavior
- [[changelog-github-restricted-input]] - commit and package-history synthesis
- [[card-brand-detection]] - brand inference that may select an input pattern but does not perform formatting
- [[braintree-web-sdk]] - browser checkout SDK context

## Sources

- [[source-github-restricted-input]] - retained README, TypeScript implementation, package metadata, and changelog
