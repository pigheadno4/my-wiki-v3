<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/pinless-debit/optimized-debit-routing/managing-authorization -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Managing Authorizations
slug: /docs/guides/pinless-debit/optimized-debit-routing/managing-authorization/
createTime: '2025-04-01T21:48:14.361Z'
updateTime: '2025-05-09T11:08:44.493Z'
---



## Managing authorization

Following are some options and limitations to know when managing your authorization workflow for transactions routed to debit networks.


#### Authorization honor period

The authorization expiration period for transactions routed through debit networks differs from that of Visa and Mastercard networks. See following:

| Network | Time before expiration |
| --- | --- |
| STAR | 10 days |
| ACCEL | 7 days |
| MAESTRO | 7 days |
| NYCE | 7 days |
| PULSE | 7 days |
| Visa | 7 days |
| Mastercard | 30 days |


#### Authorization adjustments without settlement

For some business models, there is a need to adjust an authorization for either more or less than the amount it was originally authorized for (such as incremental charges). This action is commonly referred to as an authorization or auth adjustment.


- For authorization over debit networks, you cannot adjust the authorization for an amount greater or less than the original amount authorized unless your industry, card bin, and debit network supports this authorization adjustment. Reach out to your technical account manager for more details.



| Network | Eligible | MCCs Supported | Amount Limit |
| --- | --- | --- | --- |
| STAR | Yes | All MCCs | No limit |
| PULSE | Yes | 4121, 7512, 7011, 5411 | No limit |
| ACCEL | Yes | 4121, 5411 | No limit |
| NYCE | Yes | All MCCs | No limit |
| MAESTRO | Yes | All MCCs | No limit |




#### Authorization adjustments during settlement

For some business models, there is a need to submit a transaction for settlement for either more or less than the amount it was originally authorized for (for example, tip adjustments).


- The amount submitted for settlement must be greater than 0. You can't settle more than the authorized amount unless your industry and debit network supports settlement adjustment (settling a certain percentage over the authorized amount). If you settle an amount less than authorized, the transaction object will return the amount settled. Reach out to your technical account manager for more details.



| Network | Eligible | MCCs Supported | Amount Limit |
| --- | --- | --- | --- |
| STAR | Yes | 4214, 4121, 5411, 5812, 5921, 7999 | 120% |
| PULSE | Yes | 5411, 4121 | 115% |
| ACCEL | Yes | All MCCs | 120% |
| NYCE | Yes | All MCCs | 120% |
| MAESTRO | Yes | 5812, 5814 | 130% |



For details on managing authorizations over Visa and Mastercard networks, see [here](https://developer.paypal.com/braintree/articles/control-panel/transactions/managing-authorizations)

