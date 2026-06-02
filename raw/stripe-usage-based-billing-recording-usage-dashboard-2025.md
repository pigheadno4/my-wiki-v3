<!-- Source URL: https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-in-bulk-dashboard -->
<!-- Fetched: 2026-05-05 -->

# Record usage in the Dashboard

Learn how to record your customer's usage in the Dashboard manually or using a CSV file.

You must record usage in Stripe to bill your customers the correct amounts each billing period. To record usage, you can manually add usage data or upload a CSV file with the usage data in the Dashboard. Stripe parses, validates, and transforms the usage data into meter events.

After the events upload successfully, you can see them in the live meter feed. You can also check the status of your uploaded files on the [Data management](https://dashboard.stripe.com/data-management/import-set) page.

## Add usage data manually

You can manually add usage data on the [Meters](https://dashboard.stripe.com/test/meters) page in the Stripe Dashboard.

1. On the [Meters](https://dashboard.stripe.com/test/meters) page, select the meter name.
1. On the meter page, click **Add usage** > **Manually input usage**.
1. On the **Add usage** page, do the following:
   - Select your customer from the **Customer** dropdown.
   - For **Value**, enter a sample value.
   - Click **Submit**.

## Upload a CSV file with usage data

After you prepare your CSV file with the usage data, you can upload it in the Stripe Dashboard. Make sure to format your file to match the template that’s available in the Dashboard. The maximum file size allowed is 5 MB.

### CSV file format and fields

Make sure your CSV file follows this sample file format:

| |
| |
| `timestamp` | `event_name` | `payload_stripe_customer_id` | `payload_value` |
| 2024-09-25 | ai_search_api | cus_QMJJtcu70R1x46 | 400 |
| 2024-09-26 | ai_search_api | cus_GAXJtSu6021a6s | 600 |
| 2024-09-27 | cpu_usage | cus_Qz0fwcfSysB9Z3 | 600 |

Follow the [Meter Event](https://docs.stripe.com/api/billing/meter-event/object.md) schema when including the following fields in your file:

| Field       | Description                                                                   |
| ----------- | ----------------------------------------------------------------------------- |
| `timestamp` | The date that the event occurred. We support the following timestamp formats: |

- `yyyy-MM-dd` – For example, `2024-09-23`.
- `yyyy-MM-dd'T'HH:mm:ssZ` – For example, `2024-09-23T16:22:25+0530`.
- `Epoch` – For example, `1727108545`. |
  | `event_name` | The name of the meter event. |
  | `payload_stripe_customer_id` | The ID of the customer that the event gets created against, either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-id) or a [Customer](https://docs.stripe.com/api/customers/object.md#customer_object-id). Find the `Account` ID (`acct_xxxx`) or `Customer` ID (`cus_xxxx`) on the [Customers](https://dashboard.stripe.com/customers) page. |
  | `payload_value` | The numerical usage value of the meter event, such as the number of hours to invoice for. If you specified a different key in the `value_settings`, you must update the column name to match the key value. For example, if you specify `tokens` in the `value_settings`, update the column name to `payload_tokens`. |

### Upload your CSV file

If your file contains errors, you can download an error file that includes the reason for each failed record. After you fix the errors, you can upload the updated file.

1. On the [Meters](https://dashboard.stripe.com/meters) page, select the meter name that you want to add usage events to.
1. On the meter page, click **Add usage** > **Upload file to add usage**.
1. On the **Upload file to add usage** page, select your file.
1. Click **Upload file**.
1. Verify the meter event count and aggregated value on the meter page.
