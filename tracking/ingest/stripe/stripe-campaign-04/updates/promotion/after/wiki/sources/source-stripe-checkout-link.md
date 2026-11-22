---
title: "Stripe Docs — Link with Checkout"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/link/checkout-link"
raw_files:
  - "stripe-payments-link-checkout-link-2026-11-07.md"
  - "stripe-checkout-link-2025.md"
tags: [stripe, link, checkout, dynamic-payment-methods, setup-intents, connect, otp]
---

## Summary

The May 8 and November 7, 2026 guides cover Link in Stripe-hosted and embedded prebuilt Checkout and point separately to Payment Links. Link lets customers save and reuse payment information, and it autofills for logged-in Link customers even when they originally saved it with another business. The described Link-as-payment-method Checkout flow returns `payment_method.type=link` for a received payment.

## Existing Checkout integrations

- **Dynamic methods.** Both guides direct an existing Checkout integration to enable Link in Dashboard and remove its historical manual list. Currency restricts which methods appear. The two guides make a manual-listing exception for collecting cards for future use with Setup Intents. Scope any historical request syntax to its API version and request object.
- **Historical manual examples.** Both guides' prose asks for `link` and `card` in `payment_method_types`, with all line items in the same currency. The May Node.js sample includes both. The November Ruby sample omits `payment_method_types` despite appearing under manual listing. The November dynamic example uses cURL.
- **Checkout Session Create on Endive.** The separate [Checkout changelog](https://docs.stripe.com/changelog/endive/2026-09-30/remove-payment-method-types-checkout-sessions) says `2026-09-30.endive` rejects writable `payment_method_types` with HTTP 400. Use Dashboard-managed dynamic methods, a compatibility-filtered `allowed_payment_method_types` list or `excluded_payment_method_types` to omit specific methods. The Session's computed `payment_method_types` response shows the compatible subset. Configuration and eligibility determine display.
- **Intents on Endive.** The separate [Intents changelog](https://docs.stripe.com/changelog/endive/2026-09-30/removes-the-payment-method-types-parameter-from-payment-intents-and-setup-intents) separately identifies PaymentIntent create/update/confirm and SetupIntent create/update in `2026-09-30.endive` as rejecting the writable field with HTTP 400 and `payment_method_types_no_longer_supported`. The computed property remains read-only. The changelog's Impact text names `2026-08-26.preview`; its linked endpoints and REST table identify Endive. The Setup Intents exception in the Checkout guide does not establish current literal field syntax on those endpoints.
- **Explicit Link route selection.** The November [[source-stripe-link-payment-integrations|Link integrations guide]] says an allowlist containing `link`, even alongside `card`, selects the Link-as-payment-method route with `PaymentMethod.type=link`. A list containing `card` without `link` selects the card-specific route with `PaymentMethod.type=card` and `card.wallet.type=link` for an eligible Link transaction. This route selection leaves specific Link display and payment outcomes unverified.

## Hosted and embedded scope

The dated server-side Session examples use USD, `mode=payment` and `success_url` and omit `ui_mode`. The separate November [Session create reference](https://docs.stripe.com/api/checkout/sessions/create) defaults omitted `ui_mode` to `hosted_page`, disallows `success_url` with `embedded_page` or `elements`, and requires `return_url` for those UIs when redirect-based methods are enabled. A return alone does not establish payment completion.

May's Checkout guide says Link requires domain registration without distinguishing UIs. November omits that sentence. The separate [[source-stripe-pmd-registration|domain registration guide]] identifies Link in Elements and Checkout's embeddable form. Its May full capture requires registration of every web domain and subdomain showing Link in Elements or Checkout's embeddable form. Its November selector retains that UI scope and links Dashboard and API instructions. That evidence supplies no universal hosted Checkout domain-registration requirement.

## Funding, pricing and settlement

Both Checkout guides say Link carries no additional Checkout fee compared with other card payments. The May guide limits the named support to credit cards, debit cards and qualified US bank-account purchases. November lists those same funding methods without “only.” The separate [[source-stripe-link-payment-methods|Link funding groups guide]] documents additional groups, business and transaction eligibility, and fees according to the merchant's pricing agreement. The separate Link integrations guide documents a blended rate and IC+ limitation for Link as a payment method. Checkout card pricing does not establish fees for every funding group.

May describes additional funding sources using the same settlement time and guarantees, with no integration changes. November retains the same settlement time and no integration changes, and describes the same processing behavior. The separate Link integrations guide speaks of successful payments reaching the Stripe balance on the card timeline. Bank payout is a separate event.

## Sandbox Link authentication

Both guides permit any valid email for a sandbox Link account. These accounts are tied to a publishable key. Treat them as if publicly available and keep real user data out. OTP outcomes below are for authentication in the sandbox.

| Code | Outcome |
| --- | --- |
| Any 6 digits (not below) | Sandbox authentication succeeds |
| `000001` | Error: code invalid |
| `000002` | Error: code expired |
| `000003` | Error: max attempts exceeded |

## Connect and disable

Both guides describe Link as automatically available to connected accounts using Checkout through a Connect platform. Platform and connected-account Dashboard settings are managed separately. The connected account can manage payments processed through and outside its platform in its own Link settings. Account availability and a particular session displaying Link are separate.

Disable Link in Dashboard Payment methods individually per payment method configuration. The change might take a few minutes to take effect.

## May 8, 2026 capture assets

- `raw/assets/stripe-link-in-checkout.png` — Link in Checkout UI (599 KB)
- `raw/assets/stripe-link-enable-dashboard.png` — Link enabled in Dashboard (196 KB)

## Related Pages

- [[stripe-link]]
- [[stripe-checkout]]
- [[source-stripe-pmd-registration]]
- [[source-stripe-link]] — broader Link overview
- [[stripe]]

## Raw Sources

- [[raw/stripe-payments-link-checkout-link-2026-11-07|November 7, 2026 full Link with Checkout guide]] — 114 lines. See Checkout enablement at lines 9–38, server-side examples at 40–76, sandbox and funding at 78–95, and Connect/disable at 97–108.
- [[raw/stripe-checkout-link-2025|May 8, 2026 full Link with Checkout guide]] — verbatim webpage content, 128 lines, including May Node.js examples and local capture images.
