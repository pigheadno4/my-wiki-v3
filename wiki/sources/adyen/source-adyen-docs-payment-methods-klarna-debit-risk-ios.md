---
title: "Klarna Debit Risk for iOS | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna-debit-risk/ios"
raw_files:
  - "adyen/docs/payment-methods/klarna-debit-risk/ios/2026-09-15.md"
tags: [adyen, klarna-debit-risk, ios, navigation]
---

## Overview

This 2026-09-15 Adyen Docs iOS chooser routes Klarna Debit Risk to separate **Drop-in** and **Components** guides. It also links the base iOS Sessions and Advanced integration guides that must be built before the method add-on. It is navigation, not evidence of a configured merchant, working iOS component, payment outcome or SEPA token. See [[adyen-online-payments]] and [[adyen]].

## Key takeaways

- Choose the iOS Drop-in child for the all-in-one UI route or the iOS Components child for the component route. The child guides own flow prerequisites, redirect handling, request fields and method-specific behavior.
- The Components description literally says "Use the None". The linked iOS Components guide also shows a `None` initialization placeholder; this chooser does not identify a verified SDK class. Verify the actual SDK API before implementing.
- The four `## See also` links cover iOS Drop-in and Components under both Sessions and Advanced. They are base integration routes, not proof that a given Klarna Debit Risk flow or account is enabled.

## Detail locators

- Purpose and Drop-in/Components child routes: pinned raw lines 15–27; the `None` wording is at line 27.
- Main iOS Sessions and Advanced prerequisite guide links: `## See also`, lines 29–36.

## Related

- [[adyen-online-payments]] — provider online-payment context.
- [[source-adyen-docs-payment-methods-klarna-debit-risk-ios-drop-in]] — method-specific iOS Drop-in guide.
- [[source-adyen-docs-payment-methods-klarna-debit-risk-ios-component]] — method-specific iOS Components guide and initialization caveat.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna-debit-risk/ios/2026-09-15|2026-09-15 Klarna Debit Risk iOS chooser]]
