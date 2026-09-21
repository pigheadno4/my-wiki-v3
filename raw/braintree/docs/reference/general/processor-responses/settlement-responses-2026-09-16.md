<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/general/processor-responses/settlement-responses -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Settlement
slug: /docs/reference/general/processor-responses/settlement-responses/
createTime: '2025-04-02T01:50:04.463Z'
updateTime: '2025-04-02T01:50:04.479Z'
---



# Settlement

4000-class codes indicate the success or failure of the request to capture the funds. Based on the
processor response we receive, we will update the[transaction status](/braintree/docs/reference/general/statuses#transaction)accordingly.
## Approvals

| Code | Text |
| --- | --- |
| 4000 | Settled |


## Pending requests

| Code | Text |
| --- | --- |
| 4002 | Settlement Pending |


## Declines

| Code | Text | Explanation |
| --- | --- | --- |
| 4001 | Settlement Declined | The processor declined to settle the sale or refund request. |
| 4003 | Already Captured | The transaction has already been fully captured. |
| 4004 | Already Refunded | The transaction has already been fully refunded. |
| 4005 | PayPal Risk Rejected | The sale request was rejected by PayPal risk. |
| 4006 | Capture Amount Exceeded Allowable Limit | The specified capture amount exceeded the amount allowed by the processor. |
| 4018 | PayPal Pending Payments Not Supported | PayPal returned a pending sale or refund response which is disallowed by Braintree. This failure is likely due to a misconfiguration in your PayPal account. Further details may be found in the transaction details. |
| 4019 | PayPal Refund Transaction with an Open Case Not Allowed | PayPal declined to settle the refund request as there is an open dispute against the transaction. If you have enabled PayPal disputes within Braintree, you may resolve the dispute within the Braintree disputes dashboard. Otherwise, you may do so via your PayPal account's Resolution Center. |
| 4020 | PayPal Refund Attempt Limit Reached | PayPal's maximum number of refund attempts for this transaction has been exceeded. |
| 4021 | PayPal Refund Transaction Not Allowed | PayPal does not allow you to refund this type of transaction. |
| 4022 | PayPal Refund Invalid Partial Amount | The partial refund amount is not valid. |
| 4023 | PayPal Refund Merchant Account Missing ACH | Your PayPal account does not have an associated verified bank account. |
| 4024 | Refund Time Limit Exceeded | PayPal requires that refunds are issued within 180 days of the sale. This refund can't be successfully processed. |
| 4025 | Payer Account Is Locked Or Closed | The customer’s PayPal account can't be used for transactions at this time. The customer will need to[contact PayPal's Support team](/braintree/articles/guides/payment-methods/paypal/setup-guide#contacting-paypal-support)for more information or use a different payment method. |
| 4026 | PayPal or Venmo account not configured to refund more than settled amount | Your PayPal or Venmo account is not set up to refund amounts higher than the original transaction amount.[Contact PayPal's Support team](/braintree/articles/guides/payment-methods/paypal/setup-guide#contacting-paypal-support)for information on how to enable this for your PayPal account. |

