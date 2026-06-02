<!-- Source URL: https://docs.paypal.ai/payments/troubleshooting -->
<!-- Fetched: 2026-04-16 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting

Use this guide to identify and fix common issues that prevent Payment Links and Buttons from displaying or working as expected.

## Issues with account eligibility and access

Review the following solutions if you cannot access Payment Links and Buttons or if customers experience problems completing payments.

### Payment Links and Buttons are missing from my account

Payment Links and Buttons are available only for Business accounts. To access this feature, upgrade your existing account or create a new [Business account](https://www.paypal.com/webapps/mpp/account-selection).

### Customer cannot see all payment methods

Payment method availability depends on the customer's country and eligibility. Not all payment methods appear for every buyer.

### Payment Links and Buttons are not working

Account restrictions can prevent customers from completing payments. Common symptoms include a generic "something went wrong" message or a `payment_denied` error.

To resolve this:

1. Log in to your PayPal account and check for any notifications or required action items.
2. Contact PayPal support to identify and resolve the specific restriction on your account.

## Issues with button display

Review the following solutions if a button does not appear on your page or shows an error in the browser console.

### Button does not appear on my page

The button might not display if your site cannot load required PayPal resources because of your Content Security Policy (CSP) or connectivity issues.

#### Check basic connectivity

- Make sure your internet connection works by loading a few other websites.
- Open other pages on your site, and confirm that they load as expected.

#### Confirm the button exists in your PayPal account

1. Sign in to your [PayPal Business account](https://www.paypal.com/business/open-business-account?_ga=2.49411041.673139926.1760916697-1259758161.1760473483).
2. In the left navigation, select **Pay & Get Paid** > **Create Payment Links and Buttons**.
3. Select **More actions** > **Saved links and buttons**.
4. In the list, find the button, and then select **Open** to expand options.
5. Select **View**, and verify that the button code in the UI matches the code you pasted into your page.\
   If the button still does not appear, continue with CSP checks in the next section.

### Button shows an error in the browser

The button can fail if your CSP blocks PayPal scripts, frames, images, or network calls.

#### Check the browser console for CSP errors

1. Open your product page where you pasted the button code.
2. Right-click the page, and then select **Inspect**.
3. Select the **Console** tab.
4. Look for CSP errors that mention PayPal domains or the PayPal JavaScript SDK, such as errors that refuse to load `https://www.paypal.com/sdk/js` or frame `https://www.paypal.com/`.
5. If you see these errors, update your CSP to allow the required PayPal domains.

#### Fix CSP defined in HTML

If you set your CSP in a `<meta>` tag in your HTML, replace your current CSP meta tag with this example so your page can load PayPal resources:

```html theme={null}
<meta
  http-equiv="Content-Security-Policy"
  content="default-src 'self';
script-src 'unsafe-inline' https://*.paypal.com https://*.paypalobjects.com;
style-src 'unsafe-inline' https://*.paypal.com;
connect-src https://*.paypal.com;
frame-src https://*.paypal.com;
img-src https://*.paypal.com https://*.paypalobjects.com"
/>
```

This policy allows the PayPal JavaScript SDK, frames, images, and network calls, and restricts other sources to your own origin.

#### Fix CSP defined on the server

If you configure your CSP in HTTP response headers, update your headers to include PayPal as an allowed source. Use this example as a starting point and merge it into your existing CSP header:

```text theme={null}
Content-Security-Policy: default-src 'self';
script-src 'unsafe-inline' https://*.paypal.com https://*.paypalobjects.com;
style-src 'unsafe-inline' https://*.paypal.com;
connect-src https://*.paypal.com;
frame-src https://*.paypal.com;
img-src https://*.paypal.com https://*.paypalobjects.com;
```

After you update your CSP:

1. Reload your product page.
2. Open the console again, and confirm that CSP errors related to PayPal no longer appear.
3. Verify that the button now renders correctly.

### Some buttons do not display on my page

Conflicting IDs, currencies, or scripts can prevent buttons from rendering.

- Do not reuse the same button ID on a single page. If you paste the same button ID multiple times, only the first button renders.
- Do not mix buttons that use different currencies on the same page. If you use different button IDs with different currencies, only the first button renders.
- If you add several different button IDs and the page is slow or buttons do not appear, make sure you include the PayPal JavaScript SDK script with your client ID only once on the page. The script should look like this, with your own client ID and currency value:

```xml theme={null}
<script src="https://www.paypal.com/sdk/js?client-id=XYZ&components=hosted-buttons&enable-funding=venmo&currency=USD"></script>
```

## Issues at checkout

Review the following solutions if customers encounter unexpected behavior during the checkout process.

### Continue Shopping link appears on the payment page

To remove the **Continue Shopping** link, remove the Homepage URL from your Payment Link settings.

### Billing address country incorrectly set to US

When a customer selects the credit or debit card option, the billing address country defaults to US regardless of the customer's actual location. This happens because the billing address is determined by the buyer's browser locale settings.

The fix depends on the product you are using:

| Product               | Fix                                                                                                                                                       | Notes                                                                                                                                  |
| :-------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| Payment Links         | Append `locale.x` and `country.x` query parameters to the payment link URL: `https://www.paypal.com/ncp/payment/YOUR_LINK_ID?locale.x=en_CA&country.x=CA` | This fix applies to all buyers regardless of locale or country settings. A US buyer accessing this link is also treated as a CA buyer. |
| Buy Buttons           | Not currently supported                                                                                                                                   | —                                                                                                                                      |
| Shopping Cart Buttons | Not currently supported                                                                                                                                   | —                                                                                                                                      |

### Locale and language issues

The `LANG` cookie set during a buyer's previous PayPal.com visit takes priority over their browser locale preference, which can cause the checkout page to display in an unexpected language.

The fix depends on the product you are using:

| Product               | Fix                                                                                                                                                       | Notes                                                                                                                                  |
| :-------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| Payment Links         | Append `locale.x` and `country.x` query parameters to the payment link URL: `https://www.paypal.com/ncp/payment/YOUR_LINK_ID?locale.x=en_CA&country.x=CA` | This fix applies to all buyers regardless of locale or country settings. A US buyer accessing this link is also treated as a CA buyer. |
| Buy Buttons           | Not currently supported                                                                                                                                   | —                                                                                                                                      |
| Shopping Cart Buttons | Not currently supported                                                                                                                                   | —                                                                                                                                      |
