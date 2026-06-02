<!-- Source URL: https://docs.paypal.ai/growth/payouts/send/web-ui -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Web UI

You can use this pattern to send up to 5,000 payouts at once by uploading a `.csv` file in your PayPal business account dashboard. You can send batch payouts without writing code or setting up servers.

<Tip>You can send payouts to PayPal accounts and Venmo users.</Tip>

## Prerequisites

- Complete all mandatory steps to <a href="/growth/payouts/set-up#set-up-business-account-for-web-ui-file-upload" target="_blank" rel="noopener noreferrer">get started</a>.
- Ensure your <a href="/growth/payouts/set-up#set-up-live-account" target="_blank" rel="noopener noreferrer">PayPal business account is set up</a>.
- Ensure to <a href="/growth/payouts/set-up#fund-your-account" target="_blank" rel="noopener noreferrer">fund your business account</a>.

## Send payouts

You can use the procedures in this section to send payouts using the Payouts Web UI.

### 1. Create input file

Create a `.csv` file and add payout records as line items. Use the following format and add each payout you want to send as a separate row. You can add a maximum of 5000 rows.

#### Sample payout line items

```csv Example file 1 - Pay PayPal and Venmo recipients in US from your US business account theme={null}
mbrown@email.com,100.5,USD,ID001,Here is your payment,PAYPAL
jdoe@venmo.com,100.5,USD,,Here is your payment,VENMO,FRIENDS_ONLY
```

```csv Example file 2 - Pay a recipient in Germany from your US business account theme={null}
mbrown@myco.com,"100,50",EUR,ID001,Here is your payment,PAYPAL
```

