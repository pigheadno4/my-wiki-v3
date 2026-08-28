<!-- Source URL: https://docs.metronome.com/guides/customers-billing/set-up-notifications/create-alert-specifiers.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create alert specifiers

Metronome enables you to configure certain alerts with more granular inclusion and exclusion conditions using alert specifiers. By default, a `low_remaining_contract_credit_and_commit_balance_reached` alert evaluates the **combined** balance of all active commits and credits for a customer. When that total drops below the configured threshold, you receive a single notification. With alert specifiers, you can change what gets evaluated:

* **Include** only commits and credits that match a specific set of custom field key values
* **Exclude** commits and credits that match certain custom field conditions
* **Group** balance evaluations by a custom field key, so you receive a separate notification for each unique value of that key

This enables patterns like:

* Fire an alert when the balance of product-specific credits (e.g., credits tagged `product_family: abc`) falls below a threshold, independently of your general credit pool
* Fire an alert when an individual commit (e.g., commits tagged with `unique_id: commit_xyz`) falls below a threshold
* Exclude certain perpetual credits from a general balance alert so it only fires when your standard credits are low

## How alert specifiers work

Alert specifiers are defined in the `alert_specifiers` array on a `low_remaining_contract_credit_and_commit_balance_reached` alert. Each specifier contains:

* `custom_field_filters`: An array of inclusion conditions that define which commits and credits count toward this alert. If omitted, all commits and credits are included. If a `key` is specified without a `value`, the alert groups evaluations by each unique value of that key.
* `exclude`: An array of exclusion conditions. Commits and credits matching any exclusion condition are removed from the evaluation, even if they satisfy the inclusion conditions.

