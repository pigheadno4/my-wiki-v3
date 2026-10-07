---
title: "Braintree Recurring Billing"
type: concept
category: technology
tags: [braintree, recurring-billing, subscriptions, plans]
---

## Overview

Retrieval route for Braintree-specific recurring-billing documentation. Keep article-level product guidance, SDK implementation guides, and API request or response references as distinct evidence owners; collected pages do not by themselves prove current merchant enablement or resolve the recorded Braintree Marketplace compatibility conflict.

## Article-level orientation

- [[source-braintree-recurring-article-overview]] - article-level route for monthly recurring-billing scope, the plan and Vault prerequisites, and the plan, customer and subscription relationship; distinct from the developer-guide availability and status overview and from Node operations, and not evidence of Marketplace compatibility or current merchant enablement.

## Plans

- [[source-braintree-recurring-article-plans]] - article-level Control Panel route for creating, updating, and deleting plan templates, including trial-risk navigation, the immutable existing-plan billing cycle, new-subscription-only propagation, EU notice conditions, and the former-or-current-subscription deletion restriction; distinct from Node.js guides and Plan API references

## Billing cycles

- [[source-braintree-recurring-article-billing-cycles]] - article-level route for monthly increments, calendar-date anchoring and end-of-month handling, chosen-date processing timing, final-date interpretation, immutable post-creation billing dates, and finite or `Never expires` duration; distinct from Node guides and subscription API references.

## Trial periods

- [[source-braintree-recurring-article-trial-periods]] - article-level route for delaying first billing without consuming cycles, with a payment method required at subscription start and automatic charge timing after the trial. Preserve the lack of default customer notice and the opt-out, negative-option and chargeback warning; exact timing and notice guidance remain in raw.

## Subscription administration article

- [[source-braintree-recurring-article-subscriptions]] - article-level Control Panel route for subscription creation, status-qualified updates, payment-method and price changes, Past Due retries, transaction-based refunds, cancellation and search; preserves the trial, duplicate-overbilling, EU-notice, refund-status and cancellation-date boundaries while leaving Node.js methods, request schemas and response-object detail to their dedicated sources.

> [!warning] Marketplace conflict remains unresolved
> This subscriptions article does not discuss Marketplace compatibility and must not be used to infer support. Existing collected sources conflict between recurring-billing incompatibility statements and Marketplace production guidance; follow [[braintree-marketplace]] and [[source-braintree-recurring-billing-overview]] for the preserved evidence routes.

## Automatic retries and proration

- [[source-braintree-recurring-article-advanced-settings]] - Control Panel route for status-qualified automatic and manual retries, Past Due balance effects, and configured final-failure choices; not every processor decline is retried, and a successful manual retry can reset the subscription balance regardless of its amount.
- The same article routes mid-cycle upgrade charges and downgrade credits, including failed-upgrade settings and the distinction between a subscription balance credit and a payment-method refund. Exact decline codes, timing, setup and calculations remain in its raw locators.

> [!warning] Advanced-settings scope
> These settings do not guarantee collection, current merchant enablement, or Braintree Marketplace compatibility. Use the source and its raw evidence for the exact conditions.

## Customer email notifications

- [[source-braintree-recurring-article-email-notifications]] - article-level route for decline, automatic-retry and configurable Past Due customer emails, including the Past Due qualification and authorized-signer activation; distinct from sale/refund receipts and subscription webhooks.

## Add-ons and discounts

- [[source-braintree-recurring-article-add-ons-discounts]] - article-level route for add-ons that increase and discounts that reduce a subscription price without changing its base plan, plus association, override and deletion boundaries. Exact creation steps remain in the raw locator.

## Mastercard-specific requirements

- [[source-braintree-recurring-article-mastercard-requirements]] - article-level route for the stated Mastercard recurring-billing requirements, including conditional trial reminders, term disclosure, post-enrollment communications, cancellation access, qualified subsequent-authorization guidance, and notices for billing less frequently than every six months. Do not generalize these conditions to every card or trial.

## Related routes

- [[source-braintree-docs-guides-paypal-recurring-payments-javascript-v3]] - JavaScript v3 Braintree website guide for PayPal Billing Without Purchase Checkout, creation-time recurring indicators and plan disclosure, client tokenization and the later merchant-initiated payment handoff; distinct from Braintree's plan-and-subscription engine and not current enablement, direct PayPal API or payment-execution evidence.

- [[recurring-payments]] - generic recurring-payments mechanics and cross-platform context
- [[source-braintree-recurring-billing-plans-node]] - separate Node.js recurring-billing plans guide
- [[source-braintree-plan-create-node]] - separate Node.js Plan Create request reference
- [[source-braintree-plan-update-node]] - separate Node.js Plan Update request reference
- [[source-braintree-subscription-response-node]] - Node.js Subscription response-history route for documented history categories, status and event-source values, and callback/Promise access examples; not a definition of lifecycle transitions or billing consequences.
