<!-- Source URL: https://docs.paypal.ai/growth/payouts/manage-payouts/cancel-or-reverse-payouts -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel or reverse payouts

You can use the procedure and information in this section to cancel unclaimed payouts and understand payout reversals.

## Cancel payout item

You can cancel a payout item only if its status is `UNCLAIMED`. Use the PayPal business account dashboard or the Payouts API to cancel unclaimed payout items.

To implement payment cancellation functionality, you can use the [Dashboard](#dashboard) or the [API](#api).

<Note>Unclaimed payouts expire in 30 days, and PayPal returns the money to your PayPal account.</Note>

<Tabs>
  <Tab title="Dashboard">
    1. Log into your <a href="https://www.paypal.com" target="_blank" rel="noopener noreferrer">PayPal business account</a>.
    2. Select **Activity** > **Transactions** > **All Transactions**.
    3. On the **Transactions** page:
       1. Select **Email address** from the drop-down list.
       2. Enter the recipient's email address in the search box.
       3. Select **Filter**.
       4. Select the date range.
       5. Select **Apply Filters**. The search results display the transaction list that matches your criteria.
    4. Select the title of the unclaimed payment you want to cancel.
    5. On the details page, select **Cancel** and follow the on-screen instructions.
  </Tab>

  <Tab title="API">
    Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank">valid access token</a> and make a POST call to the `/v1/payments/payouts-item/{PAYOUT-ITEM-ID}/cancel` endpoint. <br />
    **Path parameter**: `PAYOUT-ITEM-ID` is the `payout_item_id` returned in the <a href="/reference/api/rest/payouts/show-payout-batch-details" target="_blank" rel="noopener noreferrer">Show payout batch details</a> response.

    <CodeGroup>
      ```bash Sample request lines theme={null}
      curl -v -X POST https://api-m.sandbox.paypal.com/v1/payments/payouts-item/5KUDKLF8SDC7S/cancel \
          -H 'Content-Type: application/json' \
          -H 'Authorization: Bearer ACCESS-TOKEN' \
          -d '{}'
      ```

      ```json Sample response lines expandable theme={null}
      {
        "payout_item_id": "5KUDKLF8SDC7S",
        "transaction_id": "1DG93452WK758815H",
        "activity_id": "0E158638XS0329101",
        "transaction_status": "RETURNED",
        "payout_item_fee": {
          "currency": "USD",
          "value": "0.35"
        },
        "payout_batch_id": "CQMWKDQF5GFLL",
        "sender_batch_id": "Payouts_2018_100006",
        "payout_item": {
          "recipient_type": "EMAIL",
          "amount": {
            "value": "9.87",
            "currency": "USD"
          },
          "note": "Thanks for your patronage!",
          "receiver": "receiver@example.com",
          "sender_item_id": "14Feb_234"
        },
        "time_processed": "2018-01-27T10:17:41Z",
        "errors": {
          "name": "RECEIVER_UNREGISTERED",
          "message": "Receiver is unregistered",
          "information_link": "https://developer.paypal.com/docs/api/payments.payouts-batch#errors"
        },
        "links": [
          {
            "rel": "self",
            "href": "https://api-m.sandbox.paypal.com/v1/payments/payouts-item/5KUDKLF8SDC7S",
            "method": "GET"
          },
          {
            "rel": "batch",
            "href": "https://api-m.sandbox.paypal.com/v1/payments/payouts/CQMWKDQF5GFLL",
            "method": "GET"
          }
        ]
      }
      ```
    </CodeGroup>

    A successful call returns a `200 OK` response with a JSON response body that shows payout item details.

  </Tab>
</Tabs>

## Understand payout reversals

PayPal cannot reverse payments that a payer sends to an incorrect email address or phone number. However, if the status of the payout item is `UNCLAIMED`, a payer can [cancel the payout item](#cancel-payout-item) and create a new payout with the correct recipient details.
If not, all unclaimed payouts expire in 30 days, and PayPal returns the money to the payer's PayPal account.
