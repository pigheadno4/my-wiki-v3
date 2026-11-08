---
title: "Stripe — Design a Subscriptions Integration"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/design-an-integration"
raw_files:
  - "stripe-billing-subscriptions-design-an-integration-2026-11-07.md"
  - "stripe-subscriptions-design-integration-2026.md"
tags: [stripe, subscriptions, billing, pricing-models, checkout, usage-based, freemium, trial]
---

## Summary

Stripe's subscriptions design guide helps choose a pricing model, checkout interface, and payment timing, then routes six example combinations to deeper implementation guides. The four pricing categories, seven checkout interface categories, three timing models, and six use-case routes were already present in the 2026-05-12 capture. The 2026-11-07 guide adds a conditional navigation statement: use Metronome to configure **more complex** pricing models based on usage. That wording does not require Metronome for every usage-based subscription or establish a new payment capability.

**May 2026 ingest note:** Nine CDN images referenced by the earlier capture (pricing model screenshots and checkout interface previews) were not downloaded due to network restrictions. This is an evidence-asset note, not a Stripe product restriction.

## 4 Pricing Models

| Model | Guide's categories and subtypes |
| --- | --- |
| **Flat rate** | Fixed price per service tier, such as monthly or yearly. |
| **Per-seat** | Price per user or license. |
| **Tiered** | Volume-based pricing applies one tier's rate to the final quantity; graduated pricing sums charges across the tiers used. |
| **Usage-based** | Fixed fee plus overage; pay as you go by unit, package, volume or graduated rate; prepaid credit burndown. |

The May capture describes billing credits and different illustrated tiers; the November capture uses worked seat/token arithmetic and names Metronome for more complex usage pricing. These examples are illustrative prices and product routes, not universal billing amounts or model prerequisites. See the dated raw pricing sections for calculations.

## 7 Checkout Interfaces

| Interface | Guide's description |
| --- | --- |
| Stripe-hosted page | A prebuilt Stripe-hosted payment page; guide lists preset fonts/radii, colors and logo options. |
| Embedded payment page | A prebuilt Stripe-hosted page embedded in the site, with the guide's stated customization options. |
| Custom payment form | Stripe Elements integrated with the web app; the Payment Element layout can be customized to fit the checkout flow, and the Appearance API adjusts the form's look and feel. |
| Pricing table | An embeddable table displaying pricing options, followed by a Stripe-hosted payment page. |
| One-click payment buttons | Express Checkout Element; the guide names Link, Apple Pay, Google Pay, PayPal, Klarna and Amazon Pay, without establishing availability for a particular merchant. |
| Payment link | A shareable URL to a Stripe-hosted payment page. The November guide says links can be created and shared without code from the Dashboard. Both captures exclude payment links for usage-based billing. |
| Mobile app | The guide describes a prebuilt sheet or customizable drop-in component and links to iOS, Android and React Native subscription instructions; it does not verify every native SDK's current UI or eligibility. |

## 3 Billing Models

| Model | Typical flow in the guide |
| --- | --- |
| **Pay up front** | Collect payment information and require payment before product or service access. |
| **Free trial** | Collect a payment method without charging at enrollment, grant limited trial access, and begin a new billing period with an invoice after the trial. |
| **Freemium** | Begin access without requesting payment information, collect it before the trial ends, and invoice when the new billing period starts. |

These are design examples, not evidence that an actual payment, invoice, subscription or provisioned access occurred.

## Integration routes and evidence limits

The six-row matrix links flat-rate trials, usage-based checkout, pricing tables, flat-rate payment links, mobile flat-rate checkout, and one-click buttons to separate instructions. In November, two free-trial links gained `ui=full-page` query parameters; this selects a documentation variant and does not itself change the subscription contract. The guide does not establish account eligibility, selected UI/platform variant behavior, payment-method availability, live rollout, or payment outcomes.

## Related Pages

- [[stripe-subscriptions]] — concept page and subscription design decisions
- [[source-stripe-subscriptions-overview]] — lifecycle and status guide
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-subscriptions-design-an-integration-2026-11-07|Subscriptions design guide, captured 2026-11-07]]
- [[raw/stripe-subscriptions-design-integration-2026|Subscriptions design guide, captured 2026-05-12]]
