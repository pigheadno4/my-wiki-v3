<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/braintree-auth/configuration -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Configuration
slug: /docs/guides/braintree-auth/configuration/
createTime: '2025-04-01T23:28:55.399Z'
updateTime: '2025-04-01T23:28:55.419Z'
---



# Configuration

**AVAILABILITY**
Braintree Auth is in closed beta. [Contact us](https://www.braintreepayments.com/products/braintree-auth#contact) to express interest.

 Braintree Auth follows the [OAuth 2.0](https://oauth.net/2/) specification. Once accepted into the Braintree Auth beta, you will be able to create an OAuth application in the Control Panel. You will use this OAuth application to authenticate with Braintree Auth, as well as identify your platform to connecting merchants. To create an OAuth application:


- Log into either the[production Control Panel](https://www.braintreegateway.com/login)or the[sandbox Control Panel](https://sandbox.braintreegateway.com/login), depending on which environment you are working in
- Click on the gear icon in the top right corner
- Click**OAuth**from the drop-down menu
- Click the**OAuth Apps**tab
- Click the**Add Application**button at the top right of the page

Here is a list of the various fields you can configure on your OAuth application:


- **Display Name (required)**: The public name that your connected merchants will see when they authorize your application
- **Website (required)**: Where merchants should go to learn more about your company, product, or service
- **Logo Image (required)**: The logo that merchants will be shown when authorizing your application. For best results this should be a PNG or JPG at least 200px by 200px
- **Support Information (at least one required):**After the merchant has connected with your application, they will see these support channels within their Control Panel
- Phone: A phone number where merchants can contact support for your company
- Email: An email address where merchants can contact support for your company
- Articles URI: A link to support documentation you can provide to your connected merchants about your company
- Contact URI: A link to a page where merchants can contact support for your company


- **Redirect URIs (required):**A list of allowed URIs that your merchant will be redirected to after they authorize your application or choose to save and finish later. The redirect URI passed when generating the[connect URL](/braintree/docs/guides/braintree-auth/server-side)must be in this list or we will not authorize the redirect. Please use a full URI, includinghttp. In production,httpsis required
- **Configuration Name**: An internal name to help you distinguish between multiple applications. This will not display to the merchant
- **PayPal BN Code**: A BN code (or Build Notation code) is provided to partners by PayPal for transaction tracking. If you do not have a BN code, leave this blank

Once created, your OAuth application will have a client_id and a client_secret for sandbox testing and production that must be securely stored on your server. You will use these values to configure the Braintree server SDKs to make API calls and facilitate the [Connect](/braintree/docs/guides/braintree-auth/connect) flow.

[Next Page:Merchant Connect Flow→](/braintree/docs/guides/braintree-auth/connect)

