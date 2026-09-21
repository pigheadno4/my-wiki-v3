---
title: "Braintree Search Results (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/searching/search-results/node"
raw_files:
  - "braintree/docs/reference/general/searching/search-results/node-2026-09-16.md"
tags: [braintree, node-js, search, search-results]
---

## Overview

This Braintree Node.js reference explains how search results are consumed as streams or callback-provided iterables. It also documents lazy record retrieval, the resulting race conditions, and maximum result counts; implementation examples remain available at the exact raw locators below.

## Key takeaways

- As of version 1.11.0, calling a search function without a callback returns a Node stream in object mode. The page demonstrates both piping that stream to an object-mode writable stream and consuming `data` and `end` events before calling `resume()`.
- When a callback is supplied, the yielded response object defines an `each` method for result iteration. This callback form is distinct from the no-callback stream behavior.
- Searches initially return matching IDs and then fetch each record dynamically during iteration. A record deleted during iteration is skipped; an updated record is returned only if it still matches the criteria and otherwise is skipped.
- Because of those race conditions, the exact result count is not known while iterating. The displayed stream example reads `searchResponse.length()` after the `ready` event as the maximum number of results, not as a guaranteed final count.
- Transaction searches return at most 50,000 results, while all other searches return at most 10,000.

## Detail locators

- Version-qualified no-callback object-mode stream behavior and the `pipe()` example: `## Stream responses`, lines 16-29.
- Event-driven `data` / `end` consumption and `resume()`: `## Stream responses`, lines 31-43.
- Callback-provided iterable response and `response.each()`: `## Iterable responses`, lines 45-57.
- Lazy ID-first retrieval and deletion/update race behavior: `## Race conditions`, lines 59-73.
- Maximum-count qualification and `ready` / `searchResponse.length()` example: `## Maximum size`, lines 76-88.
- Transaction versus other-search result caps: `## Search limit`, lines 90-93.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/general/searching/search-results/node-2026-09-16|Braintree Node.js search-results reference]] - complete collected page covering stream and callback result consumption, lazy retrieval race behavior, maximum-count access, and result caps
