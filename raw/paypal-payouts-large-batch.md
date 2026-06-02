---
title: Large Batch
slug: /docs/payouts/standard/large-batch/
createTime: "2024-08-15T06:17:48.690Z"
updateTime: "2025-05-12T15:57:08.966Z"
---

# Large Batch

Large batch payouts help you send payouts to an unlimited amount of recipients at once. Large batch payouts are recommended for more than 15,000 payouts in one batch. For fewer payouts in a batch, use [Standard Payouts](/docs/payouts/standard/) or [Payouts Web](/docs/payouts/standard/payouts-web/) .

## How it works

![How,large,batch,payouts,work](assets/paypal-payouts-flow-sftp.svg)

- Create a payouts input file and share it in a folder tied to your account on PayPal's secure DropZone server.

- Payouts validates the input file and returns one of the following reports:

- ACK (acknowledgment) report. The file passed validations. PayPal begins processing the file.
- NACK (negative acknowledgement) report. The file failed validations, and the report explains the errors.
- DUPS (duplicate filenames) report. The file name is identical to a previous file.

- Large files are processed in parts of up to 500,000 individual records. After each part of the input file is processed, payouts provides a Part File report. When the entire file is processed, you receive an Out File report. The reports are available in your DropZone account.

  **Note** : After 30 days, you receive a Final report that contains the status for each individual record.

- Recipients are notified of the payout.

## 1. Set up DropZone account

