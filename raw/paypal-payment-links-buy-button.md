<!-- Source URL: https://docs.paypal.ai/payments/create-buy-button -->
<!-- Fetched: 2026-04-16 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create buy button

Add a buy button to your website so customers can pay for a specific product or service directly from your page, without writing custom code. Create the button, add the generated code to your site’s HTML where you want it to appear, and then test a full checkout to confirm the payment flow works end to end.

## Prerequisites

- [PayPal business account](https://www.paypal.com/business/open-business-account?_ga=2.49411041.673139926.1760916697-1259758161.1760473483)
- [PayPal sandbox account](https://www.sandbox.paypal.com/?_ga=2.235638529.1825699906.1774759059-1259758161.1760473483&_gac=1.119179899.1772050711.CjwKCAiA2PrMBhA4EiwAwpHyC1eMcD67U9yOBYbJw87PsAfFCbhlVRJOVNHzaHkwkSAo46L1wEG98xoCieUQAvD_BwE) to test the button before using it in production
- Website HTML access required if creating payment buttons

## Create buy button

Before creating your buy button, select a price type:

- **One set price**: You set a single price that every customer pays. Use this for products or services with a defined cost.
- **Customer-set price**: Customers enter the amount they want to pay. Use this for donations, tips, or pay-what-you-want offers.

1. Log in to your PayPal business account.
2. From the left navigation, select **Pay & Get Paid** > **Create Payment Links and Buttons**.
3. Select the button type, then choose the product or service you want to sell.
4. In the **Product** tab, fill out the product or service details.
5. Under **Price**, select the appropriate pricing option and enter the required details.
6. (Optional) Turn on **Images** to show product visuals on the payment page.
7. (Optional) Add quantity, variants, and inventory to help customers choose the correct options.
8. If you selected **Customer-set price**, turn on **Label for Invoice ID** so customers can enter an invoice number at checkout, and mark it as required if you need to match payments to specific invoices or orders.
9. Use stacked buttons to show multiple payment options together, and a single button when you only need one primary button. See [Customize checkout and buttons](/payments/customize-checkout) to change button layout, colors, and behaviors.
10. (Optional) In the **Checkout** tab, add shipping, taxes, discounts, and handling fees.
11. (Optional) In the **Confirmation** tab, turn on **Auto-return** and enter the URL where customers are redirected after successful payment.
12. Select **Build it**.

## Add button code to website

After your buttons are created, add them to your website so customers can see and use them during checkout. You can choose to display multiple payment options together or show just a single button, depending on your preference.

## Stacked button

Customers see multiple PayPal payment options, such as PayPal, Pay Later, and cards in one stacked experience. Choose your preferred code language, HTML or React, from the **Code language** dropdown to view the relevant example.

### Use HTML

1. Open your website editor.
2. Copy the **Part 1** HTML code.
3. Paste it once in your site’s `<head>` on every page where you plan to use buttons.
4. If you can’t edit the `<head>`, paste the **Part 1** code at the top of the `<body>`.
5. Copy the **Part 2** HTML code.
6. Paste it where you want your stacked buttons to appear in the page `<body>`, ideally near your product or checkout section.​​
7. Save your changes and publish your site.

### Use React

1. Open your React project in your code editor.
2. Copy the **Part 1** React code.
3. Paste it once in your site’s `<head>` on every page where you plan to use buttons.
4. Copy the **Part 2** React code.
5. Paste it where you want your stacked buttons to appear in the page `<body>`.
6. Copy the **Part 3** React code.
7. Paste it where you want your stacked buttons to appear in the page `<body>`, ideally near your product or checkout section.​​

## Single button

Customers see a single PayPal button experience, with just one code snippet to add to your site.

1. Open your website editor.
2. Copy the single button code snippet.
3. Paste the code where you want the button to appear in your page’s `<body>`, near your product or call to action.
4. Save your changes and publish your site.

## Test buttons

Test the workflow to ensure the buttons function correctly.

1. Refresh your website to confirm all buttons appear correctly.
2. Make a test purchase on your site.
3. Verify the transaction in your PayPal account.
4. Refund the test transaction when finished.

## Common issues

**Button code is out of date after updating product details**

- In most cases, you don't need to update the button code. The button uses configuration stored on PayPal servers, so your changes take effect after you save them in your PayPal account. However, if you change the product's currency code, ensure you replace the existing button code with the updated code.

For more information, see [FAQ](/payments/faq) and [Troubleshooting](/payments/troubleshooting).