Alert specifiers filter on custom fields. You can set custom fields on any commit or credit upon creation. Read more setting and viewing custom fields [here](https://docs.metronome.com/api-reference/custom-fields#custom-fields). Setting or updating a custom field value on a credit or commit will trigger a re-evaluation of any balance alert using `alert_specifiers` applicable to that credit or commit.

### Include specified key-value pairs

When you provide `custom_field_filters` with a specific `key` and `value`, only commits and credits matching **all** of those conditions are counted toward the alert threshold.

Multiple specifiers in the `alert_specifiers` array are evaluated as **OR** conditions — a commit or credit needs to match only one specifier to be included.

Within a single specifier's `custom_field_filters` array, multiple conditions are evaluated as **AND** — a commit or credit must match all listed conditions to be included.

<Note>
  **ALERT SPECIFIERS VS. CUSTOM FIELD FILTERS**

  `alert_specifiers[].custom_field_filter` with a specific `key` and `value` functions identically to the top-level [`custom_field_filter`](https://docs.metronome.com/api-reference/alerts/create-a-threshold-notification#body-custom-field-filters) when creating an alert. Use `alert_specifiers` for greater flexibility.
</Note>

Imagine you are granting a free credit promo on May 4th for a subset of customers and want to know when a customer’s promotional credits reach \$0. Create an alert that fires only when credits tagged `promo_code: may_the_fourth` reach a \$0 threshold.

```json theme={null}
POST /v1/alerts/create
{
  "name": "May the Fourth be with you promo alert",
  "alert_type": "low_remaining_contract_credit_and_commit_balance_reached",
  "threshold": 0,
  "alert_specifiers": [
    {
      "custom_field_filters": [
         {
            "entity": "ContractCredit",
            "key": "promo_code",
            "value": "may_the_fourth"
          }
       ]
    }
  ]
}
```

### Include all unique values of a specified key

When you provide a `custom_field_filters` entry with a `key` but no `value`, Metronome evaluates the balance **separately for each unique value** of that key. A webhook is sent if the total balance for all balances tagged with the one custom field key-value pair is below the notification threshold, and subsequently when any other groups of balances with the same key but different values meet the threshold.

An initial top-level webhook will be sent the first time any key-value pair with the defined key reaches the threshold.

<Note>
  **ONE GROUP KEY ONLY**

  Per-key grouping requires a single specifier with a single `key` and no `value`. You cannot group by more than one key at a time.
</Note>

Imagine your company offers several different promotional credits at a time. Any one customer may have multiple promotions running and wants to be alerted when each individual promotional credit reaches \$0. Instead of creating a dedicated alert to each promotion, create a grouped balance alert for all promotions.

```json theme={null}
POST /v1/alerts/create
{
  "name": "Parent promo alert",
  "alert_type": "low_remaining_contract_credit_and_commit_balance_reached",
  "threshold": 0,
  "alert_specifiers": [
    {
      "custom_field_filters": [
         {
            "entity": "ContractCreditorCommit",
            "key": "promo_code"
          }
       ]
    }
  ]
}
```

For each promotional credit given, create the credit with custom field key `promo_code` and the name of the promotion. The alert will automatically be applied to all customers and all current and future promotions without any code changes needed.

When a specific promotional credit on a customer reaches the threshold, you receive a webhook for that specific key-value pair that crossed the threshold. The `alert_specifiers` field in the payload includes the `key` and `value` that triggered the notification.

```json theme={null}
{
  "id": "notif_abc123",
  "type": "alerts.low_remaining_contract_credit_and_commit_balance_reached",
  "properties": {
    "customer_id": "cust_123",
    "alert_id": "alert_id",
    "alert_name": "Parent promo alert",
    "timestamp": "2026-05-07T15:08:44.865Z",
    "threshold": 0,
    "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
    "alert_specifiers": [
      {
        "custom_field_filters": [
          {
            "entity": "ContractCreditOrCommit",
            "key": "promo_code",
            "value": "may_7th_promo"
          }
        ]
      }
    ]
  }
}
```

If this is the first key-value pair to cross the threshold, you will also receive an additional notification for the overall alert. This webhook omits the specific `value` field in `custom_field_filters`, indicating it applies to the alert as a whole.

```json theme={null}
{
  "id": "notif_def456",
  "type": "alerts.low_remaining_contract_credit_and_commit_balance_reached",
  "properties": {
    "customer_id": "cust_123",
    "alert_id": "alert_id",
    "alert_name": "Parent promo alert",
    "timestamp": "2026-05-07T15:08:44.866Z",
    "threshold": 0,
    "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
    "alert_specifiers": [
      {
        "custom_field_filters": [
          {
            "entity": "ContractCreditOrCommit",
            "key": "promo_code"
          }
        ]
      }
    ]
  }
}
```

<Note>
  **INFO**

  You can set up to 3 per-key balance alerts for a single customer with support for up to 1K cardinality (unique key-value pairs) per group key. For keys with more than 1000 values, contact us via the [Metronome support portal](https://support.metronome.com/) to discuss your alert specifier configuration.
</Note>

### Exclude specified key-value pairs

The `exclude` field within a specifier removes specific commits or credits from an otherwise inclusive set. Multiple exclusion entries are evaluated as **OR** conditions — a commit or credit is excluded if it matches any one of them.

<Note>
  **EXCLUDED ENTITIES MUST BE INCLUDED IN THE SAME SPECIFIER**

  Exclusion conditions must target entities that are within the inclusion scope of the same specifier. For example, you cannot create a single alert specifier that includes commits but excludes credits.
</Note>

Create an alert that fires when the general (non-product-specific) credit balance falls below a threshold. Credits tagged `is_product_specific: true` are excluded from this evaluation.

```json theme={null}
POST /v1/alerts/create
{
  "customer_id": "cust_abc123",
  "name": "General credit balance alert",
  "alert_type": "low_remaining_contract_credit_and_commit_balance_reached",
  "threshold": 10000,
  "alert_specifiers": [
    {
      "exclude": [
        {
          "custom_field_filters": [
            {
              "entity": "ContractCreditOrCommit",
              "key": "is_product_specific",
              "value": "true"
            }
          ]
        }
      ]
    }
  ]
}
```

## Retrieving alert status

You can retrieve the current status of an alert with specifiers using `POST /v1/customer-alerts/get`. To retrieve the status of a specific custom field key-value pair, pass either `custom_field_filters` or `alert_specifiers` in the request body.

```json theme={null}
POST /v1/customer-alerts/get
{
  "alert_id": "alert_id",
  "customer_id": "cust_123",
  "alert_specifiers": [
    {
      "custom_field_filters": [
        {
          "entity": "ContractCreditOrCommit",
          "key": "promo_code",
          "value": "may_7th_promo"
        }
      ]
    }
  ]
}
```

The query will return the status of the specified key-value pair:

```json theme={null}
{
  "data": {
    "customer_status": "in_alarm",
    "alert": {
      "id": "alert_id",
      "name": "Per-product-family balance alert (excluding data compression)",
      "alert_type": "low_remaining_contract_credit_and_commit_balance_reached",
      "status": "active",
      "threshold": 0,
      "alert_specifiers": [
        {
          "custom_field_filters": [
            {
              "entity": "ContractCreditOrCommit",
		          "key": "promo_code",
			         "value": "may_7th_promo"
            }
          ]
        }
      ]
    }
  }
}
```

## Resolved webhooks

Receive a `low_remaining_contract_credit_and_commit_balance_resolved` webhook when an alert returns to `OK` from `IN_ALARM`. Contact us via the [Metronome support portal](https://support.metronome.com/) if you need this enabled.
