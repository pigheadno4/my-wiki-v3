---
title: "Braintree Subscription Update (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/subscription/update/node"
raw_files:
  - "braintree/docs/reference/request/subscription/update/node-2026-09-16.md"
tags: [braintree, node-js, subscriptions, recurring-billing, payment-methods, 3d-secure]
---

## Overview

This Braintree Node.js request reference documents updating an existing subscription through `gateway.subscription.update()` in callback and Promise forms. It is an update-specific retrieval entry for subscription attributes, add-on and discount changes, and a qualified 3D Secure payment-method update; it does not establish subscription-creation prerequisites or behavior.

## Key takeaways

- The opening examples invoke `gateway.subscription.update()` with a subscription identifier and illustrative update fields; the exact field list remains at the raw locator below. If the subscription cannot be found, the page routes the reader to Braintree's `notFoundError`.
- An update can add new add-ons or discounts, update existing ones associated with the subscription, or remove existing ones. The page warns that an add-on or discount can be added to a subscription only once; to apply one several times, pass `quantity` when creating or updating that add-on or discount.
- If a merchant uses 3D Secure and needs to apply 3DS to the next transaction of an existing subscription, the page says the subscription must be updated with a 3DS-enriched nonce. This condition is not a general requirement for every subscription update.
- Multiple add-on or discount changes can be made in one update. Added items inherit details from the referenced add-on or discount, with the page's exact override categories retained at the raw locator rather than reproduced here.
- Passing the displayed `replaceAllAddOnsAndDiscounts` option is the page's route for removing all existing add-ons and discounts from the subscription. This is a destructive scope qualification, not a general description of other subscription fields or billing effects.

## Detail locators

- Update invocation, illustrative subscription fields, and callback form: `# Subscription: Update > ### Callback`, lines 13-26.
- Promise form and missing-subscription error route: `# Subscription: Update > ### Promise`, lines 28-39.
- Add-on and discount one-addition qualification plus add/update/remove scope: `## Examples > ### Add-ons and discounts`, lines 43-52.
- Callback and Promise request shapes for add-on and discount changes: `## Examples > ### Add-ons and discounts`, lines 55-127.
- Conditional 3DS-enriched nonce guidance and displayed update calls: `## Examples > ### Update with 3D Secure enriched payment method nonce`, lines 129-148.
- Multiple simultaneous add-on or discount changes: `## Examples > ### Multiple updates`, lines 150-215.
- Inheritance behavior and exact override categories: `## Examples > ### Override details`, lines 217-273.
- Option for removing every existing add-on and discount: `## Examples > ### Remove add-ons and discounts`, lines 275-296.

## Evidence limitations

> [!warning] Update behavior only
> This page does not establish subscription-creation prerequisites, when an update affects billing, whether an update prorates or immediately charges, or the broader eligibility of any payment method. Use the linked navigation references and dedicated authorities for behavior not stated by this update page.

## Related

- Company: [[braintree]]
- Concepts: [[braintree-server-sdk]], [[recurring-payments]]

## Raw Sources

- [[raw/braintree/docs/reference/request/subscription/update/node-2026-09-16|Braintree Node.js subscription-update request reference]] - complete collected page covering the update invocation, add-on and discount changes, conditional 3DS-enriched nonce guidance, and remove-all option

## Related raw API references

- [[raw/braintree/docs/reference/response/subscription/node-2026-09-16|Subscription response object (Node.js)]] - unread navigation-only response reference linked by the update page
- [[raw/braintree/docs/reference/general/exceptions/node-2026-09-16|General exceptions (Node.js)]] - unread navigation-only exception reference containing the linked not-found target
- [[raw/braintree/docs/guides/3d-secure/overview-2026-09-16|3D Secure overview]] - unread navigation-only guide linked by the update page
- [[raw/braintree/docs/guides/recurring-billing/manage/node-2026-09-16|Managing subscriptions (Node.js)]] - unread navigation-only guide corresponding to the page's See Also route
