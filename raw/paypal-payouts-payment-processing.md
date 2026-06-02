<!-- Source URL: https://developer.paypal.com/docs/payouts/standard/reference/payment-processing/ -->

## <!-- Fetched: 2026-04-16 -->

title: Payouts payment processing
slug: /docs/payouts/standard/reference/payment-processing/
createTime: '2024-08-15T06:18:11.839Z'
updateTime: '2025-05-13T11:10:39.511Z'

---

# Payouts payment processing

When your payout is successfully processed, recipients that already have a PayPal or Venmo account get their payment instantly. Recipients without a PayPal or Venmo account receive a notification that a payment is available. If a payment is unclaimed after 30 days, the money is returned to your account.

PayPal sends you a summary email for each payout. You can log in to your PayPal account and [get payouts transaction logs](/docs/payouts/standard/reports/view-transaction-activities/#get-payouts-transaction-logs) .

## Payout record status

Payout records can have a status of:

|           |                                                                                                                                                                                                                                                    |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New       | Your request for a payout has been received.                                                                                                                                                                                                       |
| Pending   | Your payout request has been submitted and is being processed. The recipient will get the funds once the request is processed successfully. If the recipient doesn't claim this payout, the funds will be returned to you.                         |
| Success   | Funds have been credited to the recipient’s account.                                                                                                                                                                                               |
| Unclaimed | The recipient for this payout doesn't have a PayPal account. PayPal sent the recipient a signup link to create an account. If the recipient doesn't create an account and claim the payout within 30 days, the funds are returned to your account. |
| Refunded  | The funds have been refunded back to your account. This is because the recipient, such as a PayPal Business verified account, has issued a refund for the payout that you initiated.                                                               |
| Failed    | This payout request failed, so funds aren't deducted from the sender’s account.                                                                                                                                                                    |
| On Hold   | This payout request is under review and on hold.                                                                                                                                                                                                   |
| Blocked   | This payout request has been blocked.                                                                                                                                                                                                              |
| Denied    | This payout has been denied, so funds were not deducted from your account.                                                                                                                                                                         |
| Returned  | The funds have been returned to your account. This can be because the recipient hasn't claimed this payout, or you have cancelled the payout.                                                                                                      |
