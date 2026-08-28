<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/token-billing.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Token Billing

Many companies pass through the cost of LLM tokens to their customers, adding a markup to remain margin-positive. This guide describes how to bill customers for AI usage by token consumption in Metronome, including:

* Selecting common models from Anthropic, OpenAI, Google, and other providers
* Creating billable metrics, products, and rates based on your configured markup percentage(s)
* Automatically syncing newly released models to your rate card at your configured markup

<Info>
  **Private preview**

  Token Billing is in private preview. To request access, contact us via the [Metronome support portal](https://support.metronome.com/) or [sign up for the waitlist](https://docs.stripe.com/billing/token-billing).
</Info>

## Use case

Fictional company Designr is an AI-powered design tool. Customers use Designr to generate design assets, including prototypes, mockups, and images. Designr uses common AI models and charges customers a 10% markup on underlying model costs.

Designr offers several plan tiers. Its Pro Plan includes 200 Designr Credits -- a custom pricing unit -- each month. If a customer uses all of their Designr Credits, they can purchase additional credits during the month.

## Set up your rate card

In Metronome, a rate card is your centralized price book, where you define pricing for all products. When you use Token Billing, Metronome automatically creates billable metrics, products, and rates for managed AI products based on the markup you enter. You do not need to create these separately.

Because Designr uses a custom pricing unit, Designr Credits, first navigate to **Offering > Pricing Units > Custom Pricing Units**. Click **+ Add**, then create a custom pricing unit named **Designr Credits**. Next, create your rate card.

> **Note:** When using Token Billing, non-USD fiat currencies are not supported, as provider prices are denominated in USD.

### Create your rate card

1. Click **Offering** in the left-hand sidebar.
2. Navigate to the **Rate Cards** tab and select **+ Add**.
3. Enter the rate card name and description, then enable **Charge based on AI provider pricing (managed)**. You can also add a human-readable alias, such as `default_rate_card`, to reference the rate card more easily throughout the API.
4. Select the AI models you want to use. You can select all models from a provider or expand the provider to select individual models.
5. Add any other usage-based, subscription, or composite products that you want to include on the same rate card.
6. Click **Next** to proceed to the next page.

#### Set rates — Custom Pricing Unit

1. Under **Default markup for future AI models**, enter the markup percentage that should automatically apply when new models are added to the rate card.
2. In the upper-right corner of the AI models section, select **USD**. In the dropdown, select the **Designr Credits** custom pricing unit.
3. In the modal, define a conversion rate between USD and Designr Credits.
4. Expand each model to verify its distinct rates by author, provider, and token type.
5. Click **Save**.

#### Set rates — USD

1. Under **Default markup for future AI models**, enter the markup percentage that should automatically apply when new models are added to the rate card.
2. Enter markup percentages for each selected model, or use **Apply markup to all** in the upper-right corner to apply the same markup percentage to every selected model.
3. Expand each model to verify its distinct rates by author, provider, and token type.
4. Click **Save**.

## Define your pricing model

Because Designr’s Pro Plan includes an allocation of 200 Designr Credits per month, you can create a Package to encode the credit allocation alongside the rate card you just created. In Metronome, [Packages](/guides/implement-metronome/core-concepts/packages-overview) define customer-facing offerings, such as Pro Plan or Max Plan, and simplify assigning PLG customers to these offerings.

## Provision customers

You are now ready to assign customers to the Pro Plan. Provisioning a customer with a package creates a contract: a customer-specific agreement that applies the terms from the package.

Use the API call below to provision a customer with the Pro Plan:

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.metronome.com/v1/contracts/create \
    --header "Authorization: Bearer $METRONOME_API_TOKEN" \
    --header "Content-Type: application/json" \
    --data '{
      "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
      "package_alias": "designr_pro",
      "starting_at": "2026-08-28T00:00:00.000Z"
    }'
  ```

  ```python Python theme={null}
  response = client.v1.contracts.create(
    customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    package_alias="designr_pro",
    starting_at="2026-08-28T00:00:00.000Z"
  )
  ```

  ```javascript Node theme={null}
  await client.v1.contracts.create({
    customer_id: '13117714-3f05-48e5-a6e9-a66093f13b4d',
    package_alias: 'designr_pro',
    starting_at: '2026-08-28T00:00:00.000Z'
  });
  ```

  ```ruby Ruby theme={null}
  response = client.v1.contracts.create(
    customer_id: '13117714-3f05-48e5-a6e9-a66093f13b4d',
    package_alias: 'designr_pro',
    starting_at: '2026-08-28T00:00:00.000Z'
  )
  ```

  ```go Go theme={null}
  contractStartingTime, err := time.Parse(time.RFC3339Nano, "2026-08-28T00:00:00.000Z")
  if err != nil {
    panic(err.Error())
  }

  contractResponse, err := client.V1.Contracts.New(context.TODO(), metronome.ContractNewParams{
    CustomerID:   metronome.F("13117714-3f05-48e5-a6e9-a66093f13b4d"),
    PackageAlias: metronome.F("designr_pro"),
    StartingAt:   metronome.F(contractStartingTime),
  })
  if err != nil {
    panic(err.Error())
  }
  ```
</CodeGroup>

You can layer on or customize additional terms on this contract. For example, if a customer has exhausted all of their credits for the month and wants to purchase more, you can use Metronome’s [payment-gated credit flow](/guides/pricing-packaging/billing-model-guides/prepaid-credits) to charge for incremental Designr Credits. You can also use [overrides](/guides/pricing-packaging/make-pricing-changes/edit-or-override-a-contract) to customize rates on a per-customer basis.

## Integrate usage tracking

Ensure that your events follow the format below, with `event_type` set to `token-billing`.

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.metronome.com/v1/ingest \
    --header "Authorization: Bearer $METRONOME_API_TOKEN" \
    --header "Content-Type: application/json" \
    --data '[{
      "transaction_id": "b1d52889-f8f7-4aee-a41f-f2eb89789ece",
      "timestamp": "2026-08-24T18:38:50.597Z",
      "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
      "event_type": "token-billing",
      "properties": {
        "model": "anthropic/claude-fable-5",
        "provider": "anthropic",
        "input_tokens": 233,
        "cached_input_tokens": 1459,
        "output_tokens": 83,
        "cached_write_tokens": 210
      }
    }]'
  ```

  ```python Python theme={null}
  response = client.v1.usage.ingest(
    usage=[
      {
        "transaction_id": "b1d52889-f8f7-4aee-a41f-f2eb89789ece",
        "timestamp": "2026-08-24T18:38:50.597Z",
        "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
        "event_type": "token-billing",
        "properties": {
          "model": "anthropic/claude-fable-5",
          "provider": "anthropic",
          "input_tokens": 233,
          "cached_input_tokens": 1459,
          "output_tokens": 83,
          "cached_write_tokens": 210
        }
      }
    ]
  )
  ```

  ```javascript Node theme={null}
  async function main() {
    await client.v1.usage.ingest({
      usage: [{
        transaction_id: 'b1d52889-f8f7-4aee-a41f-f2eb89789ece',
        timestamp: '2026-08-24T18:38:50.597Z',
        customer_id: '13117714-3f05-48e5-a6e9-a66093f13b4d',
        event_type: 'token-billing',
        properties: {
          model: 'anthropic/claude-fable-5',
          provider: 'anthropic',
          input_tokens: 233,
          cached_input_tokens: 1459,
          output_tokens: 83,
          cached_write_tokens: 210
        }
      }],
    });
  }

  main();
  ```

  ```ruby Ruby theme={null}
  result = metronome.v1.usage.ingest(
      usage: [
        {
          transaction_id: 'b1d52889-f8f7-4aee-a41f-f2eb89789ece',
          timestamp: '2026-08-24T18:38:50.597Z',
          customer_id: '13117714-3f05-48e5-a6e9-a66093f13b4d',
          event_type: 'token-billing',
          properties: {
            model: 'anthropic/claude-fable-5',
            provider: 'anthropic',
            input_tokens: 233,
            cached_input_tokens: 1459,
            output_tokens: 83,
            cached_write_tokens: 210
          }
        }
      ]
  )

  puts(result)
  ```

  ```go Go theme={null}
  err := client.V1.Usage.Ingest(context.TODO(), metronome.UsageIngestParams{
    Usage: []metronome.UsageIngestParamsUsage{{
      TransactionID: metronome.F("b1d52889-f8f7-4aee-a41f-f2eb89789ece"),
      Timestamp:     metronome.F("2026-08-24T18:38:50.597Z"),
      CustomerID:    metronome.F("13117714-3f05-48e5-a6e9-a66093f13b4d"),
      EventType:     metronome.F("token-billing"),
      Properties: metronome.F(map[string]interface{}{
        "model":               "anthropic/claude-fable-5",
        "provider":            "anthropic",
        "input_tokens":        233,
        "cached_input_tokens": 1459,
        "output_tokens":       83,
        "cached_write_tokens": 210,
      }),
    }},
  })
  if err != nil {
    panic(err.Error())
  }
  ```
</CodeGroup>

The token usage fields track the number of tokens consumed by type:

* `input_tokens`: Tokens in the prompt
* `cached_input_tokens`: Cached prompt tokens
* `output_tokens`: Tokens in the response
* `cached_write_tokens`: Cache-write tokens. Supported for Anthropic models and OpenAI GPT-5.6+ models only

The `model` and `provider` fields match each token count to the correct rate.

Send events in the correct format to Metronome’s `/ingest` endpoint. Then navigate to the **Events** page to confirm that the events have matched a billable metric.

## Token price updates

When model providers release new models, Metronome automatically updates your rate card to include those models at the default markup specified on the rate card.

Coming soon: Metronome will support automatically updating prices on your rate card when a provider changes its underlying rates.
