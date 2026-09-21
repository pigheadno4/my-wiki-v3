<!-- Source URL: https://developer.paypal.com/braintree/articles/risk-and-security/risk-factors/identifying-fraud -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Identifying Fraud
slug: /articles/risk-and-security/risk-factors/identifying-fraud/
createTime: '2025-04-01T23:07:28.002Z'
updateTime: '2025-04-01T23:07:28.021Z'
---



# Identifying Fraud

While we can help you mitigate fraud with our [full suite of fraud tools](/braintree/articles/guides/fraud-tools/overview), there's always a possibility that fraudulent transactions might slip through. This is why it's important to know the common indicators of fraud so you can identify suspicious transactions and act accordingly.

Below, we’ve outlined some questions to ask yourself when determining whether a transaction is legitimate. These questions are intended to be guidelines – it's always possible that a suspicious transaction may be legitimate. Typically it’s best to trust your instincts, but if you’re still unsure, feel free to [contact us](/braintree/help/FraudProtectionQuestion).


## Customer name


- **Does the customer’s name match the name on the card?**
- **Is the name misspelled?**
- **Is the formatting of the name incorrect?**It may be a red flag if the name is in all lowercase or missing an apostrophe or hyphen where necessary.


## Customer address


- **Do the billing and shipping addresses match?**Fraudulent transactions often have a shipping address that is far away from the billing address.
- **In the billing address, do the country, state, and city match?**Sometimes fraudsters will enter a completely different country, e.g. Chicago, IL, Indonesia.
- **Did they request expedited delivery?**Fraudsters want products ASAP, so they will likely choose the fastest form of shipping available.


## Customer email


- **Do the cardholder’s name and email address align?**For example, if the customer’s name is Bob Smith, his email is more likely to be[bsmith@example.com](mailto:/bsmith@example.com)than[TrainFan24_7@example.com](mailto:/TrainFan24_7@example.com).
- **Does the customer’s email address have an old or common domain?**Fraudsters tend to use domains like[gmx.com](http://gmx.com),[mail.com](http://mail.com),[inbox.com](http://inbox.com),[outlook.com](http://outlook.com),[yahoo.com](http://yahoo.com),[juno.com](http://juno.com), or even domains that don’t exist. It can also be suspicious if the email address includes a company name followed by a generic domain, like[bsmith-sailzoom@juno.com](mailto:/bsmith-sailzoom@juno.com).
- **Are there random characters in the customer’s email address?**If the email address aligns with the cardholder name, be wary of random characters in the suffix, such as[bsmith817g2d14@example.com](mailto:/bsmith817g2d14@example.com). Any string of 3 or more random alphanumeric characters could be cause for concern.


## Customer IP address


**NOTE**
 To identify the IP address, you will need to implement IP logging on your business’s web server.

 


- **Is the IP originating from a country where fraud is common?**Some examples are Cyprus, Nigeria, and Argentina.
- **Have you seen fraudulent transactions from this IP address or geographic location in the past?**
- **Is the IP originating from a location different from where the customer is located, or having products shipped?**
- **Is there a large distance between the IP, billing, and shipping addresses?**


## Transaction details


- **Are you seeing an abnormally large number of transactions in a short period of time, especially for the same amount or from the same card brand?**This is a common indicator of a carding attack.
- **Are you seeing multiple transactions with the same Bank Identification Number (BIN), but different card numbers?**It’s unusual to see the same BIN twice, so if you do, it’s possible that a series of cards from that bank have been compromised.[Read more about BINs.](/braintree/articles/control-panel/transactions/bank-identification-numbers)
- **Is the transaction from a country that is outside of your normal demographic?**This is worth investigating, especially if the transaction amount is larger than normal.
- **Is it a prepaid or gift card?**These are often associated with suspicious activity. On the other hand, corporate or travel and expense cards are typically trustworthy.
- **Are there multiple transactions with different cards that have the same customer name?**



 You can use free BIN search websites like [binbase.com](http://binbase.com/search.html) to find out where a card originated.

 


## Next steps

If you’re trying to decide whether or not to refund a transaction that you believe might be fraudulent, it’s usually best to trust your instincts and wait to provide your products or services until you feel confident that the transaction is legitimate. A good place to start is with the customer – you can try to contact them directly to confirm the details associated with the transaction, or verify phone and email information through third-party sites. Fraudulent transactions typically do not have valid contact information associated with them, so it's an effective first step in deciding how to proceed.

If you are unable to contact the customer or you have confirmed your suspicion that the transaction is fraudulent, we suggest that you [issue a void or refund](/braintree/articles/control-panel/transactions/refunds-voids-credits) to reduce the likelihood of chargebacks. You can also file a complaint with your local police department or the [Internet Crime Complaint Center](http://www.ic3.gov/default.aspx).

