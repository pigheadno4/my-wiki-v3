<!-- Source URL: https://docs.paypal.ai/growth/agentic-commerce/store-sync/product-catalog/connect-product-feed -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect your product feed to PayPal

When your product feed is ready, you need to enable PayPal to ingest it. This page tells developers who are responsible for configuring product feed ingestion how to set up each supported ingestion method, set an update frequency, and handle multi-storefront configurations.

## Before you begin

Before you connect your feed, ensure that:

- Your product feed file is formatted and validated according to the feed specification requirements in [Create a product feed](/growth/agentic-commerce/store-sync/product-catalog/create-a-product-catalog/).
- You have your PayPal merchant ID available.
- Depending on your chosen ingestion method, you have one of the following ready:
  - **Public URL:** A stable, publicly accessible URL to your feed file. For more information about this path, see the [Public URL section](#public-url).
  - **FTP or SFTP:** Your FTP/SFTP host URL, port, username, and password. For more information about this path, see the [FTP or SFTP section](#ftp-or-sftp).
  - **S3 or GCS:** Read access granted to the PayPal service account for the bucket that hosts your feed file. For more information about this path, see the [S3 or GCS section](#s3-or-gcs).

## Catalog ingestion options

PayPal supports 3 methods for ingesting your product feed. Choose the option that best fits your infrastructure, then follow the steps for that method.

<Tip>If all options are available to you, PayPal recommends using a public URL for easier setup and maintenance.</Tip>

<AccordionGroup>
  <Accordion title="Public URL">
    Provide a publicly accessible URL to your product catalog file. PayPal fetches the file from this URL on your configured schedule.

    ### Connect your feed

    1. Host your feed file at a stable, publicly accessible URL. For example: `https://www.merchantname.com/productCatalog.csv`.
    2. If your URL requires authentication, prepare your credentials in `user:pass` format. Basic authentication is supported.
    3. If your infrastructure restricts inbound traffic, allowlist the PayPal downloader IP addresses. Contact your PayPal account manager to obtain the current IP list.
    4. Provide the URL (and credentials, if applicable) to your PayPal account manager or solutions partner to complete the configuration.

    ### Confirm that ingestion is active

    Your PayPal account manager will confirm when ingestion is active and your catalog is available in Store Sync.

    ### Example

    ```
    Feed URL: https://www.merchantname.com/productCatalog.csv
    Auth (if required): feeduser:feedpassword
    ```

  </Accordion>

  <Accordion title="FTP or SFTP">
    Provide FTP or SFTP credentials so PayPal can retrieve your feed file directly from your server.

    ### Connect your feed

    1. Ensure your feed file is available on your FTP or SFTP server and is updated on your intended schedule.
    2. Collect the following credentials:
       * Feed file URL (for example, `ftp://products.domain.com/merchant/merchantFeed.csv.gz`)
       * Port
       * Username
       * Password
    3. Provide these credentials to your PayPal account manager or solutions partner to complete the configuration.

    ### Confirm that ingestion is active

    Your PayPal account manager will confirm when ingestion is active and your catalog is available in Store Sync.

    ### Example

    ```
    Feed URL: ftp://products.domain.com/merchant/merchantFeed.csv.gz
    Port: 21
    Username: feeduser
    Password: feedpassword
    ```

  </Accordion>

  <Accordion title="S3 or GCS">
    Grant the PayPal service account read access to the S3 or GCS bucket that hosts your feed file.

    ### Connect your feed

    1. Contact your PayPal account manager to obtain the PayPal service account identifier for your region.
    2. Grant the PayPal service account read access to the bucket that contains your feed file.
    3. Ensure the feed file path within the bucket is stable and updated on your intended schedule.
    4. Provide the bucket name and feed file path to your PayPal account manager or solutions partner to complete the configuration.

    ### Confirm that ingestion is active

    Your PayPal account manager will confirm when ingestion is active and your catalog is available in Store Sync.

    ### Example

    ```
    Bucket: s3://my-merchant-bucket/feeds/
    Feed file path: feeds/productCatalog.csv
    ```

  </Accordion>
</AccordionGroup>

## Update frequency

Regardless of which ingestion method you choose, you must regularly update your feed file and ensure that it remains accessible to PayPal. By default, PayPal downloads feeds once daily.

After each download, PayPal processes the feed and updates your catalog. Updated product availability, pricing, and listings become active in Store Sync after the next successful ingestion cycle completes. If you require a different cadence, contact your PayPal account manager to adjust the schedule.

Keeping your product catalog file up to date ensures:

- Product availability is current.
- Pricing is accurate.
- New products are discoverable.
- Discontinued products are removed.

## Configure ingestion for multiple storefronts

PayPal supports merchants with multiple storefronts through ingestion from FTP/SFTP, S3, or GCS. To configure multi-storefront ingestion, provide a `manifest.csv` file with your feed.

Each row in the manifest file represents one merchant storefront and must include the following fields.

| Field                    | Description                                                     |
| ------------------------ | --------------------------------------------------------------- |
| `storeName`              | The name of the storefront                                      |
| `storeUrl`               | The URL of the storefront                                       |
| `paypalMerchantId`       | The PayPal merchant ID for the storefront                       |
| `country`                | The country of the storefront                                   |
| `currency`               | The currency used by the storefront                             |
| `favIcon`                | URL to the storefront's favicon                                 |
| `pathToFileInThisBucket` | The path to the feed file for this storefront within the bucket |

For each merchant that you list in your manifest, ensure the corresponding feed file that the manifest references in `pathToFileInThisBucket` is present in the bucket.

<Alert type="success">Your solutions and integration partner will work with the PayPal Catalog team to finalize your integration.</Alert>

## Troubleshoot common issues

The following table describes common ingestion issues and how to fix them.

| Issue                                                     | Cause                                                                    | Fix                                                                                                                                                                                                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PayPal cannot access the feed file.                       | The URL is not publicly accessible or returns a non-200 status.          | Verify that the URL is reachable from outside your network and returns a `200` status code. If your infrastructure restricts inbound traffic, add the PayPal downloader IP addresses to your allowlist. Contact your account manager for the current IP list. |
| Authentication fails on the public URL.                   | Credentials are missing or incorrect.                                    | Confirm that the credentials are in `user:pass` format and are correct. If necessary, provide the corrected credentials to your account manager.                                                                                                              |
| The FTP or SFTP connection is refused.                    | You provided an incorrect port, hostname, or credentials                 | Verify that all connection details are correct: host URL, port, username, and password. Confirm that the FTP/SFTP server is accessible from external hosts.                                                                                                   |
| S3 or GCS access is denied.                               | PayPal service account does not have read permission.                    | Confirm that the correct PayPal service account identifier for your region has been granted read access. Contact your account manager to verify the service account.                                                                                          |
| The feed file downloads, but the catalog is not updated.  | The feed file path or filename changed.                                  | Ensure the feed file is always written to the same stable path. PayPal uses the configured path on every download cycle.                                                                                                                                      |
| A multi-storefront feed is not ingesting all storefronts. | `manifest.csv` references a file that is not present in the feed bucket. | Verify that every `pathToFileInThisBucket` value in your manifest points to an existing file in the feed bucket.                                                                                                                                              |
| Catalog updates are delayed.                              | The feed is updated less frequently than the ingestion schedule.         | Update your feed file at least as often as your configured ingestion cadence. Contact your account manager if you need to adjust the download schedule.                                                                                                       |

## Next steps

When ingestion is active and confirmed, your products are available for AI-driven discovery and checkout across PayPal surfaces. The next step is to [set up your API](/growth/agentic-commerce/store-sync/your-api/api-overview/).

To review how agents interact with your catalog, see [Store Sync overview](/store-sync/overview).
