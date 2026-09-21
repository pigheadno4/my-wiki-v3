<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/recurring-billing/trial-periods -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Trial Periods
slug: /articles/guides/recurring-billing/trial-periods/
createTime: '2025-04-01T23:48:14.535Z'
updateTime: '2025-04-01T23:48:14.554Z'
---



# Trial Periods


**IMPORTANT**
 Trial periods have a certain amount of inherent risk. Please review the [risks and requirements](#risks-and-requirements) for trial periods before considering this option.

 

A trial period allows you to delay the time between the start date of a subscription and the first billing date. You can choose to apply trial periods on a [case-by-case basis](/braintree/articles/guides/recurring-billing/subscriptions#creating-a-subscription), or you can [associate them with certain plans](/braintree/articles/guides/recurring-billing/plans#creating-a-plan) to apply them automatically to new subscriptions.

Keep in mind that the duration of the trial period won’t count as a billing cycle for the customer. For instance, if you offer a 3-month trial period on a 12-month plan, the total duration of a customer’s subscription will be 15 months.


## Risks and requirements

Because subscriptions are based on the association of a payment method with a plan, your customers must provide a payment method at the start of any subscription – even those that include a trial period before the first billing cycle. The day after the trial period ends, customers will be charged automatically for the subscription. Customers are not alerted by default when they enter the first billing cycle – you must be proactive to make sure your customers know that the trial period is ending and they will be charged soon.

The failure to alert the customer prior to their charge, or give them the option to opt-out, will result in something referred to as [negative option billing](https://www.braintreepayments.com/blog/negative-option/). Negative option billing puts you at an increased risk of [chargebacks](/braintree/articles/risk-and-security/chargebacks-retrievals/overview), as customers may not be expecting this delayed charge.

Negative option billing is generally prohibited amongst banking partners. We strongly recommend you avoid this practice by notifying customers of the first [billing date](/braintree/articles/guides/recurring-billing/billing-cycles#billing-date) towards the end of their trial period. [Contact us](/braintree/help/RecurringBillingQuestion) for more information.

