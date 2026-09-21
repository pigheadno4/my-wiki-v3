<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/general/processor-responses/authorization-responses -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Authorization Response Codes | Braintree
slug: /docs/reference/general/processor-responses/authorization-responses/
createTime: '2025-04-02T00:09:37.424Z'
updateTime: '2026-06-22T11:04:21.186Z'
---



# Authorization


**NOTE**
Authorization and capture can incur merchant fees in some markets. For more information, see your [Braintree User Agreement](https://www.braintreepayments.com/legal) .


## Approvals

1000-class codes mean the processor has successfully authorized the transaction and success will be true. However, depending on your processing settings, it is possible that the authorization will be[gateway rejected](/braintree/articles/control-panel/transactions/gateway-rejections)even if the processor returns a successful response.

| Code | Text |
| --- | --- |
| 1000 | Approved. |
| 1001 | Approved. Check customer ID. |
| 1002 | Processed.This code will be assigned to certain refunds, credits, and voice authorizations that do not need to be authorized; they are immediately submitted for settlement. |
| 1003 | Approved with Risk.The bank account can be used for transactions, but some risk has been identified (e.g. some customer information does not exactly match the bank's records). |
| 1004 | Approved for Partial Amount.The transaction was approved for an amount less than the amount requested. |
| 1005 | Auth Declined but Settlement Captured. The refund authorization was attempted but declined, and was submitted for settlement. |


## Declines

2000-class codes mean the authorization was declined by the processor and success will be false; 3000-class codes indicate a problem with the back-end processing network. The code is meant to tell you more about why the card was declined, but it can sometimes be ambiguous. For some of the more elusive processor responses, we’ve included more context below.
### Types of declines

There are two types of declines: hard declines and soft declines.


- **Hard declines**are the result of an error or issue which can't be resolved immediately; the decline is not temporary and subsequent attempts with the same payment method will likely not be successful.
- **Soft declines**result from a temporary issue and can be retried; subsequent transaction attempts with the provided payment method information may process successfully.


### Handling declines

To help mitigate fraud, merchants typically show the customer a relatively generic message when a payment method is declined (e.g.There was a problem processing your credit card; please double check your payment information and try again). We still recommend that you log the processor response code in your system in case a customer contacts you for more information.
#### Retrying declined transactions

You can determine if there are any decline codes that you might want to handle differently. For example, because soft-declined transactions can sometimes work when retried, you could put the customer's order in a pending status and try again later. If subsequent attempts are unsuccessful, request a new payment method or cancel the order.

When deciding whether to retry declined transactions, be aware that restrictions exist for which transactions may be retried. Mastercard prohibits retries on transactions that are declinedcwith the following codes:


- **2009 hard decline**
- **2012 hard decline**
- **2019 hard decline**
- **2022 hard decline**
- **2047 hard decline**
- **2053 hard decline**

Additionally, some card associations have rules around retrying transactions originally passed with a recurring ecommerce indicator (ECI) flag. To comply with these rules, do not attempt manual or automated retries on transactions with this flag in the following cases:


- **Soft declines**: Do not retry the transaction more than 15 times in 30 days
- **2004 hard decline**: Do not retry the transaction
- **2005 hard decline**: Do not retry the transaction with the same payment information
- **2015 hard decline**: Do not retry the transaction


**NOTE**
The transaction response object that you receive via the API will indicate [whether this flag was passed](/braintree/docs/reference/response/transaction#recurring) .


### Decline codes

| Code | Text | Implications | Type |
| --- | --- | --- | --- |
| 2000 | Do Not Honor | The customer's bank is unwilling to accept the transaction. The customer will need to contact their bank for more details regarding this generic decline. | Soft |
| 2001 | Insufficient Funds | The account did not have sufficient funds to cover the transaction amount at the time of the transaction – subsequent attempts at a later date may be successful. | Soft |
| 2002 | Limit Exceeded | The attempted transaction exceeds the withdrawal limit of the account. The customer will need to contact their bank to change the account limits or use a different payment method. | Soft |
| 2003 | Cardholder's Activity Limit Exceeded | The attempted transaction exceeds the activity limit of the account. The customer will need to contact their bank to change the account limits or use a different payment method. | Soft |
| 2004 | Expired Card | Card is expired. The customer will need to use a different payment method. | Hard |
| 2005 | Invalid Credit Card Number | The customer entered an invalid payment method or made a typo in their credit card information. Have the customer correct their payment information and attempt the transaction again – if the decline persists, they will need to contact their bank. | Hard |
| 2006 | Invalid Expiration Date | The customer entered an invalid payment method or made a typo in their card expiration date. Have the customer correct their payment information and attempt the transaction again – if the decline persists, they will need to contact their bank. | Hard |
| 2007 | No Account | The submitted card number is not on file with the card-issuing bank. The customer will need to contact their bank. | Hard |
| 2008 | Card Account Length Error | The submitted card number does not include the proper number of digits. Have the customer attempt the transaction again – if the decline persists, the customer will need to contact their bank. | Hard |
| 2009 | No Such Issuer | This decline code could indicate that the submitted card number does not correlate to an existing card-issuing bank or that there is a connectivity error with the issuer. The customer will need to contact their bank for more information. | Hard |
| 2010 | Card Issuer Declined CVV | The customer entered in an invalid security code or made a typo in their card information. Have the customer attempt the transaction again – if the decline persists, the customer will need to contact their bank. | Hard |
| 2011 | Voice Authorization Required | The customer’s bank is requesting that the merchant (you) call to obtain a special authorization code in order to complete this transaction. This can result in a lengthy process – we recommend obtaining a new payment method instead.[Contact us](/braintree/help?issue=DeclinedTransaction)for more details. | Hard |
| 2012 | Processor Declined – Possible Lost Card | The card used has likely been reported as lost. The customer will need to contact their bank for more information. | Hard |
| 2013 | Processor Declined – Possible Stolen Card | The card used has likely been reported as stolen. The customer will need to contact their bank for more information. | Hard |
| 2014 | Processor Declined – Fraud Suspected | The customer’s bank suspects fraud – they will need to contact their bank for more information. | Hard |
| 2015 | Transaction Not Allowed | The customer's bank is declining the transaction for unspecified reasons, possibly due to an issue with the card itself. They will need to contact their bank or use a different payment method. | Hard |
| 2016 | Duplicate Transaction | The submitted transaction appears to be a duplicate of a previously submitted transaction and was declined to prevent charging the same card twice for the same service. | Soft |
| 2017 | Cardholder Stopped Billing | The customer requested a cancellation of a single transaction – reach out to them for more information. | Hard |
| 2018 | Cardholder Stopped All Billing | The customer requested the cancellation of a recurring transaction or subscription – reach out to them for more information. | Hard |
| 2019 | Invalid Transaction | The customer’s bank declined the transaction, typically because the card in question does not support this type of transaction – for example, the customer used an FSA debit card for a non-healthcare related purchase. They will need to contact their bank for more information. | Hard |
| 2020 | Violation | The customer will need to contact their bank for more information. | Hard |
| 2021 | Security Violation | The customer's bank is declining the transaction, possibly due to a fraud concern. They will need to contact their bank or use a different payment method. | Hard |
| 2022 | Declined – Updated Cardholder Available | The submitted card has expired or been reported lost and a new card has been issued. Reach out to your customer to obtain updated card information. | Hard |
| 2023 | Processor Does Not Support This Feature | Your account can't process transactions with the intended feature – for example, 3D Secure or Level 2/Level 3 data. If you believe your merchant account should be set up to accept this type of transaction,[contact us](/braintree/help?issue=DeclinedTransaction). | Hard |
| 2024 | Card Type Not Enabled | Your account can't process the attempted card type. If you believe your merchant account should be set up to accept this type of card,[contact us](/braintree/help?issue=DeclinedTransaction)for assistance. | Hard |
| 2025 | Set Up Error – Merchant | Depending on your region, this response could indicate a connectivity or setup issue.[Contact us](/braintree/help?issue=DeclinedTransaction)for more information regarding this error message. | Soft |
| 2026 | Invalid Merchant ID | The customer’s bank declined the transaction, typically because the card in question does not support this type of transaction. If this response persists across transactions for multiple customers, it could indicate a connectivity or setup issue.[Contact us](/braintree/help?issue=DeclinedTransaction)for more information regarding this error message. | Soft |
| 2027 | Set Up Error – Amount | This rare decline code indicates an issue with processing the amount of the transaction. The customer will need to contact their bank for more details. | Hard |
| 2028 | Set Up Error – Hierarchy | There is a setup issue with your account.[Contact us](/braintree/help?issue=DeclinedTransaction)for more information. | Hard |
| 2029 | Set Up Error – Card | This response generally indicates that there is a problem with the submitted card. The customer will need to use a different payment method. | Hard |
| 2030 | Set Up Error – Terminal | There is a setup issue with your account.[Contact us](/braintree/help?issue=DeclinedTransaction)for more information. | Hard |
| 2031 | Encryption Error | The cardholder’s bank does not support $0.00 card verifications. Enable the[Retry All Failed $0](/braintree/articles/control-panel/vault/card-verification#retrying-all-failed-$0-verifications)option to resolve this error.[Contact us](/braintree/help?issue=DeclinedTransaction)with questions. | Hard |
| 2032 | Surcharge Not Permitted | Surcharge amount not permitted on this card. The customer will need to use a different payment method. | Hard |
| 2033 | Inconsistent Data | An error occurred when communicating with the processor. The customer will need to contact their bank for more details. | Hard |
| 2034 | No Action Taken | An error occurred and the intended transaction was not completed. Attempt the transaction again. | Soft |
| 2035 | Partial Approval For Amount In Group III Version | The customer's bank approved the transaction for less than the requested amount. Have the customer attempt the transaction again – if the decline persists, the customer will need to use a different payment method. | Soft |
| 2036 | Authorization could not be found | An error occurred when trying to process the authorization. This response could indicate an issue with the customer’s card or that the processor doesn't allow this action –[contact us](/braintree/help?issue=DeclinedTransaction)for more information. | Hard |
| 2037 | Already Reversed | The indicated authorization has already been reversed. If you believe this to be false,[contact us](/braintree/help?issue=DeclinedTransaction)for more information. | Hard |
| 2038 | Processor Declined | The customer's bank is unwilling to accept the transaction. The reasons for this response can vary – customer will need to contact their bank for more details. | Soft |
| 2039 | Invalid Authorization Code | The authorization code was not found or not provided. Have the customer attempt the transaction again – if the decline persists, they will need to contact their bank. | Hard |
| 2040 | Invalid Store | There may be an issue with the configuration of your account. Have the customer attempt the transaction again – if the decline persists,[contact us](/braintree/help?issue=DeclinedTransaction)for more information. | Soft |
| 2041 | Declined – Call For Approval | The card used for this transaction requires customer approval – they will need to contact their bank. | Hard |
| 2042 | Invalid Client ID | There may be an issue with the configuration of your account. Have the customer attempt the transaction again – if the decline persists,[contact us](/braintree/help?issue=DeclinedTransaction)for more information. | Soft |
| 2043 | Error – Do Not Retry, Call Issuer | The card-issuing bank will not allow this transaction. The customer will need to contact their bank for more information. | Hard |
| 2044 | Declined – Call Issuer | The card-issuing bank has declined this transaction. Have the customer attempt the transaction again – if the decline persists, they will need to contact their bank for more information. | Hard |
| 2045 | Invalid Merchant Number | There is a setup issue with your account.[Contact us](/braintree/help?issue=DeclinedTransaction)for more information. | Hard |
| 2046 | Declined | The customer's bank is unwilling to accept the transaction. For credit/debit card transactions, the customer will need to contact their bank for more details regarding this generic decline; if this is a PayPal transaction, the customer will need to contact PayPal. | Soft |
| 2047 | Call Issuer. Pick Up Card | The customer’s card has been reported as lost or stolen by the cardholder and the card-issuing bank has requested that merchants keep the card and call the number on the back to report it. As an online merchant, you don’t have the physical card and can't complete this request – obtain a different payment method from the customer. | Hard |
| 2048 | Invalid Amount | The authorized amount is set to zero, is unreadable, or exceeds the allowable amount. Make sure the amount is greater than zero and in a suitable format. | Soft |
| 2049 | Invalid SKU Number | A non-numeric value was sent with the attempted transaction. Fix errors and resubmit with the transaction with the proper SKU Number. | Hard |
| 2050 | Invalid Credit Plan | There may be an issue with the customer’s card or a temporary issue at the card-issuing bank. The customer will need to contact their bank for more information or use a different payment method. | Hard |
| 2051 | Credit Card Number does not match method of payment | There may be an issue with the customer’s credit card or a temporary issue at the card-issuing bank. Have the customer attempt the transaction again – if the decline persists, ask for a different card or payment method. | Hard |
| 2052 | Invalid level III Purchase | Level III Data is inaccurate or missing. | Hard |
| 2053 | Card reported as lost or stolen | The card used was reported lost or stolen. The customer will need to contact their bank for more information or use a different payment method. | Hard |
| 2054 | Reversal amount does not match authorization amount | Either the refund amount is greater than the original transaction or the card-issuing bank does not allow[partial refunds](/braintree/docs/reference/request/transaction/refund#partial-refunds). The customer will need to contact their bank for more information or use a different payment method. | Hard |
| 2055 | Invalid Transaction Division Number | [Contact us](/braintree/help?issue=DeclinedTransaction)for more information regarding this error message. | Hard |
| 2056 | Transaction amount exceeds the transaction division limit | [Contact us](/braintree/help?issue=DeclinedTransaction)for more information regarding this error message. | Hard |
| 2057 | Issuer or Cardholder has put a restriction on the card | The customer will need to contact their issuing bank for more information. | Soft |
| 2058 | Merchant not Mastercard SecureCode enabled | The attempted card can't be processed without enabling[3D Secure](/braintree/docs/guides/3d-secure/overview)for your account.[Contact us](/braintree/help?issue=DeclinedTransaction)for more information regarding this feature or contact the customer for a different payment method. | Hard |
| 2059 | Address Verification Failed | PayPal was unable to verify that the transaction qualifies for[Seller Protection](https://www.paypal.com/webapps/mpp/security/seller-protection)because the address was improperly formatted. The customer should contact PayPal for more information or use a different payment method. | Hard |
| 2060 | Address Verification and Card Security Code Failed | Both the AVS and CVV checks failed for this transaction. The customer should contact PayPal for more information or use a different payment method. | Hard |
| 2061 | Invalid Transaction Data | There may be an issue with the customer’s card or a temporary issue at the card-issuing bank. Have the customer attempt the transaction again – if the decline persists, ask for a different card or payment method. | Hard |
| 2062 | Invalid Tax Amount | There may be an issue with the customer’s card or a temporary issue at the card-issuing bank. Have the customer attempt the transaction again – if the decline persists, ask for a different card or payment method. | Soft |
| 2063 | PayPal Business Account preference resulted in the transaction failing | You can't process this transaction because your account is set to[block certain payment types](https://www.paypal.com/selfhelp/article/FAQ2406/1), such as eChecks or foreign currencies. If you believe you have received this decline in error,[contact us](/braintree/help?issue=DeclinedTransaction). | Hard |
| 2064 | Invalid Currency Code | There may be an issue with the configuration of your account for the currency specified.[Contact us](/braintree/help?issue=DeclinedTransaction)for more information. | Hard |
| 2065 | Refund Time Limit Exceeded | PayPal requires that refunds are issued within 180 days of the sale. This refund can't be successfully processed. | Hard |
| 2066 | PayPal Business Account Restricted | [Contact PayPal’s Support team](/braintree/articles/guides/payment-methods/paypal/setup-guide#contacting-paypal-support)to resolve this issue with your account. Then, you can attempt the transaction again. | Hard |
| 2067 | Authorization Expired | The PayPal authorization is no longer valid. | Hard |
| 2068 | PayPal Business Account Locked or Closed | You'll need to[contact PayPal’s Support team](/braintree/articles/guides/payment-methods/paypal/setup-guide#contacting-paypal-support)to resolve an issue with your account. Once resolved, you can attempt to process the transaction again. | Hard |
| 2069 | PayPal Blocking Duplicate Order IDs | The submitted PayPal transaction appears to be a duplicate of a previously submitted transaction. This decline code indicates an attempt to prevent charging the same PayPal account twice for the same service. | Hard |
| 2070 | PayPal Buyer Revoked Pre-Approved Payment Authorization | The customer revoked authorization for this payment method. Reach out to the customer for more information or a different payment method. | Hard |
| 2071 | PayPal Payee Account Invalid Or Does Not Have a Confirmed Email | Customer has not finalized setup of their PayPal account. Reach out to the customer for more information or a different payment method. | Hard |
| 2072 | PayPal Payee Email Incorrectly Formatted | Customer made a typo or is attempting to use an invalid PayPal account. | Hard |
| 2073 | PayPal Validation Error | PayPal can't validate this transaction.[Contact us](/braintree/help?issue=DeclinedTransaction)for more details. | Hard |
| 2074 | Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | The customer’s payment method associated with their PayPal account was declined. Reach out to the customer for more information or a different payment method. | Hard |
| 2075 | Payer Account Is Locked Or Closed | The customer’s PayPal account can't be used for transactions at this time. The customer will need to contact PayPal for more information or use a different payment method. | Hard |
| 2076 | Payer Cannot Pay For This Transaction With PayPal | The customer should contact PayPal for more information or use a different payment method. You may also receive this response if you create transactions using the email address registered with your PayPal Business Account. | Hard |
| 2077 | Transaction Refused Due To PayPal Risk Model | PayPal has declined this transaction due to risk limitations. You'll need to[contact PayPal’s Support team](/braintree/articles/guides/payment-methods/paypal/setup-guide#contacting-paypal-support)to resolve this issue. | Hard |
| 2078 | Invalid Secure Payment Data | PIN cryptographic error found during decryption. | Soft |
| 2079 | PayPal Merchant Account Configuration Error | You'll need to[contact us](/braintree/help?issue=DeclinedTransaction)to resolve an issue with your account. Once resolved, you can attempt to process the transaction again. | Hard |
| 2080 | Invalid user credentials | Invalid user credentials. | Soft |
| 2081 | PayPal pending payments are not supported | PayPal Braintree received an unsupported Pending Verification response from PayPal. Contact[PayPal Braintree’s Support team](/braintree/help?issue=DeclinedTransaction)to resolve a potential issue with your account settings. If there is no issue with your account, have the customer reach out to PayPal for more information. | Hard |
| 2082 | PayPal Domestic Transaction Required | This transaction requires the customer to be a resident of the same country as the merchant. Reach out to the customer for a different payment method. | Hard |
| 2083 | PayPal Phone Number Required | This transaction requires the payer to provide a valid phone number. The customer should contact PayPal for more information or use a different payment method. | Hard |
| 2084 | PayPal Tax Info Required | The customer must complete their PayPal account information, including submitting their phone number and all required tax information. | Hard |
| 2085 | PayPal Payee Blocked Transaction | Fraud settings on your PayPal business account are blocking payments from this customer. These can be adjusted in the**Block Payments**section of your PayPal business account. | Hard |
| 2086 | PayPal Transaction Limit Exceeded | The settings on the customer's account do not allow a transaction amount this large. They will need to contact PayPal to resolve this issue. | Hard |
| 2087 | PayPal reference transactions not enabled for your account | PayPal API permissions are not set up to allow reference transactions. You'll need to[contact PayPal’s Support team](/braintree/articles/guides/payment-methods/paypal/setup-guide#contacting-paypal-support)to resolve an issue with your account. Once resolved, you can attempt to process the transaction again. | Hard |
| 2088 | Currency not enabled for your PayPal seller account | This currency is not currently supported by your PayPal account. You can accept additional currencies by[updating your PayPal profile](https://www.paypal.com). | Hard |
| 2089 | PayPal payee email permission denied for this request | PayPal API permissions are not set up between your PayPal business accounts.[Contact us](/braintree/help?issue=DeclinedTransaction)for more information. | Hard |
| 2090 | PayPal or Venmo account not configured to refund more than settled amount | Your PayPal or Venmo account is not set up to refund amounts higher than the original transaction amount.[Contact PayPal's Support team](/braintree/articles/guides/payment-methods/paypal/setup-guide#contacting-paypal-support)for information on how to enable this for your PayPal account. | Hard |
| 2091 | Currency of this transaction must match currency of your PayPal account | Your PayPal account can only process transactions in the currency of your home country.[Contact PayPal's Support team](/braintree/articles/guides/payment-methods/paypal/setup-guide#contacting-paypal-support)for more information. | Hard |
| 2092 | No Data Found - Try Another Verification Method | The processor is unable to provide a definitive answer about the customer's bank account. Please try a different US bank account verification method. | Soft |
| 2093 | PayPal payment method is invalid | The PayPal payment method has either expired or been canceled. | Hard |
| 2094 | PayPal payment has already been completed | Your integration is likely making PayPal calls out of sequence. Check the error response for more details. | Hard |
| 2095 | PayPal refund is not allowed after partial refund | Once a PayPal transaction is partially refunded, all subsequent refunds must also be partial refunds for the remaining amount or less. Full refunds are not allowed after a PayPal transaction has been partially refunded. | Hard |
| 2096 | PayPal buyer account can't be the same as the seller account | PayPal buyer account can't be the same as the seller account. | Hard |
| 2097 | PayPal authorization amount limit exceeded | PayPal authorization amount is greater than the allowed limit on the order. | Hard |
| 2098 | PayPal authorization count limit exceeded | The number of PayPal authorizations is greater than the allowed number on the order. | Hard |
| 2099 | Cardholder Authentication Required | The customer's bank declined the transaction because a 3D Secure authentication was not performed during checkout. Have the customer authenticate using 3D Secure, then attempt the authorization again. | Soft |
| 2100 | PayPal channel initiated billing not enabled for your account | Your PayPal permissions are not set up to allow channel initiated billing transactions.[Contact PayPal's Support team](/braintree/articles/guides/payment-methods/paypal/setup-guide#contacting-paypal-support)for information on how to enable this. Once resolved, you can attempt to process the transaction again. | Hard |
| 2101 | Additional authorization required | This transaction requires additional customer credentials for authorization. The customer should insert their chip. | Soft |
| 2102 | Incorrect PIN | The entered PIN was incorrect. | Soft |
| 2103 | PIN try exceeded | The allowable number of PIN tries has been exceeded. | Soft |
| 2104 | Offline Issuer Declined | The transaction was declined offline by the issuer. The customer will need to contact their bank for more information. | Soft |
| 2105 | Cannot Authorize at this time (Life cycle) | The transaction is refused due to invalid card data. Please try again later. | Soft |
| 2106 | Cannot Authorize at this time (Policy) | The transaction is refused due to a policy reason. Please try again later. | Soft |
| 2107 | Card Not Activated | The transaction is from a new cardholder, and the card has not been properly unblocked. | Hard |
| 2108 | Closed Card | The account is closed. Re-validate the account number for accuracy and do not reattempt with the same PAN or token. | Hard |
| 2109-2999 | Processor Declined | The customer's bank is unwilling to accept the transaction. The customer will need to contact their bank for more details regarding this generic decline. | Soft |
| 3000 | Processor Network Unavailable – Try Again | This response could indicate a problem with the back-end processing network, not necessarily a problem with the payment method. Have the customer attempt the transaction again – if the decline persists,[contact us](/braintree/help?issue=DeclinedTransaction)for more information. | Soft |

