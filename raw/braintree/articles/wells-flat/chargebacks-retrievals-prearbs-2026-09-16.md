<!-- Source URL: https://developer.paypal.com/braintree/articles/wells-flat/chargebacks-retrievals-prearbs -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: 'Chargebacks, Retrievals, and Pre-Arbs'
slug: /articles/wells-flat/chargebacks-retrievals-prearbs/
createTime: '2025-04-01T22:03:09.053Z'
updateTime: '2025-08-19T11:46:18.017Z'
---



# Chargebacks, Retrievals, and Pre-Arbs


**NOTE**
 This article describes credit card transaction disputes. For more information about PayPal disputes, see [PayPal disputes](/braintree/articles/guides/payment-methods/paypal/disputes).

 


## Dispute Process

There are four stages of the dispute lifecycle: retrieval, chargeback, pre-arbitration, and arbitration. You can manage all stages of the lifecycle except arbitration with Braintree.


- Retrieval: A Retrieval is a request for information about a charge. Unlike Chargebacks and Pre-Arbitrations, funds are not removed from your bank account, and you aren't charged a fee to process the Retrieval. It's important to note that Retrieval is an optional stage in a dispute lifecycle. The issuing bank can directly pursue a Chargeback if the cardholder provides strong evidence. Visa and Mastercard have deprecated the Retrieval stage from the dispute process. US issuers can still create Retrievals for Visa or Mastercard, but merchants do not need to respond if that happens.


- Chargeback: A Chargeback occurs when a cardholder disputes a transaction with their bank. The disputed amount is immediately debited from your bank account and held by the bank until a resolution is determined. You are also assessed a non-refundable Chargeback fee regardless of the later outcome of the Chargeback.


- Pre-Arbitration: Pre-Arbitration is an additional attempt to resolve disputes without the card networks' interference. Issuers typically pursue Pre-Arbitration to address the information provided in the Chargeback evidence. Issuers raise Pre-Arbitrations for different reasons, including but not limited to:


- A merchant's response to the Chargeback is not compelling
- A cardholder provides additional information to advance the dispute
- A cardholder changes the reason for the dispute.

You are also assessed a non-refundable Chargeback fee regardless of the later outcome of the Pre-Arbitration.


- Arbitration: Arbitration is the final stage of the dispute lifecycle and happens when an agreement can't be reached between merchants and cardholders. In that case, disputes are escalated to the card networks to decide. Filed Arbitrations carry substantial fees that can reach several hundred dollars, assessed by card networks per lost case. Braintree does not offer an end-to-end support for the Arbitration phase of the dispute lifecycle.



When a case is escalated to card networks, Braintree does not create a dispute for Arbitration. Therefore, Arbitrations are not found in the Braintree Control Panel, Disputes APIs, or Disputes reports. Please note that merchants can't submit additional evidence for Arbitrations.

Once the card networks issue the Arbitration verdict, the losing party will forfeit the disputed amount and the Arbitration fees will be assessed and passed through to merchants. Currently, Braintree is notified by our banking partner(s) about the Arbitration outcome, and we debit the lost arbitration disputed amount from the merchant's daily disbursement. The debited amount will be reflected in the Disputes Financial Impact Report as a separate line item with an “Arbitration” descriptor. Merchants on interchange pricing will see pass-through fees associated with Arbitrations in the Pass-through Fee Report on the Control Panel.

Mastercard currently assesses $575 for lost Arbitrations that are being passed to the losing party ($150 Mastercard Filing fee, $250 Mastercard Administrative Fee and $20 Arbitration, Pre-compliance, or Compliance Fee). Additionally, Mastercard assesses a $100 technical violation fee at the Arbitration stage where Mastercard determines the original transaction violated a Mastercard compliance rule. Visa currently assesses $500 per Arbitration case in which Visa determines the merchant is liable for the Arbitration.

**Braintree has no control over the Arbitration outcome and has no discretion regarding whether the above fees are passed through to you if the Arbitration is lost.**


**NOTE**
 Please note that card networks assess various network fees throughout the dispute lifecycle depending on the type of disputes, when and how merchants respond to disputes, and other criteria. Merchants on interchange pricing will see these fees in their Pass-through Fee Report.

 


## Dispute Notifications

When one of your cardholders initiates a dispute, you'll receive an email from [disputes@braintreepayments.com](mailto:disputes@braintreepayments.com) with instructions on how to proceed.

By default, your first admin [user](/braintree/articles/control-panel/users-roles/managing-users-roles) created in the gateway will receive dispute notifications, but this can be adjusted in the Control Panel. To edit your notifications:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Processing**from the drop-down menu
- Scroll to the**Notifications**section
- Next to**Dispute Notifications**, click the**Options**link

You can adjust the frequency of the notifications and designate who receives them. When designating recipients, you have two options: adding a User Recipient, or using the Email Address field.

