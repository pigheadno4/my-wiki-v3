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



## Point-of-sale risk-rule boundary

The Adyen POS guide fetched 2026-09-15, whose raw metadata says last modified 2022-12-26 and calls the engine RevenueProtect, describes a separate Customer Area switch for POS risk checks. It focuses on MOTO and Manual Key Entry (MKE), not routine in-person payments. At company scope the switch defaults across merchant accounts; a merchant account can override company settings. The guide says the company default profile applies once enabled and recommends a dedicated profile when that merchant account processes only POS, because ecommerce-oriented shared-IP and shopper-reference rules can wrongly decline terminal traffic. It also describes MOTO/MKE as having no liability shift and merchant fraud-chargeback liability. These dated POS claims do not establish current Protect account settings or the liability of other POS entry modes. [[source-adyen-docs-point-of-sale-risk-management-pos]]
## Sources

- [[source-adyen-docs-development-resources-migrating-payment-data-import-data-into-referral-lists]] — 2020-modified bulk referral CSV import guide for encrypted Support upload, sensitive type-specific fields and trust/block/delete flags; import acceptance and effective risk scope remain separate (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-mail-and-telephone-order-moto-avs-responses-pos]] — 2026-09-15 Adyen POS MOTO AVS code mapping for issuer address comparisons, Unknown/partial results, named card/region support and Android/legacy-terminal exclusion


- [[source-adyen-docs-point-of-sale-risk-management-pos]] — 2026-09-15 capture of Adyen's dated POS RevenueProtect guide for MOTO/MKE risk rules, account scope, profile tuning, liability warning, and Terminal API refusal test.


- [[source-adyen-docs-risk-management-chargeback-guidelines-cartes-bancaires-chargebacks]] — Adyen Cartes Bancaires chargeback page for non-defendable reason code 45 and three limited automatic-defense grounds (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-chargeback-guidelines-cash-app-pay-chargebacks]] — Adyen Cash App Pay dispute guide (webpage snapshot, 2026-09-15) for initiation timing, NoC-based defense, liable-account debit, and final accepted-defense reversal.


- [[source-adyen-docs-risk-management-chargeback-guidelines-nyce-chargebacks]] — NYCE NoC-based 30-day defense deadline, provisional reversal, and conditional second-chargeback rules.


- [[source-adyen-docs-risk-management-skip-risk-rules]] — per-transaction, case-sensitive payment-request parameter for skipping risk rules while retaining processing and ShopperDNA attributes (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-chargeback-guidelines-eftpos-chargebacks]] — Adyen eftpos guide to mandatory responses to the first RFI and, if issued, the second RFI, issuer review windows, and an undefendable final chargeback (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-chargeback-guidelines-billdesk-chargebacks]] — Adyen India domestic BillDesk dispute guide for supported card/UPI management, NoC defense, the qualified 60-day outcome, first-chargeback finality, and issuer pre-arbitration (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-chargeback-uploader]] — Adyen guide to CSV import of external-acquirer chargebacks for Protect, with company placement, 1,000-payment CSV limit, irreversible status update, and external dispute ownership (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-chargeback-guidelines-twint-chargebacks]] — 2026-09-15 TWINT dispute guide for 100-day initiation anchors, 10-calendar-day defense, conditional 45-day won path, journals/webhooks, debit outcomes, and its dated no-fee statement.


- [[source-adyen-docs-risk-management-chargeback-guidelines-sepa-chargebacks]] — Adyen SEPA Direct Debit chargeback guide (webpage snapshot, 2026-09-15) for shopper initiation windows, non-defensibility, refund overlap, CHARGEBACK notification, and precautions.


- [[source-adyen-docs-risk-management-control-traffic]] — Adyen control-traffic guide for random risk-evaluation sampling, selection exclusions, premium-rule boundaries, and live Customer Area inspection (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-configure-your-risk-profile-risk-field-reference]] — Protect risk-data quality and example request-field map, distinguishing optional recommended fields from configured-rule needs and the Checkout API delivery-date version split (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-chargeback-guidelines-mexicodomestic-chargebacks]] — Adyen Mexico domestic chargeback guide (webpage snapshot, 2026-09-15) for optional RFI, NoC-based defense, second chargeback, and optional arbitration pursuit.


- [[source-adyen-docs-risk-management-chargeback-guidelines-jcb-chargebacks]] — Adyen JCB dispute guide for optional RFI, first defense, conditional reversal, second chargeback, and arbitration timing (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-chargeback-guidelines-unionpay-chargebacks]] — UnionPay-specific chargeback guide with dated eligibility, optional RFI, NoC defense, pre-arbitration, and finality conditions (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-chargeback-guidelines-american-express-chargebacks]] — 2026-09-15 American Express dispute-stage guide for optional RFI, RFI and NoC defense windows, document finality, debit and reversal events, and exceptional second chargeback; no fee amount stated.


