<!-- Source URL: https://docs.metronome.com/guides/implement-metronome/production-checklist.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Metronome go-live checklist

export const Checklist = ({children}) => {
  return <>
            <style>
                {`
          .custom-checklist-from-snippet {
            list-style: none !important;
            padding-left: 0 !important;
            margin-top: 1rem;
            margin-bottom: 1rem;

          }
          .custom-checklist-from-snippet li {
            position: relative;
            padding-left: 2rem !important;
            margin-bottom: 0.75rem;
          }
          .custom-checklist-from-snippet li::before {
            content: '';
            position: absolute;
            left: 0;
            top: 5px;
            width: 16px;
            height: 16px;
            border: 2px solid rgb(var(--gray-400));
            background: none !important;
            border-radius: 3px;
            display: inline-block;
          }
          .custom-checklist-from-snippet li > ul {
              padding-left: 0rem !important;
              margin-top: 0rem !important;
              list-style-type: disc !important;
          }
          .custom-checklist-from-snippet li > ul> li {
              padding-left: 0rem !important;
          }
          

          .custom-checklist-from-snippet li > ul li::before {
              display: none;
          }
        `}
            </style>
            <ul className="custom-checklist-from-snippet">
                {children}
            </ul>
        </>;
};

A go-live readiness checklist to validate your Metronome billing integration before launching in production.

## Validate usage and metering

Invoice accuracy starts with usage ingestion. Verifying and matching required [usage event](/guides/events/design-usage-events) fields to active [billable metrics](/guides/get-started/core-concepts/create-billable-metrics/) ensures customers are charged what they used.

Verify and check that:

<Checklist>
  * all required event [fields](/api-reference/usage/ingest-events) are present:
    * `transaction_id`
    * `customer_id` (or alias)
    * `timestamp`
    * `event_type`
    * `properties`
      Follow a maximalist approach for properties: send as much metadata as possible, even if not pricing-relevant today, to future-proof your integration.
  * [idempotency](/api-reference/idempotency) is enabled for ingest events via [`transaction_id`](/guides/get-started/core-concepts/send-usage-events#heartbeat-event-idempotence%E2%80%8B). Visit the docs [here](/guides/get-started/core-concepts/send-usage-events#heartbeat-event-idempotence%E2%80%8B) for guidance on choosing a good `transaction_id`.
  * billable metrics are active and correctly match events by sampling Metronome’s [searchEvents](/api-reference/usage/search-events) endpoint.
  * usage events are queued through a reliable message queue (e.g., SQS, RabbitMQ) and that backdated usage up to 14 days is correctly ingested.
  * the ingestion pipeline is load tested to handle expected peak throughput.
  * fault injection tests are performed by simulating ingestion failures. Coordinate with  Metronome if you need help setting this up.
</Checklist>

***

## Confirm pricing and product setup

Pricing accuracy is critical. Double-check that [rate cards](/guides/get-started/core-concepts/create-manage-rate-cards) and overrides in production reflect your intended setup so invoices remain consistent and predictable.

Verify and check that:

<Checklist>
  * the correct [products](/guides/get-started/core-concepts/create-products-contracts) (usage, composite, subscription, fixed) are being used; and configure tags, conversions, and group keys.
  * usage products are mapped to the intended billable metric.
  * the rate card is correct (currency, products, tiers/changes).
</Checklist>

***

## Provision customers and contracts

[Customers](/guides/get-started/core-concepts/provision-customer) must exist in Metronome and be linked to [contracts](/guides/get-started/core-concepts/provision-contract) for billing to start. This mapping ensures all usage is attributed to the right account with the right pricing.

Verify and check that:

<Checklist>
  * customers are created and, optionally, the ingest aliases are mapped correctly.
  * contracts are provisioned against the correct rate card and billing frequency.
</Checklist>

***

## Verify invoicing and payment flows

Customers expect smooth, accurate billing. Confirm [invoices](/guides/get-started/core-concepts/how-invoicing-works) and payments are flowing correctly before launch.

Verify and check that:

<Checklist>
  * that the invoice lifecycle is understood by your teams (draft → grace period → finalized).
  * that the `invoice.finalized` webhook is enabled and tested.
  * the delivery path is confirmed for your chosen [integration](https://metronome.com/integrations).
</Checklist>

## Secure production environment

Before launch, ensure that you’re running against production credentials, not sandbox. Using the correct [API tokens](/api-reference/authorization) gives you the foundation for secure, auditable billing that finance can reconcile and trust.

Verify and check that:

<Checklist>
  * the production API token is created and stored securely.
  * IP [allowlisting](/guides/platform-configuration/allowlist) is enabled, if required.
  * all API endpoints point to production URLs (`https://api.metronome.com`)
</Checklist>

***

## Configure webhooks and error handling

Billing is only reliable if your system knows when things go wrong or statuses change. [Webhooks](https://docs.metronome.com/developer-resources/use-api/webhooks) keep your systems in sync (invoice finalization, alert triggers), and retry/backoff/error-handling ensure no usage or revenue is lost.

Verify and check that:

<Checklist>
  * the webhook endpoint is online and secured with signature verification using your Metronome webhook secret.
  * your retry/backoff policy is functional: retry on 5xx/network, backoff on 429, DLQ + alert on 4xx.
  * webhook processing is idempotent (safe on duplicate deliveries).
</Checklist>

***

## Set up monitoring

You can’t improve what you can’t see. Alerts keep you ahead of customer balance issues.

Verify and check that:

<Checklist>
  * spend, credit, and commit alerts are configured.
  * webhook notifications are firing for alerts in a timely manner.
  * monitoring is in place on webhook delivery and ingest error rates.
</Checklist>

***

## Configure data export

Data Export provides an auditable record of invoices, usage, and customer data outside Metronome. Enabling it ensures finance and RevOps can reconcile billing independently.

Verify and check that:

<Checklist>
  * Data Export is enabled for your production environment.
  * the export destination (e.g., warehouse, S3) is configured and receiving data.
  * sample exports contain the expected objects (invoices, customers, usage).
  * reconciliation processes are defined so finance can validate invoice data against exported usage.
</Checklist>

***

## Run final end-to-end test

Finally, simulate one end-to-end cycle in production. This gives confidence that invoices, totals, and payments line up in the real environment, to avoid exposing customers to errors.

<Checklist>
  * Verify and check that sandbox-to-production migration is complete.
  * Run a production dry run with a test customer: send events → confirm invoice totals → verify webhook → confirm successful payment processing.
  * Document rollback procedures in case of critical issues.
</Checklist>
