<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/guarantee-zero-overages.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Guarantee zero overages

Some customers must never be billed for usage beyond their committed balance—free trial accounts, fraud-sensitive segments, or customers on strict internal budgets. Guarantee zero overages in Metronome by setting list rates to 0 USD and encoding the real prices either as a commit rate on the rate card or as a commit-specific override on the contract. Usage burns down the commit at the real prices while balance exists, and falls back to 0 USD after the commit is exhausted.

<Note>
  **Only use this pattern when customers must never be charged for overages.** If you want to allow overages but need controls around them, Metronome offers two complementary mechanisms instead:

  * **[Prepaid balance thresholds](/guides/customers-billing/optimize-customer-experience/prepaid-balance-thresholds)** auto-recharge a customer's prepaid commit balance when it drops to a `threshold_amount`, topping it back up to a `recharge_to_amount`. Useful when you want continuous service with automatic top-ups.
  * **[Spend thresholds](/guides/customers-billing/optimize-customer-experience/set-customer-spend-control)** cap how much a customer can accrue before a payment is triggered—useful for limiting fraud exposure in PLG workflows.

  The pattern below is the right choice only when there is no tolerance for charging customers overages.
</Note>

## When to use this pattern

This approach is useful when:

* **Free trials** must hard-cap at the granted amount with no possibility of a bill.
* **Fraud-sensitive accounts** could otherwise rack up runaway usage before fraud signals fire.
* **Strict-budget customers** require a contractual guarantee that you never invoice them for overages, even if your application's gating fails.

## How it works

Two pieces work together:

1. **List rate of 0 USD** on the rate card. This is the fallback price after any commit is exhausted, so any leaked usage is billed at 0 USD.
2. **A real per-unit price that only applies while a commit is being drawn down.** You can encode this real price in one of two ways depending on whether prices are uniform across customers or set per customer.

Because both mechanisms only apply while usage is consuming a commit, pricing reverts to the 0 USD list rate the moment the commit hits zero. From that point forward, the line item resolves to 0 USD and the customer is never invoiced for overages.

## Choose your implementation

|                          | Option A: Commit rate on the rate card                                   | Option B: Commit-specific override on the contract |
| ------------------------ | ------------------------------------------------------------------------ | -------------------------------------------------- |
| **Where prices live**    | On the rate card, alongside the 0 USD list rate                          | On each customer's contract                        |
| **Best for**             | Uniform pricing across all (or most) customers on the rate card          | Per-customer customization of commit prices        |
| **Setup cost**           | Configure once on the rate card                                          | Add an override on every contract                  |
| **Customer inheritance** | All customers using the rate card automatically inherit the commit price | Each contract specifies its own commit price       |

<Tip>
  You can combine the two: set a default commit rate on the rate card for most customers, and use commit-specific overrides on contracts that need a different price. Overrides on the contract take precedence.
</Tip>

## Option A: Commit rate on the rate card

Use this when the real price is consistent across all (or most) customers on the rate card. You set the list rate to 0 USD and the real price as a `commit_rate` on the same rate card entry. Customers inherit both automatically—no per-contract override required.

### 1. Add the product to the rate card with `price: 0` and a `commit_rate`

```bash theme={null}
curl https://api.metronome.com/v1/contract-pricing/rate-cards/addRate \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
    "starting_at": "2024-10-01T00:00:00.000Z",
    "entitled": true,
    "rate_type": "FLAT",
    "price": 0,
    "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
    "commit_rate": {
      "rate_type": "FLAT",
      "price": 100
    }
  }'
```

### 2. Create the commit and tell it to use `commit_rate`

When you create the commit on the contract, set `rate_type: commit_rate` so that drawdowns are priced against the rate card's commit rate.

```bash theme={null}
curl https://api.metronome.com/v1/contracts/customerCommits/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "bc20325a-80a0-468e-868f-a2f28b972af8",
    "type": "prepaid",
    "name": "Trial credit",
    "priority": 100,
    "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
    "rate_type": "commit_rate",
    "access_schedule": {
      "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
      "schedule_items": [
        {
          "amount": 10000,
          "starting_at": "2024-10-01T00:00:00.000Z",
          "ending_before": "2025-10-01T00:00:00.000Z"
        }
      ]
    },
    "invoice_schedule": {
      "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
      "schedule_items": [
        {
          "unit_price": 10000,
          "quantity": 1,
          "timestamp": "2024-10-01T00:00:00.000Z"
        }
      ]
    }
  }'
```

While the commit has balance, usage is priced at the rate card's `commit_rate` (100 USD/unit). After the commit is exhausted, usage falls back to the rate card's 0 USD list rate.

## Option B: Commit-specific override on the contract

Use this when each customer needs different prices, or when you don't want to encode the real prices on the rate card. The list rate stays 0 USD on the rate card, and you add an `overwrite` override on each contract that only applies while the commit has balance.

### 1. Set the list rate to 0 USD on the rate card

```bash theme={null}
curl https://api.metronome.com/v1/contract-pricing/rate-cards/addRate \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
    "starting_at": "2024-10-01T00:00:00.000Z",
    "entitled": true,
    "rate_type": "FLAT",
    "price": 0,
    "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2"
  }'
```

### 2. On the contract, add a commit and a commit-specific override

The override is scoped to the commit via `override_specifiers.commit_ids`, so it only applies while that commit has remaining balance.

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "bc20325a-80a0-468e-868f-a2f28b972af8",
    "starting_at": "2024-10-01T00:00:00.000Z",
    "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
    "commits": [
      {
        "temporary_id": "prepaid_commit_A",
        "type": "prepaid",
        "priority": 1,
        "name": "Trial credit",
        "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
        "access_schedule": {
          "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
          "schedule_items": [
            {
              "amount": 10000,
              "starting_at": "2024-10-01T00:00:00.000Z",
              "ending_before": "2025-10-01T00:00:00.000Z"
            }
          ]
        },
        "invoice_schedule": {
          "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
          "schedule_items": [
            {
              "unit_price": 10000,
              "quantity": 1,
              "timestamp": "2024-10-01T00:00:00.000Z"
            }
          ]
        }
      }
    ],
    "overrides": [
      {
        "starting_at": "2024-10-01T00:00:00.000Z",
        "is_commit_specific": true,
        "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
        "type": "overwrite",
        "overwrite_rate": {
          "rate_type": "flat",
          "price": 100
        },
        "override_specifiers": [
          {
            "commit_ids": ["prepaid_commit_A"]
          }
        ]
      }
    ]
  }'
```

While the commit has balance, the override applies and usage is priced at 100 USD/unit. After the commit is exhausted, the override no longer applies and usage falls back to the rate card's 0 USD list rate.

<Note>
  **App-side gating is still required**

  This pattern guarantees zero billing for any usage that leaks through, but it does not stop usage from being submitted. Gate access in your application using [balance thresholds](/guides/pricing-packaging/apply-credits-and-commits/alerts) or webhooks so customers can't continue consuming the product after their commit is exhausted.
</Note>