You can choose to first test your integration in the PayPal sandbox and send mock payouts or go straight to production and send live payouts. Follow the steps to set up a [sandbox environment](#sandbox-environment) or [production environment](#production-environment) .

### Sandbox environment

Use the PayPal sandbox to:

- Simulate file transfer to a designated folder on PayPal’s DropZone server via SFTP.
- Validate the file name, file format, checksum and file integrity.
- Test Out File reports and reconciliations.

To set up your sandbox environment:

- Contact [PayPal](https://www.paypal-support.com/) to have your PayPal account enabled for report access.

- [Create an SFTP account](/docs/reports/sftp-reports/access-sftp-reports/) .

- To access your sandbox SFTP account, use the SFTP tool of your choice and include this information:

- Sandbox endpoint/URL: dropzone.es-ext.paypalcorp.com
- Destination host port: 22
- Sandbox user name
- Public ssh key

Next, set up your production environment to send live payouts or [create an input file](#2-create-input-file) .

### Production environment

Transactions performed in the production environment are live. Money is debited from your PayPal balance and credited to each recipient’s PayPal or Venmo account. If the recipient doesn't claim the money within 30 days from the payout date, the money is returned to your account.

**Note:** Create a new set of ssh keys for your live environment.

To set up your production environment:

- Contact [PayPal](https://www.paypal-support.com/) to have your PayPal account enabled for report access.

- [Create an SFTP account](/docs/reports/sftp-reports/access-sftp-reports/) .

- To access your production SFTP account, use the SFTP tool of your choice and include this information:

- Production endpoint/URL for the SFTP login: dropzone.paypal.com
- Destination host port: 22
- Production user name
- Public ssh key

Next, create an input file and place it in your Incoming folder.

## 2. Create input file

Create a comma separated value (.csv) input file that includes a summary line and information for each individual payout item.

The following sample .csv sends a payout to 3 PayPal recipients and 2 Venmo recipients:

**Note** : Payments to Venmo recipients require a US mobile number and information in the note .

PAYOUT_SUMMARY,17.9,USD,5,"You got paid",Payout for
PAYOUT,test-1@paypal.com,4.82,USD,REF_ID_1,NOTE_1
PAYOUT_VENMO,5551232368,4.93,USD,REF_ID_2,NOTE_2
PAYOUT_VENMO,5551232369,2.77,USD,REF_ID_3,NOTE_3
PAYOUT,test-4@paypal.com,3.51,USD,REF_ID_4,NOTE_4
PAYOUT,test-5paypal.com,1.87,USD,REF_ID_5,NOTE_5### Add Summary line
The first line of the input file must contain a PAYOUT_SUMMARY as shown in this example:

PAYOUT_SUMMARY,TOTAL_PAYOUT_AMOUNT,CURRENCY_CODE,TOTAL_NO_OF_PAYMENTS,EMAIL_SUBJECT,EMAIL_MESSAGEUse this information to complete each field of the summary:

| Field                                         | Description                                                                                                                                 |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| PAYOUT_SUMMARY                                | - Static value.                                                                                                                             |
| - Must be upper case.                         |
| TOTAL_PAYOUT_AMOUNT                           | - Value of all individual payout items.                                                                                                     |
| - Must be in decimal format.                  |
| CURRENCY_CODE                                 | - [Currency](/reference/currency-codes/) for the payout, such as USD , EUR , and so on. Only one currency type is supported per input file. |
| TOTAL_NO_OF_PAYMENTS                          | - The number of payout items in the file.                                                                                                   |
| - In the example above, the item count is 5 . |
| EMAIL_SUBJECT                                 | - The subject of the email that recipients receive as a payout notification.                                                                |

- For txt input files: - If an email subject contains a comma or other special character, enclose the subject in double quotes.
- If an email subject contains a double quote, enclose the double quote with an additional set of double quotes and enclose the subject in double quotes. Example double quote subject: "Our way of saying ""thanks"""

- Max character length: 256 |
  | EMAIL_MESSAGE | - A common note in the email notification sent to all recipients for all payout items.
- For txt input files: - If a note contains a comma or other special character, enclose the note in double quotes.
- If a note contains a double quote, enclose the double quote with an additional set of double quotes and enclose the entire note with double quotes. Example double quote note: "Our way of saying ""thanks"""

- Max character length: 1000 |

### Add individual item records

Beginning with the second line of the input file, add a record for each individual payout item as shown in this example:

PAYOUT,RECIPIENT,PAYOUT_AMOUNT,CURRENCY_CODE,UNIQUE_REF_ID, ITEM_LEVEL_NOTEUse this information to complete each field for an individual item record:

| Field                                                                                                      | Description                                                                   |
| ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| PAYOUT PAYOUT_VENMO                                                                                        | - Set to PAYOUT for a PayPal recipient or PAYOUT_VENMO for a Venmo recipient. |
| - Must be upper case.                                                                                      |
| RECIPIENT                                                                                                  | - The recipient identifier.                                                   |
| - Use the recipient's email address, phone number, Venmo handle, or their encrypted PayPal account number. |
| PAYOUT_AMOUNT                                                                                              | - Value of individual payout item.                                            |

- Only use decimal format. Localized currency formats are not supported.
- Must not be empty or a zero amount. |
  | CURRENCY_CODE | - Currency in which the payouts are sent.
- Use a single currency per input file. Multiple currencies are not supported in a single input file.
- In the example above, the currency code is USD . |
  | UNIQUE_REF_ID | - Unique identifier for a payout item.
- Must also be unique within the input file.
- Must be alphanumeric
  [ 0-9 , a-z , A-Z ]
  . Only use the underscore ( \_ ) and hyphen ( - ) as special characters.
- Maximum character length: 30 |
  | ITEM_LEVEL_NOTE | - Customized note that can be sent in email notification for every payout item.
- Use any special character or alphanumeric character.
- For txt input files: - If a note contains a comma or other special character, enclose the note in double quotes.
- If the note contains a double quote, enclose the double quote with an additional set of double quotes and enclose the entire note with double quotes. Example double quote note: "Our way of saying ""thanks"""

- Maximum character length: 1000 |
  | SOCIAL_FEED_PRIVACY | - Optional for Venmo only
- Controls whether a payment appears in a recipient's feed. Can be set to PUBLIC , FRIENDS_ONLY , or PRIVATE .
- PUBLIC —
  The payment displays on the recipient's public Venmo feed.
- FRIENDS_ONLY —
  The payment displays only to the recipient's Venmo friends.
- PRIVATE —
  The payment displays only on the recipient's personal feed. Defaults to PRIVATE if left blank. |
  | HOLLER_URL [DEPRECATED] | - Optional for Venmo only.
- Link to a Holler sticker.
- For Venmo recipients, the sticker displays with the payout message.
- The maximum URL lengh is 151 characters. |
  | LOGO_URL | - Optional for Venmo only.
- Link to a logo that displays as the sender's profile image in the recipient's Venmo feed.
- Used to add or update the business profile image.
- The maximum image size is 1024 x 1024 pixels.
- The image should be square.
- The maximum URL length is 2000 characters. |
  | PURPOSE(Optional) | Denotes the purpose of the transaction. The default value isGOODSif the purpose is not provided. Purpose can be set to:- AWARDS
- PRIZES
- DONATIONS
- GOODS
- SERVICES
- REBATES
- CASHBACK
- DISCOUNTS
- NON_GOODS_OR_SERVICES

**Note:**Add commas before providing the purpose value if you are sending a PayPal or a Venmo payout with no 'social_feed_privacy', 'holler_url', or 'log_url'. Example: PAYOUT,[test@paypal.com](mailto:test@paypal.com),1,USD,REF_ID_1,NOTE_1,,,,AWARDS. |

### Save input file

Use this naming convention to save the file:

pp*payouts*&lt;epoch*time&gt;*&lt;reference_name&gt;&lt;format&gt;Where pp_payouts is static and lowercase. Variable fields in the file name include:

| Field          | Description                                                                                                                                                                                                |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| epoch_time     | Use an[epoch timestamp](https://www.epochconverter.com/). Timestamps in the past are acceptable. Future timestamps must be within seven days from the time that you place the file on the DropZone server. |
| reference_name | Must be alphanumeric                                                                                                                                                                                       |

                 [0-9,a-z,A-Z]
                 . Only use the underscore (_) and hyphen (-) as special characters. Other special characters are not allowed. Maximum character length: 63 |

| format | Either.csvor.csv.gz |

## 3. Upload input file

You can upload and test your input file in your [sandbox environment](#sandbox-environment) or upload your input file to your [production environment](#production-environment) and make live payouts. Once you upload the file, Payouts validates the file.

### File validation

Payouts performs the following validations on your input file:

| Validation            | Fails if                                                                               |
| --------------------- | -------------------------------------------------------------------------------------- |
| Currency mismatch     | The input file contains more than one currency.                                        |
| Duplicate file        | The input file name isn't unique. The file can't match a previous input file name.     |
| File empty            | The file is empty or corrupt.                                                          |
| File encoding format  | The file isn't in UTF-8 format.                                                        |
| File existence        | The file doesn't exist in the source folder.                                           |
| File format           | The file contains characters, columns, or details not required for processing payouts. |
| File integrity        | The payout summary doesn't match the payout item record details.                       |
| File name             | The input file doesn't use the correct file naming convention.                         |
| Sandbox items limit   | The number of items in the file exceeds the sandbox file limit (sandbox only).         |
| Summary and line item | Any of these conditions exist: - Character length surpasses the maximum values         |

- Contains an invalid currency code
- Contains multiple summary records
- Currency field is empty or missing
- Currency uses a localized format
- Invalid payout summary format
- The file is missing a PAYOUT_SUMMARY
- The PAYOUT_SUMMARY is not in the first line of the file
- Total number of payments field is - Empty
- Mismatched to the total number of payments in the file
- Missing

- Contains an invalid purpose value. |

When the validation is complete, you receive an acknowledgment report.

### Acknowledgment reports

After Payouts validates your input file, you receive one of these acknowledgment reports:

- ACK report - Validation passed.
- NACK report - Validation failed.

#### ACK report

If your input file passes validation, Payouts places an ACK report in your Outgoing folder. The ACK report name matches the input file name, as shown in this example:

| Input file name                    | ACK report name                        |
| ---------------------------------- | -------------------------------------- |
| pp_payouts_6627887729_testfile.csv | pp_payouts_6627887729_testfile_ack.csv |

The file is formatted as follows:

DATE_TIME_STAMP_IN_UTC,ORIGINAL_FILE_NAME,ACCEPTED_FOR_PROCESSING

Where the date is the time of acknowledgment, as shown in this example:

2018-02-26T05:48:53Z,pp_payouts_6627887729_testfile,ACCEPTED_FOR_PROCESSING

When you receive an ACK report, Payouts begins processing the input file. You can then [view reports](#4-view-reports) to see the payout status.

#### NACK report

If your input file fails validation, PayPal places a NACK report in your Outgoing folder.

**Tip** : If you send a file with content that matches a file you sent within seven days, you receive a NACK file. You can contact your PayPal account manager and ask to override this feature.

The NACK report name matches the input file name:

| Input file name                    | NACK report name                        |
| ---------------------------------- | --------------------------------------- |
| pp_payouts_6627887729_testfile.csv | pp_payouts_6627887729_testfile_nack.csv |

The file contains the errors found and is formatted as follows:

| Line                    | Contents                                                  |
| ----------------------- | --------------------------------------------------------- |
| Summary line            | PAYOUT_SUMMARY,CURRENCY_CODE,ERROR_ENUM,ERROR_DESCRIPTION |
| Individual item records | PAYOUT,LINE_NO,REF_ID,ERROR_ENUM,ERROR_DESCRIPTION        |

This example shows a NACK file with errors:

PAYOUT_SUMMARY,ASD,CURRENCY_INVALID,Currency is not valid
PAYOUT_SUMMARY,USD,SUMMARY_AND_PAYOUT_MATCH_CONFLICT,Summary and Payout details must match
PAYOUT,4,fourth-ref-id,PAYOUT_AMOUNT_INVALID_FORMAT,Invalid Payout amount formatCorrect any issues. Give the corrected file a unique name and put it in your Incoming folder. Payouts validates again and sends a new ACK or NACK report to your Outgoing folder.

When you receive an ACK report, Payouts begins processing the input file. You can then view status reports.

For more information on errors, see [File validation errors](/docs/payouts/standard/large-batch/file-validation-errors) .

## 4. View reports

Payouts generates reports at three different file processing stages. This table describes the reports and shows the example report name for an input file named PP_PAYOUTS_1517395059_ABC123.csv :

| Report               | Description                                                                                                                                                                                                                                                                                                           | Example report name                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| Part File report     | Generated after a part of an input file is processed. In the case of multiple part files, the payout items are mutually exclusive across each part file. The Part File report contains the start and end row number in the file name. For example, if a part file name contains1_350, items1through350were processed. | PP_PAYOUTS_1517395059_ABC123_1_350.csv |
| Out / Interim report | Generated after all parts of an input file are processed.                                                                                                                                                                                                                                                             | PP_PAYOUTS_1517395059_ABC123_OUT.csv   |
| Final report         | Generated 31 days after the Interim report. Includes the final status of unclaimed transactions.                                                                                                                                                                                                                      | PP_PAYOUTS_1517395059_ABC123_FINAL.csv |

### Report format

The Part, Out/Interim, and Final reports all use the same format:

REF_ID,PAYOUT_ITEM_ID,TRANSACTION_ID,RECIPIENT_NAME,RECIPIENT,CURRENCY_CODE,PAYOUT_AMOUNT,FEE,TOTAL,TRANSACTION_STATUS,ERROR_ENUM,ERROR_MESSAGE,TIME_PROCESSED,TIME_CLAIMED[Applicable for Unilateral Case]### Sample report
REF_ID_1,SX3QT8QVBVE4L,35P324312A142790D,,test-1@paypal.com,USD,4.82,0.25,5.07,UNCLAIMED,RECEIVER_UNREGISTERED,Receiver is unregistered,2018-01-16T10:33:22Z
REF_ID_2,HP3B9BRJYMKRU,1H080416VK328525U,,bjonny-us4@paypal.com,USD,4.93,0.25,5.18,SUCCESS,,,2018-01-16T10:33:20Z
REF_ID_3,BUPR735Z5CJBJ,7FB53422KY616915S,,test-3@paypal.com,USD,2.77,0.25,3.02,UNCLAIMED,RECEIVER_UNREGISTERED,Receiver is unregistered,2018-01-16T10:33:19Z
REF_ID_6,AU49JFTXWUQ8Q,7RG81691FV520321P,,test-1@paypal.com,USD,0.86,0.25,1.11,UNCLAIMED,RECEIVER_UNREGISTERED,Receiver is unregistered,2018-01-16T10:33:20Z
REF_ID_7,C5USHNEDMCXWL,,,bjonny-us9@paypal.com,USD,1.71,0,1.71,FAILED,ACCOUNT_RESTRICTED,User is restricted,2018-01-16T10:33:16Z## Next
Learn about [file validation errors](/docs/payouts/standard/large-batch/file-validation-errors)
