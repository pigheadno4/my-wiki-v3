<!-- Source URL: https://docs.metronome.com/guides/reporting-insights/financial-reporting/revenue-recognition.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How revenue recognition works

Metronome powers usage-based business models by enabling pricing and packaging flexibility that support a broad range of business models and power a uniquely differentiated billing experience.

As a result, Metronome stores all of the raw data necessary to manage complex revenue recognition for usage-based business models. This includes maintaining detailed transaction history and ledgers to calculate deferred revenue, accrued revenue, and recognized revenue, all with daily granularity down to products and revenue categories. This data is available either through Metronome's APIs or Metronome [data export](/guides/reporting-insights/data-export).

Clients commonly use this data to:

* Integrate the data directly to a downstream system using Metronome APIs to automate revenue recognition
* Run data exports to create journal entries for posting to their enterprise resource planning (ERP) system

<Note>
  **INFO**

  Metronome does not create revenue journal entries.
</Note>

## Terminology

This section defines key terms and how they apply to Metronome's support of your usage-based business.

### Revenue reporting categories

Merchants frequently report recognized revenue in separate categories. The most common categories are:

* On-demand (pay-as-you-go) usage
* Prepaid commitment draw down
* Postpaid commitment draw down
* Overage usage
* Credit draw down

Within each category, revenue gets further broken down by product. This level of granularity allows merchants to track the performance of each go-to-market strategy, sales channel, and product offering.

### On-demand usage

On-demand usage refers to a pricing model where customers are charged based on their actual consumption, without any preset spending commitments.

Metronome issues invoices for on-demand consumption as it occurs. The merchant is entitled to recognize revenue immediately upon issuance of invoices for on-demand consumption.

### Commits

A commit refers to a customer's agreement or promise to consume a certain amount of a product or service over a specified period. This concept is common in enterprise sales for AI, cloud computing, and software-as-a-service (SaaS) industries.

Metronome supports two types of commits: prepaid and postpaid.

#### Prepaid commits

A prepaid commit refers to a customer's agreement to purchase commits (called prepaid credits) by making upfront payments. In exchange for the commitment, the customer may receive preferential terms, such as discounted draw down rates. Here's how revenue is allocated based on mechanics in Metronome:

* **Invoice for purchases**: Metronome issues invoices to the customer to collect payment for each purchase of a prepaid commit. The merchant is entitled to defer revenue associated to purchases of prepaid commits.
* **Draw down invoices**: Metronome issues invoices to draw down prepaid commit balances based on the customer's actual consumption each month during the commitment period. The merchant is entitled to recognize revenue as prepaid commits are drawn down.
* **Expiration handling**: Metronome expires any unused prepaid commits at the end of each commitment period (commit expirations are also referred to as "prepaid commit true-ups"). The merchant is entitled to recognize revenue when a prepaid commit has expired.

#### Postpaid commits

A postpaid commit refers to a customer's agreement to spend a minimum amount over a preset period of time. In exchange for the commitment, the customer may receive preferential terms, such as discounted draw down rates.

If the customer has not met the minimum spend amount by the end of the commitment period, a true-up invoice is issued for the difference between actual spending and the commitment amount.

* **Draw down process**: Metronome draws down the postpaid commit balance based on the customer's actual consumption each month during the commitment period. The merchant is entitled to recognize this usage as revenue as postpaid commits are drawn down.
* **True-up invoicing**: Metronome issues a true-up invoice to the customer at the end of the commitment period, if needed. The merchant is entitled to recognize revenue when true-up invoices are issued.

For more information on how to set up commits in Metronome, navigate to [Apply credits and commits](/guides/pricing-packaging/apply-credits-and-commits/create-a-pre-paid-commit).

### Overage

Overage refers to a customer's actual consumption spending that exceeds a preset commitment amount.

Metronome issues invoices for overages as soon as they occur. The merchant is entitled to recognize this overage as revenue when invoices are issued.

### Issue free credits

In Metronome, credits refer to free credits that are issued for free trials, promotions, SLA violations, concession credits, and similar use cases. These credits are always free and never paid for, whereas prepaid commits (sometimes referred to as "prepaid credits") are always paid for. Since credits are always free, they do not affect deferred revenue, but credit draw down may have a contra-revenue impact against recognized revenue.

### Billing in arrears versus billing in advance

All Metronome usage charges are billed in arrears, with monthly, quarterly, and annual as possible billing options. Since these charges are billed in arrears, they can be recognized as revenue immediately upon invoicing, and can be accrued as needed.

