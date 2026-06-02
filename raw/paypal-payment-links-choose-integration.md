<!-- Source URL: https://docs.paypal.ai/payments/choose-integration-option -->
<!-- Fetched: 2026-04-16 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Choose integration option

You can create and manage payment links in two ways: through the PayPal business dashboard or by using the Payment Links and Buttons API. This page helps you choose the option that fits your setup and level of control.

> **Note**: The Payment Links and Buttons API supports payment links only. Buy buttons and shopping cart buttons are created and managed in the dashboard.

<Columns>
  <Card title="UI Editor" href="/payments/create-pay-link">
    Create payment links and buttons in the PayPal dashboard and use them in emails, social posts, or on your site without writing code.
  </Card>

  <Card title="Payment Links and Buttons API" href="/payments/pay-links-buttons-api">
    Use a REST API to create and manage payment links from your application and use them wherever you accept payments.
  </Card>
</Columns>

The key difference between these options is how payment links are created, managed, and controlled, whether manually in the dashboard or programmatically in your application.

|                       | UI Editor                                                                                                                                                  | API                                                                                                                                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Who should use it** | Best for merchants who want to create and manage payment links or buttons without writing code.                                                            | Best for merchants and platforms that want to create and manage payment links programmatically from their applications and have experience with REST APIs and backend development. |
| **How it works**      | You create and customize links or buttons in the dashboard, then use the generated link or button code on your website or other channels.                  | Your application calls the Payment Links and Buttons API to create and manage payment links. You store and use the returned URLs within your own payment flows.                    |
| **Key benefits**      | <ul><li>No backend development required</li><li>Create and manage links and buttons manually</li><li>Suitable for low-to-medium volume use cases</li></ul> | <ul><li>Automate link creation and updates</li><li>Manage links from your application and deployment workflows</li><li>Suitable for high-volume or dynamic use cases</li></ul>     |
