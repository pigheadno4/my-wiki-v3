---
title: "Braintree Wells Flat Chargebacks, Retrievals, and Pre-Arbs"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-flat/chargebacks-retrievals-prearbs"
raw_files:
  - "braintree/articles/wells-flat/chargebacks-retrievals-prearbs-2026-09-16.md"
tags: [braintree, wells-flat, disputes, chargebacks, retrievals, pre-arbitration]
---

## Overview

This captured Braintree Wells Flat article describes the credit-card dispute lifecycle, notifications, response routes, deadlines, statuses, and reporting for its documented account context. It is a retrieval entry for the collected Braintree page, not independent current Wells policy, not a universal Braintree pricing schedule, and not the separate PayPal-disputes workflow.

## Key takeaways

- The article divides the credit-card dispute lifecycle into retrieval, chargeback, pre-arbitration, and arbitration. It says Braintree can manage every stage except arbitration. A retrieval is optional and does not remove funds or incur a retrieval-processing fee in this documented context; a chargeback immediately debits the disputed amount and assesses a non-refundable chargeback fee, while pre-arbitration is a further issuer challenge and also carries a non-refundable chargeback fee regardless of outcome.
- Arbitration is outside Braintree's end-to-end dispute support: Braintree does not create an Arbitration dispute, so it is absent from the Control Panel, Disputes APIs, and dispute reports, and merchants cannot submit additional evidence for it. The losing party forfeits the disputed amount and can incur substantial card-network fees passed through to merchants. The article separately says merchants on interchange pricing see arbitration pass-through fees in the Pass-through Fee Report; that interchange-pricing reporting statement must not be applied to flat-rate accounts.
- Dispute notifications can be delivered by email, and webhooks can notify on Open, Won, or Lost status updates for chargebacks, retrievals, and pre-arbitrations. The documented Control Panel procedures are not the only management route: the article expressly states that disputes can also be managed by API.
- Every chargeback, retrieval, and pre-arbitration has a reply-by date. At midnight on that date, using the account time zone established during application, the merchant loses the opportunity to submit evidence; expiration sends an Accept response on the merchant's behalf and removes the ability to dispute the chargeback. The captured article separately says Visa and Mastercard have deprecated the retrieval stage and that US issuers may still create Visa or Mastercard retrievals, but merchants do not need to respond when that happens. This qualification is snapshot article evidence, not independent current card-network policy.
- The snapshot states that, as of August 27, 2025, Braintree auto-accepts pre-arbitrations under USD 1,000 for US flat-rate merchants so arbitration fees are not passed to them; those merchants may represent pre-arbitrations above USD 1,000 and may configure a higher auto-accept threshold in the Control Panel. For pre-arbitrations that are not auto-accepted, the captured article says a merchant should dispute only with additional evidence not previously provided: responses are unlikely to succeed without new and compelling evidence, and a merchant with only the same documentation is generally advised to accept. This is captured article guidance rather than a universal or current card-network rule. The auto-accept policy is a dated, region-, pricing-, and account-qualified statement from the captured Wells Flat page, not proof of current or broader Wells policy.

## Evidence boundaries

> [!warning] Captured account and pricing context
> Keep all lifecycle, fee, reporting, and auto-accept statements scoped to this captured Braintree Wells Flat article. In particular, do not transfer the article's interchange-pricing Pass-through Fee Report statement to flat-rate merchants, or its dated US flat-rate pre-arbitration policy to interchange-pricing, non-US, or other processor/account contexts. Obtain current merchant-specific fees and policy from the applicable agreement or account channel.

> [!warning] Arbitration and response cutoff
> Arbitration is not represented as a Braintree-managed dispute and does not allow additional merchant evidence in the documented flow. Before arbitration, missing the reply-by cutoff results in acceptance on the merchant's behalf and loss of the opportunity to dispute the chargeback.

## Detail locators

- Credit-card rather than PayPal-dispute scope: opening note, lines 17-18.
- Four-stage lifecycle; retrieval meaning and fee effects; Visa/Mastercard retrieval deprecation and US-issuer no-response qualification; chargeback and pre-arbitration meanings and fee effects: `## Dispute Process`, lines 23-44.
- Arbitration's Control Panel/API/report absence, evidence prohibition, financial effect, pricing-qualified reporting, snapshot network-fee figures, and Braintree control boundary: `## Dispute Process`, lines 48-58.
- Email-recipient permissions and webhook notification route: `## Dispute Notifications`, lines 63-84.
- Current and legacy Control Panel procedures: `## Managing in the Control Panel`, lines 87-114.
- Reply-by cutoff, account-time-zone basis, expiration acceptance, and explicit API-management route: `## Managing in the Control Panel`, lines 116-129.
- Chargeback acceptance, evidence response, and snapshot USD 15 fee statements: `## Chargebacks`, lines 134-155.
- Retrieval meaning and response guidance: `## Retrievals`, lines 158-164.
- Pre-arbitration meaning, new-and-compelling-evidence success condition, same-documentation acceptance guidance, non-auto-accepted additional-evidence condition, dated US flat-rate auto-accept policy, configurable threshold, and pricing rationale: `## Pre-arbitrations`, lines 167-200.
- Status definitions: `## Statuses`, lines 203-218.
- Dispute Report and Disputes Financial Impact Report purposes: `## Dispute Reports`, lines 221-238.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]
- Administration route: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/wells-flat/chargebacks-retrievals-prearbs-2026-09-16|Braintree Wells Flat Chargebacks, Retrievals, and Pre-Arbs]] - fully read captured article covering the credit-card dispute lifecycle, notifications, Control Panel and API management, deadlines, fees, dated US flat-rate pre-arbitration policy, statuses, and reports
