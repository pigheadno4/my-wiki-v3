<!-- Source URL: https://developer.paypal.com/braintree/articles/br/chargebacks-retrievals-prearbs -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: 'Chargebacks, Retrievals, and Pre-Arbs'
slug: /articles/br/chargebacks-retrievals-prearbs/
createTime: '2025-04-01T23:11:47.886Z'
updateTime: '2025-04-01T23:11:47.913Z'
---



# Chargebacks, Retrievals, and Pre-Arbs


**NOTE**
 This article describes credit card transaction disputes. For more information about PayPal disputes, see [PayPal disputes](/braintree/articles/guides/payment-methods/paypal/disputes).

 

Unfortunately, chargebacks, retrievals, and pre-arbitrations are a standard part of doing business – even if you follow our [suggested precautions](/braintree/articles/risk-and-security/chargebacks-retrievals/reducing-chargebacks) to prevent them. Don’t worry, though – we’re here to help.


## Notifications

When one of your cardholders initiates a dispute, you’ll receive an email from [disputes@braintreepayments.com](mailto:disputes@braintreepayments.com) with instructions on how to proceed.

By default, your first admin [user](/braintree/articles/control-panel/users-roles/managing-users-roles) created in the gateway will receive notifications, but this can be adjusted in the Control Panel. To edit your notifications:


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

