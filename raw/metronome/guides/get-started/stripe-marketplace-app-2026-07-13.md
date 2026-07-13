<!-- Source URL: https://docs.metronome.com/guides/get-started/stripe-marketplace-app.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage contracts in Stripe

Use the Metronome Stripe App to create and manage usage-based contracts directly from the Stripe Dashboard. The app connects your Metronome account to Stripe, giving you a unified view of customers, revenue, and contracts without leaving Stripe.

This guide describes how to install and set up the Metronome Stripe App, manage customers and contracts, and use the app's revenue dashboard.

## Prerequisites

Before you begin, make sure you have:

* A [Metronome account](https://signup.metronome.com) with at least one production environment configured
* A Stripe account with access to the [Stripe Dashboard](https://dashboard.stripe.com)
* The [Stripe integration](/integrations/invoice-integrations/stripe) configured in Metronome

<Info>
  **INFO**

  The Metronome Stripe App manages contracts and customers through Metronome's interface embedded in the Stripe Dashboard. Invoicing still flows through Metronome's native Stripe integration. Set up the [Stripe invoicing integration](/integrations/invoice-integrations/stripe) first to ensure invoices created by your contracts reach Stripe.
</Info>

## Install the app

1. Go to the [Metronome listing](https://marketplace.stripe.com/apps/metronome) on the Stripe App Marketplace.
2. Click **Install app** and follow the prompts.
3. After installation, the Metronome app is accessible from the Stripe Dashboard.

## Sign in to Metronome

After installing the app, sign in to connect your Metronome account:

1. Open the Metronome app from the Stripe Dashboard.
2. Click **Sign in to Metronome**.
3. Complete the authentication flow.

## Overview dashboard

The Overview tab provides a snapshot of your usage-based billing:

* **Total revenue**: All-time billed amount across your Metronome contracts.
* **Revenue last month**: Billed amount for the most recent billing period.
* **Top products**: Your highest-revenue products, with remaining products grouped under "Other."
* **Usage events**: A 30-day trend of [usage events](/guides/events/send-usage-events) ingested by Metronome, with separate series for total and duplicate events.
* **Customers**: New customers added in the last month.

The Overview tab also includes links to open the Metronome app and Metronome documentation.

## Manage customers

The Customers tab displays all Stripe customers that are linked to Metronome customers. For each customer, the app shows:

* **Date created**: When the customer was added based on the Stripe creation date.
* **Lifetime billings**: Total amount billed to the customer.
* **Provision status**: The state of the customer's contracts — Active, Active Soon, or Recently Ended.

From any customer row, you can:

* **View Customer** in Stripe to see their full Stripe profile.
* **Manage in Metronome** to open the customer in the Metronome dashboard for advanced configuration.
* **Create Contract** to start the contract creation flow for that customer.

If a Stripe customer is linked to multiple Metronome customers, the **Manage in Metronome** and **Create Contract** actions expand into sub-menus so you can select which Metronome customer to act on.

### Customer detail view

When you view a Stripe customer's detail page, the Metronome module displays all [contracts](/guides/get-started/core-concepts/provision-contract) linked to that customer. Each contract shows the contract name (falling back to the rate card name if unnamed), the contract period with an "(Active)" indicator when applicable, and the products included in the contract.

If the Stripe customer does not yet have a corresponding Metronome customer, the app automatically [creates one](/guides/get-started/core-concepts/provision-customer) using the Stripe customer name when you initiate contract creation.

## Create a contract

The contract creation flow is a four-step wizard that guides you through building a usage-based [contract](/guides/get-started/core-concepts/provision-contract).

### Step 1: Invoicing

Configure the core contract terms:

* **Contract name**: A descriptive name for the contract.
* **Start date**: When the contract begins. Defaults to today.
* **End date** (optional): When the contract ends. Leave blank for open-ended contracts.
* **Invoice schedule**: How often [usage invoices](/guides/get-started/core-concepts/how-invoicing-works) are generated — Monthly, Quarterly, Annual, or Weekly.
* **Send on**: When invoices are sent — the 1st of the month or the contract start date.
* **Net payment terms**: The number of days a customer has to pay after an invoice is issued. Defaults to 30.

### Step 2: Pricing

Select a rate card and optionally customize pricing for this contract:

* **Rate card**: Choose from your configured Metronome [rate cards](/guides/get-started/core-concepts/create-manage-rate-cards). The rate card defines the base pricing for all products on the contract.
* **Price overrides**: Apply discount percentages to specific products, scoped by [product tags](/guides/get-started/core-concepts/create-products-contracts) and date range.

<Tip>
  **TIP**

  You can see which products have which product tags by hovering over their name in the table.
</Tip>

* **Subscription quantities**: If the rate card includes subscription products, set the initial quantity for each subscription line item.
* **Prices**: After selecting a rate card, view a summary of all products and their effective prices, including any overrides applied. You can check or uncheck individual products to override their entitlement on this contract.

<Tip>
  **TIP**

  To set discounts, your products must have [product tags](/guides/get-started/core-concepts/create-products-contracts) configured in Metronome. If multiple tags are selected, the override applies only to products that have **all** of the selected tags.
</Tip>

### Step 3: Credits

Add [credits](/guides/pricing-packaging/apply-credits-and-commits/create-a-pre-paid-commit) to the contract.

* **Credit**: The name that will be used on the invoice line item when this credit is applied. (This comes from a Fixed Product defined in Metronome.)
* **Applicable product tags** (optional): Restrict which [products](/guides/get-started/core-concepts/create-products-contracts) can draw from this credit. If omitted, all usage products on the contract consume the credit.
* **Schedule**: How \[credits]\(/guides/pricing-packaging/apply-credits-and-commits/create-a-pre-paid-commit) are allocated:
  * **One-time**: A single allocation with a start date and end date.
  * **Monthly**: A recurring allocation with a start date and optional end date.
  * **Custom**: Multiple segments, each with its own start date, end date, and amounts.
* **Invoice amount**: What the customer is charged for the credit.
* **Credit amount**: The usage amount the customer receives.

### Step 4: Confirmation

Click **Create contract** to finalize. The contract is created with the Stripe customer's existing billing provider configuration, so invoices flow to Stripe automatically.

## Troubleshooting

### Authentication errors

If you see "There was an error signing in to Metronome," try these steps:

1. Go to the app **Settings** page and click **Clear cached Metronome credentials** under Developer settings.
2. Go to [app.metronome.com](http://app.metronome.com)/logout and log out.
3. Navigate back to the Metronome Stripe App and click “Sign in”

### Missing customers

The Customers tab only displays Stripe customers that have a corresponding Metronome customer linked via the Stripe billing configuration in the currently connected Metronome account. If a customer doesn't appear:

* Verify you are logged in to the correct Metronome account.
  * See Authentication errors above to sign out and sign back in
* Verify the customer exists in Metronome with a Stripe billing configuration.
* Confirm the `stripe_customer_id` in the Metronome billing configuration matches the Stripe customer ID.

### Stripe account not linked

If you see "The Metronome account you've connected is not linked to this Stripe account," the Stripe integration has not been configured in your Metronome environment. Set up the [Stripe invoicing integration](/integrations/invoice-integrations/stripe) in Metronome before using the app.

For persistent issues, contact [support@metronome.com](mailto:support@metronome.com).
