<!-- Source URL: https://docs.metronome.com/guides/reporting-insights/in-app-reporting.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Access in-app reports

Metronome can trigger custom and standard in-app reports to run against your Metronome data. Download these reports in a CSV format from the Reports tab in the Metronome app.

To enable custom or standard reports, please contact your Metronome Solutions Architect.

<Note>
  **DATA PROCESSING TIMES**

  While most reports generate within 1-2 hours, it can take up to 10 hours to generate larger reports. Reports are generated using data that updates once per day. Depending on when the underlying data updates, you may see stale data requiring you to trigger the report to run again.
</Note>

## Standard reports

Standard reports are pre-defined reports you can trigger to run from the Reports tab in the Metronome app. Once triggered, the report generates and you receive an email confirmation with a link to download the resulting report in the UI as a CSV file.

**Included standard reports:**

| Report name                                          | Description                                                                                                                                                                             |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customers by created date                            | Returns all customers in your Metronome account. Useful for tracking customer growth over time.                                                                                         |
| Contracts by created date                            | Returns all contracts across customers. Helpful for understanding contract volume and sales activity.                                                                                   |
| Commits and credits by created date                  | Returns all prepaid commits and credits issued to customers. Useful for tracking commitment sales and credit grants.                                                                    |
| Invoices by status and by effective date             | Returns all finalized invoices and line items, and effective billing period. Useful for accounts receivable and revenue recognition.                                                    |
| Commit expiration ledger entries by month            | Returns ledger entries for commits that expired during each month. Useful for tracking unused commitment balances and breakage revenue.                                                 |
| True up invoices by effective date                   | Returns all true-up invoices. Useful for tracking end-of-period commitment reconciliation charges.                                                                                      |
| Monthly revenue by product name and revenue category | Returns revenue totals broken down by product and category (e.g., on-demand, commit drawdown, overage) for each month. Useful for financial reporting and product performance analysis. |

To trigger a standard report to run, visit the Reports tab in the Metronome app, select the report from the dropdown, enter filtering dates and click Generate Report.

After a report completes, you'll receive an email confirmation with a link to download the resulting report in a CSV format from the Reports tab in the Metronome app.

## Custom reports

<Info>
  **NOTE**

  Custom reports is a paid feature. If you're interested in learning more about this feature, contact your Metronome Solutions Architect.
</Info>