**User Recipients:** This field allows you to send notifications to existing users in the Control Panel. These recipients will receive notifications based on their [role](/braintree/articles/control-panel/users-roles/managing-users-roles) and any sub-merchants they are associated with (if applicable); if their permissions don't allow them to see certain transactions, or they are not associated with a certain sub-merchant, they won't receive dispute notifications for those transactions.

**Email Address:** This field allows you to send notifications to any email address, regardless of whether the email is associated with a user in the Control Panel. This can be particularly helpful if you use internal distribution lists to manage disputes (e.g. [disputes@yourcompany.com](mailto:disputes@yourcompany.com) ). Emails entered in this field will receive all dispute notifications—even if the address corresponds to a user with limited permissions, they will still receive notifications for all disputes.

Any merchant accounts that do not currently have a recipient designated will be listed here as well. While not all merchant accounts will generate dispute notifications, we recommend that you assign notification recipients to as many merchant accounts as possible.

In addition to email notifications, you can set up webhooks to notify you if a chargeback, retrieval, or pre-arb's [status](#statuses) is updated to Open, Won, or Lost. For more information on setting up webhooks, see our [webhooks guide](/braintree/docs/guides/webhooks/overview).


## Managing in the Control Panel

We're currently rolling out some changes to our user interface for managing chargebacks, retrievals, and pre-arbs in the Control Panel.

If you recently received a notice that the Disputes section of your Control Panel has been updated, follow these steps to manage your disputes:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Disputes**in the navigation bar
- Click the filter button in the upper left corner of the disputes list page to search for disputes within the provided set of parameters
- To view more information or take action on a dispute, click that dispute's row in the results list or the expand button on the far right side of the row. From this menu, select from the following options:


- **Submit Evidence**: Go to the evidence submission page, where you can upload and submit evidence
- **Accept**: Accept the dispute
- **View Transaction**: Go to the transaction against which this dispute was raised
- **View Customer**: View more information about the customer who raised this dispute
- **View Dispute**: View further details about this dispute, including its event history

Otherwise, follow these steps:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Disputes**in the navigation bar
- Search for a dispute within the provided set of parameters
- To submit evidence against a dispute, click the**Dispute**button
- To accept the dispute, click the**Accept**button


**NOTE**
 Every chargeback, retrieval, or pre-arb has a reply-by date listed in the Control Panel. At 12am on this date, you will lose the opportunity to submit evidence.

 

The time zone for your account was established during the application process; to see your current time zone settings, click on the gear icon in the top right corner, click **Business** from the drop-down menu, and scroll to the **Time Zone** section.

