<!-- Source URL: https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-in-bulk -->
<!-- Fetched: 2026-05-05 -->

# Record usage for billing using Amazon S3

Learn how to record usage events in bulk using an Amazon S3 storage bucket.

You must record usage in Stripe to bill your customers the correct amounts each billing period. To record usage, you can send meter usage events to Stripe from your Amazon S3 storage bucket. Stripe parses, validates, and transforms the usage data into meter events.

After the events upload successfully, you can see them on your subscription invoice.

## Before you begin

Make sure you have the following:

- Admin account access to the [Stripe Dashboard](https://dashboard.stripe.com/dashboard)
- AWS account access to the [AWS Management Console](https://console.aws.amazon.com/) and your S3 bucket

## Upload meter usage events

You can upload your meter usage events as a CSV, JSON, or JSON Lines file.

> #### Need support for a different file format?
>
> If you want to upload files with a different structure or in a custom format, [contact us](mailto:user-data-acquisition-platform@stripe.com).

### File format and fields

Make sure your file follows the sample file format:

#### CSV

![Example of the CSV file format](assets/stripe-ubb-csv-format.png)

CSV file format

#### JSON

```json
[
  {
    "identifier": "26ac9e54-6a13-4b2e-90b0-fedae80bb8f7",
    "timestamp": 1692852080,
    "event_name": "ai_search_api",
    "payload": {
      "value": 200,
      "stripe_customer_id": "cus_123"
    }
  },
  {
    "timestamp": 1692852080,
    "event_name": "ai_search_api",
    "payload": {
      "value": 500,
      "stripe_customer_id": "cus_123"
    }
  }
]
```

#### JSON Lines

```jsonline
{"identifier":"123456","timestamp":1692852080,"event_name":"ai_search_api","payload":{"value":200,"stripe_customer_id":"cus_123"}}
{"timestamp":1692852080,"event_name":"ai_search_api","payload":{"value":500,"stripe_customer_id":"cus_123"}}
```

Follow the [Meter Event](https://docs.stripe.com/api/billing/meter-event/object.md) schema when including the following fields in your file:

| Field             | Description                                                                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `identifier`      | A unique identifier for the event. If you don’t provide one, Stripe can generate the unique identifier. We recommend using a globally unique identifier. |
| `timestamp`       | The time that the event occurred, measured in seconds since the Unix epoch.                                                                              |
| `event_name`      | The name of the meter event.                                                                                                                             |
| `payload_columns` | The set of columns that contain key names for customer and numerical usage values:                                                                       |

- `payload_stripe_customer_id`: The ID of the customer that the event gets created against, either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-id) or a [Customer](https://docs.stripe.com/api/customers/object.md#customer_object-id). Find the `Account` ID (`acct_xxxx`) or `Customer` ID (`cus_xxxx`) on the [Customers](https://dashboard.stripe.com/customers) page.
- `payload_value`: The numerical usage value of the meter event. By default, the column name is `payload_value`. If you specified a different field name when creating the meter event, you must update the column name to match the key value. For example, if you specify tokens in the `value_settings`, update the column name to `payload_tokens`. |

## Prepare your files in Amazon S3

You can validate your connection configuration using well-formatted data in your S3 bucket. The configuration process shows the available files, and runs an initial sync when configuring the connection.

1. Go to your [Amazon S3 console](https://s3.console.aws.amazon.com/).

1. Make sure to store your files in a designated S3 bucket that’s organized according to your import preferences. If needed, follow the [AWS guidelines](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) to create an S3 bucket.

   For successful retrieval, Stripe requires that file names adhere to [S3 object naming conventions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html) and files are 1 GB maximum.

1. Remember the bucket name and region because you need them for future steps.

1. Keep your [AWS Management Console](https://console.aws.amazon.com) open to configure an IAM role later.

## Configure the Amazon S3 Connector to import files

First, use the Stripe Dashboard to add the Amazon S3 Connector.

1. In the Stripe Dashboard, on the **Data management** > [Connectors](https://dashboard.stripe.com/data-management/connectors) tab, click **Add connector**.
1. In the **Choose connector** dialog, select **Amazon S3**.
1. In the **Requirements** dialog, enter a unique name for **Connector name**, then click **Next**.
1. Complete the steps in the **Permissions** dialog.

Next, configure the appropriate permissions for the Amazon S3 Connector.

1. In the AWS Management Console, go to the [IAM console](https://console.aws.amazon.com/iam/).
1. Create a custom trust policy:
   - In the navigation pane, click **Policies** > **Create policy**.
   - Select **JSON**, and replace the existing policy text by copying and pasting the code block provided in the Stripe Dashboard.
   - In the `Resource` section of the **Policy editor** code block, replace `USER_TARGET_BUCKET` with your intended bucket name.
   - Click **Next**.
   - Under **Policy details**, add a policy name. Optionally add any tags.
   - Click **Create policy**.
1. Create a role:
   - In the navigation pane, click **Roles** > **Create role**.
   - Select **Custom trust policy**, and copy and paste the code block provided in the Stripe Dashboard.
   - Click **Next**.
   - Locate and select the newly created permission policy to enable it, then click **Next**.
   - Copy and paste the provided role name, then click **Create role** to create a role name.

Then, make sure to establish a connection between Stripe and your Amazon S3 bucket.

1. In the AWS Management Console, do the following:
   - Provide your [AWS account ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindAccountId).
   - Provide the Bucket Name and Region.
   - If you use folders to organize your files in your Amazon S3 bucket, specify a folder within the above bucket. We only fetch data from the specified folder, not the entire bucket.
1. After you set up a new connector, the file preview validates that your credentials connect Stripe with the expected Amazon S3 bucket and folder. Stripe fetches all data modified in the last 90 days. This occurs every 5 minutes for objects with a `LastModified` date later than the last sync.
1. Preview the files available in the connected Amazon S3 bucket:
   - File names must be under 255 characters and include the appropriate extension, such as `.csv`, `.json`, or `.jsonl`.
   - Initial and recurring imports have an expected file format:
     - JSON files have **Billing Meter Event Transaction Template - JSON**.
     - JSON Lines files have **Billing Meter Event Transaction Template - JSONLINE**.
     - CSV files have **Billing Meter Event Transaction Template - CSV**.
1. To create an active data connection and initiate the data import, click **Done**.

After you upload a file to the Amazon S3 Connector, the usage events update within 5 minutes. This might take longer if your bucket contains a lot of unprocessed files.

You can check the status and details of processed files on the [Import set](https://dashboard.stripe.com/data-management/import-set) tab in the Stripe Dashboard.

## Rate limits

You can upload any number of files and records to your Amazon S3 bucket. Upload a file every 10 seconds or when the current file reaches one million records, whichever comes first. After upload, you can add events in a new file.

Avoid creating empty files, such as:

- CSV files that contain only the header row
- JSON files that contain only [] (empty square brackets)
- JSON Lines files that contain only {} (empty curly brackets)

Although Amazon S3 accepts non-zero byte files, they increase the object and file count, which might cause delays in the polling of files.

[Contact sales](https://stripe.com/contact/sales) if you need to process 100,000 events per second.

Amazon S3 polls a maximum of 50 files or up to 10 GB of data, and processes your uploaded data at a rate of 10,000 events per second. If you upload large files or a high volume of files, Stripe polls and processes the data to maintain this throughput rate.

For example, if you upload 100 files that each contain 100,000 records daily, it can take approximately 17 minutes to process the entire dataset (10 million events).

## Report and handle errors

Stripe polls the files that you upload to the Amazon S3 bucket and then processes these files asynchronously. If we detect errors during processing, Stripe notifies you using [events](https://dashboard.stripe.com/events).

### Format issues

Invalid file or record format errors occur when the contents in the uploaded file contain formatting or data issues.

You can subscribe to these events using a [webhook endpoint](https://dashboard.stripe.com/webhooks). Based on the event type, you can implement your own logic to handle these errors.

| Event                                  | Description                                                                                                                                                                                                                                                                                                                                                                           | Payload type |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `data_management.import_set.failed`    | Stripe creates a [data_management.import_set.failed](https://docs.stripe.com/api/events/types.md#event_types-data_management.import_set.failed) event when processing fails for an entire file. For example, if you omit a mandatory column, such as `event_name`. You can find the reason for failure in the `failed_reason` parameter of the event, and fix it before re-uploading. | `Snapshot`   |
| `data_management.import_set.succeeded` | Stripe creates a [data_management.import_set.succeeded](https://docs.stripe.com/api/events/types.md#event_types-data_management.import_set.succeeded) event when individual records fail in a partially processed file. For example, if you omit a value for a mandatory field, such as `stripe_customer_id` or `event_name`.                                                         |

You can find details of the failed records in the `status` parameter of the event. A `succeeded_with_errors` status indicates that at least one record failed because of invalid formatting. The `result.errors` gives the number of records that failed and the `file_id` of the file containing the failed records.

Use the [Files](https://docs.stripe.com/file-upload.md#download-file-contents) API to download a complete list of the failed records and detailed error descriptions. | `Snapshot` |

### Data issues

Files with correct formatting can fail processing because of invalid data within the file, such as incorrect values for the `event_name` or `stripe_customer_id`.

For detailed information about these failures, you can subscribe to the following events using a [webhook endpoint](https://dashboard.stripe.com/webhooks).

| Event                                     | Description                                                            | Payload type |
| ----------------------------------------- | ---------------------------------------------------------------------- | ------------ |
| `v1.billing.meter.error_report_triggered` | This event occurs when a meter has invalid usage events.               | `thin`       |
| `v1.billing.meter.no_meter_found`         | This event occurs when usage events have missing or invalid meter IDs. | `thin`       |

### Example payloads

#### Example error report event

The following is an example payload for a `v1.billing.meter.error_report_triggered` event.

```json
{
  "id": "evt_test_65R2GpwDsnmpzihMjdT16R2GDhI4SQdXJGRbvn7JA8mPEm",
  "object": "v2.core.event",
  "created": "2024-08-28T20:54:12.051Z",
  "data": {
    "developer_message_summary": "There is 1 invalid event",
    "reason": {
      "error_count": 1,
      "error_types": [
        {
          "code": "meter_event_no_customer_defined",
          "error_count": 1,
          "sample_errors": [
            {
              "error_message": "Customer mapping key stripe_customer_id not found in payload.",
              "request": {
                "id": "",
                "idempotency_key": "37c741d8-1f7e-4adc-af16-afdca1d73b37"
              }
            }
          ]
        }
      ]
    },
    "validation_end": "2024-08-28T20:54:10.000Z",
    "validation_start": "2024-08-28T20:54:00.000Z"
  },
  "reason": null,
  "related_object": {
    "id": "mtr_test_61R2GlpFXJ4R3L5DN41Fb82guyGVEUmO",
    "type": "billing.meter",
    "url": "/v1/billing/meters/mtr_test_61R2GlpFXJ4R3L5DN41Fb82guyGVEUmO"
  },
  "type": "v1.billing.meter.error_report_triggered"
}
```

#### Example error event for an incorrect meter

The following is an example payload for a `v1.billing.meter.no_meter_found` event.

```json
{
  "created": "2024-10-01T20:42:52.203Z",
  "id": "evt_test_61REarcdWIsXleUiz16REahOMTSQbAhSD0fdnF9JAUdk",
  "object": "v2.core.event",
  "context": null,
  "type": "v1.billing.meter.no_meter_found",
  "data": {
    "developer_message_summary": "There is 1 invalid event",
    "reason": {
      "error_count": 1,
      "error_types": [
        {
          "code": "no_meter",
          "error_count": 1,
          "sample_errors": [
            {
              "error_message": "No meter was found matching event_name d2aa8cb3-3f00-44a4-b98f-3fbd1d0e93b1.",
              "request": {
                "identifier": "df5d4002-515b-4090-8fe2-a1b1f6f5b945"
              }
            }
          ]
        }
      ]
    },
    "validation_end": "2024-10-01T20:42:50.000Z",
    "validation_start": "2024-10-01T20:42:40.000Z"
  },
  "livemode": false,
  "reason": null,
  "related_object": {}
}
```

### Error codes

The `reason.error_types.code` provides the error categorization that triggered the error. Possible error codes include:

- `meter_event_customer_not_found`
- `meter_event_no_customer_defined`
- `meter_event_dimension_count_too_high`
- `archived_meter`
- `timestamp_too_far_in_past`
- `timestamp_in_future`
- `meter_event_value_not_found`
- `meter_event_invalid_value`
- `no_meter` (supported only for the `v1.billing.meter.no_meter_found` event type)

### Listen to events

You can listen to events by setting up an [event destination](https://docs.stripe.com/event-destinations.md).

1. On the [Event destinations](https://dashboard.stripe.com/webhooks) tab in Workbench, click **Create new destination**. Alternatively, use this [template](https://dashboard.stripe.com/webhooks/create?payload_style=thin&events=v1.billing.meter.error_report_triggered%2Cv1.billing.meter.no_meter_found) to configure a new destination in Workbench with the two event types pre-selected.

1. Click **Show advanced options**, then select the **Thin** payload style.

1. Select `v1.billing.meter.error_report_triggered` and `v1.billing.meter.no_meter_found` from the list of events.

1. Create a handler to process the event.

   #### Node.js

   ```javascript
   const express = require("express");
   const { Stripe } = require("stripe");

   const app = express();

   const apiKey = process.env.STRIPE_API_KEY;
   const webhookSecret = process.env.WEBHOOK_SECRET;

   const client = new Stripe(apiKey);

   app.post(
     "/webhook",
     express.raw({ type: "application/json" }),
     async (req, res) => {
       const sig = req.headers["stripe-signature"];

       try {
         const thinEvent = client.parseThinEvent(req.body, sig, webhookSecret);

         // Fetch the event data to understand the failure
         const event = await client.v2.core.events.retrieve(thinEvent.id);
         if (event.type == "v1.billing.meter.error_report_triggered") {
           const meter = await event.fetchRelatedObject();
           const meterId = meter.id;
           // Record the failures and alert your team
           // Add your logic here
         }
         res.sendStatus(200);
       } catch (err) {
         console.log(`Webhook Error: ${err.message}`);
         res.status(400).send(`Webhook Error: ${err.message}`);
       }
     },
   );

   app.listen(4242, () => console.log("Running on port 4242"));
   ```

1. Test your handler by configuring a [local listener](https://docs.stripe.com/cli/listen) with the [Stripe CLI](https://docs.stripe.com/stripe-cli.md) to send events to your local machine for testing before deploying the handler to production. Use the `--forward-thin-to` flag to specify which URL to forward the `thin` events to and the `--thin-events` flag to specify which thin events to forward to your application. You can forward all thin events with an asterisk (`*`), or a subset of thin events.

   ```sh
   $ stripe listen --forward-thin-to localhost:4242/webhooks --thin-events "*"
   ```

1. Trigger test events to your handler. Use the [trigger function](https://docs.stripe.com/cli/trigger) to run the following commands, which simulates the respective events in your account for testing.

   ```sh
   $ stripe trigger v1.billing.meter.error_report_triggered --api-key <your-secret-key>
   $ stripe trigger v1.billing.meter.no_meter_found --api-key <your-secret-key>
   ```

1. If you process events with a webhook endpoint, [verify the webhook signatures](https://docs.stripe.com/webhooks.md#verify-official-libraries) to secure your endpoint and validate all requests are from Stripe.

1. Correct the invalid events and save them to a new file. Then, upload the file to your Amazon S3 bucket for processing.
