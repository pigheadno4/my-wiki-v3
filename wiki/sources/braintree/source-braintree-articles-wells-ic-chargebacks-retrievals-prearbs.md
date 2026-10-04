---
title: "Braintree Wells IC Chargebacks, Retrievals, and Pre-Arbs"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-ic/chargebacks-retrievals-prearbs"
raw_files:
  - "braintree/articles/wells-ic/chargebacks-retrievals-prearbs-2026-09-16.md"
tags: [braintree, wells-ic, disputes, chargebacks, retrievals, pre-arbitration]
---

## Overview

This collected [[braintree]] Wells IC webpage explains credit-card retrieval, chargeback, pre-arbitration, and arbitration handling, notification and response routes, statuses, and reporting. It explicitly redirects PayPal disputes elsewhere. Treat it as captured Braintree Wells IC evidence for [[disputes]], not as current independent issuer or card-network policy and not as pricing or behavior for Wells Flat or another processor/account arrangement.

## Key takeaways

- The page presents a four-stage lifecycle: retrieval, chargeback, pre-arbitration, and arbitration. It says Braintree can manage all except arbitration; arbitration does not produce a Braintree dispute record, is absent from the Control Panel, Disputes APIs, and Disputes reports, and does not allow additional evidence through those routes.
- Retrieval is described as optional, without removal of funds or a retrieval-processing fee. The page says Visa and Mastercard deprecated the stage, while qualifying US issuers can still create retrievals for those networks and merchants do not need to respond in that stated case.
- A chargeback immediately debits the disputed amount pending resolution and carries a non-refundable fee. The collected article states a $15 chargeback fee whether the merchant accepts or contests it, and a $15 pre-arb processing fee regardless of outcome; these are Wells IC/account-scoped snapshot figures and must not be transferred to Wells Flat or other pricing.
- Every chargeback, retrieval, or pre-arb has a Control Panel reply-by date. The page says the evidence opportunity ends at 12am on that date under the account time zone established during application; expiry sends an Accept response, ends the ability to dispute the chargeback, and retains an Expired reporting status.
- The notification audience is account-sensitive: user recipients are filtered by role and associated sub-merchants, while an address entered directly receives all dispute notifications. Webhooks can cover status updates to Open, Won, or Lost.
- Arbitration outcomes and fees are controlled by card networks rather than Braintree. The page routes lost disputed amounts through daily disbursement and the Disputes Financial Impact Report, and says interchange-pricing merchants see applicable pass-through arbitration and network fees in the Pass-through Fee Report.

## Detail locators

- **`Dispute Process`** (raw lines 23-58): lifecycle definitions; retrieval deprecation and US-issuer qualification; arbitration support, evidence, reporting, financial impact, interchange-pricing, and network-fee warnings.
- **`Dispute Notifications`** (raw lines 63-84): default admin recipient, role/sub-merchant filtering, direct-address behavior, merchant-account coverage, and webhook route.
- **`Managing in the Control Panel`** (raw lines 87-129): interface paths, actions, reply-by cutoff, account time zone, expiry behavior, reason route, and API navigation.
- **`Chargebacks`** (raw lines 134-155): debit and resolution model, acceptance versus evidence response, stated $15 fee, automatically included transaction evidence, and evidence-advice route.
- **`Retrievals`** (raw lines 158-164): no-debit/no-fee definition and qualified information or refund guidance.
- **`Pre-arbs`** (raw lines 167-173): second dispute after a merchant win, original-evidence review, additional-evidence qualification, and stated $15 fee.
- **`Statuses`** (raw lines 176-191): Open, Accepted, Auto Accepted, Disputed, Won, Lost, and Expired meanings, including protection-tool qualifications.
- **`Dispute Reports`** (raw lines 194-209): permission prerequisite, status-history report, and disbursement-impact reconciliation report.

## Related

- [[braintree]]
- [[disputes]]

## Raw Sources

- [[raw/braintree/articles/wells-ic/chargebacks-retrievals-prearbs-2026-09-16|Braintree Wells IC — Chargebacks, Retrievals, and Pre-Arbs (2026-09-16 snapshot)]]
