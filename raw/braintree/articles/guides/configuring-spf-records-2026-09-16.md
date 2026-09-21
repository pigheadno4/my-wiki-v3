<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/configuring-spf-records -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Configuring SPF Records
slug: /articles/guides/configuring-spf-records/
createTime: '2025-04-01T23:03:49.762Z'
updateTime: '2026-01-21T10:48:24.178Z'
---



# Configuring SPF Records


**NOTE**
Configuring Sender Policy Framework (SPF) Records is no longer required for integration.

 The [Sender Policy Framework (SPF)](http://en.wikipedia.org/wiki/Sender_Policy_Framework) was designed to prevent fraudsters from using legitimate email addresses to send spam or other fraudulent emails. An SPF record is a TXT record that allows you to specify which servers can send emails on your behalf and helps prevent these emails from getting caught in recipients’ spam folders.

Some of Braintree’s features, like [email receipts](/braintree/articles/control-panel/transactions/email-receipts) and [recurring billing notifications](/braintree/articles/guides/recurring-billing/email-notifications), can send emails to customers on your behalf. Before we can enable these features, the following steps must be completed:


- Addinclude:spf.braintreegateway.comto your SPF record
- Your full SPF record should look something like this:v=spf1 a mx include:spf.braintreegateway.com -all
- If you have more than one TXT record to add to your SPF records, include them in the same line, separated by a space:v=spf1 a mx include:otherdomain.com include:spf.braintreegateway.com -all


- [Contact us](/braintree/help?issue=EmailReceiptsHelp)to verify your SPF record has been set up correctly; you will not be able to send email receipts or notifications until you complete this step

If you're having trouble setting up your SPF record, check [Mail Tester](http://www.mail-tester.com/spf/) to see if there is a guide available for your host or registrar. For additional troubleshooting assistance, contact your website’s domain provider; the process varies depending on your provider, so they will be your best resource for updating your record.

