---
title: "Stripe Declines Overview"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/declines"
raw_files:
  - "stripe-declines-2026-11-07.md"
  - "stripe-declines-2026.md"
tags: [stripe, declines, radar, fraud, issuer-declines, adaptive-acceptance, payment-failure]
---

## Overview

Stripe's May 9 and November 7, 2026 guides distinguish issuer or payment-provider declines, Stripe-blocked payments, and invalid API calls. For a failure, the guide directs readers to the Dashboard or the `Charge.outcome` attribute to inspect the type and cause. Its issuer, block, incorrect-CVC error, and `invalid` outcome snippets are separate examples, not a complete input-to-outcome mapping or evidence of a particular executed payment. See [[stripe-declines]].

## Three failure categories and diagnostic examples

| Guide category | Dated example | Decision/diagnostic boundary |
| --- | --- | --- |
| Issuer decline | `outcome.type: issuer_declined`, `network_status: declined_by_network`, `reason: expired_card` | Issuer or payment provider decides whether to authorize; Stripe reports the information received, including network decline codes when provided |
| Blocked payment | `outcome.type: blocked`, `network_status: not_sent_to_network`; examples show `highest_risk_level` or `low_probability_of_authorization` | Stripe Radar rule/risk block or, for users with IC+ pricing, Adaptive Acceptance's low-authorization-probability/network-cost block |
| Invalid API call | A separate sample `outcome.type: invalid`, `network_status: not_sent_to_network` | The guide says invalid calls typically do not produce a Dashboard payment, though some may; it does not map every malformed request or incorrect CVC to this outcome |

The guide's wrong-CVC PaymentIntent illustration uses `amount=2000`, `currency=usd`, `payment_method=pm_card_chargeDeclinedIncorrectCvc`, and `confirm=true`, then displays a possible `incorrect_cvc` `card_error` response. The May sample is Node; the November sample is equivalent curl. The later `outcome.type: invalid` snippet is separate; neither capture shows that the same incorrect-CVC request yielded that Charge outcome. The November error `doc_url` points to a `docs.stripe.com` anchor; this presentation change does not prove a runtime schema change.

## Issuer declines

A card issuer or other payment provider may evaluate spending habits, balance and card data such as expiration, address and CVC. Stripe surfaces received decline information through Stripe decline codes, and specific issuer explanations may arrive as network decline codes. The guide says non-card payment-method declines are handled similarly and includes an issuer-declined example with network code `54`, advice code `03`, `reason: expired_card`, and `advice_code: confirm_card_data`. The example is not a guarantee that a given decline has those codes.

## Stripe-blocked payments

Stripe says a blocked payment does not obtain card-issuer authorization through Stripe and has not been charged or withdrawn by Stripe. **For some card types**, a customer nevertheless might see an issuer authorization for the amount on their statement, which the issuer typically removes within a few days. These statements do not establish whether the issuer temporarily reserves the customer's available balance. Do not equate a statement authorization with a Stripe charge or settled payment.

Radar can block a high-risk payment or one violating custom rules. The guide's block example uses `reason: highest_risk_level`, `risk_level: highest`, and `type: blocked`. For users with **IC+ pricing**, Adaptive Acceptance can block some low-probability payments to avoid network costs or retry penalties; its example uses `reason: low_probability_of_authorization` and `risk_level: normal`. Both examples have `network_status: not_sent_to_network`.

If a configured Radar rule blocks a legitimate payment, **Add to allow list** in the Dashboard can stop other matching rules from blocking future attempts. It does not retry the already blocked payment. The guide says to contact Stripe if the button is unavailable.

## Detail locators

- [[raw/stripe-declines-2026-11-07|November 7, 2026 guide]]: failure categories and `Charge.outcome` lines 9–21; issuer handling lines 23–31; blocked-payment authorization caveat and allow list lines 33–45; Radar/Adaptive Acceptance examples and IC+ scope lines 47–77; incorrect-CVC curl/error, issuer outcome, and separate invalid outcome lines 79–134.
- [[raw/stripe-declines-2026|May 9, 2026 guide]]: categories and diagnostic route lines 8–26; block caveat and allow list lines 28–40; examples and IC+ scope lines 42–72; incorrect-CVC Node/error and distinct outcomes lines 74–133.

## Related

- [[stripe]]; [[stripe-declines]]; [[stripe-authorization-boost]]; [[stripe-3d-secure]]

## Raw Sources

- [[raw/stripe-declines-2026-11-07|November 7, 2026 decline guide]]
- [[raw/stripe-declines-2026|May 9, 2026 decline guide]]
