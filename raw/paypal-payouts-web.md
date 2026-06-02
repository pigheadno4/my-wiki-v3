---
title: Payouts Web
slug: /docs/payouts/standard/payouts-web/
createTime: "2024-08-15T07:14:39.853Z"
updateTime: "2025-05-12T10:53:25.969Z"
---

# Payouts Web

Payouts Web enables you to send up to 5,000 payments per file using a .csv (comma separated value) file. This page explains everything you need to know about making payouts using Payouts Web.

## 1. Enable Payouts Web

To send payout requests from Payouts Web, contact your account manager or call 1-888-221-1161. When your account is approved for payouts, complete the steps on this page.

## 2. Create a payment file

- Open a basic text editor, spreadsheet, or database application.

- In the first row, enter the following payout information for the first recipient, from left to right.

| Column | Payout information        |
| ------ | ------------------------- |
| 1      | **Recipient identifier**— |

                          Required. Use one of the following: - Email address

- Domestic mobile telephone number (required for payouts to Venmo)
- PayPal PayerID —
  If you use PayPal Checkout or an Account Authentication Service, such as Log in with PayPal, these APIs return the PayPal PayerID in the transaction's response message.
- Venmo handle
  —
  Applicable only for Venmo payouts. |
  | 2 | **Payment amount**—
  Required. Use the correct currency format. For example, senders in Italy enter5,45and senders in the U.S. enter5.45. For currencies that use a comma, enclose the amount in double quotes. For example,"100,45". If the format is incorrect, PayPal gives you the correct format when you upload the file. |
  | 3 | **Currency**—
  Required. Three-letter[currency code](/reference/currency-codes/). Currency codes are not case sensitive. For example,usdandUSDare both acceptable for U.S. dollars.**Notes:**Enter one currency type per payment file. To send payouts in multiple currencies, create a separate payment file for each currency. A few countries have[currency restrictions](/docs/payouts/standard/reference/currency-conversion/#restrictions). If your Payouts request does not comply with a country's currency restrictions, that portion of your request will fail with an error message. |
  | 4 | **Customer ID**—
  Optional. Unique identifier with 30 character maximum. Cannot contain spaces. If the customer ID contains a comma, enclose the text in double quotes. |
  | 5 | **Note to Recipient**—
  Optional for PayPal, required for Venmo. Message the sender writes. If sending to a PayPal recipient, the message is sent only to the recipient. If sending to a Venmo recipient, the message inherits the privacy setting of the recipient. 400 character maximum. If the custom note contains a comma, enclose the text in double quotes. |
  | 6 | **Recipient Wallet**—
  Required. Choose to send payouts toPAYPALorVENMOrecipients. The default is PayPal. Payouts to Venmo require a note and a US mobile phone number for the recipient. |
  | 7 | **social_feed_privacy**—
  Optional for Venmo only. Controls whether a payment appears in a recipient's feed. Use one of the following: - PUBLIC —
  The payment displays on the recipient's public Venmo feed
- FRIENDS_ONLY —
  The payment displays only to the recipient's Venmo friends
- PRIVATE —
  The payment displays only on the recipient's personal feed. Defaults to PRIVATE if left blank. |
  | 8 | **holler_url
  [deprecated]**—
  Optional for Venmo only. Link to a Holler sticker. For Venmo recipients, the sticker displays with the payout message. The maximum URL lengh is 151 characters. |
  | 9 | **logo_url**—
  Optional for Venmo only. Link to a logo that displays as the sender's profile image in the recipient's Venmo feed. Used to add or update the business profile image. The maximum image size is 1024 x 1024 pixels. The image should be square. The maximum URL length is 2000 characters. |
  | 10 | **Purpose**—
  Optional. Denotes the purpose of the transaction. The default value isGOODSif the purpose is not provided. Purpose can be set to:- AWARDS
- PRIZES
- DONATIONS
- GOODS
- SERVICES
- REBATES
- CASHBACK
- DISCOUNTS
- NON_GOODS_OR_SERVICES |

  This example shows the payment information for a U.S. recipient:

  mbrown@email.com,100.5,USD,ID001,Here is your payment,PAYPAL. This example shows payment information for a recipient in Germany. Because the EUR currency uses a comma separator, the payment amount is enclosed in double quotes:

  mbrown@myco.com,"100,50",EUR,ID001,Here is your payment, PAYPAL.

- Add a new row for each recipient.

  **Note:** The maximum is 5,000 recipients per payment file.

- When you complete the payment information for all recipients, save the file in .csv format.

## 3. Upload a payment file

Check the file meets these requirements before uploading:

- The format of the payment file is .csv .
- The payment file contains only one currency type.
- Your PayPal or Venmo account balance contains enough funds to cover the total cost of the payouts request.
- Your PayPal balance is the same currency as your payouts request unless you plan to use [currency conversion](/docs/payouts/standard/reference/currency-conversion/) .

Here's how to upload the file:

- Log in to your PayPal account at [https://www.paypal.com](https://www.paypal.com) .
- Click **Money** at the top of the Summary page and then **Send Money** on the left.
- Click **Make a Mass Payment** .
- From the Choose Payouts Recipients page, click **Browse** , select your payment file, and then click **Open** . If you upload a file with the same content as a file you've uploaded within 30 days, PayPal lets you know it could be a duplicate payout.
- (Optional) Enter text in the **Email subject** and **Custom message for recipient** .
- Click **Continue** .
  PayPal scans your payment file for errors. If the file is valid, the Review Your Payments Details page displays.
- Click **Send Payout** to process your payments file.
  The page displays Your payment has been sent . You can then choose to **Send another Payout** or **View Activity Details.**

## 4. Review transaction details

After you submit the payment file, click **View Activity Details** on the final payouts page to view transaction details. You can also view details from the Recent activity section of the Summary page or the Activity page of your PayPal account.

If the transaction status is Submitted, wait for the status to change to Processed or Completed to see the number of unclaimed payments.

PayPal places a temporary hold on the total monetary value of the payouts request, plus fees, until the transaction status is Processed. After the hold, if one or more transactions are declined, your PayPal account balance may be greater than the balance shown during the hold.

For more information, see [View Reports](/docs/payouts/standard/reports/) and [payout record status](/docs/payouts/standard/reference/payment-processing/#payout-record-status)

## Next

Customize your [Payouts Web](/docs/payouts/standard/payouts-web/customize) .
