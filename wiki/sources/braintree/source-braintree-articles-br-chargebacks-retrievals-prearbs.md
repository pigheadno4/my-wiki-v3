---
title: "Braintree BR Chargebacks, Retrievals, and Pre-Arbs"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/br/chargebacks-retrievals-prearbs"
raw_files:
  - "braintree/articles/br/chargebacks-retrievals-prearbs-2026-09-16.md"
tags: [braintree, brazil, disputes, chargebacks, retrievals, pre-arbitration]
---

## Overview

This captured [[braintree]] BR/Brazil-routed webpage explains notification, management, deadline, financial-effect, status, and reporting behavior for credit-card chargebacks, retrievals, and pre-arbitrations. It expressly routes PayPal disputes elsewhere. Treat it as a 2026-09-16 account-facing snapshot for [[disputes]], not as independent current bank or card-network policy, a merchant-specific agreement, proof of successful execution or fund arrival, or authority for another Braintree account, processor, region, pricing model, or currency.

## Key takeaways

- The first gateway admin receives dispute notifications by default. Control Panel settings can change frequency and recipients: User Recipients are constrained by their roles and associated sub-merchants, while an address entered directly receives all dispute notifications. The page also routes Open, Won, and Lost updates to webhooks, but the linked webhook guide was not used as behavioral evidence.
- The page presents both a rolling Control Panel interface and a legacy procedure, so the visible action labels depend on which interface the account has received. It separately states that disputes can be managed through the API; linked API and response-reference pages remain navigation only here.
- Every chargeback, retrieval, or pre-arb has a reply-by date. At 12am on that date in the account time zone established during application, the opportunity to submit evidence ends. Expiration sends an Accept response on the merchant's behalf and removes the documented ability to dispute the chargeback, while reporting remains Expired.
- A chargeback starts when a cardholder disputes a transaction with their bank. The article says no funds are debited and no fee is assessed when the chargeback opens; acceptance or a loss later results in the disputed amount and a chargeback fee being debited from the merchant's bank account. If the merchant contests in the Control Panel, Braintree includes pertinent original-transaction information it has, and the bank decides the result. The page says a loss debit can occur up to 120 days after representment and rarely later; this is captured timing language, not proof of execution or arrival.
- A retrieval is an information request for an unidentifiable charge and is described as non-financial, with no bank-account debit or processing fee. The article recommends providing identifying transaction information; for suspected fraud it advises that a refund may help avoid a later chargeback fee. These are recommendations, not guaranteed outcomes.
- A pre-arb is a second cardholder dispute after the merchant won the chargeback. The article says merchants rarely win without new and compelling evidence, routes them to review the original evidence PDF, and generally recommends acceptance when no additional evidence exists. Acceptance returns funds to the cardholder and, after the bank completes its process, results in a Lost status plus debit of the disputed amount and chargeback fee; the bank-dependent completion statement is not arrival proof.
- The Disputes Report records status events and can contain multiple lines for one case. The Disputes Financial Impact Report records disbursement events for reconciliation. For installment transactions, one dispute creates an adjustment for each installment with projected disbursement dates. Although the chargeback section generally says opening a case causes no debit, the reporting section expressly says rare cases are debited at Open and use Disbursement Date fields for the debit and any later Won credit.

## Evidence boundaries

> [!warning] Consequential reply-by cutoff
> The captured page says the evidence opportunity ends at 12am on the reply-by date in the account time zone; expiration sends an Accept response on the merchant's behalf and forfeits the documented right to dispute the chargeback. Confirm the live account deadline and current official guidance before acting.

> [!warning] BR snapshot, pricing, and financial-effect scope
> Keep the debit, fee, timing, status, interface, installment, and report statements scoped to this BR/Brazil-routed snapshot and the applicable account. The page names no numerical fee or currency amount and does not establish a transferable price schedule. Its bank-account and Disbursement Date statements do not prove a particular execution, settlement instruction, or actual fund arrival, and the rare debit-at-Open case qualifies the general no-debit-at-opening description.

## Detail locators

- Credit-card scope and separate PayPal-dispute route: opening `NOTE`, raw lines 17-18.
- Notification defaults, role/sub-merchant limits, direct-address behavior, merchant-account recommendation, and Open/Won/Lost webhook route: `## Notifications`, raw lines 25-46.
- Rolling versus legacy Control Panel procedures, account-time-zone reply-by cutoff, automatic Accept/Expired consequences, reason-based guidance, and API-management navigation: `## Managing in the Control Panel`, raw lines 49-85.
- Chargeback definition, general no-debit-at-open behavior, acceptance and evidence routes, later debit and fee effects, automatically included Control Panel evidence, bank decision, and up-to-120-day loss timing: `## Chargebacks`, raw lines 90-111.
- Retrieval definition, no-debit/no-fee distinction, identifying-information recommendation, and fraud-related refund guidance: `## Retrievals`, raw lines 114-120.
- Pre-arb definition, original-evidence review, additional-evidence qualification, acceptance guidance, bank-dependent completion, and resulting debit and fee: `## Pre-arbs`, raw lines 123-129.
- Status meanings and Chargeback Protection / Effortless Chargeback Protection qualification: `## Statuses`, raw lines 132-147.
- Report permission and purposes, status-event versus disbursement-event treatment, installment adjustments and projected dates, plus rare debit-at-Open handling: `## Dispute Reports`, raw lines 150-175.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]
- Administration route: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/br/chargebacks-retrievals-prearbs-2026-09-16|Braintree BR Chargebacks, Retrievals, and Pre-Arbs]] - fully read 2026-09-16 snapshot covering credit-card dispute notifications, interface-qualified management routes, deadlines, chargeback/retrieval/pre-arb effects, statuses, and reports
