---
title: "Braintree AIB BF Chargebacks, Retrievals, and Pre-Arbs"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-bf/chargebacks-retrievals-prearbs"
raw_files:
  - "braintree/articles/aib-bf/chargebacks-retrievals-prearbs-2026-09-16.md"
tags: [braintree, aib-bf, disputes, chargebacks, retrievals, pre-arbitration]
---

## Overview

This captured [[braintree]] AIB BF article describes credit-card chargebacks, retrievals, and pre-arbitrations, including notification, response, evidence, deadline, status, and reporting routes. It redirects PayPal disputes to a separate guide. Treat it as a 2026-09-16 Braintree-hosted snapshot for [[disputes]], not as independent current bank or card-network authority, and do not infer a region, pricing model, or expansion of the AIB/BF labels beyond what this page states.

## Key takeaways

- A chargeback begins when a cardholder disputes a transaction with their bank. The page says the transaction amount is immediately debited from payout funds and held by the cardholder's bank pending resolution; insufficient scheduled payout funds can leave the account negative. The bank evaluates the merchant's evidence, and the page says a chargeback fee applies regardless of whether the merchant wins, loses, or accepts. It gives no fee amount.
- Every chargeback, retrieval, or pre-arb has a Control Panel reply-by date. At 12am on that date, under the account time zone established during application, the opportunity to submit evidence ends. If the case expires, an Accept response is sent on the merchant's behalf and the chargeback can no longer be disputed, while the case retains Expired status in reporting.
- A retrieval is described as a request for information about an unidentifiable charge. In this documented AIB BF context, it does not remove the transaction amount from payout funds and does not incur a retrieval-processing fee. The article recommends providing identifying information to reduce chargeback risk, while noting that fraud-related retrievals often become chargebacks despite submitted evidence and may warrant a refund. This is article guidance, not a guaranteed outcome.
- A pre-arb occurs after a merchant wins a chargeback and the cardholder disputes the charge a second time. The article says merchants rarely win without new and compelling evidence, routes them to review the original evidence PDF, and generally recommends acceptance when there is no additional evidence. A pre-arb processing fee applies regardless of outcome, but no amount is stated.
- The article documents both Control Panel actions and an API-management route. It also describes email recipients, Open/Won/Lost webhook notifications, automatically included transaction-history evidence for Control Panel chargeback disputes, status meanings, and two dispute reports; use the raw locators for those operational details. Links to separate guides are navigation only and do not establish agreement with those linked pages.

## Evidence boundaries

> [!warning] Snapshot and account scope
> Keep deadline, fee, payout, evidence, and response statements scoped to this captured AIB BF route. The page does not define the AIB/BF labels, identify an independent current bank policy, state a region or pricing model, or provide fee amounts; do not transfer details from AF, Wells, or another account or processor variant.

> [!warning] Consequential response cutoff
> Missing the reply-by cutoff causes an Accept response to be sent on the merchant's behalf and ends the opportunity to dispute the chargeback.

## Detail locators

- Credit-card rather than PayPal-dispute scope: opening note, raw lines 17-18.
- Email recipient rules and Open/Won/Lost webhook route: `## Notifications`, raw lines 25-46.
- Current and legacy Control Panel actions, reply-by cutoff, account-time-zone basis, expiration effect, dispute-reason guidance, and API route: `## Managing in the Control Panel`, raw lines 49-85.
- Chargeback debit, evidence review, outcome and fee effects, acceptance, Control Panel evidence, and evidence-advice route: `## Chargebacks`, raw lines 90-113.
- Retrieval definition, no-debit/no-fee boundary, and qualified response guidance: `## Retrievals`, raw lines 116-122.
- Pre-arb definition, original-evidence PDF route, additional-evidence qualification, acceptance guidance, and fee effect: `## Pre-arbs`, raw lines 125-131.
- Status definitions, including Expired and the qualified Won return timing: `## Statuses`, raw lines 134-143.
- Report permission, Dispute Report purpose, and financial-impact reconciliation fields: `## Dispute Reports`, raw lines 146-163.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]
- Administration route: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/aib-bf/chargebacks-retrievals-prearbs-2026-09-16|Braintree AIB BF Chargebacks, Retrievals, and Pre-Arbs]] - fully read captured article covering credit-card dispute notifications, management, evidence, deadlines, payout and fee effects, statuses, and reports
