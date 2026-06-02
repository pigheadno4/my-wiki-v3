<!-- Source URL: https://docs.stripe.com/agentic-commerce/product-feed -->
<!-- Fetched: 2026-05-12 -->

# Catalog feed

Learn how to share structured product and inventory data with Stripe for AI agent discovery.

Use the product and inventory feed specification to share structured product and stock data with Stripe, and distribute your product feed to AI agents for search and shopping. Start with a full product feed submission, then send incremental inventory feed updates to keep stock levels and availability current.

## Product feed specification

Use the product feed specification to provide your complete structured product data (for example, titles, descriptions, identifiers, pricing, fulfillment, and media). Each row represents a product or variant.

1. Format your product data using the field reference in this document. Each field includes sample values, validation rules, and whether it’s required, recommended, or optional.
1. Send your product data securely using the [Stripe Product Catalog Import API](https://docs.stripe.com/api/v2/commerce/product-catalog-imports.md) in CSV format. Each row represents one product or variant. Submit a full initial feed to the sandbox endpoint to confirm your data parses correctly and meets all field requirements before you push to production.
1. Keep your data current and refresh your feed frequently. Update changes to product attributes, pricing, or fulfillment details when they occur to maintain customer trust and prevent stale listings. We validate and clean your data, index it into the Stripe product feed, and convert it to the format each agent requires.

### Feed processing mode

Product feed uploads support two processing modes: `upsert` (default) and `replace`.

Upsert mode treats each row as an insert or update for a product identified by its `id`.

- If the `id` doesn’t exist, we create the product.
- If the `id` already exists, we update the product with the values provided in that row.
- Products not included in the file remain unchanged.

Replace mode treats the uploaded file as the complete, authoritative product catalog.

- If the `id` doesn’t exist, we create the product.
- If the `id` already exists, we update the product with the values provided in that row.
- Products that exist in your catalog but aren’t present in the uploaded file are permanently deleted.
- Replace mode is only supported for the product feed.

Use replace mode when you want the uploaded file to fully define your catalog. Use upsert mode when you want to apply partial updates without affecting products you didn’t include.

### Deletion behavior

To remove a product or variant through the feed, include the optional `delete` column in your CSV. Set it to `true` for any products you want to delete. For products you want to keep, set it to `false` or leave the field blank.

When `delete=true`, Stripe only reads the `id` and `delete` columns for that row and ignores every other column.

### Discovery-only products

Products with `disable_checkout=true` are syndicated to AI agents for discovery, but they aren’t eligible for in-agent checkout. When an agent displays a discovery-only product, it redirects the user to the product’s `link` URL to complete the purchase on your website.

Discovery-only products follow the same feed processing rules as other products. Agents can index, search, and rank them. The only difference is that the purchase action redirects to your site instead of starting an in-agent checkout session.

To learn more about setting this field, see [Feed processing instructions](https://docs.stripe.com/agentic-commerce/product-feed.md#feed-processing-instructions).

## Product feed field reference

Review the full schema used by the Stripe product feed in the following sections. Each table lists data types, examples, and requirements.

### Basic product data

Provide the essential identifiers and descriptive text that uniquely define each product.

| Field       | Data type                                   | Requirement |
| ----------- | ------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id          | String (alphanumeric)Maximum 100 characters | Required    | Your product’s unique identifier. Use the product’s SKU where possible and keep the ID the same when updating your data.**Example: SKU12AB3456**                                                                                                                                         |
| title       | String (UTF-8 text)Maximum 150 characters   | Required    | Your product’s title. Accurately describe your product and match the title from your landing page. Avoid all-caps.**Example: Men’s Floral Polo Shirt**                                                                                                                                   |
| description | String (UTF-8 text)Maximum 5000 characters  | Required    | Your product’s description. Include only information about the product. Don’t include links to your store, sales information, details about competitors, other products, or accessories. Plain text only.**Example: Bring a burst of fun to your golf game with this Men’s Floral Polo** |
| link        | URL (RFC 1738)                              | Required    | Your product’s landing page. Use your verified domain name, starting with `https` (preferred) or `http`. Must resolve with `HTTP 200` (no broken links).**Example: https://example.com/product/SKU12AB3456**                                                                             |

### Product identifiers

Use these globally recognized identifiers to help differentiate your products for search and matching.

| Field | Data type                        | Requirement                                                            |
| ----- | -------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| brand | String                           | Required for all excluding movies, books, and musical recording brands | Your product’s brand name. Provide the brand name of the product generally recognized by consumers. Maximum 70 characters.**Example: Stripe** |
| gtin  | String (Numeric GTIN, UPC, ISBN) | Recommended                                                            | Your product’s global trade item number (GTIN). Maximum 50 characters. Exclude dashes and spaces.**Example: 3234567890126**                   |
| mpn   | String (alphanumeric)            | Required if GTIN is missing                                            | Your product’s manufacturer part number (MPN). Only submit MPNs assigned by a manufacturer. Maximum 70 characters.**Example: STR12345**       |

### Media

Provide visual and optional rich media to represent the product accurately.

| Field                 | Data type            | Requirement |
| --------------------- | -------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| image_link            | URL (RFC 1738)       | Required    | The URL of your product’s main image. Use JPEG or PNG format. Must start with `http` or `https` (`https` preferred). Must be publicly accessible. Recommended minimum size: 800 × 800 px. Avoid watermarks, text overlays, or promotional graphics.**Example: https://example.com/image1.jpg** |
| additional_image_link | URL array (RFC 1738) | Optional    | The URLs of additional images for your product. Follow the same requirements as `image_link`. Maximum of 10 images supported. Use multiple angles, packaging, or in-context views.                                                                                                             |

- To submit one image, submit the (encoded) URL: **https://www.example.com/image2.jpg**.
- To submit more than one image (up to 10), separate each URL with a comma (for example, **https://www.example.com/image2.jpg,https://www.example.com/image3.jpg**). Encode any commas (as `%2C`) within the URL, but don’t encode the comma that separates each image URL: **https://www.example.com/image2%2C3.jpg,https://www.example.com/image2%2C4.jpg**.**Example: https://example.com/image2.jpg,…** |
  | video_link | URL (RFC 1738) | Optional | A product video that shows your product in use or during unboxing. Must be publicly accessible (for example, YouTube, Vimeo, or a direct MP4 link). Recommended formats: MP4, MOV, or WebM. Recommended duration: 15–60 seconds. Include audio only if it’s relevant to the product (for example, a sound demo). Make sure you show the same product as in the main image.**Example: https://youtu.be/12345** |
  | model_3d_link | URL (RFC 1738) | Optional | An additional link that shows a 3D model of your product. Preferred formats: GLB or GLTF. Must be publicly accessible. Keep file size under 20 MB for optimal loading. Make sure the model accurately represents the product’s physical form and color.**Example: https://www.example.com/products/xyz.glb** |

### Item information

Describe physical characteristics and classification for accurate filtering and taxonomy placement.

| Field     | Data type                           | Requirement                                    |
| --------- | ----------------------------------- | ---------------------------------------------- | -------------------------------------------------- |
| condition | Enum (`new`, `refurbished`, `used`) | Required if product condition differs from new | The condition of your product at the time of sale. |

- `new`: Brand-new item in original, unopened packaging.
- `refurbished`: Professionally restored to working order, includes a warranty, and the original packaging might be missing.
- `used`: Previously used, with original packaging opened or missing.**Example: new** |
  | google_product_category | StringValue from the Google product taxonomy. The numerical category ID, or the full path of the category. | Recommended | Predefined Google product category. Include only the most relevant category. Include either the full category path or the numerical category ID, but not both. Use the category ID when possible.**Example: 2271** or **Apparel & Accessories > Clothing > Dresses** |
  | product_category | String (Category taxonomy) | Required if `google_product_category` is missing | Product category that you define for your product. Use `>` as a separator. Include the full category. Exclude dashes and spaces.**Example: Apparel & Accessories > Clothing > Outerwear** |
  | age_group | Enum (`newborn`, `infant`, `toddler`, `kids`, `adult`) | Optional | The demographic that your product is intended for.
- `newborn`: 0 through 3 months old.
- `infant`: 3 through 12 months old.
- `toddler`: 1 through 5 years old.
- `kids`: 5 through 13 years old.
- `adult`: Teens or older.**Example: infant** |
  | material | String | Required if it’s relevant for distinguishing different products in a set of variants | Your product’s primary fabric or material. Maximum 100 characters.**Example: leather** |
  | length | Number and unit (`cm` and `in`) | Optional | Your product’s length. Use the same unit of measurement for each dimension attribute (including `length`, `width`, and `height`). Decimal values are supported.**Example: 20 in** |
  | width | Number and unit (`cm` and `in`) | Optional | Your product’s width. Use the same unit of measurement for each dimension attribute (including `length`, `width`, and `height`). Decimal values are supported.**Example: 20 in** |
  | height | Number and unit (`cm` and `in`) | Optional | Your product’s height. Use the same unit of measurement for each dimension attribute (including `length`, `width`, and `height`). Decimal values are supported.**Example: 20 in** |
  | weight | Number and unit (`lb`, `oz`, `g`, `kg`) | Optional | Your product’s weight. Use the actual assembled product weight for this attribute. Decimal values are supported.**Example: 2.5 lb** |

### Variants

Define variant relationships, such as color and size, so that related SKUs group under one parent. If you submit variants, include the same `item_group_id` for every variant.

| Field            | Data type                         | Requirement                |
| ---------------- | --------------------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| item_group_id    | String                            | Required if variants exist | ID for a group of products that come in different variants. Use a unique value for each group of variants. Use the parent SKU where possible. Keep the value the same when you update your product data. Maximum 70 characters. Use the same set of variant attributes for all products that share the same `item_group_id`. For example, if a dress is available in two colors and two sizes, each variant must include values for both color and size.**Example: Shoe1234** |
| item_group_title | String (UTF-8 text)               | Optional                   | Your product group’s title. Use a clear, human-readable name that represents the group of related variants (for example, “Men’s Running Shoes”). Maximum 150 characters. Avoid all caps.**Example: Shoes**                                                                                                                                                                                                                                                                    |
| color            | String                            | Recommended (apparel)      | Your product’s color. If your product features multiple colors, list the primary color. Recommended length: 40 characters or fewer. Maximum length: 100 characters.**Example: Black**                                                                                                                                                                                                                                                                                         |
| size             | String                            | Recommended (apparel)      | Your product’s size. Maximum 20 characters.**Example: 10**                                                                                                                                                                                                                                                                                                                                                                                                                    |
| size_system      | Country code (ISO 3166)           | Recommended (apparel)      | Size system. Two-letter country code.**Example: US**                                                                                                                                                                                                                                                                                                                                                                                                                          |
| gender           | Enum (`male`, `female`, `unisex`) | Recommended (apparel)      | Your product’s intended gender.**Example: male**                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Custom variant options

Define non-standard characteristics for your product variants that aren’t already included in the Variants section using name and value pairs (for example, “Material/Oak” or “Pattern/Floral”).

| Field                             | Data type           | Requirement |
| --------------------------------- | ------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| custom*variant_option_name*{1-3}  | String (UTF-8 text) | Optional    | Defines a maximum of three custom product variant options. Number each column in the CSV 1-3: `custom_variant_option_name_1`, `custom_variant_option_name_2`, `custom_variant_option_name_3`. Each variant option name maps to the value with the same number. For example, `custom_variant_option_name_1` maps to `custom_variant_option_value_1`.**Example: Material**                                        |
| custom*variant_option_value*{1-3} | String (UTF-8 text) | Optional    | Sets custom product variant values to the variants defined by custom variant option names. Number each column in the CSV 1-3: `custom_variant_option_value_1`, `custom_variant_option_value_2`, `custom_variant_option_value_3`. Each variant option value maps to the name with the same number. For example, `custom_variant_option_value_1` is the value for `custom_variant_option_name_1`.**Example: Oak** |

### Availability and inventory

Provide live stock status and quantities to maintain purchase accuracy.

| Field                 | Data type                                                  | Requirement                                           |
| --------------------- | ---------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------ |
| availability          | Enum (`in_stock`, `out_of_stock`, `preorder`, `backorder`) | Required for all products                             | Your product’s availability.**Example: in_stock**                                    |
| availability_date     | Date (ISO 8601)                                            | Required if product availability is set to `preorder` | The date a preordered product becomes available for delivery.**Example: 2026-02-24** |
| expiration_date       | Date (ISO 8601)                                            | Optional                                              | The date your product stops showing.**Example: 2026-12-31**                          |
| inventory_not_tracked | Boolean (`true` or `false`)                                | Optional                                              | Specifies whether your product’s inventory is tracked.                               |

- `true`: Inventory isn’t tracked (for example, digital goods or made-to-order).
- `inventory_quantity` must be blank.
- `false`: Inventory is tracked and `inventory_quantity` is required.**Example: false** |
  | inventory_quantity | Integer (Non-negative integer) | Required if `inventory_not_tracked` is `false`. Leave blank if `true`. | Sellable units available for this item. Leave blank if `inventory_not_tracked` is `true`.**Example: 100** |

### Price and promotions

Specify pricing information for display and promotional logic.

| Field                     | Data type                                                                                                                           | Requirement                                                                                                                    |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| price                     | Number and currency (ISO 4217)                                                                                                      | Required for all products                                                                                                      | Your product’s price.**Example: 15.00 USD**                                                                                                                                                                                                                                                                                                                                              |
| sale_price                | Number and currency (ISO 4217)                                                                                                      | Optional                                                                                                                       | Discounted price.**Example: 12.99 USD**                                                                                                                                                                                                                                                                                                                                                  |
| sale_price_effective_date | Date (ISO 8601)                                                                                                                     | Required if you provided `sale_price`                                                                                          | Sale window. Separate the start date and end date with `/`.**Example: 2025-12-01/2025-12-15**                                                                                                                                                                                                                                                                                            |
| stripe_product_tax_code   | String (Stripe Product Tax Code (PTC))                                                                                              | Required if using Stripe Tax for tax calculation                                                                               | Use Stripe Product Tax Codes to classify your product for tax calculation. These codes help Stripe determine the correct tax rate based on product type and jurisdiction.**Example: txcd_99999999**                                                                                                                                                                                      |
| third_party_tax_code      | String`provider:tax_code`Supported provider: `anrok`Maximum 120 characters                                                          | Optional. Required if `stripe_product_tax_code` isn’t provided and you use [Anrok](https://www.anrok.com) for tax calculation. | Use this field to classify your product for tax calculation with [Anrok](https://www.anrok.com). Format the value as `<provider>:<tax_code>` with a lowercase provider name. The only currently supported provider for agentic commerce is `anrok`. Use this field instead of `stripe_product_tax_code` when you classify products specifically for Anrok.**Example: anrok:prod_abc123** |
| tax_behavior              | Enum (`inclusive` or `exclusive`)                                                                                                   | Optional                                                                                                                       | Specifies whether your product’s price includes applicable taxes (inclusive) or excludes them (exclusive). If you omit this field, the default value is `exclusive`.**Example: exclusive**                                                                                                                                                                                               |
| applicable_fees           | String`country:region:fee_label:fee_amount`: Put each option as a colon-delimited value, and separate multiple entries with commas. | Optional (required where regulatory or regional fees apply)                                                                    | Use this field to specify per-unit fees and surcharges that apply based on product type and region. These fees aren’t included in the base product price. Use them as separate line items at checkout and in reporting. Format each fee as a colon-delimited value:                                                                                                                      |

- `country` (Required): ISO 3166-1 alpha-2 country code (for example, US or DE).
- `region` (Required): Region, state, territory, or prefecture (for example, CA). Use `ALL` to apply to all regions or provinces within the specified country.
- `fee_label` (Required): Human-readable name for the fee (for example, recycling fee, bottle deposit, or eco charge). Don’t use colons in the name.
- `fee_amount` (Required): Fixed per-unit fee using a period as the decimal separator and ISO 4217 currency code (for example, 5.00 USD).**Example: US:CA:Recycling Fee:0.25 USD,DE:ALL:Bottle Deposit:0.10 EUR** |

### Fulfillment

Provide shipping options, rates, and estimated delivery times.

| Field    | Data type                                                                                                                                       | Requirement                                                         |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| shipping | String`country:delivery_area:service:speed_range:price`: Put each option as a colon-delimited value, and separate multiple entries with commas. | Required if the product is shippable (for example, a physical good) | Your product’s shipping cost, shipping speeds, and the locations your product ships to. Format each shipping option as a colon-delimited value: |

- `country` (Required): ISO 3166-1 alpha-2 country code indicating the country the product can be delivered to (for example, US or DE).
- `delivery_area` (Required): One of the following values that defines where you can deliver the product: - `region`: Region, state, territory, or prefecture using the ISO 3166-2 subdivision code without the country prefix (for example, `VA` or `NY`). Use `ALL` to apply to every region or province in the country. - `postal_code`: Postal code or postal code range (currently supported only for the US). Allowed formats: - Single code: `94012` - Range: `73114-74547` - Wildcard at the end: `94*` - Multiple wildcard ranges: `94*-95*` - `service` (Required): Human-readable name for the service (for example, standard or express shipping). - `speed_range` (Optional): Minimum and maximum number of days needed for shipping (for example, `3-5`). - `price` (Required): Fixed shipping cost using a period as the decimal separator and ISO 4217 currency code (for example, `3.00 USD`).**Example (Region): US:ALL:Standard Shipping:3-5:0.00 USD,US:ALL:Expedited Shipping:1-2:12.99 USD\*\***Example (Postal code): US:94012:Standard Shipping:3-5:0.00 USD,US:73114-74547:Expedited Shipping:1-2:9.99 USD,US:94\*:Expedited Shipping:1-2:9.99 USD,US:94\*-95\*:Standard Shipping:2-5:0.00 USD\*\* |
  | shipping_cost_basis | Enum (`per_order`, `per_item`) | Optional | Specifies how the shipping cost defined in the `shipping` field applies when customers buy multiple units of the same SKU. If you omit this setting, the default behavior is `per_order`.
- `per_order`: Charge the shipping price once per order for the matching shipping service, regardless of quantity.
- `per_item`: Charge the shipping price per unit of this SKU (that is, multiply by the quantity purchased).**Example: per_item** |
  | free_shipping_threshold | String`country:region:service:price_threshold`: Put each option as a colon-delimited value, and separate multiple entries with commas. | Optional | Defines an order-level free shipping rule. When the order merchandise subtotal meets or exceeds the specified threshold, the shipping cost for the matching shipping service is `0.00`. Format each shipping option as a colon-delimited value:
- `country` (Required): ISO 3166-1 alpha-2 country code indicating the country the product can be delivered to (for example, US or DE).
- `region` (Required): Region, state, territory, or prefecture using the ISO 3166-2 subdivision code without the country prefix (for example, VA or NY). Use `ALL` to apply to all regions or provinces within the specified country.
- `service` (Required): Shipping service name. It must match a service defined in the `shipping` field (for example, standard or express shipping).
- `price_threshold` (Required): Order merchandise subtotal after item-level discounts and before tax and shipping, expressed as amount and currency. Use a period as the decimal separator and an ISO 4217 currency code (for example, `50.00 USD`).**Example: US:ALL:Standard Shipping:50.00 USD,US:ALL:Expedited Shipping:100.00 USD** |

### Performance and review signals

Share performance and review signals to help AI agents and ranking systems identify high-quality, trusted products.

- These fields are optional but recommended. They improve discovery, ranking, and personalization across agentic interfaces.
- Provide only aggregated metrics and exclude any user-level data or personally identifiable information.
- Update these metrics periodically (for example, weekly) to maintain accuracy.

| Field                 | Data type                                  | Requirement                                          |
| --------------------- | ------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| popularity_score      | Number (0–5 scale)                         | Recommended                                          | Aggregate popularity indicator for this product or variant. Use a consistent 0 through 5 scale across your feed (0 is the lowest, 5 is the highest). Derive this from signals such as views, add-to-cart events, conversions, or sales rank. Use a consistent aggregation window (for example, the last 90 days) to keep this value current.**Example: 4.7** |
| return_rate           | Number0–100 (don’t include the `%` symbol) | Recommended                                          | Percentage of units returned for this product or variant. Express as a numeric percentage between 0 and 100 (for example, use `2.0` for 2%). Use a consistent aggregation window (for example, the last 90 days).**Example: 2.0**                                                                                                                            |
| product_review_count  | Integer (Non-negative integer)             | Recommended                                          | Total number of reviews associated with this product or variant. Match the population used to compute `product_review_rating`. Use `0` if no reviews exist. Reflect verified purchase reviews when possible.**Example: 124**                                                                                                                                 |
| product_review_rating | Number (1–5 scale)                         | Required if `product_review_count` is greater than 0 | Average review rating for this product or variant. Use a consistent 1 through 5 scale across feed (1 is the lowest, 5 is the highest). This value must correspond to the same dataset as `product_review_count`. Leave this field blank if `product_review_count` is `0`.**Example: 4.3**                                                                    |

### Product relationships

Specify product associations such as upsells, cross-sells, and related products for discovery and recommendations.

| Field            | Data type                                                                                                                   | Requirement |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------ |
| related_products | String`relationship_type:target_id`: Put each option as a colon-delimited value, and separate multiple entries with commas. | Optional    | Defines product associations for this item. Format each relationship as a colon-delimited value: |

- `relationship_type` (Required): Must be one of `upsell`, `cross_sell`, `substitute`, or `accessory`.
- `target_id` (Required): The product’s unique identifier. If the target doesn’t match existing `id` in the ingested product feed data, we remove the relationship before syndicating to the agent.
- No self-references: `target_id` can’t equal the current product.
- No duplicate `target_id` values in this row: You can’t specify multiple relationship types (for example, you can’t specify both `upsell` and `cross_sell` from this product to the same target product in one row).
- Maximum 10 product relationships per product row. **Example: upsell:SKU12AB3457,cross_sell:SKU12AB3458,accessory:SKU12AB3459** |

### Compliance

Include regulatory warnings, disclaimers, or age restrictions. These fields help you meet legal obligations and protect consumers.

| Field           | Data type                                                                                                                                                                                                       | Requirement                                                  |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| product_warning | String`type:message`: Put each option as a colon-delimited value, and separate multiple entries with commas.Supported types: `legal_disclaimer`, `safety_warning`, `prop_65`Maximum 1000 characters per message | Optional (required where regulatory or legal warnings apply) | Specifies one or more warnings that apply to this product or variant. This field is mandatory for items with regulatory warning requirements (for example, California Proposition 65). You’re responsible for compliance with all applicable laws, including product warning requirements. These warnings are displayed on the agent checkout screen when you provide them. Format each warning as a colon-delimited value: |

- `type` (Required): Warning type. Supported values: `legal_disclaimer`, `safety_warning`, `prop_65`.
- `message` (Required): Warning text shown to users.**Example: prop_65: This product can expose you to chemicals including lead.** |
  | age_restriction | Integer (Non-negative integer) | Optional | Minimum age required to purchase this product.**Example: 21** |

### Custom labels

Use custom labels to tag and group products for segmentation, filtering, and downstream integrations. These fields don’t appear to end users and don’t affect product display, pricing, or fulfillment.

| Field              | Data type                                 | Requirement |
| ------------------ | ----------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| custom*label*{0-4} | String (UTF-8 text)Maximum 100 characters | Optional    | Use up to 5 custom labels for internal purposes only. Each field accepts a single string value. Supported fields are `custom_label_0`, `custom_label_1`, `custom_label_2`, `custom_label_3`, and `custom_label_4`. Don’t use these fields to encode structured product attributes already covered by other fields, such as price, availability, or brand.**Example: Seasonal** |

### Feed processing instructions

Define operational fields that control how the system processes each row in the feed.

| Field            | Data type                   | Requirement |
| ---------------- | --------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| delete           | Boolean (`true` or `false`) | Optional    | Mark the product or variant for permanent removal. When `true`, we remove the product identified by `id` and ignore all other columns in that row. When omitted or `false`, we process the row as an _upsert_ (A combined operation that updates an existing record if it exists or inserts it if it doesn’t).**Example: true**                                                                           |
| disable_checkout | Boolean (`true` or `false`) | Optional    | Exclude this product from in-agent checkout flows. When `true`, the product is still syndicated to AI agents for discovery, but agents direct users to the product’s `link` URL to complete the purchase instead of starting an in-agent checkout session. When you omit this field or set it to `false`, checkout remains enabled if the business has completed checkout configuration.**Example: true** |

## Use the inventory feed specification

Use the inventory feed to refresh product availability and stock quantities without resubmitting your full product feed. Send frequent updates from your warehouse, point of sale, or fulfillment systems so your products reflect accurate in-stock status across agentic interfaces.

1. **Keep your product feed in sync**: The `id` values in your inventory file must already exist in the main product feed.
1. **Send frequent inventory files**: Push updates through the [Stripe Product Catalog Import API](https://docs.stripe.com/api/v2/commerce/product-catalog-imports.md) in CSV format.
1. **Send partial updates**: Include only changed SKUs—missing SKUs retain their last known inventory state.

## Inventory feed field reference

Use the following reference to format your inventory feed fields.

### Inventory feed fields

Provide live stock status and quantities to maintain purchase accuracy.

| Field              | Data type                                                  | Requirement                                           |
| ------------------ | ---------------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| id                 | String (alphanumeric)                                      | Required                                              | Must match the `id` in your primary product feed. This value is the key identifier.**Example: SKU12AB3456** |
| availability       | Enum (`in_stock`, `out_of_stock`, `preorder`, `backorder`) | Required for all products                             | Your product’s availability.**Example: in_stock**                                                           |
| availability_date  | Date (ISO 8601)                                            | Required if product availability is set to `preorder` | The date a preordered product becomes available for delivery.**Example: 2026-02-24**                        |
| inventory_quantity | Integer (Non-negative integer)                             | Required for all products                             | Sellable units.**Example: 100**                                                                             |

## Use the price feed specification

Use the price feed to refresh pricing information for display and promotions without resubmitting your full product feed.

1. **Keep your product feed in sync**: The `id` values in your price file must already exist in the main product feed.
1. **Send frequent price files**: Push updates through the [Stripe Product Catalog Import API](https://docs.stripe.com/api/v2/commerce/product-catalog-imports.md) in CSV format.
1. **Send partial updates**: Include only changed SKUs—missing SKUs retain their last known pricing information.

## Price feed field reference

Use the following reference to format your price feed fields.

### Price feed fields

Specify pricing information for display and promotional logic.

| Field                     | Data type                      | Requirement                           |
| ------------------------- | ------------------------------ | ------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| id                        | String (alphanumeric)          | Required                              | Must match the `id` in your primary product feed. This value is the key identifier.**Example: SKU12AB3456** |
| price                     | Number and currency (ISO 4217) | Required for all products             | Your product’s price.**Example: 15.00 USD**                                                                 |
| sale_price                | Number and currency (ISO 4217) | Optional                              | Discounted price.**Example: 12.99 USD**                                                                     |
| sale_price_effective_date | Date (ISO 8601)                | Required if you provided `sale_price` | Sale window. Separate the start date and end date with `/`.**Example: 2025-12-01/2025-12-15**               |

## Use the promotion feed specification

Use the promotion feed to provide your active and scheduled promotions, including discount codes, percentage-off deals, fixed-amount discounts, and free shipping offers. Each row represents a single promotion. The promotion feed works alongside your product feed and references products by `id` or `item_group_id` from your catalog.

1. **Keep your product feed in sync**: Product IDs and item group IDs in your promotion file must match `id` or `item_group_id` values in the main product feed.
1. **Send frequent promotion files**: Push updates through the [Stripe Product Catalog Import API](https://docs.stripe.com/api/v2/commerce/product-catalog-imports.md) in CSV format.
1. **Send partial updates**: Include only changed promotions. If you omit promotions, they retain their last known promotion information.

## Promotion feed field reference

Use the following reference to format your promotion feed fields.

### Basic promotion data

Provide the essential identifiers and dates that define each promotion.

| Field         | Data type                                   | Requirement |
| ------------- | ------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| promotion_id  | String (alphanumeric)Maximum 100 characters | Required    | Your promotion’s unique identifier. Keep the ID the same when updating your data.**Example: PROMO_SPRING2026**                                                                                                                          |
| title         | String (UTF-8 text)Maximum 150 characters   | Required    | Human-readable promotion title. Customers might see this during checkout.**Example: Spring Sale - 20% Off**                                                                                                                             |
| link          | URL (RFC 1738)                              | Optional    | Landing page URL for the promotion. Start with `http` or `https` (`https` preferred). Must resolve with `HTTP 200` (no broken links).**Example: https://example.com/promo**                                                             |
| active_period | DateTime (ISO 8601)                         | Required    | Start and end dates for the promotion. Separate the start date and end date with `/`. Both values must be full ISO 8601 timestamps including time and timezone (UTC recommended).**Example: 2026-05-01T00:00:00Z/2026-12-15T23:59:59Z** |

### Discount configuration

Specify the type and value of the discount the promotion provides.

| Field        | Data type                                           | Requirement |
| ------------ | --------------------------------------------------- | ----------- | --------------------------------------------- |
| benefit_type | Enum (`percent_off`, `amount_off`, `free_shipping`) | Required    | The type of discount this promotion provides. |

- `percent_off`: The promotion offers a percentage discount. Include the discount percentage in the `percent_off` field.
- `amount_off`: The promotion offers a fixed discount amount. Include the discount amount in the `amount_off` field.
- `free_shipping`: The promotion offers free shipping. Include a valid redemption code in the `promotion_code` field.**Example: percent_off** |
  | percent_off | Integer (0–100) | Required if `benefit_type` is `percent_off` | The percentage discount offered by the promotion.**Example: 20** |
  | amount_off | Number and currency (ISO 4217) | Required if `benefit_type` is `amount_off` | The fixed discount amount offered by the promotion.**Example: 10.00 USD** |
  | minimum_order_amount | Number and currency (ISO 4217) | Optional | The minimum order subtotal required for the promotion to apply. The subtotal is calculated before tax, shipping, and discounts. Applicable to all promotion types.**Example: 50.00 USD** |

### Product targeting

Specify which products the promotion applies to.

| Field            | Data type                                  | Requirement |
| ---------------- | ------------------------------------------ | ----------- | ------------------------------------------------------------------------------------- |
| target_selection | Enum (`all_products`, `specific_products`) | Required    | Specifies whether the promotion applies to all products or only to specific products. |

- `all_products`: The promotion applies to all products in the catalog. Leave `target_ids`, `target_item_group_ids`, `excluded_ids`, and `excluded_item_group_ids` empty.
- `specific_products`: The promotion applies to a subset of products. Specify at least one of `target_ids`, `target_item_group_ids`, `excluded_ids`, or `excluded_item_group_ids`. Use `target_ids` and `target_item_group_ids` to define the included set and `excluded_ids` and `excluded_item_group_ids` to remove products from that set.**Example: all_products** |
  | target_ids | String (comma-separated product SKUs) | Conditionally required if `target_selection` is `specific_products` | Limits the promotion to specific product SKUs. Values must match the `id` attribute in the product feed.**Example: SKU123,SKU456** |
  | target_item_group_ids | String (comma-separated item group IDs) | Conditionally required if `target_selection` is `specific_products` | Limits the promotion to specific item groups. All variants within a group qualify. Values must match the `item_group_id` attribute in the product feed.**Example: POLO123** |
  | excluded_ids | String (comma-separated product SKUs) | Conditionally required if `target_selection` is `specific_products` | Excludes specific product SKUs from the promotion after inclusion logic is applied. Values must match the `id` attribute in the product feed. If a product appears in both `target_ids` and `excluded_ids`, it is excluded.**Example: SKU222,SKU333** |
  | excluded_item_group_ids | String (comma-separated item group IDs) | Conditionally required if `target_selection` is `specific_products` | Excludes specific item groups from the promotion after inclusion logic is applied. Values must match the `item_group_id` attribute in the product feed. If an item group appears in both `target_item_group_ids` and `excluded_item_group_ids`, it is excluded.**Example: POLO456** |

### Redemption

Configure how customers redeem the promotion.

| Field            | Data type                            | Requirement |
| ---------------- | ------------------------------------ | ----------- | ------------------------------------------------------------------- |
| application_type | Enum (`automatic`, `promotion_code`) | Required    | Indicates whether a promotion code is required to redeem the offer. |

- `automatic`: The offer is automatically applied at checkout if the order qualifies.
- `promotion_code`: The offer is applied when a customer enters a promo code at checkout. Include a valid redemption code in the `promotion_code` field.**Example: automatic** |
  | promotion*code | String (case-insensitive)Maximum 20 charactersAllowed characters: letters, numbers, hyphens (`-`), underscores (`*`) | Required if `application_type`is`promotion_code`| The code customers use to redeem the promotion. All`free_shipping` promotions must include a valid redemption code.**Example: SPRING20** |

### Feed processing instructions

Define operational fields that control how the system processes each row in the feed.

| Field  | Data type                   | Requirement |
| ------ | --------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| delete | Boolean (`true` or `false`) | Optional    | Mark the promotion for permanent removal. When `true`, we remove the promotion identified by `promotion_id` and ignore all other columns in that row.**Example: true** |
