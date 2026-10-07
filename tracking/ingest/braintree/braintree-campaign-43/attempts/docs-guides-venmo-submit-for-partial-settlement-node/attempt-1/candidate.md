---
title: "Braintree Venmo Submit for Partial Settlement (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/venmo/submit-for-partial-settlement/node"
raw_files:
  - "braintree/docs/guides/venmo/submit-for-partial-settlement/node-2026-09-16.md"
tags: [braintree, venmo, nodejs, transactions, partial-settlement]
---

## Overview

This collected Braintree website guide is a Venmo-routed Node.js page for `gateway.transaction.submitForPartialSettlement()`. It shows callback and Promise request forms for submitting part of a parent authorization amount and describes repeated partial-settlement calls that create separate child transactions. The page is an unversioned 2026-09-16 documentation snapshot for [[braintree]] and [[braintree-server-sdk]], not package-qualified SDK implementation evidence.

## Key takeaways

- The guide frames the operation as explicit submission of a portion of an authorization. The preceding sentence has damaged option and method rendering, so this source does not reconstruct which ordinary settlement option or call must be omitted.
- The operation takes a parent authorization transaction ID and an amount. The amount must be greater than zero; multiple calls may cumulatively reach, but not exceed, the parent authorization amount unless the merchant's industry and processor support settlement adjustment. The parent-status prerequisite at raw line 40 is damaged and appears only as `ADD`, so no exact prerequisite status is retained from this page.
- The page says multiple partial settlements may be made against one authorization and describes a separate child transaction for each shipped portion. Each child carries the original transaction details with the partial amount. The captured parent and child lifecycle status names are missing, so they are not reconstructed.
- After the parent enters an unnamed terminal status, no additional settlements can be created against it. The page lists transition conditions, but several required status values are absent from the capture; use the raw locator rather than treating the damaged list as an executable lifecycle contract.
- Refunds are limited to child transactions, capped at the amount settled on each child, and allowed only after the corresponding transaction is fully settled. The required state name is missing from the captured text. The Control Panel links parent and child records through authorization and settlement identifiers.

> [!warning] Route, environment and outcome boundaries
> The Venmo URL and guide route do not by themselves establish current Venmo support, merchant or transaction eligibility, or successful authorization, settlement or funding. The page states no exact Node SDK package version and makes no Sandbox-versus-Production distinction. Its callback and Promise snippets are request examples, not runtime outcome evidence.

## Detail locators

- Explicit partial-amount submission context and damaged ordinary-settlement option or call: `# Submit for Partial Settlement`, raw lines 16-18.
- Callback and Promise `gateway.transaction.submitForPartialSettlement()` examples: `### Callback` and `### Promise`, raw lines 19-33.
- Repeated partial settlements, parent authorization and separate child-transaction purpose: raw lines 34-37.
- Damaged parent-status prerequisite plus required amount, positive-value rule, cumulative ceiling and industry/processor-qualified settlement-adjustment exception: `#### Arguments`, raw lines 38-44.
- Child creation, missing lifecycle states, terminal-parent conditions and no-further-settlement restriction: `## Transaction settlement`, raw lines 47-58.
- Child-only refund scope, per-child amount cap and fully-settled prerequisite with missing state name: `## Refunds`, raw lines 59-64.
- Parent and child linkage in the Control Panel: `## Control Panel visibility`, raw lines 67-72.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Broader request reference and retained availability conflict: [[source-braintree-transaction-submit-for-partial-settlement-node]]
- Venmo server-side transaction and Vault route: [[source-braintree-docs-guides-venmo-server-side-node]]

## Raw Sources

- [[raw/braintree/docs/guides/venmo/submit-for-partial-settlement/node-2026-09-16|Braintree Venmo Submit for Partial Settlement Node.js guide (captured 2026-09-16)]] - complete assigned page covering the partial-settlement action, amount limits, parent/child model, damaged lifecycle rendering, refund restrictions and Control Panel links
