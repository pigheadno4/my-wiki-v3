<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/make-pricing-changes/edit-contract.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Edit a contract

The ability to edit a contract helps you react quickly to the needs of your customers and your business. When a customer's contract needs updating to reflect a mid-term up-sell or to correct an error, you can edit terms on a contract through the Metronome UI or through the API with the `editContract` endpoint.

When you edit a contract, any draft invoices update immediately to reflect that edit. Finalized invoices remain unchanged. If you void and regenerate a finalized invoice, the regenerated invoice updates to reflect the edits you made.

## Contract editing examples

This section describes example contract editing scenarios for a company named BigData.

### Edit the access schedule and invoice schedule for a commit

In this example, BigData’s customer initially negotiated a 2-year SLG contract with a \$100K prepaid commit applicable for the first year. The contract started on January 1, 2025 and spans until January 1, 2027.

After only 6 months, they’ve used the product very quickly and only have \$10K left on their commit. They reach out and negotiate new terms. They’ve doubled their commit amount to \$200K, but now have the full 2-year contract term to consume \$200K.

To implement this change in Metronome, BigData:

* Increases the amount of the access schedule segment to \$200K
* Extends the `ending_before` date to the end of the contract term
* Adds another invoice schedule segment to charge the customer now for the additional \$100K commit

This example API call shows the described contract edit:

```bash theme={null}
curl https://api.metronome.com/v2/contracts/edit \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
        "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
        "contract_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        "update_commits": [
            {
                "commit_id": "2e30f074-d04c-412e-a134-851ebfa5ceb2",
                "access_schedule": {
                    "update_schedule_items": [
                        {
                            "id": "d38a8230-3614-46f9-82c6-82e53ac630d6",
                            "amount": 20000000,
                            "ending_before": "2027-01-01T00:00:00.000Z"
                        }
                    ]
                },
                "invoice_schedule": {
                    "add_schedule_items": [
                        {
                            "timestamp": "2025-07-01T00:00:00.000Z",
                            "amount": 10000000
                        }
                    ]
                }
            }
        ]
    }'
```

### Edit the applicable product IDs for a commit

In this example, a customer’s contract includes a product-specific prepaid commitment named Commit A. Only the usage of the Data Reads product is eligible to consume their commitment.

The finalized February 2025 invoice includes usage of Data Reads and Data Writes products. Only Data Reads consumes the prepaid commitment.

| Product     | Applied commit or credit | Price | Quantity | Total |
| :---------- | :----------------------- | :---- | :------- | :---- |
| Data Reads  | Commit A                 | \$10  | 10       | \$100 |
| Data Writes |                          | \$5   | 10       | \$50  |
|             |                          |       | Total    | \$50  |

The draft March 2025 invoice also includes usage of Data Reads and Data Writes. Again, only Data Reads consumes the prepaid commitment.

| Product     | Applied commit or credit | Price | Quantity | Total |
| :---------- | :----------------------- | :---- | :------- | :---- |
| Data Reads  | Commit A                 | \$10  | 3        | \$30  |
| Data Writes |                          | \$5   | 2        | \$10  |
|             |                          |       | Total    | \$10  |

The customer then negotiates a mid-term change to their contract, where Data Writes is now eligible to burn down these commits, starting with the March 2025 billing period.

This example API call from March 5, 2025 edits the applicable product IDs associated with the commitment to add Data Reads and Writes.

```bash theme={null}
curl https://api.metronome.com/v2/contracts/edit \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
        "customer_id": "40f388e0-3fa8-4b4f-b4c8-b5a7a97fdb48",
        "contract_id": "323cdf39-678a-49b8-a6ce-5c4b1e108b9c",
        "update_commits": [
            {
                "commit_id": "d0d1472b-e63a-46d2-b9cb-036cd57db7e6",
                "applicable_product_ids": [
                    "f3a30bcb-e35a-4409-b20b-45b33efc459d",
                    "4ef215cd-0bee-4518-93c9-4caf76cb3db9"
                ]
            }
        ]
    }'
```

The draft March 2025 invoice immediately reflects the change to the applicable product IDs. For the whole billing period, Commit A can now draw down both Data Reads and Data Writes.

