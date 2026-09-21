---
title: "Braintree Search Fields (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/searching/search-fields/node"
raw_files:
  - "braintree/docs/reference/general/searching/search-fields/node-2026-09-16.md"
tags: [braintree, node-js, search, filters]
---

## Overview

This Braintree Node.js reference documents the three search-field categories used in server-SDK searches: text, multiple-value and range fields. It identifies their supported operators and preserves the text-length and range-boundary qualifications needed to select and apply the correct field type; transaction examples and detailed syntax remain routed to the raw page.

## Key takeaways

- Text fields support `is`, `isNot`, `startsWith`, `endsWith` and `contains`, and each text search field is limited to 255 characters. The displayed examples apply those operators to a transaction customer-email search.
- Multiple-value fields support `is` and `in`. The page illustrates them with transaction-status searches, including an `in` list; the examples do not establish which fields are available on every searchable object.
- Range fields support `is`, `between`, `max` and `min`. For non-time filters, `between` is inclusive and `max` and `min` are respected as written.
- Time-based filters have different boundary behavior: the lower bound is inclusive, the upper bound is exclusive regardless of the chosen range operator, and one minute is automatically added to the upper bound. The page's one-hour example consequently includes timestamps through `17:00:59` but excludes `17:01:00`.
- The page links to separate search-results guidance. That navigation-only page is not used here to claim result-consumption, stream or callback behavior.

> [!warning] Time-range qualification
> Do not apply the non-time `between` semantics to time-based filters. Braintree documents an inclusive lower bound, an exclusive upper bound and an automatic one-minute addition to the upper bound for time searches, regardless of the range operator used.

## Detail locators

- Three supported field categories and separate search-results route: `# Search Fields`, lines 16-23.
- Text-field operators, 255-character limit and transaction customer-email examples: `## Text fields`, lines 26-59.
- Multiple-value operators and transaction-status examples: `## Multiple value fields`, lines 61-82.
- Range operators, non-time and time boundary qualifications, and the worked time example: `## Range fields`, lines 84-92.
- Node.js amount and created-at range examples: `## Range fields > ### Node.js`, lines 95-123.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/reference/general/searching/search-results/node-2026-09-16|Braintree Node.js search-results reference]] - navigation-only destination for result consumption; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/general/searching/search-fields/node-2026-09-16|Braintree Node.js search-fields reference]] - complete collected page covering field categories, operators, text limits, range-boundary qualifications and Node.js transaction-search examples
