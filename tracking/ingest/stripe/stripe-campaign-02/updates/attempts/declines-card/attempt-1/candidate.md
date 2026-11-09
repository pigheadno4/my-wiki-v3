---
title: "Stripe Card Declines"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/declines/card"
raw_files:
  - "stripe-declines-card-2026-11-07.md"
  - "stripe-card-declines-2026.md"
tags: [stripe, declines, card-declines, radar, network-codes, retries, on-session, off-session, advice-code]
---

## Summary

The May 9 and November 7, 2026 [[stripe]] guide captures explain card-issuer declines, their network and Stripe advice fields, retry guidance, and on-session versus off-session handling. The guide addresses issuer authorization outcomes; Stripe or Radar blocks before network submission are a separate category in [[stripe-declines]]. A decline or retry suggestion does not imply the next payment will be authorized.

## Common Decline Causes

- **Insufficient funds:** the issuer declines; Stripe suggests considering a buy now, pay later option to reduce this cause.
- **Incorrect card data:** the issuer might decline an incorrect card number, CVC, or expiry; ask the customer to re-enter details.
- **Suspected fraud:** an issuer might decline when its systems flag activity; the customer may need to contact the issuer and confirm identity.

Issuers categorize most card declines as `generic_decline`, so the exact reason can remain unclear. They generally discuss decline specifics only with the cardholder. Stripe suggests Sigma for decline-rate analysis or Card fingerprints rather than charge IDs when excluding repeat attempts.

## Network Codes

For an issuer-declined charge, the November guide's field descriptions call `network_decline_code` and `network_advice_code` **2–4 digit codes from the card network**. Both can be null if Stripe receives no response code from the card network. Their meanings vary by network, so interpret them with the card brand; Mastercard calls network advice codes Merchant Advice Codes (MAC). These network fields are distinct from Stripe's `Charge.outcome.reason`, `Charge.outcome.advice_code`, and `PaymentIntent.last_payment_error.decline_code`. Do not infer a network response for a Stripe/Radar block that was not sent to the network.

> [!warning] Contradiction
> The May 9 capture attributes the two network codes to the issuing bank. November's individual field descriptions attribute them to the card network, although its introductory sentence still says the issuer provides two types of network codes. These dated descriptions do not verify the actual origin of any particular issuer response or supply a universal mapping.

## `advice_code` Values and Retry Behavior

| `advice_code` | Captured meaning | Next step in the guide |
| --- | --- | --- |
| `do_not_try_again` | Advice not to reuse the card for **the same transaction** | Inspect the decline code; customer might need issuer help |
| `try_again_later` | Issuer declined; the card **can be retried**; the guide does not identify a temporary cause | Ask the customer to try again; if later attempts decline, contact issuer |
| `confirm_card_data` | Issuer declined because supplied information is incorrect | Check decline code and have customer validate card details |

November's captured advice table has a two-column header but three-cell rows. The May three-column table and the November row text support the meanings and next steps above; the malformed header is not a changed advice contract. `do_not_try_again` is advice for the same transaction, not a statement that an API enforces a universal card ban.

For **charges that permit retries**, Stripe recommends at most **eight** retries. Card networks also limit attempts, and issuers may interpret excess retries as possible fraud. Stripe Billing users can set subscription retry schedules or use Smart Retries to choose retry timing; neither feature makes every decline retryable or guarantees success.

## Reducing Declines

- For incorrect card details, ask the customer to correct them or use another card or method. Checkout is given as an example of presenting decline feedback and another attempt.
- For suspected fraud, the guide advises collecting CVC and postal code. Other billing data can vary in effect by brand and country; 3D Secure **can** lower declines in supported countries. For `generic_decline` or `do_not_honor`, failed CVC or AVS checks are clues to verify before another charge, not proof of the issuer's exact reason.
- A card-issue country and customer IP-country mismatch **might** be associated with a decline over possible unauthorized use; international travel is an exception. A card issued outside the Stripe-account country might have an increased decline rate.
- FSA/HSA cards can be restricted to eligible merchant categories. Some issuers restrict purchases in other countries; the customer must ask their issuer about those restrictions. The guide also suggests considering local Stripe accounts in larger markets or regions with elevated declines for a global customer base.

## Programmatic and Session Handling

Inspect `PaymentIntent.last_payment_error.decline_code`, attempted Charge `failure_message`, and `payment_intent.payment_failed` webhook events for unsuccessful attempts. Handle API exceptions and other possible failures. For an on-session customer, prompt another attempt or a different method. For an off-session customer, notify them to return and update the method; where Strong Customer Authentication applies, an attempt may require authentication and fail with `authentication_required`. These paths describe failure response, not a completed recovery.

## Related Pages

- [[stripe-declines]] — failure-category concept; distinguishes issuer declines from Stripe/Radar blocks
- [[stripe-3d-secure]] — authentication in supported markets
- [[source-stripe-declines-overview]] — broader decline taxonomy

## Raw Sources

- [[raw/stripe-declines-card-2026-11-07|November 7, 2026 card-declines guide]] — later capture with card-network field attribution and malformed advice-table header.
- [[raw/stripe-card-declines-2026|May 9, 2026 card-declines guide]] — earlier issuing-bank attribution and three-column advice table; captured declined-payment image at `raw/assets/stripe-card-declined-payment-dashboard.png`.