Metronome uses scheduled charges to issue invoices for prepaid commit purchases. Scheduled charges are billed in advance and are generally treated as deferred revenue upon invoicing.

### Accrued revenue

Accrued revenue refers to revenue that has been earned, but invoices have not yet been issued, or payment has not yet been received. Accrued revenue may also be called "earned but un-billed" revenue.

In Metronome, accrued revenue is represented by draft usage invoices, which are an accumulation of usage events that have been rated, but not yet invoiced.

## Metronome data model

To create the necessary queries for revenue recognition, it is important to first understand the Metronome data model. The ERD below shows a simplified view of the Metronome objects in data export that contain the relevant information for revenue recognition.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/TrrblT2KR7zYyGbN/images/docs/Invoices/rev-rec-model-29b0978437f475f196f6547b833ba134.png?fit=max&auto=format&n=TrrblT2KR7zYyGbN&q=85&s=29134d9f141a47dc97cc5606c28fc67a" alt="Metronome revenue recognition data model" width="2574" height="1088" data-path="images/docs/Invoices/rev-rec-model-29b0978437f475f196f6547b833ba134.png" />
</Frame>

### Key data model relationships

1. Each credit has a credit ledger. The credit ledger entry types relevant to revenue recognition are:
   * `credit_automated_invoice_deduction` represents a reduction of the credit balance from an invoice
     * If reporting on revenue from `line_items`, ignore this ledger entry type as revenue is already included from `line_items` where `invoices.type` = `CONTRACT_USAGE`
   * `credit_segment_expiration` represents the expiration of the credit balance segment (aka true-up)
     * This ledger entry is usually ignored as credit expirations do not impact revenue

2. Each commit has a commit ledger. The commit ledger entry types relevant to revenue recognition are:
   * `prepaid_automated_invoice_deduction` represents a reduction of the prepaid commit balance from an invoice
     * If reporting on revenue from `line_items`, ignore this ledger entry type as revenue is already included from `line_items` where `invoices.type` = `CONTRACT_USAGE`
   * `prepaid_segment_expiration` represents the expiration of the prepaid commit balance segment
     * Always recognize revenue from this ledger entry as prepaid expirations are not invoiced by Metronome
   * `postpaid_automated_invoice_deduction` represents a reduction of the postpaid commit balance from an invoice
     * If reporting on revenue from `line_items`, ignore this ledger entry type as revenue is already included from `line_items` where `invoices.type` = `CONTRACT_TRUEUP`
   * `postpaid_trueup` represents a true-up invoice that was issued for this postpaid commit to invoice for the remainder of the postpaid commit balance
     * If reporting on revenue from `line_items`, ignore this ledger entry type as amounts are duplicated

3. In data export, `credits` and `commits` objects are consolidated into the `balances` object to simplify reporting.

4. Metronome creates different invoice types based on the type of charges that are invoiced:
   * When `invoices.type = 'CONTRACT_SCHEDULED'`, the invoice contains scheduled charges, including prepaid commit purchases
   * When `invoices.type = 'CONTRACT_USAGE'`, the invoice contains usage charges
   * When `invoices.type = 'CONTRACT_TRUEUP'`, the invoice contains true-up charges for postpaid commits

5. Each invoice has one or more line items, which indicate the amount of revenue to recognize:
   * `invoices.credit_type_id` indicates the billing currency (for example, USD cents)
   * `invoices.start_timestamp` and `invoices.end_timestamp` indicate the service period
     * The Metronome service period determines the target accounting period in the ERP system
   * `line_items.product_id` indicates which product is being invoiced
     * `line_items.product_id` is mapped to a SKU or line item ID in the ERP system
   * If `line_items.commit_id` is populated, a credit or commit has been applied to the line item
     * Join `line_items` to `balances` (`line_items.commit_id = balances.id`) to fetch `balances.type`
     * `balances.type` determines whether line item amount should be categorized as credit, prepaid commit, or postpaid commit revenue
     * The enumerations for `balances.type` are: `credit`, `prepaid`, or `postpaid`
   * If `line_items.commit_id` is null, this indicates the line item amount should be categorized as either on-demand (pay-as-you-go) or overage revenue
     * Use metadata (client defined) on the `contracts` or `commits` objects to differentiate on-demand (pay-as-you-go) versus overage revenue

6. Querying invoices where `status = 'FINALIZED'` will produce a report of recognized revenue

7. Querying invoices where `status = 'DRAFT'` will produce a report of accrued revenue

<Note>
  **INFO**

  Data export will transfer two distinct invoice tables - one for finalized and one for draft invoices.
</Note>
