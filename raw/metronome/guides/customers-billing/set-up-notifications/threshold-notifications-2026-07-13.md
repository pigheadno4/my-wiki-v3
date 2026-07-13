<!-- Source URL: https://docs.metronome.com/guides/customers-billing/set-up-notifications/threshold-notifications.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Threshold notifications

Threshold notifications monitor real-time metrics and trigger when defined thresholds are crossed. They're best for proactive monitoring and usage-driven workflows.

Threshold notifications fall into three main categories:

* **Commit and Credit threshold notifications** monitor remaining balances of commits or credits. They can be used to notify a customer when they've used 90% of their commit, or to flag accounts that are close to running out of prepaid credits.

<Info>
  **INFO**

  Commit and credit threshold notifications alert on the balance of both customer and contract level commits and credits. [Individual seat-scoped credits](https://docs.metronome.com/guides/pricing-packaging/subscription/provision-your-customer#individual-seat-credit) are not included in the threshold calculation for these notifications.
</Info>

* **Spend and Usage threshold notifications** track how much a customer has spent or used over a given billing cycle. They can be used to trigger a message when a customer crosses a spend threshold, such as \$5,000, or to power logic for offering upgrades once a customer approaches a certain usage cap.
* **Invoice threshold notifications** monitor invoice totals after commits and credits have been applied to customer spend. They can be used to proactively notify customers when spend surpasses pre-configured budgets.

## Threshold notification types

<AccordionGroup>
  <Accordion title="Commit & Credit Notifications">
    #### Contract credit balance

    **Alert Type:** `alerts.low_remaining_contract_credit_balance_reached`

    Triggers when a customer's credit balance reaches or drops below a set amount. If multiple credits exist for a customer, Metronome sums up the remaining balances across all credits to compare against the threshold.

    To notify on a specific credit, set a custom field on the credit in Metronome and use advanced filters to evaluate only credits with that specific custom field value.

    #### Contract credit percentage

    **Alert Type:** `alerts.low_remaining_contract_credit_percentage_reached`

    Triggers if the customer's percentage of available credits on all active credits of that credit type (currency or pricing unit) reaches or goes below a set threshold.

    To notify on a specific credit, set a custom field on the credit in Metronome and use advanced filters to evaluate only credits with that specific custom field value.

    #### Commitment balance

    **Alert Type:** `alerts.low_remaining_commit_balance_reached`

    Triggers when a customer's commit balance reaches or drops below a set amount. If multiple commits exist for a customer, Metronome sums up the remaining balances across all commits to compare against the threshold.

    To notify on a specific commit, set a custom field on the commit in Metronome and use advanced filters to evaluate only commits with that specific custom field value.

    #### Commitment percentage

    **Alert Type:** `alerts.low_remaining_commit_percentage_reached`

    Triggers if the customer's percentage of available commits on all active commits of that credit type (currency or pricing unit) reaches or goes below a set threshold.

    To notify on a specific commit, set a custom field on the commit in Metronome and use advanced filters to evaluate only commits with that specific custom field value.

    #### Contract credit and commit balance

    **Alert Type:** `alerts.low_remaining_contract_credit_and_commit_balance_reached`

    Triggers when a customer's combined commit and credit balance reaches or drops below a set amount. If multiple commits and credits exist for a customer, Metronome sums up the remaining balances across all commits and credits to compare against the threshold.

    #### Seat balance

    **Alert Type:** `alerts.low_remaining_seat_balance_reached`

    Triggers when a customer's seat balance reaches or drops below a set amount. Metronome sums up the remaining balances for the specific seat across all commits and credits to compare against the threshold.

    Use the required `seat_filter` parameter to scope the notification to seat balances associated with seat-based subscriptions with a specific `seat_group_key`. Metronome will sum up the remaining balances for each seat across all commits and credits to compare against the threshold.

    Optionally, use the `seat_filter.seat_group_value` parameter to scope the notification to a specific seat.
  </Accordion>

  <Accordion title="Spend & Usage Notifications">
    #### Spend threshold

    **Alert Type:** `alerts.spend_threshold_reached`

    Triggers if the customer's usage-based spend prior to commit and credit drawdown for their current billing period reaches or goes beyond the set threshold. This notification evaluates against the sum of all usage-based charges for a particular customer, including usage drawdowns on credits and commits.

    Commit purchases are not factored into a customer's spend threshold notification. For example, if the threshold is set at \$10,000, \$7,000 in usage charges plus a \$3,000 commit purchase will not trigger the notification.

    Additionally, spend notifications are evaluated *only* against direct spend in a specific credit type. A spend notification threshold configured for a currency always evaluates to `ok` if you are using a custom pricing unit for a customer's line items. To avoid this, configure spend notification thresholds to use the same pricing unit as the line items on a customer's invoice.

    To notify on a specific contract type, set a custom field on the contract in Metronome and use advanced filters to evaluate only contracts with that specific custom field value.

    Optionally, use the `group_values` advanced filter parameter with this notification type to evaluate only usage associated with a specific group key:group value pair. You can also filter on `group_key` to evaluate usage across all group values for that key.

    #### Billable metric usage

    **Alert Type:** `alerts.usage_threshold_reached`

    Triggers if the customer's usage of a particular billable metric in their current billing period reaches or goes beyond your set threshold.

    The current billing period for a customer is calculated by taking the earliest start date and the latest end date across all active invoices.
  </Accordion>

  <Accordion title="Invoice Notifications">
    #### Invoice total

    **Alert Type:** `alerts.invoice_total_reached`

    Triggers if any of the customer's active invoices reaches or exceeds the configured threshold. This notification evaluates against the net invoice total after any credits, commits, or other adjustments have been applied. Each active invoice for the customer is evaluated separately. Additionally, only invoices in the specified currency are evaluated.

    To notify on a specific invoice type, use advanced filters to target the particular invoice type.
  </Accordion>
</AccordionGroup>

## Webhook payload examples

<CodeGroup>
  ```json low_remaining_credit_balance_reached theme={null}
  {  
    "id": "445b849e-1366-4580-a6cc-f488e27c059f",  
    "properties": {  
      "customer_id": "ac39ecc3-87ee-4d58-8ec0-24041464dddd",  
      "alert_id": "445b849e-1366-4580-a6cc-f488e27c059f",  
      "timestamp": "2024-10-07T15:08:44.865Z",  
      "threshold": 20000,  
      "alert_name": "Credit balance low",  
      "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",  
      "remaining_balance": 5000,  
      "triggered_by": "usage"  
    },  
    "type": "alerts.low_remaining_credit_balance_reached"  
  }
  ```

  ```json spend_threshold_reached theme={null}
  {  
    "id": "7f8a9b2c-3d4e-5f6g-7h8i-9j0k1l2m3n4o",  
    "properties": {  
      "customer_id": "b2c3d4e5-f6g7-h8i9-j0k1-l2m3n4o5p6q7",  
      "alert_id": "7f8a9b2c-3d4e-5f6g-7h8i-9j0k1l2m3n4o",  
      "timestamp": "2024-10-07T16:30:15.123Z",  
      "threshold": 10000,  
      "alert_name": "Spend threshold exceeded",  
      "current_spend": 12500,  
      "triggered_by": "usage"  
    },  
    "type": "alerts.spend_threshold_reached"  
  }
  ```

  ```json low_remaining_commit_balance_reached theme={null}
  {  
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",  
    "properties": {  
      "customer_id": "c3d4e5f6-g7h8-i9j0-k1l2-m3n4o5p6q7r8",  
      "alert_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",  
      "timestamp": "2024-10-07T14:45:30.456Z",  
      "threshold": 5000,  
      "alert_name": "Commit balance low",  
      "commit_id": "d4e5f6g7-h8i9-j0k1-l2m3-n4o5p6q7r8s9",  
      "remaining_balance": 1200,  
      "triggered_by": "usage"  
    },  
    "type": "alerts.low_remaining_commit_balance_reached"  
  }
  ```

  ```json usage_threshold_reached theme={null}
  {  
    "id": "e5f6g7h8-i9j0-k1l2-m3n4-o5p6q7r8s9t0",  
    "properties": {  
      "customer_id": "f6g7h8i9-j0k1-l2m3-n4o5-p6q7r8s9t0u1",  
      "alert_id": "e5f6g7h8-i9j0-k1l2-m3n4-o5p6q7r8s9t0",  
      "timestamp": "2024-10-07T17:15:45.789Z",  
      "threshold": 1000000,  
      "alert_name": "API calls threshold exceeded",  
      "billable_metric_id": "g7h8i9j0-k1l2-m3n4-o5p6-q7r8s9t0u1v2",  
      "current_usage": 1250000,  
      "triggered_by": "usage"  
    },  
    "type": "alerts.usage_threshold_reached"  
  }
  ```

  ```json invoice_total_reached theme={null}
  {  
    "id": "h8i9j0k1-l2m3-n4o5-p6q7-r8s9t0u1v2w3",  
    "properties": {  
      "customer_id": "i9j0k1l2-m3n4-o5p6-q7r8-s9t0u1v2w3x4",  
      "alert_id": "h8i9j0k1-l2m3-n4o5-p6q7-r8s9t0u1v2w3",  
      "timestamp": "2024-10-07T18:00:00.000Z",  
      "threshold": 50000,  
      "alert_name": "Invoice total exceeded",  
      "invoice_id": "j0k1l2m3-n4o5-p6q7-r8s9-t0u1v2w3x4y5",  
      "invoice_total": 55000,  
      "triggered_by": "invoice_generation"  
    },  
    "type": "alerts.invoice_total_reached"  
  }
  ```
</CodeGroup>

## Creating and managing threshold notifications

Threshold notifications can be created and managed through both the UI and the API. You can define what thresholds you care about and which customers to target.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/phb9Acjv7jlF___r/images/set-up-notification/threshold_create.png?fit=max&auto=format&n=phb9Acjv7jlF___r&q=85&s=4853446e2cd40b8c9f7bd488241e0d44" alt="Create threshold notification interface showing spend threshold configuration" width="2788" height="2188" data-path="images/set-up-notification/threshold_create.png" />
</Frame>

**In the UI**

1. Navigate to the **Notifications** tab
2. Click **Create Notification**
3. Choose any of the above threshold notification types
4. Configure threshold details and custom field level targeting where applicable
5. Determine whether you'd like the notification to evaluate customers that already meet the threshold or only trigger on customers that cross the threshold in the future
6. Select customers that notification should be applied to
7. Click **Save**
8. Metronome will begin evaluating the selected customers against the defined threshold and will trigger a notification to your configured webhooks when the customer crosses the threshold
9. Ensure your webhooks are set up to properly handle the payloads for these notifications

**Via API**

1. Call `POST /v1/alerts/create`
2. Pass in the alert type, name and threshold in the request body
3. Optionally pass in additional filters relevant to the alert type
4. A successful response will return a CustomerAlert object containing the notification configuration with its unique ID and current status

To get the real-time evaluation status for a specific threshold notification-customer pair, you can call the `POST /v1/customer-alerts/get` endpoint. This endpoint provides instant visibility into whether a customer has triggered a threshold condition, enabling you to monitor account health and take proactive action based on current state. This endpoint is useful for periodic checking of a customer's threshold notification status, but shouldn't be scraped. You should instead rely on the webhook notification to understand when customers are moved to `IN_ALARM`.

Threshold notifications can be archived in the UI or via API, removing them from active monitoring.

## Threshold notification evaluation triggers

To assess whether or not a threshold notification should be sent, Metronome routinely evaluates customers with associated notifications in real time as usage is sent to Metronome. If a customer's watched value—credit balance, spend, and so on—hits the threshold, a threshold notification is sent.

There are two possible triggers for an evaluation:

* Usage events are ingested
* Customer metadata changes (for example, a contract is assigned or a new ingest alias is assigned)

  Specifically, any CRUD (create, retrieve, update, and delete) action impacting notifications, customers, customer ingest aliases, contract, commitments, and credits are considered metadata changes and trigger a notification evaluation.

Threshold alerts have notifications sent within minutes of that condition being met.
