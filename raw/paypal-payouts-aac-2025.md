<!-- Source URL: https://docs.paypal.ai/growth/payouts/send-money/collect-recipient-information -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect recipient information with AAC

You can use Assisted Account Creation (AAC) to let your customers use their PayPal account to log in or sign up on your site. AAC simplifies onboarding, increases customer account creation, and helps your customers receive payouts quickly and securely.

When a customer completes the onboarding flow, you receive their payer ID and email address. Payer IDs are typically the most reliable way to ensure accurate and secure payouts.

AAC can:

- Identify customers with PayPal accounts and display a **Log in with PayPal** button.
- Enable merchants to customize rewards for PayPal users.
- Allow customers to connect their PayPal account at your site's payment settings screen.

## Prerequisites

- Complete all mandatory steps to <a href="/growth/payouts/set-up#set-up-sandbox-account-for-payouts-api-integration" target="_blank" rel="noopener noreferrer">get started</a>. Use the retrieved sandbox app credentials (client ID and secret) in your code to generate an access token. The access token is a server-side token that authenticates your application when accessing PayPal API resources.
- Ensure you have verified your PayPal business account and enabled it for Payouts. For more information, see <a href="/growth/payouts/set-up#set-up-live-account" target="_blank" rel="noopener noreferrer">Set up your PayPal business account</a>.
- <a href="https://www.paypal.com/us/cshelp/contact-us" target="_blank" rel="noopener noreferrer">Contact PayPal</a> or work with your account manager to enable <a href="https://www.paypal.com/in/cshelp/article/how-do-i-confirm-my-identity--help606" target="_blank" rel="noopener noreferrer"> identity services</a> and configure the following return URLs for your application:
  - **Sandbox**: [https://www.sandbox.paypal.com/conex/ac/add-offer-recipient](https://www.sandbox.paypal.com/conex/ac/add-offer-recipient)
  - **Live**: [https://www.paypal.com/conex/ac/add-offer-recipient](https://www.paypal.com/conex/ac/add-offer-recipient)
- Enable **Log in with PayPal** in your app settings:
  1. Go to your <a href="https://developer.paypal.com/dashboard/" target="_blank" rel="noopener noreferrer">PayPal developer account</a> and toggle to **Sandbox**.
  2. Go to **Apps & Credentials** and select your app.
  3. Go to **Features** and select **Log in with PayPal**.
  4. Select **Advanced settings**. This displays the Log in with PayPal page.
  5. Enter the **Return URL** to redirect your customers after they complete the Log in with PayPal flow.
  6. Go to **Information requested from customers** and select the following options:
     - **Email**
     - **Account verification status**
     - **PayPal account ID (payer ID)**
     - **Enable customers who have not yet confirmed their email with PayPal to log in to your app**: Select this option based on your business requirement. For details, see <a href="https://developer.paypal.com/docs/log-in-with-paypal/" target="_blank" rel="noopener noreferrer">Enable Log in with PayPal</a>.
  7. Save your app settings.
- Get your **Paypal Merchant ID** from the **Account Settings** > **Business information** page of your PayPal business account. Use this ID to uniquely identify your PayPal business account in your integration setup and API requests.

## Integrate assisted account creation

Integrating AAC enables your application to access customers’ email addresses and payer IDs (encrypted PayPal account numbers) during sign up, log in, or payment setup on your website or partner platform.

### Integrate client side

In your client-side code, integrate the AAC SDK to render the AAC component. The AAC SDK uses <a href="https://github.com/krakenjs/zoid" target="_blank" rel="noopener noreferrer">Zoid</a>, PayPal’s open-source cross-domain component library.
Use the following samples to integrate AAC based on your client-side framework.

<CodeGroup>
  ```html HTML lines  theme={null}
  <script src="https://www.paypalobjects.com/payouts/js/payouts_aac.js"></script>
  {/* Set up a container to render the AAC component */}
  <div id="container"></div>
  <script>
      // Render the AAC component
      paypal.PayoutsAAC.render({
          // Use sandbox for testing
          env: "<sandbox/production>",
          clientId: {
            production: "<production clientId>",
            sandbox: "<sandbox clientId>"
          },
          merchantId: "<Merchant Account ID>",
          pageType: "<signup/login>",
          onLogin: function(response) {
            if (response.err) {
              console.log(response.err)
            } else {
              console.log(response.body.code);
            }
          }
        }, '#container');
  </script>
  ```

```jsx React lines theme={null}
import React from "react";
import ReactDOM from "react-dom";
const AACComponent = paypal.PayoutsAAC.driver("react", {
  React,
  ReactDOM,
});
class OtherReactComponent extends React.Component {
  render() {
    return (
      <AACComponent
        clientId="<clientId>"
        merchantId="<Merchant Account ID>"
        env="<sandbox/production>"
        pageType="<signup/login>"
        onLogin={onLogin}
      />
    );
  }
}
```

```typescript Angular lines theme={null}
// Specify the component name as a dependency to your angular app:
angular.module('myapp', ['payouts-aac']);
// Include the tag in one of your templates (use kebab case for prop names)
<payouts-aac
  client-id="<clientId>"
  merchant-id="<Merchant Account ID>"
  env="<sandbox/production>"
  page-type="<signup/login>"
  on-login="onLogin">
</payouts-aac>
```

</CodeGroup>

### Integrate server side

After the user completes the PayPal log in or sign-up flow, PayPal redirects to your `redirect_uri` with a `code` parameter.

1. Use the authorization code from the client-side code to obtain an access token.

```shell lines theme={null}
curl -X POST https://api-m.sandbox.paypal.com/v1/identity/openidconnect/tokenservice \
  -H 'Authorization: Basic <Base64 Encoded client_id:secret>' \
  -d 'grant_type=authorization_code&code=<code>'
```

2. Use the access token to get the customer's email address and payer ID.

```shell lines theme={null}
curl -v -X GET https://api-m.sandbox.paypal.com/v1/oauth2/token/userinfo?schema=openid \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN'
```

#### Integrate with Node or Python

In your server-side code, use the following samples to integrate AAC.

<CodeGroup>
  ```javascript Node lines theme={null}
  var paypal = require('paypal-rest-sdk');
  paypal.configure({
    'mode': 'sandbox', //sandbox or live
    'client_id': '',
    'client_secret': ''
  });
  // Get tokeninfo with Authorization code
  paypal.openIdConnect.tokeninfo.create("Replace with authorization code", function(error, tokeninfo){
    console.log(tokeninfo);
  });
  // Get userinfo with Access code
  paypal.openIdConnect.userinfo.get("Replace with access_code", function(error, userinfo){
    console.log(userinfo);
  });
  ```

```python Python lines theme={null}
import paypalrestsdk
from paypalrestsdk.openid_connect import Tokeninfo, Userinfo
paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "",
  "client_secret": "" })
tokeninfo = Tokeninfo.create("Replace with authorization code")
userinfo  = tokeninfo.userinfo()
```

</CodeGroup>

## Test end-to-end flow

To test the AAC integration in the sandbox:

1. Run your application.
2. Verify if your application renders the **Log in with PayPal** button.
3. Select **Log in with PayPal** on your application.
4. Log in with your sandbox personal account credentials or complete the sign up process.
5. Approve the consent to share the customer details.
6. Use your sandbox business account to:
   - Verify that your application receives the authorization code.
   - Exchange the authorization code for an access token.
   - Use the access token to retrieve the customer details.
   - Check if the customer account exists. If not, use the retrieved customer details to create a new account in your application.
   - Use the access token to make a payout request.
7. Verify the payout:
   - Confirm if the payout status is `SUCCESS` in your sandbox business account.
   - Confirm the movement of money into your sandbox personal account.
