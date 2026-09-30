---
title: "Braintree PayPal Disputes"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/disputes"
raw_files:
  - "braintree/articles/guides/payment-methods/paypal/disputes-2026-09-16.md"
tags: [braintree, paypal, disputes, chargebacks, control-panel]
---

## Overview

This pinned Braintree article explains how merchants manage PayPal disputes through the Braintree Control Panel. It is a PayPal-specific retrieval route for account setup, PayPal dispute stages, deadlines, fees, Control Panel actions and status interpretation; it is not a general guide to Braintree credit-card disputes or Braintree's server-side dispute APIs.

## Key takeaways

- PayPal dispute actions and uploaded evidence can be managed in either the Braintree Control Panel or PayPal Resolution Center, with actions reflected across both. The article itself focuses on the Control Panel path.
- Control Panel management requires a full PayPal integration through Braintree, linked Braintree and PayPal accounts, explicit enablement, and a user role with the Add/Edit Processing Options permission.
- The article distinguishes Retrieval, Claim and Chargeback stages: the customer starts a retrieval, PayPal decides an escalated claim, and the customer's bank decides a chargeback. A retrieval places the disputed amount on temporary hold; each case has a reply-by date whose midnight cutoff uses the Control Panel's configured time zone.
- Retrievals and claims resolved through PayPal or the Braintree gateway do not incur dispute fees, while issuer or bank-account-provider fees can apply when a case becomes a chargeback or starts directly with that provider. PayPal Seller Protection may separately affect movement of money.
- The Braintree Control Panel labels PayPal's Dispute stage as Retrieval. The article recommends resolving retrievals directly with customers and escalating to PayPal only as a final resort; escalation closes the retrieval and opens a linked dispute.

## Evidence boundaries

> [!warning] PayPal-specific workflow
> The stages, labels, fees, account-linking prerequisites and cross-platform synchronization here are stated for PayPal disputes. Do not generalize them to Braintree credit-card disputes, other payment methods or server-SDK dispute operations. The article says that credit-card disputes not managed in the Control Panel must continue through the merchant's normal workflow.

> [!warning] Deadlines, funds and status interpretation
> Missing the reply-by cutoff removes the opportunity to act. Accepting a claim or chargeback returns funds to the customer, while a Braintree `Disputed` status can mean either submitted evidence is under evaluation or PayPal has placed a case Under Review without requiring evidence; the latter may return to `Open` if PayPal later requires evidence.

## Detail locators

- Control Panel and Resolution Center synchronization and article scope: opening paragraphs, lines 16-18.
- Full PayPal integration, linked-account, enablement and role-permission prerequisites: `## Setup`, lines 21-34.
- Retrieval, Claim and Chargeback roles; temporary hold; reply-by cutoff; fund release and Seller Protection qualification: `## Dispute stages` through `## Timeline`, lines 37-57.
- Notification recipients and permission behavior: `## Notifications`, lines 62-95.
- PayPal dispute fee boundary: `## Fees`, lines 98-102.
- PayPal versus credit-card Control Panel workflow and current/legacy UI routes: `## Managing in the Braintree Control Panel`, lines 105-139.
- Braintree Retrieval label, merchant actions and escalation effect: `### Retrievals` through `#### Escalating to PayPal`, lines 144-172.
- Acceptance effect and evidence examples: `### Accepting` through `#### Uploading evidence`, lines 175-210.
- Status meanings and PayPal Under Review ambiguity: `## Statuses` through `### A note on Disputed statuses`, lines 213-235.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]
- Provider route: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/paypal/disputes-2026-09-16|Braintree PayPal Disputes article]] - complete collected article covering PayPal-specific Control Panel setup, stages, deadlines, notifications, fees, actions, evidence and statuses
