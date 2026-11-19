---
title: "Customize Payment Methods in the Payment Element"
type: source
date_ingested: 2026-04-21
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/customize-payment-methods"
raw_files:
  - "stripe-payments-customize-payment-methods-2026-11-07.md"
  - "stripe-payment-element-customize-payment-methods-2025.md"
tags: [stripe, payment-element, payment-methods, dynamic-payment-methods, card-filtering, confirmation-token, accordion]
---

## Summary

Stripe's November 7, 2026 Payment Element guide covers **four** display controls: enabled methods, ordering, card brand/funding filters, and accordion count. The April 21, 2026 capture covered the other three but had no filtering section. Payment Element display and browser validation do not establish server policy enforcement, account-specific eligibility, or a successful payment. See [[stripe]], [[stripe-elements]], and [[stripe-payment-intents]].

## Enabled methods and order

The Payment Element displays enabled methods, hides those ineligible for the current transaction, and dynamically orders eligible methods for conversion. Stripe says Dashboard preferences drive dynamic payment methods by default in the **latest API version**, without giving an exact version in this guide. The April capture described a manual PaymentIntent allowed list using `payment_method_types`; the November guide links PaymentIntent **create** `allowed_payment_method_types` instead. Treat these as dated, route-specific guide wordings, not interchangeable parameter names or an automatic rename across SDKs. The separately documented `stripe@23.0.0` server request removal has its own exact version and operation scope; see [[stripe-payment-intents]]. In either guide, an unsupported currency or recurring method is hidden even if configured.

`paymentMethodOrder` on `elements.create('payment', ...)` places the specified **available** methods first. Unavailable specified types are ignored; remaining available methods retain dynamic ordering. Apple Pay and Google Pay can be named explicitly alongside payment method types. The guide says Finland and Sweden require debit methods before credit methods at checkout; this is the captured guide's regulatory statement, not independent legal advice or evidence a particular ordering complies. The earlier source's "ML-based" mechanism was not stated by either captured guide; the documented behavior is dynamic ordering for conversion.

## Card brand and funding filters

The November guide adds `disallowedCardBrands` and `disallowedCardFundingTypes` when initializing the **Elements group**, not as a PaymentIntent method list. The restrictions apply to card entry in the Payment Element, Apple Pay, and Google Pay, subject to wallet limits below. Brand values are `visa`, `mastercard`, `american_express`, and `discover_global_network` (Discover, Diners, JCB, UnionPay, Elo). Funding values are `credit`, `debit`, and `prepaid`. The guide says not to block every supported brand or every supported funding type. Its JavaScript and React snippets illustrate Elements-group initialization; they do not show a server policy being enforced.

The Payment Element checks blocked cards in the browser and shows an error during entry. **That client check does not enforce a server-side payment policy.** For such a policy, the guide offers Radar rules or server-side PaymentIntent confirmation with a ConfirmationToken: create the token in Stripe.js from the Payment Element, send its ID to the server, retrieve it, inspect `payment_method_preview.card.brand` and `.funding`, and confirm only if the server policy allows. Funding may be `unknown` or unavailable, so a strict policy needs an explicit choice for an indeterminate value. A token, browser error, Radar option, or example confirmation path is not evidence that a policy ran or a payment succeeded.

The guide says **Apple Pay cannot filter prepaid cards** and **Google Pay cannot filter debit cards**. Separately, for **Elements with Checkout Sessions**, Checkout enforces blocked funding types at payment confirmation. Keep that Checkout Sessions confirmation clause specific to that path and to funding types; it is not a blanket claim about all PaymentIntent integrations or all brand filters.

## Accordion count

In accordion layout, up to **five** methods appear by default and the rest sit behind **More**. `layout.visibleAccordionItemsCount` changes the visible count; `0` removes More and renders all available methods. This display count does not override transaction eligibility. The April and November captures agree on this behavior and on the ordering and auto-hide rules.

## Related pages

- [[source-stripe-payment-element]] — Payment Element reference
- [[source-stripe-finalize-payments-server]] — separate server-confirmation path

## Raw Sources

- [[raw/stripe-payments-customize-payment-methods-2026-11-07|Payment Element method customization — November 7, 2026 full capture]]
- [[raw/stripe-payment-element-customize-payment-methods-2025|Payment Element method customization — April 21, 2026 capture; filename retains 2025 suffix]]