Each chargeback, retrieval, or pre-arb will have a [dispute reason](/braintree/docs/reference/response/dispute#reason), which helps you determine what action you should take. We provide specific recommendations in the Control Panel based on the reason code, but there are some general guidelines to keep in mind for each type of dispute.


**NOTE**
 Disputes can be managed via the API as well. [Learn more.](/braintree/docs/guides/disputes/overview)

 


## Chargebacks

When a cardholder disputes a transaction with their bank, this is called a **chargeback**. No funds are debited from your account and no fees are assessed when a chargeback is opened. The bank then gives you the opportunity to either accept the chargeback or to submit evidence against the cardholder’s claim.


### Accepting a chargeback

When you accept a chargeback, the disputed funds will be issued to the cardholder. The amount of time it takes for the cardholder to receive their funds varies from bank to bank. Once this process has been completed, the chargeback will update to a Lost status. At that time, the disputed amount and a chargeback fee will be debited from your bank account.

Accepting a chargeback indicates that you don’t wish to take any further action, but it doesn’t necessarily imply that you agree with the cardholder’s claim. Merchants typically accept chargebacks if the transaction amount is minor enough that it doesn’t justify the work of submitting evidence, or if the transaction is known to be fraudulent. The latter is particularly true when a merchant receives a chargeback for an American Express transaction; they are strong advocates for their cardmembers, and as a result, merchants are usually at a disadvantage when the chargeback is related to fraud.


### Disputing a chargeback

If you would like to contest a chargeback, you can dispute it by submitting evidence against the cardholder's claim. You have until the reply-by date stated in the Control Panel to provide documentation identifying the validity of the transaction. Any pertinent information regarding the history of the original transaction – including AVS or CVV checks or [card verification](/braintree/articles/control-panel/vault/card-verification) performed by Braintree – will be automatically included in your claim if you dispute the chargeback in the Control Panel. If you have additional evidence, you can choose to include information in the text box and/or upload relevant attachments by clicking **Upload File**.

If the bank rules in your favor, no changes will be made to the case in the Control Panel. Because no funds were debited when the case was received, no financial movements occur when you win a case. The case will remain in Disputed, Accepted, or Expired status. If you lose, the case status will be updated to Lost status and the disputed amount, as well as the chargeback fee, will be debited from your bank account. This can occur up to 120 days after the case representment is submitted. There are rare instances where it may take longer than 120 days to be debited.


#### Submitting evidence

Every chargeback is different, so the evidence you provide will vary depending on the reason for the chargeback and the documents you have available. [See our public support article for advice on what evidence to submit.](/braintree/articles/risk-and-security/chargebacks-retrievals/disputing-chargebacks#submitting-evidence)


## Retrievals

A **retrieval** is a request for information about an unidentifiable charge. Unlike chargebacks and pre-arbs, these case types are non-financial and cannot be won or lost. This means no funds will be removed from your bank account and you will not be charged a fee to process the retrieval.

To lower the risk of a retrieval turning into a chargeback, we recommend that you dispute the retrieval and provide the cardholder with enough information to help them identify the transaction (e.g. date of the transaction, transaction amount, statement descriptor, etc.).

If the cardholder initiated the inquiry due to suspected fraud, it’s usually best to issue a refund and then respond to the retrieval with the refund details. Retrievals filed with a fraud-related [dispute reason](/braintree/docs/reference/response/dispute#reason) often become chargebacks despite any evidence submitted, so refunding the cardholder may help you avoid the chargeback fee.


## Pre-arbs

A pre-arbitration, or **pre-arb**, occurs when a chargeback is filed, the merchant wins, and the cardholder disputes the charge for a second time. While you can dispute pre-arbs, it's been our experience that merchants rarely win these cases without the introduction of new and compelling evidence.

To help determine what you should do when you receive a pre-arb, you’ll want to take a look at the original evidence that was submitted by both you and Braintree. From the Disputes page, click on the corresponding **Dispute ID**, then click the **Download** link under the **Dispute Evidence** section to download a PDF that contains this information.

If you have additional evidence, you can [dispute](#disputing-a-chargeback) the pre-arb; if you don’t have additional evidence, it is usually best to [accept it](#accepting-a-chargeback). When you accept a pre-arb, the funds will be returned to the cardholder. Once the bank completes that process, the case will be updated to Lost status and the disputed amount as well as the chargeback fee will be debited from your bank account.


## Statuses


- Open: The chargeback, retrieval, or pre-arb has been issued and no action has been taken yet
- Accepted: You have opted out of providing evidence for the chargeback or pre-arb
- Auto Accepted: The dispute has been automatically accepted for the best merchant experience
- Disputed: You have submitted evidence against the claim and no funds have been debited from your bank account
- Won: The bank has not ruled in the cardholder's favor, or has reversed a previous lost decision for the case
- If you have enrolled in the Chargeback Protection Tool or Effortless Chargeback protection Tool, PayPal evaluated the dispute and ruled in your favor. To learn more,[click here](/braintree/articles/guides/fraud-tools/premium/chargeback-protection#managing-chargebacks).


- Lost: The bank has ruled in the cardholder's favor, and the disputed funds have been debited from your bank account
- If you have enrolled in the Chargeback Protection Tool or Effortless Chargeback protection Tool, PayPal evaluated the dispute and ruled in the customer's favor. To learn more,[click here](/braintree/articles/guides/fraud-tools/premium/chargeback-protection#managing-chargebacks).


- Expired: The reply-by date to submit evidence has passed and you have forfeited your right to dispute the case


## Dispute Reports

Users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access the Dispute Report in the Control Panel. To access the report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Next to**Dispute Report**, click the**Run Report**button


### Disputes Report

This report lists every dispute status received within a given date range as individual lines items. This means you may see multiple line items for the same dispute case: one for when the case was Open and another for when it was Disputed. It will also contain important transaction details such as the payment method type used for the disputed transaction. Dispute status changes that result in a debit or credit will also include a value in the Disbursement Date column, indicating when disputed funds were credited or debited from your bank account. Use the Dispute Report when running a chargeback analysis or alongside your statement for reconciliation purposes.


### Disputes Financial Impact Report

This report lists every disbursement event within a given date range, along with important details about the dispute and transaction in question. Every disbursement event will indicate the date of impact in the Disbursement Date column and the amount debited or credited in the Disbursed Amount column, indicating when disputed funds were credited or debited from your bank account. Use this report along with your statement for reconciliation purposes.


**NOTE**
 For installment transactions, a single dispute will create one adjustment for each installment. Every adjustment will be detailed in this report, along with its associated projected disbursement date for use in reconciling with your statements.

 

In rare cases, disputes are debited when they are opened. These cases will display a Disbursement Date associated with the Open status to indicate when the funds will be debited. If a case that is debited on Open status is Won, there will be a corresponding Disbursement Date to indicate when the funds will be credited to your account. Use the [Disputes Financial Impact Report](/braintree/articles/br/chargebacks-retrievals-prearbs#disputes-financial-impact-report) when running a chargeback analysis or alongside your statement for reconciliation purposes.

