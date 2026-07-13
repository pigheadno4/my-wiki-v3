<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/subscription/define-subscription-pricing.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Define subscription pricing

Create the list prices for your subscription offerings by first creating your subscription products and then adding them to your rate card.

## Create a subscription product​

Create a subscription product in the [Metronome app](https://app.metronome.com/offering/products) or with the API using the [/v1/contract-pricing/products/create](/api-reference/products/create-a-product) end point. Create a subscription product for each type of subscription you offer. For example, if you offer a Good, Better, and Best plan, create a product for each.

## Optionally add seat id as presentation group key for usage products

If planning to support a seat based credit model, ensure that all applicable usage products have a `seat_id` presentation group key set on them. This will be used to determine the usage on a per product, per seat basis. See an example of a usage event with a `seat_id` property below:

```json theme={null}
{
  "event_type": "video_generation",
  "properties": {
    "model_name": "claude-3-opus",
    "resolution": "1080p",
    "environment": "production",
    "video_duration_seconds": 20,
    "seat_id": "example@metronome.com"
  },
  "transaction_id": "21f00039-0572-4f63-bf0f-b19faa3d10f8",
  "customer_id": "94fbf9f3-2826-4503-8446-013c68817744",
  "timestamp": "2025-10-15T15:23:48.751Z"
}
```

## Add a subscription product to a rate card​

Add your subscription product(s) to a rate card with the [Metronome app](https://app.metronome.com/offering/rate-cards) or the API. Your rate card acts as your list price for your subscription offering based on a quantity of 1. Quantity amount and associated credits are configured later, during the contract creation process.

When using the API to [add rates](/api-reference/rate-cards/add-a-rate) to a rate card:

1. Add your subscription to the rate card as a `flat` rate.
2. Specify a `price` and `billing_frequency`.
3. Specify an `entitlement` state. If you have more than one subscription rate on your rate card, Metronome recommends defaulting them to `false` and enabling them when provisioning a contract.

This call shows an example of using `rate-cards/addRate` to add subscription products to a rate card:

```json theme={null}
{
    "entitled": false,
    "product_id": "660445c5-e409-42dc-9aac-07df3b2cde35",
    "rate_card_id": "a7bc3775-b651-46b6-b7e4-d225a7e55c4c",
    "rate_type": "flat",
    "starting_at": "2025-04-01T00:00:00.000Z",
    "price": 500,
    "billing_frequency": "MONTHLY"
}
```
