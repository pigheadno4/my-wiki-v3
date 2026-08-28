<!-- Source URL: https://docs.metronome.com/guides/customers-billing/set-up-notifications/create-and-manage-notifications.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage your customer lifecycle with Metronome notifications

Metronome lets you key into real-time customer activity and contract signals with a rich set of notifications that are sent to your configured webhooks. These notifications can help you:

* **Deliver timely in-product experiences** like onboarding messages, trial expiration reminders, or managing customer access after usage thresholds are reached
* **Power internal workflows** like notifying sales when a contract is expiring or a customer's commit is exhausted, putting them into overages
* **Remove customer friction** by notifying customers ahead of key events like a credit expiration or a contract renewal date

There are three different types of notifications you can receive from Metronome:

* **[Threshold notifications](/guides/customers-billing/set-up-notifications/threshold-notifications)** that fire when specific conditions are met, like spend exceeding a dollar amount or available credit amount dropping below a certain percentage
* **[System notifications](/guides/customers-billing/set-up-notifications/system-notifications)** that fire when an object is created or updated or at scheduled points in time, such as when a contract starts or ends
* **[Offset notifications](/guides/customers-billing/set-up-notifications/offset-notifications)** that fire at scheduled points in time as defined by a user set policy, such as 7 days before a commit expires or 3 days after a contract starts

## How notifications work

Metronome notifications are delivered as JSON formatted [webhook notifications](/guides/platform-configuration/setup-webhooks/) to an endpoint you configure. These notifications are sent asynchronously and are designed to power automated workflows, customer communication, and internal operations.

### Delivery mechanics

* **Webhook-based delivery**: All notification types are sent as HTTPS POST requests.
* **Standard format**: All payloads follow a consistent JSON schema and include contextual data like `customer_id`, `timestamp`, and relevant object fields.
* **Reliable retries**: If the endpoint is unavailable, Metronome will automatically retry delivery using exponential backoff with jitter. Retries continue for up to 48 hours (or until successful).
* **At least once delivery**: You may receive duplicate notifications; webhook endpoints should be idempotent.
* **Security**: Webhook payloads include a signature header so you can verify the origin

### Evaluation & scheduling

| **Notification** | **Timing**                                                                                                                                                                                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Threshold**    | *Emitted when new usage or data triggers a threshold condition.*<br />The threshold is evaluated at least once every three minutes. Notifications will fire within 5 minutes of the usage triggering the breach of the threshold being ingested.                                     |
| **System**       | *Emitted at the point in time the event happens*<br />Notifications are generated based on the configured timestamp of the object (e.g. contracts start) or action (e.g. contract edited) and are delivered in near real-time.                                                       |
| **Offset**       | *Emitted at the point in time of the defined policy for the event*<br />Notifications are generated based on the user-defined policy associated with a particular event (e.g. 3 days after commit segment starts or 4 days before contract ends) and are delivered in near real-time |

### Notification states

Notification types in Metronome fall into two behavioral models: **stateless** and **stateful**.

**System and Offset Notifications** are stateless; they trigger once at a scheduled moment like when a contract ends and they do not track ongoing conditions or transitions.

**Threshold Notifications** are stateful; they are continuously evaluated and move between two states: `OK` and `IN_ALARM`. For example, a commit balance notification may enter the `IN_ALARM` state when a customer's remaining balance drops below 10%, and return to `OK` once new prepaid credits are issued.

* The threshold notification states are defined as follows:
  * **EVALUATING:** The threshold has yet to be evaluated, typically due to a customer having just been created
  * **OK**: The condition has not been met
  * **IN\_ALARM**: The condition is actively met
* When a threshold notification returns to `OK` from `IN_ALARM`, an additional `*_resolved` notification may be sent (if enabled).

<Note>
  **DEFAULT STATE FOR THRESHOLD NOTIFICATIONS**

  The default state for threshold notifications depends on the presence of underlying data. For example, a customer with no active commits would be in an `OK` state for commit balance notifications until a commit is created and consumed.
</Note>

## Best practices

To get the most value from Metronome notifications, we recommend the following:

* **Use system notifications for time-based automation.** They offer precise control over the customer lifecycle, notifying you when events like contracts are created or commits have ended.
* **Leverage threshold notifications for continuous monitoring.** Set spend, usage, and credit thresholds to warn or remind customers before they reach a limit. Give customers the ability to enable their own notifications (for example, when their balance is low or when spend crosses a certain threshold) for budgeting purposes.
* **Use offset notifications for proactive workflows.** For example, fire a `credit.segment.ended` notification 7 days before credits expire to encourage further use.
* **Use custom fields to target key customer groups.** Create notifications for just your enterprise customers or those on a specific tier.
* **Make endpoints idempotent.** Webhooks are retried if delivery fails, so your systems should safely handle duplicates.
* **Log notification deliveries.** Keeping a delivery record helps with auditing and debugging downstream processes.

## Limits

Metronome sets different limit restriction behavior for the number of notifications that can be created based on the notification type.

### System and Offset Notifications

There are no restrictions on the number of active system and offset notifications that can be created.

### Threshold notifications

Threshold notifications do have different limit restrictions depending on if the notification affects a single customer or all active customers:

* The number of active threshold configurations that can apply to all customers is 300.
* The number of active threshold notifications that can apply to a single customer is 1200.

<Note>
  To request higher limits for your Metronome account, please contact us via the [Metronome support portal](https://support.metronome.com/).
</Note>

## Additional notes

* Metronome currently supports webhook delivery only and all notifications are sent to all webhooks you've configured.
* We are continuously expanding the types of system notifications and threshold notifications available, so you can cover more billing milestones and build even richer workflows over time.
