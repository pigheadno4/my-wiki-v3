---
title: "Stripe: Manage Recurring Payments on Apple Pay"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/apple-pay/apple-pay-recurring"
raw_files:
  - "stripe-apple-pay-recurring-2025.md"
tags: [stripe, wallets, apple-pay, recurring, dpan, mpan, cryptogram, cit, mit, setup-intent, off-session]
---

## Summary

Stripe's May 7, 2026 guide describes the customer-initiated transaction (CIT) that consumes an Apple Pay cryptogram before later off-session merchant-initiated transactions (MITs). [[stripe]] Checkout and Elements automatically apply the guide's best practices; its manual implementation sequence is for API integrations. See [[stripe-wallets]]. The November 7 same-URL capture changes presentation only and does not announce a new recurring-payment contract.

## Key Details

**DPAN and MPAN:** Apple Pay can generate a device-tied DPAN or a merchant token (MPAN), depending on OS version and integration. The guide says a DPAN **can be unintentionally deactivated** if a user switches devices and adds the same card. It describes MPAN as more reliable for recurring payments and says device switching does not deactivate it. This is not a guarantee about every card or device lifecycle.

**Cryptogram and first authorization:** Each DPAN or MPAN arrives with an expiring one-time-use cryptogram. Stripe says to conduct the CIT and send the token and cryptogram to the authorization network as soon as possible, before expiration. Failure to trigger the CIT in time is often a cause of authorization failure. If the first CIT fails, later MITs using the same Card **will likely also fail** because they are internally linked to it; the guide does not say every later MIT must fail. It supplies no fixed cryptogram lifetime or measured authorization lift.

**API integration sequence:** Save the DPAN or MPAN and cryptogram in a `Card`; initiate a CIT promptly using a SetupIntent's 0 USD validation or a charge, retaining the network transaction; then reuse the saved payment method for future off-session MITs. The later request uses the DPAN or MPAN and original CIT network transaction ID. This is the guide's recommended sequence, not a guarantee that any payment succeeds.

**Free trials and direct setup:** For an Apple Pay free trial, the captured guide says a Stripe Subscription creates a SetupIntent that performs a 0 USD network validation as the CIT before the trial's first charge. A directly created and confirmed SetupIntent can likewise consume the cryptogram and save the Apple Pay PaymentMethod for a Subscription created later. See the raw Use subscriptions for free trials section.

**Legacy Tokens and Charges:** Stripe **discourages** these APIs for recurring Apple Pay and recommends migrating to PaymentIntents and SetupIntents. The guide says the Tokens API does not trigger authorization in time to consume the cryptogram; it also lists Charges API limitations for India, bank-requested authentication, and Strong Customer Authentication. For an existing token flow, it describes creating a PaymentMethod immediately from the token and then a SetupIntent for 0 USD validation; Stripe.js can combine these steps with `stripe.confirmCardSetup` and a token. This is migration advice, not a formal API deprecation date or removal schedule.

**Saved payment boundaries:** The guide supports saved DPAN or MPAN use for `usage=off_session` when the customer is outside the checkout flow, while warning that these payments lack network liability shift and might have lower than average authorization rates. When the customer is in the flow, Apple Pay terms forbid using a saved payment method for `usage=on_session`: the customer must authorize that transaction and generate a fresh cryptogram. The guide also says incremental authorization is supported only when increasing an authorized amount before capture. See the raw Set up off-session payments section.

## Raw Sources

- [[raw/stripe-apple-pay-recurring-2025|May 7, 2026 recurring Apple Pay guide]] — factual source for the behavior and qualifications above.

## Related raw API references

- [[raw/stripe-apple-pay-apple-pay-recurring-2026-11-07|November 7, 2026 same-URL capture]] — navigation and presentation variant; its diff changes numbering and whitespace, without a new substantive recurring-payment rule.
