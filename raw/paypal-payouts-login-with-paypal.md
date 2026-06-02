---
title: Log in with PayPal for Payouts
slug: /docs/payouts/standard/login-with-payouts/
createTime: "2024-05-19T22:56:03.864Z"
updateTime: "2025-05-14T09:43:27.696Z"
---

# Log in with PayPal for Payouts

To simplify payouts, Assisted Account Creation (AAC) enables customers to use their PayPal account to log in or sign up to a merchant site. This can accelerate and increase creation of customer accounts on the merchant site.

The merchant receives the payer ID and email address of each customer who completes the onboarding flow. Barring compliance or fraud issues, payer IDs are the most reliable way to send payouts.

AAC can also:

- Identify users with PayPal accounts and display a **Log in with PayPal** button.
- Enable merchants to customize rewards for PayPal users.
- Enable customers to connect their PayPal account at the merchant site's payment settings screen.

Use AAC with these payouts integration methods:

- [Large Batch Payouts](/docs/payouts/standard/large-batch/)
- [API Integration](/docs/payouts/standard/integrate-api/)
- [Payouts Web](/docs/payouts/standard/payouts-web/)

## Prerequisites

Before you integrate AAC, you'll need to:

- Be sure you get your OAuth and secret credentials. If not, [get started](/docs/api/overview/) .

- Contact your PayPal account manager to enable identity services. Your PayPal account manager adds:

| App settings | Return URL                                                                                                                 |
| ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Sandbox      | [https://www.sandbox.paypal.com/conex/ac/add-offer-recipient](https://www.sandbox.paypal.com/conex/ac/add-offer-recipient) |
| Live         | [https://www.paypal.com/conex/ac/add-offer-recipient](https://www.paypal.com/conex/ac/add-offer-recipient)                 |

- In your sandbox app settings, select **Log in with PayPal** .

- Click **Advanced Options** and select **Email address** , **Account status (verified)** , and **PayPal account ID (payer ID)** . Based on your company’s requirements, you can **Enable customers who have not yet confirmed their email address with PayPal to log in to your app** . For details, see [Enable Log in with PayPal](/docs/log-in-with-paypal/) .

- Get your merchant account ID from the Settings page of your PayPal business account.

You can use AAC to acquire customers’ email addresses and Payer IDs, which are encrypted PayPal account numbers, at sign up, log in, or payment set up on a merchant or partner website.

AAC requires client-side and server-side integration. For client-side integration, AAC uses [Zoid](https://github.com/krakenjs/zoid) , PayPal’s open-source cross-domain-component library. Server-side integration includes two PayPal API calls.

To integrate AAC:

- [Integrate the AAC SDK](/docs/payouts/standard/login-with-payouts/#integrate-client-side) on your client-side application.
- [Add PayPal’s server-side API calls](/docs/payouts/standard/login-with-payouts/#integrate-server-side) to your server-side application.

### Integrate client side

Drop the AAC SDK onto your applicable pages as follows:

**Note:** In the client side scripts, information you need to fill in (for example, container , client_id , or signup/login ) has quotation marks and angled brackets around it.

#### **`Integrate client side`**

```javascript
<script src="https://www.paypalobjects.com/payouts/js/payouts_aac.js"></script>
<!-- Set up a container for ACC to be rendered into -->
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

Use this code to integrate AAC if your client-side application runs on React or Angular.

#### **`React`**

```javascript
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
        clientId="<client_id>"
        merchantId="<Merchant Account ID>"
        env="<sandbox/production>"
        pageType="<signup/login>"
        onLogin={onLogin}
      />
    );
  }
}
```

#### **`Angular`**

```javascript
// Specify the component name as a dependency to your angular app:
angular.module('myapp', ['payouts-aac])
// Include the tag in one of your templates (don't forget to use spine case prop names):
<payouts-aac client-id={clientIds} merchant-id="<Merchant Account ID>" env="<sandbox/production>" page-type="<signup/login>" on-login={onLogin}/>
```

Server-side integration includes two PayPal API calls.

- Use the authorization code returned in the client-side integration to obtain an access token.

#### **`Integrate server side`**

```curl
curl -X POST https://api-m.paypal.com/v1/identity/openidconnect/tokenservice
  -H 'Authorization: Basic <Base64 Encoded client_id:secret>'
  -d 'grant_type=authorization_code&code=<code>'
```

- Use the access token to get the customer's email address and Payer ID.

#### **`Integrate server side step 2`**

```curl
curl -v -X GET https://api-m.paypal.com/v1/oauth2/token/userinfo?schema=openid \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer <access_token>"
```

Use this code to install AAC if your server runs on Node or Python.

#### **`Node`**

```javascript
npm install paypal-rest-sdk
var paypal = require('paypal-rest-sdk');
paypal.configure({
  'mode': 'sandbox', //sandbox or live
  'client_id': '',
  'client_secret': ''
});
// Get tokeninfo with Authorize code
paypal.openIdConnect.tokeninfo.create("Replace with authorize code", function(error, tokeninfo){
  console.log(tokeninfo);
});
// Get userinfo with Access code
paypal.openIdConnect.userinfo.get("Replace with access_code", function(error, userinfo){
  console.log(userinfo);
});
```

#### **`Python`**

```javascript
apt-get install libssl-dev libffi-dev
pip install paypalrestsdk
import paypalrestsdk
from paypalrestsdk.openid_connect import Tokeninfo, Userinfo
paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "",
  "client_secret": "" })
tokeninfo = Tokeninfo.create("Replace with Authorize code")
userinfo  = tokeninfo.userinfo()
```
