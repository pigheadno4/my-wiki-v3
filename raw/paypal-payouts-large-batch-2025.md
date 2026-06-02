<!-- Source URL: https://docs.paypal.ai/growth/payouts/send/large-batch -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Use large-batch file transfer

You can use this pattern to pay more than 15,000 people at once with a single payment file. Common use-cases for this functionality include payroll payouts, rebate payouts, reward payouts, and affiliate program payouts.

<Tip>You can send payouts to PayPal accounts and Venmo users.</Tip>

## Prerequisites

- Complete all mandatory steps to <a href="/growth/payouts/set-up#set-up-sftp-account" target="_blank" rel="noopener noreferrer">get started</a>.
- Ensure your <a href="/growth/payouts/set-up#set-up-live-account" target="_blank" rel="noopener noreferrer">PayPal business account is set up</a>.
- Ensure to <a href="/growth/payouts/set-up#fund-your-account" target="_blank" rel="noopener noreferrer">fund your business account</a>.

## Send payouts

You can use the procedures in this section to send payouts using the large-batch file transfer.

### 1. Create input file

1. **Add a summary line**: Follow <a href="#summary-line-format">the required format</a> and add a summary line as the first row of your file.
2. **Add payout records**: Follow <a href="#payout-item-row-format">the required format</a> and add each payment as a separate row.
3. Name your file using this pattern: `pp_payouts_<epoch_time>_<reference_name><format>` <br />**Example**: `pp_payouts_1728883200_batch1.csv`
   - `pp_payouts`: Always use these exact words in lowercase.
   - `<epoch_time>`: A special <a href="https://www.epochconverter.com/" target="_blank" rel="noopener noreferrer">time code</a> (from the past or up to 7 days ahead).
   - `<reference_name>`: Your chosen name using letters, numbers, underscore (\_), or hyphen (-). Maximum: 63 characters.
   - `<format>`: File type - use `.csv` or `.csv.gz`.

#### Summary line format

```csv Sample summary line theme={null}
PAYOUT_SUMMARY,1500.75,USD,5,"Thank you, ""Top Seller""!",Payout for May
```

