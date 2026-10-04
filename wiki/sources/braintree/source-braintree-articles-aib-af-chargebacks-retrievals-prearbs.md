---
title: "Braintree AIB AF Chargebacks, Retrievals, and Pre-Arbs"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-af/chargebacks-retrievals-prearbs"
raw_files:
  - "braintree/articles/aib-af/chargebacks-retrievals-prearbs-2026-09-16.md"
tags: [braintree, aib-af, disputes, chargebacks, retrievals, pre-arbitration]
---

## Overview

This collected [[braintree]] AIB AF webpage explains notifications, response routes, deadlines, financial effects, statuses, and reporting for credit-card chargebacks, retrievals, and pre-arbitrations. It expressly routes PayPal disputes elsewhere. Treat it as captured AIB AF document evidence for [[disputes]], not as AIB BF behavior, independent current bank or card-network authority, a merchant-specific agreement, or a universal Braintree pricing schedule. The article body identifies no region or pricing plan and gives no numerical fee amount.

## Key takeaways

- Dispute notifications go by email to the first gateway admin by default, with Control Panel configuration for frequency and recipients. User recipients are limited by role and associated sub-merchants, while an address entered directly receives every dispute notification even if it belongs to a limited-permission user. The page also routes Open, Won, and Lost status updates for chargebacks, retrievals, and pre-arbs to webhooks.
- The page documents both a rolling Control Panel interface and a legacy interface, and it separately states that disputes can be managed through an API. Every listed dispute type has a reply-by date; at 12am on that date in the account time zone, the evidence opportunity ends. Expiration sends an Accept response on the merchant's behalf and removes the ability to dispute the chargeback, while the case remains Expired in reporting.
- A chargeback immediately debits the transaction amount from payout funds scheduled for deposit; an insufficient payout makes the account negative until further processing. The cardholder's bank evaluates submitted evidence. If the merchant wins, the amount returns to payout funds; if the merchant loses or accepts, the cardholder keeps it. The page says a chargeback fee applies regardless of outcome but does not state an amount.
- A retrieval is described as an information request for an unidentifiable charge. Unlike chargebacks and pre-arbs, it does not remove the transaction amount from payout funds or incur a retrieval-processing fee. The article recommends providing identifying information, but says a fraud-related retrieval often becomes a chargeback despite submitted evidence and usually favors a refund; these are captured article recommendations, not guaranteed outcomes.
- A pre-arb is described as a second cardholder challenge after the merchant wins a chargeback. The article says merchants rarely win without new and compelling evidence, routes them to review the original evidence, generally recommends accepting when there is no additional evidence, and says a pre-arb processing fee applies regardless of outcome. Its Won status says funds should return to the bank account within 2–3 business days; that schedule is not proof of actual deposit arrival. The Dispute Report shows status-history lines and is expressly not for reconciliation.

## Evidence boundaries

> [!warning] Captured AIB AF scope
> Keep the documented behavior and fee statements scoped to this captured AIB AF article. Do not transfer them to AIB BF, another processor/account variant, or current bank/card-network policy. The body does not identify a region or pricing plan and does not state numerical chargeback or pre-arb fee amounts; obtain merchant-specific terms from the applicable agreement or account channel.

> [!warning] Deadline and linked-authority boundaries
> Missing the reply-by cutoff triggers acceptance on the merchant's behalf and ends the evidence opportunity described here. The page's links establish navigation only: they do not prove that unread API, webhook, reason-code, card-verification, role-permission, or support pages agree with this snapshot or establish a broader contract. A Control Panel procedure does not imply API absence, and the page itself states an API route.

## Detail locators

- Credit-card rather than PayPal-dispute scope: opening note, raw lines 17–18.
- Email defaults, recipient permission behavior, merchant-account coverage recommendation, and Open/Won/Lost webhook route: `## Notifications`, raw lines 23–44.
- Rolling and legacy Control Panel procedures, reply-by cutoff, account-time-zone basis, expiration effect, reason-code guidance, and stated API route: `## Managing in the Control Panel`, raw lines 47–83.
- Chargeback debit, negative-account condition, bank decision, outcome-dependent fund disposition, fee boundary, acceptance meaning, and automatically included Control Panel evidence: `## Chargebacks`, raw lines 88–111.
- Retrieval definition, no-debit/no-fee distinction, identifying-information recommendation, and fraud-related refund guidance: `## Retrievals`, raw lines 114–120.
- Pre-arb definition, original-evidence review, additional-evidence qualification, acceptance guidance, and outcome-independent processing-fee statement: `## Pre-arbs`, raw lines 123–129.
- Status definitions, including the captured 2–3-business-day Won wording and reply-by forfeiture: `## Statuses`, raw lines 132–140.
- Dispute Report permission and status-history purpose, plus the express non-reconciliation boundary: `## Dispute Report`, raw lines 143–152.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]

## Raw Sources

- [[raw/braintree/articles/aib-af/chargebacks-retrievals-prearbs-2026-09-16|Braintree AIB AF Chargebacks, Retrievals, and Pre-Arbs]] - fully read 2026-09-16 snapshot covering credit-card dispute notifications, management routes, deadlines, chargeback/retrieval/pre-arb effects, statuses, and reporting
