<!-- Source URL: https://docs.stripe.com/agentic-commerce/product-feed/sftp-catalog-ingestion -->
<!-- Fetched: 2026-05-12 -->

# SFTP catalog ingestion

Learn how to receive and ingest business product catalogs from Stripe over SFTP.

Stripe provides business product catalogs to your SFTP (SSH File Transfer Protocol) server as daily full-catalog snapshots. Use this guide to set up your ingestion pipeline and validate incoming data.

## Connectivity and directory structure

Stripe connects to your server using the following configuration:

- **Protocol**: SFTP (SSH File Transfer Protocol) over port `22`
- **Authentication**: SSH key-based using Ed25519
- **Password authentication**: Disabled

### Metadata

Each business directory contains a `merchant_metadata.json` file. Read this file before you ingest catalog data to verify that you’re importing data for the correct business.

```json
{
  "stripe_profile_id": "profile_12345",
  "business_url": "https://www.acmewidgets.com",
  "return_policy": "https://www.acmewidgets.com/returns",
  "privacy_policy": "https://www.acmewidgets.com/privacy",
  "terms_of_service": "https://www.acmewidgets.com/tos",
  "last_updated": "2026-03-30T10:00:00Z"
}
```

### Directory structure

Stripe assigns each business a unique top-level directory. Stripe organizes the SFTP root by business Stripe profile ID and separates data by feed type within each business directory.

```
/root
  stripe-verification.txt      # Uploaded by agent during onboarding
  /[stripe_profile_id]/
    merchant_metadata.json
    /catalog/                  # Full daily snapshots
      full_catalog_part_1_of_2.csv.gz
      full_catalog_part_2_of_2.csv.gz
      manifest.json
    /updates/                  # High-frequency deltas (opt-in)
      delta_part_1_of_1.csv.gz
      manifest.json
```

### SFTP server verification

During agent onboarding in the Stripe Dashboard, you provide your SFTP host details and Stripe generates a unique challenge token. You must upload this token to the root of your SFTP server in a file named `stripe-verification.txt`.

After Stripe receives your SFTP host details and a seller enables your agent, Stripe starts syndicating that seller’s product catalog to your SFTP host. Syndication begins only after Stripe verifies that the challenge token in `stripe-verification.txt` matches the token generated during onboarding. Keep this file in place—removing it can affect your ability to receive feeds.

## Hybrid feed model

Stripe delivers data in two distinct streams to optimize bandwidth and processing.

| Feed                | Frequency      | Primary purpose                                                  | File name pattern                         |
| ------------------- | -------------- | ---------------------------------------------------------------- | ----------------------------------------- |
| Product Master Feed | Every 24 hours | Stable metadata: descriptions, images, brand, and taxonomy       | `full_catalog_part_[N]_of_[Total].csv.gz` |
| Delta Feed (opt-in) | Hourly         | Real-time price, sale price, availability, and inventory changes | `delta_part_[N]_of_[Total].csv.gz`        |

## Sharding and manifest

