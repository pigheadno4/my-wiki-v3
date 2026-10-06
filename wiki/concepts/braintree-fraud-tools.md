---
title: "Braintree Fraud Tools"
type: concept
category: technology
tags: [braintree, fraud-tools, risk-management, carding, velocity-checks]
---

## Braintree Fraud Tools

Braintree's collected risk-threshold guide documents one basic fraud-control mechanism: risk threshold rules, also called velocity checks, detect and help prevent carding attacks by reacting when specified customer information passes through the gateway repeatedly within a designated period. Their documented actions are email notification or automatic rejection of the triggering verifications or transactions. The page limits these rules to credit-card and certain Google Pay transactions. [[source-braintree-fraud-tools-basic-risk-threshold-rules]]

## Risk threshold rules

A custom rule is created under **Fraud Management** > **Risk Thresholds** in the Control Panel and has five criteria: Action, Threshold, Operation, Field, and Window. This page describes repeated-value counters and time windows rather than a numeric risk score. Many listed Fields are not otherwise required by the gateway, so submitted transactions must include every Field on which their configured rules rely. The only documented override is temporarily disabling the rules in the Control Panel, which the guide says is typically not recommended. [[source-braintree-fraud-tools-basic-risk-threshold-rules]]

## AVS and CVV rules

Braintree's collected AVS/CVV guide documents a separate Basic Fraud Tools mechanism limited to credit cards: issuing banks return numeric address and CVV match results after an approval response, and merchant-configured rules can then cause Braintree to gateway-reject a transaction or verification and send a void request. A bank may not recognize the void immediately. These checks and rule outcomes therefore must remain distinct from processor authorization. [[source-braintree-fraud-tools-basic-avs-cvv-rules]]

Rules are configured under **Fraud Management** in the Control Panel and can apply to all transactions or selected card types, amounts, or merchant accounts. By default they apply only to first-time transactions, not recurring or vaulted-card transactions; card verification must be enabled to check a card before vaulting, and CVV must be recollected because Braintree says it does not store CVVs. Default AVS country scope and the documented Global AVS false-rejection warning remain material setup boundaries. [[source-braintree-fraud-tools-basic-avs-cvv-rules]]

## Scope boundary

These collected sources establish only the documented risk-threshold and credit-card AVS/CVV mechanisms and their own availability, configuration and gateway-decision boundaries. They do not establish 3D Secure authentication, premium fraud-product behavior, chargeback protection, per-transaction liability shift, settlement, funding or current support beyond the collected snapshots; AVS/CVV match checks and rule outcomes do not replace processor authorization.

## Sources
- [[source-braintree-articles-guides-fraud-tools-basic-overview]] - 2026-09-16 Basic Fraud Tools orientation for customizable Control Panel rules, snapshot-scoped no-extra-cost/all-merchant/no-developer-setup labels, AVS/CVV versus risk-threshold payment-method scope, and an umbrella override route whose exact mechanisms remain tool-specific
- [[source-braintree-articles-guides-fraud-tools-overview]] - 2026-09-16 umbrella comparison of Basic and Premium fraud-tool tiers, snapshot-scoped availability and fee labels, account enablement and rule routing, and Control Panel lookup of fraud-related `Gateway Rejected` requests; its broad pre-processor wording does not override the dedicated AVS/CVV post-authorization and void flow, and its all-merchants label for Fraud Protection Advanced conflicts with the same-date dedicated product guide's eligible-Braintree-Direct-and-latest-SDK condition, so neither source proves current merchant eligibility or enablement
- [[source-braintree-articles-risk-and-security-risk-factors-identifying-fraud]] - manual merchant investigation checklist for customer, address, email, IP and transaction-pattern indicators, with an explicit guidance-not-proof boundary and conditional contact, fulfillment and void/refund next steps
- [[source-braintree-premium-fraud-management-tools-configuration]] - umbrella PFMT configuration checklist coordinating Control Panel enablement, client-side collection and server-side submission, with a sandbox-first warning; not named-product eligibility, bypass/exemption, liability or conflict-resolution evidence
- [[source-braintree-premium-fraud-management-tools-server-side-node]] - captured Node.js server-side half of the umbrella Premium Fraud Management Tools integration: receives client-collected device data, attaches it to customer, payment-method, verification or transaction requests, and routes page-qualified skipping, Advanced custom-field prerequisites and product-qualified risk responses; named-product behavior remains separate
- [[source-braintree-premium-fraud-management-tools-overview]] - 2026-09-16 umbrella developer-guide snapshot for pre-processing fraud-check purpose, tool-sensitive transaction-data applicability, qualified Chargeback Protection evidence automation and payment-method compatibility routing; not evidence that named fraud products are interchangeable
- [[source-braintree-premium-fraud-management-tools-client-side-android-v5]] - Android v5 device-data collection, merchant-server handoff, location-consent and disclosure responsibilities, and a dated mobile-certificate lifecycle warning; an umbrella Premium Fraud Management Tools integration route, not named-product behavior
- [[source-braintree-premium-fraud-management-tools-client-side-ios-v7]] - iOS v7 client device-data collection and merchant-server handoff, with automatic-vault verification, PayPal Vault and historical certificate qualifications; an umbrella Premium Fraud Management Tools integration route, not named-product behavior
- [[source-braintree-premium-fraud-management-tools-client-side-javascript-v3]] - JavaScript v3 custom and Drop-in device-data collection, merchant-server handoff, conditional FraudNet race callback and automatic-vault verification warning; an umbrella Premium Fraud Management Tools integration route, not named-product behavior
- [[source-braintree-payment-methods-unionpay]] - UnionPay-specific route for certain cards without CVV, rarely collected postal codes and Braintree's stated bypass of CVV and AVS rules for certain UnionPay transactions


- [[source-braintree-fraud-tools-basic-risk-threshold-rules]] - carding-oriented velocity checks, payment-method availability, Control Panel configuration, five rule criteria, supporting-field prerequisite and override boundary
- [[source-braintree-fraud-tools-basic-avs-cvv-rules]] - credit-card AVS/CVV checks, Control Panel rule configuration, post-approval gateway-rejection and void behavior, Vault defaults and international AVS warning
