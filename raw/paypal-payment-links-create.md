<!-- Source URL: https://docs.paypal.ai/payments/create-pay-link -->
<!-- Fetched: 2026-04-16 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create payment link

Use payment links to collect payments by sharing a URL with customers through email, text, social media, or on your website. Create the link in your PayPal business dashboard, set product details, pricing, and checkout behavior, then send it so customers can complete payment on a checkout page.

## Prerequisites

- [PayPal business account](https://www.paypal.com/business/open-business-account?_ga=2.49411041.673139926.1760916697-1259758161.1760473483)
- (Optional) [PayPal sandbox account](https://www.sandbox.paypal.com/?_ga=2.235638529.1825699906.1774759059-1259758161.1760473483&_gac=1.119179899.1772050711.CjwKCAiA2PrMBhA4EiwAwpHyC1eMcD67U9yOBYbJw87PsAfFCbhlVRJOVNHzaHkwkSAo46L1wEG98xoCieUQAvD_BwE) to test the payment link before using it in production

## Create payment link

Create a secure, shareable payment link to accept payments for your products or services. Set a fixed or customer-defined price, configure checkout options, and send the link to customers to complete payments without needing a website.

- **One set price**: You set a single price that every customer pays. Use this for products or services with a defined cost.
- **Customer-set price**: Customers enter the amount they want to pay. Use this for donations, tips, or pay-what-you-want offers.

1. Log in to your PayPal business account.
2. From the left navigation, select **Pay & Get Paid** > **Create Payment Links and Buttons**.
3. Create a payment link for the product or service you want to sell.
4. In the **Product** tab, fill out the product or service details.
5. Under **Price**, select the appropriate pricing option and enter the required details.
6. (Optional) Turn on **Images** to show product visuals on the payment page.
7. Add quantity, variants, and inventory to help customers choose the correct options.
8. If you selected **Customer-set price**, turn on **Label for Invoice ID** so customers can enter an invoice number at checkout, and mark it as required if you need to match payments to specific invoices or orders.
9. (Optional) In the **Checkout** tab, add shipping, taxes, discounts, and handling fees.
10. (Optional) In the **Confirmation** tab, turn on **Auto-return** and enter the URL where customers are redirected after successful payment.
11. Select **Build it**, then copy the link and share it with customers by email, SMS, or social media.

## Test your payment link

Verify that customers can open the link, see the correct pricing, and complete payment.

1. Open the payment link in a new browser window.
2. Confirm the product name, price, and currency display correctly.
3. Complete a test payment:
   - Use a low-value transaction if testing in live mode.
   - Use a sandbox buyer account if testing in the sandbox.
4. Confirm that the:
   - Payment completes successfully.
   - Confirmation page automatically redirects buyers to the expected return URL if auto-return is set.
   - Transaction appears in your dashboard activity.

## Common issues

**Auto-return does not redirect correctly**

- Verify that the return URL is valid and publicly accessible.

**Checkout experience is not customized**

- You haven't customized your checkout experience yet. Update your business name, logo, and brand colors to match your brand. Customization options vary depending on the checkout type you use. For more information, see [Customize checkout and buttons](/payments/customize-checkout).

<Columns>
  <Card title="Share a payment link" href="/payments/share-pay-links">
    Share a payment link by email, text, social, or on your website, and use QR codes or buttons so customers can pay from wherever they are.
  </Card>

  <Card title="Settings" href="/payments/customize-checkout">
    After your payment link or button is built, customize which payment methods are shown and update branding to match your business.
  </Card>

  <Card title="Manage inventory, variants, and optional features" href="/payments/manage-inventory-variants-taxes">
    Set variants, track stock levels, and manage taxes, discounts, and fees so your payment links and buttons stay in sync with your current inventory.
  </Card>
</Columns>

For more information, see [FAQ](/payments/faq) and [Troubleshooting](/payments/troubleshooting).