For catalogs larger than 100,000 rows, Stripe might split the data into multiple shard files. Stripe uploads `manifest.json` last. Treat it as the signal that the batch is complete and ready to ingest. Don’t begin ingestion until `manifest.json` is present. If data files appear in `catalog/` or `updates/` but `manifest.json` doesn’t arrive, [contact Stripe Support](https://support.stripe.com/contact).

### Manifest structure

The manifest includes the Stripe profile ID, batch metadata, feed type, total shard count, and the full list of shard file names.

```json
{
  "stripe_profile_id": "profile_12345",
  "batch_timestamp": "2026-03-25T14:30:00Z",
  "feed_type": "product_master",
  "total_shards": 2,
  "files": [
    "full_catalog_part_1_of_2.csv.gz",
    "full_catalog_part_2_of_2.csv.gz"
  ]
}
```

## CSV file format

All data files use gzip compression with a `.csv.gz` extension. The uncompressed content is UTF-8 encoded, comma-separated, includes a header row, and follows standard CSV quoting rules for commas, quotes, and embedded line breaks.

For all fields:

- An empty value means the field is unset.
- Each row has a unique `id`.
- Multi-value fields such as `additional_image_link` are serialized as comma-separated URLs within a single quoted CSV field.

## Product Master Feed schema

The Product Master Feed contains the full catalog snapshot for stable product metadata. Each row represents a product or variant. Required fields are always present. Recommended fields are typically present but might be absent for some products. Optional fields might or might not be populated, depending on the business’s data.

### Required and recommended fields

| Field                   | Requirement                      | Description                                                                                                                      |
| ----------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| id                      | Required                         | Unique product or SKU ID. Maximum 100 characters.**Example: SKU12AB3456**                                                        |
| title                   | Required                         | Product name. Maximum 150 characters.**Example: Men’s Floral Polo Shirt**                                                        |
| description             | Required                         | Plain text description. Maximum 5,000 characters.**Example: Bring a burst of fun to your golf game with this Men’s Floral Polo** |
| link                    | Required                         | Business landing page URL.**Example: https://example.com/product/SKU12AB3456**                                                   |
| image_link              | Required                         | Main high-resolution image URL.**Example: https://example.com/image1.jpg**                                                       |
| brand                   | Required                         | Brand name. Maximum 70 characters.**Example: Acme**                                                                              |
| price                   | Required                         | Price and currency code.**Example: 29.99 USD**                                                                                   |
| availability            | Required                         | Stock status. Allowed values: `in_stock`, `out_of_stock`, `preorder`, or `backorder`.**Example: in_stock**                       |
| gtin                    | Recommended                      | Global Trade Item Number (for example, UPC or ISBN).**Example: 3234567890126**                                                   |
| google_product_category | Recommended                      | Google taxonomy value.**Example: Apparel & Accessories > Clothing**                                                              |
| mpn                     | Required if `gtin` is missing    | Manufacturer Part Number. Maximum 70 characters.**Example: STR12345**                                                            |
| condition               | Required if not `new`            | Product condition. Allowed values: `new`, `refurbished`, or `used`.**Example: new**                                              |
| item_group_id           | Required if variants exist       | Shared ID for a group of product variants.**Example: GROUP_ABC**                                                                 |
| inventory_quantity      | Required if inventory is tracked | Total units available.**Example: 100**                                                                                           |
| shipping                | Required for physical goods      | Shipping cost and speed.**Example: US:::5.99 USD**                                                                               |

### Optional fields

| Field                         | Requirement                                          | Description                                                                                                                                                                                              |
| ----------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| disable_checkout              | Optional                                             | When `true`, this value excludes the product from in-agent checkout. Redirect the customer to `link` to complete the purchase.**Example: true**                                                          |
| additional_image_link         | Optional                                             | Up to 10 additional image URLs, serialized as comma-separated values in a single quoted CSV field.**Example: https://example.com/image2.jpg,https://example.com/image3.jpg**                             |
| video_link                    | Optional                                             | Product video URL.**Example: https://youtu.be/12345**                                                                                                                                                    |
| model_3d_link                 | Optional                                             | URL for a 3D product model in GLB or GLTF format.**Example: https://example.com/products/xyz.glb**                                                                                                       |
| product_category              | Optional                                             | Business-defined category, separated by `>`.**Example: Clothing > Shirts > Polo**                                                                                                                        |
| age_group                     | Optional                                             | Intended demographic.**Example: adult**                                                                                                                                                                  |
| material                      | Optional                                             | Primary fabric or material.**Example: Cotton**                                                                                                                                                           |
| length                        | Optional                                             | Product length with unit.**Example: 20 in**                                                                                                                                                              |
| width                         | Optional                                             | Product width with unit.**Example: 20 in**                                                                                                                                                               |
| height                        | Optional                                             | Product height with unit.**Example: 10 in**                                                                                                                                                              |
| weight                        | Optional                                             | Product weight with unit.**Example: 2.5 lb**                                                                                                                                                             |
| item_group_title              | Optional                                             | Human-readable variant group title.**Example: Men’s Floral Polo**                                                                                                                                        |
| color                         | Optional                                             | Primary color.**Example: Blue**                                                                                                                                                                          |
| size                          | Optional                                             | Product size.**Example: XL**                                                                                                                                                                             |
| size_system                   | Optional                                             | Two-letter country code (ISO 3166).**Example: US**                                                                                                                                                       |
| gender                        | Optional                                             | Intended gender. Allowed values: `male`, `female`, or `unisex`.**Example: male**                                                                                                                         |
| custom_variant_option_name_1  | Optional                                             | First custom variant option name.**Example: Frame Color**                                                                                                                                                |
| custom_variant_option_value_1 | Optional                                             | Value for the first custom variant option.**Example: Matte Black**                                                                                                                                       |
| custom_variant_option_name_2  | Optional                                             | Second custom variant option name.                                                                                                                                                                       |
| custom_variant_option_value_2 | Optional                                             | Value for the second custom variant option.                                                                                                                                                              |
| custom_variant_option_name_3  | Optional                                             | Third custom variant option name.                                                                                                                                                                        |
| custom_variant_option_value_3 | Optional                                             | Value for the third custom variant option.                                                                                                                                                               |
| availability_date             | Optional                                             | Date a preordered product becomes available (ISO 8601).**Example: 2026-06-01**                                                                                                                           |
| expiration_date               | Optional                                             | Date the product should stop showing (ISO 8601).**Example: 2026-12-31**                                                                                                                                  |
| inventory_not_tracked         | Optional                                             | When `true`, inventory isn’t tracked for this product, such as digital goods.**Example: true**                                                                                                           |
| sale_price                    | Optional                                             | Discounted price and currency code.**Example: 24.99 USD**                                                                                                                                                |
| sale_price_effective_date     | Optional                                             | Sale window using `YYYY-MM-DD/YYYY-MM-DD`.**Example: 2026-12-01/2026-12-15**                                                                                                                             |
| stripe_product_tax_code       | Optional                                             | Stripe Product Tax Code for tax classification.                                                                                                                                                          |
| third_party_tax_code          | Optional                                             | Tax classification for [Anrok](https://www.anrok.com). See the [price and promotions field reference](https://docs.stripe.com/agentic-commerce/product-feed.md#price-and-promotions) for format details. |
| tax_behavior                  | Optional                                             | Indicates whether the price is tax-inclusive or tax-exclusive.                                                                                                                                           |
| applicable_fees               | Optional                                             | Per-unit fees and surcharges based on product type and region.                                                                                                                                           |
| shipping_cost_basis           | Optional                                             | Whether shipping cost applies per order or per item. Allowed values: `per_order` or `per_item`.                                                                                                          |
| free_shipping_threshold       | Optional                                             | Order-level free-shipping threshold.                                                                                                                                                                     |
| popularity_score              | Optional                                             | Aggregate popularity indicator on a 0–5 scale.**Example: 4.7**                                                                                                                                           |
| return_rate                   | Optional                                             | Percentage of units returned, expressed as a numeric value on a 0–100 scale (for example, 2.0 represents 2%).**Example: 2.0**                                                                            |
| product_review_count          | Optional                                             | Total number of reviews.**Example: 124**                                                                                                                                                                 |
| product_review_rating         | Required if `product_review_count` is greater than 0 | Average review rating on a 1–5 scale.**Example: 4.3**                                                                                                                                                    |
| delete                        | Optional                                             | When `true`, the product has been permanently removed. Only the `id` and `delete` columns are populated for that row.**Example: true**                                                                   |

## Optional: Delta Feed schema

The Delta Feed contains only fields that change frequently. It updates existing products and doesn’t replace the full Product Master Feed. Delta Feed delivery isn’t enabled by default. [Contact us](https://support.stripe.com/contact) to enable it for your account.

When a field appears in both the Product Master Feed and a later delta batch, the newer successfully processed batch takes precedence.

### Delta Feed fields

| Field                     | Requirement                              | Description                                                                                                                                     |
| ------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| id                        | Required                                 | Matches the `id` from the Product Master Feed.**Example: SKU12AB3456**                                                                          |
| price                     | Required                                 | Current price with currency code.**Example: 29.99 USD**                                                                                         |
| availability              | Required                                 | Current availability status. Allowed values: `in_stock`, `out_of_stock`, `preorder`, or `backorder`.**Example: in_stock**                       |
| inventory_quantity        | Required                                 | Exact count of sellable units.**Example: 42**                                                                                                   |
| availability_date         | Required if `availability` is `preorder` | Date the preordered product becomes available (ISO 8601).**Example: 2026-06-01**                                                                |
| sale_price                | Optional                                 | Discounted price if a promotion has started.**Example: 24.99 USD**                                                                              |
| sale_price_effective_date | Optional                                 | Sale window using `YYYY-MM-DD/YYYY-MM-DD`.**Example: 2026-12-01/2026-12-15**                                                                    |
| disable_checkout          | Optional                                 | When `true`, this value excludes the product from in-agent checkout. Redirect the customer to `link` to complete the purchase.**Example: true** |

## Synchronization rules

The contents of the SFTP directory are the current source of truth.

### How Stripe delivers data

Use the following delivery behaviors to design your ingestion process.

- Stripe overwrites the contents of `catalog` and `updates` each cycle. The SFTP directory always reflects the latest batch. Stripe doesn’t retain prior batches.
- Stripe uploads data files first and uploads `manifest.json` last so you don’t ingest a partial batch.

### Process feeds

Use these guidelines to process each feed batch correctly.

- Use `batch_timestamp` to determine whether you already processed a batch.
- Treat the latest full Product Master Feed as authoritative for the complete catalog state.

### Deletion behavior

Support both explicit and implicit deletion:

- **Explicit deletion**: If a row in the Product Master Feed includes `delete=true`, remove the product or mark it inactive.
- **Implicit deletion**: If a product was previously known but is absent from the latest full Product Master Feed, remove the product or mark it inactive.
- **Reappearance**: If a previously deleted or omitted product appears again in a later full Product Master Feed, treat it as active unless `delete=true` is set.

## Ingestion rules

Apply these rules to make your ingestion pipeline reliable and auditable:

- **Timestamp validation**: Only update local records if the incoming record is newer than the stored record when record-level timestamps are available.
- **Idempotency**: Reprocessing the same successfully processed batch must not create duplicate products or duplicate updates.
- **Auditability**: Retain your own record of processed `batch_timestamp` values.
