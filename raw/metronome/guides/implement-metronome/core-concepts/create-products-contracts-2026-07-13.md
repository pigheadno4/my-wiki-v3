<!-- Source URL: https://docs.metronome.com/guides/implement-metronome/core-concepts/create-products-contracts.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create products

Products in Metronome represent your company’s individual product or service offerings. This is analogous to SKUs or items in an ERP system. For example, an infrastructure company’s products might include Reads, Writes, and Storage. For an AI company, the products might map to individual models.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/TrrblT2KR7zYyGbN/images/docs/get-started/core-concepts/products/products_diagram-f2766fbc59707cfcfc68ad9071d153ec.png?fit=max&auto=format&n=TrrblT2KR7zYyGbN&q=85&s=1d464ba9a88576fc7881821b9c019b2f" alt="a diagram showing where products fit into the metronome data model" width="3852" height="2864" data-path="images/docs/get-started/core-concepts/products/products_diagram-f2766fbc59707cfcfc68ad9071d153ec.png" />
</Frame>

Products defined in Metronome dictate:

* **How a customer gets charged**

  Products can either be usage-based, composite (derived from usage-based products), subscription-based, or fixed (for example, a platform fee).

* **Invoice line item display**

  Each product (or grouping of products) becomes a line item on generated invoices.

<Note>
  **PRODUCTS DON'T HAVE PRICES**

  Products determine *how* a customer is charged (for example, which billable metrics impact a charge), but they don't dictate  *how much* a customer pays. For usage-based, composite, and subscription products, prices are set on a [rate card](/guides/get-started/core-concepts/create-manage-rate-cards), which you can modify on a [contract](/guides/get-started/core-concepts/provision-contract). Prices on fixed products are set on a contract.
</Note>

## Product types​

Metronome supports four types of products:

* **Usage** , variably priced based on reported customer usage for the period. With usage products, you must [set up billable metrics beforehand](/guides/get-started/core-concepts/create-billable-metrics/). Associate each product to a single billable metric. The same billable metric can be associated with multiple products.
* **Composite** , percentage charge on a group of applicable products.
* **Subscription** , a recurring fee billed on a schedule. Use subscription fees for seat billing models, platform fees, or other recurring charges.
* **Fixed** , used to power scheduled charges, commits, and credits.

## Create products​

To define products in the [Metronome app](https://app.metronome.com/products), go to Offering -> Products -> click **+ Add new product** :

1. Give the product a meaningful name; this will appear on customer invoices.
2. Optionally enter any product tags.
3. Select the product type.
4. For usage-based products, select a billable metric.
5. (Optional) Add presentation and pricing group keys. Presentation and pricing group keys can only be added if they have been defined as group keys on the underlying billable metric. This field is only applicable for usage products.
6. (Optional) Add a quantity conversion. Multiply or divide by a conversion factor. This field is only applicable for usage products.
7. (Optional) Add rounding. Round up, down, or half up to the specified number of decimal places. This field is only applicable for usage products.
8. Click **Save**.

## Update products​

Within Metronome, you can edit products even when they're actively in use for customer billing. Changes to products are scheduled to take effect at a specified `Starting at` time, which you can define when changing a product. This date can be set in the future to schedule out product changes ahead of time. If set in the past, it will be retroactively applied at the time specified.

The following fields are available to edit:

* Name
* Tags
* Billable metric
* Quantity conversion
* Rounding
* Pricing and presentation group keys (only editable with the API)

You cannot change the product type. If you create a product with the wrong type, create a new product with the correct type and archive the original product.

To update products in the [Metronome app](https://app.metronome.com/products), go to Offering -> Products:

1. Click on the product to edit.
2. In the product details pane, click the overflow action -> **Edit product...**
3. In the resulting modal, set the **Starting at** value to specify when the product edits should take effect and update the desired product fields.
4. Click **Save**.

## Product tags​

Metronome supports adding one or more tags to products. Consistent use of tags helps you select products more easily, whether when creating a composite product or adding products to a commit or discount.

Product tags are also useful for adding your company's internal identifying information to your products in Metronome. For example, you may have internal product codes that you want to store in Metronome to maintain a consistent integration pattern across your systems.

## Group keys​

You can set two types of group keys on your new product: pricing group key and presentation group keys. To set a group key on a product, you must use a billable metric with the relevant group keys. You can use these group keys to encode your price book and customize the display of invoices in Metronome.

### Pricing group keys​

Many AI and infrastructure companies opt to price their products differently across dimensions like region and cloud provider. This approach aligns COGS and revenue, allowing for consistent margins across SKUs within a product catalog.

Pricing group keys allow you to set different prices for the same product based upon a set of variables you can choose during product creation.

For example, you have two products (P1 and P2), priced per hour of uptime. To support this pricing model, set the `region` and `cloud_provider` fields as pricing group keys on the products. The unique rates for each key-value permutation are then defined on the Metronome rate card:

|           | Region 1, AWS | Region 1, AZURE | Region 2, AWS | Region 2, AZURE |
| --------- | ------------- | --------------- | ------------- | --------------- |
| Product 1 | \$0.12/hr     | \$0.14/hr       | \$0.16/hr     | \$0.18/hr       |
| Product 2 | \$0.18/hr     | \$0.22/hr       | \$0.20/hr     | \$0.24/hr       |

In the above setup, you only need to create and manage two products while encoding eight distinct rates. Metronome doesn’t restrict the number of pricing group keys you can use when defining pricing. To learn more about configuring rates in Metronome, see [Manage rate cards](/guides/get-started/core-concepts/create-manage-rate-cards).

### Presentation group keys​

You may want to override the display of information on an invoice by grouping across certain properties. Do this with presentation group keys, which will group a set of line items together. Pricing and presentation group keys can be the same property if desired.

For example, you have two products, two regions, and two orgs. The pricing group key in this situation is `region`, while the presentation group key will be `org`. This allows you to split out `region` level usage by `org`. The resulting invoice contains:

|       | Region 1, Product 1 | Region 2, Product 1 | Region 1, Product 2 | Region 2, Product 2 |
| ----- | ------------------- | ------------------- | ------------------- | ------------------- |
| Org 1 | 15 units            | 10 units            | 10 units            | 5 units             |
| Org 2 | 10 units            | 0 units             | 6 units             | 3 units             |

Showing your customers usage at a granular level enables them to derive novel insights from their usage patterns.

<Note>
  **CONFIGURATION NOTE**

  Using multiple pricing and presentation group keys with many possible values for a given customer can increase latency when calling the Metronome API. If you anticipate the cardinality of these possible values reaching one thousand, contact your Metronome representative to discuss your configuration.
</Note>
