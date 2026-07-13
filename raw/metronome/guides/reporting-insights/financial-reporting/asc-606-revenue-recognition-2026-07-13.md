<!-- Source URL: https://docs.metronome.com/guides/reporting-insights/financial-reporting/asc-606-revenue-recognition.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ASC 606 revenue recognition guide for usage companies

This guide explains U.S. GAAP's ASC 606 Revenue from Contracts with Customers in practical terms and helps illustrate how each step of the standard connects to Metronome's data model and product features. Our goal is to ensure every product decision, from data schema design to reporting output, supports customers' ability to comply with ASC 606 with minimal manual work.

Metronome directly impacts your ability to comply with ASC 606 because:

* We capture usage and billing data that feed into your revenue recognition process
* Our ability to map charges to obligations, track contract changes, and provide granular event data makes us a key system of record
* By mapping our data structure to ASC 606, we eliminate manual steps for you and better align our platform with your needs

<Warning>
  **Disclaimer**

  This guide is provided for informational purposes only. While Metronome provides data, reporting, and system capabilities that can support you in applying revenue recognition principles, Metronome itself is not a revenue recognition platform and does not generate revenue journal entries or make accounting determinations. Revenue recognition outcomes depend on your specific contracts, policies, and interpretations of accounting standards. The examples and scenarios described in this guide are intended to illustrate how Metronome's features and data may be used, but they should not be taken as prescriptive guidance.

  You are solely responsible for determining and applying your revenue recognition policies. Metronome recommends that you consult with qualified accounting and revenue recognition professionals to ensure compliance with applicable standards.
</Warning>

## Data model and reporting principles for ASC 606

Metronome is purpose-built to serve the needs of modern, usage-based, and hybrid SaaS businesses. It goes beyond traditional billing engines by providing real-time infrastructure, fine-grained data models, and flexible commercial constructs—all of which support scalable and compliant revenue recognition under ASC 606.

To support the revenue recognition process, our platform follows these principles:

### Comprehensive data

Metronome provides the raw and structured data needed to manage complex revenue recognition and support audit-ready reporting and analytics. This data includes:

* Full transaction history and ledger-level entries
* Daily granularity of usage and service delivery
* Breakdowns by product, customer, commitment, and revenue category

### Granularity and period-specific data

Metronome captures detailed transaction history and ledgers with daily granularity down to products and revenue categories, including:

* Tracking prepaid commits, postpaid draws and true-ups
* Free credits or promotional discounts

This allows for period-specific, detailed data essential for revenue recognition and audit support.

### Comprehensive contract and pricing management

Metronome maintains a centralized contract object containing pricing, terms, product access, commitments, credits, and billing schedules, with flexible rate structures and preserved version history. Metronome encodes each deal through flexible, contract-based modeling and supports pricing models such as:

* Pay-as-you-go
* Prepaid usage commitments
* Subscriptions with usage-based overage
* Enterprise credits with tiered pricing
* Bundled or hybrid pricing structures
* Seats and seats with overages pricing models

### Clear product and obligation tagging

Stable identifiers and explicit categorization of revenue types (point-in-time vs over-time) are kept to assist with allocation and recognition rules. Stable identifiers allow you to automate allocation and recognition rules in ERP tools and avoid manual remapping when historical data is re-pulled.

### Real-time usage processing and invoices

The platform is engineered for high-volume, real-time environments, capable of:

* Ingesting billions of usage events via APIs
* Processing events through billable metrics
* Applying pricing and discounts dynamically
* Issuing invoices or updating balances instantly

This real-time flow is critical for fraud detection, spend throttling, and usage enforcement, helping companies reduce exposure to uncollectible revenue.

### Traceable data and audit trail

Every billed amount links back to original usage, applied rate, and adjustments, with consistent tags and an immutable audit trail. All changes to contracts, pricing, or obligation tagging are captured with version history which ensures transparency, prevents retroactive data inconsistencies, and builds trust in Metronome's outputs as a reliable system of record.

### Robust reporting and integration

Flexible reporting with product/SKU-level detail, schema-stable exports, and APIs for seamless ERP/revenue tool integration. Reporting allows for cross-system reconciliation, including:

* API and data warehouse integrations
* Detailed exports of line items, ledgers and balances
* Reconciliations with systems such as Salesforce, Stripe, ERPs, and customer data warehouses

### Forecasting and breakage insights

Ability to track and estimate unused commitments and credit rollovers for future revenue impact analysis.

## The five-step ASC 606 model

The standard requires companies to follow this sequence:

1. Identify the contract(s) with a customer
2. Identify the performance obligations in the contract
3. Determine the transaction price
4. Allocate the transaction price to the performance obligations
5. Recognize revenue when (or as) the obligations are satisfied

Each step below includes:

* What ASC 606 requires
* Customer challenges
* How Metronome supports this step
* Critical Callouts / Common Issues

## Step 1: Identify the contract

### Accounting meaning

A contract is a legally enforceable agreement with a customer with defined rights, obligations, and payment terms. For revenue recognition, every usage event, charge, or credit in Metronome must tie back to a specific contract with a customer, as the contract is the basis for all subsequent ASC 606 steps.

Customers may have multiple contracts with one company (e.g., a master agreement and separate orders) that need separate tracking. In addition, contracts can change over time, through extensions, renewals, scope increases, rate changes, which can trigger new accounting assessments.

### Customer challenges

* Linking billing data back to the correct contract
* Tracking contract start/end dates and changes over time
* Maintaining an audit trail for contract amendments

### How Metronome supports

* **Unique contract ID field** in all relevant data exports and API calls
* **Key contract data capture** including start and end dates, effective dates for amendments and total contract value (TCV)
* **Store version history** to retain contract amendments without overwriting historical data
* **Support contract hierarchy** to provide linkage of contracts (treat multiple related agreements as one contract from an accounting perspective) if needed
* **Integration hooks** to CRM/ERP contract records so finance can reconcile

<Info>
  **Key product focus:** Ensure all usage, billing, and adjustment data is tied to a persistent, unique Contract ID.
</Info>

### Helpful links to learn more

