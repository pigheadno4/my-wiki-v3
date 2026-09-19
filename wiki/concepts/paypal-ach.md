---
title: "PayPal ACH Web SDK Samples"
type: concept
category: technology
tags: [paypal, ach, web-sdk-v6, bank-payments]
---

## Scope

Commit-qualified integration evidence for PayPal bank ACH samples, not a claim of general merchant availability. The `default-branch@bb23e7c` sample adds an ACH Wallet path alongside the earlier ACH one-time button. Its README describes US merchants/USD and links a limited-release guide; current enablement must be verified separately.

## Wallet Flow at `bb23e7c`

1. Obtain a browser-safe client token; initialize `bank-ach-payments` with client metadata and checkout page type. The environment example now lists ACH Wallet alongside Fastlane for `DOMAINS` configuration.
2. Check `ach` eligibility using USD, `ONE_TIME_PAYMENT`, and an amount.
3. Create `createBankAchWalletPaymentSession()` with `standardEntryClassCode: "WEB"` and approval/error callbacks.
4. Connect the `bank-ach-wallet-payments` element to a lazy create-order callback. This differs from starting the earlier ACH button session with an order promise.
5. On approval, call the sample server's `POST /paypal-api/checkout/orders/:orderId/capture-ach-wallet`. It retrieves order details, constructs a consent record, calls `storeConsent()`, then captures.

## Sample Limitations

> [!warning] Contradiction - consent storage description
> The README describes storing consent, but `storeConsent()` only logs it. The handler's comment requires an APPROVED order, but its code checks GET HTTP status, not the order's lifecycle status. Neither establishes compliance or production-safe finalization.

- Bank details are accessed using a TypeScript assertion with optional properties. This does not prove the underlying SDK deserializer retains unmodeled fields.
- `authorizedAt` is the server's current time, not a separately verified buyer-consent timestamp.
- Eligibility uses USD 100.00, while the empty create-order body invokes a server default cart totaling USD 205.00. Align these values before testing a real integration.
- A capture response or sample success message does not establish final settlement.
- No React ACH Wallet example is added in this comparison.

## Related

- [[paypal]]
- [[paypal-checkout]]
- [[paypal-apm]]

## Sources

- [[source-github-v6-web-sdk-sample-integration]] - exact-SHA wallet client, capture handler and retained earlier button flow
- [[changelog-github-v6-web-sdk-sample-integration]] - introduction and subsequent commit history
