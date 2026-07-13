<!-- Source URL: https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/get-remaining-balance.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Track the remaining balance of a credit or commit

Tracking the remaining balance of credits and commits helps you accurately understand account health, forecast revenue, and track assets and liabilities. It also supports providing customers with up-to-date information on their remaining balance. There are many ways to display remaining balance to customers and Metronome provides the flexibility to display both aggregated and detailed views.

<Warning>
  Balance values can be **fractional numbers** (e.g., `0.8` cents for USD). When integrating with the balances API, do not truncate balances to integers — doing so may cause data loss. Rounding is acceptable if done intentionally. For USD, amounts are denominated in cents, so a balance of `0.8` represents \$0.008.
</Warning>

## Fetch the total remaining balance on a customer

To display an aggregated real-time balance to your customers, call the [`/getNetBalance`](https://docs.metronome.com/api-reference/credits-and-commits/get-the-net-balance-of-a-customer) endpoint. This endpoint returns a single aggregated sum of the remaining balance on a customer, with advanced filtering by balance type, currency, pending charges, and custom fields.

## Build a detailed ledger view of individual balances

Metronome also supports more detailed views of individual balances by tracking ledger entries using the [`listBalances`](https://docs.metronome.com/api-reference/credits-and-commits/list-balances) endpoint. Each credit or commit is associated with a ledger, which records events that change the balance of the commit or credit. Adding all of the entries in a ledger results in the total remaining balance associated with that ledger. For example, there are ledger entries associated with the `access_schedule` beginning, invoice deductions (drawdowns of the credit or commit corresponding to usage), and expirations.

Each ledger entry is associated with a `type`, an `amount` (which can be positive or negative), and an effective `timestamp`. There is one invoice deduction ledger entry for each invoice that consumes a credit or commit. The `timestamp` associated with invoice deduction ledger entries is always the end of the service period associated with the usage invoice. Use the `timestamp` to show customers their remaining balance including pending charges, or excluding pending charges.

### Example ledger

Consider an example where a customer is issued a \$100 credit with one access segment from September 01, 2024 through October 01, 2024. During the month of September, the customer consumed \$63 of the credit. The remaining credit balance expired after October 01.

As a result, this credit has three ledger entries:

<CardGroup cols={1}>
  <Card>
    <table style={{ width: '100%', borderCollapse: 'collapse' }}>
      <thead>
        <tr>
          <th style={{ borderBottom: '1px solid #ccc', textAlign: 'left', padding: '8px' }}>Type</th>
          <th style={{ borderBottom: '1px solid #ccc', textAlign: 'left', padding: '8px' }}>Timestamp</th>
          <th style={{ borderBottom: '1px solid #ccc', textAlign: 'left', padding: '8px' }}>Amount</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>credit\_segment\_start</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>9/1/2024</td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>+\$100</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>credit\_automated\_invoice\_deduction</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>10/1/2024</td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>-\$63</td>
        </tr>

        <tr>
          <td style={{ padding: '8px' }}><code>credit\_segment\_expiration</code></td>
          <td style={{ padding: '8px' }}>10/1/2024</td>
          <td style={{ padding: '8px' }}>-\$37</td>
        </tr>
      </tbody>
    </table>
  </Card>
</CardGroup>

### Manual ledger entries

You may want to adjust a credit or commit's ledger to account for mistakes, migrate existing customers with outstanding balances to Metronome, or many other reasons. Apply positive or negative adjustments to a credit or commit's ledger through the [Metronome app](https://app.metronome.com/) or API using the [`/addManualBalanceLedgerEntry`](/api-reference/credits-and-commits/add-a-manual-balance-entry) endpoint.

### Credit ledger entry types

<CardGroup cols={1}>
  <Card>
    <table style={{ width: '100%', borderCollapse: 'collapse' }}>
      <thead>
        <tr>
          <th style={{ borderBottom: '1px solid #ccc', textAlign: 'left', padding: '8px' }}>Type</th>
          <th style={{ borderBottom: '1px solid #ccc', textAlign: 'left', padding: '8px' }}>Description</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>credit\_segment\_start</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents that a credit segment started and the customer now has access to the usage amount for that segment. The access schedule of the credit describes these segments.</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>credit\_automated\_invoice\_deduction</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents deductions from the credit segment caused by a usage invoice that included usage applicable to this credit.</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>credit\_segment\_expiration</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents the unused credit amount that expired at the end of a credit segment.</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>credit\_manual</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents a manual ledger entry added to a credit.</td>
        </tr>

        <tr>
          <td style={{ padding: '8px' }}><code>credit\_seat\_based\_adjustment</code></td>
          <td style={{ padding: '8px' }}>Represents the additional credit associated with a seat increment when using recurring credits linked to a subscription</td>
        </tr>
      </tbody>
    </table>
  </Card>
</CardGroup>

### Commit ledger entry types

<CardGroup cols={1}>
  <Card>
    <table style={{ width: '100%', borderCollapse: 'collapse' }}>
      <thead>
        <tr>
          <th style={{ borderBottom: '1px solid #ccc', textAlign: 'left', padding: '8px' }}>Type</th>
          <th style={{ borderBottom: '1px solid #ccc', textAlign: 'left', padding: '8px' }}>Description</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>postpaid\_initial\_balance</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents the starting balance of a postpaid commit.</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>postpaid\_automated\_invoice\_deduction</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents deductions from the remaining obligation of the postpaid commit as the result of an invoice with usage that applies to this commit.</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>postpaid\_trueup</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents a true-up invoice issued for this commit to cover usage not covered by automated usage invoices.</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>postpaid\_rollover</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents unused usage from the postpaid commit which was rolled over to a new contract.</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>postpaid\_manual</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents a manual ledger entry added to a postpaid commit.</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>postpaid\_commit\_expiration</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents commit amount unused and expired at the end of a commit segment. Does not include usage that rolled over to a new contract.</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>prepaid\_segment\_start</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents that a prepaid commit segment started and the customer now has access to the usage amount for that segment. The access schedule of the prepaid commit describes these segments.</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>prepaid\_automated\_invoice\_deduction</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents deductions from the prepaid commit segment caused by a usage invoice that included usage applicable to this commit.</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>prepaid\_rollover</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents unused usage from the prepaid commit that rolled over to a new contract.</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>prepaid\_segment\_expiration</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents commit amount unused and expired at the end of a commit segment. Does not include usage that rolled over to a new contract.</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>prepaid\_commit\_expiration</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents commit amount unused and expired at the end of a commit segment. Does not include usage that rolled over to a new contract.</td>
        </tr>

        <tr>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}><code>prepaid\_manual</code></td>
          <td style={{ borderBottom: '1px solid #eee', padding: '8px' }}>Represents a manual ledger entry added to a prepaid commit.</td>
        </tr>

        <tr>
          <td style={{ padding: '8px' }}><code>prepaid\_commit\_seat\_based\_adjustment</code></td>
          <td style={{ padding: '8px' }}>Represents the additional commit associated with a seat increment when using recurring commits linked to a subscription</td>
        </tr>
      </tbody>
    </table>
  </Card>
</CardGroup>
