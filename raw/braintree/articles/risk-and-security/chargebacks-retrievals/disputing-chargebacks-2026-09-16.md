<!-- Source URL: https://developer.paypal.com/braintree/articles/risk-and-security/chargebacks-retrievals/disputing-chargebacks -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Disputing Chargebacks
slug: /articles/risk-and-security/chargebacks-retrievals/disputing-chargebacks/
createTime: '2025-04-01T23:03:52.005Z'
updateTime: '2025-08-19T11:17:29.839Z'
---



# Disputing Chargebacks

If one of your customers issues a chargeback through their bank, you have the chance to dispute it and win back the funds.

The way you manage chargebacks depends on your account setup. For details on how to receive notifications of chargebacks, accept or dispute them, and submit evidence to support your case, refer to your bank-specific articles. If you're unsure of where to find those, [contact us](/braintree/help).


## When to accept

Merchants typically accept chargebacks if:


- The transaction amount is minor enough that it doesn’t justify the work of submitting evidence
- The transaction is known to be fraudulent
- A refund is warranted and the chargeback can be accepted in lieu of issuing a manual refund

When it comes to fraudulent transactions, accepting a chargeback is particularly common when a merchant receives a chargeback for an American Express transaction; they are strong advocates for their cardmembers, and as a result merchants are usually at a disadvantage when the chargeback is related to fraud.

When you accept a chargeback, the funds will be issued to the cardholder and you will still be charged a [chargeback fee](/braintree/articles/risk-and-security/chargebacks-retrievals/overview#fees). Accepting a chargeback indicates you don’t wish to take any further action, but it doesn’t necessarily imply you agree with the cardholder’s claim.


## When to dispute

Merchants typically dispute chargebacks if:


- They are confident the transaction was legitimate
- They have compelling evidence against the chargeback
- The disputed amount is large enough to justify the work of submitting evidence

Merchants should also dispute a chargeback if they have already [issued a refund for the disputed amount](#refunds).


### Submitting evidence

Every chargeback is different, so the evidence you provide will vary depending on the reason for the chargeback and the documents you have available. We recommend keeping records of all transactions, so you are prepared in the event that a chargeback does happen.

Helpful items may include, but are not limited to:


- Screenshots of any signatures proving payment authorization from the customer
- Email correspondence between you and the customer
- Proof of delivery screenshots
- Your site's terms of service
- Social media screenshots (if the customer has posted pictures, or checked in with your business)
- User’s IP address
- Customer’s username (if applicable)
- Service usage times, dates, etc.

If you have any other meaningful evidence that you believe may prove the legitimacy of a transaction, always include it. The more evidence you can provide, the better.


#### Required evidence

Certain types of chargebacks involving fraud or merchandise/services not received require specific compelling evidence, as defined by the card brands. These chargebacks are identified by their [dispute reason](/braintree/docs/reference/response/dispute#reason), and we'll always let you know when specific compelling evidence is required.

For chargebacks related to fraud or merchandise/services not received, you'll need to provide at least one of the following:


- Documentation to prove the customer is in possession of or using the merchandise
- Proof of a signed delivery form, or copy of customer ID as proof goods were picked up at your business location
- Proof of delivery to the address associated with an AVS matched response
- Proof of delivery and customer proof of employment at the delivery location
- Proof that ticket was received or used
- Proof that the transaction was completed by an authorized signer associated with the cardholder
- Proof of a signed order form for a mail or phone transaction
- Proof of digital goods downloaded from your website or app
- Proof of previously undisputed transaction for the same merchandise or service
- Proof of previously undisputed recurring transaction history

We recommend providing whichever pieces of relevant evidence you feel most confident in. There is not a limit to the amount of evidence you can provide.

If you're unable to provide required evidence, your dispute will not be accepted by the card brand, and you will need to accept the case.


#### Dispute Evidence Recommendations

Currently in beta, our Dispute Evidence Recommendations offering uses numerous machine learning models to guide you in deciding which kinds of evidence will likely help you win a given dispute. For chargebacks that do not have specific compelling evidence requirements, the models will provide an ordered list of the top kinds of evidence to submit. For chargebacks that do require specific compelling evidence, the models will highlight category groups to focus on.


**NOTE**
 These recommendations are only intended to provide guidance and do not limit your options if you choose to provide different or additional types of evidence.

 

To enable this feature, please reach out to your Customer Success Manager and ask to join the beta. If you do not currently have a Customer Success Manager, please [Contact us](/braintree/help/ChargebackDisputeInfo).


### PayPal disputes

PayPal disputes can be managed in your Braintree Control Panel and your PayPal Resolution Center. [See our PayPal disputes support article for details.](/braintree/articles/guides/payment-methods/paypal/disputes)


## Refunds

Sometimes, customers may request a refund from you directly while simultaneously issuing a chargeback with their bank. Because these requests are communicated through different channels, you may receive notification of a chargeback for a transaction that you have already refunded directly to the customer.

Refunding a transaction does not automatically cancel any existing chargebacks or prevent the customer from issuing one in the future. You will still be debited the disputed amount for all chargebacks, so you could lose double the amount of the original transaction if you refund a transaction that is also charged back.

If you are notified of a chargeback for a refunded transaction, we strongly encourage you to dispute it. We will automatically add evidence to your dispute submission if the disputed transaction was refunded via Braintree. If you issued the refund outside of Braintree, and the disputed transaction requires compelling evidence, you are responsible for providing evidence of the refund. [Contact us](/braintree/help/ChargebackDisputeInfo) for assistance with the dispute.


**IMPORTANT**
 If you lose or accept a chargeback that you have already issued a refund for, Braintree is not liable for the chargeback loss.

 


## Pre-arbitrations

While you can dispute pre-arbitrations, it's been our experience that merchants rarely win these cases without the introduction of new and compelling evidence.


**NOTE**
 As of **August 27th, 2025**, Braintree will auto accept pre-arbitrations under $1,000 for flat-rate merchants in the US, ensuring that arbitration fees are not passed on to them. Flat-rate merchants will have the ability to represent pre-arbitrations exceeding $1,000.

 



To help determine what you should do when you receive a pre-arb, you’ll want to take a look at the original evidence that was submitted in the dispute. If you have additional evidence, you can dispute the pre-arb. If you don’t have additional evidence, it is usually best to accept it. Regardless of the final outcome, you will still be charged a fee to process the pre-arb.

