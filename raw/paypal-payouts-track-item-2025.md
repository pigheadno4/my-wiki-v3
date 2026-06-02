<!-- Source URL: https://docs.paypal.ai/growth/payouts/send-money/track-payout-item-status -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Track payout item status

You can track the status of the individual payout items in a payout batch.

Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a GET call to the `/v1/payments/payouts-item/{PAYOUT-ITEM-ID}` endpoint.<br />
**Path parameter**: `PAYOUT-ITEM-ID` is the `payout_item_id` returned as part of the <a href="/growth/payouts/send-money/use-payouts-api#2-track-status" target="_blank" rel="noopener noreferrer">payout batch details</a> response.

<CodeGroup>
  ```bash Sample request lines theme={null}
  curl -v -X GET https://api-m.sandbox.paypal.com/v1/payments/payouts-item/8AELMXH8UB2P8 \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer ACCESS-TOKEN'  
  ```

```json Sample response lines expandable theme={null}
{
  "payout_item_id": "8AELMXH8UB2P8",
  "transaction_id": "0C413693MN970190K",
  "activity_id": "0E158638XS0329106",
  "transaction_status": "SUCCESS",
  "payout_item_fee": {
    "currency": "USD",
    "value": "0.35"
  },
  "payout_batch_id": "Q8KVJG9TZTNN4",
  "sender_batch_id": "Payouts_1753867886",
  "payout_item": {
    "recipient_type": "EMAIL",
    "amount": {
      "value": "9.87",
      "currency": "USD"
    },
    "note": "Thanks for your patronage!",
    "receiver": "receiver@example.com",
    "sender_item_id": "14Feb_234",
    "recipient_wallet": "PAYPAL",
    "purpose": "GOODS"
  },
  "time_processed": "2018-01-27T10:17:41Z",
  "links": [
    {
      "rel": "self",
      "href": "https://api-m.sandbox.paypal.com/v1/payments/payouts-item/8AELMXH8UB2P8",
      "method": "GET",
      "encType": "application/json"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/payments/payouts/Q8KVJG9TZTNN4",
      "rel": "batch",
      "method": "GET",
      "encType": "application/json"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `200 OK` response. The response includes the `transaction_status` parameter, which indicates the current status of the payout item.

The following table summarizes the possible values of `transaction_status` and what they mean:

| Status      | Description                                                                                                                                                                                                                                                                                                                                                                                    | Possible management action                                                                                                                                                                                 |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SUCCESS`   | PayPal has completed processing the payout and credited the money to the recipient's account.                                                                                                                                                                                                                                                                                                  | No action required.                                                                                                                                                                                        |
| `FAILED`    | The payout has failed. PayPal does not deduct money from your account.                                                                                                                                                                                                                                                                                                                         | Review the failure reason and <a href="/growth/payouts/send-money/use-payouts-api#1-create-payout-batch" target="_blank" rel="noopener noreferrer">create a new payout request</a> if needed.              |
| `PENDING`   | PayPal is processing the payout.                                                                                                                                                                                                                                                                                                                                                               | Check the status again later.                                                                                                                                                                              |
| `UNCLAIMED` | The recipient has not claimed the payout. This typically occurs when the recipient does not have a PayPal or Venmo account. PayPal sends a signup link, and the payout status remains unclaimed until claimed or returned. For more information, see <a href="/growth/payouts/manage-payouts/handle-unclaimed-payouts" target="_blank" rel="noopener noreferrer">Handle unclaimed payouts</a>. | Notify the recipient to claim the payout.                                                                                                                                                                  |
| `RETURNED`  | PayPal has returned the money to your account. This occurs when the recipient does not claim the payout or you cancel it.                                                                                                                                                                                                                                                                      | <a href="/growth/payouts/send-money/use-payouts-api#1-create-payout-batch" target="_blank" rel="noopener noreferrer">Create a new payout request</a> if needed.                                            |
| `ONHOLD`    | PayPal has temporarily placed the payout on hold.                                                                                                                                                                                                                                                                                                                                              | Check the status again later.                                                                                                                                                                              |
| `BLOCKED`   | PayPal has blocked the payout.                                                                                                                                                                                                                                                                                                                                                                 | Review the reason, resolve the issues, and <a href="/growth/payouts/send-money/use-payouts-api#1-create-payout-batch" target="_blank" rel="noopener noreferrer">create a new payout request</a> if needed. |
| `REFUNDED`  | The recipient has refunded the payout. PayPal returns the money to your account.                                                                                                                                                                                                                                                                                                               | No action required.                                                                                                                                                                                        |
| `REVERSED`  | PayPal has reversed the payout. PayPal returns the money to your account. <Note>This status is specific to payouts created through web uploads.</Note>                                                                                                                                                                                                                                         | No action required.                                                                                                                                                                                        |
