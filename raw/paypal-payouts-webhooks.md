<!-- Source URL: https://developer.paypal.com/docs/payouts/standard/reference/webhooks/ -->

## <!-- Fetched: 2026-04-16 -->

title: Payouts webhook event names
slug: /docs/payouts/standard/reference/webhooks/
createTime: '2024-08-15T06:02:08.625Z'
updateTime: '2024-08-15T06:02:08.872Z'

---

# Payouts webhook event names

**Note:** The PAYOUTSBATCH webhooks do not contain item-related information.

To get item-related information, use the [HATEOAS links](/api/rest/responses/#hateoas-links) from the webhooks response.

| Event                           | Trigger                                                    | Related method                                                                           |
| ------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| PAYMENT.PAYOUTSBATCH.DENIED     | A batch payout payment is denied.                          | [Show payout details](/docs/api/payments.payouts-batch/v1/#payouts_get)                  |
| PAYMENT.PAYOUTSBATCH.PROCESSING | The state of a batch payout payment changes to processing. | [Show payout details](/docs/api/payments.payouts-batch/v1/#payouts_get)                  |
| PAYMENT.PAYOUTSBATCH.SUCCESS    | A batch payout payment completes successfully.             | [Show payout details](/docs/api/payments.payouts-batch/v1/#payouts_get)                  |
| PAYMENT.PAYOUTS-ITEM.BLOCKED    | A payouts item is blocked.                                 | [Show payout item details](/docs/api/payments.payouts-batch/v1/#payouts-item_get)        |
| PAYMENT.PAYOUTS-ITEM.CANCELED   | A payouts item is canceled.                                | [Cancel unclaimed payout item](/docs/api/payments.payouts-batch/v1/#payouts-item_cancel) |
| PAYMENT.PAYOUTS-ITEM.FAILED     | A payouts item fails.                                      | [Show payout item details](/docs/api/payments.payouts-batch/v1/#payouts-item_get)        |
| PAYMENT.PAYOUTS-ITEM.HELD       | A payouts item is held.                                    | [Show payout item details](/docs/api/payments.payouts-batch/v1/#payouts-item_get)        |
| PAYMENT.PAYOUTS-ITEM.REFUNDED   | A payouts item is refunded.                                | [Show payout item details](/docs/api/payments.payouts-batch/v1/#payouts-item_get)        |
| PAYMENT.PAYOUTS-ITEM.RETURNED   | A payouts item is returned.                                | [Show payout item details](/docs/api/payments.payouts-batch/v1/#payouts-item_get)        |
| PAYMENT.PAYOUTS-ITEM.SUCCEEDED  | A payouts item succeeds.                                   | [Show payout item details](/docs/api/payments.payouts-batch/v1/#payouts-item_get)        |
| PAYMENT.PAYOUTS-ITEM.UNCLAIMED  | A payouts item is unclaimed.                               | [Show payout item details](/docs/api/payments.payouts-batch/v1/#payouts-item_get)        |
