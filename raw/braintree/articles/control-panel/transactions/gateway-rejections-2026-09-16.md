<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/transactions/gateway-rejections -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Gateway Rejections
slug: /articles/control-panel/transactions/gateway-rejections/
createTime: '2025-04-01T23:49:35.810Z'
updateTime: '2025-04-01T23:49:35.831Z'
---



# Gateway Rejections


**NOTE**
 Gateway rejections are not the same as declines. Gateway rejections are blocked by your gateway settings, while declines are blocked by the customer's bank. [Learn more about declines.](/braintree/articles/control-panel/transactions/declines)

 

A gateway rejection indicates that a transaction or verification request did not pass certain settings or rules in your Braintree gateway. Depending on what triggered the gateway rejection, some requests are rejected before we send the information to the processor, and some are rejected after the authorization has been completed. If a transaction was authorized before being rejected, the gateway will automatically void it.


**NOTE**
 Some banks don’t acknowledge these voids right away, and others don’t acknowledge them at all. If a customer is requesting the authorization be removed, they can contact their bank to speed this process along.

 

If a transaction or verification is rejected, we’ll update the status of the request to Gateway Rejected and provide a reason for the rejection. The possible responses are:


- [Reason = 3D Secure](/braintree/articles/guides/fraud-tools/3d-secure)
- [Reason = Application Incomplete](#a-note-on-application-incomplete)
- [Reason = AVS](/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules)
- [Reason = CVV](/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules)
- [Reason = Duplicate](/braintree/articles/control-panel/transactions/duplicate-checking)
- [Reason = Fraud](/braintree/articles/guides/fraud-tools/premium/overview)
- [Reason = Risk Thresholds](/braintree/articles/guides/fraud-tools/basic/risk-threshold-rules)
- [Reason = Token Issuance](/braintree/docs/guides/venmo/server-side#gateway-rejections)
- [Reason = Payment Method Blocked](/braintree/articles/guides/payment-methods/ach)


## A note on Application Incomplete

All merchants must complete and submit their application for approval to Braintree before they can begin processing transactions. Depending on their account setup, some merchants can begin processing to a certain limit before their application has been approved. If you reach the processing limits on your provisional account, any subsequent transaction or verification attempts will be rejected with Application Incomplete until you have been approved for a full merchant account. [Contact us](https://www.braintreepayments.com/contact) if you have any questions regarding Application Incomplete rejections.

