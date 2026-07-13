<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/create-a-pre-paid-commit.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Apply credits and commits to contracts

You can grant free credits and encode prepaid and postpaid commits on Metronome contracts. The balance of these credits and commits, and their application against draft invoices, updates continuously in real time as customers use your product. Credits and commits power a range of business models, from product-led growth motions to complex enterprise contracts.

## How credits and commits work​

Credits and commits in Metronome are flexible on these dimensions:

* **Effective time period**: Credits and commits have an `access_schedule` that defines spend allotments associated with one or many date ranges. Define the date ranges by any hour-aligned time, and only usage falling within the range consumes the credit or commit.
* **Applicable products**: Specify a subset of products, defined by product IDs (`applicable_product_ids`) or product tags (`applicable_product_tags`), to consume a credit or commit. Applicable product tags ensure that new products launched in an existing family can consume the correct commits automatically. Alternatively use the [specifiers](/guides/pricing-packaging/apply-credits-and-commits/target-credit-and-commits) field to target usage of credits and commits based on pricing group values or presentation group values.
* **Invoice schedule**: With prepaid commits, define a one-time invoice or break the payment into multiple invoices on any schedule. Customize the amount invoiced for any prepaid commit.
* **Custom fields**: Tag credits and commits with metadata useful for downstream workflows like [alerting](/guides/customers-billing/set-up-notifications/create-and-manage-notifications), [data reconciliation](/guides/reporting-insights/financial-reporting/reconcile-data), and [revenue recognition](/guides/reporting-insights/financial-reporting/revenue-recognition). For example, get alerted when the remaining balance of credits with the custom field `free_trial`reaches 0.

Credits and commits are always associated with a fixed product. This is because products are used to invoice. In the case of commits, the product is used to invoice the prepaid commit amount or the postpaid commit true-up amount. It contains metadata like a name and ID, which enables you to query things like, what's the revenue for this commit's product across my customers?

## Grant a free credit​

Credits give customers a monetary amount of free usage. Common scenarios for free credits include free trials, reimbursement for downtime (SLA credits), and promotions.

