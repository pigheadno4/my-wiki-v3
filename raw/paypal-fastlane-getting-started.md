<!-- Source URL: https://developer.paypal.com/docs/checkout/fastlane/getting-started/ -->
<!-- Fetched: 2026-04-13 -->

# How Fastlane Works

Fastlane is PayPal's quick guest checkout solution. It securely saves and retrieves payment and shipping information for Fastlane members. Fastlane members enter their email and receive pre-filled checkout forms.

## Consumer Benefits

- Members can enter their email address and receive autofilled checkout forms.
- Members can securely check out with their email address at any site that integrates Fastlane.
- No password required. Members get a one-time confirmation code after entering their email address.

Fastlane is a separate profile from a PayPal account and is meant to augment your existing PayPal integration and allow guests to enjoy faster checkouts in a lightweight manner.

![Workflow for integrating PayPal Fastlane Checkout](assets/SwimlaneDiagram.png)

## Integration workflow

1. The script tag fetches the PayPal JS SDK to render the checkout page. You create a client token for the session.
2. The buyer enters the email address on the client side.
3. PayPal checks if the email is associated with a Fastlane profile and triggers the guest or member flow.

### Guest Flow

1. The email is not associated with a Fastlane profile. The customer enters their payment information and shipping address.
2. The payment information is tokenized and sent to PayPal along with other information entered.
3. The information is passed in an Orders API capture request and the response is sent to the merchant.

### Member Flow

1. The email is associated with a Fastlane profile. PayPal retrieves payment and shipping information.
2. The buyer confirms information and pays. The payment is tokenized and sent to PayPal with the info.
3. The information is passed in an Orders API capture request and a response is sent to the merchant.

## How Fastlane speeds up guest checkout flow

After a user signs up for Fastlane, they enter their email to get the member flow at any site with a Fastlane integration.

### Guest sign-up at checkout

1. Guest bypasses signed-in checkout and PayPal checkout.
2. Guest is prompted to enter their email address.
3. Guest enters payment methods and shipping info to associate with the email.
4. Guest completes checkout and becomes a Fastlane member.

Guest flow screenshots:

![Merchant cart](assets/merchantCart.png)
![Merchant contact — guest](assets/merchantContact.png)
![Merchant payment — guest](assets/merchantPayment.png)
![Merchant confirm](assets/merchantConfirm.png)

### Members receive prefilled info at checkout

1. Member bypasses signed-in checkout and PayPal checkout.
2. Member enters their email and receives a one-time confirmation code.
3. Fastlane returns autofilled payment and shipping info.
4. Member completes checkout.

Member flow screenshots:

![Merchant cart](assets/merchantCart.png)
![Merchant contact — member](assets/merchantMemberContact.png)
![Merchant payment — member](assets/merchantMemberPayment.png)
![Merchant confirm](assets/merchantConfirm.png)

## Set up your development environment (Node.js)

### 1. Install Node.js and npm
Node.js version 18 or higher and npm required. Download from nodejs.org.

### 2. Install dependencies
```bash
npm init
npm install express dotenv cors consolidate mustache
```

- `dotenv` — loads environment variables from `.env` into `process.env`
- `express` — Node.js web application framework
- `mustache` (with `consolidate`) — lightweight static HTML templating
- `cors` — enables CORS middleware for Express

### 3. Verify package.json
```json
{
  "name": "test-project",
  "version": "1.0.0",
  "dependencies": {
    "consolidate": "^1.0.4",
    "cors": "^2.8.5",
    "dotenv": "^16.4.5",
    "express": "^4.21.1",
    "mustache": "^4.2.0"
  }
}
```

### 4. Set up .env
```
PAYPAL_CLIENT_ID=YOUR_CLIENT_ID_HERE
PAYPAL_CLIENT_SECRET=YOUR_CLIENT_SECRET_HERE
DOMAINS=YOUR_DOMAINS_HERE
```

Replace `DOMAINS` with a comma-separated list of domain name(s) where Fastlane will be presented.

## Know before you code

- Requires a PayPal developer account and sandbox credentials.
- Requires a sandbox business account with **Fastlane and Vault** enabled:
  1. Developer Dashboard → toggle Sandbox → Apps & Credentials → select/create app
  2. Features → Accept payments → enable **Fastlane and Vault** checkboxes → Save Changes

## Resources

- JavaScript SDK — adds PayPal-supported payment methods
- Orders REST V2 API — create, update, retrieve, authorize, and capture orders
- Sandbox testing guide — test before production
