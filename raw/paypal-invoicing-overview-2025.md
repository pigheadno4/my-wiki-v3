<!-- Source URL: https://docs.paypal.ai/growth/grow-business/invoicing -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

PayPal Invoicing lets merchants and partners create and send itemized invoices and get paid through a secure PayPal payment page, without building their own payment flow. Customers can pay using PayPal, major credit and debit cards, and other eligible payment methods, often without needing a PayPal account, depending on regional availability. Merchants can share invoices via a secure URL, merchant-branded email, or scannable QR code, and configure automatic payment reminders.

### Invoicing vs Payment Link

Use the following table to compare PayPal’s Invoicing and [Payment Links](/payments/pay-links-buttons), and choose the option that best matches your needs.

|                                                                                            | Invoicing                                                                             | Payment Links                                                             |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Description                                                                                | Use Invoicing to collect one-time or recurring payments from a specific customer      | Use Payment Links to sell a product, service, or accept a donation or tip |
| Customer                                                                                   | Specific individual or business                                                       | Anyone with the link                                                      |
| Reusability                                                                                | One invoice per transaction                                                           | Reuse the same link multiple times                                        |
| Integration options                                                                        | Business Dashboard or API                                                             | Business Dashboard or API                                                 |
| Sharing options                                                                            | Email invoice, share hosted invoice link, or provide a QR code that opens the invoice | Share link through email, SMS, or social channels                         |
| Customization                                                                              | Invoice branding and business details.                                                | Limited checkout customization                                            |
| Payment methods                                                                            | PayPal, Pay Later, Venmo, Debit or Credit Cards, Apple Pay, and Pay by Bank (ACH)     | PayPal, cards, and eligible local methods                                 |
| Recurring payments                                                                         | One-time invoices                                                                     | One-time payments only                                                    |
| Collection tools                                                                           | Invoice reminders and status tracking                                                 | Not supported                                                             |
| Customers can choose what to pay                                                           | ❌                                                                                    | ✅                                                                        |
| Hosted payment page                                                                        | ✅                                                                                    | ✅                                                                        |
| Partial payments                                                                           | ✅                                                                                    | ❌                                                                        |
| Discounts                                                                                  | ✅                                                                                    | ✅                                                                        |
| Taxes                                                                                      | ✅                                                                                    | ✅                                                                        |
| [PCI compliance handling](https://www.paypal.com/us/brc/article/pci-dss-compliance-basics) | ✅                                                                                    | ✅                                                                        |

<Columns>
  <Card title="How Invoicing works" href="/growth/grow-business/invoicing/lifecycle">
    Learn what happens after you create and send an invoice, including how customers pay, what you can change along the way, and how to track the final outcome.
  </Card>

  <Card title="Choose Invoicing solution" href="/growth/grow-business/invoicing/choose-solution">
    Decide between using the PayPal dashboard or the Invoicing API by comparing setup effort, automation needs, invoice volume, and how invoices are created and managed.
  </Card>

  <Card title="Quick start" href="/growth/grow-business/invoicing/quickstart">
    Create and send an invoice from your Dashboard using just the essential fields—no code required.
  </Card>

  <Card title="Integrate Invoicing API" href="/growth/grow-business/invoicing/integrate">
    The Invoicing REST API lets you to create, update, send, and manage invoices programmatically from your backend systems.
  </Card>
</Columns>
