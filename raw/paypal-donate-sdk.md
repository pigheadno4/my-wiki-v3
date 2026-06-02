<!-- Source URL: https://docs.paypal.ai/payments/donate/integrate -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a Donate button to your website with PayPal's Donate SDK

With the Donate SDK, users can select the PayPal Donate button to donate in a pop-up overlaid on your website. This keeps users on your website instead of redirecting them to a donation page on PayPal.

# Eligibility

The easiest way to find out if you're eligible to integrate the Donate SDK is to use paypal.com.

1. Log into <a href="https://www.paypal.com/donate/buttons?_ga=2.37509794.365520210.1755702720-1032254505.1740765755" target="_blank">paypal.com/donate/buttons/</a> with the account you want to use to make a Donate button.
2. If you can start a flow to make a **Donate** button, you're eligible to integrate the Donate SDK.

# 1. Create a Donate button

To use the Donate SDK, create a Donate button in the sandbox.

1. Log in to <a href="https://sandbox.paypal.com/donate/buttons?_ga=2.99832476.365520210.1755702720-1032254505.1740765755" target="_blank">sandbox.paypal.com/donate/buttons/</a>, and make your Donate button.
   After you create a button, you get code.
2. From the code, copy:
   - The `hosted_button_id` value if you have a business account
   - The `business` value if you have a personal account
3. You'll need this parameter to pass to the SDK.

The Donate SDK accepts all parameters that a Donate button accepts, such as `item_name` or `item_number`.

# 2. Add the Donate SDK to your web page

Add the Donate JavaScript SDK to your web page to integrate the Donate button into your site.

```html theme={null}
<!DOCTYPE html>

<head>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <!-- Ensures optimal rendering on mobile devices. -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <!-- Optimal Internet Explorer compatibility -->
</head>

<body>
  <script
    src="https://www.paypalobjects.com/donate/sdk/donate-sdk.js"
    charset="UTF-8"
  ></script>
</body>
```

# 3. Render the Donate button

Render the **Donate** button to a container element on your web page.

If you have a business account, provide the `hosted_button_id` parameter value. For any other account type, provide the `business` parameter value.

```html theme={null}
<body>
  <div id="paypal-donate-button-container"></div>

  <script>
    PayPal.Donation.Button({
      env: "sandbox",
      hosted_button_id: "YOUR_SANDBOX_HOSTED_BUTTON_ID",
      // business: 'YOUR_EMAIL_OR_PAYERID',
      image: {
        src: "https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif",
        title: "PayPal - The safer, easier way to pay online!",
        alt: "Donate with PayPal button",
      },
      onComplete: function (params) {
        // Your onComplete handler
      },
    }).render("#paypal-donate-button-container");
  </script>
</body>
```

To render another button on the same page, create another container, for example, `<div id="paypal-donate-button-container-2">`. Then render the button in the new container: `}).render('#paypal-donate-button-container-2')`.

# 4. Test the Donate button

1. On the site, click the **Donate** button.
2. Confirm that the button opens a pop-up window and displays your donation page.
3. Complete a donation using a sandbox credit card or sandbox PayPal account.
4. Verify that the `onComplete` function returns an object parameter.

This object parameter contains the following fields.

| Variable      | Description                                         |
| ------------- | --------------------------------------------------- |
| `tx`          | Transaction ID                                      |
| `st`          | Status of the transaction                           |
| `amt`         | Amount of the transaction                           |
| `cc`          | Currency code                                       |
| `cm`          | Custom message                                      |
| `item_number` | Configurable field for the transaction              |
| `item_name`   | Value that the donor selects during the transaction |

# 5. Go live

To go live with your new Donate button, replace the sandbox data with live data.

1. Replace the `hosted_button_id` value for the sandbox with a live `hosted_button_id` for a business account. For any other type of account, replace the sandbox `business` value with a live `business` value.
2. Remove the `env` value, or change `env` to `production`.

```html theme={null}
<body>
  <div id="paypal-donate-button-container"></div>

  <script>
    PayPal.Donation.Button({
      env: "production",
      hosted_button_id: "YOUR_LIVE_HOSTED_BUTTON_ID",
      // business: 'YOUR_LIVE_EMAIL_OR_PAYERID',
      image: {
        src: "https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif",
        title: "PayPal - The safer, easier way to pay online!",
        alt: "Donate with PayPal button",
      },
      onComplete: function (params) {
        // Your onComplete handler
      },
    }).render("#paypal-donate-button-container");
  </script>
</body>
```

# See also

- <a href="https://developer.paypal.com/api/nvp-soap/ipn/IPNandPDTVariables/" target="_blank">IPN and PDT variables</a>
- <a href="https://developer.paypal.com/api/nvp-soap/paypal-payments-standard/integration-guide/Appx-websitestandard-htmlvariables/" target="_blank">HTML variables for PayPal Payments Standard</a>
