<!-- Source URL: https://docs.paypal.ai/payments/customize-checkout -->
<!-- Fetched: 2026-04-16 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Customize your checkout and buttons

Use the Payment Links and Buttons settings to choose payment methods, button styles, business branding, and return URLs for checkout.

## Before you begin

1. Log in to your [PayPal Business Account](https://www.paypal.com/business/open-business-account?_ga=2.49411041.673139926.1760916697-1259758161.1760473483).
2. From the left navigation, select **Pay & Get Paid** > **Create Payment Links and Buttons** or **Create Shopping Cart Buttons**.
3. Select **Settings**.

## Choose payment methods

Select which payment methods to appear at checkout.

- Available options include: PayPal, Pay Later, Venmo, and Apple Pay. Credit and debit cards are enabled by default.

## Set business identity and branding

- Configure how your business appears during checkout.
- Display **business name**.
- Display **business logo**.
- Set a **homepage URL**. Customers are sent here when selecting your logo or home icon.

Business name, logo, and profile details can be updated in [account settings](https://www.paypal.com/businessprofile/settings/info/edit).

## Button layout and styles

Control how your PayPal buttons look and behave across your site. Use stacked buttons to show multiple payment options together, single buttons for a primary checkout action, and cart buttons to keep your existing shopping cart buttons consistent.

<Tabs>
  <Tab title="Stacked buttons">
    Stacked button settings apply to all existing stacked buttons on your site. Use stacked buttons to offer multiple payment options within the same checkout entry point.

    * **Layout:** Vertical or horizontal
    * **Color:** Standard PayPal color schemes only (custom colors not supported)
    * **Shape:** Pill or rectangle
    * **Size:** Small, medium, or large

    Second button behavior:

    * Control what appears on the second button in the stack. The options you see depend on which payment methods are available in the buyer’s region. For example, you can show a Venmo button when available, or select **None** to hide the second button entirely.

    Checkout button label:

    * Choose the text that appears on your checkout button. The button redirects buyers to a PayPal checkout page, where available payment methods are displayed.
    * Choose the button label: **Checkout**, **Proceed**, **Pay**, or **Custom**.

  </Tab>

  <Tab title="Single button">
    Changes to single buttons apply only to new buttons that you create. Use a single button when you want a single primary option for customers to select.

    * **Shape:** Pill or rectangle
    * **Size:** Small, medium, or large
    * **Color:** Standard PayPal colors or customize the button color

  </Tab>

  <Tab title="Cart button">
    Changes to cart buttons apply to all existing shopping cart buttons you have already added to your website. Configure how cart buttons look:

    * **Shape:** Pill or rectangle
    * **Size:** Small, medium, or large
    * **Color:** Standard PayPal colors or customize the button color

  </Tab>
</Tabs>

Each shopping cart button automatically generates a payment link and a QR code that you can reuse across other channels.

## Auto-return URL

Use auto-return to send customers back to your site after checkout. The URL applies to all shopping cart transactions. Configure the auto-return URL in the **Cart Buttons** tab under **Settings**.

> **Note**: For Payment Links and Buy Buttons, the auto-return URL is set in the **Confirmation** tab. This URL applies only to the transactions for that specific link or button.
