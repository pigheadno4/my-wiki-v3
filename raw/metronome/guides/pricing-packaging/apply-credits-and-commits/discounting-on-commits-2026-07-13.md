<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/discounting-on-commits.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Offer discounts on commits

To generate more predictable revenue, companies prefer their customers to commit to spending thresholds. To incentivize customers to do so, companies can offer discounts for larger commitments.

Metronome provides the flexibility to model these discounts in two primary ways:

1. Reduce the cost basis for the commit
2. Create commit-specific overrides on the customer contract

For advanced billing structures, Metronome also supports a third way to discount commits: encoding *commit rates* on a rate card.

## Reduce the commit cost basis​

A common approach to discounting commits is to reduce the cost basis.

As an example, an enterprise contract states that in exchange for a \$10,000 pre-committed amount, the customer receives a 20% discount when consuming the commit.

One option for encoding this pricing model is to change the cost basis of the pre-committed amount. You can encode a 20% discount by granting the customer \$10,000 of spend, but only billing \$8,000.

This example API call creates a commit with a \$10,000 access schedule but an \$8,000 invoice schedule:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/customerCommits/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
    "type": "prepaid",
    "name": "Prepaid Commitment",
    "priority": 1,
    "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
    "access_schedule": {
      "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
      "schedule_items": [
        {
          "amount": 100000,
          "starting_at": "2024-10-01T00:00:00.000Z",
          "ending_before": "2025-10-01T00:00:00.000Z"
        }
      ]
    },
    "invoice_schedule": {
      "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
      "schedule_items": [
        {
          "unit_price": 80000,
          "quantity": 1,
          "timestamp": "2024-10-01T00:00:00.000Z"
        }
      ]
    }
  }'
