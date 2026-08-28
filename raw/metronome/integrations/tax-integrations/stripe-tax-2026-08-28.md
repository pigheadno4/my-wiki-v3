<!-- Source URL: https://docs.metronome.com/integrations/tax-integrations/stripe-tax.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Stripe Tax

> Learn how to configure Stripe Tax with Metronome for automatic sales tax calculation on Stripe invoices.

[Stripe Tax](https://docs.stripe.com/tax) is Stripe's native tax calculation engine. When configured, Stripe automatically calculates and applies sales tax to invoices that Metronome creates in Stripe.

<Note>
  This page covers **Stripe Tax**—Stripe's own tax product. If you use **Anrok** or **Avalara** through the [Stripe Tax integration](https://docs.stripe.com/tax/third-party-apps), see [Anrok setup](/integrations/tax-integrations/anrok) or [Avalara setup](/integrations/tax-integrations/avalara).
</Note>

## Prerequisites

Before you begin:

1. [Activate and set up Stripe Tax](https://docs.stripe.com/tax/set-up) in your Stripe dashboard under **Settings > Tax**.
   1. [Complete tax registration](https://docs.stripe.com/tax/registering) in the applicable jurisdictions for sales tax, VAT, and GST.
2. [Connect your Stripe account](/integrations/invoice-integrations/stripe) to Metronome.
3. Link each Metronome customer to their Stripe customer ID.
4. Ensure each Stripe customer has a [**Customer Address**](https://docs.stripe.com/api/customers/object#customer_object-address) set and is marked as **Taxable**.
5. Once you've completed initial setup, contact us via the [Metronome support portal](https://support.metronome.com/) to enable tax application on your account.

<Note>
  The Customer Address field is the `address` object on the [Stripe Customer object](https://docs.stripe.com/api/customers/object#customer_object-address), which determines tax jurisdiction. Failure to assign a Customer Address results in failure to apply tax.
</Note>

## Step 1: Create Stripe products

Stripe Tax uses the **product** on each invoice line item to [determine the applicable tax code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior) and rate. Create at least one Stripe product and assign the appropriate [tax code](https://docs.stripe.com/tax/tax-codes) to it in Stripe (under **Product Settings > Tax code**).

You can map multiple Metronome products to the same Stripe product as long as they share the same tax code. Create additional Stripe products only when you need a different tax classification.

<Note>
  If no tax code is specified on a product, Stripe Tax falls back to the account-level preset product tax code set under the **Preset product category** section in the [Stripe Dashboard](https://dashboard.stripe.com/settings/tax).
</Note>

## Step 2: Create the Stripe Product ID custom field in Metronome

Create a [custom field](/api-reference/custom-fields) on the **Product** entity in Metronome to store the Stripe product ID:

1. Go to **General Settings > Custom fields** (or use the Custom fields API).
2. Create a new custom field:
   * **Entity**: Product
   * **Key**: `stripe_product_id`
3. For each Metronome product, set the `stripe_product_id` value to the corresponding Stripe product ID (for example, `prod_ABC123`).

<Warning>
  **Do not** enable "Enforce uniqueness" (`enforce_uniqueness`). The same Stripe product ID is intentionally reused across multiple Metronome products. Enabling uniqueness can't be undone—you would need to archive the field and create a new one.
</Warning>

## Step 3: Configure entity mapping

Set up the entity mapping so Metronome passes the product ID to Stripe on each invoice line item:

1. Go to **Developer > Integrations > Stripe > Edit Mapping**.
2. Add the following mapping:

| Stripe vendor entity | Stripe vendor key | Metronome entity  | Metronome key       |
| -------------------- | ----------------- | ----------------- | ------------------- |
| `invoiceitem.price`  | `product`         | `ContractProduct` | `stripe_product_id` |

3. Click **Save**.

**Optional: Additional entity mappings**

If you need to pass additional metadata, you can add more mappings:

| Metronome entity            | Stripe entity            | Use case                                                               |
| --------------------------- | ------------------------ | ---------------------------------------------------------------------- |
| Product (any custom field)  | `invoiceitem.metadata.*` | Pass line-item-level metadata (for example, `TaxCode`)                 |
| Customer (any custom field) | `invoice.metadata.*`     | Pass invoice-level metadata (for example, customer tax classification) |

## Test your configuration

After completing tax setup:

1. Create a test customer in your sandbox environment with a valid Stripe customer.
2. Generate an invoice in Metronome.
3. Check the corresponding Stripe invoice to confirm tax has been calculated and applied.

If tax isn't being calculated, verify:

* Stripe Tax is [**enabled**](https://docs.stripe.com/tax/set-up) in your Stripe dashboard.
* The Stripe customer has a **Customer Address** and is **Taxable**.
* The entity mapping is saved and the `stripe_product_id` custom field has values set on your Metronome products.
* The Stripe product has a valid [**tax code**](https://docs.stripe.com/tax/tax-codes) assigned.

<Note>
  If automated tax isn't applying on the synced Stripe invoices, contact us via the [Metronome support portal](https://support.metronome.com/).
</Note>

## Threshold billing

For customers using [prepaid balance thresholds](/guides/customers-billing/optimize-customer-experience/prepaid-balance-thresholds) or spend thresholds, tax is configured differently than for arrears invoices.

<Warning>
  The account-level tax enablement does **not** apply to threshold billing—you must explicitly set the tax type in the API.
</Warning>

When setting up the `payment_gate_config`, specify `tax_type: "STRIPE"` and `"payment_type": "INVOICE"`:

```json theme={null}
{
  "prepaid_balance_threshold_configuration": {
    "is_enabled": true,
    "threshold_amount": 500,
    "recharge_to_amount": 1500,
    "commit": {
      "product_id": "<your-product-id>",
      "name": "Auto-recharge credits"
    },
    "payment_gate_config": {
      "payment_gate_type": "STRIPE",
      "tax_type": "STRIPE",
      "stripe_config": {
        "payment_type": "INVOICE"
      }
    }
  }
}
```

The same applies when adding one-off payment-gated commits through the edit contract endpoint.

For spend thresholds, the configuration is similar:

```json theme={null}
{
  "spend_threshold_configuration": {
    "is_enabled": true,
    "threshold_amount": 5000,
    "commit": {
      "product_id": "<your-product-id>"
    },
    "payment_gate_config": {
      "payment_gate_type": "STRIPE",
      "tax_type": "STRIPE",
      "stripe_config": {
        "payment_type": "INVOICE"
      }
    }
  }
}
```

## Settings that affect tax

### Collection method: charge\_automatically versus send\_invoice

Both collection methods work with all tax providers. The collection method determines what happens after the invoice is finalized with tax:

* `charge_automatically`—Stripe charges the customer's [default payment method](https://docs.stripe.com/api/customers/update#update_customer-invoice_settings-default_payment_method) on file. The customer must have a default payment method set in Stripe before the invoice is finalized, or payment will fail. The customer doesn't receive an invoice email by default (but you can enable [Successful Payments](https://docs.stripe.com/invoicing/automatic-charging) for receipt emails in Stripe).
* `send_invoice`—Stripe emails the invoice to the customer with payment instructions. You must specify `days_until_due`.

<Info>
  Tax is applied regardless of collection method. The choice between these methods is independent of your tax configuration.
</Info>

### Leave invoices as drafts

This setting (under **Developer > Integrations > Stripe > Settings**) controls whether Metronome immediately finalizes invoices in Stripe or leaves them as drafts. Stripe's [automatic tax](https://docs.stripe.com/tax) calculates tax inline when the invoice is finalized. It is generally recommended to switch this preference to **OFF** for automatic tax calculation upon invoice syncing.

If you prefer to leave invoices as draft so you can review and finalize manually in Stripe, mark the "leave invoices as drafts" option in Metronome.

## FAQ and troubleshooting

**Q: Can I reuse the same Stripe product for multiple Metronome products?**

Yes, as long as they share the same [tax code](https://docs.stripe.com/tax/tax-codes). If your products are taxed differently, create separate Stripe products with different tax codes.

**Q: Why is my threshold billing invoice not calculating tax?**

The account-level tax enablement only applies to arrears invoices. For threshold billing, you must set `tax_type: "STRIPE"` in the `payment_gate_config` when creating or editing the contract. See the [Threshold billing](#threshold-billing) section above.

**Q: My invoices are failing or are finalizing without tax -- what should I check?**

The most common causes are a missing [Customer Address](https://docs.stripe.com/api/customers/object#customer_object-address) on the Stripe customer or an incomplete entity mapping in Metronome. Start by confirming that the Stripe customer has sufficient location information to accurately calculate tax rates for the customer. Next, check if the entity mapping is complete in Metronome. If both are verified and tax still isn't being applied, contact us via the [Metronome support portal](https://support.metronome.com/) to check your account configuration.

**Q: Do I need to set a default tax behavior in Stripe?**

In the Stripe dashboard, make sure that you have a default tax behavior selected to ensure tax is correctly added to each invoice.