| Product     | Applied commit or credit | Price | Quantity | Total |
| :---------- | :----------------------- | :---- | :------- | :---- |
| Data Reads  | Commit A                 | \$10  | 3        | \$30  |
| Data Writes | Commit A                 | \$5   | 2        | \$10  |
|             |                          |       | Total    | \$0   |

The finalized February 2025 invoice remains untouched.

| Product     | Applied commit or credit | Price | Quantity | Total |
| :---------- | :----------------------- | :---- | :------- | :---- |
| Data Reads  | Commit A                 | \$10  | 10       | \$100 |
| Data Writes |                          | \$5   | 10       | \$50  |
|             |                          |       | Total    | \$50  |

If the client had voided and regenerated the month 1 invoice, Commit A would apply to both Data Reads and Data Writes, based on the current state of the contract.

## Track edits over time

View a contract’s history to track all changes and edits made over time.

The `getEditHistory` endpoint returns all edits ever made to a contract. This includes any edits made through:

* The `editContract` endpoint
* The `updateEndDate` API endpoint
* Adding usage filters with the `setUsageFilters` endpoint
* The Metronome UI

Here’s an example response from getEditHistory. This response shows that the contract was edited twice: once to add an override and once to add a commit.

```json theme={null}
{
    "data": [
        {
            "add_overrides": [
                {
                    "applicable_product_tags": [],
                    "id": "80c8e124-a4fb-4264-b2e6-ac2479d075dc",
                    "is_commit_specific": false,
                    "multiplier": 0.5,
                    "override_specifiers": [
                        {
                            "product_id": "90c47b63-8095-4369-9779-c65cc4fe3af7"
                        }
                    ],
                    "product": {
                        "id": "90c47b63-8095-4369-9779-c65cc4fe3af7",
                        "name": "Reads"
                    },
                    "starting_at": "2025-02-01T00:00:00+00:00",
                    "type": "MULTIPLIER"
                }
            ],
            "id": "a19c750a-ffe4-57ae-9645-cb8682904afb",
            "timestamp": "2025-02-26T23:07:00.727000+00:00"
        },
        {
            "add_commits": [
                {
                    "access_schedule": {
                        "credit_type": {
                            "id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                            "name": "USD (cents)"
                        },
                        "schedule_items": [
                            {
                                "amount": 10000,
                                "ending_before": "2025-03-01T00:00:00+00:00",
                                "id": "11980e47-96b5-4527-bb38-149edc205c34",
                                "starting_at": "2025-02-01T00:00:00+00:00"
                            }
                        ]
                    },
                    "id": "e647c959-9eeb-49d2-ac21-2f2141e3e1fd",
                    "invoice_schedule": {
                        "credit_type": {
                            "id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                            "name": "USD (cents)"
                        },
                        "schedule_items": [
                            {
                                "amount": 10000,
                                "id": "c5cb2f25-fa4e-4ff6-9cdd-ff5edfe73acc",
                                "invoice_id": "0ce97fbd-d19f-52c8-80d6-4b877ad31177",
                                "quantity": 1,
                                "timestamp": "2025-02-01T00:00:00+00:00",
                                "unit_price": 10000
                            }
                        ]
                    },
                    "priority": 100,
                    "product": {
                        "id": "35a467c7-fc24-46c2-884b-66af8d349674",
                        "name": "Support"
                    },
                    "rate_type": "LIST_RATE",
                    "type": "PREPAID"
                }
            ],
            "id": "0551864c-edc7-5045-bcec-3688b4d53c3f",
            "timestamp": "2025-02-26T23:07:16.031000+00:00"
        }
    ]
}
```

To view the full state of a contract at any historical point, use the `as_of_date` parameter on the `getContract` endpoint.

This example response shows the full state of the contract after the first edit but before the second edit. It takes the `created_at` time for the first edit and passes that into the `as_of_date` parameter in `getContract`.

