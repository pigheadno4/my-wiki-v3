<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/network-tokens/how-it-works -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: How Network Tokens Work
slug: /docs/guides/network-tokens/how-it-works/
createTime: '2025-04-01T21:49:25.943Z'
updateTime: '2026-07-22T09:50:06.493Z'
---



# How Network Tokens Work

![Swimlane,diagram,of,the,network,token,process,across,four,lanes:,merchant,,Braintree,,card,network,,and,issuer.,The,diagram,shows,three,phases.,The,first,phase,is,provisioning,a,token.,The,merchant,vaults,a,card,with,Braintree,,Braintree,sends,the,PAN,to,the,card,network,,the,network,requests,and,receives,issuer,approval,,then,returns,the,token,to,Braintree.,The,second,phase,is,processing,a,payment.,The,merchant,sends,a,payment,request,to,Braintree,,which,sends,the,token,and,a,single-use,cryptogram,to,the,card,network,for,PAN,exchange.,The,third,phase,is,lifecycle,management,updates.,The,issuer,sends,updated,card,details,to,the,card,network,,which,notifies,Braintree,to,update,the,token.](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/network-tokens-how-it-works.png)To create a network token, Braintree, acting as a Token Service Provider and Acquirer, sends a card (the PAN) from a merchant's Braintree vault to a card network such as Visa or Mastercard. The card network provisions a network token and sends it back to Braintree, which stores it in the merchant's vault. The card network ties each network token to a specific card and merchant, so no other merchant can use it.

After the card network provisions a network token, Braintree can use it to process a transaction. When a customer goes to checkout, Braintree sends the token from a merchant's vault along with a one-time-use cryptogram to the card network. The network exchanges the token for a PAN and sends it to the issuer to process the transaction.

Unlike a traditional PAN, a network token can receive Lifecycle Management (LCM) Updates. These updates occur whenever a card is reissued, stolen, or lost. Traditionally, whenever the issuer updated a card number, the burden was on the cardholder to update their card details before using the card. With network tokens, the card network passes any update from a card issuer through to Braintree, which updates the card details in the merchant's Braintree vault. Now, when a cardholder goes to checkout, the updated card and token are ready to use and can help avoid a failed transaction which may lead to churn or cart abandonment.

Card networks that issue network tokens have their own set of eligibility criteria when they receive a request for card tokenization. Card networks will sometimes run a $0 verification before issuing a network token to ensure the card is active and not fraudulent, similar to the regular verifications card networks run when Braintree vaults a card. These $0 verifications may show up in the cardholder's credit card statement but are not monetary charges and do not affect merchant operations in any way. When Braintree sends a card to a card network for tokenization, it has no control over whether or not the card network runs a $0 verification on the card as part of tokenization.

[Next Page: Getting Started](/braintree/docs/guides/network-tokens/getting-started)