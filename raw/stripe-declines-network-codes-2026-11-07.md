<!-- Source URL: https://docs.stripe.com/declines/network-codes -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Network decline codes

Learn about network decline codes and how to resolve them when a charge fails.

Network decline codes are typically alphanumeric error codes that indicate a reason for a payment decline. These codes often come from issuing banks, payment processors, or credit networks. Use the following table to help resolve issues relating to network decline codes:

#### Payment Method - ACH Direct Debit

| Raw network code | Decline code | Explanation | Next steps |
| --- | --- | --- | --- |
| `R01`, `R09` | `insufficient_funds` | The payment process can’t be completed because your customer’s bank account doesn’t have the necessary funds. | Contact your customer to verify that they have the required funds, then retry the transaction. |
| `R02` | `bank_account_closed` | The payment can’t be processed because your customer’s bank account is closed. | Contact your customer to provide new account details, then retry the transaction. |
| `R03`, `R04` | `bank_account_invalid_details` | The transaction can’t be processed because the bank account information that your customer provided is incorrect. | Contact your customer for correct account details, then retry the transaction. |
| `R05`, `R07`, `R08`, `R10`, `R11`, `R29`, `R31` | `debit_not_authorized` | This payment doesn’t have an authorized mandate. | Collect a new mandate, then retry the transaction. |
| `R15` | `recipient_deceased` | The attempt to set up a mandate is made on the account of a potentially deceased individual. | Verify your customer’s status, then retry the transaction. |
| `R16` | `bank_account_frozen` | The payment can’t be processed because your customer’s bank account is frozen. | Contact your customer to provide new account details, then retry the transaction. |
| `R20` | `bank_account_restricted` | The payment can’t be processed because your customer’s bank has blocked direct debits, either by the bank’s actions or your customer’s. | Contact your customer to understand the reason for the block. If the bank unblocks the account, retry the transaction. |

#### Payment Method - Australia BECS Direct Debit

| Raw network code | Failure code | Explanation | Next steps |
| --- | --- | --- | --- |
| `1` | `invalid_routing_number` | The transaction can’t be processed because the routing number that your customer provided is incorrect. | Contact your customer to provide new account details, then retry the transaction. |
| `2` | `debit_not_authorized` | This payment doesn’t have an authorized mandate. | Collect a new mandate, then retry the transaction. |
| `3` | `account_closed` | The payment can’t be processed because your customer’s bank account is closed. | Contact your customer to provide new account details, then retry the transaction. |
| `4` | `recipient_deceased` | The attempt to set up a mandate is made on the account of a potentially deceased individual. | Verify your customer’s status, then retry the transaction. |
| `5` | `no_account` | The transaction can’t be processed because the bank account information that your customer provided is incorrect. | Contact your customer to provide new account details, then retry the transaction. |
| `6` | `refer_to_customer` | The payment failed and Stripe doesn’t have detailed information about the cause. Your customer’s bank didn’t provide a reason code. | Contact your customer for more information. |
| `8` | `internal` | The payment failed. | The payment failed. |
| `9` | `refer_to_customer` | The payment failed and Stripe doesn’t have detailed information about the cause. | Contact your customer for more information. |

#### Payment Method - Bacs Direct Debit

| ADDACS Raw network code | Failure code | Explanation | Next steps |
| --- | --- | --- | --- |
| `0`, `1` | `refer_to_customer` | The payment failed because your customer’s bank canceled the Direct Debit Instruction. The mandate is no longer active in the bank’s system. | Contact your customer because direct debits can’t be collected from this account anymore. To continue collecting payments with direct debits, you need to obtain a new Direct Debit Instruction (DDI) for a different account. |
| `2` | `recipient_deceased` | The attempt to set up a mandate is made on the account of a potentially deceased individual. | Verify your customer’s status, then retry the transaction. |
| `3`, `C`, `E` | `bank_ownership_changed` | The payment can’t be processed because your customer’s bank account has changed ownership. | Contact your customer to provide new account details, then retry the transaction. |
| `B` | `account_closed` | The payment can’t be processed because your customer’s bank account is closed. | Reach out to your customer to provide new account details. To continue collecting payments with direct debits, you need to obtain a new Direct Debit Instruction (DDI) for a different account. |
| `R` | `generic_could_not_process` | The payment failed. | The payment failed. |

| ARUDD Raw network code | Failure code | Explanation | Next steps |
| --- | --- | --- | --- |
| `0` | `insufficient_funds` | The payment process can’t be completed because your customer’s bank account doesn’t have the necessary funds. | Contact your customer to verify that they have the required funds, then retry the transaction. |
| `1`, `6` | `debit_not_authorized` | This payment doesn’t have an authorized mandate. | Obtain a new Direct Debit Instruction (DDI), then retry the transaction. |
| `5` | `invalid_account_number` | The transaction can’t be processed because the bank account details that your customer provided are incorrect. | Contact your customer to provide new account details, then retry the transaction. |
| `4`, `7`, `8` | `generic_could_not_process` | The payment failed. | The payment failed. |
| `2` | `recipient_deceased` | The attempt to set up a mandate is made on the account of a potentially deceased individual. | Verify your customer’s status, then retry the transaction. |

