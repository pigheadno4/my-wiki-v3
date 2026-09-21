<!-- Source URL: https://developer.paypal.com/braintree/articles/aib-bf/chargebacks-retrievals-prearbs -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: 'Chargebacks, Retrievals, and Pre-Arbs'
slug: /articles/aib-bf/chargebacks-retrievals-prearbs/
createTime: '2025-04-01T23:40:10.778Z'
updateTime: '2025-04-01T23:40:10.806Z'
---



# Chargebacks, Retrievals, and Pre-Arbs


**NOTE**
 This article describes credit card transaction disputes. For more information about PayPal disputes, see [PayPal disputes](/braintree/articles/guides/payment-methods/paypal/disputes).

 

Unfortunately, chargebacks, retrievals, and pre-arbitrations are a standard part of doing business – even if you follow our [suggested precautions](/braintree/articles/risk-and-security/chargebacks-retrievals/reducing-chargebacks) to prevent them.


## Notifications

When one of your cardholders initiates a dispute, you’ll receive an email from [disputes@braintreepayments.com](mailto:disputes@braintreepayments.com) with instructions on how to proceed.

By default, your first admin [user](/braintree/articles/control-panel/users-roles/managing-users-roles) created in the gateway will receive dispute notifications, but this can be adjusted in the Control Panel. To edit your notifications:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Processing**from the drop-down menu
- Scroll to the**Notifications**section
- Next to**Dispute Notifications**, click the**Options**link

You can adjust the frequency of the notifications and designate who receives them. When designating recipients, you have two options: adding a User Recipient, or using the Email Address field.

**User Recipients** : This field allows you to send notifications to existing users in the Control Panel. These recipients will receive notifications based on their role and any sub-merchants they are associated with (if applicable); if their permissions don’t allow them to see certain transactions, or they are not associated with a certain sub-merchant, they won’t receive dispute notifications for those transactions.

**Email Address** : This field allows you to send notifications to any email address, regardless of whether the email is associated with a user in the Control Panel. This can be particularly helpful if you use internal distribution lists to manage disputes (e.g. [disputes@yourcompany.com](mailto:disputes@yourcompany.com) ). Emails entered in this field will receive all dispute notifications—even if the address corresponds to a user with limited permissions, they will still receive notifications for all disputes.

Any merchant accounts that do not currently have a recipient designated will be listed here as well. While not all merchant accounts will generate dispute notifications, we recommend that you assign notification recipients to as many merchant accounts as possible.

