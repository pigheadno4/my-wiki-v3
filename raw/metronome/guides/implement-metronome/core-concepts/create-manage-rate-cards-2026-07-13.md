<!-- Source URL: https://docs.metronome.com/guides/implement-metronome/core-concepts/create-manage-rate-cards.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create and manage rate cards

Rate cards provide a centralized vehicle to store and update pricing information for your products in Metronome. This includes the ability to encode today’s standard rates and schedule changes in the future. Given its role as the source of truth for pricing, all Metronome contracts are built on top of rate cards. Aggregating this information in one entity enables you to quickly implement pricing changes for all customers whose contracts reference it.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/TrrblT2KR7zYyGbN/images/docs/get-started/core-concepts/rate-cards/rate_cards_diagram-120a8ab65c3f51bfd6cc7d81694c3335.png?fit=max&auto=format&n=TrrblT2KR7zYyGbN&q=85&s=9a3d2fb51d7cc2889496f0c8d64c4d32" alt="Diagram showing where rate cards fit in the Metronome data model" width="5400" height="2864" data-path="images/docs/get-started/core-concepts/rate-cards/rate_cards_diagram-120a8ab65c3f51bfd6cc7d81694c3335.png" />
</Frame>

## How rate cards work​

Rate cards represent your standard pricing rates.

Beyond those standard rates, overrides on the rate card enable you to configure flexible discounting by any custom dimension, such as region, service type, and model type.

For example, AI research companies commonly use a pricing pattern to charge by token used in queries to individual LLM models. These companies can charge different rates for different types of customers, like PayGo or enterprise. Additionally, they might offer premium models to enterprise customers and limit PayGo to legacy models. In Metronome, they could design these two options by creating two distinct rate cards or by managing a single rate card that represents the standard listing with configured overrides for enterprise contracts.

## Prerequisites​

Before setting up a rate card, you need products in Metronome.

Products serve as the base entity to price on. Given this dependency, create your [products](/guides/get-started/core-concepts/create-products-contracts) in Metronome before moving on to pricing.

## Create a rate card​

You can create a rate card with the Metronome app or API.

### Create a rate card via UI​