| AUDDIS Raw network code | Failure code | Explanation | Next steps |
| --- | --- | --- | --- |
| `2` | `recipient_deceased` | The attempt to set up a mandate is made on the account of a potentially deceased individual. | Verify your customer’s status, then retry the transaction. |
| `5` | `refer_to_customer` | The payment failed because the account number wasn’t recognized by the customer’s bank. There might be an issue with the bank account details. | We recommend that you check the Direct Debit Instruction (DDI) information and reach out directly to your customer to verify their banking details. |
| `6` | `refer_to_customer` | The payment failed because the Direct Debit Instruction (DDI) doesn’t exist in your customer’s bank database. The mandate might not be properly set up or has been canceled. | Check the status of the Direct Debit Instruction and contact your customer to verify the mandate is still active with their bank. |
| `B` | `account_closed` | The payment can’t be processed because your customer’s bank account is closed. | Contact your customer to get updated banking details and set up a new Direct Debit Instruction (DDI). |
| `F`, `G` | `debits_not_supported_for_account` | The payment failed because your customer’s bank doesn’t allow direct debits on their type of account. This account isn’t compatible with direct debit payments. | Contact your customer to get alternative bank account details that support direct debits and set up a new Direct Debit Instruction (DDI). |

#### Payment Method - Card Payments

Raw network response codes for card payments vary by card network. The following tables describe each network’s codes.

## Visa 

| Raw network code | Explanation |
| --- | --- |
| `01` | Refer to card issuer. |
| `02` | Refer to card issuer, special condition. |
| `03` | Invalid merchant. |
| `04` | Pick up card (no fraud). |
| `05` | Don’t honor. |
| `06` | Error. |
| `07` | Pick up card, special condition (fraud account). |
| `12` | Invalid transaction. |
| `13` | Invalid amount or currency conversion field overflow. |
| `14` | Invalid account number (no such number). |
| `15` | No such issuer. |
| `19` | Re-enter transaction. |
| `21` | No action taken. |
| `25` | Unable to locate record in file. |
| `28` | File temporarily not available for update or inquiry. |
| `39` | No credit account. |
| `41` | Lost card, pick up (fraud account). |
| `43` | Stolen card, pick up (fraud account). |
| `46` | Closed account. |
| `51` | Not sufficient funds. |
| `52` | No checking account. |
| `53` | No savings account. |
| `54` | Expired card or expiration date is missing. |
| `55` | Incorrect PIN or PIN missing. |
| `57` | Transaction not permitted to cardholder. |
| `58` | Transaction not allowed at terminal. |
| `59` | Suspected fraud. |
| `61` | Exceeds approval amount limit. |
| `62` | Restricted card (card invalid in this region or country). |
| `63` | Security violation (source isn’t correct issuer). |
| `64` | Transaction does not fulfill AML requirement. |
| `65` | Exceeds withdrawal frequency limit. |
| `70` | PIN data required. |
| `74` | Different value than that used for PIN encryption errors. |
| `75` | Allowable number of PIN entry tries exceeded. |
| `76` | Unsolicited reversal. |
| `78` | “Blocked, first used”—Transaction from new cardholder, and card not properly unblocked |
| `79` | Already reversed (by Switch). |
| `80` | No financial impact. |
| `81` | Cryptographic error found in PIN. |
| `82` | Negative CAM, dCVV, iCVV, or CVV results. |
| `86` | Can’t verify PIN; for example, no PVV. |
| `89` | Ineligible to receive financial position information (GIV). |
| `91` | Issuer or switch inoperative and STIP not applicable or not available for this transaction; time-out when no stand-in; POS Check Service: destination unavailable; credit voucher and merchandise return authorizations: V.I.P. sent the transaction to the issuer, but the issuer was unavailable. |
| `92` | Financial institution or intermediate network facility can’t be found for routing (receiving institution ID is invalid). |
| `93` | Transaction can’t be completed—violation of law. |
| `94` | Request is identified as a duplicate. |
| `96` | System malfunction. |
| `1A` | Additional customer authentication required. |
| `6P` | Verification data failed. |
| `B1` | Surcharge amount not permitted on Visa cards or EBT food stamps (US acquirers only). |
| `B2` | Surcharge amount not supported by debit network issuer. |
| `N0` | Force STIP. |
| `N3` | Cash service not available. |
| `N4` | Cash request exceeds issuer or approved limit. |
| `N5` | Ineligible for resubmission. |
| `N7` | Decline for CVV2 failure. |
| `N8` | Transaction amount exceeds preauthorized approval amount. |
| `P5` | Denied PIN unblock—PIN change or unblock request declined by issuer. |
| `P6` | Denied PIN change—requested PIN unsafe. |
| `Q1` | Card authentication failed. |
| `R0` | Stop this payment. |
| `R1` | Stop all future payments. |
| `R2` | Transaction does not qualify for Visa PIN. |
| `R3` | Stop all merchants. |
| `Z3` | Unable to go online; offline-declined. |
| `5C` | Transaction not supported/blocked by issuer. |
| `9G` | Blocked by cardholder/contact cardholder. |

## Cartes Bancaires 

