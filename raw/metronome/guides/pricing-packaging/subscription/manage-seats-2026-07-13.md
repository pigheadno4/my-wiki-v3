<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/subscription/manage-seats.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage seats

Understand how to change the number of seats on a subscription, monitor active balance, and poll history of edits.

## Change seat count

Once a contract is created, you can edit the amount of seats on the subscription using the [edit contract end point](/api-reference/contracts/edit-a-contract). The mechanism for changing seat count depends on whether you are using the `quantity` field to adjust count or the `seat_config`.

### Quantity change​ for standard subscriptions and credit pools

Schedule a change of the quantity of a subscription using the `update_subscription` action on the [edit contract endpoint](/api-reference/contracts/edit-a-contract). Either pass the new total count through `quantity` or the difference between the previous count through `quantity_delta`. Updates scheduled with the same `starting_at` are applied in the order they are submitted in. Quantity changes are invoiced based on the proration settings in the subscription configuration on the contract.

For subscriptions linked to recurring credits, the change in `quantity` will also release new credit balance. The balance amount depends the proration settings and `access_amount` on the recurring credit configuration.

This call shows an example of using `/contracts/edit` to change a subscription seat count:

```json theme={null}
{
    "customer_id": "68cd7fb2-235a-4d4d-9ee3-15c49e866884",
    "contract_id": "7f865c1b-1c08-40e8-9c09-b3238fd3b50d",
    "update_subscriptions": [
        {
            "subscription_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            "quantity_updates": [
                {
                    "quantity": 3,
                    "starting_at": "2025-04-29T00:00:00.000Z"
                }
            ]
        }
    ]
}
```

### Quantity change​ for seat-based credit subscriptions

As opposed to just changing the `quantity`, specify the `seat_ids` which are being added or removed from the subscription. Optionally add or remove unassigned seats. Invoices are billed and credits are released based on the settings of the subscription and recurring credits configs.

See an example of changing the seat count for seat-based credit subscriptions:

```json theme={null}
{
    "customer_id": "1f79c5c6-400a-4be4-9573-30c667454e4c",
    "contract_id": "2159a5c1-7436-43eb-a46c-7a2e5f030afa",
    "update_subscriptions": [
        {
            "subscription_id": "16de7fa0-b387-44e9-b521-0945db3b8af8",
            "seat_updates": {
                "add_seat_ids": [
                    {
                        "seat_ids": ["customer4@metronome.com"],
                        "starting_at": "2025-12-01T00:00:00Z"
                    }
                ],
                "remove_seat_ids": [
                     {
                         "seat_ids": ["customer2@metronome.com"],
                         "starting_at": "2025-11-15T00:00:00Z"
                     }
                 ],
                 "add_unassigned_seats": [
                     {
                         "quantity": 2,
                         "starting_at": "2025-10-01T00:00:00Z"
                     }
                 ]
            }
        }
    ]
}
```

### Removing a seat ID while maintaining total quantity

In certain cases, your customers may change who has access to a seat. As people change roles or leave their company, they may want to free up the seat for someone else to use. To do this in Metronome, remove the seat ID and add an unassigned seat. This ensures that the total quantity for the subscription stays the same, but that a seat is now available for someone else to use.

This example removes a seat ID and adds an unassigned in the same call:

```json theme={null}
{
    "customer_id": "1f79c5c6-400a-4be4-9573-30c667454e4c",
    "contract_id": "2159a5c1-7436-43eb-a46c-7a2e5f030afa",
    "update_subscriptions": [
        {
            "subscription_id": "16de7fa0-b387-44e9-b521-0945db3b8af8",
            "seat_updates": {
                "remove_seat_ids": [
                     {
                         "seat_ids": ["customer1@metronome.com"],
                         "starting_at": "2025-11-15T00:00:00Z"
                     }
                 ],
                 "add_unassigned_seats": [
                     {
                         "quantity": 1,
                         "starting_at": "2025-11-15T00:00:00Z"
                     }
                 ]
            }
        }
    ]
}
```

## Monitor credit balance

You can set [threshold notifications](/guides/customers-billing/set-up-notifications/create-and-manage-notifications) on credit balance to receive webhooks when the customer's balance reaches a certain level. Upon receiving these webhooks, you can gate the customer’s access until they purchase a top-up credit pack or the next billing period begins. This alert will only evaluate credits at the customer or contract level - seat scoped credits are not included in the calculation.

