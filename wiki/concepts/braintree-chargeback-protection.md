---
title: "Braintree Chargeback Protection"
type: concept
category: technology
tags: [braintree, chargeback-protection, fraud-management, disputes, credit-cards, debit-cards]
---

## Braintree Chargeback Protection

Braintree's collected article distinguishes PayPal's **Chargeback Protection tool** from its **Effortless Chargeback Protection tool**. For the former, PayPal makes real-time risk decisions on credit- and debit-card transactions, processes transactions it does not deem fraudulent or high risk, and declines those it considers high risk without manual review or later re-review. Effortless Chargeback Protection separately removes the delivery-confirmation requirement for eligible fraud chargebacks. [[source-braintree-fraud-tools-premium-chargeback-protection]]

## Conditional protection and bypass

For an eligible processed transaction, the page says the disputed amount and PayPal Chargeback fees are waived only if a chargeback is received and the merchant provides required evidence; evidence requirements can vary by the goods or services. The page does not say Effortless removes all evidence requirements or protects every chargeback. It documents `Options.SkipAdvancedFraudChecking` as a bypass for a declined transaction and says the merchant must still pay for the services. The page then uses the wording that the merchant "waives the right to indemnify PayPal" for the chargeback amount and PayPal chargeback fee; this source does not clarify or safely establish the direction of indemnity. [[source-braintree-fraud-tools-premium-chargeback-protection]]

> [!warning] Unresolved bypass conflict
> The collected [[raw/braintree/articles/guides/fraud-tools/premium/chargeback-protection-2026-09-16|Chargeback protection tools article]] (line 40) distinguishes override from bypass: it says a merchant cannot override a declined Chargeback Protection-tool decision but can bypass the decision with `Options.SkipAdvancedFraudChecking`. The separately collected [[raw/braintree/articles/guides/fraud-tools/premium/overview-2026-09-16|Premium Fraud Management Tools overview]] (line 132) says the Chargeback Protection and Effortless Chargeback Protection tools do not support bypassing or skipping fraud checks. These statements conflict. Treat bypass availability as unresolved and do not use either statement as current operational guidance without clarification from Braintree/PayPal.

## Automated evidence-submission route

A collected 2026-09-16 developer-guide snapshot describes an automated route for a Chargeback Protection dispute: receive chargeback-status webhooks, act only on an `Open` chargeback, look up the `dispute_id`, confirm that `chargeback_protection_level` references a Chargeback Protection tool and that the dispute remains `Open`, add eligible text or file evidence, and finalize before the reply-by date. This workflow does not itself establish transaction or chargeback eligibility, remove product-specific evidence conditions, guarantee protection or a dispute result, or resolve the separate collected conflict over bypass support. [[source-braintree-premium-fraud-management-tools-overview]]

## Eligibility boundary

The page says merchants should have a Braintree business account, says Chargeback Protection is available in the US and Brazil, and says Fraud Protection tools cannot be used while a Chargeback Protection tool is enabled. In supported regions it describes both named tools as compatible with debit- and credit-card transactions that Braintree should fund and with Braintree's use of Fiserv, American Express and Wells Fargo. Integration requires mandatory fields from a separate developer guide and may require additional signup data depending on the business's risk profile. These collected statements do not prove eligibility or support for a particular merchant or transaction. [[source-braintree-fraud-tools-premium-chargeback-protection]]

> [!warning] The source refers to an **Eligible Chargeback Types** section that is absent from the collected raw. Do not infer covered chargeback types or generalize the conditional waiver into a chargeback guarantee.

## Sources
- [[source-braintree-premium-fraud-management-tools-server-side-node]] - captured Node.js server-side page with generic `skipAdvancedFraudChecking` wording; it does not resolve the retained conflict over whether Chargeback Protection tools support bypass

- [[source-braintree-fraud-tools-premium-chargeback-protection]] - two named tools, real-time decisioning, conditional waiver and evidence scope, bypass consequence, integration prerequisites and account, region, payment and processor eligibility boundaries
