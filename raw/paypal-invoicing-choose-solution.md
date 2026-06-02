<!-- Source URL: https://docs.paypal.ai/growth/grow-business/invoicing/choose-solution -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Choose Invoicing solution

PayPal Invoicing supports two ways to create and manage invoices:

- [PayPal Invoicing (Dashboard)](/growth/grow-business/invoicing/quickstart) – Manual invoice creation in the PayPal dashboard
- [Invoicing REST API](/growth/grow-business/invoicing/integrate) – Programmatic invoice creation and automation through backend integration

The key difference between these options is how invoices are created, sent, and tracked: either manually in the Dashboard, programmatically in your application, or a mix of both.

<Columns>
  <Card title="PayPal Invoicing (Dashboard)" href="/growth/grow-business/invoicing/quickstart">
    PayPal Invoicing (Dashboard) lets you to create, send, and manage invoices directly from your PayPal business account without writing code.
  </Card>

  <Card title="Invoicing API" href="/growth/grow-business/invoicing/quickstart-api">
    The Invoicing REST API lets you to create, update, send, and manage invoices programmatically from your backend systems.
  </Card>
</Columns>

All invoices, regardless of how they are created, are accessible in the PayPal dashboard for tracking and management. The primary difference between these options is how invoices are created and updated: manually in the dashboard or programmatically through your application.

## Comparision

| Category                     | PayPal Invoicing (Dashboard)                                                                                                                              | Invoicing REST API                                                                                                                                        |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Who should use it            | Businesses that want a no-code solution and manually create invoices from the PayPal dashboard <br />Ideal for low to moderate invoice volume             | Businesses that need automated invoicing, higher invoice volumes, or integration with backend systems such as ERP, CRM, or SaaS platforms                 |
| How invoices are created     | Manually in the PayPal dashboard                                                                                                                          | Programmatically via REST API calls from your backend                                                                                                     |
| Technical requirements       | No development required                                                                                                                                   | Requires backend development and REST API integration <br />Uses OAuth 2.0 authentication                                                                 |
| Automation                   | Limited to dashboard-based workflows                                                                                                                      | Full automation of invoice creation, sending, reminders, and reconciliation                                                                               |
| Invoice lifecycle management | Manage invoices in the PayPal dashboard (status tracking, reminders, refunds, offline payments)                                                           | Manage invoices via API and webhooks <br />Invoices are also visible in the PayPal dashboard for operational support                                      |
| Payer experience             | PayPal-managed payment workflow with multiple payment methods such as PayPal, debit and credit cards, digital wallets, and eligible local payment methods | PayPal-managed payment workflow with multiple payment methods such as PayPal, debit and credit cards, digital wallets, and eligible local payment methods |
