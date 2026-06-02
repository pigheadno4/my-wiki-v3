<!-- Source URL: https://docs.paypal.ai/payments/ -->
<!-- Fetched: 2026-04-16 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Payment Links and Buttons

Use PayPal Payment Links and Buttons to accept payments without building your own payment flow. Create shareable payment links, add buy buttons to your website, or generate QR codes for in-person sales. Customers complete their purchase on a secure PayPal payment page, and funds are deposited into your PayPal business account.

Payment Links and Buttons support PayPal, Pay Later, Venmo, Apple Pay, and major debit and credit cards. Payments are available in more than 200 [countries and regions](https://docs.paypal.ai/reference/codes/country-codes), across multiple [languages](https://docs.paypal.ai/reference/codes/locale-codes), and in more than 23 [currencies](https://docs.paypal.ai/reference/codes/currency-codes). You can customize the payment page with product details and images, allow customers to set an amount when appropriate, and rely on PayPal to handle PCI compliance requirements.

## Choose a payment option

Each option supports different payment scenarios and integration approaches.

| **Options**              | **Best for**                                                                                  | Setup requirement                                                    | **Use case**                                                                                                                                   |
| :----------------------- | :-------------------------------------------------------------------------------------------- | :------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| **Payment Link**         | Accepting payments by sharing a link on social media, email, or through messages              | No-code                                                              | Share a payment link with customers so they can complete payments online.​                                                                     |
| **Buy Button**           | Selling a specific product or service with a direct payment option on your website            | No-code<br /> Requires a website and basic knowledge of editing HTML | Copy the generated Buy Button code into your website so customers can proceed directly to payment for a specific item.​                        |
| **Shopping Cart Button** | Selling multiple products and allowing customers to purchase them together in one transaction | No-code<br /> Requires a website and basic knowledge of editing HTML | Copy the generated Add to Cart and View Cart button code into your website so customers can purchase multiple items in a single transaction.​​ |
| **QR Code**              | Accepting in-person or contactless payments without building a website                        | No-code                                                              | Generate QR codes that link to PayPal-hosted checkout for contactless payments.​                                                               |

To get started, [build now](https://www.paypal.com/signin?returnUri=https%3A%2F%2Fwww.paypal.com%2Fncp%2Flinks%2Fcreate) with Payment Links and Buttons.

## Choose between Invoicing and Payment Links

If you send bills or collect payments, compare Payment Links and Invoicing in the following table and choose the option that best fits your workflow.

|                                                                                                | Payment Links                                                             | Invoicing                                                                                 |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Description**                                                                                | Use Payment Links to sell a product, service, or accept a donation or tip | Use Invoicing to collect one-time or recurring payments from a specific customer          |
| **Customer**                                                                                   | Anyone with the link                                                      | Specific individual or business                                                           |
| **Reusability**                                                                                | Reuse the same link multiple times                                        | One invoice per transaction                                                               |
| **Integration options**                                                                        | Business Dashboard or API                                                 | Business Dashboard or API                                                                 |
| **Sharing options**                                                                            | Share link through email, SMS, or social channels                         | Email invoice, share the hosted invoice link, or provide a QR code that opens the invoice |
| **Customization**                                                                              | Basic checkout customization is available                                 | Invoice branding and business details                                                     |
| **Payment methods**                                                                            | PayPal, Pay Later, Venmo, Apple Pay, and major debit and credit cards     | PayPal, Pay Later, Venmo, Debit or Credit Cards, Apple Pay, and Pay by Bank (ACH)         |
| **Recurring payments**                                                                         | One-time payments only                                                    | One-time invoices                                                                         |
| **Collection tools**                                                                           | Not supported                                                             | Invoice reminders and status tracking                                                     |
| **Customers can choose what to pay**                                                           | ✓                                                                         | ✕                                                                                         |
| **Hosted payment page**                                                                        | ✓                                                                         | ✓                                                                                         |
| **Partial payments**                                                                           | ✕                                                                         | ✓                                                                                         |
| **Discounts**                                                                                  | ✓                                                                         | ✓                                                                                         |
| **Taxes**                                                                                      | ✓                                                                         | ✓                                                                                         |
| **[PCI compliance handling](https://www.paypal.com/us/brc/article/pci-dss-compliance-basics)** | ✓                                                                         | ✓                                                                                         |

<Columns>
  <Card title="Choose your integration option" href="/payments/choose-integration-option">
    Compare dashboard and API options for creating and managing payment links so you can pick the right balance of control, effort, and automation for your setup.
  </Card>

  <Card title="Create a payment link" href="/payments/create-pay-link">
    Create payment links in your PayPal business account and use them in emails, social posts, or on your site without writing code.
  </Card>
</Columns>
