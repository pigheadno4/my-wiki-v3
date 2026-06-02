---
title: "PayPal Fastlane: How It Works (Getting Started)"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-fastlane-getting-started.md"
  - "paypal-fastlane-integrate.md"
  - "paypal-fastlane-integrate-flexible.md"
  - "paypal-fastlane-3d-secure.md"
  - "paypal-fastlane-reference.md"
  - "paypal-fastlane-upgrade.md"
  - "paypal-fastlane-sdk-v6.md"
tags: [paypal, fastlane, guest-checkout, one-time-code, tokenization, orders-api, node-js, javascript-sdk, javascript-sdk-v6]
---

## PayPal Fastlane: How It Works (Getting Started)

Overview and dev environment setup for PayPal Fastlane — a guest checkout acceleration product that pre-fills payment and shipping info for returning buyers using email + one-time code (no password).

Source URL: <https://developer.paypal.com/docs/checkout/fastlane/getting-started/>

## Key Takeaways

### What Fastlane is

Fastlane is PayPal's **quick guest checkout** solution — separate from a PayPal account. It stores payment and shipping info against a buyer's email and retrieves it with a one-time confirmation code (no password). Works at any merchant site that integrates Fastlane.

Key distinction: Fastlane is a **lightweight guest profile**, not a PayPal wallet. Meant to augment existing PayPal integrations, not replace them.

### Two flows

| Flow | Trigger | Experience |
| ---- | ------- | ---------- |
| **Guest** | Email not in Fastlane | Buyer enters payment + shipping → tokenized → captured → becomes Fastlane member |
| **Member** | Email in Fastlane | PayPal retrieves stored info → buyer confirms → one-time code → tokenized → captured |

### Integration workflow (high level)

1. Load PayPal JS SDK via script tag; create a **client token** for the session
2. Buyer enters email on client side
3. PayPal checks email against Fastlane profiles → routes to guest or member flow
4. Both flows end with tokenized payment passed in an **Orders API capture request**

### Sandbox capability requirement

Sandbox business account must have **Fastlane and Vault** enabled:
Developer Dashboard → Sandbox → Apps & Credentials → app → Features → Accept payments → enable **Fastlane and Vault**.

### Environment variables

Three required env vars:

```env
PAYPAL_CLIENT_ID=...
PAYPAL_CLIENT_SECRET=...
DOMAINS=...        # comma-separated domains where Fastlane will be presented
```

`DOMAINS` is Fastlane-specific — not required for standard Expanded Checkout.

### Node.js dependencies

```bash
npm install express dotenv cors consolidate mustache
```

Node.js 18+ required.

### Integration details (from integrate page)

#### Client token vs access token

Fastlane requires a **client token** (not a regular access token) for SDK initialization — generated with extra parameters:

```javascript
searchParams.append("response_type", "client_token");
searchParams.append("intent", "sdk_init");
searchParams.append("domains[]", DOMAINS);
```

#### Key Fastlane SDK methods

| Method | Purpose |
| ------ | ------- |
| `identity.lookupCustomerByEmail(email)` | Returns `customerContextId` if Fastlane/PayPal member |
| `identity.triggerAuthenticationFlow(id)` | Shows OTP modal; returns `AuthenticatedCustomerResult` |
| `profile.showShippingAddressSelector()` | Opens address picker for authenticated members |
| `FastlanePaymentComponent()` | Pre-built payment UI (card + billing address) |
| `FastlaneWatermarkComponent()` | "Powered by Fastlane" logo + tooltip |
| `paymentComponent.getPaymentToken()` | Returns `paymentToken.id` for server-side capture |
| `paymentComponent.setShippingAddress(addr)` | Updates shipping on payment component |

#### Payment source on Orders API

Fastlane uses `single_use_token`, not a vault token or network token:

```json
"payment_source": { "card": { "single_use_token": "PAYMENT_TOKEN_ID" } }
```

#### Special use cases

- **Store pickup**: `shipping.type = "PICKUP_IN_STORE"` prevents store address being saved to buyer's Fastlane profile
- **Vault with transaction**: add `store_in_vault` to orders request → returns vault ID for future use
- **Vault without transaction**: payment token generated but Fastlane profile NOT created until a transaction completes

#### Sandbox testing

OTP codes: `111111` = success; any other 6 digits = failure. No SMS sent in sandbox.

Test cards: Visa 4005519200000004, Visa 4012000077777777, Mastercard 5555555555554444, Amex 378282246310005.

Phone number must be valid (not `111-111-1111`) for Fastlane profile creation.

#### PayPal member handling

Handled automatically by SDK — no extra integration needed. `lookupCustomerByEmail()` returns a `customerContextId`; `triggerAuthenticationFlow()` shows CTA to create Fastlane profile from PayPal account. If accepted → `profileData` like member; if dismissed → empty `profileData` → treat as guest.

#### Reference: key facts

