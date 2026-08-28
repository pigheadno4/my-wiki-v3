<!-- Source URL: https://docs.metronome.com/guides/platform-configuration/setup-webhooks.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Webhooks

Metronome provides programmatic notifications in the form of webhooks. If you configure a webhook URL, Metronome sends an HTTP POST request to that URL when certain events occur, such as a contract being created, a threshold being reached or an invoice being finalized. Your service can then react to that notification by updating customer state, sending an email, or notifying internal users to take some action.

## Webhook Types

Metronome sends these webhook types:

**Threshold Notifications**

**`alerts.<notification_type>`**

Threshold notifications monitor real-time metrics and trigger when defined thresholds are crossed. See our threshold notifications [documentation](/guides/customers-billing/set-up-notifications/threshold-notifications) for more on how to configure these types of notifications

Threshold notifications have this structure:

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

**System notifications for contract, credit and commit affiliated events**

**`contract.<notification_type>`**

**`commit.<notification_type>`**

**`credit.<notification_type>`**

System notifications monitor when events or actions occur based on the configured timestamp of an object (e.g contract start) or the time at which an action occurred (e.g. contract created). See our system notifications [documentation](/guides/customers-billing/set-up-notifications/system-notifications) for more on how to configure these types of notification

System notifications have this structure:

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

**Offset notifications for contract, credit and commit affiliated events**

Offset notifications allow you to schedule notifications to fire relative to a known date (e.g. a commit’s end date or a contract’s creation date). See our offset notifications [documentation](/guides/customers-billing/set-up-notifications/offset-notifications) for more on how to configure these types of notification