| Raw network code | Explanation |
| --- | --- |
| `02` | Refer to card issuer. |
| `03` | Invalid merchant. |
| `04` | Pick-up. |
| `05` | Don’t honor. |
| `06` | Error (bilateral usage). |
| `07` | Pick-up card, special condition. |
| `08` | Honor with identification. |
| `12` | Invalid transaction. |
| `13` | Invalid amount. |
| `14` | Invalid card number. |
| `15` | No such issuer. |
| `17` | Customer cancellation. |
| `19` | Re-enter transaction. |
| `20` | Invalid response (error in server domain). |
| `21` | No action taken. |
| `24` | File update not supported by receiver. |
| `25` | Unable to locate record on file. |
| `26` | Duplicate file update record, old record replaced. |
| `27` | File update field edit error. |
| `28` | File update file locked out. |
| `29` | File update not successful, contact acquirer. |
| `30` | Format error. |
| `31` | Bank not supported by switch. |
| `32` | Completed partially. |
| `33` | Expired card with card capture. |
| `34` | Suspected fraud. |
| `38` | Allowable PIN tries exceeded. |
| `39` | No such account type. |
| `40` | Requested function not supported. |
| `41` | Lost card. |
| `43` | Stolen card, pick-up. |
| `46` | Business-specific error. |
| `47` | Restricted card. |
| `51` | Not sufficient funds. |
| `54` | Expired card without card capture. |
| `55` | Incorrect PIN. |
| `56` | No card record. |
| `57` | Transaction not permitted to cardholder. |
| `58` | Transaction not permitted to terminal. |
| `59` | Suspected fraud. |
| `5C` | Transaction not supported/blocked by issuer. |
| `61` | Exceeds withdrawal amount limit. |
| `62` | Card invalid in region or country. |
| `63` | Security violation. |
| `64` | Transaction does not fulfil Anti-Money Laundering requirement. |
| `65` | Exceeds withdrawal frequency limit. |
| `68` | Response received too late. |
| `6P` | Verification data failed. |
| `75` | Allowable number of PIN tries exceeded. |
| `76` | Card already in the exception file, previous record stored. |
| `77` | Closed account. |
| `78` | Blocked, first used transaction from new cardholder, and card not properly unblocked. |
| `79` | Life cycle. |
| `81` | Cryptographic error found in PIN. |
| `82` | Incorrect CVV, dCVV, iCVV. |
| `83` | Fraud/security. |
| `85` | Conditional agreement—subject to additional cardholder authentication. |
| `86` | Can’t verify PIN. |
| `8P` | Policy. |
| `90` | Cutoff is in process. |
| `91` | Issuer or switch is inoperative. |
| `93` | Transaction can’t be completed—violation of law. |
| `94` | Duplicated transmission. |
| `95` | Loop. |
| `96` | System malfunction, no rerouting requested. |
| `97` | General monitoring timeout. |
| `98` | Server unavailable, network rerouting requested. |
| `99` | Initiator domain incident. |
| `9G` | Blocked by cardholder/contact cardholder. |
| `A0` | Fallback in EMV contact mode. |
| `A1` | Soft decline (electronic commerce only), 3DS with challenge required. |
| `A2` | PIN request in single TAP mode. |
| `A3` | New TAP with required authentication. |
| `B0` | Mandatory service can’t be performed. |
| `N0` | Force STIP. |
| `R0` | Stop payment order. |
| `R1` | Revocation of all recurring payments for the card at the merchant. |
| `R3` | Revocation of all recurring payments for the card. |
| `Z5` | Valid account but amount isn’t supported. |

## Eftpos AU 

| Raw network code | Explanation |
| --- | --- |
| `01` | Refer to card issuer. |
| `04` | Pick up card. |
| `05` | Don’t honor. |
| `06` | Error. |
| `08` | Honor with signature. |
| `12` | Invalid transaction. |
| `13` | Invalid amount. |
| `14` | Invalid card number. |
| `15` | No such issuer. |
| `19` | Re-enter transaction. |
| `21` | No action taken. |
| `30` | Format error. |
| `31` | Bank not supported by switch. |
| `33` | Expired card. |
| `34` | Suspected fraud. |
| `36` | Restricted card. |
| `38` | PIN retries exceeded. |
| `39` | No credit account. |
| `40` | Function not supported. |
| `41` | Lost card. |
| `43` | Stolen card. |
| `44` | No investment account. |
| `51` | Insufficient funds. |
| `52` | No cheque account. |
| `53` | No savings account. |
| `54` | Expired card. |
| `55` | Incorrect PIN. |
| `56` | No card record. |
| `57` | Transaction not permitted to cardholder. |
| `58` | Transaction not permitted to terminal. |
| `59` | Suspected fraud. |
| `61` | Exceeds withdrawal amount limit. |
| `62` | Restricted card. |
| `64` | Original amount incorrect. |
| `65` | Exceeds withdrawal frequency limit. |
| `67` | Hot card. |
| `75` | PIN tries exceeded. |
| `80` | Invalid KEK ID. |
| `81` | Invalid session keyset. |
| `91` | Issuer not available. |
| `92` | Financial institution/intermediate network not found for routing. |
| `94` | Duplicate transmission. |
| `95` | Reconcile error. |
| `96` | System malfunction. |
| `97` | Settlement date advanced. |
| `98` | MAC error. |

## UnionPay 

| Raw network code | Explanation |
| --- | --- |
| `01` | Refer to card issuer. |
| `03` | Invalid merchant. |
| `04` | Pick-up. |
| `05` | ID certification fails. |
| `11` | VIP. |
| `12` | Invalid related transaction. |
| `13` | Invalid amount. |
| `14` | Invalid card number (no such account). |
| `15` | No such issuer. |
| `1A` | Additional customer authentication required (SCA). |
| `20` | Update the QRC. |
| `21` | Card not initialized / dormant card. |
| `22` | Suspected malfunction; related transaction error. |
| `25` | Unable to locate original transaction. |
| `30` | Format error. |
| `34` | Fraud. |
| `38` | PIN try limit exceeded. |
| `40` | Function requested not supported. |
| `41` | Lost card. |
| `43` | Stolen card. |
| `45` | Fallback transaction not allowed. |
| `51` | Insufficient balance. |
| `54` | Expired card. |
| `55` | Incorrect PIN. |
| `57` | Transaction not allowed to be processed by cardholder. |
| `58` | Transaction not allowed to be processed by terminal. |
| `59` | Suspected fraud. |
| `61` | Transaction amount limit exceeded. |
| `62` | Restricted card. |
| `64` | Original transaction amount error. |
| `65` | Exceeded withdrawal velocity limit. |
| `68` | Issuer response timeout. |
| `75` | Allowable number of PIN tries exceeded. |
| `90` | Cutoff in progress. |
| `91` | Issuer not capable to process. |
| `92` | Financial institution or intermediate network facility can’t be found for routing. |
| `94` | Duplicated transaction. |
| `96` | Switch system malfunction. |
| `97` | ATM/POS terminal not located. |
| `98` | Issuer response not received. |
| `99` | PIN block error. |
| `A0` | MAC failed. |
| `A3` | Account not found in transfer-in side. |
| `A7` | Security processing failure. |
| `B1` | No arrears (transaction receipt not printed). |
| `C1` | Illegal acquirer status. |
| `D1` | Incorrect institution identification code. |
| `D2` | Date error. |
| `D3` | Invalid file type. |
| `D4` | File processed. |
| `D5` | No such file. |
| `D6` | Not supported by receiver. |
| `D7` | File locked. |
| `D8` | Unsuccessful. |
| `D9` | Incorrect file length. |
| `DA` | File decompression error. |
| `DB` | File name error. |
| `DC` | File can’t be received. |
| `F1` | File record format error. |
| `F2` | File record repeated. |
| `F3` | File record not existing. |
| `F4` | File record error. |
| `N1` | Items not on bankbook beyond limit. |
| `N2` | Transaction amount exceeds institution’s account balance. |
| `P1` | Cardholder contact number not found in issuer’s system. |
| `Z1` | Offline transaction fails. |
| `Z3` | Can’t process online; offline transaction fails. |

