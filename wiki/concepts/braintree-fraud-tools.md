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

- [[source-braintree-fraud-tools-basic-risk-threshold-rules]] - carding-oriented velocity checks, payment-method availability, Control Panel configuration, five rule criteria, supporting-field prerequisite and override boundary
- [[source-braintree-fraud-tools-basic-avs-cvv-rules]] - credit-card AVS/CVV checks, Control Panel rule configuration, post-approval gateway-rejection and void behavior, Vault defaults and international AVS warning
