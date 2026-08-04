---
title: "PayPal Fastlane"
type: concept
category: technology
tags: [paypal, fastlane, guest-checkout, one-time-code, tokenization, checkout-acceleration, vault]
---

## PayPal Fastlane

PayPal Fastlane is a guest checkout acceleration product. It stores payment and shipping information against a buyer's email address and retrieves it with a one-time confirmation code — no password, no PayPal account required.

## What it is (and what it isn't)

- **Is**: a lightweight guest profile that pre-fills checkout forms
- **Is not**: a PayPal wallet or PayPal account
- **Relationship to PayPal**: Fastlane is a **separate profile** — it augments an existing PayPal integration but doesn't replace it
- **Works across merchants**: once a buyer is a Fastlane member, their info is pre-filled at any merchant with Fastlane integrated

## Two Flows

### Guest Flow (first-time buyer)

1. Buyer enters email → not found in Fastlane
2. Buyer enters payment + shipping info manually
3. Info is tokenized → passed in Orders API capture
4. Buyer becomes a Fastlane member

### Member Flow (returning Fastlane member)

1. Buyer enters email → found in Fastlane
2. PayPal retrieves stored payment + shipping info
3. Buyer receives a **one-time confirmation code** (no password)
4. Buyer confirms pre-filled info → tokenized → Orders API capture

## Integration Pattern

```text
JS SDK (components=buttons,fastlane) + data-sdk-client-token
→ paypal.Fastlane({ styles, shippingAddressOptions, cardOptions })
→ buyer enters email → identity.lookupCustomerByEmail()
→ if member: identity.triggerAuthenticationFlow() → OTP modal
→ FastlanePaymentComponent().render() → paymentComponent.getPaymentToken()
→ POST /v2/checkout/orders with payment_source.card.single_use_token
```

### Client token (SDK init) ≠ access token (API calls)

Fastlane requires a special **client token** for SDK initialization:

```javascript
// Extra params vs regular access token:
searchParams.append("response_type", "client_token");
searchParams.append("intent", "sdk_init");
searchParams.append("domains[]", DOMAINS);
```

Required sandbox capability: **Fastlane and Vault** must be enabled in Developer Dashboard → app → Features → Accept payments.

Required env var unique to Fastlane:

```env
DOMAINS=comma-separated-domains   # domains where Fastlane will be presented
```

### v6 sample implementation at `b5f2df2`

The current v6 sample loads the Fastlane component with a browser-safe client token, looks up the buyer by email, authenticates returning members, allows saved-address selection, and obtains a single-use payment token from `FastlanePaymentComponent`. The merchant server creates the order with `paymentSource.card.singleUseToken`.

The sample README names `/paypal-api/checkout/orders/create`, but its code calls `/paypal-api/checkout/orders/create-order-for-card-with-single-use-token`. Use the implementation route when reproducing this exact baseline.

## Key Distinctions vs PayPal Checkout / Vault

| Aspect | Fastlane | PayPal Checkout | PayPal Vault |
| ------ | -------- | --------------- | ------------ |
| Target user | Guest buyers | PayPal account holders | Any buyer |
| Authentication | Email + one-time code | PayPal login | Setup token flow |
| Profile stored at | PayPal (Fastlane profile) | PayPal account | Merchant vault token |
| Cross-merchant | Yes | Yes (PayPal account) | No (merchant-specific) |
| Password required | No | Yes | No (but requires initial consent) |

## Relevant Companies

- [[paypal]] — PayPal company overview

## Sources

- [[source-paypal-fastlane-getting-started]] — How Fastlane works: guest/member flows, swimlane diagram, Node.js setup
- [[source-github-v6-web-sdk-sample-integration]] — current browser-token, identity, address, and single-use-token sample