## CAFIS JCB 

| Raw network code | Explanation |
| --- | --- |
| `G12` | The card isn’t usable. |
| `G30` | The outcome of the transaction is pending. |
| `G42` | The personal identification number (PIN) entered by the cardholder is incorrect. |
| `G44` | The security code is incorrect. |
| `G45` | No security code entered. |
| `G46` | Incorrect JIS2 stripe information. |
| `G54` | The number of times or amount of usage per day exceeds the specified limit. |
| `G55` | The amount available per day exceeds the specified upper limit. |
| `G56` | An invalid card is used and a card capture is required. |
| `G59` | Incorrect secondary amount. |
| `G60` | Accident card. |
| `G61` | Invalid card. |
| `G65` | Incorrect membership number. |
| `G67` | Incorrect product code. |
| `G68` | Incorrect amount. |
| `G69` | Incorrect tax and shipping information. |
| `G70` | Incorrect number of bonus payments. |
| `G71` | Incorrect bonus month. |
| `G72` | Incorrect bonus amount. |
| `G73` | Incorrect payment start month. |
| `G74` | Incorrect number of installment payments. |
| `G75` | Incorrect payment amount for installment. |
| `G76` | Incorrect first payment amount. |
| `G77` | Incorrect business classification. |
| `G78` | Incorrect payment method. |
| `G79` | Incorrect inquiry category. |
| `G80` | Incorrect reversal category. |
| `G81` | Incorrect handling category. |
| `G83` | Card expired. |
| `G85` | Card not applicable to the service. |
| `G95` | The online service has been discontinued. |
| `G96` | Invalid accident card data. |
| `G97` | The request message can’t be processed for some reason. |
| `G98` | Request not supported. |
| `G99` | Data is received from a center which hasn’t made the contract. |
| `K01` | The relevant destination center isn’t available. |

## Cybersource 

| Raw network code | Explanation |
| --- | --- |
| `01` | Declined. Contact the issuer. |
| `03` | Declined. Invalid merchant. |
| `04` | Pick up. China UnionPay recommends withholding the card. |
| `05` | Declined. Failed cardholder certification. |
| `12` | Declined. Invalid transaction. |
| `13` | Declined. Invalid amount. |
| `14` | Declined. Invalid card number. |
| `15` | Declined. No matching issuer. |
| `20` | Declined. Update the QR code. |
| `21` | Declined. The card hasn’t been initialized or it is dormant. |
| `22` | Declined. Operation error or exceeds the number of days allowed for transaction. |
| `25` | Declined. Unable to locate original transaction. Contact the issuer. |
| `30` | Declined due to format error. Retry. |
| `34` | Pick up (fraudulent card). China UnionPay recommends withholding the card. |
| `38` | Declined. PIN retry limit exceeded. |
| `40` | Declined. The transaction isn’t supported. |
| `41` | Pick up (lost card). China UnionPay recommends withholding the card. |
| `43` | Pick up (stolen card). China UnionPay recommends withholding the card. |
| `45` | Declined. Fallback transaction not allowed. |
| `51` | Declined. Insufficient balance. |
| `54` | Declined. Expired card. |
| `55` | Declined. Incorrect PIN. |
| `57` | Declined. The transaction isn’t allowed on the card. |
| `58` | Declined. The transaction isn’t allowed by the issuer. |
| `59` | Declined. Suspected fraud. |
| `61` | Declined. Transaction amount exceeds limit. |
| `62` | Declined. Restricted card. |
| `64` | Declined. Transaction amount does not match original transaction amount. |
| `65` | Declined. Transaction exceeds the limited times of withdrawal. |
| `68` | Declined. Issuer response time-out. Retry later. |
| `75` | Declined. Number of PIN tries exceeds the limit. |
| `90` | Declined. Daily cutoff is in progress. Retry later. |
| `91` | Declined. Issuer status is abnormal. Retry later. |
| `92` | Declined. Connectivity of issuer is abnormal. Retry later. |
| `94` | Declined. Duplicate transaction. |
| `96` | Declined. Switch system malfunction. Retry later. |
| `97` | Declined. Unregistered terminal number. |
| `98` | Declined. Issuer response time-out. |
| `99` | Declined. Error in PIN format. Retry sign-in. |
| `A0` | Declined. Error in MAC verification. Retry sign-in. |
| `A3` | Declined. Transfer recipient’s account not found. |
| `A7` | Security processing failure. |
| `B1` | Declined. Transaction receipt not printed. |
| `C1` | Declined. Illegal status of acquirer. |
| `D1` | Incorrect institution identification code. |
| `D2` | Data error. |
| `D3` | Invalid file type. |
| `D4` | File processed. |
| `D5` | File not found. |
| `D6` | Transaction not supported by recipient. |
| `D7` | File locked. |
| `D8` | Unsuccessful. |
| `D9` | Incorrect file length. |
| `DA` | File decompression error. |
| `DB` | File name error. |
| `DC` | The file can’t be received. |
| `F1` | File record format error. |
| `F2` | File record repeated. |
| `F3` | File record does not exist. |
| `F4` | File record error. |
| `N1` | Declined. Unregistered account exceeds transaction limit. |
| `N2` | Declined. Transaction amount exceeds balance. |
| `P1` | Declined. Contact phone number not found. |
| `Z1` | Declined. |
| `Z3` | Declined. |
| `1A` | Declined. Additional customer authentication is required. |

