<!-- Source URL: https://docs.metronome.com/guides/customers-billing/set-up-notifications/offset-notifications.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Offset notifications

Offset notifications allow you to schedule notifications to fire relative to a known date (e.g. a commit's end date or a contract's creation date). They're best for designing proactive, customer-centric experiences. For example, sending a "trial credits expiring soon" email to customers 7 days before their expiration date to encourage further adoption and usage. Offset amounts can be configured in hours, days, weeks, months, and years.

## Offset notification types and payloads

<Note>
  **PAYLOAD SCHEMA DIFFERENCES**

  The payloads schema for offset notifications differ slightly from the payload schema for threshold notifications. Specifically, the payload for offset notifications do not include a `properties` field. Ensure your webhooks are properly configured to handle both notification types.
</Note>

Offset notifications can be configured around any of the system notification types above. A sample payload for offset notifications is below:

```json theme={null}
{
  "id": "c9656215-3e96-59f4-7284-0021bdfd4c9a",
  "type": "contract.start",
  "timestamp": "2025-07-02T00:00:00Z",
  "environment_type": "PRODUCTION",
  "contract_id": "1bd74703-0854-4730-9549-893585c519e8",
  "contract_custom_fields": {
    "ContractType": "PayGo"
  },
  "customer_id": "eadab230-ef95-4c3c-d696-4391c205c982",
  "customer_custom_fields": {
    "CustomerType": "Tier2"
  },
  "offset_id": "8ed3d961-7b61-4c0a-8f2b-e546f45c33d6",
  "offset_duration": "-P3DT12H"
}
```

The timestamp included in the offset payload is the time associated with the source event itself, not the offset. For example, for an offset configured to fire 3 days after the contract started, the timestamp will be the contract start time itself, *not* contract start time + 3 days.

## Enabling and managing offset notifications

Offset notifications can be enabled and managed through both the UI and the API.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/phb9Acjv7jlF___r/images/set-up-notification/offset_create.png?fit=max&auto=format&n=phb9Acjv7jlF___r&q=85&s=d7f226206d47cd73ee32a20cea1de3a0" alt="Create offset notification interface showing contract end notification configuration" width="2780" height="2182" data-path="images/set-up-notification/offset_create.png" />
</Frame>

**In the UI**

1. Navigate to the **Notifications** tab
2. Click **Create Notification**
3. Choose any of the above system notification types
4. Configure offset details (e.g. 3 days after contract starts, 60 days before commit segment ends)
5. Click **Save**
6. You will begin receiving notifications about this offset event for all customers to all configured webhooks
7. Ensure your webhooks are set up to properly handle the payloads for these notifications.

**Via API**

1. Call `POST /v2/notifications/create`
2. Pass in the name of the offset and the offset policy, including type of system event you'd like to create an offset and the associated offset amount in ISO-8601 format
3. A successful response will return details about the created offset including the notification configuration with its unique ID

## Offset behavior by scenario

When you enable an offset notification, Metronome starts generating events from that point forward. It does not go back and create events for past data. See the table below for examples of scenarios under which offset notifications will or will not fire.

| **Scenario**                                                                             | **Will the notification fire?**                 | **Example**                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Offset time for an existing entity is already in the past at the time of offset creation | No                                              | A `credit.end - 3d` offset is configured on May 20, but an existing credit ends May 22. The offset fire time (May 19) has already passed, so nothing is sent.                                          |
| Entity is created but offset fire time is already in the past                            | No                                              | A credit is created on May 15 with an end date of May 30. A matching offset (`-30d`) was defined earlier. Since May 1 has already passed, no notification is sent.                                     |
| Entity is edited and new offset fire time is in the past                                 | No                                              | A commit originally ended on May 25 with an offset for `-5d` which fired on May 20. On May 22, the end date is edited to May 23. The offset fire time (May 18) has already passed, so nothing is sent. |
| Offset is archived before fire time                                                      | No                                              | A `contract.end - 1d` offset is scheduled to fire on June 4. The offset config is archived on June 2. The notification does not fire.                                                                  |
| Entity is created after offset config is defined                                         | Yes, if offset fire time is still in the future | A `commit.end - 7d` offset is configured. On May 10, a new commit is created with an end date of May 20. A notification will fire on May 13.                                                           |

## Additional caveats

There are a few additional caveats for specific offset types:

* Offset notifications cannot be configured to fire *before* `.create`, `.edit` and `.archive` events
* If you've configured an offset notification to fire before `commit.segment.start`, there is an edge case to be aware of when using this offset type alongside Metronome's recurring commits feature.
  * For recurring commits, Metronome only generates subsequent child commits at most one future billing period ahead. This means if you have an offset configured to fire before a commit segment starts and that offset duration is *longer than one billing period*, the notification will not fire at its scheduled time. Instead it will fire at the time the next child commit is created. For example, you've set up a monthly recurring commit and configured an offset notification to fire 90 days before a commit segment starts, the offset for that recurring commit will not fire 90 days before the future child commit segment starts because the child commit does not exist yet. Instead, it will fire \~30 days before the future child commit segment starts at the time the next child commit is created as that is when the next billing period becomes available.
