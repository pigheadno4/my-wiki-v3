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

## Braintree Adapter Error Boundary

The independent `braintree-web@3.145.0` adapter still depends on `@paypal/fastlane-sdk-loader@1.2.1`. Its load/initialization catch now preserves existing Braintree errors; other errors become `FASTLANE_SDK_LOAD_ERROR` with the original error under `details.originalError`. This improves adapter diagnostics, not Fastlane eligibility or the delegated identity/payment flow. Braintree processing must not be inferred to use the direct PayPal Orders API pattern above. Source: [[source-github-braintree-web]].

## Relevant Companies

- [[paypal]] — PayPal company overview

## Sources

- [[source-braintree-docs-guides-fastlane-setup-integration]] - collected unversioned Braintree website setup page for Sandbox-account creation, Account Settings enablement, CSP-update orientation and the client-side next-step route; not SDK-version, saved-method/profile lifecycle, current eligibility, deployed client/server behavior or payment-execution evidence

- [[source-braintree-docs-guides-fastlane-server-side-node]] - unversioned Braintree Node-routed server-side guide for root-domain-qualified client-token generation and payment-time shipping-profile updates, with Braintree SDK and GraphQL material-input, device-data and success-conditioned vault-option locators; examples are not direct PayPal Orders API, current eligibility, Vault-outcome or payment-execution evidence

- [[source-braintree-docs-guides-fastlane-client-side-node]] - collected Braintree website client-side integration guide at the `/node` route for same-version Web `3.120.0`+ initialization, email lookup/authentication and guest fallback, conditional watermark/compliance notice, member/guest payment-component rendering, the example's payment-token plus previously captured device-data handoff to the merchant server to complete checkout, and the separate statement that the payment token can be used like a `paymentMethodNonce` for Transact or Vault; browser HTML/JavaScript guidance, not a Node runtime implementation, current eligibility, direct PayPal Orders API, or payment/Vault outcome evidence

- [[source-braintree-docs-guides-fastlane-overview]] - collected unversioned Braintree website overview for Fastlane identity, guest versus authenticated-profile framing, merchant integration conditions and the snapshot country matrix; not current availability, eligibility, exact-version GitHub or payment-execution evidence

- [[source-braintree-docs-guides-fastlane-faq]] - collected unversioned Braintree FAQ for provisioning/disablement diagnostics, guest fallback, token lifetime and refresh, delivery/pickup controls, CSP guidance, integration-pattern responsibilities and an unresolved internal vaulting contradiction; not current eligibility, country-support, compliance or payment/Vault-outcome evidence

- [[source-braintree-docs-guides-fastlane-appendix]] - collected unversioned Braintree Fastlane appendix for profile-field priority, client-returned payment-token lifetime, transaction-time vaulting limitations, allowed-location input and checkout-reload authentication guidance; preserves the captured vault-ordering inconsistency and does not identify an SDK version or environment

- [[source-braintree-docs-guides-fastlane-best-practices]] - collected unversioned Braintree website best-practices guide for guest/member checkout UX, refresh authentication, server-side profile-change handoff and accessible styling; recommendations are not runtime or payment guarantees

- [[source-braintree-docs-guides-fastlane-testing-go-live]] - unversioned Braintree website checklist for Sandbox Fastlane guest/member scenarios, profile-update cases, OTP and test-card fixtures; expected checklist outcomes do not establish production eligibility or payment success

- [[source-braintree-docs-guides-fastlane-advanced-option]] - Braintree Fastlane advanced-options route for conditional saved-card versus card-field rendering, client payment-token/device-data handoff to merchant-server processing, shipping and store-pickup safeguards, and optional vaulting; not direct PayPal Orders API or payment-outcome evidence

- [[source-braintree-docs-guides-fastlane-flexible-payment]] - collected Braintree website guide to the client-side Flexible Integration, where the merchant owns guest billing collection, member card/address rendering and selector state, and Card Component token acquisition; preserves SDK-version, authentication, Sandbox OTP, missing-profile-data and token-versus-payment-execution boundaries

- [[source-paypal-fastlane-getting-started]] — How Fastlane works: guest/member flows, swimlane diagram, Node.js setup
- [[source-github-v6-web-sdk-sample-integration]] — current browser-token, identity, address, and single-use-token sample
- [[source-github-braintree-web]] - independently versioned Braintree loader and error boundary
