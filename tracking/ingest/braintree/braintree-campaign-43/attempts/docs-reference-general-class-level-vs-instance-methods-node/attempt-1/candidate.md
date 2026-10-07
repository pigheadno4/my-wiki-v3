---
title: "Braintree Class-Level vs Instance Methods (Node.js route)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/class-level-vs-instance-methods/node"
raw_files:
  - "braintree/docs/reference/general/class-level-vs-instance-methods/node-2026-09-16.md"
tags: [braintree, node-js, server-sdk, gateway, authentication, legacy-integration]
---

## Overview

This collected Braintree page explains the historical distinction between class-level methods backed by one shared configuration object and instance methods backed by a configurable gateway object. Although the canonical route is labeled for Node, the page says Node SDK integrations can skip this change because instance methods were already the default there; its migration examples and dated rollout details concern Ruby, Python and PHP rather than a Node API transition.

## Key takeaways

- Class-level methods use one shared configuration object for Braintree requests, while instance methods use a configurable gateway object. The page presents instance methods as avoiding global authentication management and making differently credentialed tools, such as OAuth-based tools, easier to add.
- For Node, the captured page says instance methods were already the default and that the January 2018 documentation change did not affect existing or planned Node integrations. This is a page-level historical statement, not a newly verified claim about a current Node package.
- The displayed gateway-construction and transaction-sale before/after examples are Ruby. The constructor example sets the Ruby gateway environment to `:sandbox`; the page supplies no Node method signature, Node construction snippet, production-environment behavior, package version, runtime version or release boundary.
- The dated transition applies to Ruby documentation on January 4, 2018 and to new Python or PHP integrations after February 27, 2018. Existing integrations were not required to change, and the page says both gateway-configuration methods would continue to be supported.

## Detail locators

- Applicability exclusions for Node, .NET and Java plus dated Ruby, Python and PHP conditions: `# Class-Level vs Instance Methods > **AVAILABILITY**`, lines 17-28.
- Shared class-level configuration versus configurable gateway-instance distinction and the authentication rationale: `## Background`, lines 31-39.
- Historical Ruby documentation change, Ruby `Braintree::Gateway.new` sandbox construction and `gateway.transaction.sale` examples: `## What changed in January 2018`, lines 42-101.
- Page-level statement that instance methods were already the default for Node and that Node integrations were unaffected: `## What changed in January 2018`, line 102, and `## What this means for you`, lines 105-107.

## Evidence limitations

> [!warning] Node route without Node code or version evidence
> The canonical URL ends in `/node`, but every displayed configuration and sale example is Ruby. This unversioned website snapshot does not identify a Node SDK package version or runtime, establish current authentication behavior or support, or supply exact Node method or constructor semantics. The Ruby `:sandbox` example must not be generalized into a Node environment guarantee. Use exact package-qualified implementation evidence for current Node behavior.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/general/class-level-vs-instance-methods/node-2026-09-16|Braintree Class-Level vs Instance Methods (Node.js route)]] - complete collected page containing the applicability notice, historical distinction and Ruby-only examples
