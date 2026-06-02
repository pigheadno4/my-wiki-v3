<!-- Source URL: https://docs.paypal.ai/growth/agentic-commerce/store-sync/product-catalog/create-a-product-catalog -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a product catalog

Your platform needs to provide essential product data to enable product discovery and merchant management in Store Sync. A well-structured product feed ensures that AI agents can find, understand, and transact against your inventory across PayPal surfaces.

This page tells developers who are responsible for integrating product feeds into Store Sync how to format and structure their product feed. To complete the integration, you will review prerequisites, choose a file format, select a feed specification, structure your product variants, and verify your feed before connecting it to Store Sync.

## Before you begin

Before you create your product feed, be sure that you're ready to meet these requirements:

- To access Store Sync and the product feed integration, merchants must [contact the PayPal AI team](https://www.paypal.com/us/business/ai#form) to request access.
- Your feed file must not exceed 4 GB in size.
- All feeds must be UTF-8 encoded and include a header row specifying column names.
- For compressed formats, the archive must contain only one CSV or TSV file.

## Supported file formats

PayPal supports the following file formats for product feeds. Choose the format that best fits your existing export pipeline.

| Format | Description            | Delimiter |
| ------ | ---------------------- | --------- |
| `CSV`  | Comma-separated values | `,`       |
| `TSV`  | Tab-separated values   | `\t`      |
| `PSV`  | Pipe-separated values  | `\|`      |

You can also compress your feed file in either of the following formats before uploading. The archive must contain only one CSV or TSV file.

| Format | Description                                                    |
| ------ | -------------------------------------------------------------- |
| `GZ`   | Gzip compressed archive that contains a single CSV or TSV file |
| `ZIP`  | ZIP compressed archive that contains a single CSV or TSV file  |

## Feed specifications

PayPal supports 3 feed specifications. Choose the option that best fits your existing setup and business needs. A more complete and detailed product feed enables PayPal to surface your products more effectively in relevant shopping experiences.

Regardless of which specification you use, each row in your feed represents a single product variant. The sections below describe the required and important optional fields for each specification.

<Tip>The field lists in the following sections highlight the most critical fields for each specification, but they are not exhaustive. For the complete field reference, see the full specification documentation for [Google Product Feed](https://support.google.com/merchants/answer/7052112) or [OpenAI ACP Product Feed](https://platform.openai.com/docs/guides/acp).</Tip>

<AccordionGroup>
  <Accordion title="Google Product Feed specification">
    The most common product feed format. If you already maintain a [Google Product Feed](https://support.google.com/merchants/answer/7052112), you can reuse it to power both traditional and AI-driven discovery with minimal extra work.

    The following fields apply when using the Google Product Feed specification.

    ### Required fields

    You must include the following fields in every row of your Google Product Feed.

    | Field          | Description                                 | Example                                                     |
    | -------------- | ------------------------------------------- | ----------------------------------------------------------- |
    | `id`           | Unique product identifier (variant ID)      | `"shirt123-red-m"`                                          |
    | `title`        | Product title                               | `"Classic T-Shirt - Red, Medium"`                           |
    | `link`         | URL to the product page                     | `"https://www.yourstore.com/products/classic-tshirt-red-m"` |
    | `image_link`   | URL to the main product image               | `"https://www.yourstore.com/images/tshirt-red-m.jpg"`       |
    | `description`  | Product description (minimum 25 characters) | `"Comfortable cotton t-shirt in vibrant red color..."`      |
    | `price`        | Product price with currency code            | `"19.99 USD"`                                               |
    | `availability` | Stock status                                | `"in_stock"`                                                |

    ### Important optional fields

    Including these fields improves product discoverability, search relevance, and personalized recommendations.

    | Field                     | Description                                                           | Example                                                    |
    | ------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------- |
    | `item_group_id`           | Parent product ID for variants. Required if the product is a variant. | `"shirt123"`                                               |
    | `brand`                   | Product brand name                                                    | `"YourBrand"`                                              |
    | `mpn`                     | Manufacturer Part Number                                              | `"MP12345"`                                                |
    | `gtin`                    | Global Trade Item Number                                              | `"5901234123457"`                                          |
    | `sale_price`              | Discounted price                                                      | `"15.99 USD"`                                              |
    | `google_product_category` | Google taxonomy category                                              | `"Apparel & Accessories > Clothing > Shirts & Tops"`       |
    | `product_type`            | Your store's category path                                            | `"Men's > T-Shirts"`                                       |
    | `additional_image_link`   | URL to an additional product image                                    | `"https://www.yourstore.com/images/tshirt-red-m-back.jpg"` |
    | `color`                   | Product color                                                         | `"red"`                                                    |
    | `size`                    | Product size                                                          | `"medium"`                                                 |
    | `size_system`             | Size system (country code or system code)                             | `"US"`                                                     |
    | `gender`                  | Target gender                                                         | `"male"`                                                   |
    | `group_id`                | Parent product ID for variants                                        | `"shirt123"`                                               |

  </Accordion>

  <Accordion title="OpenAI ACP Product Feed specification">
    A newer specification that is optimized for conversational, agent-led shopping and instant checkout in LLM environments, the OpenAI ACP Product Feed format has richer requirements around inventory, shipping, and structured context.

    The following fields apply when using the OpenAI ACP Product Feed specification.

    ### Required fields

    You must include the following fields in every row of your OpenAI ACP feed.

    | Field                    | Description                                                           | Example                                                     |
    | ------------------------ | --------------------------------------------------------------------- | ----------------------------------------------------------- |
    | `item_id`                | Unique product identifier (variant ID)                                | `"shirt123-red-m"`                                          |
    | `group_id`               | Parent product ID for variants. Required if the product is a variant. | `"shirt123"`                                                |
    | `title`                  | Product title                                                         | `"Classic T-Shirt - Red, Medium"`                           |
    | `url`                    | URL to the product page                                               | `"https://www.yourstore.com/products/classic-tshirt-red-m"` |
    | `image_url`              | URL to the main product image                                         | `"https://www.yourstore.com/images/tshirt-red-m.jpg"`       |
    | `description`            | Product description (minimum 25 characters)                           | `"Comfortable cotton t-shirt in vibrant red color..."`      |
    | `price`                  | Product price with currency code                                      | `"19.99 USD"`                                               |
    | `availability`           | Stock status                                                          | `"in_stock"`                                                |
    | `brand`                  | Product brand name                                                    | `"YourBrand"`                                               |
    | `listing_has_variations` | Indicates if the listing has variations                               | `"true"`                                                    |
    | `seller_name`            | Seller name                                                           | `"Example Store"`                                           |
    | `seller_url`             | Seller page URL                                                       | `"https://yourstore.com"`                                   |
    | `seller_privacy_policy`  | Seller privacy policy URL                                             | `"https://yourstore.com/privacy"`                           |
    | `seller_tos`             | Seller terms of service URL                                           | `"https://yourstore.com/terms"`                             |
    | `return_policy`          | Return policy URL                                                     | `"https://yourstore.com/returns"`                           |
    | `target_countries`       | Target countries for the item (first entry is used)                   | `"US"`                                                      |
    | `store_country`          | Store country of the item                                             | `"US"`                                                      |

    ### Important optional fields

    Including these fields enables richer agentic discovery and checkout capabilities.

    | Field                   | Description                                                                                                                              | Example                                                    |
    | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
    | `is_eligible_search`    | Controls whether the product can be surfaced in search results.                                                                          | `"true"`                                                   |
    | `is_eligible_checkout`  | Controls whether the product can be directly purchased in agentic surfaces. `is_eligible_search` must be `true` for this to take effect. | `"true"`                                                   |
    | `item_group_title`      | Group product title                                                                                                                      | `"Classic T-Shirt"`                                        |
    | `mpn`                   | Manufacturer Part Number                                                                                                                 | `"MP12345"`                                                |
    | `gtin`                  | Global Trade Item Number                                                                                                                 | `"5901234123457"`                                          |
    | `sale_price`            | Discounted price                                                                                                                         | `"15.99 USD"`                                              |
    | `product_category`      | Category path                                                                                                                            | `"Apparel & Accessories > Clothing > Shirts & Tops"`       |
    | `additional_image_urls` | URLs to additional product images (comma-separated)                                                                                      | `"https://www.yourstore.com/images/tshirt-red-m-back.jpg"` |
    | `color`                 | Product color                                                                                                                            | `"red"`                                                    |
    | `size`                  | Variant size                                                                                                                             | `"medium"`                                                 |
    | `size_system`           | Size system (country code)                                                                                                               | `"US"`                                                     |
    | `gender`                | Gender target                                                                                                                            | `"male"`                                                   |
    | `variant_dict`          | Variant attributes map                                                                                                                   | `{"color": "Red", "size": "Medium"}`                       |

  </Accordion>

  <Accordion title="PayPal Enhanced Shopping Feed specification">
    The PayPal Enhanced Shopping Feed specification extends the Google Product Feed specification with a select set of additional fields for agentic commerce. This specification lets you prepare for AI-driven commerce with minimal changes to your existing Google feed. It requires two additional fields (`is_eligible_search` and `is_eligible_checkout`) and supports several additional optional fields.

    The PayPal Enhanced Shopping Feed specification uses the same fields as the Google Product Feed specification with the following additions.

    ### Additional required fields

    Use these two fields in addition to all Google Product Feed required fields.

    | Field                  | Description                                                                                                                              | Example  |
    | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | -------- |
    | `is_eligible_search`   | Controls whether the product can be surfaced in search results.                                                                          | `"true"` |
    | `is_eligible_checkout` | Controls whether the product can be directly purchased in agentic surfaces. `is_eligible_search` must be `true` for this to take effect. | `"true"` |

    ### Additional important optional fields

    These fields extend the Google Product Feed with agentic commerce and policy information.

    | Field                     | Description                                               | Example                           |
    | ------------------------- | --------------------------------------------------------- | --------------------------------- |
    | `item_group_title`        | Group product title                                       | `"Classic T-Shirt"`               |
    | `warning` / `warning_url` | Product disclaimer text or a URL resolving to HTTP `200`. | `"Contains lithium battery"`      |
    | `seller_privacy_policy`   | Seller privacy policy URL                                 | `"https://yourstore.com/privacy"` |
    | `seller_tos`              | Seller terms of service URL                               | `"https://yourstore.com/terms"`   |
    | `return_policy`           | Return policy URL                                         | `"https://yourstore.com/returns"` |

  </Accordion>
</AccordionGroup>

<Tip>For tips for setting up fields and other best practices, see [Best practices](#best-practices).</Tip>

## Handle product variants

You must list products with variations, such as different sizes or colors, as separate rows in your feed, using one row for each variant. Each variant row must include:

1. A unique `id` or `item_id` value for the variant.
2. The same `item_group_id` or `group_id` value to indicate the variants belong to the same product.
3. Variant-specific attributes, such as `color` and `size`.

The following example shows 3 variants of the same T-shirt:

```csv theme={null}
id,item_group_id,title,description,link,image_link,price,availability,color,size
shirt123-red-m,shirt123,"Classic T-Shirt - Red, Medium","Comfortable cotton t-shirt in red",https://yourstore.com/products/shirt-red-m,https://yourstore.com/images/shirt-red-m.jpg,"19.99 USD","in_stock",red,medium
shirt123-red-l,shirt123,"Classic T-Shirt - Red, Large","Comfortable cotton t-shirt in red",https://yourstore.com/products/shirt-red-l,https://yourstore.com/images/shirt-red-l.jpg,"19.99 USD","in_stock",red,large
shirt123-blue-m,shirt123,"Classic T-Shirt - Blue, Medium","Comfortable cotton t-shirt in blue",https://yourstore.com/products/shirt-blue-m,https://yourstore.com/images/shirt-blue-m.jpg,"19.99 USD","in_stock",blue,medium
```

<Warning>Before submitting, validate each variant row for correct data types and required fields. Rows with missing required fields or malformed values are skipped during ingestion without failing the entire feed.</Warning>

## Verify your feed

Before you upload your feed to Store Sync, confirm that it meets these requirements to ensure a smooth ingestion process and optimal product representation.

- All required fields for your chosen specification are present in every row.
- Each variant has a unique `id` or `item_id` and shares the correct `item_group_id` or `group_id` with its siblings.
- The feed file is UTF-8 encoded and includes a header row.
- The file does not exceed 4 GB. If it does, split it into multiple smaller files.
- All URLs (product links, image links, policy URLs) are accessible and return HTTP `200`.
- All image URLs resolve to a JPG or PNG file at a minimum resolution of 300×300 pixels.
- Price values follow the `"XX.XX USD"` format and the currency code matches your merchant profile.
- For the PayPal Enhanced Shopping Feed, `warning_url` values resolve to HTTP `200`.

## Best practices

Use these best practices to keep your product feed accurate, complete, and ready for reliable product discovery and checkout experiences.

### Feed quality and maintenance

Follow these recommendations to maintain a high feed quality over time and to reduce ingestion or catalog issues.

**Maintain data quality**

- Use only fields from your chosen feed specification.
- Complete all required fields for every product.
- Provide accurate, detailed product information and high-quality images.

**Update regularly**

- Update your catalog at least once daily.
- Keep availability status current.
- Remove discontinued products promptly.

**Validate before publishing**

- Validate your CSV format before uploading.
- Confirm all URLs are accessible and return HTTP `200`.
- Verify that all image links load correctly.
- For the `warning_url` field (PayPal Enhanced), ensure the URL resolves to HTTP `200` before submitting.

### Optimize fields for discoverability and performance

Follow these recommendations for the most common fields to ensure that your products are accurately represented and discoverable.

**Product identifier (`id` / `item_id`)**

- Must be unique within your catalog.
- Used for deduplication and product updates.
- Should identify the specific variant (for example, `shirt-red-medium`).

**Product title (`title`)**

- Should match the title on your product page.
- Include variant details such as color and size.
- Keep under 150 characters for optimal display.

**Product link (`link` / `url`)**

- Must be a valid, accessible URL.
- Should link directly to the specific variant page.

**Product images (`image_link` / `image_url`)**

- Must be a direct URL to a JPG or PNG image file.
- Image should clearly show the product.
- Minimum recommended resolution: 300×300 pixels.
- Additional images can be included in `additional_image_link` or `additional_image_urls`.

**Price (`price`, `sale_price`)**

- Format as `"XX.XX USD"` (for example, `"19.99 USD"`).
- The currency code must match your merchant profile.
- Include `sale_price` if a discounted price applies.

**Availability (`availability`)** must be one of the following exact values.

| Value          | Meaning                                     |
| -------------- | ------------------------------------------- |
| `in_stock`     | Ready to ship                               |
| `out_of_stock` | Currently unavailable                       |
| `preorder`     | Available for future shipping               |
| `backorder`    | Temporarily out of stock but can be ordered |

## Troubleshoot common issues

The following table describes common feed issues and how to fix them.

| Issue                                                                             | Cause                                                                 | Fix                                                                                                                                |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Feed file is rejected on upload.                                                  | The file exceeds 4 GB.                                                | Split the feed into multiple smaller files, each under 4 GB.                                                                       |
| Products are missing from the catalog after ingestion.                            | Rows are skipped due to missing required fields.                      | Ensure that all required fields for your specification are present and non-empty in every row.                                     |
| There are encoding errors during processing.                                      | The file is not UTF-8 encoded.                                        | Re-export your feed file with UTF-8 encoding. Most spreadsheet and export tools offer this as an option.                           |
| The image is not displayed for a product.                                         | Image URL is inaccessible or returns a non-`200` status.              | Verify that all image URLs are publicly accessible and return a `200` status. Ensure the URL points directly to a JPG or PNG file. |
| A product is not appearing in the search results (OpenAI ACP or PayPal Enhanced). | `is_eligible_search` is missing or set to `false`.                    | Set `is_eligible_search` to `"true"` for all products that you want to surface in search.                                          |
| Agentic checkout not available for a product.                                     | `is_eligible_checkout` is `true` but `is_eligible_search` is `false`. | `is_eligible_search` must be `"true"` for `is_eligible_checkout` to take effect. Update both fields.                               |
| Variants are not grouped correctly.                                               | `item_group_id` or `group_id` values are inconsistent across rows.    | Confirm that all variants of the same product share an identical `item_group_id` or `group_id` value.                              |
| A compressed archive is rejected.                                                 | The archive contains more than 1 data file.                           | Ensure that your `.gz` or `.zip` archive contains only a single CSV or TSV file.                                                   |

## Next steps

To enable AI-driven discovery and checkout across PayPal surfaces, connect your product feed to Store Sync. For details, see [Connect your product feed](/growth/agentic-commerce/store-sync/product-catalog/connect-product-feed/).
Your platform needs to provide essential data components to enable product discovery and merchant management in Store Sync. These components ensure that AI agents find and understand your inventory. They also facilitate seamless transactions across your entire network.
