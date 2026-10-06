---
title: "Braintree Fastlane Reference Types"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/fastlane/reference"
raw_files:
  - "braintree/docs/guides/fastlane/reference-2026-09-16.md"
tags: [braintree, fastlane, javascript, reference, card-fields, accessibility]
---

## Overview

This collected Braintree website reference maps the JavaScript-facing configuration, namespace, result objects and card/payment components presented for Fastlane. It is a retrieval entry for the documented object and action identities; the exact field, enum, style and asset inventories remain in the pinned raw reference.

The page carries no SDK package or version label. This 2026-09-16 website snapshot is not evidence of current availability, merchant or buyer eligibility, successful authentication, token consumption, payment authorization, settlement, or the behavior of the separately versioned Braintree Web adapter or independently hosted Fastlane runtime.

## Key takeaways

- The page presents `braintree.fastlane.create()` with an options surface containing authorization, Braintree client, device-data, shipping-address, card and style inputs. Its returned `Fastlane` namespace groups identity lookup/authentication actions, saved-profile address/card selectors, locale selection, and card, payment and watermark component factories. The displayed interface is a reference shape, not proof that every listed input is required or accepted in every SDK/runtime version.
- `identity.lookupCustomerByEmail(email)` returns a `LookupCustomerResult` shape containing `customerContextId`; `identity.triggerAuthenticationFlow()` returns an authentication-state/profile shape. The documented states are `succeeded`, `failed`, `canceled` and `not_found`. Supplying an email or context ID is not evidence that authentication succeeded or that the returned profile data is complete for a particular buyer.
- Both documented card-entry components can render and return a `PaymentToken`. The payment component also exposes `setShippingAddress`, while the card component is described as using Hosted Card Fields and exposing a subset of the Card Fields interface. A returned token is an integration output, not proof that it was consumed by a server transaction or that any payment was authorized or settled.
- Configuration routes include country/region shipping restrictions, allowed card brands, card-field selection/prefill and style properties. Empty location and brand arrays are shown with all-locations/all-brands defaults, while country/region lists and component initialization snippets are examples rather than eligibility, acceptance or runtime guarantees. Use the raw locators for exact values instead of treating this entry as a comprehensive API property inventory.
- The styling section requires Fastlane integrations to conform to published WCAG A and AA levels and describes automatic fallback to default colors when contrast or distinguishability conditions are not met. The raw table owns the exact style defaults, ranges, allowed font families and color constraints.

## Material boundaries

> [!warning] Website reference, runtime and processing boundary
> Keep these names and shapes scoped to the collected unversioned Braintree website page. Do not transfer them to a particular `braintree-web` release, infer behavior of the independently hosted PayPal/Fastlane runtime, or recast this Braintree path as a direct PayPal Orders API integration. A displayed or returned payment-token value is input to a later integration step, not evidence that a downstream system consumed it or completed a payment.

> [!warning] Examples and field lists
> The country/region, component creation, field prefill and CVV-only snippets illustrate documented shapes. They do not guarantee merchant enablement, buyer eligibility, card-brand acceptance, successful verification or the availability of a field in another SDK or environment.

## Detail locators

- `braintree.fastlane.create()` option shape, location filtering syntax/default and allowed-brand enum: `# Reference Types`, raw lines 16-77.
- Returned `Fastlane` namespace and identity/profile/locale/component actions: `**Fastlane Namespace**`, raw lines 79-100.
- Customer lookup, authentication states, profile, address and payment-token object shapes: `**LookupCustomerResult**` through `**AuthenticatedCustomerResult**`, raw lines 101-166.
- Profile selector result shapes: `**Profile Method Reference Types**`, raw lines 167-181.
- Hosted-Card-Fields relationship, render action, token action and component inputs: `**FastlaneCardComponent**`, raw lines 182-219.
- Payment-component render, token and shipping-address actions: `**FastlanePaymentComponent**`, raw lines 220-251.
- Card-field configuration example and exact optional-field table, including the CVV-only example: `**Card Field Configurations**` and `**Available Fields**`, raw lines 252-283.
- Style object, contrast fallback, WCAG statement and exact UI defaults/ranges: `#### Style Options and Guidelines` through `#### Payment Component UI`, raw lines 286-357.
- Card-brand asset URLs and unread advanced-options navigation: `#### Loading Card Assets`, raw lines 360-376.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-web-sdk]]
- Product boundary: [[paypal-fastlane]]

## Related raw API references

- [[raw/braintree/docs/guides/fastlane/advanced-option-2026-09-16|Braintree Fastlane Advanced Options]] - unread navigation-only destination linked by the reference; not used as behavioral or prerequisite evidence here

## Raw Sources

- [[raw/braintree/docs/guides/fastlane/reference-2026-09-16|Braintree Fastlane Reference Types]] - complete collected snapshot for create configuration, namespace actions, result/object shapes, card and payment components, available fields, styling constraints and asset locators
