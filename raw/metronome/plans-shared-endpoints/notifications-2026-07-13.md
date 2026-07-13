<!-- Source URL: https://docs.metronome.com/plans-shared-endpoints/notifications.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Notifications

Metronome supports a shared set of Alert endpoints that allow you to create, retrieve, and manage alert configurations related to both **Plans** and **Contracts**.

While these endpoints are shared between Plans and Contracts, note that some input and response parameters differ slightly depending on the entity you are targeting.

## Available Endpoints

| Endpoint                 | Description                                                    |
| ------------------------ | -------------------------------------------------------------- |
| `/alerts/create`         | Creates a new alert configuration for a plan or contract.      |
| `/customer-alerts/get`   | Retrieves a specific alert configuration for a given customer. |
| `/customer-alerts/list`  | Lists all active alerts for a customer.                        |
| `/customer-alerts/reset` | Resets an alert, clearing its triggered state.                 |
| `/alerts/archive`        | Archives an alert configuration so it no longer triggers.      |

## Supported Alert Types

When using these endpoints, the `alert_type` field determines what condition triggers the alert.

The supported values for `alert_type` when using plans include:

* `low_credit_balance_reached`
* `low_remaining_days_in_plan_reached`
* `low_remaining_credit_percentage_reached`
* `usage_threshold_reached`

Check out the Contracts version of the documentation [here →](/api-reference/alerts/create-a-threshold-notification)
