<!-- Source URL: https://docs.stripe.com/invoicing/hosted-invoice-page -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Hosted invoice page

Use the hosted invoice page to securely collect payment from your customers.

The hosted invoice page provides a secure, private URL where your customers can:

- View the details, amounts, and status of the invoice.
- Pay the invoice using any of the enabled payment methods.
- Download PDF copies of the invoice and receipt.
![](https://b.stripecdn.com/docs-statics-srv/assets/hosted-invoice-page.3f79f6d4ded5d51047ae2b16270c2c42.png)

A sample hosted invoice page

Stripe assigns all invoices a unique URL that you can send to your customer. We host these invoices, which means you can securely collect payments without any extra implementation code.

## Invoice URLs 

When you create and send an invoice, Stripe generates a unique URL for the hosted invoice page. The URL includes a secure, long, and random identifier, resembling the following example:

```missingLanguage
https://invoice.stripe.com/i/acct_abcdefghijklmno/test_YWNjdF8xRGZ3UzJDbENJS2xqV3ZzLF9MNGJvMDBzY0xFQ2c1cG1QZzZ6Wk5jV0RXR2lOS1V6LDM0Mjk3NjEz0200wpYOWgBE?s=em
```

Invoice URLs expire 30 days after the due date. If the invoice doesn’t have a due date, the invoice expires 30 days after it finalizes. In all cases, the expiration window is never longer than 120 days.

> Even after expiration, any URLs that the Dashboard displays or a user retrieves through the API are guaranteed to be valid for at least 10 days.

#### Dashboard

When a URL expires, it no longer loads the intended resource. Instead, Stripe redirects invoiced customers to a page that states that the URL has expired and to contact the business. This page also provides the business’s contact information.

> If you sent an invoice through the Dashboard or API, any email recipients are automatically associated with that invoice. In this case, Stripe redirects the user to a recovery page where they can enter their email address to receive a new copy of the original email with non-expired links.

#### API

While expired URLs normally redirect (302) to a recovery page, PDF download URLs are an exception. If Stripe detects that a non-browser client (for example, curl) has requested PDF download URLs, we return a 400 error with a `URL expired` body response. This allows integrations to more easily detect when an invoice URL has expired, and to retrieve a new working URL by re-requesting the invoice or credit note resource.

## Invoice email links 

You can configure the invoice email to include a link to the hosted invoice page. When enabled, the hosted invoice page URL appears in:

- Invoice emails as a payment link.
- The footer of invoice PDFs.
- The Invoice API response as [hosted_invoice_url](https://docs.stripe.com/api/invoices/object.md#invoice_object-hosted_invoice_url).

To enable the hosted invoice page for all newly created invoices, select the checkbox for **Include a link to a payment page in the invoice email** in the [Invoice settings](https://dashboard.stripe.com/settings/billing/invoice) of the Dashboard.

When sending an invoice, you can use the **Delivery** section to have Stripe automatically send an email to your customer with the hosted invoice page or generate a hosted invoice page that you can send yourself. To send the hosted invoice page yourself, create the invoice and then copy the link to send to your customer.

## Page customization 

The hosted invoice page is customizable with your:

- Brand color
- Logo
- Icon

You can customize these [branding settings](https://dashboard.stripe.com/account/branding) in the Dashboard.

## Set allowed payment methods 

Using the hosted invoice page, you can configure invoices to allow payment with one or more of the [supported payment methods](https://docs.stripe.com/invoicing/payment-methods.md). You can set defaults to apply to all of the newly created invoices from the [Invoice default payment method configuration](https://dashboard.stripe.com/settings/billing/invoice). You can also select the payment method on a per-invoice basis when you’re [creating an invoice](https://dashboard.stripe.com/invoices/create) through the Dashboard.

With the hosted invoice page, you can display the allowed payment method list to the customer. This gives them the option to choose a payment method that suits them best. Additionally, enabling the hosted invoice page gives the customer the benefit of having Stripe handle complex payment and authentication flows (without any extra implementation effort from you). For example, the *Strong Customer Authentication* (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) regulation in Europe requires customers to confirm their payment with *3D Secure* (3D Secure (3DS) provides an additional layer of authentication for credit card transactions that protects businesses from liability for fraudulent card payments) (3DS)—in this case, the hosted invoice page displays the payment confirmation modal to your customer.

> If a customer has a [default payment method](https://docs.stripe.com/api/customers/object.md#customer_object-invoice_settings-default_payment_method), then they can use it on the hosted invoice page even when the invoice’s payment method configuration doesn’t include it.

## Payment method persistence 

> Global privacy laws are complicated and differ by region. You might be required to present your customer with terms and obtain requisite consents before storing a customer’s payment method. Before using this feature, consult with your legal counsel for advice specific to your business.

You can configure how payment method details that customers enter on the hosted invoice page are saved for future use. By default, Stripe doesn’t store payment methods used for one-time payments, unless the customer opts in using a checkbox displayed on the hosted invoice page.

When a customer returns to the hosted invoice page, saved payment methods with [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) of `always` are displayed and available to use.

> Customers are only presented with saved payment methods of type Card, Link, ACH Direct Debit, or SEPA Debit.

### Configuration Options

The following configurations are available for storing payment methods used for one-time invoice payments on the hosted invoice page.

1. **Offer**: Payment methods for one-time invoices are saved only if the customer selects a checkbox displayed before completing payment. (Default for new accounts created after May 30, 2025.)
   - If your integration uses the deprecated [Sources API](https://docs.stripe.com/sources.md) for invoices or uses [card installments](https://docs.stripe.com/payments/installments.md), this checkbox won’t be displayed, so the payment method won’t be saved since the customer can’t provide consent.
   - Have terms in place with the customer about how you plan to use payment methods that they decide to save.
   - [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) is set to `always` if the customer selects the checkbox, and `limited` if they don’t.
2. **Never**: Payment methods used for one-time invoices aren’t saved.
   - [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) is set to `limited`.
3. **Always**: Payment methods used for one-time invoices are always saved, without asking the customer.
   - Saving payment methods without explicit customer permission can violate privacy regulations in many jurisdictions. Before selecting this option, make sure that it complies with local laws.
   - [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) is set to `limited`.

### Select a configuration

#### Dashboard

To configure saving payment methods, use the controls in the **Default payment terms** section of the [Invoice settings page](https://dashboard.stripe.com/settings/billing/invoice) of your Dashboard. To enable saving payment methods, select **Save customer payment information**. To allow saving without asking the customer first, deselect **Ask customers before saving their payment information**.

| Configuration | Save customer payment information | Ask customers before saving their payment information |
| --- | --- | --- |
| Offer | On | On |
| Always | On | Off |
| Never | Off | Off |

#### API

You can configure saving payment methods for connected accounts by using the [Accounts API](https://docs.stripe.com/api/accounts.md). When you create or update an `Account`, set the `settings.invoices.hosted_payment_method_save` property to `never`, `offer`, or `always`.

```curl
curl https://api.stripe.com/v1/accounts \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "settings[invoices][hosted_payment_method_save]=offer"
```

### Limitations

If saving a payment method is enabled, the hosted invoice page only saves reusable payment methods. These payment methods include:

- Cards
- Link
- Pre-authorized Debit
- BECS Direct Debit
- Bacs Direct Debit
- SEPA Direct Debit
- ACH Direct Debit

### Overrides

Some cases override this setting, depending on the invoice and account properties. This only applies to payment methods that are reusable (see list above).

- If the invoice has an attached subscription, the payment method is saved only if the customer doesn’t have a default invoice payment method.
- If your Stripe account allows customers to [schedule payments](https://docs.stripe.com/invoicing/hosted-invoice-page/scheduled-payments.md) and the customer chooses to schedule their invoice payment, the payment method is always saved.
- If [card installments](https://docs.stripe.com/payments/installments.md) is enabled on the invoice and by the customer, the payment method is always saved.
- If the invoice’s attached PaymentIntent has a [setup_future_usage](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-setup_future_usage) value of `off_session` or `on_session`, the payment method is always saved.
- If your integration uses the deprecated [Sources API](https://docs.stripe.com/sources.md) to collect hosted invoice payments, the `offer` configuration doesn’t save customer payment methods. Those cases don’t support the customer consent checkbox, so the customer can’t provide consent.

## Let customers pay in their local currency

[Adaptive Pricing](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md) lets your customers pay in their local currency in more than 150 countries on your hosted invoice page. With Adaptive Pricing, Stripe infers the presentment currency from the customer’s public IP address, then automatically calculates the localized price and handles all currency conversion. Manage Adaptive Pricing for hosted invoice pages in your [payment settings](https://dashboard.stripe.com/settings/adaptive-pricing) in the Dashboard.

## Partial payments

You can allow your customers to make [partial payments](https://docs.stripe.com/invoicing/partial-payments.md) on the hosted invoice page, letting them pay a custom amount toward an invoice rather than the full balance at once. To enable this in the Dashboard, go to the **Default payment terms** section of your [Invoice settings page](https://dashboard.stripe.com/settings/billing/invoice).

## Public support information 

Invoices include any public information that you specified under [Public business information](https://dashboard.stripe.com/settings/public), such as your support email address or business website. Using these settings, you can also choose to include a support phone number in customer-facing documents—like invoice PDFs and emails—or default to your business address.
