---
title: "Braintree Managing Disputes via the API"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/disputes/managing"
raw_files:
  - "braintree/docs/guides/disputes/managing-2026-09-16.md"
tags: [braintree, disputes, chargebacks, evidence, api]
---

## Overview

This unversioned Braintree website guide, captured 2026-09-16, explains how an eligible merchant can locate and respond to cardholder-bank disputes through the API. It covers notification and retrieval routes, the choice to accept or challenge an open dispute, the reply-by deadline, evidence association, and the separate finalization step that sends the response and evidence to the cardholder's bank for review.

## Key takeaways

- API dispute management is available only to merchants who can access disputes in the Braintree Control Panel. A new bank-reported dispute creates an `open` dispute object for the relevant merchant account; the merchant then decides how to respond.
- Merchants can learn of disputes through configured email notifications or dispute webhooks, and can locate them through Dispute Search or Dispute Find requests. These are discovery routes, not proof that a response was accepted or that the dispute was won.
- Every dispute has a `replyByDate()`. Supporting evidence must be added and the dispute finalized before that deadline for the response to be considered by the cardholder's bank. Missing it forfeits the merchant's right to contest and changes the dispute status to `expired`.
- Accepting indicates that the merchant will take no further action; it does not necessarily mean agreement with the cardholder's claim. If the merchant does not respond by the reply-by date, Braintree says an Accept response is sent on the merchant's behalf and the dispute can no longer be contested.
- To challenge instead, the merchant associates text or file evidence with the dispute and then finalizes it before the reply-by date. File evidence requires upload followed by attachment to the dispute. Finalization forwards the response and evidence for bank review; this page does not establish a win, settlement, fund-return, or successful adjudication outcome.

## Detail locators

- Control Panel dispute-access prerequisite: `# Managing > AVAILABILITY`, lines 17-18.
- Creation of an `open` dispute object, merchant decision point, default email notification, webhook option, and Search/Find option: `## Locate open disputes`, lines 25-35.
- Dispute webhook setup and Dispute Opened notification route: `### Using dispute webhooks`, lines 38-44.
- Search, Find, and dispute response-object routes: `### Using dispute search and find requests`, lines 47-55.
- Reason-code purpose, reply-by deadline, forfeiture of contest rights, and transition to `expired`: `## Respond to open disputes`, lines 58-62.
- Accept call route, meaning of acceptance, and automatic Accept response after no timely response: `### Accepting disputes`, lines 65-69.
- Evidence requirements, text/file distinction, upload-and-attach sequence, repetition, and finalization route: `### Responding with evidence`, lines 72-89.
- Forwarding to the cardholder's bank for review and the warning that Braintree does not forward an unfinalized response after the reply-by date: `### Responding with evidence`, lines 91-95.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]
- API operation routes: [[source-braintree-dispute-search-node]], [[source-braintree-dispute-find-node]], [[source-braintree-dispute-accept-node]], [[source-braintree-dispute-add-text-evidence-node]], [[source-braintree-document-upload-create-node]], and [[source-braintree-dispute-finalize-node]]

## Related raw API references

- Dispute webhooks, Search, Find, Accept, Add Text Evidence, Document Upload Create, Add File Evidence, Finalize, the dispute response object, and Evidence Requirements are linked navigation targets in the captured guide; they were not read as factual evidence for this source.

## Raw Sources

- [[raw/braintree/docs/guides/disputes/managing-2026-09-16|Braintree Managing Disputes via the API guide]] - complete captured webpage covering access eligibility, dispute discovery, response deadline, acceptance, evidence association, finalization, and bank-review handoff