This API call shows how to create a threshold notification when the customer has 10 AI credits remaining using the [/alerts/create](/api-reference/alerts/create-a-threshold-notification) end point.

```json theme={null}
{  
    "alert_type": "low_remaining_contract_credit_and_commit_balance_reached",  
    "credit_type_id": "d3cb2827-dcb5-44af-9354-947a7197b9a6",  
    "threshold": 10,  
    "name": "10 AI credits remaining reached",  
    "customer_id": "d8319d6f-8ee0-43a7-b76f-d7587c0a811c"  
}
```

To set up a threshold notification for seat scoped credits and commits, create a `low_remaining_seat_balance_reached` notification using the [/alerts/create](/api-reference/alerts/create-a-threshold-notification) end point.

The `seat_filter` parameter, required on the request body when creating this notification, provides a `seat_group_key` field which is used to scope the notification to seat balances associated with seat-based subscriptions with a specific `seat_group_key` in their `seat_config` configuration.

This API call shows how to create a threshold notification when a customer has 15 AI credits remaining for any seat on a subscription with a `seat_group_key` of `seat_id`.

```bash theme={null}
curl https://api.metronome.com/v1/alerts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "alert_type": "low_remaining_seat_balance_reached",
    "threshold": 15,
    "name": "15 AI credits remaining reached",
    "credit_type_id": "d3cb2827-dcb5-44af-9354-947a7197b9a6",
    "customer_id": "d8319d6f-8ee0-43a7-b76f-d7587c0a811c",
    "seat_filter": { "seat_group_key": "seat_id" }
  }'
```

To retrieve the alert state for a specific seat, use the [/customer-alerts/get](/api-reference/alerts/get-an-alert) end point.

Here's an example of retrieving the alert state for a specific seat:

```bash theme={null}
curl https://api.metronome.com/v1/customer-alerts/get \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
        "customer_id": "5cceec38-51fe-4399-8bed-fcb2a8ad1fb7",
        "alert_id": "e9c0d89d-040e-4ffc-91f6-001c6954d7a7"
        "seat_filter": {"seat_group_key": "seat_id", "seat_group_value": "seat123"}
    }'
```

Optionally, use the `seat_filter.seat_group_value` parameter to scope the notification to a specific seat.

Here's an example of creating a threshold notification when a customer has 5 AI credits remaining for a specific seat on a subscription with a `seat_group_key` of `seat_id` and a `seat_group_value` of `seat123`.

```bash theme={null}
curl https://api.metronome.com/v1/alerts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "alert_type": "low_remaining_seat_balance_reached",
    "threshold": 5,
    "name": "5 AI credits remaining reached",
    "credit_type_id": "d3cb2827-dcb5-44af-9354-947a7197b9a6",
    "customer_id": "d8319d6f-8ee0-43a7-b76f-d7587c0a811c",
    "seat_filter": {"seat_group_key": "seat_id", "seat_group_value": "seat123"}
  }'
```

## Visualize seat history

As part of your product experience, you may want to present the change in seat quantity over time to provide transparency to your customer:

* **Quantity history:** To poll the changes to subscription quantity, use the [/getSubscriptionQuantityHistory](/api-reference/contracts/get-subscription-quantity-history) end point.
* **Seat id history:** If managing seats using the `seat_config`, you can poll the history of each `seat_id` using the [/get-subscription-seats-history](/api-reference/contracts/get-subscription-seats-history) end point.

## Visualize seat balance

If building a seat-scoped subscription billing model, you likely will want to display the active balance per seat and seat's balance over time. To query this information, use the [/contracts/seatBalances/list](/api-reference/credits-and-commits/list-seat-balances) endpoint:

* **Current seat balance:** Passing the `customer_id` and `contract_id` will return the current `balance` for all seats. Passing a `seat_id` to the request body will scope the results to an individual seat.
* **Seat ledger history:** To create a view which shows the history of credit grants and associated burn-down, pass `include_ledgers: true` to the request body. Optionally pass in the `starting_at` and `ending_before` dates to filter the response to a specified time period.
