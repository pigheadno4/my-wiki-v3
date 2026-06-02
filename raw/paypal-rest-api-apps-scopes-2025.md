<!-- Source URL: https://docs.paypal.ai/developer/how-to/apps-scopes-credentials -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Apps, scopes, and credentials

PayPal Apps are registered apps within the PayPal Developer ecosystem that verify and authorize your software to interact with PayPal's services. Each app receives unique credentials (client ID and client secret) that establish a secure connection between your app and PayPal's payment processing network.

Register your application with PayPal to get the credentials needed for API access and understand which permissions your app requires.

PayPal Apps operate on a modern REST API architecture and follow a structured development process:

- App Registration
- Sandbox Testing
- API Integration

PayPal's sandbox environment provides developers with testing accounts to simulate real payment scenarios without processing actual transactions. PayPal sandbox provides testing environments with two main account types:

## Understanding scopes

Scopes define your app's permissions and access levels to PayPal services. The scope field in the authentication response shows all available permissions for your app.

### Common PayPal API scopes

#### Payment processing

- `https://uri.paypal.com/services/payments/payment/authcapture` - Process payments and captures
- `https://uri.paypal.com/services/payments/payment` - Real-time payment processing
- `https://uri.paypal.com/services/payments/refund` - Process refunds
- `https://uri.paypal.com/services/payments` - General payments API access

#### Vault services

- `https://uri.paypal.com/services/vault/payment-tokens/creditcard` - Store credit card info
- `https://uri.paypal.com/services/vault/payment-tokens/read` - Manage stored credit cards

#### Business services

- `https://uri.paypal.com/services/invoicing` - Create and manage invoices
- `https://uri.paypal.com/services/subscriptions` - Subscription management
- `https://uri.paypal.com/services/payments/payouts` - Send payouts

#### Dispute management

- `https://uri.paypal.com/services/disputes/read-buyer` - Read buyer dispute info
- `https://uri.paypal.com/services/disputes/read-seller` - Read seller dispute info
- `https://uri.paypal.com/services/disputes/update-seller` - Update seller dispute status

#### System integration

- `https://uri.paypal.com/services/webhooks` - Webhook management
- `openid` - OpenID Connect authentication

### PayPal API credentials

PayPal REST APIs use two types of credentials for authentication:

**Client ID**: A public identifier for your PayPal app. Safe to use in client-side code and sufficient for basic payment buttons and card fields.

**Client Secret**: A private key that verifies your app for API calls. Must be kept secure and used only server-side.

### Getting credentials

Obtain credentials through the PayPal Developer Dashboard:

- New accounts get a "Default Application" with ready-to-use credentials
- Create additional apps through "Create App" in Apps & Credentials
- Copy the client ID and client secret for your setup

For detailed implementation guides, refer to each service area's specific PayPal API docs.
