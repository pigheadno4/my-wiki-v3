---
title: "Adyen Risk Management"
type: concept
category: technology
tags: [adyen, risk-management, protect, fraud, disputes]
---

## Overview

Protect is Adyen's risk-management engine. Adyen's captured overview says payment risk evaluations can result in a block, allow, or review action, based on account risk settings, a risk profile, and rules on that profile.

## Configuration and scope

The 2026-09-15 documentation snapshot describes Protect as enabled by default, with a default risk profile available when risk management is first configured. Company risk settings and at least one risk profile are needed in either the basic or premium tier. Premium features are enabled in risk settings and extend the basic feature set with machine-learning fraud detection, custom rules and backtesting, experiments, and case management. Adyen recommends high-quality payment-request data and review of its recommended and required integration options; the overview does not itself establish that every example field is mandatory or guarantee a fraud or authorization result.

The risk-management documentation also routes to dispute monitoring and handling through Customer Area or the Disputes API. This page is a documentation snapshot, not proof of a merchant account's premium enablement or a particular payment or dispute outcome.

## Sources

- [[source-adyen-docs-risk-management-handle-risk-rule-notifications]] — Adyen online-payment risk results in API responses and Standard webhooks, including optional formatting and Protect premium limits (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-chargeback-guidelines-visa-chargebacks]] — 2026-09-15 Adyen Visa dispute guide distinguishing Allocation, Collaboration, and RDR, with dated defense windows, fund-return timing, pre-arbitration, and arbitration exposure.


- [[source-adyen-docs-risk-management-chargeback-guidelines-paypal-chargebacks]] — Adyen marketplace guide to PayPal inquiry/claim handling, seller-level responsibility, defense submission, and final chargeback outcomes (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-case-management]] — premium manual-review cases after authorization, with capture-delay, configurable decision effects, role, and irreversible-cancellation qualifications (webpage snapshot, 2026-09-15)


- [[source-adyen-docs-risk-management-avs-checks]] — 2026-09-15 Adyen AVS guide for billing-address checks, post-authorization rules, card/issuer limits, and simulated test versus live response mapping.


- [[source-adyen-docs-risk-management-disputes-api]] — Adyen Defend Disputes API workflow for webhook-triggered retrieval, evidence upload, final defense submission, and approval-qualified pre-arbitration (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-understanding-disputes-dispute-process-and-flow]] — Adyen dispute-stage and monitoring guide, including chargeback debit, defense, conditional pre-arbitration, and `CHARGEBACK_REVERSED` status and finality qualifications (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-disputes-api-dispute-notifications]] — Standard dispute webhook events, reference fields, statuses, and setup; includes Brazil and non-final reversal qualifications (webpage snapshot, 2026-09-15)


- [[source-adyen-docs-risk-management-chargeback-guidelines-ach-chargebacks]] — 2026-09-15 Adyen webpage guide to non-defensible ACH Direct Debit returns, return-stage webhooks, refund overlap, reason-code retry limits, and test fixtures.


- [[source-adyen-docs-risk-management-dispute-and-fraud-monitoring]] — Adyen Risk & dispute analytics dashboard and dated scheme-monitoring program reference, with company-account, RFI, and shopper-data access limits (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-disputes-api-disputes-api-reference]] — Adyen Defend Disputes API reference for request errors and scheme-specific defense reason and document type codes (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management]] — Adyen risk-management overview (webpage snapshot, 2026-09-15) for Protect's risk-decision framing, tiered features, configuration prerequisites, data-quality recommendation, and dispute routes.
