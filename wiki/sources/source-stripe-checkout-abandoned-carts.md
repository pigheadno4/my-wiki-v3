---
title: "Stripe Checkout: Recover Abandoned Carts"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-abandoned-carts-2025.md"
tags: [stripe, checkout, abandoned-carts, recovery, promotional-emails, consent, webhooks, conversion]
---

## Summary

Guide for recovering abandoned Checkout sessions via email. Covers consent collection, the `after_expiration.recovery` session param, the `checkout.session.expired` webhook, recovery URL handling, anti-spam considerations, conversion tracking, and optional promo code integration.

## Key Takeaways

- **Prerequisites**: `consent_collection.promotions: 'auto'` + `after_expiration.recovery.enabled: true` on session create
- **Recovery URL**: `after_expiration.recovery.url` in `checkout.session.expired` payload; creates exact copy of original session; valid 30 days
- **Only email consented customers**: check `session.consent.promotions === 'opt_in'`; email from `session.customer_details.email` (only present if consent given)
- **Anti-spam**: each abandoned session fires separate event — track sent recovery emails to avoid spamming
- **`expires_at`**: shorten to 30min minimum (default 24h) to detect abandonment sooner
- **Conversion tracking**: `session.recovered_from` on `checkout.session.completed` — references original expired session ID
- **Promo codes**: `after_expiration.recovery.allow_promotion_codes: true` — recovery session shows promo code field

## Recovery Flow

```
1. Create session with:
   - consent_collection.promotions: 'auto'
   - after_expiration.recovery.enabled: true

2. Session expires → checkout.session.expired fires
   
3. Extract from webhook:
   - email = session.customer_details?.email
   - recoveryUrl = session.after_expiration?.recovery?.url
   - consented = session.consent?.promotions === 'opt_in'

4. Guard checks:
   - Skip if no email or no recoveryUrl
   - Skip if not consented
   - Skip if already sent recovery email to this address

5. Send email with recoveryUrl embedded

6. Customer opens URL → new session (copy of original) created
   → checkout.session.completed fires with recovered_from = original_session_id
```

## Session Params

```js
stripe.checkout.sessions.create({
  customer: '...',  // or customer_account
  consent_collection: { promotions: 'auto' },
  after_expiration: {
    recovery: {
      enabled: true,
      allow_promotion_codes: true,  // optional
    },
  },
  expires_at: Math.floor(Date.now() / 1000) + (3600 * 2),  // optional: 30min min
  ...
})
```

## `checkout.session.expired` Payload (recovery enabled)

```json
{
  "consent": { "promotions": "opt_in" },
  "after_expiration": {
    "recovery": {
      "enabled": true,
      "url": "https://buy.stripe.com/r/live_...",
      "expires_at": 1622908282
    }
  }
}
```

## Conversion Tracking

Listen to `checkout.session.completed`:

```js
const recoveredFrom = session.recovered_from;
if (recoveredFrom) {
  // Log: session.id was recovered from recoveredFrom (original abandoned session)
}
```

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-how-checkout-works]] — Promotional email consent (consent_collection.promotions)

## Raw Sources

- [[stripe-checkout-abandoned-carts-2025]] — Abandoned cart recovery: consent setup, after_expiration.recovery, checkout.session.expired webhook, recovery URL, anti-spam, expires_at, conversion tracking, promo codes