```

When using the cost basis to encode the discount, note:

* The prices reflected on usage statements are not affected by the cost basis. The 20% discount when using the commit is not visible on the usage statement.
* Using the cost basis only works when commit rates are a uniform percentage off, not when commit rates are completely distinct from list rates or have different per-product rates.
* This discount method is suitable when the commit is prepaid, but not for postpaid commits, where the invoice schedule amount must match the access schedule amount.

If your use case doesn't meet these criteria, you can use commit-specific overrides instead.

## Create commit-specific overrides​

An alternative way of granting a discount when consuming a commit is to apply *commit-specific overrides* to encode adjusted rates when consuming a commit. You can specify whether the override should apply when consuming **all commits and credits** (prepaid commits, postpaid commits, and credits) or **only specific commits or credits** (e.g. commit\_id A and recurring\_credit\_id B).

You can create commit-specific multiplier, overwrite, or tiered overrides. You can use product IDs, product tags, pricing group keys, and presentation group keys to specify which line items should get an override.

Commit-specific overrides are higher priority than non-commit-specific overrides. Overrides are prioritized using the following logic:

1. Commit-specific overwrite overrides.
2. Commit-specific multiplier overrides, prioritized with your contract's prioritization scheme (lowest multiplier or explicit).
3. Non-commit-specific (contract-level) overwrite overrides.
4. Non-commit-specific multiplier overrides, prioritized with your contract's prioritization scheme (lowest multiplier or explicit).

<Info>
  **INFO**

  Commit-specific overrides are not prioritized based on the number of commits associated with an override. If you add a multiplier override that applies to all commits, and a multiplier override that applies only to commit B, these two overrides are prioritized based on normal prioritization rules (lowest multiplier or explicit).
</Info>

<Info>
  **INFO**

  Metronome provides functionality to target a commit-specific override to a specific `commit_id` or `recurring_commit_id`, `credit_id`, or `recurring_credit_id`. Use the field `any_commit_or_credit_ids` to limit the scope of a commit-specific override. If no specific credits or commits are targeted, the override will apply whenever usage burns down any prepaid commit, postpaid commit, or credit.
</Info>

### Continued discount example

As an example of overriding the commit on a customer contract, take this example with a discount on both the commit spend and additional consumption:

* Your list rates for audio models are \$1 per million input tokens and \$2 per million output tokens. Both products are tagged with `audio`.
* The customer committed to \$10,000 of prepaid spend on their contract (commit A).
* The customer has negotiated prices when consuming the prepaid spend and after the commit has been fully consumed:
  * When consuming the commit, the customer gets 20% off list prices.
  * When not consuming the commit, the customer get 5% off list prices.

To implement this in Metronome, add two overrides on the contract. The commit-specific override takes higher priority over any non-commit-specific overrides:

* Override 1: 0.95 multiplier against the `audio` product tag
* Override 2: 0.8 multiplier against the `audio` product tag when consuming commit A

This example API request creates the contract, including the prepaid commit and commit-specific overrides. Notice the commit is referred to using a `temporary_id` to allow encoding both commits and commit-specific overrides on contract creation.

```bash theme={null}
curl https://api.staging.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
  "customer_id": "bc20325a-80a0-468e-868f-a2f28b972af8",
  "starting_at": "2024-10-01T00:00:00.000Z",
  "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
  "commits": [
    {
      "temporary_id": "prepaid_commit_A",
      "type":"prepaid",
      "priority":1,
      "name":"Prepaid Commit A",
      "product_id":"f14d6729-6a44-4b13-9908-9387f1918790",
      "access_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "amount": 1000000,
            "starting_at": "2024-10-01T00:00:00.000Z",
            "ending_before": "2025-10-01T00:00:00.000Z"
          }
        ]
      },
      "invoice_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "unit_price": 1000000,
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
      "multiplier": 0.95,
      "type": "multiplier",
      "override_specifiers": [
        {
          "product_tags": [
            "audio"
          ]
        }
      ]
    },
    {
      "starting_at": "2024-10-01T00:00:00.000Z",
      "is_commit_specific": true,
      "multiplier": 0.8,
      "type": "multiplier",
      "override_specifiers": [
        {
          "commit_ids": [
            "prepaid_commit_A"
          ],
          "product_tags": [
            "audio"
          ]
        }
      ]
    }
  ]
}'
```

### Discount when consuming any commit or credit​

As another example of creating commit-specific overrides, take this example with a discount when consuming any commit:

* Again, your list rates for audio models are \$1 per million input tokens and \$2 per million output tokens.
* The customer has committed to \$3,000 of prepaid spend on their contract (commit A). The customer wants to leave open the option of adding more prepaid commits in the future.
* The customer has negotiated prices when consuming commits: audio model input tokens are \$0.75 per million and audio model output tokens are \$0.889 per million.
* When all commits are consumed, further usage of audio models use the list rate.

To implement this in Metronome, add two overrides on the contract:

* Override 1: overwrite override of \$0.75 on input tokens when consuming **any commit or credit**
* Override 2: overwrite override of \$0.889 on output tokens when consuming **any commit or credit**

This example API request adds both overrides by editing the contract:

```bash theme={null}
curl https://api.staging.metronome.com/v2/contracts/edit \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "bc20325a-80a0-468e-868f-a2f28b972af8",
    "contract_id": "82a884c5-5e3e-47ae-b056-63b6f3a84674",
    "add_overrides": [
      {
        "starting_at": "2024-10-01T00:00:00.000Z",
        "product_id": "c8dccd54-0ca8-4580-861d-1e26854ab2f1",
        "is_commit_specific": true,
        "type": "overwrite",
        "overwrite_rate": {
            "rate_type":"flat",
            "price": 75
        }
      },
      {
        "starting_at": "2024-10-01T00:00:00.000Z",
        "product_id": "1e0f9c54-56c9-4587-b0ad-a94b53fe623a",
        "is_commit_specific": true,
        "type": "overwrite",
        "overwrite_rate": {
            "rate_type":"flat",
            "price": 88.9
        }
      }
    ]
}'
```

## Encoding commit rates on the rate card​

Some clients have a business model with consistent *commit rates* offered to all customers who sign up for a commitment. Metronome makes it easy to encode these commit rates on the rate card, so you don’t need to use commit-specific overrides for every customer who makes a commitment. In addition, Metronome offers the flexibility to further discount the commit rate to account for per-customer negotiation.

### 1. Set up commit rates on the rate card.​

First, define the commit rate on the rate card. You can do this using the [Metronome app](https://app.metronome.com/) or the [Metronome API](/api-reference/rate-cards/add-a-rate). Note:

* Commit rates are only supported for usage products.
* Commit rates must be added with a list rate. There is no way to just change a commit rate; you must add a list rate with it.
* List and commit rate must be in the same pricing unit.
* The commit rate (and the list rate) can be tiered. The tier quantity is not reset between using the commit rate and the list rate.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/C_lGxKgdkdHt6xoX/images/docs/pricing-packaging/apply-credits/discounts/add-commit-rate-68340b60850c9b9f13b197158243a07d.png?fit=max&auto=format&n=C_lGxKgdkdHt6xoX&q=85&s=f10f75d2d94e2e363350be17e334306f" alt="Commit rate on a rate card" width="2888" height="1456" data-path="images/docs/pricing-packaging/apply-credits/discounts/add-commit-rate-68340b60850c9b9f13b197158243a07d.png" />
</Frame>

### 2. Create the commit.​

Next, create the commit on a contract. Specify that the commit should use the commit rate.

Only specify that a commit or credit uses the commit rate if you’ve added distinct commit rates to the rate card.

<Warning>
  **FALLBACK BEHAVIOR**

  If you add to a customer or contract a commit or credit that uses a commit rate and there is no commit rate for a given product, Metronome applies the list rate as well as any overrides that target list rate. Any overrides that target commit rate are ignored.
</Warning>

### 3. (Optional) Offer discounts on the commit rate.​

Metronome supports discounting the default commit rate by adding a commit-specific override on the contract. To do so:

* Specify that the type of override is `commit-specific`.
* Specify that the target of the override is `COMMIT_RATE`.
* Add specific `commit ids`. If `commit_ids` are not specified, the override applies whenever a prepaid or postpaid commit is used.

You should only specify overrides with the rate target `COMMIT_RATE` if you’ve added distinct commit rates to the rate card. Otherwise Metronome applies the fallback behavior (mentioned above).

### Commit and on-demand rates with no discounts example​

As an example, consider a client with list rates and commit rates consistent across all customers or a subset of their customers.

First, specify the commit rates on the rate card:

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
    "price": 1000,
    "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
    "commit_rate": {
      "rate_type":"FLAT",
      "price":800
    }
  }'
```