Offset notifications have this structure:

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
  "offset_duration": "-P3DT12H" // signed ISO-8601 duration
}
```

**Invoice finalized notifications**

**`invoice.finalized`**

Triggered whenever an invoice is finalized (happens after the grace period).

Invoice finalized notifications have this structure:

```json theme={null}
{
  "id": "fc00bd44-8d4b-4913-9b7c-fd1f8da61e62",
  "properties": {
    "invoice_id": "de99894e-f9ce-4b6c-92b0-f4ec0d09b6f1",
    "customer_id": "3c9e87ba-0e49-44a3-9aa9-6917f8da3491",
    "invoice_finalized_date": "2024-02-20T15:50:07.457Z"
  },
  "type": "invoice.finalized"
}
```

<Note>
  **NOTIFICATION CONFIGURATION**

  Contact us via the [Metronome support portal](https://support.metronome.com/) to set up `invoice.finalized` notifications.
</Note>

**Billing provider error notifications (Stripe)**

**`invoice.billing_provider_error`**

Billing provider error webhooks only apply to Stripe and are triggered any time there is an error in sending an invoice to Stripe (for example, the customer does not exist within Stripe or the customer does not have a valid payment method). No additional configuration is needed for this webhook; notifications are automatically sent when a webhook destination is set up and the Stripe integration is enabled on the account. Note that no Metronome webhook is triggered for errors residing entirely within Stripe (such as payment failures).

Billing provider error notifications have this structure:

```json theme={null}
{
  "id": "c941cccc-a890-45e4-96de-3fdb8a6809f3",
  "properties": {
    "invoice_id": "9927e175-c1d3-4f94-875b-8906bc773a95",
    "customer_id": "83518c41-76ff-4ac4-85d4-bd7010112bd3",
    "billing_provider": "STRIPE",
    "billing_provider_error": "No such customer: 'cus_PQzIVPOCGb4otV'"
  },
  "type": "invoice.billing_provider_error"
}
```

**Integration Issues**

**`integration.issue`**

Integration issue webhooks are triggered when there is an error with the client's third party integration (for example, invalid credentials, misconfigured connections, or API errors). No additional configuration is needed; notifications are automatically sent when a webhook destination is set up and the integration is enabled.

Integration issue notifications have this structure:

```json theme={null}
{
  "id": "c941cccc-a890-45e4-96de-3fdb8a6809f3",
  "type": "integration.issue",
  "properties": {
    "integration": "NETSUITE",
    "error": "Authentication failed: Invalid client credentials",
    "error_code": "INVALID_CREDENTIALS",
    "timestamp": "2025-10-03T12:34:56.789Z"
  }
}
```

**AWS marketplace notifications**

**`marketplaces.aws_metering_disabled`**

Triggered when an AWS marketplace customer is disabled

AWS marketplaces metering notifications have this structure:

```json theme={null}
{
  "id": "daf54f25-12f4-4b2a-8462-ebfff4b622b7",
  "properties": {
    "customer_id": "4ffe51f1-3702-490c-816e-35fad3e271de",
    "aws_customer_id": "SJyeYLq7123",
    "aws_product_code": "6m81ochldaiejgnw0b8391bfn"
  },
  "type": "marketplaces.aws_metering_disabled"
}
```

**Azure marketplace notifications**

**`marketplaces.azure_metering_disabled`**

Triggered when an Azure marketplace customer is disabled

Azure marketplaces metering notifications have this structure:

```json theme={null}
{
  "id": "c9afa306-4449-45f3-9bce-68e4927a1f0b",
  "properties": {
    "customer_id": "1eea08e0-2fe0-45ad-96e2-3c1dbc2ce3a8",
    "subscription_id": "f6ccac8e-9918-4c8f-9597-8a210a84c31c"
  },
  "type": "marketplaces.azure_metering_disabled"
}
```

**GCP marketplace notifications**

**`marketplaces.gcp_metering_disabled`**

Triggered when a GCP marketplace customer is disabled

GCP marketplaces metering notifications have this structure:

```json theme={null}
{
  "id": "c9afa306-4449-45f3-9bce-68e4927a1f0b",
  "properties": {
    "customer_id": "1eea08e0-2fe0-45ad-96e2-3c1dbc2ce3a8",
    "gcp_usage_reporting_id": "project_number:012345678912",
    "gcp_entitlement_id": "f6ccac8e-9918-4c8f-9597-8a210a84c31c",
    "gcp_service_name": "your-listing.endpoints.provider.cloud.goog"
  },
  "type": "marketplaces.gcp_metering_disabled"
}
```

### Payment gating notifications

Payment gating notifications are tied to specific workflows in Metronome that gate access to some product (e.g. commit balance) based on successful payment collection.

**Payment threshold reached**

This webhook is fired when a payment gating action is triggered, such as when a customer hits their `threshold_amount` for Threshold Billing.

**Payment gate status**

After a payment is attempted for a payment gate workflow, this webhook returns the status. It includes relevant metadata from the gateway, such as error codes, if applicable.

**Payment gate action required**

This webhook is fired if an additional action is required to complete payment. It includes relevant metadata to identify the associated payment in the gateway, if applicable.

**External workflow initiated**
If processing payment via an external gateway outside of a native Metronome integration, this webhook will provide you the information to process that transaction. The `workflow_id` provided is used to release or cancel the balance, pending payment outcome.

Payment gating notifications have this structure:

<AccordionGroup>
  <Accordion title="Payment gate status">
    ```json theme={null}
    {  
      "id": "d304936c-a287-492c-b546-ac79dc673191",  
      "properties": {  
        "workflow_type": "manual_commit",     
        "customer_id": "6352d562-213f-4a6e-819f-58fdabc3f2b9",  
        "contract_id": "bbf87cf7-beaa-4d96-aea4-2cd87009dcb6",  
        "invoice_id": "6644b5ec-394a-4d07-a037-e2827a0af4be",  
        "payment_status": "failed",  
        "timestamp": "2025-01-01T00:00:00Z",  
        "error_message": "Your card has insufficient funds.",  
        "billing_provider": {  
            "type": "stripe",  
            "stripe": {  
                "payment_intent_id": "pi_3RP3ioIkTQSg6Mm31jR006rF",  
                "error": {  
                    "type": "card_error",  
                    "code": "card_declined",  
                    "decline_code": "insufficient_funds",  
                    "message": "Your card has insufficient funds."  
                },  
            },  
        },  
      },  
      "type": "payment_gate.payment_status"  
    }  
    ```
  </Accordion>

  <Accordion title="Payment gate action required">
    ```json theme={null}
    {  
      "id": "417fcaa4-f3cf-434e-ab20-f70204cfd5ef",  
      "properties": {  
        "workflow_type": "spend",     
        "customer_id": "d290dec8-4ebb-4e73-89ef-45ed3443ca67",  
        "contract_id": "80b07d70-c84e-4ff0-b42c-875defff0931",  
        "invoice_id": "dd864572-9787-573f-9c74-e5159b4ea97c",  
        "error_message": "three_d_secure_redirect",  
        "billing_provider": {  
            "type": "stripe",  
            "stripe": {  
                "payment_intent_id": "pi_3ROpJCIkTQSg6Mm31fNUnPKx",  
            },  
        },  
      },  
      "type": "payment_gate.payment_pending_action_required"  
    }  
    ```
  </Accordion>

  <Accordion title="Threshold reached">
    ```json theme={null}
    {  
      "id": "417fcaa4-f3cf-434e-ab20-f70204cfd5ef",  
      "properties": {  
        "workflow_type": "spend",     
        "customer_id": "d290dec8-4ebb-4e73-89ef-45ed3443ca67",  
        "contract_id": "80b07d70-c84e-4ff0-b42c-875defff0931",  
        "timestamp": "2025-01-01T00:00:00.000Z",  
      },  
      "type": "payment_gate.threshold_reached"  
    }  
    ```
  </Accordion>

  <Accordion title="External workflow initiated">
    ```json theme={null}
    {  
      "id": "417fcaa4-f3cf-434e-ab20-f70204cfd5ef",  
      "properties": {  
        "workflow_type": "spend",     
        "customer_id": "d290dec8-4ebb-4e73-89ef-45ed3443ca67",  
        "contract_id": "80b07d70-c84e-4ff0-b42c-875defff0931",  
        "workflow_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",  
        "invoice_id": "6a37bb88-8538-48c5-b37b-a41c836328bd",  
        "invoice_total": 1500,  
        "invoice_currency": "USD",  
      },  
      "type": "payment_gate.external_initiate"  
    }  
    ```
  </Accordion>
</AccordionGroup>

## Webhook IP Addresses

Webhook notifications may come from the following IP addresses. This list may change, but if it does we'll give at least 30 days notice.

```
52.39.198.29
44.241.254.184
52.42.224.184
52.89.217.131
44.231.139.128
54.245.125.92
3.134.178.31
3.12.62.53
3.140.90.67
3.142.231.113
3.131.206.70
3.132.225.181
```

## Handle Webhook Notifications

To receive Metronome webhooks, you need a webhook handler listening at a publicly accessible HTTPS URL that performs the below tasks.

### Acknowledge the Notification

Upon receiving a notification, your endpoint must return a successful status code, such as `200 OK`. If Metronome receives a status code >`299`, notification retries are attempted until a successful status code is returned.

If your webhook endpoint does not properly acknowledge the notification, Metronome continuously retries it with exponential backoff until it hits a 15-minute retry cadence. Once the retry process hits 15 minutes, Metronome repeats the notification until it is either accepted or two days have passed since the initial notification attempt (\~200 retries).

It is recommended that you process webhooks asynchronously: store the webhook payload in a queue, return a `200` response code, and only then validate or process the payload. Removing webhook processing from the receiving path reduces the likelihood of your systems getting blocked.

### Prepare for Duplicate Notifications

Under normal circumstances, Metronome sends each notification exactly once. However, there are a few situations that could cause you to receive the same notification multiple times:

* **Retries** — As mentioned above, if Metronome receives an error when attempting to deliver the notification to your webhook handler, we retry the notification. Depending on the nature of the error, it's possible that your endpoint receives a notification without acknowledging it, in which case your endpoint receives the same notification again.
* **Multiple webhook URLs** — If you configure Metronome to notify multiple webhook URLs, or even the same URL multiple times, notifications are sent multiple times. If you want to ensure duplicate notifications are ignored, you can use the notification's `id` field to deduplicate.

### Verify Notifications

Because your webhook endpoint is a public URL, anyone could send a request to it. Before you take actions based on the notification, you should verify the information it contains. You can do this in two ways: by fetching data from the Metronome API yourself or by verifying the webhook request's signature.

<Info>
  **INFO**

  Metronome may make introduce backward-compatible changes to existing webhook shapes without notice, such as adding a new webhook field. Metronome recommends that you validate only fields that are expected to be present according to the documentation at time of integration.
</Info>

#### Call the Metronome API

Webhook notifications contain only minimal information about the event that occurred. This means it's often useful to call the appropriate Metronome API endpoint to get the full details. For example, if you receive a webhook notification informing you that an invoice has been finalized, you can call the `/customers/{customer_id}/invoices/{invoice_id}` endpoint to fetch the details of the invoice mentioned in the notification. In this way, the notification serves as a hint that something has changed, but your code relies only on data obtained directly from the Metronome API.

#### Verify Signatures

If the above strategy doesn't work for your use case, Metronome also provides a method to verify the authenticity of notifications as you receive them by using the `Metronome-Webhook-Signature` HTTP header. The value of this header is a cryptographic signature of the HTTP request, using a secret key set up when you configure your webhook.

<Tip>
  **Secret keys are unique per webhook**

  If you have multiple webhooks configured on your Metronome account, each webhook has its own secret key.
</Tip>

To validate the signature, first concatenate the value of the request's `X-Metronome-Date` header and the exact bytes of the request body, separated by a newline character (`\n`). Then compute the HMAC-SHA256 of the resulting string, keyed by the webhook's secret key. Finally, compare the hexadecimal representation of the HMAC you computed with the one found in the `Metronome-Webhook-Signature` header. If they don't match, the webhook notification did not come from Metronome.

```
HMAC_SHA256(secret_key, X_METRONOME_DATE_HEADER + "\n" + BODY)
```

<Tip>
  **Use `X-Metronome-Date` instead of `Date`**

  Metronome sends both an `X-Metronome-Date` header and a standard `Date` header with the same value. Prefer `X-Metronome-Date` for signature verification: it's preserved end-to-end and isn't rewritten by intermediaries (load balancers, proxies, or frameworks) that may overwrite the standard `Date` header, which would otherwise cause signature verification to fail. The `Date` header is still supported for backward compatibility, but isn't recommended.
</Tip>

The `X-Metronome-Date` header is included to aid in deduplication. You should ignore webhook requests that are older than five minutes, which means your webhook handler only needs to store recent notification IDs to prevent duplicates.

<Warning>
  **THE BODY MUST BE TREATED AS BYTES**

  When computing the signature, Metronome uses the exact bytes sent in the request body. Be careful to do the same in your code. If you try to use the parsed JSON body for verification purposes, you'll likely fail signature verification because serializing the data again is not guaranteed to produce the same JSON.
</Warning>

The following code example shows how to perform signature validation:

<CodeGroup>
  ```bash bash theme={null}
  echo -n "$X_METRONOME_DATE_HEADER\n$BODY" | openssl dgst -sha256 -hmac $KEY
  ```

  ```javascript JavaScript theme={null}
  crypto
    .createHmac("sha256", KEY)
    .update(`${headers["X-Metronome-Date"]}\n${body}`)
    .digest("hex");
  ```

  ```go Go theme={null}
  func isSignatureValid(r *http.Request, body []byte, webhookSecret string) bool {
  	signatureHeader := r.Header.Get("Metronome-Webhook-Signature")
  	date := r.Header.Get("X-Metronome-Date")

  	buff := bytes.NewBufferString(date)
  	buff.WriteByte('\n')
  	buff.Write(body)

  	mac := hmac.New(sha256.New, []byte(webhookSecret))

  	mac.Write(buff.Bytes())
  	expectedMac := hex.EncodeToString(mac.Sum(nil))

  	if !hmac.Equal([]byte(expectedMac), []byte(signatureHeader)) {
  		return false
  	}
  	return true
  }
  ```
</CodeGroup>

To test this, consider the following example webhook notification. The secret key for verification is `correct-horse-battery-staple`:

```http theme={null}
POST /webhook HTTP/1.1
Host: example.com
User-Agent: Metronome
Content-Type: application/json
Date: Mon, 02 Jan 2006 22:04:05 GMT
X-Metronome-Date: Mon, 02 Jan 2006 22:04:05 GMT
Metronome-Webhook-Signature: b82652fa2246cf1d8a27e591f155c865f68b46c19b9213fd9c052f2419b4742b

