---
title: "Braintree Dispute Add Text Evidence (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/dispute/add-text-evidence/node"
raw_files:
  - "braintree/docs/reference/request/dispute/add-text-evidence/node-2026-09-16.md"
tags: [braintree, node-js, disputes, evidence]
---

## Overview

This Braintree Node.js reference documents adding textual evidence to a dispute with `gateway.dispute.addTextEvidence()`. API dispute management is restricted to merchants who can access disputes in the Braintree Control Panel, and text evidence can be added only while the dispute has status `open`.

## Key takeaways

- Managing disputes through the API is available only to merchants who can access disputes in the Braintree Control Panel.
- The page limits text-evidence addition to disputes with status `open`.
- The examples show a dispute ID paired either with a plain text string or with an object containing `category` and `content`. Use the raw locators below for the full category table, conditional combinations, length guidance and categorized-input examples rather than treating this entry as an exhaustive evidence schema.
- If evidence is added successfully, the result is successful and includes the evidence object; otherwise the page directs readers to validation errors.
- Categorized evidence is conditional: the page says compelling evidence should use the listed category codes, warns that additional validation can depend on the dispute reason code, and notes that not every dispute requires categorized evidence.

> [!warning] Adding evidence is not final submission
> This page uses "submit textual evidence" for adding an evidence item to an `open` dispute. The separate [[source-braintree-dispute-finalize-node|Braintree Dispute Finalize (Node.js)]] reference documents the required finalization step for submitting accumulated evidence to the banks and changing the dispute to `Disputed`. Do not treat `addTextEvidence()` as final submission or infer a status transition from this page.

## Detail locators

- Control Panel access restriction and `open`-status eligibility: `# Dispute: Add Text Evidence`, lines 16-20.
- Plain-text `gateway.dispute.addTextEvidence()` invocation and result/evidence handling: `# Dispute: Add Text Evidence > first ### Promise`, lines 21-40.
- Categorization purpose, reason-code-dependent validation and not-all-disputes qualification: `## Valid text evidence categories`, lines 42-47.
- Complete category descriptions, conditional combinations and stated length or URL guidance: `## Valid text evidence categories`, lines 49-195.
- Categorized `{ category, content }` examples: `## Examples > ### Submitting categorized evidence > ### Node`, lines 198-220.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]
- Separate final-submission operation: [[source-braintree-dispute-finalize-node]]

## Related raw API references

- [[raw/braintree/docs/reference/response/dispute/node-2026-09-16|Braintree Node.js Dispute response reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/dispute/add-text-evidence/node-2026-09-16|Braintree Node.js add-text-evidence request reference]] - complete collected page covering access and status restrictions, plain and categorized text-evidence examples, category guidance, result handling and validation routes
