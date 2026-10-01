---
title: "Braintree Recurring Billing Trial Periods"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/recurring-billing/trial-periods"
raw_files:
  - "braintree/articles/guides/recurring-billing/trial-periods-2026-09-16.md"
tags: [braintree, recurring-billing, subscriptions, trial-periods]
---

## Overview

This Braintree article explains how a recurring-billing trial period delays a subscription's first billing date, either for an individual subscription or through a plan for new subscriptions. It preserves the payment-method, billing-duration, automatic-charge and customer-notice consequences needed to evaluate this option while leaving implementation details to dedicated guides and references.

## Key takeaways

- A trial period delays the interval between a subscription's start date and first billing date. It can be applied case by case or associated with a plan so that it applies automatically to new subscriptions.
- Trial duration does not count as a billing cycle. The article's example says a three-month trial on a twelve-month plan produces a fifteen-month total subscription duration.
- A customer must provide a payment method when the subscription starts even when the first billing cycle follows a trial. The article says the customer is charged automatically the day after the trial ends.
- Customers are not alerted by default when they enter the first billing cycle. The article tells merchants to notify customers that the trial is ending and that a charge is coming.

## Consequential warning

> [!warning] Notice, opt-out and chargeback risk
> The article calls charging without prior customer notice or an opt-out option negative option billing, says it increases chargeback risk, and states that the practice is generally prohibited among banking partners. It strongly recommends notifying customers of the first billing date toward the end of the trial period; this collected page does not establish that Braintree sends such notice automatically.

## Detail locators

- Trial-period purpose and case-by-case versus plan association: `# Trial Periods`, line 22.
- Trial duration excluded from billing cycles and the three-plus-twelve-month example: `# Trial Periods`, line 24.
- Payment method at subscription start, automatic charge timing and lack of default first-cycle alert: `## Risks and requirements`, line 29.
- Negative-option billing definition and chargeback risk: `## Risks and requirements`, line 31.
- Banking-partner prohibition warning and recommended first-billing-date notice: `## Risks and requirements`, line 33.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-recurring-billing]]
- Cross-provider context: [[recurring-payments]]

## Raw Sources

- [[raw/braintree/articles/guides/recurring-billing/trial-periods-2026-09-16|Braintree Trial Periods article]] - complete collected article covering trial timing, billing-cycle treatment, payment-method requirements, automatic charging and customer-notice risk
