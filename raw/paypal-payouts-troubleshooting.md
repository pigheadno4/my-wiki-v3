<!-- Source URL: https://developer.paypal.com/docs/payouts/standard/reference/troubleshooting/ -->

## <!-- Fetched: 2026-04-16 -->

title: Payouts troubleshooting
slug: /docs/payouts/standard/reference/troubleshooting/
createTime: '2024-08-15T05:50:34.938Z'
updateTime: '2024-08-15T05:50:35.182Z'

---

# Payouts troubleshooting

Use this information to troubleshoot Payouts transactions:

## API error messages

For a description of API error messages, see [Error Codes](/docs/api/payments.payouts-batch/v1/#errors) in the Payouts API Reference or the [Activity log and error codes](/docs/payouts/standard/reports/view-transaction-activities/#transaction-activity-log-error-and-reason-codes) table.

## Incorrect email address

If the recipient's email address was entered incorrectly, you'll need to resend their payment.

- Log in to your PayPal business account and make sure you have enough money in your PayPal balance to cover the total cost of the payout.
- Create a .CSV or .TXT file with the recipient's corrected email address, payment amount, and currency type.
- Upload and submit your payout.

## Recipient did not receive the email

If you suspect the email may have been redirected to a recipient's spam folder, ask your recipient to log in to their PayPal account to view the payment.

## Reverse payments

PayPal is unable to reverse funds for any incorrect recipient email addresses or mobile phone numbers included in an uploaded file unless the money is unclaimed after 30 days.

## Unclaimed payments

If money is not claimed within 30 days, PayPal will return the money to your PayPal account. Go to your transaction history to view any unclaimed payments.

## Additional information

- [FAQs](/docs/payouts/standard/reference/faq/)
