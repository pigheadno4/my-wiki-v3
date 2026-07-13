<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/make-pricing-changes/edit-or-override-a-contract.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Contract edits and overrides

Metronome [rate cards](/guides/get-started/core-concepts/create-manage-rate-cards) contain default rates and entitlement states for your customers, or a subset of your customers. Individual customers can negotiate custom discounts when signing a contract, or you may want to grant time-based promotions to a cohort of customers. To enable these use cases in Metronome, use contract-level overrides.

## Override types​

Use overrides with usage, subscription, and composite products to override the rate or entitlement of a product.

There are three types of rate overrides:

* **Multiplier** multiplies the rate on the rate card by the specified number. For example, a 0.9 multiplier gives a 10% discount from the list rate. As the list rate on the rate card changes, the effective rate after the multiplier is applied also changes.
* **Overwrite** sets a flat or tiered rate for the product. For example, an overwrite can specify that a product’s price is \$3.23. The price for that product remains at \$3.23 regardless of changes to the list price on the rate card.
* **Tiered** multiplies the rate on the rate card by the specified number, for a given quantity range. For example, specify a 0.9 multiplier with `size = 5` to give a 10% discount from the list rate only on the first 5 uses in the billing period.

<Info>
  **INFO**

  You can only use tiered overrides when the contract uses explicit override prioritization.
</Info>

You can also override the entitlement for any product. For example, if a given product is disabled on the rate card but a customer has early access to the product, add an override to enable the product on the customer’s rate card. Once a product's entitlement is enabled, usage of that product appears on the customer’s invoices.

## Target overrides​

To fine-tune what overrides apply to, target them to specific product IDs, product tags, or pricing and presentation group values.

For most cases, use the `applicable_product_tags` and `product_id` fields in the API or UI. Any product that has a product tag included in the `applicable_product_tags` array, or with the specified product ID is targeted for the override.

If you need more complex logic, use the `override_specifiers` field in the API to target overrides based on combinations of product ID, product tags, and pricing and presentation group values.

The `override_specifiers` field takes in an array of objects, where each object is called a specifier. Within each specifier all fields are ANDed together. If the conditions of any specifier in the array are met, then the line item is targeted for the override.

For example, this `override_specifiers` field targets a multiplier against any usage that meets either of these requirements:

* The product has the product tags `Read` and `Write` and a pricing group value of `resource.region = af-south-1`
* The product has the product tag `Query` and the pricing group values `resource.region = uaenorth` and `resource.hardware = gpu1`

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d 
  '{
  "customer_id": "e15ce0e6-33f0-44bb-89c7-05bc296f5b5e",
  "contract_id": "f9e0b117-42e0-4145-b524-b97302a57518",
  "starting_at": "2024-01-01T00:00:00.000Z",
  "overrides": [
    {
      "starting_at": "2024-01-01T00:00:00.000Z",
      "type": "multiplier",
      "multiplier": 0.7,
      "priority":1,
      "override_specifiers": [
        {
          "product_tags": ["Read", "Write"],
          "pricing_group_values": {
            "resource.region": "af-south-1"
          }
        },
        {
          "product_tags": ["Query"],
          "pricing_group_values": {
            "resource.region": "uaenorth",
            "resource.hardware":"gpu1"
          }
        }
      ]
    }
  ]
}'
```

<Info>
  **INFO**

  You cannot use product tags to target overwrite overrides. When using dimensional pricing, you must use the product ID with or without pricing group values and specify all pricing group values to apply the override. For example, if the rate is specifically for the `us-east1` region and `gpu1` hardware type, you must specify the product ID and both pricing group values in the `override_specifiers`.
</Info>

## Example: Time-based discount against a product tag​

To create time-based discounts, specify `starting_at` and `ending_before` dates on the override. Beyond that, using product tags to target overrides makes launching new products easier. Add the pertinent product tags to a new product on creation, and any discounts automatically apply.

This API call grants a 30% discount on all products that have either the product tag `Read` or `Write` for all of 2024. This example has simple targeting logic, so it uses the `applicable_product_tags` field. To target products that have both `Read` and `Write` product tags, you would use the `override_specifiers` field instead.

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d
'{
  "customer_id": "e15ce0e6-33f0-44bb-89c7-05bc296f5b5e",
  "contract_id": "f9e0b117-42e0-4145-b524-b97302a57518",
  "starting_at": "2024-01-01T00:00:00.000Z",
  "overrides": [
    {
      "starting_at": "2024-01-01T00:00:00.000Z",
      "ending_before": "2025-01-01T00:00:00.000Z",
      "type": "multiplier",
      "multiplier": 0.7,
      "priority":1,
      "applicable_product_tags":["Read", "Write"]
    }
  ]
}'
```

