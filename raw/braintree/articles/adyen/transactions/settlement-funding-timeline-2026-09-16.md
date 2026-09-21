<!-- Source URL: https://developer.paypal.com/braintree/articles/adyen/transactions/settlement-funding-timeline -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Settlement and Funding Timeline
slug: /articles/adyen/transactions/settlement-funding-timeline/
createTime: '2025-04-02T01:49:03.058Z'
updateTime: '2025-04-02T01:49:03.146Z'
---



# Settlement and Funding Timeline

At the end of each day, we will mark any transactions that have been submitted for settlement as Settled and send them to Adyen. Adyen must then verify each transaction with the issuing banks before the funds can be paid out to you. While typically faster, it can take 1-4 weeks for issuing banks to verify transactions.

Once they have verification, Adyen will send the funds for these transactions to you. You should expect to see funds for verified transactions deposited into your bank account within 2-3 business days of payout.

By default, funds are paid out every Tuesday and Friday, excluding bank holidays. On bank holidays, funds will be sent to your bank account the following business day, and it typically takes an additional business day before you see the funds in your account.

Adyen offers a variety of alternative funding schedules. If you’d like to set up an alternative schedule, [contact us](/braintree/help) for your available options.