## Girocard 

| Raw network code | Explanation |
| --- | --- |
| `05` | Don’t honor. |
| `21` | Cancellation not possible. |
| `30` | Format error. |
| `51` | Insufficient funds. |
| `54` | Expired card. |
| `55` | Incorrect PIN. |
| `57` | Transaction not allowed to cardholder. |
| `58` | Transaction not allowed at terminal. |
| `60` | Cardholder authentication required; repeat authorization with PIN. |
| `62` | Card blocked. |
| `65` | Cardholder authentication required; insert card. |
| `75` | Allowable PIN entry tries exceeded. |
| `77` | Chip error / invalid MAC. |
| `84` | PIN not active. |
| `85` | Cashback not possible. |
| `91` | Issuer not available. |
| `92` | Wrong routing partner. |
| `96` | System error. |
| `97` | Invalid MAC. |
| `98` | Date/time implausible. |
| `99` | Invalid PIN block. |

## JCB International 

| Raw network code | Explanation |
| --- | --- |
| `01` | Refer to issuer. |
| `03` | Invalid merchant. |
| `04` | Pick-up. |
| `05` | Don’t honor. |
| `06` | Error. |
| `07` | Pick-up card, special condition, counterfeit. |
| `09` | Request in progress. |
| `12` | Invalid transaction (duplicate transaction). |
| `13` | Invalid amount. |
| `14` | Invalid card number (no such number). |
| `15` | No such issuer. |
| `17` | Customer cancellation. |
| `20` | Invalid response. |
| `30` | Format error. |
| `31` | Bank not supported by switch. |
| `33` | Expired card. |
| `34` | Suspected fraud. |
| `36` | Restricted card. |
| `40` | Requested function not supported. |
| `41` | Lost card. |
| `42` | No universal account. |
| `43` | Stolen card, pick-up. |
| `51` | Not sufficient funds. |
| `54` | Expired card, or expiration date error. |
| `55` | Incorrect personal identification number. |
| `56` | No card record. |
| `57` | Transaction not permitted to cardholder. |
| `58` | Transaction not permitted to terminal. |
| `59` | Suspected fraud. |
| `61` | Exceeds withdrawal amount limit. |
| `62` | Restricted card. |
| `63` | Security violation. |
| `65` | Exceeds withdrawal frequency limit. |
| `68` | Response received too late. |
| `75` | Allowable number of PIN tries exceeded. |
| `76` | Incorrect reversal (Auth-ID, STAN, AMNT). |
| `77` | Lost, stolen, pick-up. |
| `78` | Shop in black list. |
| `79` | Account status flag false. |
| `81` | PIN cryptographic error found. |
| `85` | Not declined (only used for balance inquiry and address verification with zero amount). |
| `87` | Incorrect passport number. |
| `88` | Incorrect date of birth. |
| `89` | (Not approved: free message). |
| `90` | Cutoff is in progress. |
| `91` | Issuer or switch is inoperative. |
| `92` | The financial institution can’t be found for routing. |
| `94` | Duplicate transmission. |
| `96` | System malfunction. |

## Mastercard 

| Raw network code | Explanation |
| --- | --- |
| `01` | Refer to card issuer. |
| `12` | Invalid transaction. |
| `15` | Invalid issuer. |
| `30` | Format error. |
| `39 (MAC 04)` | POS cardholder presence indicator. |
| `71` | PIN not changed. |
| `86` | PIN validation not possible. |
| `88` | Cryptographic failure. |
| `91` | Authorization system or issuer system inoperative. |
| `92` | Unable to route the transaction. |
| `94` | Duplicate transmission detected. |
| `96` | System error. |
| `04` | Capture card. |
| `41` | Lost card. |
| `43` | Stolen card. |
| `55` | Invalid PIN. |
| `63` | Security violation. |
| `51 (MAC 01)` | Insufficient funds / over credit limit. |
| `51 (MAC 02)` | Insufficient funds / over credit limit. |
| `51 (MAC 03)` | Insufficient funds / over credit limit. |
| `03` | Invalid merchant. |
| `13` | Invalid amount. |
| `57` | Transaction not permitted to issuer / cardholder. |
| `58` | Transaction not permitted to acquirer / terminal. |
| `61` | Exceeds withdrawal amount limit. |
| `62` | Restricted card. |
| `65` | Exceeds withdrawal count limit (or Identity Check soft-decline of EMV 3DS authentication). |
| `75` | Allowable number of PIN tries exceeded. |
| `14 (MAC 01)` | Invalid card number. |
| `14 (MAC 03)` | Invalid card number. |
| `54 (MAC 01)` | Expired card. |
| `54 (MAC 03)` | Expired card. |
| `72` | Account not yet activated. |
| `79 (MAC 01)` | Expired card (lifecycle decline; updated card data available). |
| `79 (MAC 02)` | Invalid credentials (lifecycle decline; can retry later). |
| `79 (MAC 03)` | Account credentials not found (don’t retry). |
| `82 (MAC 01)` | Invalid transaction/merchant. |
| `82 (MAC 02)` | Invalid transaction/merchant. |
| `82 (MAC 03)` | Invalid transaction or merchant, don’t retry. |
| `83 (MAC 01)` | Suspected fraud. |
| `83 (MAC 02)` | Retry the transaction later. |
| `83 (MAC 03)` | Suspected fraud. |
| `05 (MAC 01)` | Don’t honor. |
| `05 (MAC 03)` | Don’t honor. |
| `05 (MAC 21)` | Don’t honor. |

