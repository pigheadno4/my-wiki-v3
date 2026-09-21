<!-- Source URL: https://developer.paypal.com/braintree/articles/risk-and-security/chargebacks-retrievals/chargeback-reason-codes -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Chargeback Reason Codes
slug: /articles/risk-and-security/chargebacks-retrievals/chargeback-reason-codes/
createTime: '2025-04-01T22:49:01.721Z'
updateTime: '2025-09-22T15:44:30.451Z'
---


**Chargeback Reason Codes**

All received credit card disputes include a reason code. Reason codes vary by card brand. The list of chargeback reason codes in this article is organized by card brand and type of dispute.



**Please note** : Reason codes may vary depending on the region in which you process or the payment network that the payment was processed through.

This list was generated 9/22/2025 based on thechargeback reason codes actively being received and surfaced to merchants. It is subject to change and may not include every currently known dispute reason code.

[See our Automated Clearing House (ACH) support article if you are looking for ACH Return Codes.](/braintree/articles/guides/payment-methods/ach#returns)


## American Express

| Reason | Reason Code |
| --- | --- |
| cancelled_recurring_transaction | C28 |
| credit_not_processed | 175 |
| credit_not_processed | 684 |
| credit_not_processed | 4513 |
| credit_not_processed | C02 |
| credit_not_processed | C04 |
| credit_not_processed | C05 |
| credit_not_processed | C18 |
| duplicate | 173 |
| duplicate | P08 |
| fraud | 193 |
| fraud | 4540 |
| fraud | F29 |
| fraud | FR2 |
| general | M38 |
| general | R03 |
| general | R13 |
| general | S01 |
| not_recognized | 127 |
| not_recognized | 177 |
| product_not_received | 155 |
| product_not_received | 4554 |
| product_not_received | C08 |
| product_unsatisfactory | C31 |
| product_unsatisfactory | C32 |
| transaction_amount_differs | P05 |




## Diners

| Reason code | Description |
| --- | --- |
| ```syntax-inline
A02
``` | Authorization Processing Errors |
| ```syntax-inline
A06
``` | Unissued Account Number |
| ```syntax-inline
B24
``` | Charge Older than Thirty Days |
| ```syntax-inline
B25
``` | Duplicate Charge |
| ```syntax-inline
B26
``` | Alternate Settlement Currency Incorrect Exchange Rates |
| ```syntax-inline
B27
``` | Incorrect Currency |
| ```syntax-inline
C41
``` | Fraud - Card Present Transaction |
| ```syntax-inline
C42
``` | Fraud - Card Not Present Transaction |
| ```syntax-inline
C46
``` | Multiple Charges at Service Establishment Fraudulent Transaction |
| ```syntax-inline
C49
``` | Reason Code No Longer in Use |
| ```syntax-inline
C50
``` | Suspect Service Establishment – No Response to the Suspected Fraudulent Service Establishment Report |
| ```syntax-inline
C51
``` | Suspect Service Establishment – Terminated Service Establishment |
| ```syntax-inline
D61
``` | Altered Amount |
| ```syntax-inline
D62
``` | Non-Receipt of Goods or Services |
| ```syntax-inline
D65
``` | Incorrect Transaction Type |
| ```syntax-inline
D66
``` | Credit not Processed |
| ```syntax-inline
D67
``` | Cardmember Paid by Other Means |
| ```syntax-inline
D69
``` | Canceled Recurring Transactions |
| ```syntax-inline
D70
``` | Cardmember Does Not Recognize |
| ```syntax-inline
D71
``` | Non–receipt of Cash (ATM) |


## Discover

| Reason | Reason Code |
| --- | --- |
| cancelled_recurring_transaction | 4541 |
| credit_not_processed | 4550 |
| credit_not_processed | 8002 |
| duplicate | 4534 |
| duplicate | 4865 |
| fraud | 37 |
| fraud | 1040 |
| fraud | 4863 |
| fraud | 4866 |
| fraud | 6005 |
| fraud | 6040 |
| fraud | 6041 |
| fraud | 7030 |
| not_recognized | 4752 |
| not_recognized | 6021 |
| product_not_received | 4755 |
| product_unsatisfactory | 4553 |
| transaction_amount_differs | 4586 |


## Elo

| Reason | Reason Code |
| --- | --- |
| credit_not_processed | 85 |
| general | 1 |
| fraud | 7030 |
| fraud | 83 |


## Hipercard

| Reason | Reason Code |
| --- | --- |
| fraud | 4837 |


## JCB


### Retrieval reason codes

| Reason code | Description |
| --- | --- |
| ```syntax-inline
01
``` | Sales Draft (copy) |
| ```syntax-inline
02
``` | Sales Draft (original) |
| ```syntax-inline
03
``` | T&E Document (copy) |
| ```syntax-inline
04
``` | T&E Document (original) |
| ```syntax-inline
05
``` | Substitute Draft |
| ```syntax-inline
06
``` | Sales Draft (copy) + T&E Document (copy) |
| ```syntax-inline
07
``` | Sales Draft (original) + T & E Document (original) |
| ```syntax-inline
08
``` | Sales Draft (copy) + Substitute Draft |
| ```syntax-inline
09
``` | T&E Document (copy) + Substitute Draft |


### Chargeback reason codes

| Reason code | Description |
| --- | --- |
| ```syntax-inline
501
``` | Non-JCB Card |
| ```syntax-inline
502
``` | Card-Member Dispute |
| ```syntax-inline
503
``` | Expired JCB Card |
| ```syntax-inline
507
``` | Incorrect Transaction Amount |
| ```syntax-inline
510
``` | Mis-Post |
| ```syntax-inline
512
``` | Duplicate Processing |
| ```syntax-inline
513
``` | Credit Not Received |
| ```syntax-inline
516
``` | Non-Receipt of Requested Item |
| ```syntax-inline
517
``` | Requested Copy Illegible |
| ```syntax-inline
521
``` | Transaction Exceeds Floor Limit |
| ```syntax-inline
522
``` | Authorisation Declined |
| ```syntax-inline
523
``` | Incorrect Card Number |
| ```syntax-inline
524
``` | Addition Error/Transaction amount differs |
| ```syntax-inline
525
``` | Altered Amount |
| ```syntax-inline
526
``` | No Signature |
| ```syntax-inline
527
``` | No Imprint |
| ```syntax-inline
534
``` | Unauthorized Multiple Transactions |
| ```syntax-inline
536
``` | Late Submission |
| ```syntax-inline
537
``` | No Show Dispute |
| ```syntax-inline
538
``` | Advance Deposit |
| ```syntax-inline
541
``` | Illegible Item |
| ```syntax-inline
544
``` | Canceled Recurring Transaction |
| ```syntax-inline
546
``` | Unauthorized Purchase/Fraud |
| ```syntax-inline
547
``` | JCB Card on Stop List |
| ```syntax-inline
554
``` | Non-Receipt of Merchandise/Cash at ATM |
| ```syntax-inline
580
``` | Non-Receipt of T&E Documentation |
| ```syntax-inline
581
``` | Split Sale |
| ```syntax-inline
582
``` | Domestic Transaction |
| ```syntax-inline
583
``` | Paid By Other Means |


## Maestro

| Reason | Reason Code |
| --- | --- |
| fraud | 4837 |
| general | 74 |


## Mastercard

| Reason | Reason Code |
| --- | --- |
| cancelled_recurring_transaction | 41 |
| cancelled_recurring_transaction | 4841 |
| credit_not_processed | 60 |
| credit_not_processed | 4860 |
| duplicate | 34 |
| duplicate | 4834 |
| fraud | 7 |
| fraud | 37 |
| fraud | 70 |
| fraud | 81 |
| fraud | 4808 |
| fraud | 4837 |
| fraud | 4868 |
| fraud | 6000 |
| fraud | UF |
| general | 1 |
| general | 71 |
| general | 74 |
| general | 4000 |
| invalid_account | 12 |
| invalid_account | 4812 |
| not_recognized | 8 |
| product_not_received | 55 |
| product_not_received | 59 |
| product_not_received | 4555 |
| product_not_received | 4855 |
| product_unsatisfactory | 53 |
| product_unsatisfactory | 4853 |
| transaction_amount_differs | 31 |
| transaction_amount_differs | 4831 |


## UnionPay

| Reason | Reason Code |
| --- | --- |
| fraud | 6005 |
| fraud | 7030 |


## Visa

**Please note** : Since reason codes do not currently support decimals, Visa's new reason codes are represented as 4 characters with a 0 (e.g. 10.4 = 1040).

| Reason | Reason Code |
| --- | --- |
| cancelled_recurring_transaction | 41 |
| cancelled_recurring_transaction | 1320 |
| credit_not_processed | 85 |
| credit_not_processed | 136 |
| credit_not_processed | 1360 |
| credit_not_processed | 1370 |
| credit_not_processed | 4560 |
| credit_not_processed | 5000 |
| duplicate | 34 |
| duplicate | 82 |
| duplicate | 126 |
| duplicate | 1260 |
| duplicate | 1261 |
| duplicate | 1262 |
| fraud | 37 |
| fraud | 49 |
| fraud | 81 |
| fraud | 83 |
| fraud | 104 |
| fraud | 1040 |
| fraud | 1050 |
| fraud | 1340 |
| fraud | 4868 |
| fraud | 6000 |
| fraud | 6500 |
| fraud | UF |
| general | 0 |
| general | 1 |
| general | 1220 |
| general | 1230 |
| general | 1350 |
| general | 3000 |
| general | 4000 |
| general | A1 |
| general | R3 |
| invalid_account | 1240 |
| invalid_account | 1270 |
| not_recognized | 8 |
| not_recognized | 1130 |
| product_not_received | 30 |
| product_not_received | 131 |
| product_not_received | 1310 |
| product_not_received | 4555 |
| product_unsatisfactory | 53 |
| product_unsatisfactory | 1330 |
| product_unsatisfactory | 4553 |
| transaction_amount_differs | 1250 |
| transaction_amount_differs | 4586 |