Next, when creating a commit on a customer or contract, specify that the commit should use `commit_rate`:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/customerCommits/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
    "type": "prepaid",
    "name": "Commitment - using commit rate",
    "priority": 100,
    "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
    "rate_type":"commit_rate",
    "access_schedule": {
      "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
      "schedule_items": [
        {
          "amount": 10000,
          "starting_at": "2024-10-01T00:00:00.000Z",
          "ending_before": "2024-11-01T00:00:00.000Z"
        }
      ]
    },
    "invoice_schedule": {
      "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
      "schedule_items": [
        {
          "unit_price": 8000,
          "quantity": 1,
          "timestamp": "2024-10-01T00:00:00.000Z"
        }
      ]
    }
  }'
```

Now, when consuming the commit, commit rates on the rate card are used.

<Tip>
  **TIP**

  Note that it's possible to encode specific rates when burning down commits for a customer by only using commit-specific overrides. But by using commit rates on the rate card, you can set the rates up once rather than adding commit-specific overrides to each customer’s contract.
</Tip>

### Negotiated commit and on-demand rates example

As another example, consider a client with list rates and commit rates consistent across all customers (see the table below). A single customer can negotiate both the rate when using a specific commit (off of commit rate) and their rate when not consuming a commit (off of list rate).

| List rate shared across all customers | Commit rate shared across all customers | Negotiated commit rate for commit A for customer A | Negotiated on-demand rate for customer A |      |
| ------------------------------------- | --------------------------------------- | -------------------------------------------------- | ---------------------------------------- | ---- |
| Audio Input tokens (1M)               | \$10                                    | \$8                                                | \$7.2                                    | \$8  |
| Audio output tokens (1M)              | \$20                                    | \$19                                               | \$17.1                                   | \$16 |

To implement this discount pattern:

1. Specify the commit rates on the rate card (\$8 and \$19).
2. When creating commit A on the contract, specify that commit A should use `commit_rate`.
3. Add two overrides to the contract:

* Override 1: commit-specific override, against `commit_rate`, limited to commit A, 0.9 multiplier.
* Override 2: override against list rate, 0.8 multiplier.

This example API request edits a contract, including the prepaid commit:

```bash theme={null}
curl https://api.staging.metronome.com/v2/contracts/edit \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
  "customer_id": "bc20325a-80a0-468e-868f-a2f28b972af8",
  "contract_id": "82a884c5-5e3e-47ae-b056-63b6f3a84674",
  "add_commits": [
    {
      "temporary_id": "prepaid_commit_A",
      "type": "prepaid",
      "priority": 1,
      "rate_type": "commit_rate",
      "name": "Prepaid Commit A",
      "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
      "access_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "amount": 1000000,
            "starting_at": "2024-10-01T00:00:00.000Z",
            "ending_before": "2025-10-01T00:00:00.000Z"
          }
        ]
      },
      "invoice_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "unit_price": 1000000,
            "quantity": 1,
            "timestamp": "2024-10-01T00:00:00.000Z"
          }
        ]
      }
    }
  ],
  "add_overrides": [
    {
      "starting_at": "2024-10-01T00:00:00.000Z",
      "multiplier": 0.9,
      "is_commit_specific": true,
      "rate_target": "commit_rate",
      "type": "multiplier",
      "override_specifiers": [
        {
          "commit_ids": [
            "prepaid_commit_A"
          ]
        }
      ]
    },
    {
      "starting_at": "2024-10-01T00:00:00.000Z",
      "multiplier": 0.8,
      "rate_target": "list_rate",
      "type": "multiplier",
      "override_specifiers": [
        {
          "product_tags": [
            "audio"
          ]
        }
      ]
    }
  ]
}'
```
