---
title: File validation errors
slug: /docs/payouts/standard/large-batch/file-validation-errors/
createTime: "2024-08-15T07:56:52.536Z"
updateTime: "2024-09-23T20:24:52.770Z"
---

# File validation errors

These errors may occur when Payouts validates your input file. Once you've fixed the errors, retry the payout:

| Error                             | Description                                                                                                                                                             |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DUPLICATE_REF_ID                  | Reference IDs must be unique within an input file.                                                                                                                      |
| EMAIL_MESSAGE_EXCEEDED_MAX_SIZE   | The email message exceeded the maximum character limit. The limit is 1000.                                                                                              |
| EMAIL_SUBJECT_EXCEEDED_MAX_SIZE   | The email subject exceeded the maximum character limit. The limit is 255.                                                                                               |
| ENCODING_ERROR                    | The payout input file is not in UTF-8 format.                                                                                                                           |
| FILE_EMPTY_OR_CORRUPT             | The payout input file is empty or corrupt and cannot be processed.                                                                                                      |
| FILE_NOT_FOUND                    | The file has been removed from the source folder. Contact our customer support.                                                                                         |
| FILE_SIZE_ERROR                   | The payout input file is empty.                                                                                                                                         |
| GZ_FILE_CORRUPT_ERROR             | The payout input file is corrupt or has a checksum issue.                                                                                                               |
| INVALID_CURRENCY                  | The currency code is invalid.                                                                                                                                           |
| INVALID_FILE_FORMAT               | The input file contains characters, columns, or details that are not required for processing payouts. Remove these characters, columns, or details and upload the file. |
| INVALID_FILE_NAME                 | The format of the file name is invalid.                                                                                                                                 |
| INVALID_FIRST_COLUMN              | The first column entry in the summary must bePAYOUT_SUMMARY. For an item record, this must bePAYOUT.                                                                    |
| INVALID_REF_ID_FORMAT             | The reference ID must be alphanumeric. The maximum character limit is 63.                                                                                               |
| INVALID_SUMMARY_LINE_POSITION     | The payout summary record is missing from the first line in the payout input file.                                                                                      |
| MANDATORY_COLUMN_MISSING          | The file is missing mandatory columns. Please enter the required information and retry the Payout.                                                                      |
| MULTI_CURRENCY_NOT_SUPPORTED      | The payout input file has more than one currency.                                                                                                                       |
| MULTIPLE_SUMMARY_RECORDS          | The payout input file should contain only one summary record.                                                                                                           |
| PAYOUT_AMOUNT_INVALID_FORMAT      | The payout amount must use a decimal. Other special characters aren't allowed.                                                                                          |
| PAYOUT_AMOUNT_NON_POSITIVE        | The payout amount must be greater than zero.                                                                                                                            |
| SANDBOX_LIMIT_ERROR               | The number of items in the file exceeds the sandbox file limit (sandbox only).                                                                                          |
| SCHEDULED_TIME_ERROR              | The payout can be scheduled a maximum of seven days in advance.                                                                                                         |
| SUMMARY_AMOUNT_INVALID_FORMAT     | The summary amount must be a decimal. Other special characters aren't allowed.                                                                                          |
| SUMMARY_AMOUNT_NON_POSITIVE       | The total payout amount in the summary line must be greater than zero.                                                                                                  |
| SUMMARY_AND_PAYOUT_MATCH_CONFLICT | The payout amount in the summary line doesn’t match the total item value.                                                                                               |
| SUMMARY_LINES_NON_INTEGER         | The total number of payments field in the summary line must be an integer.                                                                                              |
| SUMMARY_LINES_NON_POSITIVE        | The total number of payments field in summary line must be greater than zero.                                                                                           |
| SUMMARY_MISSING                   | The summary line is missing from the payout input file.                                                                                                                 |
| TOTAL_PAYMENTS_MISMATCH           | TheTOTAL_NO_OF_PAYMENTSin thePAYOUTS_SUMMARYrow must match the total records in the payout input file.                                                                  |
| INVALID_PURPOSE                   | The purpose specified for the transaction is invalid.                                                                                                                   |

## See also

- [Payouts reference](/docs/payouts/standard/reference/)
- [Payout reports](/docs/payouts/standard/reports/)
