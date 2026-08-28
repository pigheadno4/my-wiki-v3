<!-- Source URL: https://docs.metronome.com/api-reference/introduction.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API Reference

Metronome powers your billing to ensure accurate invoices and enable easy pricing changes as you grow.

Our APIs support idempotency, pagination, and customer fields to provide robust flexibility and reliability at any scale. To get started, read our [API Quickstart](/api-reference/api-quickstart), learn more about [How Metronome Works](/guides/get-started/how-metronome-works), or check out our SDKs:

<Columns cols={4}>
  <Card title="Python" href="https://github.com/Metronome-Industries/metronome-python/blob/main/README.md" />

  <Card title="Go" href="https://github.com/Metronome-Industries/metronome-go/blob/main/README.md" />

  <Card title="Ruby" href="https://github.com/Metronome-Industries/metronome-ruby/blob/main/README.md" />

  <Card title="Node.js" href="https://github.com/Metronome-Industries/metronome-node/blob/main/README.md" />

  <Card title="Java" href="https://github.com/Metronome-Industries/metronome-java/blob/main/README.md" />
</Columns>

<span class="apiReferenceHeader">
  # Endpoints
</span>

<span id="homeTopCards">
  <Columns cols={3}>
    <Card title="Usage" href="/api-reference/usage/ingest-events">
      Send usage events from your application.
    </Card>

    <Card title="Billable Metrics" href="/api-reference/billable-metrics/create-a-billable-metric">
      Convert raw usage events into invoice quantities.
    </Card>

    <Card title="Products" href="/api-reference/products/create-a-product">
      Define line items on an invoice.
    </Card>

    <Card title="Rate cards" href="/api-reference/rate-cards/create-a-rate-card">
      Set your base prices.
    </Card>

    <Card title="Customers" href="/api-reference/customers/create-a-customer">
      Represent your customer relationships.
    </Card>

    <Card title="Contracts" href="/api-reference/contracts/create-a-contract">
      Define invoice behavior for a given customer.
    </Card>

    <Card title="Packages" href="/api-reference/contracts/create-a-package">
      Reusable, time-relative sets of contract terms.
    </Card>

    <Card title="Commits and Credits" href="/api-reference/credits-and-commits/create-a-commit">
      Modify invoice amounts.
    </Card>

    <Card title="Invoices" href="/api-reference/invoices/get-an-invoice">
      A set of charges for a single billing cycle.
    </Card>

    <Card title="Notifications" href="/api-reference/alerts/create-a-threshold-notification">
      Power workflows based on state from Metronome.
    </Card>
  </Columns>
</span>
