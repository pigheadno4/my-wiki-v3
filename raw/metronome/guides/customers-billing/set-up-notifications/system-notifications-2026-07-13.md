<!-- Source URL: https://docs.metronome.com/guides/customers-billing/set-up-notifications/system-notifications.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# System notifications

System notifications monitor when events or actions occur based on the configured timestamp of an object (e.g contract start) or the time at which an action occurred (e.g. contract created). They're best for time-based automation workflows around a customer's key lifecycle events.

## System notification types

<Note>
  **PAYLOAD SCHEMA DIFFERENCES**

  The payload schema for system notifications differ slightly from the payload schema for threshold notifications. Specifically, the payload for system notifications do not include a `properties` field. Ensure your webhooks are properly configured to handle both notification types.
</Note>

| **Type**        | **Name**               | **Details**                                                                                                                                                             |
| --------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Contract        | `contract.create`      | Triggers when a new contract is created                                                                                                                                 |
| Contract        | `contract.start`       | Triggers when a contract is started                                                                                                                                     |
| Contract        | `contract.edit`        | Triggers when a contract is edited                                                                                                                                      |
| Contract        | `contract.end`         | Triggers when a contract ends                                                                                                                                           |
| Contract        | `contract.archive`     | Triggers when a contract is archived                                                                                                                                    |
| Commit & Credit | `commit.create`        | Triggers when a new commit is created                                                                                                                                   |
| Commit & Credit | `commit.edit`          | Triggers when a commit is edited                                                                                                                                        |
| Commit & Credit | `commit.archive`       | Triggers when a commit is archived                                                                                                                                      |
| Commit & Credit | `commit.segment.start` | Triggers when a commit segment starts<br /><br />The segment number that triggered the notification and the total number of commit segments can be found in the payload |
| Commit & Credit | `commit.segment.end`   | Triggers when a commit segment ends<br /><br />The segment number that triggered the notification and the total number of commit segments can be found in the payload   |
| Commit & Credit | `credit.create`        | Triggers when a new credit is created                                                                                                                                   |
| Commit & Credit | `credit.edit`          | Triggers when a credit is edited                                                                                                                                        |
| Commit & Credit | `credit.archive`       | Triggers when a credit is archived                                                                                                                                      |
| Commit & Credit | `credit.segment.start` | Triggers when a credit segment starts<br /><br />The segment number that triggered the notification and the total number of credit segments can be found in the payload |
| Commit & Credit | `credit.segment.end`   | Triggers when a credit segment ends<br /><br />The segment number that triggered the notification and the total number of credit segments can be found in the payload   |

## Webhook payload examples

