<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/pinless-debit/optimized-debit-routing/transaction-workflow -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Transaction Workflow
slug: /docs/guides/pinless-debit/optimized-debit-routing/transaction-workflow/
createTime: '2025-04-01T23:13:22.974Z'
updateTime: '2025-04-01T23:13:22.996Z'
---



## Transaction workflow

We check if a transaction is eligible for PINless debit. If ineligible, it will go through Visa or Mastercard.

![How,it,works](https://www.paypalobjects.com/ppdevdocs/optimized-debit-routing.png)
### Refund experience

Refunds for sale transactions will be sent on the same pinless debit network used for the original sale transaction. If unsuccessful, Braintree will automatically retry the refund through Visa/Mastercard for a better merchant experience.

