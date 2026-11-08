---
title: "Stripe: Configure an Invoice Finalization Grace Period"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/usage-based/configure-grace-period"
raw_files:
  - "stripe-billing-subscriptions-usage-based-configure-grace-period-2026-11-07.md"
  - "stripe-usage-based-billing-configure-grace-period-2025.md"
tags: [stripe, billing, usage-based, invoicing, grace-period, finalization]
---

## Summary

The May 5 and November 7, 2026 same-URL guides describe a configurable invoice **finalization** grace period. The account default is 1 hour; rules can delay eligible automatically collected invoices from `draft` to finalized by up to 72 hours. The service period should exceed the configured grace period. This timing setting does not establish payment collection, invoice delivery, or successful settlement.

## Which invoices include usage reported during grace

The November guide says subscription-cycle invoices and subscription-schedule phase-transition invoices **that modify metered items** can include usage reported during the grace period for the prior billing period. Other invoices, including threshold invoices, use usage recorded before invoice creation even if a grace period is configured (new raw lines 9, 63–70). The May capture named cycling invoices and threshold invoices but did not identify qualifying phase transitions (old raw line 8).

> [!warning] Contradiction
> The prior source summarized only cycling versus threshold invoices and could imply all cycling invoices include grace-period usage. November adds qualifying phase-transition invoices and a material exception: after a mid-cycle subscription-item price change, Stripe skips recomputation at finalization, so grace-period usage appears on neither current nor subsequent invoices for classic and flexible subscriptions using billing meters (new raw lines 72–76). Do not treat a longer grace setting as a guarantee of usage allocation.

Stripe may accept usage reported **after** the grace period and show it in meter summaries, yet does not add it to the finalized **or next** invoice (new raw line 11). Meter acceptance and summary visibility are distinct from invoice allocation and payment.

## Default and rule configuration

The Dashboard path is Invoice settings → Invoice finalization grace period. The account default is 1 hour; setting a delay longer than the service period is discouraged, including a 24-hour-or-longer delay for daily service. Rules can target subscription-cycle invoices, invoices with a metered price, or both conditions. Rules have an order and the account default is last. When several rules match a multi-product invoice, Stripe applies the more conservative, longer grace period; the guide gives a 72-hour metered product plus 1-hour simple product example (new raw lines 19–46; old raw lines 16–43).

The **first invoice of a subscription set to `charge_automatically`** finalizes immediately regardless of these rules (new raw line 36; old raw line 33). Neither capture establishes the same exception for first `send_invoice` invoices.

Separately, when Stripe does not receive a successful `invoice.created` response, it can delay finalization of automatically collected invoices for up to 72 hours, except those with a custom scheduled finalization time (new raw line 15). This webhook-response delay is distinct from the configured grace rule and does not make an otherwise ineligible invoice include late usage.

## Meter timestamps and draft invoices

Newly recorded usage ordinarily appears when an eligible invoice is finalized rather than on its draft. The invoice must still be `draft`, and the meter event timestamp must be within that invoice's service period; a threshold invoice does not take usage reported after its creation. A timestamp **after** draft invoice creation routes usage to the next invoice under the ordinary timestamp rule (new raw lines 48–57; old raw lines 45–54). That rule does not override the post-grace non-allocation or mid-cycle price-change exceptions above. Verify reflected usage on the Meters page or via the Meters API.

The captured guide does not specify a recovery path for usage omitted after a mid-cycle price change. Regional finalization rules may differ; this capture supplies no jurisdiction-specific requirement. Neither capture demonstrates a live account setting, accepted event, finalized invoice, or successful payment.

## Related pages

- [[stripe-usage-based-billing]] — usage-based billing concept
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-subscriptions-usage-based-configure-grace-period-2026-11-07|Stripe grace-period guide, November 7 2026]] — updated same-URL capture
- [[raw/stripe-usage-based-billing-configure-grace-period-2025|Stripe grace-period guide, May 5 2026]] — historical capture; filename ends in 2025 but fetched header is May 2026