## Example: Discount on dimensional pricing​

When using [dimensional pricing](/guides/get-started/core-concepts/create-manage-rate-cards#dimensional-pricing%E2%80%8B), you may want to grant a discount on a subset of rates associated with one product without granting a discount on all rates.

For example, a customer may know that they only use resources in regions `af-south-1` and `uaenorth`. So, they negotiate a discount for the usage of your product only in those two regions. If they use resources in other regions, they get charged at the list rate. This API call grants a discount on rates associated with usage in specific regions.

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d
'{
  "customer_id": "e15ce0e6-33f0-44bb-89c7-05bc296f5b5e",
  "contract_id": "f9e0b117-42e0-4145-b524-b97302a57518",
  "starting_at": "2024-01-01T00:00:00.000Z",
  "overrides": [
    {
      "starting_at": "2024-01-01T00:00:00.000Z",
      "type": "multiplier",
      "multiplier": 0.7,
      "priority":1,
      "override_specifiers": [
        {
          "product_id": "329e6313-ecda-4548-bb71-750ecc2af11a",
          "pricing_group_values": {
            "resource.region": "af-south-1"
          }
        },
        {
          "product_id": "329e6313-ecda-4548-bb71-750ecc2af11a",
          "pricing_group_values": {
            "resource.region": "uaenorth"
          }
        }
      ]
    }
  ]
}'
```

Pricing group values specified in the override can be a subset of all the pricing group values associated with a product. For example, imagine that the product has two pricing group keys, `resource.region` and `resource.hardware`. Adding the above override ensures that usage within `af-south-1` and `uaenorth` receive a 30% discount, regardless of the hardware type.

## Example: Discount against usage for a specific cluster ID​

Some clients have a business model where they grant customers discounts for using specific resources, like bring-your-own-model pricing. These resources aren’t set as pricing group keys to allow distinct pricing across all customers. Instead, they’re set as presentation group keys.

This API call grants 20% off of a product when using a specific `cluster_id` and `resource_id` combination.

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d
'{
  "customer_id": "e15ce0e6-33f0-44bb-89c7-05bc296f5b5e",
  "contract_id": "f9e0b117-42e0-4145-b524-b97302a57518",
  "starting_at": "2024-01-01T00:00:00.000Z",
  "overrides": [
    {
      "starting_at": "2024-01-01T00:00:00.000Z",
      "type": "multiplier",
      "multiplier": 0.8,
      "priority":1,
      "override_specifiers": [
        {
          "product_id": "329e6313-ecda-4548-bb71-750ecc2af11a",
          "presentation_group_values": {
            "cluster_id":"43145",
            "resource_id":"5436436"
          }
        }
      ]
    }
  ]
}'
```

## Example: Discount based on quantity consumed​

Use tiered overrides to incentivize usage and give a customer discounts based on the quantity they consume.

This API call grants a 20% discount on list prices for the first 10 uses of a product in the billing period, and a deeper discount of 30% for the next 10 uses.

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d
'{
  "customer_id": "e15ce0e6-33f0-44bb-89c7-05bc296f5b5e",
  "contract_id": "f9e0b117-42e0-4145-b524-b97302a57518",
  "starting_at": "2025-01-01T00:00:00.000Z",
  "overrides": [
    {
      "starting_at": "2024-01-01T00:00:00.000Z",
      "type": "tiered",
      "priority":1,
      "product_id": "2fc7d449-2e30-4d7d-accb-37835722a313",
      "tiers": [
        {
          "size":10,
          "multiplier":0.8
        },
        {
          "size":10,
          "multiplier":0.7
        }
      ]
    }
  ]
}'
```

## Override prioritization​

For a given line item on a usage invoice, only one override is prioritized. Overrides don't stack.

Overwrite overrides have the highest priority and always take precedence over multiplier or tiered overrides. In the case of multiple applicable overwrite overrides, the last-added overwrite override applies.

Specify how to prioritize multiplier overrides when creating the contract.

* **Lowest multiplier** : The applicable multiplier that grants the largest discount is applied.
* **Explicit** : Specify a priority on each multiplier override. The override with the lowest priority value is prioritized.