<Info>
  For USD, all monetary amounts in the API are in **cents** (for example, `1000` = \$10.00). Other supported currencies use whole units. See [currency denomination](/guides/pricing-packaging/make-pricing-changes/use-currency-custompricingunits#currency-denomination) for details.
</Info>

As a common scenario, clients grant free credits to a customer where the customer can use the credits during the access period for all active contracts. Learn how to [provision customers](/guides/customers-billing/manage-customers/provision-a-customer) with contracts.

To grant credits to a customer through the [Metronome app](https://app.metronome.com/):

1. Go to **Customers** > select the customer > Contract commits and credits > click **Add credit**.
2. Link the credit to a fixed product by selecting the Credit product from the dropdown. Credits and commits in Metronome are always associated with a fixed product. For example, you can create separate products for a free credit, SLA credit, and promotion credit.
3. (Optional) Add an internal description to explain why you’re granting the credit.
4. (Optional) If the credit can only be consumed by a subset of usage, specify applicable product IDs or applicable product tags. If omitted, all usage, subscription, and composite charges can consume credits.
5. (Optional) If the credit should only be consumed by a subset of the customer’s contracts, specify applicable contract names or IDs. If omitted, usage tied to all contracts consumes the credit.
6. Create an access schedule. An access schedule consists of one or more segments, each defined by a date range and associated with an amount. For example, to grant a \$10/month credit for three months, create three segments in the access schedule:
7. (Optional) Specify the rollover percentage of the credit. In the case of a contract renewal, specify what percent of the initial balance of the credit should roll over to the new contract. Learn more about [contract transitions](/guides/customers-billing/manage-customers/manage-customer-lifecycle).

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/C_lGxKgdkdHt6xoX/images/docs/pricing-packaging/apply-credits/apply-credits-commits/create_credit_access_schedule-9a80a10c5a765bc18b27726bf421c6a2.png?fit=max&auto=format&n=C_lGxKgdkdHt6xoX&q=85&s=eb05b6d8102e7331800000012a20c828" alt="Credit Access Schedule Example" width="1786" height="708" data-path="images/docs/pricing-packaging/apply-credits/apply-credits-commits/create_credit_access_schedule-9a80a10c5a765bc18b27726bf421c6a2.png" />
</Frame>

7. Define the priority of the credit. If a customer has multiple credits or commits that could apply against usage, the priority dictates the order in which the credits and commits are consumed. Lower priorities get consumed first. For example, you may want all credits to be consumed fist before consuming any commits. Read about the full list of [prioritization rules](/guides/pricing-packaging/apply-credits-and-commits/prioritization-rules).

This example API request shows how to create a free credit:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/customerCredits/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
    "name": "SLA Credit",
    "priority": 1,
    "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
    "access_schedule": {
      "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
      "schedule_items": [
        {
          "amount": 1000,
          "starting_at": "2024-10-01T00:00:00.000Z",
          "ending_before": "2024-11-01T00:00:00.000Z"
        }, 
        {
          "amount": 1000,
          "starting_at": "2024-11-01T00:00:00.000Z",
          "ending_before": "2024-12-01T00:00:00.000Z"
        },
        {
          "amount": 1000,
          "starting_at": "2024-12-01T00:00:00.000Z",
          "ending_before": "2025-01-01T00:00:00.000Z"
        }
      ]
    }
  }'
```

## Issue a prepaid or postpaid commit​

Prepaid and postpaid commits represent an agreement by a customer to spend a dollar amount over a period of time. Prepaid commits get paid in advance, while postpaid commits get paid in arrears.

While usually associated with contracts, you can also encode commits at a customer level, where they’re consumed by all or a subset of contracts for that customer.

### Prepaid commits​

Prepaid commits get paid in advance.

For example, imagine a customer committed to \$10,000 of spend over the lifetime of their contract, for which they get charged in two invoices: one for \$4,000 and one for \$6,000. The contract spans from October 01, 2024 to October 01, 2025.

To add a prepaid commit to a contract in the Metronome app:

1. When creating a contract, click **Add commit.**
2. Link the commit to a fixed product.
3. (Optional) Add an internal description explaining the reason for granting the commit.
4. (Optional) If the commit can only get consumed by a subset of usage, specify applicable product IDs or applicable product tags. If omitted, all usage, subscription, and composite charges can consume the commit.
5. Create an access schedule. An access schedule consists of segments, each defined by a date range and associated with an amount. For example, set the access schedule to October 01, 2024 to October 01, 2025, matching the term of the contract.
6. (Optional) Create an invoice schedule. This determines the cadence to bill your customer for the commit.
   * You can bill your customer for any amount in any number of installments. For example, create two invoice schedule segments:
     * One segment on October 01, 2024 for \$4,000
     * Another segment on November 01, 2024 for \$6,000
   * To capture the invoiced amount without generating an invoice for downstream billing providers, select the **Do not invoice** option after entering the invoice amount.
7. Define the priority of the commit. If a customer has multiple credits or commits that could apply against usage, the priority dictates the order in which the credits and commits are consumed. Lower priority commits get consumed first.
8. (Optional) Specify the rollover percentage of the commit. In the case of a contract renewal, specify what percent of the initial balance of the commit should roll over to the new contract. Learn more about [contract transitions](/guides/customers-billing/manage-customers/manage-customer-lifecycle).

This example API call shows how to create a contract with the example prepaid commit:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
  "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
  "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
  "starting_at": "2024-10-01T00:00:00.000Z",
  "commits": [
    {
      "type": "prepaid",
      "product_id": "cc69a00a-fa8f-4ae6-afdb-703e63fb4777",
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
            "amount": 400000,
            "timestamp": "2024-10-01T00:00:00.000Z"
          },
          {
            "amount": 600000,
            "unit_price": 600000,
            "quantity": 1,
            "timestamp": "2024-11-01T00:00:00.000Z"
          }
        ]
      }
    }
  ]
}'
```

### Postpaid commits​

For postpaid commits, usage during the access period (defined by `access_schedule`) gets paid for in arrears. If the total amount paid during the access period is less than the committed amount, there’s a final true-up invoice on the `invoice_date`.

For example, if a customer has a contract with a postpaid commitment to spend \$10,000 over the one-year contract term from October 01, 2024 to October 01, 2025, billed monthly, each month, the customer gets billed in arrears for usage incurred in that month. At the end of the contract, the customer spent a total of \$9,000. On the specified `invoice_date`, a true-up invoice for \$1,000 is issued to reach the commitment of \$10,000.

To add a postpaid commit to a contract in the Metronome app:

1. When creating a contract, click **Add commit.**
2. Link the commit to a fixed product.
3. (Optional) Add an internal description explaining the reason for granting the commit.
4. (Optional) If the commit can only get consumed by a subset of usage, specify applicable product IDs or applicable product tags. If omitted, all usage, subscription, and composite charges can consume the commit.
5. Create an access schedule. By default, the access schedule is the term of the contract. You can allocate a proportion of spend to distinct time windows across the contract. In the example scenario, the access schedule is from October 01, 2024 to October 01, 2025.
6. Select the invoice date. The invoice date is the date when a true-up invoice gets issued if the actual spend falls short of the committed amount. By default, the invoice date is the end date of the contract, but you can customize it to any date after the access schedule. For the example scenario, the invoice date is October 01, 2025, the end date of the contract.
   * To capture the invoiced amount without generating an invoice for downstream billing providers, select the **Do not invoice** option after entering the invoice amount.
7. Define the priority of the commit. Prepaid commits and credits burn down first. If a customer has multiple postpaid commits that could apply against usage, the priority dictates the order in which the postpaid commits are consumed. Lower priority commits get consumed first.
8. (Optional) Specify the rollover percentage of the commit. In the case of a contract renewal, specify what percent of the initial balance of the commit should roll over to the new contract. Learn more about [contract transitions](/guides/customers-billing/manage-customers/manage-customer-lifecycle).

This example API call shows how to create a contract with the example postpaid commit:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
  "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
  "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
  "starting_at": "2024-10-01T00:00:00.000Z",
  "ending_before": "2025-10-01T00:00:00.000Z",
  "commits": [
    {
      "type": "postpaid",
      "product_id": "1cca616f-d6c7-44d3-b02d-cfcc85f97fd6",
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
            "amount": 1000000,
            "timestamp": "2025-10-01T00:00:00.000Z"
          }
        ]
      }
    }
  ]
}'
```

## Provision recurring usage credits​

As part of a subscription or contract, organizations commonly allocate a fixed amount of usage to a customer. The amount generally scales with the tier of the plan, such as Good, Better, and Best. Organizations adopt this model to get the benefits of subscription with fixed recurring revenue and usage-based billing with collecting on overages. Model this behavior in Metronome by setting up a recurring credit or commit on a contract.

### Configure recurring credits or commits​

Similar to how you can issue individual credits and commits, you can also schedule the release of credits and commits on a recurring basis. With recurring grants, a new credit or commit is issued with a unique ledger attached to it at the start of each period.

1. For free usage with a \$0 cost basis, create a recurring credit. For paid usage, create a recurring commit.
2. Specify the credit or commit product that generates the invoice line item for the recurring charge. This product’s metadata, such as custom fields, is passed through to the invoice where the commit or credit is applied.
3. Specify which products the grant should apply to. If left blank, it applies to all products. Use product tags for easier configuration.
4. Specify whether unused credits and commits expire at the end of each period by defining the `commit_duration`. You can roll over the total amount of credits remaining for a number of periods.
5. Optionally update the recurrence schedule. It defaults to the usage schedule defined on the contract.

<Info>
  **INFO**

  If a `recurrence_frequency` is set on the contract, the anchor date for the recurring commit will default to the `starting_at` of the commit. This means that if the contract start date and the recurring commit start date are distinct, the first period **will not** be prorated.
</Info>

6. Define proration behavior. If left null, the default behavior is prorate any grants that don't cover a full period (`FIRST_AND_LAST`).
7. Optionally, define rounding behavior when commit access and invoice schedules are prorated. This can be used to only grant and charge whole-number amounts, for example.
8. To issue commit charges on the same invoice as the contract’s usage statement, specify that usage and scheduled charges should [consolidate on the contract](/guides/customers-billing/manage-customers/provision-a-customer#consolidate-usage-and-scheduled-invoices).

### Upgrade or downgrade a customer’s contract​

Customers may upgrade or downgrade to new tiers after familiarizing themselves with your product. To facilitate this, create a new contract using a [contract renewal](/guides/customers-billing/manage-customers/manage-customer-lifecycle#contract-renewal). This ends the current contract and all future recurring charges and generates a new contract with updated terms. If a customer is entitled to maintain their existing balance as part of the upgrade or downgrade, specify a **Contract Transition Rollover** of 100% when creating the initial contract.

#### Upgrade at the start of new period​

To facilitate or schedule an upgrade at the start of a new billing period:

1. Create a new contract and set the start date to the start of the billing period. Specify the contract transition as a **Renewal** and pass the previous contract’s ID.
2. If a contract roll-over was specified for the recurring commit on the first contract, the remaining balance rolls over to the new contract based on this setting.

The future recurring charges from the first contract are removed. The new contract generates a `FINALIZED` scheduled invoice for the first recurring commit. It also generates a new `DRAFT` usage invoice to meter usage for the first month.

#### Upgrade mid-period​

To facilitate a mid-period upgrade:

1. Create a new contract and set the start date to today’s date. Specify the contract transition as a **Renewal** and pass the previous contract’s ID.
2. The commit amount for the first period will be prorated.
3. If a contract roll-over was specified for the recurring commit on the first contract, the remaining balance rolls over to the new contract based on this setting.

The `DRAFT` usage invoice on the first contract will finalize with the usage up to that date. The new contract generates a new `DRAFT` usage invoice to capture usage from the rest of the period and a `FINALIZED` scheduled invoice with the prorated charge for the first recurring commit.

#### Backdate an upgrade​

The benefit of backdating an upgrade is that the user only receives a single usage invoice during the billing period.

To backdate an upgrade:

1. Create a contract and set the start date to the first day of the current billing period. Specify the contract transition as a **Renewal** and pass the previous contract’s ID.
2. This finalizes the current `DRAFT` usage invoice from the first contract. The updated service period starts and ends on the same day, meaning that usage from the open period moves to the new contract.
3. On the new contract, create a on-time commit that represents the discounted amount for the first period. The amount should be *(prorated total) - (amount paid on first contract)*.
4. Create a recurring schedule that starts on the second period of the contract on a move-forward basis.

### Recurring credit example​

Consider an example where a customer signs up for your company’s lowest tier plan on January 1st. This free plan gives them access to \$10 in free credits each month and access to the Basic products. If the customer doesn’t use their credits each month, they expire at the start of the next month.

This example API call shows how to create the contract with a recurring free credit:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "<id>",
    "rate_card_id": "<id>",
    "starting_at": "2025-01-01T00:00:00Z",
    "name": "recurring-commit-contract",
    "commits": [],
    "custom_fields": {
        "contract_tier": "basic"
    }
    "recurring_credits": [
        {
            "name": "recurring credit",
            "description": "recurring credit",
            "product_id": "<id>",
            "access_amount": {
                "unit_price": 1000,
                "quantity": 1,
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2"
            },
            "priority": 1,
            "commit_duration": {
                "unit": "periods",
                "value": 1
            },
            "starting_at": "2024-12-01T00:00:00Z",
            "rollover_fraction": 100
        }
    ]
}'
```