```json theme={null}
{
    "data": {
        "commits": [],
        "created_at": "2025-02-26T23:06:32.574000+00:00",
        "created_by": "User",
        "credits": [],
        "custom_fields": {},
        "customer_id": "d0d1472b-e63a-46d2-b9cb-036cd57db7e6",
        "id": "c5e8d83b-23e7-4747-a5fe-8a33f4404fe1",
        "multiplier_override_prioritization": "LOWEST_MULTIPLIER",
        "name": "test rate card",
        "overrides": [
            {
                "applicable_product_tags": [],
                "id": "80c8e124-a4fb-4264-b2e6-ac2479d075dc",
                "is_commit_specific": false,
                "multiplier": 0.5,
                "override_specifiers": [
                    {
                        "product_id": "90c47b63-8095-4369-9779-c65cc4fe3af7"
                    }
                ],
                "product": {
                    "id": "90c47b63-8095-4369-9779-c65cc4fe3af7",
                    "name": "Reads"
                },
                "starting_at": "2025-02-01T00:00:00+00:00",
                "type": "MULTIPLIER"
            }
        ],
        "rate_card_id": "c38bc471-0c45-41d1-b802-0bae4554e771",
        "recurring_commits": [],
        "recurring_credits": [],
        "scheduled_charges": [],
        "starting_at": "2025-02-01T00:00:00+00:00",
        "transitions": [],
        "usage_filter": [],
        "usage_statement_schedule": {
            "billing_anchor_date": "2025-02-01T00:00:00+00:00",
            "frequency": "MONTHLY"
        }
    }
}
```

<Tip>
  **TIP**

  All edits to a contract are also recorded in the Metronome audit logs, available in the Metronome UI and through the API.
</Tip>

## Supported Edits

Currently, the following edits are supported:

* Adding new commits
* Editing Commit access and invoice schedules
* Editing Commit name and description
* Editing Applicable product IDs and Applicable product tags on commits
* Editing Rollover fraction on commits
* Archiving commits
* Adding new recurring commits
* Editing ending\_before, the invoice amount, and the access amount on recurring commits
* Adding new credits
* Editing credit access schedules
* Editing Credit name and description
* Editing Applicable product IDs and Applicable product tags on credits
* Adding new recurring credits
* Archiving credits
* Editing ending\_before and the access amount on recurring credits
* Adding new overrides
* Removing overrides
* Adding new scheduled charges
* Editing scheduled charge invoice schedules
* Archiving scheduled charges
* Adding spend threshold configuration
* Updating spend threshold configuration
* Updating contract end date
* Updating contract name

## Limitations

The contract editing feature has these guardrails.

**Commit and scheduled charge invoice schedules**

* If the invoice schedule item is associated with a *finalized invoice* , you cannot remove or update the invoice schedule item.
* If the invoice schedule item is associated with a *voided invoice* , you cannot remove the invoice schedule item.

**Commit and credit access schedules**

* You cannot remove an access schedule segment that was applied to a finalized invoice. You can void the invoice beforehand *and then* remove the access schedule segment.
* If you remove an access schedule segment, its manual ledger entry is also removed.
* If you change the access schedule of a commit or credit, any draft invoices reflects the change in access schedule immediately. Finalized invoices remain untouched. If you void and regenerate the finalized invoices, the regenerated invoices reflect the new access schedule of the credit or commit.

**Rollover commits**

* You cannot edit rollover commits.
* You can edit the access schedule of the originating commit until the contract it was transitioned to has a finalized invoice.
* You can edit the invoice schedule of the originating commit until the original contract has ended.

**Finalized scheduled invoices**

Consider a scenario where you add a new invoice schedule item on timestamp X, or edit the timestamp for an invoice schedule item to date X. In the case where there’s already a finalized scheduled invoice for that timestamp, that finalized scheduled invoice remains untouched. Metronome creates a new finalized scheduled invoice for the edited invoice schedule items.

**Archiving terms**

* Before archiving a commit, all finalized usage invoices that the commit was applied to must be voided. Any finalized invoices for commit payment must also be voided.
* Before archiving a credit, all finalized usage invoices that the credit was applied to must be voided.
* Before archiving a scheduled charge, all finalized invoices created by the scheduled charge must be voided.