- **paymentToken validity**: 3 hours from issuance
- **OTP session**: a member who authenticated won't receive OTP for additional transactions with the same merchant during the same session; re-authentication required after session expires
- **MOTO not supported**: Fastlane does not support mail order/telephone order or manual entry
- **Fastlane disabled fallback**: if `identity.triggerAuthenticationFlow()`, `profile.showShippingAddressSelector()`, or `profile.showCardSelector()` return `undefined`, Fastlane is disabled — SDK falls back to guest experience automatically
- **`authenticationState` values**: `'succeeded'`, `'failed'`, `'canceled'`, `'not_found'`
- **Allowed font families**: Arial, Verdana, Tahoma, Trebuchet MS, Times New Roman, Georgia, Garamond, Courier New, Brush Script MT (no custom web fonts)
- **WCAG AA required**: all Fastlane integrations must conform; colors auto-revert to defaults if contrast fails
- **Load SDK on checkout page load**: delayed loading causes conversion issues
- **Call `triggerAuthenticationFlow()` on every page reload**: returns new single-use token each time

#### 3D Secure for Fastlane

Two 3DS integration options:

| Option | Retry on failure? | enrollmentStatus available? |
| ------ | ----------------- | -------------------------- |
| **JS SDK** (`ThreeDomainSecureClient`) | Yes — can repeat or fall back | No |
| **Orders v2 API** | No — one attempt per transaction | Yes |

JS SDK 3DS requires adding `three-domain-secure` to the `components` param and using `nonce` from the client token response.

Key JS SDK flow:

1. `window.paypal.ThreeDomainSecureClient` → `isEligible(params)` with amount, currency, nonce
2. `threeDomainSecureComponent.show()` → `{ liabilityShift, authenticationState, nonce }`
3. On `liabilityShift: "POSSIBLE"` → continue; on `"NO"` or `"UNKNOWN"` → do not proceed

Orders v2 API 3DS: add `payment_source.card.attributes.verification.method: "SCA_WHEN_REQUIRED"` to the create order request.

**enrollmentStatus is not available from the JS SDK** — only from Orders v2 server-side response.

Sandbox test card for 3DS: Mastercard `5186459910794125`, any future expiry, CVV 123.

Vault with 3DS: add `attributes.vault.store_in_vault: "ON_SUCCESS"` to orders request. Vault-only (no transaction): `POST /v3/vault/payment-tokens` with `payment_source.token.type: "NONCE"`.

#### Quick Start vs Flexible

| Aspect | Quick Start | Flexible |
| ------ | ----------- | -------- |
| Payment component | `FastlanePaymentComponent()` — pre-built | `FastlaneCardComponent()` — raw card fields |
| Billing address | Inside payment component | Merchant's own billing form |
| Card selector | Built-in | `profile.showCardSelector()` |
| `getPaymentToken()` | No args | `{ billingAddress }` required |
| State tracking | Simpler | `memberHasSavedPaymentMethods` required |
| Backend | Identical | Identical |

#### Accessibility requirement

`backgroundColor` vs `textColor` contrast ratio must be ≥ 4.5:1. PayPal auto-corrects if not met.

## Raw Sources

- [[paypal-fastlane-getting-started]] — verbatim content with swimlane diagram, guest/member flow screenshots, Node.js setup
- [[paypal-fastlane-integrate]] — Quick Start integration: HTML, init-fastlane.js (all SDK methods), Node.js server (client token, access token, createOrder), test cards/OTP, vaulting, PayPal member handling
- [[paypal-fastlane-integrate-flexible]] — Flexible integration: FastlaneCardComponent, separate billing address form, showCardSelector(), memberHasSavedPaymentMethods state, getPaymentToken({ billingAddress })
- [[paypal-fastlane-3d-secure]] — Fastlane 3DS: JS SDK component vs Orders v2 API, nonce from client token, ThreeDomainSecureClient, liabilityShift/authenticationState, enrollmentStatus (server only), sandbox test card
- [[paypal-fastlane-reference]] — Full reference: troubleshooting, FAQs, best practices, all TypeScript types (ProfileData, PaymentToken, AuthenticatedCustomerResult), card fields, StyleOptions, WCAG AA requirement
- [[paypal-fastlane-upgrade]] — Upgrade guide: PayPal buttons (add fastlane component + data-client-metadata-id) and card-fields (swap card-fields for fastlane) → same email/auth flow for both
- [[paypal-fastlane-sdk-v6]] — SDK v6 integration (docs.paypal.ai): `clientToken` auth, `createFastlane()`, email-lookup → member/guest routing, `getPaymentToken()` → `card.singleUseToken`, `FastlaneWatermarkComponent` required, `clientMetadataId: crypto.randomUUID()`

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-fastlane]] — Fastlane concept page
- [[paypal-checkout]] — standard PayPal Checkout (Fastlane augments this)
- [[paypal-vault]] — vault/payment tokens (Fastlane uses vault capability)
