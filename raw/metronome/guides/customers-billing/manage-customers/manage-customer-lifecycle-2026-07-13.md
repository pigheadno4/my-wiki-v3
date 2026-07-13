<!-- Source URL: https://docs.metronome.com/guides/customers-billing/manage-customers/manage-customer-lifecycle.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage contract lifecycle transitions

This use case walks through examples of how to use Metronome to manage contract lifecycle transitions.

Contract lifecycle transitions happen when the relationship between a business and their customers changes. For example, after the initial signing of a deal, alterations like mid-term upsells, renewals, and the contract's expiration can occur.

Metronome helps you manage the contract lifecycle, including the frictionless transitions between contract states. To support pricing and packaging flexibility for your organization, you can:

* Create contracts that fully capture the agreed upon terms, pricing, and schedule
* Update contracts to reflect new terms, upsells, downgrades, or new product launches
* Conclude complex contracts and gate product usage
* View a clear audit log of all contract lifecycle changes

The examples on this page show how Metronome supports contract lifecycle management through the lens of different sales motions.

## Create an enterprise contract motion

The terms of an enterprise contract can vary from one customer to another. Terms could include special access to non-public products, discounts on SKU-level list pricing, prepaid or postpaid commitments, and so on. Metronome supports an array of pricing and packaging motions, empowering your sales team to offer tailored deals without requiring IT or others to update the billing system. Metronome also powers your product entitlements workflow, ensuring that only a customer with an active contract can use your company's products and services.

For example, your organization's sales team just offered a 1 year enterprise contract to a company named Moogle. The terms of the deal are a \$100,000 prepaid commitment for the right to use Product A starting on January 1st, 2025, with a discount of 10% off Product A's standard list price.

To support this use case in Metronome:

1. Configure billable metrics to properly aggregate your customer’s usage.
2. Create products that represent the SKUs you’ll invoicing your customers for.
3. Set up a rate card to define your products’ standard pricing and entitlement.
4. Set up an integration with a downstream invoice provider like Stripe to support billing the customer.
5. Create a customer object representing Moogle.
6. Create a contract in Metronome associated with Moogle.

You can create the contract with the [/contracts/create API](/api-reference/contracts/create-a-contract):

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "450f7264-9b3d-43d5-8ee1-fc369a144c01",
    "name": "Enterprise Contract",
    "uniqueness_key": "1234",
    "rate_card_id": "6f06fad5-d017-4674-8b7f-1e00a1208109",
    "starting_at": "2025-01-01T00:00:00Z",
    "ending_before": "2026-01-01T00:00:00Z",
    "commits": [
      {
        "type": "prepaid",
        "name": "Prepaid Commit Moogle",
        "product_id": "7bb1bdf6-e4af-42e0-be27-3cde86056919",
        "access_schedule": {
          "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
          "schedule_items": [
            {
              "amount": 1000000,
              "starting_at": "2025-01-01T00:00:00Z",
              "ending_before": "2026-01-01T00:00:00Z"
            }
          ]
        },
        "invoice_schedule": {
          "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
          "schedule_items": [
            {
              "amount": 1000000,
              "timestamp": "2025-01-01T00:00:00Z"
            }
          ]
        },
        "rollover_fraction": 0.5,
        "priority": 100,
        "applicable_product_ids": ["d6695114-299b-4bd7-b57c-7a9134ba50ae"]
      }
    ],
    "overrides": [
      {
        "starting_at": "2025-01-01T00:00:00Z",
        "ending_before": "2026-01-01T00:00:00Z",
        "entitled": true,
        "type": "multiplier",
        "multiplier": 0.9,
        "product_id": "d6695114-299b-4bd7-b57c-7a9134ba50ae"
      }
    ]
  }'
```

After creating the contract, power your entitlement workflows with the `/contracts/get` API. For example, use the `/contracts/get` API to confirm Moogle's contract is active before allowing them to use Product A.

## Mid-term add-ons and renewals motion

Opportunities often arise to capture more value from an existing business relationship. This typically manifests in the form of mid-term add-ons to an active contract, including access to new SKUs, new monetary commitments with variable list price discounting, and early contract renewals. Metronome helps your sales team capitalize on opportunities as they arise, enables your product teams to roll out and charge for new features, and saves your IT team from the stress of managing frequent and complex contractual changes.

### Execute a mid-term add-on

Your company plans to beta launch Product B on October 1st, 2025. You offer a 20% discounted rate to your customer named Moogle in exchange for a new \$10,000 prepaid commitment. This \$10,000 prepaid commitment would only apply to use of Product B, and would begin on October 1st, 2025.

To support this use case in Metronome:

1. Create a usage-based product representing Product B.

2. Update the existing rate card to include Product B with your list pricing and default entitlement. Set Product B's entitlement to **false** by default. This ensures that only customers with access to Product B are charged for its usage.

3. Edit the existing Moogle contract to:
   * Change Product B's entitlement to **true**, scheduled for October 1st, 2025

   * Add a new prepaid commit to the existing contract for \$10,000 scheduled for October 1st, 2025, configured so that only usage for Product B gets drawn down

   * Override the list rate for Product B to give a 20% discount to Moogle

Edit the contract with the [/contracts/edit API](/api-reference/contracts/edit-a-contract):

```bash theme={null}
curl https://api.metronome.com/v2/contracts/edit \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "450f7264-9b3d-43d5-8ee1-fc369a144c01",
    "contract_id": "7b347536-56ac-4036-b5d1-67142b0d00e5",
    "add_commits": [
      {
        "type": "prepaid",
        "name": "mid-term prepaid commit",
        "product_id": "7bb1bdf6-e4af-42e0-be27-3cde86056919",
        "access_schedule": {
          "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
          "schedule_items": [
            {
              "amount": 1000000,
              "starting_at": "2025-10-01T00:00:00Z",
              "ending_before": "2026-01-01T00:00:00Z"
            }
          ]
        },
        "invoice_schedule": {
          "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
          "schedule_items": [
            {
              "amount": 1000000,
              "timestamp": "2025-10-01T00:00:00Z"
            }
          ]
        },
        "rollover_fraction": 0.5,
        "priority": 100,
        "applicable_product_ids": ["f0608ff2-30b6-4010-b2a6-bada4296b8a0"]
      }
    ],
    "add_overrides": [
      {
        "starting_at": "2025-10-01T00:00:00Z",
        "ending_before": "2026-01-01T00:00:00Z",
        "type": "multiplier",
        "multiplier": 0.8,
        "product_id": "f0608ff2-30b6-4010-b2a6-bada4296b8a0",
        "entitled": true
      }
    ]
  }'
