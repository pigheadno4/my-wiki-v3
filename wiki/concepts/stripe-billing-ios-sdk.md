---
title: "Stripe BillingSDK for iOS"
type: concept
category: framework
tags: [stripe, ios, swift, billing, subscriptions, entitlements, buy-button, customer-portal, customer-sessions, preview]
---

## Overview

BillingSDK for iOS (`github.com/stripe-samples/billing-ios-sdk`) is a **private preview** higher-level SDK for managing subscription lifecycle on iOS. It wraps Customer Sessions, buy buttons, entitlement checking, and customer portal into a single unified interface — distinct from the lower-level `stripe-ios` SDK.

## Requirements

- iOS 15.0+, macOS 12.0+, Xcode 15.0+
- Stripe account with private preview access
- Backend server to create Customer Sessions

## Installation

SPM via Xcode → File → Add Package Dependencies:
```
https://github.com/stripe-samples/billing-ios-sdk
```

## Architecture

The SDK authenticates via Customer Sessions created by your backend. The backend must create a session with the required components enabled and return `{clientSecret, expiresAt, customer}`. HTTP 401 puts the SDK in unauthenticated state.

Required Customer Session components:
```js
components: {
  buy_button: { enabled: true },
  active_entitlements: { enabled: true },
  customer_portal: { enabled: true }
}
```

## SDK initialization

```swift
let config = BillingSDK.Configuration(
    publishableKey: "pk_test_...",
    maximumStaleEntitlementsDuration: TimeInterval(60 * 5)
)
let billing = BillingSDK(configuration: config)
billing.setCustomerSessionProvider { await fetchCustomerSession() }
billing.onEntitlementsChanged { entitlements in ... }
```

Thread-safe — all methods callable from any thread.

## Authentication management

- `setCustomerSessionProvider` — async callback called by SDK when authentication is needed. Return `nil` → unauthenticated state.
- `billing.reset()` — call on sign-out to clear session data and caches.
- SDK auto-refreshes sessions before expiry.

## Buy buttons

```swift
let button = try await billing.getBuyButton(id: "buy_btn_xxx")
button.view() // SwiftUI view
```

- Button ID comes from Stripe Dashboard
- **Works without authentication** — creates a new Customer if needed during purchase
- Products should have Entitlements attached for entitlement gating to work

## Entitlements

```swift
// Check one feature
let has = try await billing.hasEntitlement(lookupKey: "premium_tier")

// Get all
let all = try await billing.getActiveEntitlements(forceRefresh: true)

// React to changes
billing.onEntitlementsChanged { updated in ... }
```

- Returns empty array when unauthenticated
- `forceRefresh: true` bypasses the stale entitlement cache
- Cache TTL: `maximumStaleEntitlementsDuration` in Configuration

## Customer portal

```swift
let portal = try await billing.getCustomerPortal()
portal.presentCustomerPortal(from: vc)   // in-app (recommended)
portal.redirectToCustomerPortal()         // opens browser
```

- **Requires active authenticated session** — throws `.unauthenticated` if not logged in
- Handles subscription changes, payment methods, billing info

## vs stripe-ios SDK

| | BillingSDK (this) | stripe-ios |
|---|---|---|
| Buy buttons | Built-in | Not included |
| Entitlement checking | Built-in | Not included |
| Customer portal | Built-in | Separate integration |
| Auth model | Customer Sessions | STPAPIClient direct |
| Status | Private preview | GA (v25+) |

## Sources

- [[source-stripe-billing-ios-sdk]] — Stripe docs: BillingSDK for iOS integration guide (private preview)