In addition to email notifications, you can set up webhooks to notify you if a chargeback, retrieval, or pre-arb’s [status](#statuses) is updated to Open, Won, or Lost. For more information on setting up webhooks, see our [webhooks guide](/braintree/docs/guides/webhooks/overview).


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

Every chargeback, retrieval, or pre-arb has a reply-by date listed in the Control Panel. At 12am on this date you will lose the opportunity to submit evidence. The time zone for your account was established during the application process; to see your current time zone settings, click on the gear icon in the top right corner, click **Business** from the drop-down menu, and scroll to the **Time Zone** section.

If you let the case expire, an Accept response will be sent on your behalf and you will no longer be able to dispute the chargeback. This is to mitigate any non-response fees assessed by the card brands, and will not affect your reporting (e.g. cases you allow to expire will still have the Expired  [status](#statuses) ).

Each chargeback, retrieval, or pre-arb will have a [dispute reason](/braintree/docs/reference/response/dispute/ruby#reason), which helps you determine what action you should take. We provide specific recommendations in the Control Panel based on the reason code, but there are some general guidelines to keep in mind for each type of dispute.


**NOTE**
 Disputes can now be managed via the API as well. [Learn more.](/braintree/docs/guides/disputes/overview)

 


## Chargebacks

When a cardholder disputes a transaction with their bank, this is called a **chargeback**. The transaction amount is immediately debited from the payout funds scheduled for deposit into your bank account, and held by the cardholder’s bank until a resolution is determined. If the amount set for payout is not enough to cover this chargeback debit, your account will go negative until you process again.

The cardholder's bank will then give you the opportunity to submit evidence against the chargeback and evaluates any documentation you provide. If the bank rules in your favor, the transaction amount will be returned to your payout funds; if you lose or accept the chargeback, the cardholder will keep the funds. Regardless of the outcome, you will be charged a chargeback fee.


### Accepting a chargeback

When you accept a chargeback, the funds will be issued to the cardholder and you will still be charged the chargeback fee. Accepting a chargeback indicates that you don’t wish to take any further action, but it doesn’t necessarily imply that you agree with the cardholder’s claim.

Merchants typically accept chargebacks if the transaction amount is minor enough that it doesn’t justify the work of submitting evidence, or if the transaction is known to be fraudulent. The latter is particularly true when a merchant receives a chargeback for an American Express transaction; they are strong advocates for their cardmembers, and as a result merchants are usually at a disadvantage when the chargeback is related to fraud.


### Disputing a chargeback

If you would like to contest a chargeback, you can **dispute** it. The evidence you provide to help identify the validity of the transaction will be passed on to the bank for review. If the bank rules in your favor, the transaction amount will be returned to your payout funds; if you lose, the funds will remain in the cardholder’s account. Regardless of the outcome, you will be charged the chargeback fee.

Any pertinent information regarding the history of the original transaction—including AVS or CVV checks or [card verification](/braintree/articles/control-panel/vault/card-verification) performed by Braintree—will be automatically included in your claim if you dispute the chargeback in the Control Panel. If you have additional evidence, you can choose to include information in the text box and/or upload relevant attachments by clicking **Attach Image**.


#### Submitting evidence

Every chargeback is different, so the evidence you provide will vary depending on the reason for the chargeback and the documents you have available. [See our public support article for advice on what evidence to submit.](/braintree/articles/risk-and-security/chargebacks-retrievals/disputing-chargebacks#submitting-evidence)


## Retrievals

A **retrieval** is a request for information about an unidentifiable charge. Unlike chargebacks and pre-arbs, the transaction amount will not be removed from your payout funds, and you will not be charged a fee to process the retrieval.

To lower the risk of a retrieval turning into a chargeback, we recommend that you **Dispute** the retrieval and [provide information](#submitting-evidence) that will help the cardholder identify the transaction.

If the cardholder initiated the inquiry due to suspected fraud, it’s usually best to issue a refund. Retrievals filed with a fraud-related [dispute reason](/braintree/docs/reference/response/dispute/ruby#reason) often become chargebacks despite any evidence submitted, so refunding the cardholder may help you avoid the chargeback fee.


## Pre-arbs

A pre-arbitration, or **pre-arb**, occurs when a chargeback is filed, the merchant wins, and the cardholder disputes the charge for a second time. While you can dispute pre-arbs, it's been our experience that merchants rarely win these cases without the introduction of new and compelling evidence.

To help determine what you should do when you receive a pre-arb, you’ll want to take a look at the original evidence that was submitted by both you and Braintree. From the Disputes page, click on the corresponding **Dispute ID**, then click the link next to **Original Evidence** to download a PDF that contains this information.

If you have additional evidence you can [dispute](#disputing-a-chargeback) the pre-arb; if you don’t have additional evidence, it is usually best to [accept](#accepting-a-chargeback) it. Regardless of the final outcome, you will still be charged a fee to process the pre-arb.


## Statuses


- Open: The chargeback, retrieval, or pre-arb has been issued and no action has been taken yet
- Accepted: You have opted out of providing evidence for the chargeback or pre-arb
- Auto Accepted: The dispute has been automatically accepted for the best merchant experience
- Disputed: You have submitted evidence against the claim and are waiting for the decision from the bank
- Won: The bank has ruled in your favor, and the funds should return to your bank account within 2-3 business days
- Lost: The bank has not ruled in your favor, and the funds will remain with the cardholder
- Expired: The reply-by date to submit evidence has passed and you have forfeited your right to dispute the case


## Dispute Reports

Users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access the Dispute Report in the Control Panel. To access the report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Click the**Run Report**button for the report you'd like to create


### Disputes Report

This report lists every dispute within a given date range, along with important details such as the status of the dispute or the payment method type used for the disputed transaction. Use the Dispute Report when running a chargeback analysis.


### Disputes Financial Impact Report

This report lists every disbursement event within a given date range, along with important details about the dispute and transaction in question. Every disbursement event will indicate the date of impact in the Disbursement Date column and the amount debited or credited in the Disbursed Amount column, indicating when disputed funds were credited or debited from your bank account. Use this report along with your statement for reconciliation purposes.