* **[How Metronome works - Contracts: Encode Your Commercial Model](/guides/get-started/how-metronome-works#contracts%3A-encode-your-commercial-model%E2%80%8B):** This section explains that Metronome uses contracts to connect customers to pricing structures and define specific commercial arrangements, including base pricing, custom terms, product access, payment structures, and billing cycles.
* **[Reconcile data - Contract Reconciliation](/guides/reporting-insights/financial-reporting/reconcile-data#contract-reconciliation):** This section details how Metronome data, including contract start and end dates, commit amounts, and custom negotiated discounts, can be reconciled against Salesforce CPQ to ensure accuracy. To support this reconciliation, you will need to add the relevant SFDC object ids to each Metronome object using custom fields. You can also use the [Metronome to Salesforce integration](/integrations/platform-integrations/sfdc-integration) to automatically export `metronome__Contract__c` and `metronome__Commit__c` data objects into Salesforce which contain contract ID, customer, rate card, name, start/end dates, and usage statement schedule frequency, as well as commit details like type, priority, total amount, and current balance.
* **[Revenue recognition examples](/guides/reporting-insights/financial-reporting/revenue-recognition-examples):** This section includes example tables for Customer and Contract data, demonstrating how contract IDs, customer IDs, and start/end dates are populated for various revenue reporting scenarios.

### Critical callouts / Common issues

#### Multiple agreements = One contract

Under ASC 606, contracts signed close together with a single commercial objective may need to be combined. Metronome clients sometimes fail to link related contracts in Metronome. Metronome supports the linkage of related contracts through its parent-child account linkage feature, in which multiple contract IDs can be linked together.

<Tip>
  **Example:** A SaaS provider (company) executes a three-year subscription agreement and at or near the same time, also executes a separate professional services SOW to assist in implementing its platform. Because these agreements were likely negotiated together as part of one commercial package, ASC 606 may require combining them into a single contract for revenue recognition purposes. In Metronome, users have the ability to link these accounts as parent-child relationships; otherwise these will show as separate customer contracts.
</Tip>

#### Contract modifications

Upsells, downgrades, and renewals require careful accounting treatment (prospective vs. retrospective). Metronome can track modifications and maintain version history and an audit trail for such amendments, but you must ultimately decide how to treat them under ASC 606.

<Tip>
  **Example:** A SaaS provider (company) has a customer on a \$100k/year subscription that upgrades mid-term to add \$40k/year of additional functionality. The company must determine if this is a separate contract (prospective accounting) or a modification of the original contract (retrospective catch-up). Metronome can capture and track the change, but the company still needs to apply the correct ASC 606 treatment.
</Tip>

#### Opt-out clauses and termination rights

Multi-year deals with opt-outs may not count as one multi-year contract. Metronome clients may incorrectly report TCV without considering the enforceable contract period under ASC 606.

<Tip>
  **Example:** A SaaS provider (company) signs what appears to be a three-year, \$300k deal. However, the customer can terminate after the first year with no penalty. For ASC 606 purposes, only the first year (\$100k) is enforceable. If the company reports \$300k TCV without considering the opt-out, they are overstating revenue expectations. Metronome can flag these terms, but the accounting conclusion must be made by the client.
</Tip>

#### Committed "free" periods

Metronome clients often neglect to include committed "free" periods in the contract definition, leading to mismatches between system usage and revenue recognition.

<Tip>
  **Example:** A SaaS provider (company) offers a 12-month contract with a 2-month "free" period at the start, followed by 10 months of paid service at \$10k/month. The enforceable contract period is still 12 months, with \$100k in total consideration, but companies sometimes only record 10 months. This creates a mismatch between usage data in Metronome (12 months of service) and the revenue contract (12 months, \$100k). Correctly setting this up avoids gaps in recognition and reporting.
</Tip>

## Step 2: Identify the performance obligations

### Accounting meaning

Performance obligations are distinct (separable) promises to deliver goods or services; in any contract with a customer there can be single obligations (e.g., a year of platform access) or multiple obligations (e.g., subscription plus implementation services plus add-ons). Identifying performance obligations is important because each obligation may be accounted for separately under ASC 606.

In SaaS and usage-based revenue models, performance obligations might be:

* Platform access (subscription)
* Usage-based services (API calls, data processed)
* Implementation/setup
* Enhanced support

### Customer challenges

* Disaggregating or combining charges into clear performance obligations (i.e., mapping)
* Handling bundled offerings without losing line-level detail

### How Metronome supports

* **Product and rate card structure** allows mapping SKUs/usage metrics to specific obligation categories or obligation ID
* **Obligation tags** in the data model to flag each charge or usage event
* **Bundle support** while retaining disaggregated product-level exports
* **Ability to retroactively tag** historical data if obligations change

<Info>
  **Key product focus:** Provide customers with obligation-level granularity in all outputs, which is essential for allocation and revenue rules.
</Info>

### Mapping to Metronome's current documentation

* **[How Metronome works - Products & Rate Cards section](/guides/get-started/how-metronome-works#price%3A-products-%26-rate-cards%E2%80%8B):** This section describes Products as what is being sold to customers (individual SKUs that appear as line items on invoices) and mentions support for various product types, including usage-based, fixed, or subscription charges. This directly relates to defining performance obligations. It also notes the ability to customize invoice appearance, organize related SKUs with tags, and control granularity.
* **[How revenue recognition works - Revenue reporting categories subsection](/guides/reporting-insights/financial-reporting/revenue-recognition#revenue-reporting-categories):** This section lists common revenue reporting categories such as on-demand usage, prepaid/postpaid commitment drawdown, overage usage, and credit drawdown, further broken down by product, which aligns with identifying distinct performance obligations.
* **[Sync into Salesforce](/integrations/platform-integrations/sfdc-integration):** The `metronome__Invoice_Line_Item__c` data object, which includes `Product_Type__c`, helps track what specific products are being invoiced, supporting the identification of performance obligations.

### Critical callouts / Common issues

#### Complexity in identifying performance obligations

What appears to be a distinct SKU in Metronome may not always be a separate performance obligation under ASC 606. Or vice versa, as in the case of a hybrid model, such as usage plus subscription services, which may need to be separated into distinct performance obligations. Misclassifying SKUs, e.g., treating everything as stand-alone or failing to separate hybrid models, can lead to revenue recognition errors. Metronome allows mapping SKUs and usage metrics to specific obligation categories or IDs, but user is responsible for setting this up and mapping correctly.

<Tip>
  **Example:** A SaaS provider (company) includes "Premium Analytics" as a separate SKU in Metronome. In practice, this feature is integrated into the core subscription and not distinct on its own. If treated as a separate performance obligation, the company may allocate revenue incorrectly. Conversely, another company bundles "free" implementation services into the core subscription without breaking them out as a separate SKU. If those services are distinct under ASC 606, failing to separate them leads to incorrect revenue recognition. Both scenarios highlight the risk of misclassifying SKUs in Metronome and the importance of properly evaluating performance obligations beyond system configuration.
</Tip>

#### Implementation / setup fees

One-time charges must be evaluated; are they distinct services or part of a broader service obligation? Once determined, users can then map such services to their specific obligation within Metronome (e.g., either as combined or as a separate obligation ID).

<Tip>
  **Example:** The customer of a SaaS provider (company) pays a \$20k onboarding fee plus \$100k for the annual software subscription. If the onboarding activities do not transfer a distinct good or service (e.g., they only enable the customer to access the subscription), the \$20k is likely not a separate performance obligation and in such case would be deferred and recognized over the subscription term (i.e., combined with the subscription).
</Tip>

#### Support and service tiers

Customers may combine support activities with the core platform services, but certain support offerings may require it to be assessed separately as a performance obligation and mapped to their own obligation ID.

<Tip>
  **Example:** A SaaS provider (company) includes "24/7 Premium Support" as an add-on support service. Some companies treat this as incidental and bundle it into the main subscription. However, this may represent a distinct performance obligation that should be separated and allocated its share of the transaction price in Metronome.
</Tip>

## Step 3: Determine the transaction price

### Accounting meaning

The transaction price is the total amount the entity expects to be entitled to under the contract's enforceable term, and while it usually aligns with TCV (total contract value) it may differ depending on how TCV is defined. The transaction price can include:

* Fixed fees (subscription fee, flat setup fee)
* Variable usage fees (usage-based fees, overages)
* Discounts and credits
* Constraints on variable consideration to avoid overstatement

### Customer challenges

* Capturing all pricing components separately for accounting purposes, such that the total contract value (transaction price) within Metronome is accurate
* Handling variable consideration (VC), including tracking and mapping to usage. Metronome's system can accommodate variable components like overages and rollovers. For complex scenarios, Metronome clients may need to estimate the transaction price to effectively defer revenue
* Understanding how much of billed amounts are fixed vs. variable, and how discounts or credits were applied
* Maintaining a record of all adjustments

### How Metronome supports

* **Granular price capture** provides separate fields for fixed, variable, discounts, credits
* **Raw usage linkage** stores raw usage alongside the final billed amount for auditability
* **Flexible contract and rate card architecture** supports varied commercial models and dynamic pricing structures for ramped deals and tiered pricing structures
* **Adjustment tracking** with exported logs of discounts, credits, and reason codes
* **Currency handling** supported by storing original and functional currency amounts

<Info>
  **Key product focus:** Make sure all pricing elements are explicitly stored and exportable and not buried in aggregated totals.
</Info>

### Mapping to Metronome's current documentation

* **[How Metronome works - Price: Products & Rate Cards section](/guides/get-started/how-metronome-works#price%3A-products-%26-rate-cards%E2%80%8B):** This section describes Rate Cards as defining the default pricing for usage products, supporting scheduled price changes and different tiers. This relates to how prices are set and applied across commercial models. The system also supports commit-specific pricing, incentivizing higher commitments with discounts.
* **[How revenue recognition works - Terminology section](/guides/reporting-insights/financial-reporting/revenue-recognition#terminology):** This source defines concepts like On-demand usage, Commits (prepaid and postpaid), and Overage, which all contribute to the transaction price.
* **[Sync into Salesforce](/integrations/platform-integrations/sfdc-integration):** The `metronome__Commit__c` data object includes `Total_Amount__c`, representing the total dollar amount of the commit or credit, which is a key component of the transaction price. The `metronome__Invoice__c` object includes `Total__c`, representing the invoice total.

### Critical callouts / Common issues

#### Variable consideration

Overage fees, rollovers, and future credits create complexity. Customers sometimes assume invoice amounts equal transaction price, but under ASC 606, VC may be required to be estimated and it could also be constrained. Metronome allows for capture and tracking of different types of consideration if designated correctly by the user.

<Tip>
  **Example:** A cloud storage provider charges \$120k for a base annual subscription plus \$0.05 per GB over a 1 TB limit. By October, a customer has fully consumed the prepaid balance and is issued an invoice for overages. Under ASC 606, those overages may represent variable consideration that should be estimated and constrained at contract inception, instead of recognized when billed. If the company simply books the invoice amounts, revenue could be misstated.
</Tip>

#### Foreign currency

ASC 606 requires consistent policy on FX treatment. While Metronome captures billing currency, users will need to ensure that their FX treatment is consistent under U.S. GAAP based on their currency designation(s).

<Tip>
  **Example:** A U.S.-based SaaS vendor (company) bills a German customer €100k annually. Metronome tracks the billing in euros, but ASC 606 requires revenue to be reported consistently in the company's functional currency (e.g., USD). The company must establish and apply a clear FX translation policy (e.g., using the contract inception rate or monthly average rates).
</Tip>

## Step 4: Allocate the transaction price

### Accounting meaning

Once the total transaction price is determined, it must be allocated to the individual performance obligations based on their standalone selling price (SSP; i.e., relative selling price). This step ensures that discounting of one product or SKU doesn't mismatch its value, and it can be challenging, especially with bundled services or complex discount structures. Allocation affects the amount of revenue recognized for each obligation.

### Customer challenges

* Determining SSPs for performance obligations and properly allocating consideration in ERP/revenue tools
* Retaining historical data for reallocation if SSPs change

### How Metronome supports

* **Charge-level reporting** by SKU/obligation
* **Usage-to-obligation mapping** for every event and charge
* **Data formatted** so ERP systems can allocate automatically without manual intervention
* **Historical allocation support** including the availability of historical data from which to determine/support SSP analysis, and the ability to retain raw amounts even after pricing changes in case a customer's SSP changes and allocations are needed for past periods
* **Maintain consistent identifiers** across all reports and APIs for allocation mapping

<Note>
  Metronome's strength lies in its ability to track revenue at a granular level and provide the granular data necessary for allocation, but it does not perform reallocations.
</Note>

<Info>
  **Key product focus:** Preserve obligation-level allocation data in a clean, consistent format for downstream processing.
</Info>

### Mapping to Metronome's current documentation

* **[How Metronome works - Contracts: Encode Your Commercial Model](/guides/get-started/how-metronome-works#contracts%3A-encode-your-commercial-model%E2%80%8B):** This section describes how Contracts allow for custom terms and overrides, such as percentage or per-unit discounts, to be applied to specific products or product tags. While Metronome itself doesn't perform SSP allocation, it captures the custom pricing and discount structures at the contract level.
* **[How revenue recognition works - Revenue reporting categories](/guides/reporting-insights/financial-reporting/revenue-recognition#revenue-reporting-categories):** Metronome's ability to break down revenue by product within each category (e.g., on-demand, commit drawdown) provides the granularity needed to track performance and helps facilitate allocation outside the system.
* **[Sync into Salesforce](/integrations/platform-integrations/sfdc-integration):** The `metronome__Invoice_Line_Item__c` data object contains `Quantity__c`, `Unit_Price__c`, `Product_Type__c`, and `Total__c`, providing the specific data points that, when combined, can be used by the customer for price allocation logic. The `metronome__InvoiceLineItemPricingDimensionAssoc__c` and `metronome__Pricing_Dimension__c` objects also offer metadata for granular pricing details.

### Critical callouts / Common issues

#### SSP allocation

Metronome provides granular invoice data, but does not allocate transaction price across performance obligations. Companies may fail to adjust for relative SSP (Standalone Selling Price) allocations when discounts are bundled, whether a significant discount is included on a particular SKU or a service is included for "free".

<Tip>
  **Example:** A SaaS vendor (company) sells a \$100k annual subscription bundled with \$20k of professional services, discounting the package to \$105k total. Under ASC 606, the \$105k must be allocated to each performance obligation based on relative SSP. If the company simply books the \$100k subscription and \$5k services from the invoice data in Metronome, revenue will be misallocated.
</Tip>

#### Commit / usage attribution

Companies must determine how prepaid commits or rollovers relate to performance obligations. Without explicit allocation, they risk misclassification.

<Tip>
  **Example:** A cloud provider (company) sells a \$240k annual commit that includes \$20k of monthly usage credits. The customer uses only \$15k in some months and \$25k in others, with rollovers applying. Without clear attribution rules, the company may misclassify revenue (e.g., treating overages as new revenue instead of part of the original commit).
</Tip>

#### Discounts and material rights

Commit-specific discounts, tiered pricing, or future discount rights (e.g., renewal discounts) may create additional customer rights that require revenue allocation.

<Tip>
  **Example:** A SaaS vendor (company) sells a one-year contract for \$120k but also gives the customer a right to renew the following year at a 50% discount. That renewal option may be considered a "material right" under ASC 606. Part of the \$120k paid today would be allocated to the renewal right, not just to the first year of service.
</Tip>

## Step 5: Recognize revenue

### Accounting meaning

The final step is to recognize revenue when or as performance obligations are satisfied. This can occur either over time (e.g., access to a platform over a period) or at points in time (e.g. as usage occurs, or a specific service is delivered). Metronome, as a usage-based platform, generally aligns with point in time recognition as usage occurs. However, it also supports subscriptions and seats which are typically recognized over time.

### Customer challenges

* Matching usage to the correct recognition period
* Handling true-ups and overages tied to prior periods
* Differentiating between billing and earned revenue

### How Metronome supports

* **Timestamped usage events** can be exported back to Data Warehouse for reconciliation
* **Billed vs. earned views** in exports to separate invoicing from recognition
* **True-up alignments** link adjustments back to the original usage period
* **Long-term retention** of usage and billing data for audit lookbacks

<Info>
  **Key product focus:** Ensure granularity + historical linkage so clients can confidently build recognition schedules.
</Info>

### Mapping to Metronome's current documentation

* **[How Metronome works - Invoice Generation: Bringing It All Together section](/guides/get-started/how-metronome-works#invoice-generation%3A-bringing-it-all-together%E2%80%8B):** This section explains that Metronome processes usage data, applies pricing from the customer's contract, and generates invoices in real-time with usage, on-demand via API, or at billing cycle close. This reflects the timing of when usage is measured and therefore when revenue could be recognized.
* **[How revenue recognition works](/guides/reporting-insights/financial-reporting/revenue-recognition):** This section explains how Metronome maintains detailed transaction history and ledgers to calculate deferred, accrued, and recognized revenue with daily granularity down to products and revenue categories. It details how revenue is recognized for on-demand usage (immediately upon invoice issuance), prepaid commit drawdown (as commits are drawn down or expire), and postpaid commits (as usage occurs or when true-up invoices are issued).
* **[How revenue recognition works - Metronome data model](/guides/reporting-insights/financial-reporting/revenue-recognition#metronome-data-model):** This section explains that querying invoices with `status = 'FINALIZED'` produces a report of recognized revenue, while `status = 'DRAFT'` produces a report of accrued revenue. It also details specific ledger entry types for credits and commits that are relevant to revenue recognition, indicating when certain amounts should be recognized (e.g., `prepaid_segment_expiration` should always be recognized as revenue).
* **[Revenue recognition examples](/guides/reporting-insights/financial-reporting/revenue-recognition-examples):** This source provides concrete scenarios (e.g., on-demand usage with free credits, prepaid commitments, postpaid commitments) with accompanying data export tables and explanations of how CloudNet (the example company) recognizes revenue in each situation.

### Critical callouts / Common issues

#### Timing of revenue recognition

Metronome shows usage in real time, but companies must confirm that their policy is point in time (as consumed) vs. over time (ratable) recognition.

<Tip>
  **Example:** A SaaS vendor (company) charges per API call. Metronome shows usage in real time, but under ASC 606, the company must decide whether the API service transfers at a point in time (each call) or over time (continuous access). If treated incorrectly, revenue may be accelerated or deferred improperly.
</Tip>

#### Cutoff / partial month issues

Daily breakdowns solve cutoff problems, but if companies don't use them, they may incorrectly prorate revenue at month-end.

<Tip>
  **Example:** A SaaS company's contract starts on March 20. If they only recognize revenue by full months instead of using Metronome's daily breakdown, they may record all of March's revenue even though the service was only provided for 12 days, overstating revenue for that period.
</Tip>

#### Breakage estimates

If you expect breakage, recognize it in proportion to the pattern of rights exercised, subject to the constraint. Companies often fail to estimate breakage upfront, leading to deferral errors.

<Tip>
  **Example:** The customer of a SaaS vendor (company) prepays \$120k for annual usage credits but historically only uses about 80%. Under ASC 606, the company may need to estimate and recognize expected breakage (\$24k) as revenue over the service period. If they wait until credits expire, they may understate revenue throughout the year and then have a large "catch-up" later.
</Tip>

#### Invoicing vs. revenue recognition timing

Recognize revenue when control transfers (per-event point in time or, for stand-ready arrangements, over time), not when invoices are issued. Invoice timing and recognition often differ. Companies may incorrectly align revenue only with invoice timing, missing accrued-but-unbilled obligations

<Tip>
  **Example:** A vendor invoices \$120k upfront for a one-year subscription. Under ASC 606, revenue must be recognized ratably as services are provided, not when invoiced. If the company books the full \$120k in January, they've overstated Q1 revenue and understated the remainder of the year.
</Tip>

## Appendix: Examples and data components

Metronome provides the foundational data needed to support complex revenue recognition requirements in usage-based business models. Through detailed transaction history, ledger entries, and configurable pricing logic, Metronome enables its clients to calculate deferred, accrued, and recognized revenue with daily granularity. This data is accessible via Metronome's APIs or data export functionality and can be integrated into external revenue subledgers, ERPs, or custom reports exportable as CSVs.

Metronome's data model includes:

* Invoice timestamps (`invoices.start_timestamp`, `invoices.end_timestamp`) to define service periods
* Line item attributes (`line_items.product_id`, `line_items.commit_id`) for product-level revenue recognition
* Credit and balance ledger entries to support treatment of prepaid, postpaid, free credits, and expirations

Below are common revenue scenarios and how Metronome's data components map to each use case:

### 1. On-demand (pay-as-you-go) usage

**Description:** Customer is billed based on actual usage with no precommitments.

**Revenue recognition:** Recognized at the time of invoicing, as usage is incurred.

**Metronome data mapping:**

* `invoices.type = 'CONTRACT_USAGE'` for usage-based billing
* `line_items.commit_id = null` indicates on-demand or overage (differentiated via metadata)

**Example:** Customer A incurs \$384 for CloudCompute and \$75 for CloudStorage between Jan 16–31, invoiced on at the end of the month and recognized as on-demand revenue.

### 2. Prepaid commitment drawdown

**Description:** Customer prepays a fixed amount (e.g., \$10,000) for future usage at a discount.

**Revenue recognition:** Prepayment deferred initially; recognized as revenue as credits are consumed.

**Metronome data mapping:**

* `invoices.type = 'CONTRACT_SCHEDULED'` for the initial prepaid commit (deferred revenue)
* `invoices.type = 'CONTRACT_USAGE'` for usage during drawdown (often \$0 invoices)
* `line_items.commit_id` populated; joins to `balances.type = 'prepaid'`

**Example:** \$900 of usage is consumed against a \$10,000 commit and recognized upon consumption, even if no invoice is issued for usage.

### 3. Prepaid commit expirations (breakage)

**Description:** Unused credits at the end of the commitment period are expired.

**Revenue recognition:** Recognized as revenue when expired (or earlier if using a breakage model).

**Metronome data mapping:**

* `balances_ledger.entry_type = 'prepaid_segment_expiration'` indicates credit expiration
* No invoice is issued; the expiration is tracked via the ledger

**Example:** \$1,400 of unused commit is expired on Jan 1, 2025, and recognized as revenue as the company does not have a history of rolling over expired credits.

### 4. Postpaid commitment drawdown

**Description:** Customer commits to a minimum spend but pays monthly in arrears.

**Revenue recognition:** Recognized as usage occurs.

**Metronome data mapping:**

* `invoices.type = 'CONTRACT_SCHEDULED'` or `'CONTRACT_USAGE'`
* `line_items.commit_id` populated; linked to `balances.type = 'postpaid'`

**Example:** \$700 for CloudCompute and \$100 for CloudStorage is recognized for the month based on usage.

### 5. Postpaid commitment true-ups

**Description:** Customer falls short of minimum commitment, and a true-up invoice is issued.

**Revenue recognition:** Recognized when true-up invoice is finalized (unless rolled into a renewal).

**Metronome data mapping:**

* `invoices.type = 'CONTRACT_TRUEUP'`
* `balances_ledger.entry_type = 'postpaid_trueup'`

**Example:** A \$400 true-up is invoiced at the end of the term and recognized (upon expiration).

### 6. Overage usage

**Description:** Usage exceeds the committed amount.

**Revenue recognition:** Recognized upon invoicing.

**Metronome data mapping:**

* `line_items.commit_id = null` indicates overage (if no commit applies)
* Differentiated from on-demand using client-defined metadata

**Example:** \$900 of overage in month 11 is invoiced and recognized.

### 7. Free credits

**Description:** Credits provided as promotions, free trials, or SLA compensation.

**Revenue recognition:** Not deferred or recognized as revenue. May offset recognized revenue as contra-revenue.

**Metronome data mapping:**

* `balances_ledger.entry_type = 'credit_automated_invoice_deduction'`

**Example:** \$410 in credits are applied to usage; \$90 of unused credits expire.

## Metronome data model highlights

Metronome's data structure supports compliance with ASC 606 through the following capabilities:

### Product-level granularity

Metronome categorizes revenue by type (on-demand, commit drawdown, overage) and product, enabling precision in revenue tracking and reporting. It does so while capturing detailed transaction history and ledgers with daily granularity, down to products and revenue categories, which is crucial for period-specific revenue recognition and audit support.

### Custom fields on SKUs

Metronome clients can define performance obligations at the SKU level using custom fields, which are available in data exports for revenue allocation and categorization.

### Invoice line item detail

* `line_items.commit_id`: indicates commit-based usage
* `line_items.product_id`: used for product-level recognition
* `invoices.credit_type_id`: identifies the billing currency
* `invoices.start_timestamp` / `end_timestamp`: define the service delivery period

### Reporting and reconciliation

Metronome provides invoicing information that is critical for determining deferred revenue balances and contract assets/liabilities. This data can be reconciled against external systems like Salesforce and Stripe. Metronome offers robust data exports and APIs that allow customers to extract detailed data (contracts, invoices, usage, pricing) for reconciliation with their external ERP or accounting systems.

* `invoices.status = 'FINALIZED'`: used for recognized revenue
* `invoices.status = 'DRAFT'`: used for revenue accruals

These views support reconciliation of revenue recognized, deferred, and contract assets.

### Support for complex pricing

Rate cards define default pricing, and can accommodate tiered pricing, composite charges, commit-specific pricing, scheduled price changes, and dynamic overrides. While the platform does not perform allocation under ASC 606, the necessary data for determining standalone selling prices is available.

### Contract management

Metronome's contract object serves as a central hub for defining a customer's commercial model, including base pricing, custom terms, product access, payment structure (commitments, credits, subscriptions), and billing cycles, important for capturing TCV. Framework includes support for:

* Multi-year ramp deals
* Opt-out and renewal clauses
* Access schedules for commitments
* Parent-child account structures a.k.a. account hierarchy
