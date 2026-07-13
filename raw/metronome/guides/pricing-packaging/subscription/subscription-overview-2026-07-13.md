<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/subscription/subscription-overview.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

Metronome's billing platform supports subscriptions as a product type. Subscriptions are recurring fees billed on a schedule. Use subscription fees for seat based billing models, platform fees, or other recurring charges.

## How subscriptions work​

Learn how to work with the subscription data model to support your use cases.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/C_lGxKgdkdHt6xoX/images/docs/pricing-packaging/manage-contracts/create-subscription/subscription-data-model-d9853d14d7b23497d8f1c34b59f26f84.png?fit=max&auto=format&n=C_lGxKgdkdHt6xoX&q=85&s=65de2014fd6c80c8957eb9d1cace44fa" alt="Subscription data model" width="1043" height="436" data-path="images/docs/pricing-packaging/manage-contracts/create-subscription/subscription-data-model-d9853d14d7b23497d8f1c34b59f26f84.png" />
</Frame>

### Products​

The product is what ultimately drives the line item on the customer's invoice.

Create a subscription product for each type of subscription you offer. For example, if you offer a Good, Better, and Best plan, create a product for each. Think of products as similar to SKUs.

### Rates​

Add a rate to the rate card for each standard price you offer. The price set on the rate card is the *price for a quantity of 1.*

A product can map to multiple rates. For example, consider a scenario where you sell your Good, Better, and Best subscriptions at different rates depending on whether your customer pays for it monthly, quarterly, or annually. To model this in Metronome, create 9 rates, with 3 rates per product, to represent the distinct prices for each billing frequency.

### Contracts​

With contracts, you can encode different types of billing models in Metronome. When a customer purchases a subscription plan, create a contract for the customer and set `entitlement`to `true` for the corresponding subscription rate (for example, Good - Monthly).

Use the contract to set quantity, proration behavior, and collection behavior: in-advance or in-arrears.Metronome doesn't distinguish between types of subscription, such as a recurring platform fee or a seat-based subscription. `quantity` defines how many subscriptions a customer has. Most commonly, this models how many seats a customer is entitled to.

Optionally define whether credit balance should provisioned as part of the subscription. Credits can be pooled at the subscription level or scoped per seat.

### Learn how to manage subscriptions within Metronome

<Card title="Define subscription pricing" icon="link" href="/guides/pricing-packaging/subscription/define-subscription-pricing" arrow="true" cta="Learn more">
  Create subscription products and add them to your rate card to define standard list prices.
</Card>

<Card title="Provision your customer" icon="link" href="/guides/pricing-packaging/subscription/provision-your-customer" arrow="true" cta="Learn more">
  Create contracts for your customers based on the subscription plan they choose. Supports standard subscription recurring fees and hybrid credit models.
</Card>

<Card title="Manage seats" icon="link" href="/guides/pricing-packaging/subscription/manage-seats" arrow="true" cta="Learn more">
  Change the count of seats per subscription and optionally associate a seat to user id. View changes over time and manage seat balance for hybrid models.
</Card>

<Card title="Subscription lifecycle" icon="link" href="/guides/pricing-packaging/subscription/manage-subscription-lifecycle" arrow="true" cta="Learn more">
  Moodel subscription transitions within Metronome.
</Card>
