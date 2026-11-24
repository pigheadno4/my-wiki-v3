---
title: "Stripe — Fraud Prevention Rules"
type: source
date_ingested: 2026-05-10
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/radar/rules"
raw_files:
  - "stripe-radar-rules-2026-11-07.md"
  - "stripe-radar-rules-2026.md"
tags: [stripe, radar, rules, fraud, block, allow, review, 3ds, cvc, avs, metadata, radar-assistant]
---

## Summary

[[stripe]]'s [[stripe-radar|Radar]] guide covers built-in rules, custom transaction and account rules, 3D Secure (3DS), and the Radar Assistant. The 2026-11-07 capture documents Dashboard custom rules conditional on an eligible Radar plan. The account owner, administrators, and developers can create rules. The 2026-05-10 guide named Radar for Fraud Teams and Radar for Platforms for custom rules.

## Rule Actions

| Action | Documented effect |
| --- | --- |
| Request 3DS | Requests authentication, which the issuer might not perform. Applies to Checkout, Payment Intents, and Setup Intents and is evaluated before Allow, Block, and Review. |
| Allow | Contact Stripe for the ability to create Allow rules. Within the rule's scope, Allow overrides Stripe risk assessment and matching default and custom rules after the Request 3DS evaluation. |
| Block | Prevents processing of payments subject to the block action. |
| Review payment | Stripe processes the payment normally. Only successful payments go to the team's review queue. |
| Review account or pause payouts | Platforms can raise an account review. A payout pause also raises a review. Account rules apply to existing and future accounts on activation. |

Stripe handles issuer soft declines that require 3DS and triggers it when required for regulatory SCA even with Radar disabled. Transaction rules evaluate future transactions. They cover supported payment methods by default, subject to any method specified by `:payment_method_type:` and the applicable rule and plan scope.

## Traffic Allocation

The November capture documents adjustable traffic allocation for eligible custom transaction rules. It can be set during creation or adjusted later for rollout or rollback. The default of 100% enforces the action on every match. A partial percentage limits enforcement to that share of matching payments. At 0% (shadow), Radar evaluates and reports counterfactual outcomes without enforcing the action.

Retries stay in the same allocation bucket. For cards, Radar groups by the same invoice first, then the same customer and amount if there is no invoice, then the same card and amount if there is no customer. For other methods, retries of the same payment share a bucket. The guide documents allocation consistency for retries. Behavior after other predicates or settings change between attempts is unresolved. Account rule activation uses a separate flow.

## Built-in Rules

- **Transaction risk**. The guide describes `if :risk_level: = 'highest'` as a deprecated default block rule. The November risk-controls section describes early fraud warnings and dynamic risk thresholds for blocking the highest-risk payments. The May guide described early fraud warnings there. For `if :risk_level: = 'elevated'`, May named Fraud Teams and Platforms for default review. November describes the default review of suspected elevated-risk payments with no tier specified in that row.
- **Account risk**. The May guide names the Platforms account models and lists `:account_risk_level:` for `highest` and `elevated`. November lists `:account_fraud_risk_level:` for those two predicates. Neither capture assigns those predicates to specific actions. The November [[source-stripe-radar-rules-supported-attributes|supported-attributes reference]] lists `account_fraud_risk_level` for connected-account rules and `account_risk_level` separately for private-preview Treasury transaction rules. Alias and migration behavior are unresolved.
- **CVC and AVS**. From 2024-12-17, the Dashboard shows the risk-score-based CVC and postal-code verification rules to new customers and existing customers who have never used the legacy rules. The legacy options are shown to existing customers who enabled at least one. When enabled, the risk-score-based rules block a failed issuer check unless Stripe assesses the payment as low risk. Both variants exempt absent verification input or unsupported issuer checks. Enabled checks can also affect attaching a card to a customer or creating the card and customer together.
- **Legacy 3DS**. For Payment Intents and Setup Intents, the May capture lists three deprecated card rules (recommended, supported, and required). November lists the deprecated supported-for-card rule. Availability of the other two remains unresolved.

> [!note] Payment-method coverage and plan scope
> The May method section named cards, ACH, and SEPA Direct Debit for most users. November describes default fraud protection across supported methods. The same-day [[source-stripe-radar-supported-payment-methods|supported-methods guide]] scopes the default high-risk controls to Standard and above and says Stripe may still block payments on Lite. Custom features depend on the [[source-stripe-radar-how-it-works#November plan matrices|plan comparison]]. The rules guide's removal of named tiers does not establish wider eligibility.

## Rule Syntax

```
{action} if {attribute} {operator} {value}
```

- Custom metadata: `::field::` or `::customer:field::`
- List membership: `:attribute: in @list_alias`
- Max: **200 transaction rules**, **100 account rules**

## Key 3DS Attributes

| Attribute | Meaning |
| --- | --- |
| `is_3d_secure` | Card supports 3DS, issuer attempted it, and the customer did not fail authentication. The guide generally recommends it for Block rules. |
| `is_3d_secure_authenticated` | The issuer attempted 3DS and the customer completed full authentication. Using it in Block rules can exclude legitimate payments, such as those with SCA exemptions. |
| `has_liability_shift` | Stripe expects liability shift for the payment, which can also apply outside a 3DS flow (for example, Apple Pay in certain regions). |

In the risk-based 3DS Block example, the predicate excludes off-session payments, Apple Pay, and Google Pay (represented as `android_pay`) when Google Pay has a cryptogram. See May lines 122–123 and November lines 118–119 for the amount-based example. In both captures, a separate risk-level and edge-cases example says its Request 3DS and Block predicates apply above a certain amount, although the predicates contain no amount condition (May lines 179–180, November lines 175–176).

## Radar Assistant

The rule editor's LLM assistant drafts a transaction rule from natural language. By using it, users agree that Stripe can log and use their chat entries to train and improve the assistant. Rules can also be written manually.

## Best Practices

- Use Allow rules minimally. The guide recommends excluding the highest-risk matches from Allow.
- Keep Block false positives low and test before enabling. Target Review narrowly to keep the queue manageable.
- Transaction testing simulates the previous six months of charges. Account testing shows the accounts that would match today. Rule activity covers the past 180 days.
- The guide says EU businesses might be affected by the Geo-blocking Regulation and its limits on blocking payments from customers based in EU member states.
- The May metrics section explicitly qualified Allow and Review metrics and additional Block metrics by Fraud Teams. November omits those labels. Both Block metrics sections describe payments **allowed** under Risk score (May lines 374–376, November lines 388–390). The row does not establish a Block risk-score metric definition.

## Related Pages

- [[stripe-radar]] — Radar concept
- [[source-stripe-radar-how-it-works#November plan matrices|Radar plan comparison]]
- [[source-stripe-radar-rules-supported-attributes]] — supported rule attributes
- [[source-stripe-radar-supported-payment-methods]] — default protection, controls and method-specific scope
- [[source-stripe-radar-lists]] — lists used in rules (`@list_alias`)
- [[source-stripe-radar-risk-settings]] — automatic risk controls
- [[source-stripe-radar-rules-reference]] — rule evaluation and syntax reference

## Raw Sources

- [[raw/stripe-radar-rules-2026-11-07|2026-11-07 fraud prevention rules]]
- [[raw/stripe-radar-rules-2026|2026-05-10 fraud prevention rules]] — includes five historical screenshot references