Custom reports provide a flexible mechanism to download custom Metronome datasets in a CSV format from the Reports tab in the Metronome app. The reporting engine can query the same data tables that are available via [Data Export](/guides/reporting-insights/data-export#data-availability).

To create a custom report, follow these steps:

1. Contact your Metronome Solutions Architect to request a custom report

2. Share detailed requirements about your reporting needs (e.g. end of month books close, customer cohorting, etc.)

3. Review sample data with Metronome Solutions Architect

4. Approve the resulting data

5. Confirm how you want to trigger the reports (you can either trigger the report from the Metronome App or schedule via cron)

To trigger a custom report to run, visit the Reports tab in the Metronome app, select the report from the dropdown, enter filtering dates and click Generate Report.

After a report completes, you'll receive an email confirmation with a link to download the resulting report in a CSV format from the Reports tab in the Metronome app.

## In-app dashboards

<Info>
  In-app dashboards are currently in beta. Contact your Metronome representative to have them turned on for your account.
</Info>

In-app dashboards provide Metronome clients with access to critical revenue and monetization metrics directly within the Metronome app. Rather than exporting data and building views externally, you can use these dashboards to monitor business performance, track key financial metrics, and explore customer-level details in real time.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/pUEKr5nqd5TnxR9X/images/docs/guides/reporting-insights/in-app-dashboard-screenshot.png?fit=max&auto=format&n=pUEKr5nqd5TnxR9X&q=85&s=79e2747ca5dcb288f833c5c451d2c6e8" alt="In-app dashboards" width="3420" height="1666" data-path="images/docs/guides/reporting-insights/in-app-dashboard-screenshot.png" />
</Frame>

**Included in-app dashboards:**

| Dashboard                          | Description                                                                                                                                                                                             |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Basic Revenue Overview             | Provides monthly summaries of invoiced amounts, usage and subscription revenue, commit and credit metrics, and customer-level consumption details.                                                      |
| Committed & Run Rate ARR Dashboard | Provides key financial metrics for consumption-based businesses, including Annual Recurring Revenue (ARR), Net Revenue Retention (NRR), Gross Revenue Retention (GRR), and logo movement.               |
| Filterable Customer List           | Provides a flexible, filterable view of your customer list — built from common feature requests and designed to make it easier to search and sort by billing provider, spend, and other key attributes. |

### Committed & Run Rate ARR Dashboard

The Committed & Run Rate ARR Dashboard surfaces the key financial metrics consumption businesses use to track growth and retention. The sections below describe how each metric is defined and computed.

#### Metrics definitions

**Committed ARR**

Committed ARR measures the contractually committed revenue from customers, including usage commitments and scheduled charges. It is derived from `scheduled_charges` and `balances` in your Metronome data.

* **Balances (commits and credits)**: Schedule items are unnested to extract individual commitment periods with their amounts and date ranges. ARR is calculated by dividing each schedule item's amount by its duration in days, then annualizing: `(amount / duration_days) × 365`. For CPU commits, amounts are converted to dollars using the corresponding rate card conversion.
* **Scheduled charges**: Schedule items are unnested to sum the total amount per charge over its contract period (`starting_at` to `ending_before`). ARR is calculated by dividing the total amount by the duration in days, then annualizing.

**Run Rate ARR**

Run Rate ARR estimates annualized revenue based on actual usage and subscription revenue over a shorter, configurable window. For example, with a 3-month window: `run_rate_ARR = average monthly revenue across the last 3 months × 12`. Usage and subscription line items are used to calculate usage revenue.

Methodology notes:

* For customers with less than X months of history, whatever months are available are used to calculate the moving average MRR.
* Run Rate ARR continues to be calculated for churned customers. If a customer's latest month's usage is `$0`, the run rate MRR is still the average across the last X months.

#### ARR movement

All metrics compare the current period to the base period (X months ago, configurable).

* **New ARR**: ARR from customers who had `$0` ARR (or didn't exist) in the base period but have ARR `> $0` in the current period.
* **Expansion ARR**: *Additional* ARR from existing customers whose ARR grew (current ARR `>` base period ARR). This is the difference between current and base.
* **Contraction ARR**: *Lost* ARR from existing customers whose ARR decreased (base period ARR `>` current ARR, but current ARR `> $0`). This is the difference between base and current.
* **Churned ARR**: The *full base period ARR* from customers who had ARR `> $0` in the base period but have `$0` ARR in the current period.

**Net ARR Change** = New ARR + Expansion ARR − Contraction ARR − Churned ARR

#### Revenue retention

* **GRR (Gross Revenue Retention)**: The percentage of base period ARR retained, *excluding expansion*.
  * Formula: `retained_arr / starting_arr`
  * Where `retained_arr = min(current ARR, base ARR)` for each customer.
  * GRR `< 100%` means revenue was lost through contraction and churn.
* **NRR (Net Revenue Retention)**: The percentage the base cohort's ARR grew to, *including expansion*.
  * Formula: `ending_arr_from_base_cohort / starting_arr`
  * Where `ending_arr_from_base_cohort` is the current ARR for customers who existed in the base period.
  * NRR `> 100%` means expansion exceeded contraction and churn.
  * NRR `< 100%` means contraction and churn exceeded expansion.

#### Customer/logo movement

* **New customers**: Customers who had `$0` ARR (or didn't exist) in the base period but have ARR `> $0` in the current period.
* **Expanding customers**: Existing customers whose ARR grew (current ARR `>` base period ARR).
* **Retained customers**: Existing customers whose ARR stayed exactly the same (current ARR `=` base period ARR).
* **Contracting customers**: Existing customers whose ARR decreased but still have ARR `> $0` (base ARR `>` current ARR `> $0`).
* **Churned customers**: Customers who had ARR `> $0` in the base period but have `$0` ARR in the current period.
* **Active customers**: Total count of customers with ARR `> $0` in the current period, regardless of base period status.

#### Available filters

**Committed ARR tab**

These filters apply to the combined scheduled charges and commits dataset.

| Filter                             | Type        | Default                 | Behavior                                                                                                                                  |
| ---------------------------------- | ----------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Exclude customer                   | Multiselect | *(none)*                | Removes selected customers.                                                                                                               |
| Exclude contract                   | Multiselect | *(none)*                | Removes selected contracts. Rows without a contract (e.g., standalone scheduled charges) are preserved.                                   |
| Exclude commit type                | Multiselect | `credit`                | Removes selected commit types (e.g., `credit`, `prepaid`, `postpaid`). Scheduled charges without a commit type are preserved.             |
| Exclude commit shorter than (days) | Number      | `30`                    | Excludes commits/charges with duration below this threshold. Always active.                                                               |
| Exclude non-recurring charge       | Checkbox    | Off                     | When checked, keeps only rows with a recurring schedule. Removes fees that would occur only once.                                         |
| Exclude commit not invoiced        | Checkbox    | Off                     | When checked, keeps only commits that have associated invoice schedule items.                                                             |
| Select rate card                   | Multiselect | *(none — all included)* | When populated, restricts to only the selected rate card(s).                                                                              |
| Lookback period (months)           | Number      | `12`                    | Controls how many months of history are used for ARR movement, NRR/GRR, and customer movement calculations. Shared with the Run Rate tab. |

**Run Rate ARR tab**

These filters apply to the usage-based revenue dataset. A hardcoded filter also restricts data to **completed months only** (month `<` current month start).

| Filter                   | Type        | Default                 | Behavior                                                                                                                                        |
| ------------------------ | ----------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Exclude customer         | Multiselect | *(none)*                | Removes selected customers.                                                                                                                     |
| Exclude product          | Multiselect | *(none)*                | Removes selected products.                                                                                                                      |
| Exclude product type     | Multiselect | *(none)*                | Removes selected product types.                                                                                                                 |
| Exclude rev rec type     | Multiselect | `credit_drawdown`       | Removes selected revenue recognition types (e.g., `credit_drawdown`, `prepaid_commit_drawdown`, `postpaid_commit_drawdown`, `on_demand_usage`). |
| Customers without commit | Checkbox    | Off                     | When checked, excludes customers who have any non-credit commits. Useful for isolating pure on-demand customers.                                |
| Select rate card         | Multiselect | *(none — all included)* | When populated, restricts to only the selected rate card(s).                                                                                    |
| Average last X months    | Number      | `3`                     | Number of trailing completed months used to compute the run rate. Monthly revenue is averaged over this window, then annualized.                |
| Lookback period (months) | Number      | `12`                    | Shared with the Committed ARR tab. Controls ARR movement, NRR/GRR, and customer movement history window.                                        |

#### Caveats

* Only contract data and finalized invoices are used.
* All invoices are prorated by day, so invoices spanning multiple months are split across those months.
* Non-USD fiat currencies are not supported.
