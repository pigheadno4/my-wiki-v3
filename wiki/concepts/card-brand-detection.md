---
title: "Card Brand Detection"
type: concept
category: technology
tags: [cards, card-brand, bin, iin, checkout, input-formatting]
---

## Definition

Card-brand detection infers one or more likely payment-card brands from a partial or complete primary account number prefix. Checkout interfaces use the result to select formatting gaps, expected number lengths, security-code labels, brand artwork, or candidate-network controls while the shopper types.

Detection is not equivalent to validating a card number, confirming that a network will accept it, proving merchant enablement, or authorizing a payment. Those decisions require separate validation, processor configuration, network rules, and transaction evidence.

## Partial and Ambiguous Matches

A detector may intentionally return several candidates for a short prefix. A more specific complete BIN/IIN pattern can resolve the ambiguity later. For example, a broad Visa prefix can initially overlap with a more specific Elo prefix; once the complete stronger Elo pattern is present, the result can narrow to Elo.

Brand order matters when candidates have equal specificity or when a checkout chooses how to present unresolved candidates. Co-badged network selection is a separate concern: detection can identify possible networks, but regulatory or merchant-choice logic must preserve the cardholder's permitted choice rather than silently treating detector priority as the selected processing network. See [[co-badged-cards]].

## Metadata and UI Use

Useful detector metadata commonly includes:

- a stable brand identifier and display name;
- accepted number lengths;
- display-gap positions; and
- the security-code label and expected length.

Consumers should normalize input before detection and apply their own validity rules. A detector's length and prefix metadata can support a form, but it does not establish Luhn validity, expiry validity, CVV correctness, tokenization success, or payment acceptance.

## Braintree `credit-card-type@10.3.0`

Braintree's retained `credit-card-type@10.3.0` implementation is a CommonJS TypeScript utility with no runtime dependencies. It supports 15 built-in brands and adds Troy in `10.3.0`; Naranja and Verve entered earlier in the v10 line.

The default function returns all configured brands for an empty string, returns zero or more candidates for input prefixes, and reduces to one candidate only when every match has a complete pattern and one has the strongest pattern length. Built-in or custom behavior can be changed through process-level `addCard`, `updateCard`, `removeCard`, `changeOrder`, and `resetModifications` operations.

The 2026-11-07 release-notes revision supplies upstream confirmation of the already-retained Troy feature for the same 10.3.0 SHA. It changes evidence availability, not detector code or payment acceptance. The earlier June 30 commit-backed record and August baseline ingest remain historical evidence; the new GitHub record reports publication on October 13. [[source-github-credit-card-type]] [[changelog-github-credit-card-type]]

> [!warning] Documentation and runtime differences
> The README tells callers to supply normalized numeric input, but the exact runtime only checks whether the value is a string-like object; it does not itself reject every non-digit character before matching. The README also says an unknown `getTypeInfo` value returns `undefined`, while the exact implementation passes the missing value through its JSON clone helper and returns `null`. The repository changelog says v9 dropped boxed `String` support, but the retained v10 input check still accepts `cardNumber instanceof String`. Consumers should rely on explicit input validation and test exact-version behavior.

## Elo Range Extension in `credit-card-type@10.3.1`

The separately retained 10.3.1 source adds Elo ranges `650057-650081` and `651680-651704` without changing the detector algorithm, public API, brand count, card-length/CVV definitions or runtime dependencies. Under the default configuration, the complete new six-digit patterns outrank the broader Discover `65` and Maestro `6` patterns; shorter input may still return several candidates. These are exact-package recognition rules, not an authoritative current BIN allocation list or proof of acceptance. [[source-github-credit-card-type]] [[changelog-github-credit-card-type]]

Braintree Web 3.148.0 separately pins this package version. The independent utility evidence now explains its Elo-range change; it does not establish live Hosted Fields, network routing or successful payments. The older 10.3.0 Troy baseline and documentation/runtime conflicts above remain preserved. [[braintree-web-sdk]]

## Related

- [[source-github-credit-card-type]] - cumulative exact 10.3.0/10.3.1 source and behavior boundaries
- [[changelog-github-credit-card-type]] - package-qualified release history
- [[braintree-web-sdk]] - checkout SDK that consumes card-brand information in Hosted Fields
- [[co-badged-cards]] - network choice and compliance beyond brand inference

## Sources

- [[source-github-credit-card-type]] - retained implementation, package metadata, README, and repository changelog