If you let the case expire, an Accept response will be sent on your behalf and you will no longer be able to dispute the chargeback. This is to mitigate any non-response fees assessed by the card brands, and will not affect your reporting (e.g. cases you allow to expire will still have the Expired  [status](#statuses) ).

Each chargeback, retrieval, or pre-arb will have a [dispute reason](/braintree/docs/reference/response/dispute#reason), which helps you determine what action you should take. We provide specific recommendations in the Control Panel based on the reason code, but there are some general guidelines to keep in mind for each type of dispute.


**NOTE**
 Disputes can now be managed via the API as well. [Learn more.](/braintree/docs/guides/disputes/overview)

 


## Chargebacks

When a cardholder disputes a transaction with their bank, this is called a **chargeback**. The disputed amount is immediately debited from your bank account and held by the bank until a resolution is determined. The bank then gives you the opportunity to either accept the chargeback or to submit evidence against the cardholder's claim.


### Accepting a chargeback

When you accept a chargeback, the funds will be issued to the cardholder and you will still be charged a $15 chargeback fee. Accepting a chargeback indicates that you don't wish to take any further action, but it doesn't necessarily imply that you agree with the cardholder's claim.

Merchants typically accept chargebacks if the transaction amount is minor enough that it doesn't justify the work of submitting evidence, or if the transaction is known to be fraudulent. The latter is particularly true when a merchant receives a chargeback for an American Express transaction; they are strong advocates for their cardmembers, and as a result merchants are usually at a disadvantage when the chargeback is related to fraud.


### Disputing a chargeback

If you would like to contest a chargeback, you can dispute it by submitting evidence against the cardholder's claim. You have until the reply-by date stated in the Control Panel to provide documentation identifying the validity of the transaction. If the bank rules in your favor, the transaction amount will be returned to your bank account; if you lose, the funds will remain in the cardholder's account. Regardless of the outcome, you will be charged a $15 chargeback fee.

Any pertinent information regarding the history of the original transaction—including AVS or CVV checks or [card verification](/braintree/articles/control-panel/vault/card-verification) performed by Braintree—will be automatically included in your claim if you dispute the chargeback in the Control Panel. If you have additional evidence, you can choose to include information in the text box and/or upload relevant attachments by clicking **Attach Image**.


#### Submitting evidence

Every chargeback is different, so the evidence you provide will vary depending on the reason for the chargeback and the documents you have available. [See our public support article for advice on what evidence to submit.](/braintree/articles/risk-and-security/chargebacks-retrievals/disputing-chargebacks#submitting-evidence)


## Retrievals

A **retrieval** is a request for information about an unidentifiable charge. Unlike chargebacks and pre-arbs, funds are not removed from your bank account, and you will not be charged a fee to process the retrieval.

To lower the risk of a retrieval turning into a chargeback, we recommend that you dispute the retrieval and [provide information](#submitting-evidence) that will help the cardholder identify the transaction.

If the cardholder initiated the inquiry due to suspected fraud, it's usually best to issue a refund. Retrievals filed with a fraud-related [dispute reason](/braintree/docs/reference/response/dispute#reason) often become chargebacks despite any evidence submitted, so refunding the cardholder may help you avoid the chargeback fee.


## Pre-arbitrations

A pre-arbitration, or **pre-arb**, occurs when a chargeback initially resolved in the merchant’s favor is challenged again by the cardholder. Merchants may respond to pre-arbitrations; however, according to card network guidelines, responses are unlikely to succeed unless new and compelling evidence is provided. If only the same documentation as previously submitted is available, merchants are generally advised to accept the pre-arbitration.


**NOTE**
 As of **August 27th, 2025**, Braintree will auto accept pre-arbitrations under $1,000 for flat-rate merchants in the US, ensuring that arbitration fees are not passed on to them. Flat-rate merchants will have the ability to represent pre-arbitrations exceeding $1,000.

 


### What to expect

For pre-arbitrations below the $1,000 threshold, you’ll notice the status **Auto Accepted**. This means Braintree has accepted the pre-arbitration on your behalf.

If you wish to set a higher threshold, you can do so within the control panel:


- Log in to your**Control Panel**
- Navigate to Account Settings -&gt; Processing Options -&gt; Disputes -&gt; Auto Accept Pre-Arbitrations
- Click "Options" and choose a value above $1,000 to configure your preferred threshold

For pre-arbitrations that are not auto accepted, you can dispute the pre-arbitration if you have additional evidence not previously provided. However, if you lack new evidence, per network guidance, the pre-arb should be accepted.




### Why this change is necessary



Network changes have made arbitrations more frequent and costly. By auto accepting lower-value pre-arbitrations, we aim to keep our services affordable for all merchants and align with industry standards.

Pre-arbitrations below $1,000 typically have low recovery rates and can cost $500-$600 or more for cases that escalate to arbitration, which is paid by the losing party. Since flat-rate merchants don’t currently bear these fees, this policy is preferred to avoid introducing new fees or increasing existing ones in response to market changes.


## Statuses


- Open: The chargeback, retrieval, or pre-arb has been issued and no action has been taken yet
- Accepted: You have opted out of providing evidence for the chargeback or pre-arb
- Auto Accepted: The dispute has been automatically accepted and no action is required
- Disputed: You have submitted evidence against the claim and are waiting for the decision from the bank
- Won: The bank evaluated the dispute and ruled in your favor, and the funds should return to your bank account within 2-3 business days
- If you have enrolled in the Chargeback Protection Tool or Effortless Chargeback protection Tool, PayPal evaluated the dispute and ruled in your favor. To learn more,[click here](/braintree/articles/guides/fraud-tools/premium/chargeback-protection#managing-chargebacks).


- Lost: The bank evaluated the dispute and ruled in the customer’s favor, and the funds will remain with the cardholder
- If you have enrolled in the Chargeback Protection Tool or Effortless Chargeback protection Tool, PayPal evaluated the dispute and ruled in the customer's favor. To learn more,[click here](/braintree/articles/guides/fraud-tools/premium/chargeback-protection#managing-chargebacks).


- Expired: The reply-by date to submit evidence has passed and you have forfeited your right to dispute the case


## Dispute Reports

Users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access the Dispute Report in the Control Panel. To access the report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Click the**Run Report**button for the report you'd like to create


### Disputes Report

This report will provide you with a line-by-line breakdown that shows every status change in your transactions' dispute history. For example, you might see one line item that represents when the dispute was Opened, another line item that represents when the dispute was Disputed, and a final line item that represents when the dispute was Won. Use the Dispute Report when running a chargeback analysis.


### Disputes Financial Impact Report (DFIR)

This report lists every disbursement event within a given date range, along with important details about the dispute and transaction in question. Every disbursement event will indicate the date of impact in the Disbursement Date column and the amount debited or credited in the Disbursed Amount column, indicating when disputed funds were credited or debited from your bank account. Use this report along with your statement for reconciliation purposes.