<CodeGroup>
  ```json contract.create theme={null}
  {
    "id": "fca7b4ef-6187-51d5-a9d9-b57f40117728",
    "type": "contract.create",
    "timestamp": "2025-09-12T20:20:04Z",
    "environment_type": "PRODUCTION",
    "contract_id": "33d206f6-7455-49f6-857d-2172c37db68d",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "customer_id": "1ed86915-97f1-4d92-8fa6-763c0235093a",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```

  ```json contract.start theme={null}
  {
    "id": "4dcef5c4-ed3b-5d0e-baa4-beec74544158",
    "type": "contract.start",
    "timestamp": "2025-08-07T00:00:00Z",
    "environment_type": "PRODUCTION",
    "contract_id": "33d206f6-7455-49f6-857d-2172c37db68d",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "customer_id": "1ed86915-97f1-4d92-8fa6-763c0235093a",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```

  ```json contract.edit theme={null}
  {
    "id": "ba0d43a2-9426-5219-9191-becdfb43e102",
    "type": "contract.edit",
    "timestamp": "2025-09-15T17:27:41Z",
    "environment_type": "PRODUCTION",
    "contract_id": "3b1cf6f5-e4ea-449f-acc3-afceffaddea7",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "customer_id": "541be796-88fa-4081-8f8f-7ac230c43b2c",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```

  ```json contract.end theme={null}
  {
    "id": "ba0d43a2-9426-5219-9191-becdfb43e102",
    "type": "contract.end",
    "timestamp": "2025-09-15T17:27:41Z",
    "environment_type": "PRODUCTION",
    "contract_id": "3b1cf6f5-e4ea-449f-acc3-afceffaddea7",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "customer_id": "541be796-88fa-4081-8f8f-7ac230c43b2c",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```

  ```json contract.archive theme={null}
  {
    "id": "ba0d43a2-9426-5219-9191-becdfb43e102",
    "type": "contract.archive",
    "timestamp": "2025-09-15T17:27:41Z",
    "environment_type": "PRODUCTION",
    "contract_id": "3b1cf6f5-e4ea-449f-acc3-afceffaddea7",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "customer_id": "541be796-88fa-4081-8f8f-7ac230c43b2c",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```

  ```json commit.create theme={null}
  {
    "id": "23bbd69c-28bb-5f04-b609-ea716b0f00b4",
    "type": "commit.create",
    "timestamp": "2025-08-07T00:00:00Z",
    "environment_type": "PRODUCTION",
    "commit_id": "529a023b-3d3c-52b1-b6d5-4d3dd06c6cb0",
    "commit_custom_fields": {
      "tier_key": "f_minor"
    },
    "contract_id": "33d206f6-7455-49f6-857d-2172c37db68d",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "parent_recurring_commit_id": "0719c77c-e3e1-4d1d-bb59-6cee63773f24",
    "customer_id": "1dd86915-97f1-4d92-8fa6-763c0235093a",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```

  ```json commit.edit theme={null}
  {
    "id": "33bbd69c-28bb-5f04-b609-ea716b0f00b4",
    "type": "commit.edit",
    "timestamp": "2025-08-07T00:00:00Z",
    "environment_type": "PRODUCTION",
    "commit_id": "529a023b-3d3c-52b1-b6d5-4d3dd06c6cb0",
    "commit_custom_fields": {
      "tier_key": "f_minor"
    },
    "contract_id": "33d206f6-7455-49f6-857d-2172c37db68d",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "parent_recurring_commit_id": "0719c77c-e3e1-4d1d-bb59-6cee63773f24",
    "customer_id": "1dd86915-97f1-4d92-8fa6-763c0235093a",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```

  ```json commit.archive theme={null}
  {
    "id": "43bbd69c-28bb-5f04-b609-ea716b0f00b4",
    "type": "commit.archive",
    "timestamp": "2025-08-07T00:00:00Z",
    "environment_type": "PRODUCTION",
    "commit_id": "529a023b-3d3c-52b1-b6d5-4d3dd06c6cb0",
    "commit_custom_fields": {
      "tier_key": "f_minor"
    },
    "contract_id": "33d206f6-7455-49f6-857d-2172c37db68d",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "parent_recurring_commit_id": "0719c77c-e3e1-4d1d-bb59-6cee63773f24",
    "customer_id": "1dd86915-97f1-4d92-8fa6-763c0235093a",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```

  ```json commit.segment.start theme={null}
  {
    "id": "92adc38c-671c-59dd-8f2e-39fc7482a4df",
    "type": "commit.segment.start",
    "timestamp": "2025-08-07T00:00:00Z",
    "environment_type": "PRODUCTION",
    "commit_id": "529a023b-3d3c-52b1-b6d5-4d3dd06c6cb0",
    "commit_custom_fields": {
      "tier_key": "f_minor"
    },
    "contract_id": "33d206f6-7455-49f6-857d-2172c37db68d",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "parent_recurring_commit_id": "0718c77c-e3e1-4d1d-bb59-6cee63773f24",
    "segment_index": 0,
    "segment_count": 1,
    "segment_id": "dea59112-dadb-52c4-8789-304e2cddff92",
    "customer_id": "1ed86915-97f1-4d92-8fa6-763c0235093a",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```

  ```json commit.segment.end theme={null}
  {
    "id": "a2adc38c-671c-59dd-8f2e-39fc7482a4df",
    "type": "commit.segment.end",
    "timestamp": "2025-08-07T00:00:00Z",
    "environment_type": "PRODUCTION",
    "commit_id": "529a023b-3d3c-52b1-b6d5-4d3dd06c6cb0",
    "commit_custom_fields": {
      "tier_key": "f_minor"
    },
    "contract_id": "33d206f6-7455-49f6-857d-2172c37db68d",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "parent_recurring_commit_id": "0718c77c-e3e1-4d1d-bb59-6cee63773f24",
    "segment_index": 0,
    "segment_count": 1,
    "segment_id": "dea59112-dadb-52c4-8789-304e2cddff92",
    "customer_id": "1ed86915-97f1-4d92-8fa6-763c0235093a",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```

  ```json credit.create theme={null}
  {
    "id": "23bbd69c-28bb-5f04-b609-ea716b0f00b4",
    "type": "credit.create",
    "timestamp": "2025-08-07T00:00:00Z",
    "environment_type": "PRODUCTION",
    "credit_id": "529a023b-3d3c-52b1-b6d5-4d3dd06c6cb0",
    "credit_custom_fields": {
      "tier_key": "f_minor"
    },
    "contract_id": "33d206f6-7455-49f6-857d-2172c37db68d",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "parent_recurring_credit_id": "0719c77c-e3e1-4d1d-bb59-6cee63773f24",
    "customer_id": "1dd86915-97f1-4d92-8fa6-763c0235093a",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```

  ```json credit.edit theme={null}
  {
    "id": "33bbd69c-28bb-5f04-b609-ea716b0f00b4",
    "type": "credit.edit",
    "timestamp": "2025-08-07T00:00:00Z",
    "environment_type": "PRODUCTION",
    "credit_id": "529a023b-3d3c-52b1-b6d5-4d3dd06c6cb0",
    "credit_custom_fields": {
      "tier_key": "f_minor"
    },
    "contract_id": "33d206f6-7455-49f6-857d-2172c37db68d",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "parent_recurring_credit_id": "0719c77c-e3e1-4d1d-bb59-6cee63773f24",
    "customer_id": "1dd86915-97f1-4d92-8fa6-763c0235093a",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```

  ```json credit.archive theme={null}
  {
    "id": "43bbd69c-28bb-5f04-b609-ea716b0f00b4",
    "type": "credit.archive",
    "timestamp": "2025-08-07T00:00:00Z",
    "environment_type": "PRODUCTION",
    "credit_id": "529a023b-3d3c-52b1-b6d5-4d3dd06c6cb0",
    "credit_custom_fields": {
      "tier_key": "f_minor"
    },
    "contract_id": "33d206f6-7455-49f6-857d-2172c37db68d",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "parent_recurring_credit_id": "0719c77c-e3e1-4d1d-bb59-6cee63773f24",
    "customer_id": "1dd86915-97f1-4d92-8fa6-763c0235093a",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```

  ```json credit.segment.start theme={null}
  {
    "id": "92adc38c-671c-59dd-8f2e-39fc7482a4df",
    "type": "credit.segment.start",
    "timestamp": "2025-08-07T00:00:00Z",
    "environment_type": "PRODUCTION",
    "credit_id": "529a023b-3d3c-52b1-b6d5-4d3dd06c6cb0",
    "credit_custom_fields": {
      "tier_key": "f_minor"
    },
    "contract_id": "33d206f6-7455-49f6-857d-2172c37db68d",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "parent_recurring_credit_id": "0718c77c-e3e1-4d1d-bb59-6cee63773f24",
    "segment_index": 0,
    "segment_count": 1,
    "segment_id": "dea59112-dadb-52c4-8789-304e2cddff92",
    "customer_id": "1ed86915-97f1-4d92-8fa6-763c0235093a",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```

  ```json credit.segment.end theme={null}
  {
    "id": "a2adc38c-671c-59dd-8f2e-39fc7482a4df",
    "type": "credit.segment.end",
    "timestamp": "2025-08-07T00:00:00Z",
    "environment_type": "PRODUCTION",
    "credit_id": "529a023b-3d3c-52b1-b6d5-4d3dd06c6cb0",
    "credit_custom_fields": {
      "tier_key": "f_minor"
    },
    "contract_id": "33d206f6-7455-49f6-857d-2172c37db68d",
    "contract_custom_fields": {
      "org_key": "g_major"
    },
    "parent_recurring_credit_id": "0718c77c-e3e1-4d1d-bb59-6cee63773f24",
    "segment_index": 0,
    "segment_count": 1,
    "segment_id": "dea59112-dadb-52c4-8789-304e2cddff92",
    "customer_id": "1ed86915-97f1-4d92-8fa6-763c0235093a",
    "customer_custom_fields": {
      "bill_customer_id": "0cu21JDIRIUDQKDS6wmx"
    }
  }
  ```
