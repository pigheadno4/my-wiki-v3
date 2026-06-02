---
title: Settlement and transaction detail reports
slug: /docs/payouts/standard/reports/settlement-and-transaction-details/
createTime: "2024-08-15T06:06:01.276Z"
updateTime: "2025-05-12T09:07:35.524Z"
---

# Settlement and transaction detail reports

**Note:** Only approved merchants and processing partners can use the Settlement and Transaction Detail reports. Contact your PayPal account manager for more information.

The Settlement and Transaction Detail reports identify different types of payouts (Mass Payment) transactions with transaction event codes (T-codes). Payouts transactions display these T-codes:

- T0001 - Mass Payment (successful)
- T0104 - Mass Payment batch fee
- T1105 - Account hold released
- T1114 - Mass Payment reversal transaction
- T1115 - Mass Payment refund transaction
- T1503 - Temporary hold on funds during processing

While the transaction is being processed, the transaction event code is T1503 . This means PayPal placed a temporary hold on funds to reserve the total payout amount plus fees. When the batch transaction completes, the hold releases, and the transaction event code becomes T1105 .

Your PayPal account balance reflects each payment. If any payments are declined, your balance may exceed the balance shown during the hold.

You can track transactions with the Transaction ID in the PayPal Reference ID column.

## Settlement Report

The Settlement Report contains summary information for transactions that affect your PayPal balance. This report shows sent and refunded payouts. Declined payments don't appear in this report.

To access the Settlement report:

- Log in to your [PayPal business account](https://www.paypal.com) .
- Under Activity, select **All Reports** .
- Select **Transactions &gt; Settlement** .

For more information, see the [Settlement Report Specification](https://www.paypalobjects.com/webstatic/en_US/developer/docs/pdf/PP_LRD_Gen_SettlementReport.pdf) .

## Transaction Detail Report

The Transaction Detail Report contains information for transactions that affect your PayPal balance. This report shows all payouts transactions. Declined payments don't appear in this report.

To access the Transaction Detail Report:

- Log in to your [PayPal business account](https://www.paypal.com) .
- Under Activity, select **All Reports** .
- Select **Transactions &gt; Transactions detail** .

For more information, see the [Transaction Detail Report Specification](https://www.paypalobjects.com/webstatic/en_US/developer/docs/pdf/PP_LRD_Gen_TransactionDetailReport.pdf) .

**Note:** You can also access both reports from the PayPal Secure FTP Server, as described in the [Reporting FTP Server Specification](https://www.paypalobjects.com/webstatic/en_US/developer/docs/pdf/PP_LRD_SecureFTP.pdf) document.

## Additional reports

- [Search payouts transactions](/docs/payouts/standard/reports/search-transactions/)
- [View transaction activities](/docs/payouts/standard/reports/view-transaction-activities/)
