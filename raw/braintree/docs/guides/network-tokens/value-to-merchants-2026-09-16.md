<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/network-tokens/value-to-merchants -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Value to Merchants
slug: /docs/guides/network-tokens/value-to-merchants/
createTime: '2025-04-02T00:47:19.736Z'
updateTime: '2025-04-02T00:47:19.754Z'
---



# Value to Merchants


- Drive Authorization Rate Performance: Network Tokens receive lifecycle management event updates if card details change, such as when a card nears its expiry date, is lost or stolen, or is reissued). Network Tokens also provide additional information to issuers and are authenticated using details specific to each merchant, helping increase an issuer's confidence and the probability a transaction is approved.
- Drive Checkout Conversion: Network Tokens keep card details up to date in real-time, helping reduce the possibility of declines due to incorrect or out-of-date information, thus reducing the friction for customers at checkout and possibility of cart abandonment.
- Reduce Transaction Expense: Merchants who use Network Tokens may see reduced interchange fees as some card networks may charge a higher rate for non-token transactions.
- Improve Security and Reduce Fraud: Network token transactions use a one-time use cryptogram that can only be decrypted by the issuer, helping secure the transaction. Network tokens are unique to every customer card and are not shared between any two merchants, helping to reduce the effectiveness of stolen cards. Tokens are given by a token service provider (such as Braintree) and restricted to a single token requestor.
- Automatic Token Management: Braintree seamlessly manages Network Tokens for merchants, from provisioning tokens with the card networks to updating them in the vault for lifecycle management events to using them at checkout.



[Next Page: How it Works →](/braintree/docs/guides/network-tokens/how-it-works)