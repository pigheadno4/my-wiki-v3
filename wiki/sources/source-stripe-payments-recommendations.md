---
title: "Stripe Docs — Recommendations"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/analytics/recommendations"
raw_files:
  - "stripe-payments-analytics-recommendations-2026-11-07.md"
  - "stripe-payments-recommendations-2025.md"
tags: [stripe, recommendations, authorization-rates, ntid, avs, radar, 3d-secure, payment-optimization]
---

## Overview

The May 8 and November 7, 2026 full captures describe **Payments analytics recommendations** as suggestions shown on the Stripe Dashboard **Acceptance** page to help a business consider revenue or fraud-protection changes. Depending on account availability, there can be **none or up to three** at a time. Stripe bases them on settings, integration, thresholds and other account relevance, updates them daily, and allows a user to dismiss one with **X** or submit **Feedback** in Payments analytics. Displaying, dismissing or sending feedback on a suggestion does not execute an optimization or prove any payment outcome (new raw lines 9-21; old raw lines 8-20).

Stripe says the business must decide whether to act. Recommendations are **not professional advice**; projected effects are **not guaranteed**, and action may raise costs or fraud risk or involve additional legal terms. Stripe lacks all relevant business information to guarantee an outcome.

## Estimated impact

Each recommendation has an estimated impact, which can be **a revenue/payment-volume increase or a fraud-model improvement**. Revenue increases are displayed in the account's settlement currency. An annual revenue estimate, where applicable, uses the most recent month's **all payment volume** or only **relevant payment volume**, multiplied by an average increase observed among other businesses that took the action and then by 12. Stripe excludes inapplicable payments from the relevant-volume base, regularly tests the average increase, and assumes payment volume stays constant while annualizing. The guide's card account updater example excludes cards without an available update. This calculation is not an annual revenue estimate for every recommendation, and none of these estimates is observed merchant gain (new raw lines 23-33; old raw lines 22-34).

## Five recommendation topics

| Topic | Captured recommendation and boundary |
| --- | --- |
| Network transaction IDs (NTIDs) | For an off-session **merchant-initiated transaction**, provide the NTID of a prior **on-session transaction or validation from the same customer** when Stripe lacks that ID. The page identifies transactions whose underlying card Stripe did not previously authorize and card-number payments without a Stripe `Customer` object. If all payments pass through Stripe, it handles this automatically; with other processors it may lack the NTID unless supplied when creating the PaymentIntent. The guide says this can increase authorization and reduce issuer 3DS requests, not guarantee either outcome (new raw lines 35-44; old raw lines 36-45). |
| Visa credit postal codes | Share postal codes for Visa credit cards; AVS compares the address with issuer records and can support more favorable US interchange rates and cost savings (new raw lines 46-48; old raw lines 47-49). |
| AVS/CVC Radar rules | Stripe recommends disabling the broad `Block if CVC verification fails` and `Block if postal code verification fails` rules to avoid blocking legitimate payments. It describes risk-score variants for blocking failed checks unless Stripe assesses low risk; its highest-risk machine-learning block remains regardless of configured rules. Rule changes are made on the Dashboard **Rules** tab, and involve business-specific fraud tradeoffs (new raw lines 50-66; old raw lines 51-67). |
| Optional 3D Secure (3DS) requests | Stripe recommends reducing requests on low-risk transactions **outside regions with authentication requirements** where extra friction may hurt success. API-requested 3DS is changed through the API; a Radar-requested rule is disabled in Dashboard. This does **not** affect payments that require 3DS by regulation, including cited European SCA and Japanese card-security examples. Radar Authentication control is a separate option for Stripe to request 3DS when it might reduce fraud (new raw lines 68-79; old raw lines 69-80). |
| High 3DS abandonment | A large number of abandoned requests may indicate a 3DS integration issue; the page links to a separate 3DS payment-flow guide. It does not establish the cause for an individual merchant (new raw lines 81-83; old raw lines 82-84). |

## Capture comparison and limits

The November capture retains the May recommendations and qualifications. The recorded diff changes heading whitespace and the formatting of the impact table; it does not establish a new recommendation policy, API, eligibility threshold, automatic account change or realized improvement. The page links to Acceptance, Authentication and Disputes analytics and to implementation guides, but those links alone do not supply their client/server procedures. A forecast, recommendation display or changed Radar/3DS setting does not prove authorization, fraud-model result, settlement or net revenue improvement.

## Related

- [[stripe]] — company context.
- [[stripe-authorization-boost]] — related payment optimization concept and reciprocal recommendations route.
- [[source-stripe-payments-optimization]] — Authorization Boost feature overview, separate from these recommendations.

## Raw Sources

- [[raw/stripe-payments-analytics-recommendations-2026-11-07|November 7, 2026 recommendations guide]] — full 89-line capture.
- [[raw/stripe-payments-recommendations-2025|May 8, 2026 recommendations guide]] — prior full 90-line capture.
