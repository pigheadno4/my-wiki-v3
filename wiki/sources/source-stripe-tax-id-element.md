---
title: "Stripe Tax ID Element"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/elements/tax-id-element
raw_files:
  - "stripe-tax-id-element-2025.md"
tags: [stripe, elements, tax-id, vat, invoicing, address-element, checkout-sessions, payment-intents, beta]
---

## Summary

The Tax ID Element is an embeddable UI component for collecting customer business tax IDs for tax calculation and invoice display. The April 21, 2026 capture documents both Checkout Sessions and Payment Intents paths, lists **95 country and region codes** across six sections, and shows separate beta flags in its two examples. The November 7, 2026 same-URL capture is only a variant index. It does not verify current country coverage, beta status, flag requirements, visibility rules, or CustomerSession behavior.

> [!warning] Contradiction: the earlier source summary said "100+ countries" and "currently in beta"; the paired April guide enumerates 95 codes and shows beta flags only in dated examples. The November index does not resolve current coverage or beta status.

## April 21 Guide: Visibility and Tax ID Collection

The captured guide describes `auto` visibility as the default: the element appears where tax ID collection is common. It uses country from an Address Element in shipping or billing mode, and falls back to customer IP address when that element is absent. The guide says `always` displays the element even where collection is uncommon. With Address Element, tax ID type and format adapt to the customer's address. These are descriptions from the April guide; the November variant bodies were not captured.

The guide's demo also lets a user change theme and desktop or mobile parent width, choose a customer location, and enable optional business-name collection. It says the collected business name appears as the customer name on invoices. The element collects information; this capture does not demonstrate a completed tax calculation or VAT refund.

## April 21 Guide: API Path Examples

The Checkout Sessions embedded-components example initializes Stripe with `betas: ["custom_checkout_tax_id_1"]`, initializes the Checkout Elements SDK with a client secret, creates a Tax ID Element with `visibility: "always"`, and mounts it. The Payment Intents Elements example instead uses `betas: ["elements_tax_id_1"]`, creates an Elements instance with a PaymentIntent client secret, then creates and mounts `taxId`. The beta flags are **shown in those April examples**; this same-URL November index does not establish whether they remain required.

For the Payment Intents path, the April guide says a `CustomerSession` must be created **to save and redisplay the tax ID**. This is a conditional save/redisplay statement for that path, not a prerequisite to every Tax ID Element use; its current behavior is unverified here. Full examples and their client/server placement are at old raw:152-236.

## Listed Regions in the April 21 Capture

The old guide lists 95 country and region codes: North America 6, South America 5, Europe 44, Asia 19, Oceania 2, and Africa 19. This is a count of the **April list**, not a guarantee of today's coverage. Consult the raw list for exact codes and country-specific tax ID formats.

| Region | Codes listed in April | Examples |
| --- | ---: | --- |
| North America | 6 | AW, BB, BS, CA, CR, MX |
| South America | 5 | CL, EC, PE, SR, UY |
| Europe | 44 | AT, DE, FR, GB, CH, NO, RU, UA |
| Asia | 19 | AE, IN, KR, SA, SG, TH, TR, TW |
| Oceania | 2 | AU, NZ |
| Africa | 19 | AO, EG, KE, MA, NG, ZA, ZM, ZW |

## Related Pages

- [[stripe-tax-id-element]] — concept route
- [[stripe-address-element]] — related address input
- [[stripe-tax]] — tax concepts
- [[stripe-elements]] — Elements framework
- [[stripe]] — provider

## Related raw API references

- [[stripe-elements-tax-id-element-2026-11-07]] — November 7 same-URL variant index linking Checkout Sessions embedded-components and Payment Intents elements; linked bodies are not part of this capture

## Raw Sources

- [[stripe-tax-id-element-2025]] — April 21 captured guide with region list and both API-path examples