{
  "id": "b2c9e307-624e-4e7d-a5a4-1b74107d78c4",
  "type": "widget_created",
  "properties": {
    "customer_id": "5f794d50-085a-4db6-8d15-286e518b7225",
    "widget_id": "0891458d-b6f0-4fdd-a41e-380aae1a1e38"
  }
}
```

## Send Webhooks to Slack

If you want to receive Metronome notifications in Slack without building a custom webhook handler, you can configure Metronome to send notifications directly to a Slack channel. From there, you can triage and act on them. To send Metronome webhooks to Slack:

To send Metronome webhooks to Slack:

1. [Create an incoming webhook in Slack](https://api.slack.com/messaging/webhooks) and copy the generated webhook URL. It'll look something like: `https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX`
2. Create a webhook destination in Metronome for your Slack channel. In the Metronome app, go to **Developer** > **Notifications** > **Webhooks** > **Add** and paste your Slack webhook URL.
3. Set up a test notification to verify the integration. In the Metronome app, go to **Developer** > **Notifications** > **Create Notification** and create a notification like **Low credit balance reached**.
4. Verify the integration by testing the webhook connection. Trigger your test notification and check your Slack channel for a message from Metronome.

When properly configured, you'll receive Slack messages that look like this:

```json theme={null}
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
