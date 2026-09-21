<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/extend/oauth/configuration -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Configuration
slug: /docs/guides/extend/oauth/configuration/
createTime: '2025-04-01T22:54:01.922Z'
updateTime: '2025-04-01T22:54:01.945Z'
---



# Configuration

**AVAILABILITY**
OAuth is in closed beta in production, and open beta in sandbox. [Contact us](https://www.braintreepayments.com/products/braintree-auth#contact) to express interest in the production beta release.


## Creating an OAuth application


- Log into either the[production Control Panel](https://www.braintreegateway.com/login)or the[sandbox Control Panel](https://sandbox.braintreegateway.com/login), depending on which environment you are working in
- Click on the gear icon in the top right corner
- Click**OAuth**from the drop-down menu
- Click on the**OAuth Apps**tab
- Click the**Create Application**button

**NOTE**
In sandbox, you'll have access to the **OAuth Apps** page by default. In production, we'll need to enable this access for you.

 Here is a list of the various fields you can configure on your OAuth application:


- **Display Name (required)**: The public name that your connected merchants will see when they authorize your application
- **Website (required)**: Where merchants should go to learn more about your company, product, or service
- **Logo Image (required)**: The logo that merchants will be shown when authorizing your application. For best results this should be a PNG or JPG at least 200px by 200px
- **Support Info (at least one required):**After the merchant has connected with your application, they will see these support channels within their Control Panel
- Phone: A phone number where merchants can contact support for your company
- Email: An email address where merchants can contact support for your company
- Articles URI: A link to support documentation you can provide to your connected merchants about your company
- Contact URI: A link to a page where merchants can contact support for your company


- **Redirect URIs (required):**A list of allowlisted URIs that your merchant will be redirected to after they authorize your application. The redirect URI passed when generating the[connect URL](/braintree/docs/guides/extend/oauth/connect-urls)must be in this list or we will not authorize the redirect. Please use a full URI, including the protocol (httporhttps). In production,httpsis required
- **Configuration Name**: An internal name to help you distinguish between multiple applications. This will not be displayed to the merchant
- **PayPal BN Code**: A BN code (or Build Notation code) is provided to partners by PayPal for transaction tracking. If you do not have a BN code, leave this blank

[ ](/braintree/docs/guides/extend/oauth/connect-urls)

[Next Page:Connect URLs→](/braintree/docs/guides/extend/oauth/connect-urls)