</CodeGroup>

## Enabling and managing system notifications

System notifications can be enabled and managed through both the UI and the API.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/phb9Acjv7jlF___r/images/set-up-notification/notiifcations_list.png?fit=max&auto=format&n=phb9Acjv7jlF___r&q=85&s=a933a4ab80194beeacde9697912cfd03" alt="Notifications list interface showing various notification types and their status" width="2160" height="1694" data-path="images/set-up-notification/notiifcations_list.png" />
</Frame>

**In the UI**

1. Navigate to the **Notifications** tab
2. Find the system notification that you'd like to enable. All available system notifications will appear in the notifications list view and be disabled by default for any account
3. Click on the notification
4. Click the toggle next to **Status** to enable
5. Confirm action to enable
6. You will begin receiving notifications about this system event for all customers to all configured webhooks
7. Ensure your webhooks are set up to properly handle the payloads for these notifications

**Via API**

1. Call `POST /v2/notifications/edit`
2. Pass in the policy of the system notification you'd like to enable (e.g. `contract.create`) and `is_enabled` set to true
3. A successful response will return a 200 response code

<Note>
  **HISTORICAL DATA LIMITATION**

  When you enable a system notification, Metronome starts generating events from that point forward. It does not go back and create events for past data. Additionally, the policy for system notifications cannot be edited.
</Note>
