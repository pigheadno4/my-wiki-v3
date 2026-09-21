<!-- Source URL: https://developer.paypal.com/braintree/articles/apac/chargebacks-retrievals-prearbs -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: 'Chargebacks, Retrievals, and Pre-Arbs'
slug: /articles/apac/chargebacks-retrievals-prearbs/
createTime: '2025-04-01T22:02:36.753Z'
updateTime: '2025-04-01T22:02:36.773Z'
---



# Chargebacks, Retrievals, and Pre-Arbs


**NOTE**
 This article describes credit card transaction disputes. For more information about PayPal disputes, see [PayPal disputes](/braintree/articles/guides/payment-methods/paypal/disputes).

 

Unfortunately, chargebacks, retrievals, and pre-arbitrations are a standard part of doing business—even if you follow our [suggested precautions](/braintree/articles/risk-and-security/chargebacks-retrievals/reducing-chargebacks) to prevent them. Don’t worry, though—we’re here to help.


## Notifications

When one of your cardholders initiates a dispute, you’ll receive an email from [disputes@braintreepayments.com](mailto:disputes@braintreepayments.com) with instructions on how to proceed. To add or change notifications, follow the instructions below:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Processing**from the drop-down menu
- Scroll to the**Notifications**section
- Next to**Dispute Notifications**, click the**Options**link

You can adjust the frequency of the notifications and designate who receives them. When designating recipients, you have two options: adding a User Recipient, or using the Email Address field.

**User Recipients:** This field allows you to send notifications to existing users in the Control Panel. These recipients will receive notifications based on their [role](/braintree/articles/control-panel/users-roles/managing-users-roles) and any sub-merchants they are associated with (if applicable); if their permissions don’t allow them to see certain transactions, or they are not associated with a certain sub-merchant, they won’t receive dispute notifications for those transactions.

**Email Address:** This field allows you to send notifications to any email address, regardless of whether the email is associated with a user in the Control Panel. This can be particularly helpful if you use internal distribution lists to manage disputes (e.g. [disputes@yourcompany.com](mailto:disputes@yourcompany.com) ). Emails entered in this field will receive all dispute notifications – even if the address corresponds to a user with limited permissions, they will still receive notifications for all disputes.

Any merchant accounts that do not currently have a recipient designated will be listed here as well. While not all merchant accounts will generate dispute notifications, we recommend that you assign notification recipients to as many merchant accounts as possible.