To create a rate card in the [Metronome app](https://app.metronome.com/products), go to Offering → Rate cards → click **Add new rate card** :

1. Give the rate card an internally meaningful **Name** (for example, *Enterprise Price Book - 2024*).

2. Add an optional **Description** (for example, *Standard pricing from October 2024 – July 2025*).

3. Optionally **Add aliases**. Aliases can be used in place of the Metronome-generated rate card IDs when provisioning contracts via API.

<Tip>
  **TIP**

  Rate card aliases help maintain the integrity of API integrations while switching the underlying rate card associated with the integration. This allows for more flexibility to overhaul your pricing and packaging while maintaining your integration infrastructure.
</Tip>

4. Select the products to add to the rate card.

5. Choose the rate card's fiat currency. Each rate card is associated with one fiat currency. The default is USD.

6. Define the rates, default entitlements, and effective dates for each product.

7. Review the rate card and click **Save** to create the completed card.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/C_lGxKgdkdHt6xoX/images/docs/get-started/core-concepts/rate-cards/sample-rate-card-3a41126b2e411e72ddbf6d41b94a7cf5.png?fit=max&auto=format&n=C_lGxKgdkdHt6xoX&q=85&s=31f8bd0484e4c0414b38361a46036318" alt="Rate card example" width="2334" height="1026" data-path="images/docs/get-started/core-concepts/rate-cards/sample-rate-card-3a41126b2e411e72ddbf6d41b94a7cf5.png" />
</Frame>

### Create a rate card via API​

To create a rate card with the API, make a POST request to the [/contract-pricing/rate-cards/create](/api-reference/rate-cards/create-a-rate-card) endpoint:

This example shows how to generate a rate card that has two different aliases with start and end dates.

```bash theme={null}
curl https://api.metronome.com/v1/contract-pricing/rate-cards/create \  
  -H "Authorization: Bearer <TOKEN>" \  
  -H "Content-Type: application/json" \  
  -d '{  
  "name": "Rate Card Sample",  
  "description": "Rate Card Sample",  
  "aliases": [  
    {  
      "name": "Sample Alias - Customer Workflow 1",  
      "starting_at": "2024-01-01T00:00:00.000Z",  
      "ending_before": "2025-01-01T00:00:00.000Z"  
    },  
    {  
      "name": "Sample Alias - Custom Workflow 2",  
      "starting_at": "2025-01-01T00:00:00.000Z",  
      "ending_before": "2026-01-01T00:00:00.000Z"  
    }  
  ]  
}'
```

To add rates with the API, make a POST request to the [/contract-pricing/rate-cards/addRates](/api-reference/rate-cards/add-a-rate) endpoint.

This example shows how to create two rates for usage-based products that leverage pricing group keys. These rates make use of the same product, but show pricing variation between regions.

```bash theme={null}
 curl https://api.metronome.com/v1/contract-pricing/rate-cards/addRates \  
  -H "Authorization: Bearer <TOKEN>" \  
  -H "Content-Type: application/json" \  
  -d '{  
  "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",  
  "rates": [  
    {  
      "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",  
      "starting_at": "2024-01-01T00:00:00.000Z",  
      "entitled": true,  
      "rate_type": "FLAT",  
      "price": 100,  
      "pricing_group_values": {  
        "region": "us-west-2",  
        "cloud": "aws"  
      }  
    },  
    {  
      "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",  
      "starting_at": "2024-01-01T00:00:00.000Z",  
      "entitled": true,  
      "rate_type": "FLAT",  
      "price": 120,  
      "pricing_group_values": {  
        "region": "us-east-2",  
        "cloud": "aws"  
      }  
    }  
  ]  
}'
```

## Update a rate card​

After creation, you have two options for updating the rate card: edit the rate card metadata or schedule a rate change.

### Edit rate card metadata​

When editing the rate card metadata, you can:

* Change the rate card name
* Change the rate card description
* Add or remove rate card aliases
* Rate new products on your rate card

To edit the rate card metadata, go to the specific rate card from the **Offering** > **Rate Cards** page or make a POST request to [/contract-pricing/rate-cards/update](/api-reference/rate-cards/update-a-rate-card).

### Schedule a rate change​

Scheduling a price change is a common workflow for organizations. In traditional billing systems, this process can require significant cross-functional coordination to ensure the change takes place at the right moment.

Metronome streamlines this process by allowing you to schedule changes for a specified time period. For example, if you know you’re launching a product next month, you can schedule a rate change to go into effect on the launch day. On the day your rate changes take place, you can focus on your customers, not on their billing configuration.

To schedule a rate change through the API, make a POST request to [/contract-pricing/rate-cards/addRates](/api-reference/rate-cards/add-a-rate). This is the same endpoint used to create new rates.

The example below uses the same API call as the prior example, however, it adds two important additions: a `starting_at` date set for one year after the initial pricing and the updated price.

```bash theme={null}
 curl https://api.metronome.com/v1/contract-pricing/rate-cards/addRates \  
  -H "Authorization: Bearer <TOKEN>" \  
  -H "Content-Type: application/json" \  
  -d '{  
  "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",  
  "rates": [  
    {  
      "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",  
      "starting_at": "2025-01-01T00:00:00.000Z",  
      "entitled": true,  
      "rate_type": "FLAT",  
      "price": 120,  
      "pricing_group_values": {  
        "region": "us-west-2",  
        "cloud": "aws"  
      }  
    },  
    {  
      "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",  
      "starting_at": "2025-01-01T00:00:00.000Z",  
      "entitled": true,  
      "rate_type": "FLAT",  
      "price": 140,  
      "pricing_group_values": {  
        "region": "us-east-2",  
        "cloud": "aws"  
      }  
    }  
  ]  
}'
```

## Dimensional pricing​

Cloud-based companies seeking to align their COGS with pricing strategies commonly adopt dimensional pricing. For these companies, the product may cost a variable amount depending on its configuration. Dimensional pricing helps you set a product’s rate across multiple dimensions (cost drivers) without creating new product entities. You can define these dimensions by pricing [group keys](/guides/get-started/core-concepts/create-billable-metrics#3-define-group-keys%E2%80%8B) on the underlying product.

### How dimensional pricing works​

The dimensional pricing structure simplifies the management of products and billable metrics by minimizing the amount of each required to represent your business’s pricing scheme. The relationship between rates and the underlying objects looks like this:

**Traditional Metronome object relationship:** 1 billable metric → 1 product → 1 rate

**Dimensional pricing object relationship:** 1 billable metric → 1 product → many rates

To further explain dimensional pricing, consider an example infrastructure SaaS client. This client has 3 products: reads, writes, and data storage.

Traditionally, a single product would get a single price. Instead, for this client, rates are based on four additional dimensions:

* Cloud provider: AWS, Azure, or GCP
* Zone: na, emea, apac, or sa
* Classification: basic, premium, or platinum
* Number of cloud availability zones: 3 or 1

To determine how many total rates the client has, multiply the number of products by each of the possible values for each group:

3 cloud providers \* 4 zones \* 3 classifications \* 2 availability zones \* 3 products = 216 combinations that could need distinct prices.

This pricing model is advantageous for the example infrastructure company given price variability across dimensions. AWS, Azure, and GCP may charge them different rates depending on the region. Using dimensional pricing in Metronome, they only need to manage three products and billable metrics by instead relying on the grouping keys (for example, cloud provider) for each.

For help determining if dimensional pricing is right for your business model, contact your Metronome representative.

### Set up dimensional pricing​

Set up a rate card with dimensional pricing in the Metronome app or with the API.

To set up dimensional pricing in the Metronome app:

1. Create a new rate card and choose product(s) to add. Ensure that the products you're adding have [pricing group keys](/guides/get-started/core-concepts/create-products-contracts#pricing-group-keys%E2%80%8B) defined.
2. Define the potential values present across each pricing key dimension. For example, if the dimension is `aws_region`, define each possible region.
3. Assign rates to each combination of pricing group keys.

To set dimensional prices with the API, make a POST request to the [/contract-pricing/rate-cards/addRates](/api-reference/rate-cards/add-a-rate) endpoint.

## Tiered pricing​

Tiered pricing is a usage-based pricing model where the rate applied depends on the quantity used so far in the billing period. For example, a rate card for a cloud database product might dictate that the first thousand gigabytes of data cost \$0.10 per gigabyte, and every gigabyte thereafter costs \$0.09. Or, another product might offer a free tier up to a usage limit, then charge for usage past that limit.

### How tiered pricing works​

You can define tiers when creating a rate card or as an [override](/guides/pricing-packaging/make-pricing-changes/edit-or-override-a-contract) on a contract. On contract overrides you can change the tier boundaries or price assigned to each tier for a specific customer.

When you configure tiered pricing on a rate card, the minimum usage value is exclusive and the maximum usage value is inclusive.

Consider an example communications client with a long distance phone call product. This product has three pricing tiers: the first 5 uses are free, uses 6-10 are \$1 each, and uses 11 and above are \$1.50 each. Their tiering rate in the Metronome app looks like this:

| Minimum | Maximum | Value |
| ------- | ------- | ----- |
| 0       | 5       | \$0   |
| 5       | 10      | \$1   |
| 10      | ∞       | \$1.5 |

<Info>
  **INFO**

  You only need to set up tiered pricing once for a product with [presentation group keys](/guides/get-started/core-concepts/create-products-contracts#group-keys%E2%80%8B). Metronome automatically applies tiers per presentation group value. For example, if a client uses `project_id` as a presentation group key on product X, setting a tiered rate on product X automatically applies per `project_id`.
</Info>

Invoices for tiered products group charges by tier and reflect each tier as a separate line item.

### Set up tiered pricing​

Set up a rate card with tiered pricing in the Metronome app or with the API.

To set up tiered pricing in the Metronome app:

1. Create a new rate card and choose the product(s) to add.
2. In the **Usage** table, find the product you want to rate and click **...** > **Add Tiers**.
3. Define the tiers and dollar amounts. Fill out the minimum usage value on the left (exclusive) and the maximum usage value on the right (inclusive).
4. Click **Save**.

To set tiered pricing with the API, make a POST request to the [/contract-pricing/rate-cards/addRate](/api-reference/rate-cards/add-a-rate) endpoint and use `"rate_type": "tiered"`.