| Field                                                                                                                                                                                 | Description                                                                         | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recipient identifier <br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>                                                                                          | Identifier for the payout recipient based on the wallet type.                       | PayPal: Recipient's PayPal-associated email address or PayPal PayerID (retrieved through PayPal Checkout or Assisted Account Creation).<br />Venmo: Recipient's US mobile number or Venmo handle.<br /><br />**Examples:** `mbrown@email.com`, `jdoe@venmo.com`, `mbrown@myco.com`                                                                                                                                                                          |
| Payment amount <br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>                                                                                                | Amount to send.                                                                     | For currencies that use a comma, enclose the amount in double quotes. PayPal validates the format on upload.<br /><br />**Example:** `100.5` or `"100,50"`                                                                                                                                                                                                                                                                                                  |
| Currency <br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>                                                                                                      | Three-letter ISO 4217 currency code. Each file must contain only one currency type. | Use separate files for different currencies. To pay recipients in the local currency, group the recipients by their currency type and create one file for each payout currency. For more information, see <a href="/growth/payouts/customize/customize-web-ui-payouts#pay-recipients-in-their-local-currency" target="_blank" rel="noopener noreferrer">Pay in local currency</a>.<br /><br />**Example:** `USD` or `EUR`<br />**Max length:** 3 characters |
| Customer ID                                                                                                                                                                           | Unique recipient identifier.                                                        | No spaces allowed. Use double quotes if value contains commas.<br /><br />**Example:** `ID001`<br />**Max length:** 30 characters                                                                                                                                                                                                                                                                                                                           |
| Note to recipient <br /><span style={{color: 'red', fontSize: 'smaller'}}>Required for Venmo</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>Optional for PayPal</span> | Custom message sent to the recipient.                                               | PayPal: Overrides the default message set in the PayPal UI, if provided.<br />Venmo: A message must be included for each recipient. The message inherits the recipient’s privacy setting.<br /><br />**Example:** `Here is your payment`<br />**Max length:** 400 characters                                                                                                                                                                                |
| Recipient wallet <br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>                                                                                              | Target wallet for the payout.                                                       | **Default value:** `PAYPAL`<br /><br />**Possible values:**<br />• `PAYPAL`<br />• `VENMO`                                                                                                                                                                                                                                                                                                                                                                  |
| Social feed privacy <br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>Venmo only</span>                                                                                     | Visibility setting for the Venmo recipient’s social feed.                           | **Default value:** `PRIVATE`<br /><br />**Possible values:**<br />• <code>PUBLIC</code><br />• <code>FRIENDS_ONLY</code><br />• <code>PRIVATE</code>                                                                                                                                                                                                                                                                                                        |
| Holler URL <span style={{color: '#f57c00', fontSize: 'smaller', fontWeight: 'bold'}}>Deprecated</span> <br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>Venmo only</span>  | URL of a Holler sticker to include with the Venmo message.                          | **Example:** [https://example.com/sticker.png](https://example.com/sticker.png)<br />**Max length:** 151 characters                                                                                                                                                                                                                                                                                                                                         |
| Logo URL <br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>Venmo only</span>                                                                                                | URL of the business logo shown in the Venmo feed.                                   | Image uploaded at the access URL must be a square image of max size 1024 × 1024 px.<br /><br />**Example:** [https://example.com/logo.png](https://example.com/logo.png)<br />**Max length:** 2000 characters<br />                                                                                                                                                                                                                                         |
| Purpose                                                                                                                                                                               | Reason for the transaction.                                                         | **Default value:** `GOODS`<br /><br />**Possible values:**<br />• `AWARDS`<br />• `PRIZES`<br />• `DONATIONS`<br />• `GOODS`<br />• `SERVICES`<br />• `REBATES`<br />• `CASHBACK`<br />• `DISCOUNTS`<br />• `NON_GOODS_OR_SERVICES`                                                                                                                                                                                                                         |

#### CSV file format specifications

Use the following specifications to ensure your payout file meets the required format and is accepted:

- Use a period (`.`) as the decimal separator for currencies like U.S. dollars (USD), Canadian dollars (CAD), and British pounds (GBP). For example: `100.5`.
- Use a comma (`,`) for currencies such as euros (EUR) and Brazilian reais (BRL), and enclose the amount in double quotes. For example: `"100,50"`.
- Each file must contain only one currency. For multi-currency payouts, upload a separate file per currency.
- Preserve the defined column order and ensure all rows include the same number of columns. Leave optional fields blank if not used and do not remove them.
- Add one row per recipient, adhering to the exact column structure.
- Wrap values containing commas or special characters in double quotes. For example, `"100,50"` or `"Custom Message with Comma, Here"`.

### 2. Upload input file

<Note>You can upload a sample input file in your sandbox account, test the payout, and then move to production.</Note>

1. Log in to your PayPal account.
2. Go to **Business Tools** > **Make Payments** > **Payouts** > **Get Started**.
3. On the Send a Mass Payment page:
   - Go to **Choose File** to select your `.csv` payment file.
   - Select **Open** to upload it.
4. (Optional) Enter additional details:
   - **Email subject:** Appears in the recipient’s email.
   - **Custom message for recipient:** Overrides the default message (applies to PayPal payouts only).
5. Review the consent statement and select the checkbox to acknowledge it.
6. Select **Continue**. PayPal validates your file and displays a Review Your Payments Details page.
7. Select **Send Payout** to submit the file. If you have set up a payout approval flow for your business account, PayPal sends the payout for approval and an approver must approve it. See <a href="/growth/payouts/customize/customize-web-ui-payouts#set-up-payout-approval-flow" target="_blank" rel="noopener noreferrer">Set up payout approval flow</a>.
8. After submission, select one of the following:
   - **Send another payout:** Process a new `.csv` file.
   - **View activity details:** Check payment status and transaction details.

<Note>If you reupload the same file within 30 days, PayPal shows a duplicate warning.</Note>

### 3. Track and manage payouts

You can:

- Monitor the status of each payment after submitting your `.csv` file.
- View payout details on the confirmation page or in the **Activity** tab of your PayPal business account dashboard.
- Download reports and transaction logs to review fees, statuses, and currency conversion details.

For more information, see <a href="/growth/payouts/manage-payouts/track-payout-item-status" target="_blank" rel="noopener noreferrer">Track payout item status</a>.

### 4. Go live

If you tested an input file in sandbox and the payout is successful:

1. Modify your input file to reflect actual payouts.
2. Go to your live account and upload the input file.