- [[source-adyen-docs-risk-management-configure-your-risk-profile-post-auth-rules]] — built-in post-authorization AVS, CVC, and liability-shift risk-rule guide, with default-disabled state, Block/Allow paths, recurring limits, and decline warning (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-shopper-dna]] — premium, role-gated Shopper DNA transaction-network visualization and phased strong-identifier rollout, with PII masking qualifications (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-run-ab-test-experiments]] — Adyen Protect guide for premium risk-profile A/B experiments on live merchant-account traffic, including split, stop, exclusion, and reporting limits (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-chargeback-guidelines-diners-discover-chargebacks]] — Adyen Diners/Discover dispute guide (webpage snapshot, 2026-09-15) for optional RFI, chargeback defense, conditional reversal, pre-arbitration, and arbitration filing.


- [[source-adyen-docs-risk-management-chargeback-guidelines-mastercard-chargebacks]] — Adyen Mastercard chargeback guide with defense timing, reason-code arbitration exceptions, conditional pre-arbitration, and finality and fee limits (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-automate-submitting-referrals]] — 2026-09-15 Adyen Referrals API guide for company-account block/trust list scope, actions and setup, input limits, skip/failure behavior, and test-endpoint payload examples.


- [[source-adyen-docs-risk-management-chargeback-guidelines-afterpay-chargebacks]] — region-qualified Afterpay/Cash App Afterpay/Clearpay dispute guide for the dated NoC transition, 13-day defense and 30-day decision windows, final routes, conditional fraud liability, and fees (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-chargeback-guidelines-elo-chargebacks]] — Adyen Elo chargeback guide with optional RFI, merchant defense, Adyen-handled pre-arbitration, and Elo arbitration terms (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-understanding-disputes-dispute-timeframes]] — 2026-09-15 Adyen webpage snapshot of scheme- and payment-method-specific dispute, RFI, chargeback-defense, pre-arbitration, and final-decision windows with Visa, Klarna, and other footnoted exceptions.


- [[source-adyen-docs-risk-management-chargeback-guidelines-accel-star-chargebacks]] — Adyen Accel/STAR fraud and non-fraud chargeback guide with reason-dependent windows, NoC-based defense timing, and distinct reversal/finality paths (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-chargeback-guidelines-pulse-chargebacks]] — Adyen PULSE chargeback guide (webpage snapshot, 2026-09-15) covering the default and fraud reason code 4868 flows, defense timing, qualified reversals, and route-specific finality.


- [[source-adyen-docs-risk-management-automate-submitting-referrals-referrals-api-reference]] — test-platform Referrals API schema for company-scoped block/trust/delete uploads, conditional address and PSP-reference payloads, and rate limits (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-chargeback-guidelines-riverty-chargebacks]] — Riverty-specific dispute guide for the 14-day first RFI, optional five-day second-RFI appeal, fraud-notice cutoff, final chargeback and conditional fees (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-configure-your-risk-profile-machine-learning-rules]] — Adyen Protect guide to basic/premium bot and fraud machine-learning rules, pre-authorization thresholds, Allow-rule effect, and signal inspection (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-manage-disputes]] — Adyen Customer Area guide to accepting and defending chargebacks, conditional auto-defense, and approval-qualified pre-arbitration (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-configure-your-risk-profile-risk-lists]] — Adyen risk-lists guide for default and premium custom lists, company or merchant scope, supported payment-method settings, and editing routes (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-configure-your-risk-profile-custom-rules]] — Protect premium custom-rule guide for pre/post-authorization actions, condition building, qualified Dynamic 3DS triggers, pre-authorization backtesting, and profile copy (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-chargeback-guidelines-klarna-chargebacks]] — Klarna-specific dispute guide with conditional physical-goods protection, RFI defense and final chargeback route, plus announced November 2026 workflow and deadline changes (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-fraud-data-collection]] — Adyen Web fraud-data collection guide (webpage snapshot, 2026-09-15) distinguishing automatic checkout collection from API-only SDK handoff, Protect-independent defaults, privacy duties, and collected-data categories.


- [[source-adyen-docs-risk-management-chargeback-guidelines]] — Adyen chargeback-guidelines directory linking to scheme- and payment-method-specific guides (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-understanding-disputes]] — Adyen dispute-definition and navigation page for issuer-raised chargebacks, method-dependent disputability, optional notices, and linked defense/timeframe guidance (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-configure-your-risk-profile]] — Protect risk-profile configuration guide covering basic/premium rule availability, rule timing and priority, and result/analytics routes (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-create-a-risk-profile]] — Adyen Protect guide to creating company-account risk profiles, assigning merchant defaults, and overriding a payment by profile reference (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-risk-management-configure-risk-settings]] — Adyen Customer Area risk-settings guide (webpage snapshot, 2026-09-15) for company and merchant overrides, basic/premium controls, company-wide Protect disablement, and live-only region migration.


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
