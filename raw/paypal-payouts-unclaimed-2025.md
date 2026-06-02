<!-- Source URL: https://docs.paypal.ai/growth/payouts/manage-payouts/handle-unclaimed-payouts -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Handle unclaimed payouts

When recipients do not claim their payouts, the status of the payout items remains `UNCLAIMED`. Typically, unclaimed payouts can occur due to:

- Incorrect recipient details such as email address or mobile number.
- Unverified email addresses.
- Unaccepted payments in the recipient's PayPal account.

Track and resolve unclaimed payouts promptly to avoid delays and improve the payment success rate. If not, these payouts expire in 30 days, and PayPal automatically returns the money to your PayPal account.

## Track unclaimed payouts

<a href="/growth/payouts/manage-payouts/reports-transaction-logs#generate-activity-report" target="_blank" rel="noopener noreferrer">Download the Activity report</a> to view the details of the payout items. To view the unclaimed payouts, filter the status column for `UNCLAIMED`.

## Resolve unclaimed payouts

Verify recipient details, such as email address and phone number.

1. If the recipient details are incorrect:
   1. <a href="/growth/payouts/manage-payouts/cancel-reverse-payouts#cancel-payout-item" target="_blank" rel="noopener noreferrer">Cancel the payout item</a>.
   2. <a href="/growth/payouts/send-money/use-payouts-api#1-create-payout-batch" target="_blank" rel="noopener noreferrer">Create a new payout</a> with the correct recipient information.
2. If the recipient details are correct:
   1. Contact the recipient to verify their email address and phone number.
   2. If the recipient has not verified their email address, notify them to confirm it.
   3. If the recipient has not accepted the payment, notify your recipient to log in to their PayPal account and accept the payment.

## Best practices to reduce unclaimed payouts

- Validate recipient data before initiating payouts.
- Notify payout timelines to recipients.
- Monitor payout statuses regularly to track and resolve issues.
