<!-- Source URL: https://docs.paypal.ai/payments/create-shopping-cart-button -->
<!-- Fetched: 2026-04-16 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create shopping cart button

You can add Add to Cart and View Cart buttons to your website without building a custom integration. Use the PayPal Business Dashboard to define product details, pricing, and checkout behavior, then copy the generated code snippets into your site. You can also customize the layout and styling of your buttons to match the look and feel of your website and brand.

## How buttons work

- Add to Cart button helps customers select and store products in their shopping cart so they can continue browsing or shopping before completing the purchase.
- View Cart button helps customers review the items they add, modify quantities, and proceed to checkout.

## Prerequisites

- [PayPal business account](https://www.paypal.com/business/open-business-account?_ga=2.49411041.673139926.1760916697-1259758161.1760473483)
- Website HTML access

## Create shopping cart buttons

1. Log in to your [PayPal Business Account](https://www.paypal.com/business/open-business-account?_ga=2.49411041.673139926.1760916697-1259758161.1760473483).
2. In the left navigation, select **Pay & Get Paid** > **Create Shopping Cart Buttons**.
3. Enter the details in the **Product**, **Checkout**, and **Confirmation** tabs.
4. Select **Build it**.
5. Copy the generated code snippets to place the buttons on your website. A downloadable PDF with detailed instructions is available on this page.
6. Select **More Actions** > **Settings** > **Cart buttons** to customize button appearance and preview the customization.

> **Note**: If you select **Settings** while you are still building a button, the editor is replaced by the **Settings** page, and any unsaved changes are lost.

For more information on customization, see [Customize checkout](/payments/customize-checkout).

## Add shopping cart buttons

Add both the View Cart and Add to Cart buttons after you create your shopping cart buttons so the cart works correctly.

### Add the View Cart button

1. Open your website editor.
2. Copy the **Part 1 View Cart** code from the UI:
   - Paste it once into your site’s `<head>` on each page.
   - If you can’t edit the `<head>`, paste it at the top of the `<body>`.
3. Copy the **Part 2 View Cart** code:
   - Paste it into a visible location in the `<body>` that appears on every page, such as the site navigation.
   - You can paste Part 2 in more than one location if needed.
4. Save your changes.

### Add the Add to Cart button

1. Open your website editor.
2. In the page’s `<body>`, paste the Add to Cart button code where you want it to appear, ideally near the product.
3. Save your changes.
4. Repeat these steps for each product on the page.

## Test buttons

Test the workflow to ensure the buttons function correctly.

1. Refresh your website to confirm all buttons appear correctly.
2. Make a test purchase on your site.
3. Verify the transaction in your PayPal account.
4. Refund the test transaction when finished.

## Common issues

**Site builder doesn't expose the HTML `<head>`**

- If your site builder doesn't allow access to the `<head>`, paste the Part 1 code at the top of your page's `<body>`, above the Part 2 code.
