<!-- Source URL: https://developer.paypal.com/braintree/articles/wells-flat/pre-dispute-programs -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Pre-dispute programs
slug: /articles/wells-flat/pre-dispute-programs/
createTime: '2025-04-02T02:09:47.487Z'
updateTime: '2025-04-02T02:09:47.504Z'
---



# Pre-dispute programs

Disputes are an inevitable part of running a business. However, some card networks offer programs that help merchants resolve disputes at the pre-dispute stage, before a dispute turns into a formal chargeback and counts against a merchant’s chargeback ratio.

Submitting evidence to represent disputes can be time-consuming and costly. Pre-dispute programs help merchants avoid the dispute representment process and the operational costs involved.


## Visa Rapid Dispute Resolution

The Visa Rapid Dispute Resolution (RDR) pre-dispute program is supported by Braintree in the US to improve customer experience and reduce operational requirements.

RDR is a pre-dispute program that helps:


- Resolve disputes using Visa’s Verifi platform.
- Avoid the chargeback process at the pre-dispute stage.
- Prevent escalation to a formal chargeback.

Enroll in the RDR program directly with Visa.

With RDR, a pre-dispute is evaluated against custom merchant-defined rules for automated resolution. If the pre-dispute satisfies the custom rules, a credit is sent to the cardholder to prevent a chargeback. Pre-disputes that do not satisfy the rules are processed through the standard chargeback flow. Using RDR to resolve pre-disputes accepts dispute liability and avoids the expensive process of managing chargebacks.


### How does Braintree handle pre-disputes resolved with RDR?

When a Visa chargeback satisfies RDR rules, the dispute is automatically accepted. RDR disputes are shown with a status of Auto-accepted in the Control Panel, through dispute webhooks, and in Dispute reports. Sign up for webhooks for the new Auto-Accepted status.

RDR-resolved chargebacks also have a Pre-Dispute Program: Visa RDR identifier on the Dispute Details page to help differentiate from standard chargebacks. If you use the Disputes APIs to manage your cases, pre_dispute_program: "visa_rdr" appears on RDR-resolved chargebacks in the dispute webhooks.

To filter by pre-disputes that are RDR-resolved, go to Dispute Search and select Visa RDR under the Pre-Dispute Program filter. The search returns all RDR pre-disputes that match the selected search criteria.


**NOTE**
 Qualifying RDR-resolved disputes do not count against the merchant's dispute ratio monitored by Visa.

 