| Field                                                                                      | Description                                                                                        | Notes                                                                                                                                                                                                                               |
| :----------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Entry type <br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>         | The first line must always contain `PAYOUT_SUMMARY`.                                               | Use uppercase only.<br /><br />**Example:** `PAYOUT_SUMMARY`                                                                                                                                                                        |
| Total payout amount<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span> | Total of all payout items.                                                                         | Must be in decimal format.<br />Currency symbols not allowed.<br />Cannot be empty or zero.<br /><br />**Example:** `1500.75`                                                                                                       |
| Currency <br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>           | Three-letter ISO 4217 currency code. Each file must contain only one currency type.                | Use separate files for different currencies.<br /><br />**Example:** `USD`<br />**Max length:** 3 characters                                                                                                                        |
| Total payments <br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>     | Total number of payout items in the file.                                                          | Use numbers only.<br /><br />**Example:** `5`                                                                                                                                                                                       |
| Email subject <br /><span style={{color: '#95a5a6', fontSize: 'smaller'}} />               | A standard subject line in the email notification sent to all recipients for each payout item.     | If text has commas or special characters, use double quotes (") around it.<br />If text has quotes, double them ("") and wrap in quotes.<br /><br />**Example:** `"Thank you, ""Top Seller""!"`<br />**Max length:** 256 characters |
| Email message <br /><span style={{color: '#95a5a6', fontSize: 'smaller'}} />               | A standard message included in the email notification sent to all recipients for each payout item. | If text has commas or special characters, use double quotes (") around it.<br />If text has quotes, double them ("") and wrap in quotes.<br /><br />**Example:** `Payout for May`<br />**Max length:** 1000 characters              |

#### Payout item row format

```csv Sample payout line items theme={null}
PAYOUT,test@paypal.com,1000.50,USD,REF_ID_1,Thanks for your work
PAYOUT_VENMO,5551232368,500.25,USD,REF_ID_2,"Congrats!"
PAYOUT,test@paypal.com,1,USD,REF_ID_1,NOTE_1,,,AWARDS
```

<Note>If you skip any optional fields, add commas to keep the columns in the correct order.</Note>

| Field                                                                                                                                                                                | Description                                                                         | Notes                                                                                                                                                                                                                               |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recipient wallet <br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>                                                                                             | Target wallet for the payout.                                                       | Use uppercase only.<br /><br />**Possible values:**<br />• `PAYOUT`<br />• `PAYOUT_VENMO`                                                                                                                                           |
| Recipient identifier <br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>                                                                                         | Identifier for the payout recipient based on the wallet type.                       | PayPal: Recipient’s PayPal-associated email address, phone number, or encrypted PayPal account number.<br />Venmo: Recipient’s US mobile number or Venmo handle.<br /><br />**Example:** `test@paypal.com`                          |
| Payout amount <br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>                                                                                                | Amount to send.                                                                     | Use decimal format only (local currency formats are not supported). Cannot be empty or zero.<br /><br />**Example:** `100.50`                                                                                                       |
| Currency <br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>                                                                                                     | Three-letter ISO 4217 currency code. Each file must contain only one currency type. | Use separate files for different currencies.<br /><br />**Example:** `USD`<br />**Max length:** 3 characters                                                                                                                        |
| Reference ID                                                                                                                                                                         | Unique identifier for each payout item.                                             | Use letters, numbers, underscore (\_), or hyphen (-).<br /><br />**Example:** `REF_ID_1`<br />**Max length:** 30 characters                                                                                                         |
| Item-level note <br /><span style={{color: '#95a5a6', fontSize: 'smaller'}} />                                                                                                       | Custom note included in the email for each payout item.                             | If text has commas or special characters, use double quotes (") around it.<br />If text has quotes, double them ("") and wrap in quotes.<br /><br />**Example:** `Thanks for your work`<br />**Max length:** 1000 characters        |
| Social feed privacy <br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>Venmo only</span>                                                                                    | Visibility setting for the Venmo recipient’s social feed.                           | **Default value:** `PRIVATE`<br /><br />**Possible values:**<br />• `PUBLIC`<br />• `FRIENDS_ONLY`<br />• `PRIVATE`                                                                                                                 |
| Holler URL <span style={{color: '#f57c00', fontSize: 'smaller', fontWeight: 'bold'}}>Deprecated</span> <br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>Venmo only</span> | URL of a Holler sticker to include with the Venmo message.                          | **Example:** [https://example.com/sticker.png](https://example.com/sticker.png)<br />**Max length:** 151 characters                                                                                                                 |
| Logo URL <br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>Venmo only</span>                                                                                               | URL of the business logo shown in the Venmo feed.                                   | Image uploaded at the access URL must be a square image of max size 1024 × 1024 px.<br /><br />**Example:** [https://example.com/logo.png](https://example.com/logo.png)<br />**Max length:** 2000 characters                       |
| Purpose <br /><span style={{color: '#95a5a6', fontSize: 'smaller'}} />                                                                                                               | Reason for the transaction.                                                         | **Default value:** `GOODS`<br /><br />**Possible values:**<br />• `AWARDS`<br />• `PRIZES`<br />• `DONATIONS`<br />• `GOODS`<br />• `SERVICES`<br />• `REBATES`<br />• `CASHBACK`<br />• `DISCOUNTS`<br />• `NON_GOODS_OR_SERVICES` |

### 2. Upload input file

<Note>You can use your Sandbox DropZone credentials, log into the DropZone account, test your file upload, and rectify errors if any. You can then use your Production DropZone credentials and upload your file for payouts.</Note>

1. Connect to PayPal’s DropZone on the SFTP server using your <a href="/growth/payouts/set-up#set-up-sftp-account" target="_blank" rel="noopener noreferrer">SFTP login details</a>.
2. Go to the `Incoming` folder on the server and upload your file. PayPal checks the file and creates an acknowledgement report. See <a href="#file-validation-steps-and-outcomes">File validation steps and outcomes</a>. PayPal places the report in the `Outgoing` folder.
3. Review the report to verify the file validation status.

#### Acknowledgment reports

| <span style={{textAlign: 'left', display: 'block'}}>Report</span> | <span style={{textAlign: 'left', display: 'block'}}>File name suffix</span> | <span style={{textAlign: 'left', display: 'block'}}>What it means</span> | <span style={{textAlign: 'left', display: 'block'}}>What to do</span> |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| Accepted (**ACK**)                                                | `_ack.csv`                                                                  | File is ready for processing.                                            | Wait for PayPal to process your payouts.                              |
| Not Accepted (**NACK**)                                           | `_nack.csv`                                                                 | File has errors.                                                         | Fix the errors and upload a new file with a different name.           |
| Duplicate (**DUPS**)                                              | `_dups.csv`                                                                 | File name already used.                                                  | Change the file name and upload again.                                |

**NACK report**

The NACK report consists of two types of errors lines.

- **Summary error line**
  - Columns: Entry type, Currency code, Error code, Error message

  ```csv Example theme={null}
  PAYOUT_SUMMARY,USD,INVALID_CURRENCY,Invalid currency code in line 3
  ```

- **Item-level error line**
  - Columns: Payout type, Line number, Reference ID, Error code, Error message

  ```csv Example theme={null}
  PAYOUT,3,REF_ID_1,INVALID_CURRENCY,Invalid currency code
  ```

For a complete list of possible error codes, see <a href="#file-validation-errors">File validation errors</a>.

**ACK report**

The ACK report shows:

- The date and time (in UTC) when PayPal received your file.
- Your original file name (without the ending).
- The status: `ACCEPTED_FOR_PROCESSING`.

```csv Example theme={null}
2018-02-26T05:48:53Z,pp_payouts_6627887729_testfile,ACCEPTED_FOR_PROCESSING
```

### 3. Review stage reports

As PayPal processes payouts, stage reports are saved in your `Outgoing` folder to help you track and match your payments.

| <span style={{textAlign: 'left', display: 'block'}}>Report</span> | <span style={{textAlign: 'left', display: 'block'}}>When you get it</span> | <span style={{textAlign: 'left', display: 'block'}}>What it shows</span>                                             | <span style={{textAlign: 'left', display: 'block'}}>What to do</span>   |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Part File report                                                  | After part of your file is processed.                                      | Shows results for the processed part. Large files may have multiple part files as PayPal processes them in sections. | Check each part file to track progress and fix problems as they appear. |
| Out or Interim report                                             | After your whole file is processed.                                        | Shows results for all payments in your file, including status and errors.                                            | Use this to check your records and confirm all payments were sent.      |
| Final report                                                      | 31 days after the Interim report.                                          | Shows the final status of payments that were not claimed.                                                            | Check which payments were not claimed and decide what to do next.       |

<Note>If a recipient does not claim their payment within 30 days, PayPal automatically returns the money to your account.</Note>

#### Report file format

The Part, Out or Interim, and Final reports are `.csv` files that include the following columns:

- Reference ID
- Payout item ID
- Transaction ID
- Recipient name
- Recipient identifier
- Currency code
- Payout amount
- Fee
- Total
- Transaction status
- Error enum
- Error message
- Processed time
- Claimed time (applicable for unilateral case)

```csv Sample report entries theme={null}
REF_ID_1,SX3QT8QVBVE4L,35P324312A142790D,,test-1@paypal.com,USD,4.82,0.25,5.07,UNCLAIMED,RECEIVER_UNREGISTERED,Receiver is unregistered,2018-01-16T10:33:22Z
REF_ID_2,HP3B9BRJYMKRU,1H080416VK328525U,,bjonny-us4@paypal.com,USD,4.93,0.25,5.18,SUCCESS,,,2018-01-16T10:33:20Z
REF_ID_3,BUPR735Z5CJBJ,7FB53422KY616915S,,test-3@paypal.com,USD,2.77,0.25,3.02,UNCLAIMED,RECEIVER_UNREGISTERED,Receiver is unregistered,2018-01-16T10:33:19Z
REF_ID_6,AU49JFTXWUQ8Q,7RG81691FV520321P,,test-1@paypal.com,USD,0.86,0.25,1.11,UNCLAIMED,RECEIVER_UNREGISTERED,Receiver is unregistered,2018-01-16T10:33:20Z
REF_ID_7,C5USHNEDMCXWL,,,bjonny-us9@paypal.com,USD,1.71,0,1.71,FAILED,ACCOUNT_RESTRICTED,User is restricted,2018-01-16T10:33:16Z
```

## Reference

You can use the following information to understand the file validation process and errors. You can review the errors, fix them, and upload your payout file again.

### File validation steps and outcomes

The following table summarizes the various file validation steps and the possible results:

| <span style={{textAlign: 'left', display: 'block'}}>Validation step</span> | <span style={{textAlign: 'left', display: 'block'}}>What PayPal checks</span>                                           | <span style={{textAlign: 'left', display: 'block'}}>Result</span> |
| -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| File exists                                                                | Checks if your file is in the folder.                                                                                   | `NACK` if missing                                                 |
| File not empty                                                             | Checks if your file has content and is not broken.                                                                      | `NACK` if empty or broken                                         |
| File encoding                                                              | Makes sure your file uses UTF-8 text format.                                                                            | `NACK` if wrong format                                            |
| File format                                                                | Checks for correct file type (`.csv` or `.csv.gz`) and proper columns.                                                  | `NACK` if wrong                                                   |
| File matches                                                               | Checks if summary totals match your payment details.                                                                    | `NACK` if they do not match                                       |
| File name                                                                  | Makes sure your file name follows the rules.                                                                            | `NACK` or `DUPS` if wrong                                         |
| Duplicate file                                                             | Checks if you already sent a file with this name.                                                                       | `DUPS` if already used                                            |
| Sandbox limit                                                              | Checks if you have too many items (sandbox only).                                                                       | `NACK` if too many                                                |
| Summary and line checks                                                    | Checks for: text length, valid currency, one summary only, summary in first line, correct payment count, valid purpose. | `NACK` if wrong                                                   |
| Payment details                                                            | Checks each payment line has all needed info.                                                                           | `NACK` if missing info                                            |
| Amount and currency                                                        | Makes sure amounts and currency codes are valid.                                                                        | `NACK` if wrong                                                   |

### File validation errors

The following table summarizes the file validation errors that PayPal may find in your payout file:

| <span style={{textAlign: 'left', display: 'block'}}>Error</span> | <span style={{textAlign: 'left', display: 'block'}}>Description</span>                                                                                                  |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DUPLICATE_REF_ID`                                               | Reference IDs must be unique within an input file.                                                                                                                      |
| `EMAIL_MESSAGE_EXCEEDED_MAX_SIZE`                                | The email message exceeded the maximum character limit. The limit is 1000.                                                                                              |
| `EMAIL_SUBJECT_EXCEEDED_MAX_SIZE`                                | The email subject exceeded the maximum character limit. The limit is 255.                                                                                               |
| `ENCODING_ERROR`                                                 | The payout input file is not in UTF-8 format.                                                                                                                           |
| `FILE_EMPTY_OR_CORRUPT`                                          | The payout input file is empty or corrupt and cannot be processed.                                                                                                      |
| `FILE_NOT_FOUND`                                                 | The file does not exist in the source folder. Contact our customer support.                                                                                             |
| `FILE_SIZE_ERROR`                                                | The payout input file is empty.                                                                                                                                         |
| `GZ_FILE_CORRUPT_ERROR`                                          | The payout input file is corrupt or has a checksum issue.                                                                                                               |
| `INVALID_CURRENCY`                                               | The currency code is invalid.                                                                                                                                           |
| `INVALID_FILE_FORMAT`                                            | The input file contains characters, columns, or details that are not required for processing payouts. Remove these characters, columns, or details and upload the file. |
| `INVALID_FILE_NAME`                                              | The format of the file name is invalid.                                                                                                                                 |
| `INVALID_FIRST_COLUMN`                                           | The first column entry in the summary must be `PAYOUT_SUMMARY`. For an item record, this must be `PAYOUT`.                                                              |
| `INVALID_REF_ID_FORMAT`                                          | The reference ID must be alphanumeric. The maximum character limit is 63.                                                                                               |
| `INVALID_SUMMARY_LINE_POSITION`                                  | The payout summary record is missing from the first line in the payout input file.                                                                                      |
| `MANDATORY_COLUMN_MISSING`                                       | The file is missing mandatory columns. Please enter the required information and retry the Payout.                                                                      |
| `MULTI_CURRENCY_NOT_SUPPORTED`                                   | The payout input file has more than one currency.                                                                                                                       |
| `MULTIPLE_SUMMARY_RECORDS`                                       | The payout input file should contain only one summary record.                                                                                                           |
| `PAYOUT_AMOUNT_INVALID_FORMAT`                                   | The payout amount must use a decimal. Other special characters are not allowed.                                                                                         |
| `PAYOUT_AMOUNT_NON_POSITIVE`                                     | The payout amount must be greater than zero.                                                                                                                            |
| `SANDBOX_LIMIT_ERROR`                                            | The number of items in the file exceeds the sandbox file limit (sandbox only).                                                                                          |
| `SCHEDULED_TIME_ERROR`                                           | The payout can be scheduled a maximum of seven days in advance.                                                                                                         |
| `SUMMARY_AMOUNT_INVALID_FORMAT`                                  | The summary amount must be a decimal. Other special characters are not allowed.                                                                                         |
| `SUMMARY_AMOUNT_NON_POSITIVE`                                    | The total payout amount in the summary line must be greater than zero.                                                                                                  |
| `SUMMARY_AND_PAYOUT_MATCH_CONFLICT`                              | The payout amount in the summary line does not match the total item value.                                                                                              |
| `SUMMARY_LINES_NON_INTEGER`                                      | The total number of payments field in the summary line must be an integer.                                                                                              |
| `SUMMARY_LINES_NON_POSITIVE`                                     | The total number of payments field in summary line must be greater than zero.                                                                                           |
| `SUMMARY_MISSING`                                                | The summary line is missing from the payout input file.                                                                                                                 |
| `TOTAL_PAYMENTS_MISMATCH`                                        | The `TOTAL_NO_OF_PAYMENTS` in the `PAYOUTS_SUMMARY` row must match the total records in the payout input file.                                                          |
| `INVALID_PURPOSE`                                                | The purpose specified for the transaction is invalid.                                                                                                                   |