## American Express (Amex) 

| Raw network code | Explanation |
| --- | --- |
| `001` | Approve with ID. |
| `003` | Approve VIP (Visa only). |
| `100` | Deny. |
| `101` | Expired card / invalid expiration. |
| `106` | Exceeded PIN attempts. |
| `107` | Call issuer. |
| `109` | Invalid merchant. |
| `110` | Invalid amount. |
| `111` | Invalid account. |
| `115` | Invalid function (not certified). |
| `116` | Not sufficient funds. |
| `117` | Invalid PIN. |
| `119` | Not enrolled / permitted. |
| `121` | Limit exceeded. |
| `122` | Invalid CVC. |
| `125` | Invalid effective date. |
| `130` | Additional customer authentication required. |
| `181` | Format error. |
| `183` | Invalid currency code. |
| `187` | Deny - new card issued. |
| `188` | Deny - account cancelled. |
| `189` | Deny - canceled merchant. |
| `190` | National ID mismatch. |
| `200` | Deny - pick up card. |
| `912` | Issuer not available. |
| `977` | Invalid payment plan. |
| `978` | Invalid payment times. |

## Discover 

| Raw network code | Explanation |
| --- | --- |
| `03` | Invalid merchant. |
| `04` | Capture card. |
| `05` | Don’t honor. |
| `07` | Pick-up card, special condition. |
| `12` | Invalid transaction. |
| `13` | Invalid amount. |
| `14` | Invalid card number. |
| `19` | Re-enter transaction. |
| `30` | Format error. |
| `31` | Bank not supported by switch. |
| `34` | Suspected fraud, bot-driven. |
| `38` | Allowable PIN tries exceeded. |
| `39` | No credit account. |
| `40` | Requested function not supported. |
| `41` | Lost card. |
| `43` | Stolen card. |
| `51` | Decline. |
| `53` | No savings account. |
| `54` | Expired card. |
| `55` | Invalid PIN. |
| `56` | No card record. |
| `57` | Transaction not permitted to issuer / cardholder. |
| `58` | Transaction not permitted to acquirer / terminal. |
| `59` | Suspected fraud. |
| `60` | Card acceptor contact acquirer. |
| `61` | Exceeds withdrawal amount limit. |
| `62` | Restricted card. |
| `63` | Security violation. |
| `64` | Original amount incorrect. |
| `65` | Exceeds withdrawal count limit. |
| `66` | Card acceptor contact acquirer’s security department. |
| `67` | Hard capture. |
| `68` | Response received too late. |
| `75` | Allowable number of PIN tries exceeded. |
| `76` | Invalid/nonexistent “To Account” specified. |
| `77` | Invalid/nonexistent “From Account” specified. |
| `78` | Invalid/nonexistent account specified (general). |
| `83` | Domain restriction controls failure. |
| `87` | Network unavailable. |
| `91` | Authorization system or issuer system inoperative. |
| `92` | Unable to route transaction. |
| `93` | The transaction can’t be completed, violation of law. |
| `94` | Duplicate transmission detected. |
| `96` | System malfunction. |
| `N1` | System up. |
| `N2` | Soft down. |
| `N3` | System down. |
| `N7` | Decline for AVS or CID mismatch. |
| `P5` | PIN change/unblock failed. |
| `P6` | New PIN not accepted. |

## NYCE 

