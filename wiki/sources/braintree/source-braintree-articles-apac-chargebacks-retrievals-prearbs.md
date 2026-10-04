---
title: "Braintree APAC Chargebacks, Retrievals, and Pre-Arbs"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/apac/chargebacks-retrievals-prearbs"
raw_files:
  - "braintree/articles/apac/chargebacks-retrievals-prearbs-2026-09-16.md"
tags: [braintree, apac, disputes, chargebacks, retrievals, pre-arbitration]
---

## Overview

This 2026-09-16 Braintree-hosted APAC-route snapshot explains merchant handling of credit-card chargebacks, retrievals, and pre-arbitrations through dispute notifications, the Control Panel, and a linked API route. It describes response deadlines, evidence handling, bank adjudication, and the resulting chargeback, fee, and net-disbursement effects. It explicitly directs PayPal disputes to separate documentation.

The article is Braintree account-facing documentation, not independent current bank or card-network policy, a merchant-specific agreement, or evidence that its account, regional, pricing, status, or timing behavior applies to sibling Braintree routes. Its references to net disbursements and deposits describe dispute-related funding effects; they do not define authorization, capture, ordinary transaction settlement, or a general funding timeline.

## Key takeaways

- A dispute notification can be handled by replying to the email with evidence or through the Control Panel. User Recipients receive notifications according to their roles and associated sub-merchants, while addresses entered directly in the Email Address field receive all dispute notifications. The page also routes to API management and webhook setup, but those linked targets were not used here as behavioral evidence.
- Each chargeback, retrieval, or pre-arb has a Control Panel reply-by date. At 12am on that date in the account time zone, the opportunity to submit evidence ends; expiration causes an Accept response to be sent on the merchant's behalf and forfeits further dispute of the chargeback, while reporting remains Expired.
- For a chargeback, the article says the transaction amount and fee are debited from net disbursements before bank-account deposit and held by the cardholder's bank pending resolution. A win returns the disputed amount to net disbursements; a loss or acceptance returns the funds to the cardholder. The chargeback fee remains non-refundable regardless of outcome.
- The listed chargeback fee depends on settlement currency: 30 SGD, 160 HKD, or 90 MYR. This captured list is not a universal or current price schedule and should not be transferred to another account, region, currency, processor, or commercial model.
- A retrieval is an information request for an unidentifiable charge; unlike a chargeback or pre-arb, it does not remove funds from net disbursements or incur a processing fee in this snapshot. The article recommends disputing with identifying information, and separately advises that refunding may help when suspected fraud would likely turn into a chargeback; these are recommendations, not guarantees.
- A pre-arb is described as a second cardholder dispute after the merchant won the chargeback. The article permits a response but characterizes low merchant success without new and compelling evidence, then recommends reviewing the original evidence and accepting when no additional evidence exists.
- Status presentation depends on response channel: Accepted and Disputed are shown only for Control Panel responses; evidence sent by email can still be disputed, with the displayed result later becoming Won or Lost. A Won status says funds should return to the bank account within 2-3 business days, while the issuing bank may have up to 45 days after evidence submission to continue the dispute.

> [!warning] Reply-by cutoff and account time zone
> Treat the Control Panel's reply-by date and the account time zone as controlling for this captured route. The article says the evidence opportunity is lost at 12am on that date and an Accept response is then sent on the merchant's behalf. Recheck the live account and current official guidance before acting.

> [!warning] Snapshot, pricing, and adjudicator boundary
> The amounts, timing, status display, and net-disbursement behavior are qualified by this APAC-route Braintree snapshot and the merchant account's settlement currency and settings. The cardholder's bank evaluates the submitted documentation; this page is neither independent current bank/network authority nor authorization, settlement-instruction, or general funding-timeline documentation.

## Detail locators

- Credit-card-only scope and separate PayPal-dispute route: opening `NOTE`, raw lines 17-18.
- Email notification trigger, Control Panel notification settings, recipient role/sub-merchant limits, direct-address behavior, and merchant-account recommendation: `## Notifications`, raw lines 25-44.
- Email versus Control Panel evidence submission and available Control Panel actions: `## Managing Disputes`, raw lines 47-60.
- Reply-by cutoff at 12am in the account time zone and automatic Accept/Expired consequences: `## Managing Disputes`, raw lines 64-66.
- API-management navigation and reason-based recommendation boundary: `## Managing Disputes`, raw lines 68-72.
- Chargeback definition, net-disbursement debit, bank adjudication, return paths, and non-refundable fee: `## Chargebacks`, raw lines 77-86.
- Settlement-currency-qualified fee list (30 SGD, 160 HKD, 90 MYR): `### Chargeback fees`, raw lines 84-92.
- Acceptance effect and advisory examples: `### Accepting a chargeback`, raw lines 94-98.
- Evidence route and Braintree facilitation statement: `#### Submitting evidence`, raw lines 106-110.
- Submission deadline, issuer's stated up-to-45-day continuation window, and monthly-statement reflection: `#### Dispute timelines`, raw lines 113-117.
- Retrieval definition, no-removal/no-fee distinction, and qualified recommendations: `## Retrievals`, raw lines 120-126.
- Pre-arb definition, experience-qualified success warning, original-evidence download route, and additional-evidence condition: `## Pre-arbs`, raw lines 129-135.
- Status meanings, 2-3-business-day Won wording, and response-channel display qualification: `## Statuses`, raw lines 138-149.
- Permission-qualified Dispute Report route and explicit non-reconciliation warning: `## Dispute Report`, raw lines 152-161.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]

## Raw Sources

- [[raw/braintree/articles/apac/chargebacks-retrievals-prearbs-2026-09-16|Braintree APAC Chargebacks, Retrievals, and Pre-Arbs]] - complete captured article for APAC-routed credit-card dispute handling, deadlines, fund and fee effects, retrievals, pre-arbs, statuses, and report boundaries
