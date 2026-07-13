<!-- Source URL: https://docs.metronome.com/guides/reporting-insights/financial-reporting/reconcile-data.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reconcile data

Data reconciliation is a key step in most finance workflows wherein you verify that two sets of records are in agreement for a given time period. These workflows typically occur when closing an accounting period, before revenue is recognized in downstream systems.

Performing data reconciliation ensures that data is completely and accurately transmitted across systems. Further, the due diligence guarantees that you correctly invoice your customers and recognize the correct revenue.

Given that Metronome stores all of your contract, usage, and pricing information, Metronome is uniquely suited to power this process. Your Metronome data can be reconciled against:

* Salesforce
* Stripe
* Your own internal system
* Third-party data warehouses

Metronome provides two tools for performing data reconciliation: data exports and the API.

## Reconcile against data exports

Metronome enables you to programmatically export your data to your existing data warehouse using [data export](/guides/reporting-insights/data-export). Data exports are a more efficient way to export larger quantities of data all at once, as opposed to repeatedly calling the API.

The data exported from Metronome to your data warehouse can be queried to produce reports that compare an internal or external system to Metronome. A key part of enabling this comparison is foreign key mapping. Foreign keys enable you to map an entity in one system to another based on the primary keys in both tables. [Custom fields](/developer-resources/custom-fields/) provide the most common way to do this. Through foreign key mapping, you can compare whether a deal closed in SFDC exactly matches what's stored in Metronome. This includes things like the contract start and end dates, the commit amount, or custom negotiated discounts. You can also use data export to check that the finalized invoice amount in Metronome matches exactly what was invoiced with your invoice provider.

Metronome's data export ensures that you have a reliable mechanism to receive all of your data and that it's structured in such a way that can be reconciled to the other systems that connect to Metronome.

## Data export reconciliation examples

Imagine your organization uses Salesforce CPQ to store customer and deal information, Metronome for processing your usage based billing, and Stripe as your invoice provider.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/TrrblT2KR7zYyGbN/images/docs/Invoices/data-rec-process-6f80e025db48f6dc8cc46fe923c5ad9f.png?fit=max&auto=format&n=TrrblT2KR7zYyGbN&q=85&s=3fb440126fe60c3e22765c77dcc179c1" alt="Data reconciliation workflow diagram" width="2860" height="1320" data-path="images/docs/Invoices/data-rec-process-6f80e025db48f6dc8cc46fe923c5ad9f.png" />
</Frame>

As depicted above:

* Salesforce and Metronome are integrated so that when a new customer and contract is created in Salesforce it is also created within Metronome.
* Metronome begins metering the usage once the customer and contract is created from the Salesforce integration. At the end of the invoice period, Metronome sends the finalized invoices to Stripe so they can be billed to the end customer.
* Additionally, Metronome regularly exports snapshots of data to your data warehouse for your reconciliation needs as covered below.

### Contract reconciliation

To begin your data reconciliation, confirm that the customer and contract information in Metronome exactly matches what is contained within your Salesforce CPQ instance. Using Metronome's data exports, information like the start and end dates, commit details, and price overrides for your customers' contracts are exported directly to your data warehouse for you to cross check against SFDC.

A common method that customers use to match the contract in Metronome to the corresponding contract in SFDC is to create a custom field on the contract that holds the SFDC opportunity ID. To verify that the Metronome contract information matches SFDC you would use a query like the following and match the SFDC opportunity ID stored as a custom field on the Metronome contract to the entry within your SFDC instance:

```sql theme={null}
-- from the most recent view of your contracts,
WITH max_contract_snapshot AS (
    SELECT 
         max(snapshot_id) AS max_snapshot_id
    FROM "contracts_contracts"
)
-- find that contract by ID
SELECT *
FROM "contracts_contracts"
WHERE id = '[insert Metronome contract id]'
AND snapshot_id = (SELECT max_snapshot_id FROM max_contract_snapshot);
```

Similar to the example above, you also want to confirm that the commit created in Metronome matches the commit details that are stored within SFDC as part of your reconciliation flow. To find the contract's most recent commit information in Metronome (access schedule, invoice schedule, total amount) in data export, you would use a query like the following and again use the SFDC opportunity ID as the key to match on:

```sql theme={null}
WITH max_commit_snapshot AS (
    SELECT 
         max(snapshot_id) AS max_snapshot_id
    FROM "contracts_commits"
)     
SELECT *
FROM "contracts_commits"
WHERE id = '[insert Metronome commit id]'
AND snapshot_id = (SELECT max_snapshot_id FROM max_commit_snapshot);
```

Additionally, within SFDC, you may have custom terms that were negotiated with a customer that are represented in Metronome as contract overrides. As part of your reconciliation workflow, you want to crosscheck that the overrides created in Metronome match the custom terms that were entered within SFDC when the deal was closed. To find the current overrides on the contract in data export, you would use a query like the following and use the SFDC opportunity ID as the key to match on:

```sql theme={null}
WITH max_overrides_snapshot AS (
    SELECT 
         max(snapshot_id) AS max_snapshot_id
    FROM "contracts_overrides"
)      
SELECT *
FROM "contracts_overrides"
WHERE contract_id = '[insert Metronome contract id]'
AND snapshot_id = (SELECT max_snapshot_id FROM max_overrides_snapshot);
```

### Invoice reconciliation

Now that you have verified that the customer's contract information in Metronome matches what is in SFDC, you can move to the next step in your reconciliation workflows: reconciling finalized invoices in Metronome against Stripe. To reconcile the finalized invoices within Metronome, you would find the customer's most recent finalized invoice for the customer in data export using a query like the following and then match that to the record in Stripe to compare relevant details:

```sql theme={null}
SELECT *
FROM "invoice"
WHERE customer_id = '[insert Metronome customer ID]'
AND status = 'FINALIZED'
ORDER BY end_timestamp DESC
LIMIT 1;
```

## Reconcile against the API

Alternatively, you can power reconciliation workflows by pulling data from the Metronome API. The API allows you to query the common objects necessary for reconciliation—contracts, customers, invoices, and so on—through their LIST endpoints.

Although Metronome suggests using Data Export for reconciliation, the API provides users with lower latency access to information. This enables business users to create real-time dashboards that highlight changes as you make them.
