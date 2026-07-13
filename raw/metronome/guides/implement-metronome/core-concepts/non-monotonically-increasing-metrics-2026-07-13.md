<!-- Source URL: https://docs.metronome.com/guides/implement-metronome/core-concepts/non-monotonically-increasing-metrics.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Non-monotonically increasing metrics

Most billable metrics in Metronome track usage that only goes up over time — for example, the total count of API calls made. These are **monotonically increasing** metrics. However, some metrics can fluctuate up *and* down over a billing period — for example, the number of connected devices or storage in use. These are **non-monotonically increasing** metrics, and they require a few special considerations when working with Metronome contracts, commits, credits, rate changes, and usage APIs.

Non-monotonically increasing metrics typically use the `latest` aggregation type, which captures the most recent reported value at each point in time rather than counting or summing all events together.

This page covers behavioral nuances specific to non-monotonically increasing (e.g., `latest`) metrics. For general information about creating billable metrics, see [Create billable metrics](/guides/implement-metronome/core-concepts/create-billable-metrics#1-identify-usage-components).

## How Metronome bills non-monotonically increasing metrics

When Metronome processes a `latest` metric for billing purposes, it calculates the **incremental change** between consecutive reporting windows rather than billing on the absolute value. This is a critical distinction that affects how charges, commits, credits, and rate changes are applied.

**Example:** You send in the following `latest` values over four days:

| Day   | Reported value | Incremental quantity billed |
| ----- | -------------- | --------------------------- |
| Day 1 | 7              | 7                           |
| Day 2 | 9              | 2 *(9 − 7)*                 |
| Day 3 | 10             | 1 *(10 − 9)*                |
| Day 4 | 5              | −5 *(5 − 10)*               |

Metronome computes the daily incremental change and uses that as the billable quantity. When the reported value **decreases**, the incremental quantity is **negative**, which results in a credit back to the customer for that period.

## Commit and credit coverage

Commits and credits apply only to the **incremental usage that falls within their effective date range** — not the absolute reported value.

### Example

Suppose you have a `latest` metric and send the following values:

* **Day 1:** reported value = **7**
* **Day 2:** reported value = **9**

You create a contract with a commit that covers **Day 2 onward only**.

Even though the absolute value on Day 2 is 9, the commit only covers the **incremental quantity** of **2** (the change from 7 to 9). The usage from Day 1 (quantity of 7) is not covered by the commit because it falls outside the commit's effective range.

| Period | Reported value | Incremental quantity | Covered by commit? |
| ------ | -------------- | -------------------- | ------------------ |
| Day 1  | 7              | 7                    | No                 |
| Day 2  | 9              | 2                    | Yes                |

This behavior ensures that commits and credits are applied proportionally to the usage that actually occurred during their effective period.

The same logic applies to **credits**. In the invoice below, the \$100 credit labeled "Free credit" covers only the incremental quantity that falls within its effective date range (March 17th onward).

**Example invoice with credit coverage:**

| Name           | Applied commit or credit | Effective date | Quantity | Unit price           | Total        |
| -------------- | ------------------------ | -------------- | -------- | -------------------- | ------------ |
| Latest Product | –                        | Mar 1 – Mar 17 | 40       | \$3.00               | \$120.00     |
| Latest Product | Free credit              | Mar 17 – Apr 1 | 25       | \$4.00               | \$100.00     |
| Latest Product | –                        | Mar 17 – Apr 1 | 55       | \$4.00               | \$220.00     |
|                |                          |                |          | Free credit consumed | −\$100.00    |
|                |                          |                |          | **Total due**        | **\$340.00** |

In this example, the free credit covers 25 of the 80 incremental units that accrued during the Mar 17 – Apr 1 period. The remaining 55 units are billed at the standard rate.

## Rate changes

When a rate change takes effect mid-period, Metronome applies each rate only to the **incremental usage that occurred during that rate's effective window**. This interacts with non-monotonically increasing metrics in two important ways depending on whether the value increased or decreased.

### Scenario 1: Value increases (incremental is positive)

* **Day 1:** reported value = **7** (rate = \$3.00/unit)
* **Day 2:** reported value = **9** (rate changes to \$4.00/unit)

The incremental quantity on Day 2 is **2**. Only that quantity of 2 is billed at the new \$4.00 rate. Day 1's quantity of 7 remains at \$3.00.

| Period | Quantity | Rate      | Charge      |
| ------ | -------- | --------- | ----------- |
| Day 1  | 7        | \$3.00    | \$21.00     |
| Day 2  | 2        | \$4.00    | \$8.00      |
|        |          | **Total** | **\$29.00** |

### Scenario 2: Value decreases (incremental is negative)

When the reported value drops after a rate change, the **negative incremental quantity** is priced at the **new rate**, resulting in a credit at that rate.

* **Mar 1 – Mar 17:** reported value reaches **40** (rate = \$3.00/unit)
* **Mar 17 – Apr 1:** reported value drops by **10** (rate changes to \$4.00/unit)

**Example invoice with rate change and negative quantity:**

| Name           | Effective date | Quantity | Unit price    | Total       |
| -------------- | -------------- | -------- | ------------- | ----------- |
| Latest Product | Mar 1 – Mar 17 | 40       | \$3.00        | \$120.00    |
| Latest Product | Mar 17 – Apr 1 | −10      | \$4.00        | −\$40.00    |
|                |                |          | **Total due** | **\$80.00** |

In this case, the customer is billed \$120.00 for the first period at \$3.00/unit, then credited \$40.00 for the decrease of 10 units at the new \$4.00 rate, resulting in a net total of **\$80.00**.

<Warning>
  Because negative incremental quantities are priced at the **current effective rate** (not the original rate), a rate increase combined with a usage decrease can result in a credit that is larger per unit than the original charge. Make sure your rate change timing accounts for this behavior.
</Warning>

## Credits combined with rate changes and usage decreases

When a credit is present alongside a rate change and a usage decrease, the interaction between these factors can produce **negative invoice totals**. This happens because Metronome evaluates each charge line independently and applies credits as it encounters positive charges — it does **not** look ahead to account for negative charges that appear later on the invoice.

### Example

Using the same scenario as above — a rate change from \$3.00 to \$4.00 on Mar 17, with usage rising to 40 then dropping by 10 — now add a **\$100.00 free credit** that covers the full billing period.

Metronome processes the charges in chronological order:

1. **Mar 1 – Mar 17:** 40 units × \$3.00 = \$120.00. The \$100.00 credit is applied here, covering 33.33 units. The remaining 6.67 units are billed at \$3.00.
2. **Mar 17 – Apr 1:** −10 units × \$4.00 = −\$40.00. This negative charge is processed as-is — the credit has already been consumed.

**Example invoice with credit, rate change, and negative quantity:**

| Name           | Applied commit or credit | Effective date | Quantity | Unit price           | Total        |
| -------------- | ------------------------ | -------------- | -------- | -------------------- | ------------ |
| Latest Product | Free credit              | Mar 1 – Mar 17 | 33.33    | \$3.00               | \$100.00     |
| Latest Product | –                        | Mar 1 – Mar 17 | 6.67     | \$3.00               | \$20.00      |
| Latest Product | –                        | Mar 17 – Apr 1 | −10      | \$4.00               | −\$40.00     |
|                |                          |                |          | Subtotal             | \$80.00      |
|                |                          |                |          | Free credit consumed | −\$100.00    |
|                |                          |                |          | **Total due**        | **−\$20.00** |

The subtotal of the charges is \$80.00 (the same as the scenario without a credit). However, the full \$100.00 credit was consumed against the first tranche of positive charges. The result is a **negative total due of −\$20.00**.

<Warning>
  **Metronome does not look forward when applying credits.** Credits are drawn down against positive charge line items as they are encountered. The system does not pre-calculate the net invoice total and limit the credit accordingly. This means that when positive charges early in a period are followed by negative charges later (due to a usage decrease), a credit can be consumed in full even though the net invoice total would have been lower than the credit amount. This can result in negative invoice totals.
</Warning>

Keep this in mind when configuring credits for products that use non-monotonically increasing metrics, especially in combination with mid-period rate changes.

<Tip>
  When using non-monotonically increasing metrics, we recommend configuring commits and credits to cover the **entire billing period** rather than a partial date range. This ensures that credits are applied holistically across all line items, including any negative incremental charges from usage decreases, and avoids unexpected negative invoice totals caused by credits being fully consumed against early positive charges before later negative charges are processed.
</Tip>

## Invoice breakdowns

When you call the [invoice breakdowns endpoint](/api-reference/invoices/list-invoice-breakdowns), Metronome returns the **incremental quantity and its associated cost for each time window** — not the absolute reported value. This includes negative quantities when usage decreases.

### Example

You send the following `latest` values:

| Day   | Reported value |
| ----- | -------------- |
| Day 1 | 7              |
| Day 2 | 9              |
| Day 3 | 10             |
| Day 4 | 5              |

The invoice breakdowns endpoint returns:

| Day   | Quantity | Cost            |
| ----- | -------- | --------------- |
| Day 1 | 7        | 7 × unit price  |
| Day 2 | 2        | 2 × unit price  |
| Day 3 | 1        | 1 × unit price  |
| Day 4 | −5       | −5 × unit price |

The **quantity** column reflects the incremental change, and the **cost** is calculated based on that incremental quantity. Negative quantities produce negative costs (credits).

This breakdown gives you a granular, day-by-day view of how the metric's value changed and how each change was priced.

## Usage endpoints

Unlike invoice breakdowns, the [usage endpoints](/api-reference/usage/get-usage-data-with-paginated-groupings) return the **absolute latest reported value per time window** — not the incremental change. The value you see depends on the granularity you request.

### Example

You send the following `latest` values:

| Day   | Reported value |
| ----- | -------------- |
| Day 1 | 7              |
| Day 2 | 8              |
| Day 3 | 9              |

**With a daily breakdown**, the usage endpoint returns:

| Day   | Value |
| ----- | ----- |
| Day 1 | 7     |
| Day 2 | 8     |
| Day 3 | 9     |

**With no breakdown** (full period), the usage endpoint returns:

| Period        | Value |
| ------------- | ----- |
| Day 1 – Day 3 | 9     |

The value returned with no breakdown is the **latest reported value** across the entire queried window.

<Info>
  **Key distinction:** Invoice breakdowns show **incremental quantities** (the change between windows), while usage endpoints show the **absolute latest value** within each window. Keep this difference in mind when reconciling data between the two.
</Info>

## Summary

| Behavior                           | What to expect                                                                                                                    |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Billing quantity                   | Incremental change between reporting windows — can be negative                                                                    |
| Commits and credits                | Applied only to incremental usage within the commit/credit's effective date range                                                 |
| Rate changes                       | Each rate applies to the incremental quantity during its effective window; negative increments are priced at the current rate     |
| Credits + rate changes + decreases | Credits are consumed against positive charges as encountered; they do not look ahead. This can result in negative invoice totals. |
| Invoice breakdowns                 | Returns incremental quantities and costs per time window, including negative values                                               |
| Usage endpoints                    | Returns the absolute latest value per time window (not incremental)                                                               |
