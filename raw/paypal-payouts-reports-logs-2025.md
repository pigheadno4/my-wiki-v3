<!-- Source URL: https://docs.paypal.ai/growth/payouts/manage-payouts/reports-transaction-logs -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# View reports and transaction logs

You can access the reports and transaction logs for payouts using your PayPal business account. These reports help you monitor, download, and analyze payout activity for reconciliation, compliance, and troubleshooting.

## Generate Activity report

You can use the Activity report to get a list of all the transaction activity for your PayPal business account.

1. Log into your <a href="https://www.paypal.com" target="_blank" rel="noopener noreferrer">PayPal business account</a>.
2. Go to **Activity** > **All reports**.
3. On the All reports page, select **Activities** tab > **Activity report**.
4. On the Activity report page, choose the **Transaction type**, **Date range**, and **Format**.
5. Optional: Select **Customize report fields** to add or remove fields from the report.
6. Select **Create report**. The report appears in the Activity reports list. You will receive a notification when it is ready for download.
7. Select **Download**. The report contains the transaction details such as **Date**, **Name**, **Status**, **Transaction ID**, **Fee**, and so on.

## Generate Settlements report and Transaction details report

You can use the [Settlements report](#generate-settlements-report) and [Transaction details report](#generate-transaction-details-report) to identify different types of payout transactions using [Transaction event codes](#understand-transaction-event-codes).

### Understand transaction event codes

You can use the Transaction event codes (T-codes) to identify the type of payout transactions in your reports. For payouts, T-codes help you monitor payout transactions at every step.

| T-code  | Description                              |
| ------- | ---------------------------------------- |
| `T0001` | Mass Payment (successful)                |
| `T0104` | Mass Payment batch fee                   |
| `T1105` | Account hold released                    |
| `T1114` | Mass Payment reversal transaction        |
| `T1115` | Mass Payment refund transaction          |
| `T1503` | Temporary hold on payout amount and fees |

For example:

- `T1503`: When you start a payout, PayPal assigns this code to the transaction and places a temporary hold on the payout amount and associated fees.
- `T1105`: When the batch payout completes, PayPal changes the T-code to this value and releases the hold on the payout amount. If PayPal declines any payments, your final balance may be higher than during the hold.

### Generate Settlements report

You can use the Settlements report to view a summary of transactions that affect your PayPal balance. It includes details of sent and refunded payouts but excludes declined payments.

1. <a href="https://www.paypal-support.com/" target="_blank" rel="noopener noreferrer">Contact PayPal</a> to enable the Settlements report access for your PayPal business account.
2. After you get the report access, log into your <a href="https://www.paypal.com" target="_blank" rel="noopener noreferrer">PayPal business account</a>.
3. Go to **Activity** > **All reports**.
4. On the All reports page, select **Payments** tab > **Settlements report**.
5. Set the date range and filters.
6. Download the report as a `.csv` or `.tsv` file.
7. In the downloaded report, you can:
   - Use the **Transaction ID** from the [Activity report](#generate-activity-report) to filter the **PayPal Reference ID** column and track specific transactions.
   - Use the T-codes in the **Transaction Event Code** column to find the type of payout transaction. For more information about T-codes, see [Understand transaction event codes](#understand-transaction-event-codes).

For more information, see the <a href="https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/" target="_blank" rel="noopener noreferrer">Settlement Report Specification</a>.

### Generate Transaction details report

You can use the Transaction details report to view a summary of transactions that affect your PayPal balance. It includes details of all payout transactions but excludes declined payments.

1. <a href="https://www.paypal-support.com/" target="_blank" rel="noopener noreferrer">Contact PayPal</a> to enable the Transaction details report access for your PayPal business account.
2. After you get the report access, log into your <a href="https://www.paypal.com" target="_blank" rel="noopener noreferrer">PayPal business account</a>.
3. Go to **Activity** > **All reports**.
4. On the All reports page, select **Payments** tab > **Transaction details report**.
5. Download the report as a `.csv` or `.tsv` file.
6. In the downloaded report, you can:
   - Use the **Transaction ID** from the [Activity report](#generate-activity-report) to filter the **PayPal Reference ID** column and track specific transactions.
   - Use the T-codes in the **Transaction Event Code** column to find the type of payout transaction. For more information about T-codes, see [Understand transaction event codes](#understand-transaction-event-codes).

For more information, see the <a href="https://developer.paypal.com/docs/reports/sftp-reports/transaction-detail/" target="_blank" rel="noopener noreferrer">Transaction Detail Report Specification</a>.

## Access stage reports for large-batch file transfer

PayPal provides the <a href="/growth/payouts/send-money/use-large-batch-file-transfer#3-review-stage-reports" target="_blank" rel="noopener noreferrer">stage reports</a> for payouts made through large-batch file transfer.

To access these reports:

1. Connect to the DropZone SFTP server using your credentials.
2. Go to the `Outgoing` folder on PayPal's DropZone SFTP server.
3. Download the report files in `.csv` format.

## View transaction log

1. Log into your <a href="https://www.paypal.com" target="_blank" rel="noopener noreferrer">PayPal business account</a>.
2. You can view the transaction log using one of these ways:
   - Go to **Activity** > **All transactions**.
   - From the dashboard, go to **Recent activity** section > select **View Activity**.
3. On Transactions page, select **Filter**.
4. Choose **Payouts** as the **Transaction type**.
5. Select the date range. By default, the Transactions page displays a list of transactions from last 30 days. You can view payout transactions for any date range in the last three years.
6. Optional: Adjust other search filters.
7. Select **Apply filters**. The search results display transaction list that matches your criteria, showing:
   - Date
   - Type
   - Name
   - Status
   - Gross Amount
   - Fee
   - Net Amount
8. Select the payout transaction you want to review.
9. On the Transaction details page, you can review the payout details.
10. Select **Download (CSV)** or **Download (TXT)** to download the payment log and view all the individual payment details. If the payout required currency conversion, the log includes the exchange rate, fee, and total amount in both currencies.

Transaction logs also include error and reason codes. For more information, see [Review error and reason codes](#review-error-and-reason-codes).

### Review error and reason codes

The following errors may occur when PayPal processes your payouts. After you review and fix the errors, retry the payout.

| Reason  | Error code                                                  | Description                                                                                                                                                                                                                                                                                           |
| ------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `400`   | `ITEM_ALREADY_CANCELLED`                                    | Requested item is already cancelled.                                                                                                                                                                                                                                                                  |
| `400`   | `ITEM_CANCELLATION_FAILED`                                  | Requested item is already cancelled.                                                                                                                                                                                                                                                                  |
| `400`   | `ITEM_INCORRECT_STATUS`                                     | You can only cancel items that are in `UNCLAIMED` state.                                                                                                                                                                                                                                              |
| `400`   | `USER_BUSINESS_ERROR`                                       | A business error occurred for the user.                                                                                                                                                                                                                                                               |
| `403`   | `REQUIRED_SCOPE_MISSING`                                    | Access token does not have the required scope.                                                                                                                                                                                                                                                        |
| `403`   | `SENDER_ACCOUNT_UNVERIFIED`                                 | Verify your account to send a payout. To verify your account, confirm your bank account or credit card. For assistance, contact your account manager or <a href="https://www.paypal.com/in/smarthelp/contact-us" target="_blank" rel="noopener noreferrer">customer support</a>.                      |
| `429`   | `RATE_LIMIT_VALIDATION_FAILURES`                            | Request blocked due to multiple failed attempts. Try again later.                                                                                                                                                                                                                                     |
| `504`   | `REQUEST_TIMEOUT_EXCEEDED`                                  | System did not respond within the timeout period. Try again later.                                                                                                                                                                                                                                    |
| `1000`  | `UNDEFINED`                                                 | An error occurred while processing this payout request. Try again later or make a new request.                                                                                                                                                                                                        |
| `1002`  | `INSUFFICIENT_FUNDS`                                        | To complete the payout transaction, add money to your account.                                                                                                                                                                                                                                        |
| `1003`  | `USER_COUNTRY_NOT_ALLOWED`                                  | Payouts not allowed in the country mentioned in your address. For assistance, contact your account manager or <a href="https://www.paypal.com/in/smarthelp/contact-us" target="_blank" rel="noopener noreferrer">customer support</a>.                                                                |
| `1004`  | `USER_FUNDING_SOURCE_INELIGIBLE`                            | Funding source for this transaction is not allowed. Try again using your PayPal balance.                                                                                                                                                                                                              |
| `1005`  | `PENDING_RECIPIENT_NON_HOLDING_CURRENCY_PAYMENT_PREFERENCE` | Transaction is pending because the recipient has set their account preferences to review credits in this currency. PayPal has notified the recipient. Check the payout status later.                                                                                                                  |
| `3004`  | `SELF_PAY_NOT_ALLOWED`                                      | You cannot send a payout to yourself. Try sending it to a different account.                                                                                                                                                                                                                          |
| `3014`  | `SENDER_ACCOUNT_LOCKED`                                     | Account locked or inactive. Cannot send a payout now, For assistance, contact your account manager or <a href="https://www.paypal.com/in/smarthelp/contact-us" target="_blank" rel="noopener noreferrer">customer support</a>.                                                                        |
| `3015`  | `RECEIVER_ACCOUNT_LOCKED`                                   | Recipient's account locked or inactive. Cannot send a Payouts now. Money returned to your account.                                                                                                                                                                                                    |
| `3017`  | `SPENDING_LIMIT_EXCEEDED`                                   | Exceeded your spending limit. For assistance, contact your account manager or <a href="https://www.paypal.com/in/smarthelp/contact-us" target="_blank" rel="noopener noreferrer">customer support</a>.                                                                                                |
| `3047`  | `ACCOUNT_RESTRICTED`                                        | Restricted account access. For assistance, contact your account manager or <a href="https://www.paypal.com/in/smarthelp/contact-us" target="_blank" rel="noopener noreferrer">customer support</a>.                                                                                                   |
| `3078`  | `NEGATIVE_BALANCE`                                          | Insufficient amount in your PayPal balance. Add funds to your account to complete the payout.                                                                                                                                                                                                         |
| `3107`  | `REFUSED_RECEIVER_REFUSED`                                  | Recipient refused payout in this currency. Try resending in a different currency.                                                                                                                                                                                                                     |
| `3141`  | `REFUSED_ACTION_DENIED`                                     | Access denied. This merchant cannot use the send money option.                                                                                                                                                                                                                                        |
| `3148`  | `RECEIVER_COUNTRY_NOT_ALLOWED`                              | PayPal cannot send this payout because the recipient lives in a country where Payouts are not allowed.                                                                                                                                                                                                |
| `3501`  | `INVALID_EMAIL_ID`                                          | Email ID entered for this recipient is invalid.                                                                                                                                                                                                                                                       |
| `3547`  | `SENDER_STATE_RESTRICTED`                                   | Cannot send this transaction since your address is in a restricted state.                                                                                                                                                                                                                             |
| `3558`  | `RECEIVER_STATE_RESTRICTED`                                 | Cannot send this transaction because the recipient lives in a state where Payouts are not allowed.                                                                                                                                                                                                    |
| `3769`  | `CLOSED_MARKET`                                             | Account is not allowed to receive Payouts from other countries. Try resending this payout to another account.                                                                                                                                                                                         |
| `4002`  | `INTERNAL_ERROR`                                            | Internal error occurred during payout request processing. Retry this payout as a new batch or file.                                                                                                                                                                                                   |
| `8304`  | `ACCOUNT_UNCONFIRMED_EMAIL`                                 | Verify your PayPal account to send Payouts. To verify your account, confirm your email and your bank account or credit card. For assistance, contact your account manager or <a href="https://www.paypal.com/in/smarthelp/contact-us" target="_blank" rel="noopener noreferrer">customer support</a>. |
| `8319`  | `ZERO_AMOUNT`                                               | Provide a valid payment amount.                                                                                                                                                                                                                                                                       |
| `8330`  | `RECEIVING_LIMIT_EXCEEDED`                                  | Recipient cannot accept this Payouts because it exceeds the amount they can receive at this time. Resubmit your payout request for a different amount.                                                                                                                                                |
| `8331`  | `DUPLICATE_ITEM`                                            | Duplicate transaction in the batch. Check the reference ID and sender ID.                                                                                                                                                                                                                             |
| `9302`  | `RISK_DECLINE`                                              | Transaction declined due to risk concerns.                                                                                                                                                                                                                                                            |
| `9500`  | `GAMER_FAILED_COUNTRY_OF_RESIDENCE_CHECK`                   | Recipient lives in a country that is not allowed to accept this Payouts transaction.                                                                                                                                                                                                                  |
| `9501`  | `GAMER_FAILED_FUNDING_SOURCE_CHECK`                         | Funding source that was selected for this payout is not allowed. Try again using your PayPal balance.                                                                                                                                                                                                 |
| `9502`  | `GAMING_INVALID_PAYMENT_FLOW`                               | Payment flow is not allowed for gaming merchant accounts.                                                                                                                                                                                                                                             |
| `11711` | `TRANSACTION_LIMIT_EXCEEDED`                                | Payouts request exceeds the limit for this type of transaction. The money has been returned to your account.                                                                                                                                                                                          |
| `14159` | `CURRENCY_NOT_SUPPORTED_FOR_RECEIVER`                       | Recipient's account does not support this currency. Resend this payout with a different currency.                                                                                                                                                                                                     |
| `14550` | `CURRENCY_COMPLIANCE`                                       | Transaction not allowed, due to currency compliance regulations.                                                                                                                                                                                                                                      |
| `14763` | `REGULATORY_PENDING`                                        | Transaction is pending while it is reviewed for compliance with government regulations.                                                                                                                                                                                                               |
| `14764` | `REGULATORY_BLOCKED`                                        | Transaction blocked due to regulatory compliance restrictions.                                                                                                                                                                                                                                        |
| `14765` | `RECEIVER_UNREGISTERED`                                     | Recipient for this payout does not have an account. Sent a sign up link to the recipient. However, if the recipient does not claim this Payouts amount within 30 days, money returns to your account.                                                                                                 |
| `14766` | `RECEIVER_UNCONFIRMED`                                      | Recipient's email or phone number is unconfirmed. Until the recipient confirms their account information, payments made to this account will be marked `UNCLAIMED`. Money will be returned to your account if they are not claimed within 30 days.                                                    |
| `14767` | `RECEIVER_YOUTH_ACCOUNT`                                    | Unable to send Payouts because the recipient has a youth account. Check with the recipient for an alternate account to receive the money.                                                                                                                                                             |
| `14776` | `TRANSACTION_DECLINED_BY_TRAVEL_RULE`                       | An error occurred while processing this payout request. Try resending as part of a new request or file later. For assistance, contact your account manager or <a href="https://www.paypal.com/in/smarthelp/contact-us" target="_blank" rel="noopener noreferrer">customer support</a>.                |
| `14800` | `POS_LIMIT_EXCEEDED`                                        | You have exceeded the POS cumulative spending limit. For assistance, contact your account manager or <a href="https://www.paypal.com/in/smarthelp/contact-us" target="_blank" rel="noopener noreferrer">customer support</a>.                                                                         |
| `14801` | `UNVERIFIED_RECIPIENT_NOT_SUPPORTED`                        | Payout request incomplete because of unverified recipient account. Your account can send Payouts only to verified accounts.                                                                                                                                                                           |
| `14802` | `NON_HOLDING_CURRENCY`                                      | No PayPal balance in this currency. Try again with a currency that has money in your PayPal account, or change your account settings to this currency.                                                                                                                                                |
