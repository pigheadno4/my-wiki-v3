<!-- Source URL: https://docs.stripe.com/payments/managed-payments/use-payment-links -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Use payment links with Managed Payments

Sell digital products globally while Stripe handles indirect tax compliance, fraud protection, dispute management, and customer transaction support for you.

Enable Managed Payments and then create a [payment link](https://docs.stripe.com/payment-links.md) to instantly collect payments for your digital products. You can create payment links in the [Dashboard](https://dashboard.stripe.com/payment-links) without writing any code, or with the [Payment Links API](https://docs.stripe.com/api/payment-link.md). Learn more about [how Managed Payments works](https://docs.stripe.com/payments/managed-payments/how-it-works.md).

## Before you begin

- Make sure your products meet the [eligibility requirements](https://docs.stripe.com/payments/managed-payments/eligibility.md#product-eligibility) for Managed Payments. You can only create a payment link with Managed Payments enabled if all the products your customer wants to purchase are eligible.
- Activate Managed Payments in your [Dashboard](https://dashboard.stripe.com/settings/managed-payments).

## Create a payment link

#### Dashboard

1. In the Dashboard, on the [Payment Links](https://dashboard.stripe.com/payment-links) page, click **New** (or click the plus (**+**) symbol, and select **Payment link**.
2. Select an existing product, add a new product, or allow customers to choose what to pay.
3. Make sure your selected products have a product category that’s eligible for Managed Payments.
4. Make sure **Enable Managed Payments** is selected.
5. Click **Create link**.

> We don’t support creating payment links with Managed Payments enabled through the Stripe iOS app. Use the web version of the Dashboard instead.

#### API

To use Managed Payments with the [Payment Links API](https://docs.stripe.com/api/payment-link.md), you must use API version `2025-03-31.basil` or [later](https://docs.stripe.com/changelog.md). 

#### Products or subscriptions

### Create a product

You can use **Products and Prices** to sell one-time products or subscriptions. To do so, create a product and then assign a price. You must include a tax code that’s [eligible for Managed Payments](https://docs.stripe.com/payments/managed-payments/eligibility.md#eligible-tax-codes).

```curl
curl https://api.stripe.com/v1/products \
  -u "<<YOUR_SECRET_KEY>>:" \
  --data-urlencode "name=Hamlet (e-book)" \
  -d "description=A Shakespearean tragedy" \
  -d tax_code={{TAX_CODE}} \
  -d "default_price_data[unit_amount]=1000" \
  -d "default_price_data[currency]=usd"
```

### Create a payment link

[Create a payment link](https://docs.stripe.com/api/payment-link/create.md) with the `managed_payments[enabled]` parameter along with [line_items](https://docs.stripe.com/api/payment-link/create.md#create_payment_link-line_items). Each line item contains a [price](https://docs.stripe.com/api/payment-link/create.md#create_payment_link-line_items-price) and [quantity](https://docs.stripe.com/api/payment-link/create.md#create_payment_link-line_items-quantity). You can add up to 20 line items for flat rate prices.

```curl
curl https://api.stripe.com/v1/payment_links \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "managed_payments[enabled]=true" \
  -d "line_items[0][price]={{PRICE_ID}}" \
  -d "line_items[0][quantity]=1"
```

You can also use [price_data](https://docs.stripe.com/api/payment-link/create.md#create_payment_link-line_items-price_data) to create a product and price inline when you create the payment link.

To create a subscription using a payment link, specify a price with [type=recurring](https://docs.stripe.com/api/prices/object.md#price_object-type) for `line_items`. Use [subscription_data](https://docs.stripe.com/api/payment-link/create.md#create_payment_link-subscription_data) to specify the configuration for the subscriptions created from the payment link, including trials.

#### Customer chooses price

### Create a variable price

Set up [variable pricing](https://docs.stripe.com/products-prices/how-products-and-prices-work.md#variable-pricing) to let your customers choose what to pay for your product. Your product must be a digital product that’s [eligible for Managed Payments](https://docs.stripe.com/payments/managed-payments/eligibility.md#product-eligibility).

```curl
curl https://api.stripe.com/v1/prices \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d currency=usd \
  -d "custom_unit_amount[enabled]=true" \
  -d "product={{PRODUCT_ID}}"
```

### Create a payment link

[Create a payment link](https://docs.stripe.com/api/payment-link/create.md) by passing the `managed_payments[enabled]` parameter along with the ID of the `Price` object in [line_items](https://docs.stripe.com/api/payment-link/create.md#create_payment_link-line_items).

```curl
curl https://api.stripe.com/v1/payment_links \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "managed_payments[enabled]=true" \
  -d "line_items[0][price]={{PRICE_ID}}" \
  -d "line_items[0][quantity]=1"
```

### Share the payment link

Each payment link contains a URL that you can share with your customers through email, on social media, with a website link, in an app, or through other channels.

## Update an existing Payment Links API integration to use Managed Payments

Follow the steps above to create new payment links with Managed Payments enabled.

### Remove unsupported parameters

To act as the merchant of record, Stripe controls some parts of the checkout session. As a result, some parameters aren’t available when using Managed Payments, and you must remove them when creating payment links with Managed Payments enabled.

| Category | Parameter | Reason |
| --- | --- | --- |
| Tax | `automatic_tax` | Managed Payments handles tax calculation and withholding for you. |
| `tax_id_collection` |
| Payment methods | `payment_method_types` | Managed Payments controls the payment methods available on the payment link using [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) to display the most relevant payment methods to your customer. Refer to [Payment method configurations](https://support.stripe.com/questions/payment-method-configurations-for-managed-payments) for information about how to configure payment method settings for Managed Payments. |
| Shipping | `shipping_address_collection` | Managed Payments only supports digital products, so shipping information is never collected. |
| `shipping_options` |
| Connect | `application_fee_amount` | Managed Payments doesn’t support Connect integrations. |
| `application_fee_percent` |
| `on_behalf_of` |
| `transfer_data` |
| `payment_intent_data.transfer_group` |
| Post-sale | `subscription_data.invoice_settings` | Managed Payments handles post-sale actions, such as invoicing and confirmation emails for you. |
| `invoice_creation` |
| Statement descriptors | `payment_intent_data.statement_descriptor` | Managed Payments manages statement descriptors on behalf of your business. |
| `payment_intent_data.statement_descriptor_suffix` |
| `consent_collection.payment_method_reuse_agreement.position` |
| Submit button options (limited) | `submit_type='donate'` | Managed Payments doesn’t support donations or selling services. The remaining [submit_type](https://docs.stripe.com/api/payment-link/object.md#payment_link_object-submit_type) options are supported. |
| `submit_type='book'` |
| Customization | `custom_text` | Managed Payments provides a standardized checkout that doesn’t support custom text. |

## Edit payment links

After creating a payment link, you can’t change the Managed Payments state on that link.

- You can’t enable Managed Payments on existing payment links—you must create a new payment link to use Managed Payments.
- After you create the payment link with Managed Payments enabled, you can’t disable Managed Payments on that link. Instead, you must create a new payment link without Managed Payments enabled.

## Testing

Test that your integration works correctly for your customers.

### Checkout

1. Go to the payment link URL to load your checkout page.
2. On the checkout page, enter different billing addresses to see how Managed Payments calculates tax for customers in different locations.
3. To process the payment, use the test card number `4242 4242 4242 4242` with any CVC and an expiration date in the future.

For additional information, see [Testing](https://docs.stripe.com/testing.md).

### Payment details

#### Item 1

1. After you confirm the test payment, go to the **Dashboard** > [Transactions](https://dashboard.stripe.com/test/payments).
2. Click your test payment to view the payment details. This page shows the:
   - Product that was purchased
   - [Subscription](https://docs.stripe.com/api/subscriptions.md) that was created
   - [Invoice](https://docs.stripe.com/api/invoices.md) that was created
   - Amount of tax calculated and withheld through Managed Payments
   - Statement descriptor that displays on your customer’s statements

> #### Customer authorization
> 
> When a customer purchases a subscription through Managed Payments, it only authorizes their payment method to be charged by Managed Payments. Make sure you obtain the appropriate consent from your customer to charge this payment method for any transactions outside of Managed Payments.

#### Item 2

1. After you confirm the test payment, go to the **Dashboard** > [Transactions](https://dashboard.stripe.com/test/payments).
2. Click your test payment to view the payment details. This page shows the:
   - Product that was purchased
   - [Subscription](https://docs.stripe.com/api/subscriptions.md) that was created (if purchased)
   - [Invoice](https://docs.stripe.com/api/invoices.md) that was created
   - Amount of tax calculated and withheld through Managed Payments
   - Statement descriptor that displays on your customer’s statements

### Preview the receipt

1. Under **Receipt history**, click **View receipt**.
2. Click **Send receipt** to preview the receipt email sent to your customer.

> In sandbox mode, you won’t receive receipt emails automatically after a purchase, but you can manually send them using the instructions above.

### Test Link

[Link](https://docs.stripe.com/payments/link.md) acts as the merchant of record at checkout and provides subscription management and transaction support on the [Link website](https://link.com).

You can test how Link works during checkout by creating a Link account during an initial Checkout Session. After you create the Link account, attempt another session using the same email address. To authenticate, use the test passcode `000000`.

Test purchases won’t appear in the Link app. You can test the order management tools in the Link app by creating a Link account during a live mode Checkout Session.

## Optional: Configure the tax behavior of your prices

The [tax_behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#tax-behavior) of a price specifies whether tax is added on top of the price you set (`tax_behavior: exclusive`) or already included in the price (`tax_behavior: inclusive`).

Managed Payments uses the [tax behavior specified on your price](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#set-tax-behavior-on-price). If you don’t specify the price’s tax behavior, Managed Payments adds tax on top of the price you set, by default.

To change the default, go to the [Tax settings](https://dashboard.stripe.com/settings/tax) page in the Dashboard, and update the **Include tax in prices** setting.
