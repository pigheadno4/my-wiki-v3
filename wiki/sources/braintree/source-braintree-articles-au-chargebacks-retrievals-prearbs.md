---
title: "Braintree AU Chargebacks, Retrievals, and Pre-Arbs"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/au/chargebacks-retrievals-prearbs"
raw_files:
  - "braintree/articles/au/chargebacks-retrievals-prearbs-2026-09-16.md"
tags: [braintree, australia, disputes, chargebacks, retrievals, pre-arbitration]
---

## Overview

This captured [[braintree]] AU webpage explains notifications, management routes, deadlines, financial effects, statuses, and reporting for credit-card chargebacks, retrievals, and pre-arbitrations. It expressly routes PayPal disputes elsewhere. Treat it as a 2026-09-16 Braintree-hosted snapshot for [[disputes]], not as independent current bank or card-network policy, proof of merchant eligibility or execution, or a pricing promise beyond the article's stated AU context.

## Key takeaways

- The page documents email notifications, configurable recipients, and webhook notifications when a chargeback, retrieval, or pre-arb becomes Open, Won, or Lost. User recipients are constrained by their role and associated sub-merchants; an address entered directly receives all dispute notifications even when it corresponds to a limited-permission user.
- A chargeback begins when a cardholder disputes a transaction with their bank. The article says the transaction amount is immediately debited from the merchant's bank account and held pending resolution. The merchant may accept or submit evidence; if the bank rules for the merchant, the amount returns, while acceptance or loss leaves the funds with the cardholder. The captured page states a $25 AUD chargeback fee for acceptance and loss.
- Every listed dispute type has a Control Panel reply-by date. At 12am on that date, in the account time zone established during application, the opportunity to submit evidence ends. Expiration sends an Accept response on the merchant's behalf and removes the ability to dispute the chargeback, while the case remains Expired in reporting. The page documents a rolling Control Panel interface, a legacy interface, and a separate API-management route.
- A retrieval is an information request for an unidentifiable charge. Unlike chargebacks and pre-arbs, the article says it does not remove funds from the merchant's bank account and does not incur a processing fee. It recommends providing identifying transaction information, while noting that fraud-related retrievals often become chargebacks despite evidence and may warrant a refund; this is captured guidance, not a guaranteed outcome.
- A pre-arb is a second cardholder challenge after the merchant wins a chargeback. The article says merchants rarely win without new and compelling evidence, routes them to review the original-evidence PDF, and generally recommends acceptance when no additional evidence exists. It states a $25 AUD fee when a pre-arb is accepted. The Dispute Report shows status-history lines and is expressly not for reconciliation; the Disputes Financial Impact Report is intended to be used with the statement for reconciliation.

## Evidence boundaries

> [!warning] Captured AU account context
> Keep the deadline, debit, outcome, fee, evidence, and response statements scoped to this captured AU article. It is not independent current bank or card-network authority, does not establish a merchant-specific agreement, and does not prove that another region, processor, account type, or pricing arrangement uses the stated $25 AUD fees.

> [!warning] Consequential reply-by cutoff
> Missing the account-time-zone reply-by cutoff causes an Accept response to be sent on the merchant's behalf and ends the documented opportunity to dispute the chargeback. Linked support, API, webhook, reason-code, role, and card-verification pages are navigation only unless independently read.

## Detail locators

- Credit-card rather than PayPal-dispute scope: opening note, raw lines 17-18.
- Email defaults, recipient permission behavior, merchant-account coverage guidance, and the Open/Won/Lost webhook route: `## Notifications`, raw lines 25-46.
- Rolling and legacy Control Panel procedures, reply-by cutoff, account-time-zone basis, expiration effect, reason-code guidance, and the stated API route: `## Managing in the Control Panel`, raw lines 49-85.
- Chargeback definition, immediate bank-account debit, acceptance and evidence routes, $25 AUD acceptance/loss fees, and automatically included Control Panel evidence: `## Chargebacks`, raw lines 90-111.
- Retrieval definition, no-debit/no-fee distinction, identifying-information recommendation, and fraud-related refund guidance: `## Retrievals`, raw lines 114-120.
- Pre-arb definition, original-evidence review, new-evidence qualification, acceptance guidance, and the stated $25 AUD acceptance fee: `## Pre-arbs`, raw lines 123-129.
- Status definitions, including the qualified 2-3-business-day Won wording and reply-by forfeiture: `## Statuses`, raw lines 132-141.
- Report permission, status-history purpose, express non-reconciliation boundary, and financial-impact reconciliation fields: `## Dispute Reports`, raw lines 144-161.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]
- Administration route: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/au/chargebacks-retrievals-prearbs-2026-09-16|Braintree AU Chargebacks, Retrievals, and Pre-Arbs]] - fully read 2026-09-16 snapshot covering credit-card dispute notifications, management routes, deadlines, chargeback/retrieval/pre-arb effects, AU-denominated fees, statuses, and reporting
