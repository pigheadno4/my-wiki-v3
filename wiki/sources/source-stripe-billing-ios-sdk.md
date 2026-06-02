---
title: "Stripe — Manage Subscriptions on iOS (BillingSDK for iOS)"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-billing-ios-sdk-2026.md"
tags: [stripe, ios, swift, billing, subscriptions, entitlements, buy-button, customer-portal, customer-sessions]
---

## Summary

Integration guide for the BillingSDK for iOS (`github.com/stripe-samples/billing-ios-sdk`) — a higher-level private preview SDK wrapping subscription purchase, entitlement checking, and customer portal into a unified iOS experience. Distinct from the lower-level `stripe-ios` SDK.

## Status

**Private preview** — requires Stripe account access to private preview.

## Requirements

- iOS 15.0+ and macOS 12.0+
- Xcode 15.0+
- Backend server creating Customer Sessions
- SPM install via `https://github.com/stripe-samples/billing-ios-sdk`

## Architecture

```
iOS App ←→ BillingSDK ←→ Customer Session endpoint (your backend) ←→ Stripe
```

Backend creates a Customer Session with these components enabled: `buy_button`, `active_entitlements`, `customer_portal`. Returns `{clientSecret, expiresAt, customer}` to the SDK. HTTP 401 → SDK enters unauthenticated state.

Backend API version used in example: `2025-07-30.basil`.

## SDK initialization

```swift
let config = BillingSDK.Configuration(
    publishableKey: "pk_test_...",
    maximumStaleEntitlementsDuration: TimeInterval(60 * 5) // 5 min cache TTL
)
let billing = BillingSDK(configuration: config)
billing.setCustomerSessionProvider { await fetchCustomerSession() }
billing.onEntitlementsChanged { updatedEntitlements in ... }
```

Thread-safe — all methods can be called from any thread.

## Authentication

`setCustomerSessionProvider` — async callback the SDK calls whenever it needs to authenticate. Returns `UBCustomerSessionDetails?`:
- Returns `nil` → unauthenticated state (e.g. HTTP 401 from backend)
- `billing.reset()` on sign-out to clear session + caches

## Buy buttons

```swift
let button = try await billing.getBuyButton(id: "buy_btn_xxx")
button.view()  // SwiftUI view; or access raw data for custom UI
```

- Linked to a specific Stripe product/price via Dashboard
- **Works unauthenticated** — creates a new Customer during purchase if needed
- Products should have Entitlements attached if entitlement checking is used

## Entitlements

```swift
// Boolean check
let has = try await billing.hasEntitlement(lookupKey: "premium_tier")

// Full list (forceRefresh bypasses cache)
let all = try await billing.getActiveEntitlements(forceRefresh: true)

// Change listener
billing.onEntitlementsChanged { updatedEntitlements in ... }
```

- Returns empty array when unauthenticated
- Cache TTL controlled by `maximumStaleEntitlementsDuration`

## Customer portal

```swift
let portal = try await billing.getCustomerPortal()
portal.presentCustomerPortal(from: viewController) // in-app (recommended)
// or
portal.redirectToCustomerPortal() // opens in browser
```

- **Requires authenticated session** — throws `.unauthenticated` if no session
- Lets users manage subscriptions, payment methods, billing info

## Key behavioral differences from stripe-ios SDK

| Feature | BillingSDK (this) | stripe-ios |
|---|---|---|
| Buy buttons | Built-in, Dashboard-configured | Not built-in |
| Entitlements | Built-in (`hasEntitlement`) | Not built-in |
| Customer portal | Built-in (`getCustomerPortal`) | Separate integration |
| Auth model | Customer Sessions | STPAPIClient + publishable key |
| Status | Private preview | GA |

## Related pages

- [[stripe-billing-ios-sdk]] — concept page
- [[stripe-ios-sdk]] — lower-level stripe-ios SDK
- [[stripe-entitlements]] — entitlements concept
- [[stripe]] — company page

## Raw Sources

- [[stripe-billing-ios-sdk-2026]] — verbatim Stripe docs webpage