In addition to email notifications, you can set up webhooks to notify you if a chargeback, retrieval, or pre-arb’s [status](#statuses) is updated to Open, Won, or Lost. For more information on setting up webhooks, see our [webhooks guide](/braintree/docs/guides/webhooks/overview).


## Managing Disputes

If you recently received a notice that a new dispute has been opened, you can reply to the email with evidence or follow the steps below to submit your response in the Control Panel:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Disputes**in the navigation bar
- Click the filter button in the upper left corner of the disputes list page to search for disputes within the provided set of parameters
- To view more information or take action on a dispute, click that dispute's row in the results list or the expand button on the far right side of the row. From this menu, select from the following options:
- **Submit Evidence**: Go to the evidence submission page, where you can upload and submit evidence
- **Accept**: Accept the dispute
- **View Transaction**: Go to the transaction against which this dispute was raised
- **View Customer**: View more information about the customer who raised this dispute
- **View Dispute**: View further details about this dispute, including its event history



Every chargeback, retrieval, or pre-arb has a reply-by date listed in the Control Panel. At 12am on this date you will lose the opportunity to submit evidence. The time zone for your account was established during the application process; to see your current time zone settings, click on the gear icon in the top right corner, click **Business** from the drop-down menu, and scroll to the **Time Zone** section.

If you let the case expire, an Accept response will be sent on your behalf and you will no longer be able to dispute the chargeback. This is to mitigate any non-response fees assessed by the card brands, and will not affect your reporting (e.g. cases you allow to expire will still have the Expired  [status](#statuses) ).

Each chargeback, retrieval, or pre-arb will have a [dispute reason](/braintree/docs/reference/response/dispute/ruby#reason), which helps you determine what action you should take. We provide specific recommendations in the Control Panel based on the reason code, but there are some general guidelines to keep in mind for each type of dispute.


**NOTE**
 Disputes can be managed via the API as well. [Learn more.](/braintree/docs/guides/disputes/overview)

 


## Chargebacks

When a cardholder disputes a transaction with their bank, this is called a chargeback. The transaction amount and [chargeback fee](#chargeback-fees) are debited from your net disbursements prior to being deposited in your bank account and are held by the cardholder’s bank until a resolution is determined. You can locate these deductions on your [Daily Disbursement Details](/braintree/articles/apac/statements-reconciliation#daily-disbursement-details) under **Chargeback Debits**. If you need additional details on individual chargebacks, including case numbers and amounts, download your [APAC Transaction Detail Report](/braintree/articles/apac/statements-reconciliation#downloading-the-apac-transaction-detail-report).

The cardholder’s bank then gives you the opportunity to submit evidence against the cardholder’s claim and evaluates any documentation you provide. If the bank rules in your favor, the disputed amount will be returned to your net disbursements for deposit into your bank account; if you lose or accept the chargeback, the funds will be returned to the cardholder. Regardless of the outcome, the chargeback fee will not be returned.


### Chargeback fees

A chargeback fee is applied for all chargebacks, and is non-refundable — regardless of the outcome. The fee is determined by your settlement currency.


- 30 SGD
- 160 HKD
- 90 MYR


### Accepting a chargeback

When you accept a chargeback, the funds will be issued to the cardholder and you will still be charged a [chargeback fee](#chargeback-fees). Accepting a chargeback indicates that you don’t wish to take any further action, but it doesn’t necessarily imply that you agree with the cardholder’s claim.

Merchants typically accept chargebacks if the transaction amount is minor enough that it doesn’t justify the work of submitting evidence, or if the transaction is known to be fraudulent. The latter is particularly true when a merchant receives a chargeback for an American Express transaction; they are strong advocates for their cardmembers, and as a result merchants are usually at a disadvantage when the chargeback is related to fraud.


### Disputing a chargeback

If you would like to contest a chargeback, you can **dispute** it. The evidence you provide to help identify the validity of the transaction will be passed on to the bank for review. Regardless of the outcome, you will be charged a [chargeback fee](#chargeback-fees).


#### Submitting evidence

Every chargeback is different, so the evidence you provide will vary depending on the reason for the chargeback and the documents you have available. [See our public support article for advice on what evidence to submit.](/braintree/articles/risk-and-security/chargebacks-retrievals/disputing-chargebacks#submitting-evidence)

All evidence should be submitted via the Control Panel or directly to our [Disputes team](/braintree/help/ChargebackDisputeInfo). Once we receive your evidence, we’ll submit it to the appropriate banking partner and facilitate the dispute process for you.


#### Dispute timelines

If you would like to dispute a chargeback, you’ll need to submit your evidence prior to the submission deadline, which is indicated in the dispute notification email and displayed in the Control Panel.

After your evidence has been submitted, the issuing bank for the cardholder will have up to 45 days to continue the dispute. Funds lost or won from disputes will be reflected in your [monthly statement](/braintree/articles/apac/statements-reconciliation).


## Retrievals

A retrieval is a request for information about an unidentifiable charge. Unlike chargebacks and pre-arbs, funds are not removed from your net disbursements, and you will not be charged a fee to process the retrieval.

To lower the risk of a retrieval turning into a chargeback, we recommend that you **Dispute** the retrieval and [provide information](#submitting-evidence) that will help the cardholder identify the transaction.

If the cardholder initiated the inquiry due to suspected fraud, it’s usually best to issue a refund. Retrievals filed with a fraud-related [dispute reason](/braintree/docs/reference/response/dispute/ruby#reason) often become chargebacks despite any evidence submitted, so refunding the cardholder may help you avoid the chargeback fee.


## Pre-arbs

A pre-arbitration, or **pre-arb**, occurs when a chargeback is filed, the merchant wins, and the cardholder disputes the charge for a second time. While you can dispute pre-arbs, it's been our experience that merchants rarely win these cases without the introduction of new and compelling evidence.

To help determine what you should do when you receive a pre-arb, you’ll want to take a look at the original evidence that was submitted by both you and Braintree. From the Disputes page, click on the corresponding **Dispute ID**, then click the link next to **Original Evidence** to download a PDF that contains this information.

If you have additional evidence you can [dispute](#disputing-a-chargeback) the pre-arb; if you don’t have additional evidence, it is usually best to [accept it](#accepting-a-chargeback).


## Statuses


- Open: The chargeback, retrieval, or pre-arb has been issued and no action has been taken yet
- Accepted: You have opted out of providing evidence for the chargeback or pre-arb
- Auto Accepted: The dispute has been automatically accepted for the best merchant experience
- Disputed: You have submitted evidence against the claim and are waiting for the decision from the bank
- Won: The bank has ruled in your favor, and the funds should return to your bank account within 2-3 business days
- Lost: The bank has not ruled in your favor, and the funds will remain with the cardholder
- Expired: The reply-by date to submit evidence has passed and you have forfeited your right to dispute the case

Note that **Accepted** and **Disputed** statuses will only be available if you submit your response via the control panel. If you do not respond in the Control Panel, disputes will be updated to **Expired** after the submission deadline has passed. If you have submitted evidence by email, your evidence will still be disputed, and the dispute will be updated to **Won** or **Lost** based on the results of the adjudication.


## Dispute Report

Users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access the Dispute Report in the Control Panel. To access the report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Next to**Dispute Report**, click the**Run Report**button

This report will provide you with a line-by-line breakdown that shows every status change in your transactions’ dispute history. For example, you might see one line item that represents when the dispute was Opened, another line item that represents when the dispute was Disputed, and a final line item that represents when the dispute was Won. While the Dispute Report can be helpful in identifying disputes trends, it should not be used for reconciliation purposes.