| Raw network code | Explanation |
| --- | --- |
| `01` | Function not available - refer to card issuer. |
| `02` | Refer to card issuer’s special conditions. |
| `03` | Invalid merchant or terminal. |
| `04` | Pick-up. |
| `05` | Don’t honor. |
| `07` | Capture card, special conditions (bad debt). |
| `12` | Invalid transaction. |
| `13` | Invalid amount. |
| `14` | Invalid card number (no such number). |
| `15` | Cardholder not on file. |
| `24` | File update not supported by receiver. |
| `25` | Unable to locate record on file. |
| `26` | Duplicate file update record, no action. |
| `27` | File update field edit error. |
| `28` | File update record locked out. |
| `29` | File update not successful, contact acquirer. |
| `30` | Format error; DE 044 contains bit \\# in error. |
| `31` | Bank not supported by switch. |
| `33` | Expired card, capture. |
| `34` | Suspected fraud, capture. |
| `38` | Allowable PIN tries exceeded, capture. |
| `39` | No credit account. |
| `40` | Requested function not supported. |
| `41` | Lost card, capture. |
| `42` | Invalid account. |
| `43` | Stolen card, capture. |
| `44` | Lost/stolen card, no capture. |
| `51` | Insufficient funds. |
| `52` | No checking account. |
| `53` | No savings account. |
| `54` | Expired card. |
| `55` | Incorrect PIN. |
| `56` | No card record. |
| `57` | Transaction not permitted to cardholder. |
| `58` | Transaction not permitted to terminal. |
| `59` | Suspected fraud. |
| `61` | Exceeds withdrawal amount limit. |
| `62` | Restricted card. |
| `63` | Security violation (might also be a chargeback). |
| `65` | Exceeds withdrawal frequency limit. |
| `67` | Hard capture, permanent restraint. |
| `75` | Allowable number of PIN tries exceeded. |
| `76` | Key synchronization error (NYCE). |
| `81` | Issuer-requested stand-in. |
| `82` | Count exceeds limit. |
| `88` | Information not on file. |
| `89` | Card Verification Value validation failed (no pickup) suspected counterfeit card. |
| `90` | Processor not signed on. |
| `91` | Card issuer unavailable. |
| `92` | Financial institution or intermediate network unknown for routing. |
| `93` | The transaction can’t be completed, violation of law. |
| `94` | Duplicate transaction. |
| `96` | System malfunction. |
| `N0` | Authorization life cycle unacceptable. |
| `N1` | Authorization life cycle expired. |
| `RD` | RMS reject (due to risk scoring). |
| `SA` | Inactive card. |
| `SD` | Account closed. |
| `SE` | Ineligible account. |
| `SG` | No account on file. |
| `SK` | Cross-reference card not found. |
| `SL` | Category limit exceeded. |
| `SM` | Transaction limit exceeded. |
| `SN` | Daily limit exceeded. |
| `SO` | Monthly limit exceeded. |
| `SV` | Stop recurring payments. |
| `S2` | Check deposit limit exceeded. |
| `S3` | Cash back limit exceeded. |
| `S7` | Unmatched voucher information. |
| `S9` | Expiration date mismatch. |
| `SP` | Invalid AVS. |
| `TA` | ARQC validation failed for ICC chip card. |
| `T4` | Closed account. |
| `T5` | Dormant account. |
| `T9` | Insufficient funds for fees. |

## Everlink (Interac) 

| Raw network code | Explanation |
| --- | --- |
| `05` | Don’t honor (POLICY). |
| `06` | Edit error (POLICY). |
| `11` | Invalid processing code (POLICY). |
| `12` | Invalid processing code (IOP) (POLICY). |
| `13` | Invalid amount (edit error in amount) (POLICY). |
| `14` | Invalid card number (edit error in PAN) (POLICY). |
| `19` | Acquirer error. Re-enter transaction. (SYSTEM). |
| `23` | Invalid transaction fee (future) (POLICY). |
| `40` | Requested function not supported (POLICY). |
| `51` | Not sufficient funds (POLICY). |
| `52` | No chequing account (POLICY). |
| `53` | No savings account (POLICY). |
| `54` | Expired card (POLICY). |
| `55` | Incorrect PIN (POLICY). |
| `56` | No card record (PAN not on authorizer’s database) (POLICY). |
| `57` | Transaction not permitted to cardholder (POLICY). |
| `58` | Transaction not permitted to terminal (POLICY). |
| `61` | Exceeds withdrawal amount limit (POLICY). |
| `62` | Restricted card - temporarily disallowed from interchange (POLICY). |
| `63` | MAC security failure (SYSTEM). |
| `65` | Exceeds withdrawal frequency limit (POLICY). |
| `68` | Response received too late (timeout) (SYSTEM). |
| `75` | Allowable number of PIN entry tries exceeded (POLICY). |
| `77` | Invalid capture date (SYSTEM). |
| `78` | Hold on funds has expired (POLICY). |
| `81` | Invalid PIN block (SYSTEM). |
| `82` | PIN length error (SYSTEM). |
| `84` | Counter out of sequence in file (SYSTEM). |
| `85` | No keys available (SYSTEM). |
| `86` | KME sync error (SYSTEM). |
| `87` | KPE sync error (SYSTEM). |
| `88` | KMAC sync error (SYSTEM). |
| `89` | Contactless decline. Try again using contact (POLICY). |
| `91` | Issuer or switch is inoperative (SYSTEM). |
| `92` | The financial institution or intermediate network facility can’t be found for routing (SYSTEM). |
| `94` | Duplicate transmission (SYSTEM). |
| `96` | System malfunction (SYSTEM). |
| `Q0` | Edit error on capture date (SYSTEM). |
| `Q7` | Exceeds acquirer limit (SYSTEM). |
| `Q9` | Response received that was not listed above (SYSTEM). |
| `U0` | ARQC verification failed; decline (SYSTEM). |
| `U1` | Hardware security module parameter error; decline (SYSTEM). |
| `U2` | Hardware security module failure; decline (SYSTEM). |
| `U3` | Cryptograms required for chip card authentication not found; decline (SYSTEM). |
| `U4` | ATC check failure; decline (SYSTEM). |
| `U5` | CVR failure; decline (SYSTEM). |
| `U6` | TVR failure; decline (SYSTEM). |
| `U7` | Reason online code decline (SYSTEM). |
| `U8` | Fallback decline (POLICY). |
| `V0` | ARQC verification failed; refer (SYSTEM). |
| `V1` | CVR failure; refer (SYSTEM). |
| `V2` | TVR failure; refer (SYSTEM). |
| `V3` | Reason online code referral (SYSTEM). |
| `V4` | Fallback referral (POLICY). |
| `V7` | ARQC verification failed; capture card (SYSTEM). |
| `V8` | CVR failure; capture card (SYSTEM). |
| `V9` | TVR failure; capture card (SYSTEM). |

#### Payment Method - Cash App Pay

