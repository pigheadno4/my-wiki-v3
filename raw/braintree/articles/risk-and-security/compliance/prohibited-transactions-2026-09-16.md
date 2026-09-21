<!-- Source URL: https://developer.paypal.com/braintree/articles/risk-and-security/compliance/prohibited-transactions -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Prohibited Transactions
slug: /articles/risk-and-security/compliance/prohibited-transactions/
createTime: '2025-04-01T23:17:55.244Z'
updateTime: '2025-04-01T23:17:55.263Z'
---



# Prohibited Transactions

Governing bodies often have regulations and financial sanctions in place that prohibit transactions with certain restricted or high-risk countries, individuals, corporate entities, and organizations.

Restrictions can also be placed on specific banks that have been linked to any prohibited sources or countries. A credit card may not successfully process if its [Bank Identification Number (BIN)](/braintree/articles/control-panel/transactions/bank-identification-numbers) indicates that it was issued from a high-risk region or bank.

In most cases, the processing bank will decline a prohibited transaction. In the rare instance that the processing bank authorizes the transaction, the funding bank will typically prevent it from settling, and we will let you know.

Restrictions can vary depending on the country where your business is domiciled and who you may be transacting with. Keep in mind that these restrictions are fluid and can change over time as political climates and laws evolve. Be sure to check applicable government sites for your country – such as the [Office of Foreign Assets Control (OFAC) Resources page for the US](https://www.treasury.gov/about/organizational-structure/offices/Pages/Office-of-Foreign-Assets-Control.aspx) – for the most up-to-date information.