```

### Contract renewal

Imagine it's now December 1st, 2025, meaning that Moogle has 1 month left on their existing contract. They're mostly satisfied with your services, and want to renew their contract to begin on January 1st, 2026 for another year. However, Moogle still has \$10,000 of prepaid commit remaining for Product A. Per the initial contract's details, the rollover percentage was set to 50% of the original balance in the event of a renewal. As \$10,000 is less than 50% of \$100,000, all \$10,000 of the remaining commit will roll over. Moogle likes this agreement, and renews with an additional \$200,000 prepaid commit for the combined usage of Product A and Product B.

To support this use case in Metronome, create a new contract scheduled to begin on January 1st, 2026:

1. Assign the contract transition type **renewal** and link to the previous contract.
2. Add a prepaid commitment for \$200,000 configured to burn down as Product A and Product B get used.
3. Assume that one \$200,000 invoice gets sent on the contract start date (Jan 1st, 2026).

On January 1st, 2026, the remaining \$10,000 in prepaid commit for Product A's usage rolls over to the new contract. This means that Moogle has two commits: one \$10,000 rollover commit solely for Product A's usage, and one \$200,000 prepaid commit for both Product A and Product B's usage. On this new contract, the \$10,000 rollover commit gets burned down first, before the \$200,000 commit is used.

Complete the renewal with the `/contracts/create` API:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "450f7264-9b3d-43d5-8ee1-fc369a144c01",
    "name": "Enterprise Contract Renewal",
    "uniqueness_key": "12345",
    "rate_card_id": "6f06fad5-d017-4674-8b7f-1e00a1208109",
    "starting_at": "2026-01-01T00:00:00Z",
    "ending_before": "2027-01-01T00:00:00Z",
    "commits": [
      {
        "type": "prepaid",
        "name": "renewal prepaid commit",
        "product_id": "7bb1bdf6-e4af-42e0-be27-3cde86056919",
        "access_schedule": {
          "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
          "schedule_items": [
            {
              "amount": 20000000,
              "starting_at": "2026-01-01T00:00:00Z",
              "ending_before": "2027-01-01T00:00:00Z"
            }
          ]
        },
        "invoice_schedule": {
          "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
          "schedule_items": [
            {
              "amount": 20000000,
              "timestamp": "2026-01-01T00:00:00Z"
            }
          ]
        },
        "rollover_fraction": 0.5,
        "priority": 101,
        "applicable_product_ids": [
          "d6695114-299b-4bd7-b57c-7a9134ba50ae",
          "f0608ff2-30b6-4010-b2a6-bada4296b8a0"
        ]
      }
    ],
    "transition": {
      "type": "renewal",
      "from_contract_id": "7b347536-56ac-4036-b5d1-67142b0d00e5"
    }
  }'
```

## End a contract motion

The end of a business relationship involves two critical tasks: ensuring the financial obligations stated in the contract are met, and that access to your company's products and services get quickly gated. Metronome supports both requirements, as the system automatically tracks the contract's terms in relation to your customer's usage and offers features to power your product entitlements workflow. This means that if a contract concludes before the expected end date, the client receives an invoice for their remaining financial obligations while simultaneously sending a signal to your product entitlements system that the customer is no longer active.

For example, Moogle decides to part ways with your company before using their entire prepaid commitment, and wants to exit the renewed contract on March 1st, 2026.

To support this use case in Metronome:

1. Schedule the end date of the existing contract to be effective on March 1st, 2026.

2. Ensure that you gate access to your product at the time of contract end:

   * Set up an [alert](/guides/customers-billing/set-up-notifications/create-and-manage-notifications) to generate a webhook upon a commit reaching a low balance (in this case, \$0.00)
   * Configure your entitlement system to listen for the webhook and immediately gate access

As this customer was invoiced for the prepaid commit at the time of contract start (January 1st, 2026), they already received their \$200,000 bill from your invoice provider. On March 1st, 2026, the contract's remaining prepaid commit goes to \$0.00.

Update the contract end date with the [/contracts/updateEndDate API](/api-reference/contracts/update-the-contract-end-date):

```bash theme={null}
curl https://api.metronome.com/v1/contracts/updateEndDate \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "450f7264-9b3d-43d5-8ee1-fc369a144c01",
    "contract_id": "7b347536-56ac-4036-b5d1-67142b0d00e5",
    "ending_before": "2026-03-01T00:00:00Z"
  }'
```