For more information on specific Cash App Pay error codes, refer to the [Cash App Pay error code reference](https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/errors/error-code-reference#payment-processing-errors).

| Raw network code | Decline code |
| --- | --- |
| `PAYMENT_INVALID_TOO_SMALL` | `invalid_amount` |
| `PAYMENT_INVALID_TOO_LARGE` | `invalid_amount` |
| `PAYMENT_DECLINED_COMPLIANCE` | `compliance_violation` |
| `PAYMENT_DECLINED_RISK` | `payment_declined_risk` |
| `PAYMENT_INVALID_CURRENCY_MISMATCH` | `currency_not_supported` |
| `PAYMENT_INVALID_AMOUNT_MISMATCH` | `invalid_amount` |
| `PAYMENT_DECLINED_INSUFFICIENT_FUNDS` | `insufficient_funds` |
| `PAYMENT_DECLINED_LIMIT_REACHED` | `limit_exceeded` |
| `PAYMENT_DECLINED_OTHER` | `payment_declined` |
| `PAYMENT_DECLINED_CUSTOMER_BLOCKED_MERCHANT` | `invalid_customer_account` |

#### Payment Method - New Zealand BECS Direct Debit

| Raw network code | Failure code | Explanation | Next steps |
| --- | --- | --- | --- |
| `1` | `invalid_routing_number` | The transaction can’t be processed because the routing number that your customer provided is incorrect. | Contact your customer to provide new account details, then retry the transaction. |
| `2` | `debit_not_authorized` | This payment doesn’t have an authorized mandate. | Collect a new mandate, then retry the transaction. |
| `3` | `account_closed` | The payment can’t be processed because your customer’s bank account is closed. | Contact your customer to provide new account details, then retry the transaction. |
| `4` | `recipient_deceased` | The attempt to set up a mandate is made on the account of a potentially deceased individual. | Verify your customer’s status, then retry the transaction. |
| `5` | `no_account` | The transaction can’t be processed because the bank account information that your customer provided is incorrect. | Contact your customer to provide new account details, then retry the transaction. |
| `6` | `refer_to_customer` | The payment failed and Stripe doesn’t have detailed information about the cause. Your customer’s bank didn’t provide a reason code. | Contact your customer for more information. |
| `8` | `internal` | The payment failed. | The payment failed. |
| `9` | `refer_to_customer` | The payment failed and Stripe doesn’t have detailed information about the cause. | Contact your customer for more information. |

#### Payment Method - Pre-authorized debit in Canada

| Raw network code | Failure code | Explanation | Next steps |
| --- | --- | --- | --- |
| `901`, `908` | `insufficient_funds` | The payment process can’t be completed because your customer’s bank account doesn’t have the necessary funds. | Contact your customer to verify that they have the required funds, then retry the transaction. |
| `900` | `generic_could_not_process` | The payment failed. | The payment failed. |
| `903`, `915` | `debit_not_authorized` | This payment doesn’t have an authorized mandate. | Collect a new mandate, then retry the transaction. |
| `905` | `account_closed` | The payment can’t be processed because your customer’s bank account is closed. | Contact your customer to provide new account details, then retry the transaction. |
| `912` | `invalid_account_number` | The transaction can’t be processed because the account number that your customer provided is incorrect. | Contact your customer to provide new account details, then retry the transaction. |
| `911` | `account_frozen` | The payment can’t be processed because your customer’s bank account is frozen. | Contact your customer to provide new account details, then retry the transaction. |
| `902` | `no_account` | The transaction can’t be processed because the bank account information that your customer provided is incorrect. | Contact your customer to provide new account details, then retry the transaction. |
| `907` | `bank_account_restricted` | The payment can’t be processed because your customer’s bank has blocked direct debits, either by the bank’s actions or your customer’s. | Contact your customer to understand the reason for the block. If the bank unblocks the account, retry the transaction. |
| `910` | `recipient_deceased` | The attempt to set up a mandate is made on the account of a potentially deceased individual. | Verify your customer’s status before retrying the transaction. |

#### Payment Method - SEPA Direct Debit

| Raw network code | Failure code | Explanation | Next steps |
| --- | --- | --- | --- |
| `AC01` | `invalid_account_number` | The transaction can’t be processed because the IBAN that your customer provided is incorrect. | Contact your customer for correct account details, then retry the transaction. |
| `AC04` | `account_closed` | The payment can’t be processed because your customer’s bank account is closed. | Contact your customer for new account details, then retry the transaction. |
| `AG02`, `AM05`, `CNOR`, `DNOR`, `DN05`, `FF01`, `AC13` | `generic_could_not_process` | Stripe can’t identify a specific reason for the payment failure. | Contact Support for more information. |
| `AM04` | `insufficient_funds` | The payment process can’t be completed because your customer’s bank account lacks the necessary funds. | Contact your customer to verify that they have the required funds, then retry the transaction. |
| `MD01` | `debit_not_authorized` | The payment doesn’t have an authorized mandate. | Collect a new mandate, then retry the transaction. |
| `MD02`, `BE05` | `debit_authorization_not_match` | The transaction can’t be processed due to missing or incorrect mandate information. | Collect a new mandate from your customer, then retry the transaction. |
| `MD06` | `debit_disputed` | Your customer requested that their bank refund this payment. | Contact your customer to resolve any dispute, then retry the transaction. |
| `MD07` | `recipient_deceased` | The mandate was set up on the account of a potentially deceased individual. | Verify your customer’s status before retrying the transaction. |
| `RC01` | `branch_does_not_exist` | The payment can’t be processed because the bank branch associated with your customer’s IBAN doesn’t exist. | Contact your customer to provide new account details, then retry the transaction. |
| `RR01`, `RR02`, `RR03` | `incorrect_account_holder_name` | The transaction can’t be processed because your customer’s account information is missing or incorrect. | Collect a new mandate and ask your customer to provide their name and address exactly as it appears on their bank account. Then, retry the transaction. |
| `SL01`, `MS03` | `refer_to_customer` | We don’t have detailed information about the payment failure because your customer’s bank didn’t provide a reason code. | Contact your customer for more information. |