After using the product for a few weeks, the customer decides to upgrade their plan on January 21st while they have \$2 in remaining balance. This new plan costs \$20 a month. It gives them a \$30 usage allotment each month and access to the Premium feature set. As part of the new plan, the customer can roll over the commits to the next period if they don’t use it all.

This example API call shows how to use a contract transition to create a new contract:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "<id>",
    "rate_card_id": "<id>",
    "starting_at": "2025-01-01T00:00:00Z",
    "name": "recurring-commit-contract",
    "commits": [],
    "custom_fields": {
        "contract_tier": "basic"
    },
    "recurring_commits": [
        {
            "name": "recurring commit",
            "description": "recurring commit",
            "product_id": "<id>",
            "access_amount": {
                "unit_price": 3000,
                "quantity": 1,
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2"
            },
            "priority": 1,
            "commit_duration": {
                "unit": "periods",
                "value": 2
            },
            "starting_at": "2024-12-01T00:00:00Z",
            "invoice_amount": {
                "unit_price": 2000,
                "quantity": 1,
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2"
            }
            "rollover_fraction": 100
        }
    ]
    "transition": {
        "from_contract_id": "<id of first contract>",
        "type": "renewal"
    }
}'
```

Once the new contract is provisioned, the customer has the following balance:

* \$2 in free usage rolled over from the first contract
* \$10 from a paid commit with a cost basis of 0.67

## How credits and commits work with invoices​

In Metronome, credits and commits are always applied against usage at a line-item level rather than the aggregate invoice level. This attribution creates the ability to more accurately recognize precommitted and overage spend against each product.

On an invoice, line items are separated based on whether the usage draws down a commit, a credit, or is in overage.

<Info>
  **INFO**

  The same usage can apply against only one commit or credit. For example, if you incurred \$500 of usage and have a contract encoded with a \$400 prepaid commit and a \$400 postpaid commit, the prepaid commit gets consumed first. \$400 of the usage fully consumes the prepaid commit. Then, the remaining \$100 counts toward fulfilling the postpaid commit. As postpaid commits get paid in arrears, the customer would still get charged \$100.
</Info>

This example invoice API response demonstrates a situation where a customer consumed \$10 of Data Storage during the billing period. Of the \$10, \$4 is covered by a prepaid commit, and \$6 is not covered by a credit or commit. In the invoice response, this results in 3 line items:

* Usage covered by the prepaid commit, with a total of \$4
* Commit application line item, with a total of -\$4
* Usage not covered by a prepaid commit or credit (”Overage” line item), with a total of \$6

```json theme={null}
{
  "data": {
    "billable_status": "billable",
    "contract_custom_fields": {},
    "contract_id": "222fd78f-c93d-4b11-bec8-a7b12b510214",
    "credit_type": {
      "id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
      "name": "USD (cents)"
    },
    "custom_fields": {},
    "customer_custom_fields": {},
    "customer_id": "b61bf255-d6f2-49fc-a062-b32431e2d22d",
    "end_timestamp": "2024-11-01T00:00:00+00:00",
    "external_invoice": null,
    "id": "e1937b93-64a5-5117-99e1-eb963a71e764",
    "issued_at": "2024-11-02T12:00:00+00:00",
    "line_items": [
      {
        "commit_custom_fields": {},
        "commit_id": "fde728f0-af26-45c3-92f6-7587dedadef3",
        "commit_segment_id": "fc696ca9-58b6-49e1-b2dc-888d78acd00e",
        "commit_type": "PrepaidCommit",
        "credit_type": {
          "id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
          "name": "USD (cents)"
        },
        "ending_before": "2024-11-01T00:00:00+00:00",
        "name": "Data Storage",
        "product_custom_fields": {},
        "product_id": "c8dccd54-0ca8-4580-861d-1e26854ab2f1",
        "product_type": "UsageProductListItem",
        "quantity": 4,
        "starting_at": "2024-10-01T00:00:00+00:00",
        "total": 400,
        "unit_price": 100
      },
      {
        "commit_custom_fields": {},
        "commit_id": "fde728f0-af26-45c3-92f6-7587dedadef3",
        "commit_netsuite_item_id": "1234",
        "commit_segment_id": "fc696ca9-58b6-49e1-b2dc-888d78acd00e",
        "commit_type": "PrepaidCommit",
        "credit_type": {
          "id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
          "name": "USD (cents)"
        },
        "ending_before": "2024-11-01T00:00:00+00:00",
        "name": "Prepaid Commit applied",
        "product_custom_fields": {},
        "product_id": "c8dccd54-0ca8-4580-861d-1e26854ab2f1",
        "product_type": "UsageProductListItem",
        "starting_at": "2024-10-01T00:00:00+00:00",
        "total": -400
      },
      {
        "credit_type": {
          "id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
          "name": "USD (cents)"
        },
        "ending_before": "2024-11-01T00:00:00+00:00",
        "name": "Data Storage",
        "product_custom_fields": {},
        "product_id": "c8dccd54-0ca8-4580-861d-1e26854ab2f1",
        "product_type": "UsageProductListItem",
        "quantity": 6,
        "starting_at": "2024-10-01T00:00:00+00:00",
        "total": 600,
        "unit_price": 100
      }
    ],
    "start_timestamp": "2024-10-01T00:00:00+00:00",
    "status": "DRAFT",
    "total": 600,
    "type": "USAGE"
  }
}
```
