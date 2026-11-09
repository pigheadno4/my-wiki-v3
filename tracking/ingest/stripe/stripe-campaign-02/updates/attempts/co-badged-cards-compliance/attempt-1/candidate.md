---
title: "Stripe: Co-badged Cards Compliance"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/co-badged-cards-compliance"
raw_files:
  - "stripe-co-badged-cards-compliance-2025.md"
tags: [stripe, co-badged, cartes-bancaires, girocard, eu-regulation, elements, terminal]
---

## Overview

The 2026-05-01 Stripe guide explains cardholder network choice for co-badged cards, including regional applicability, Stripe integration variants, Connect merchant-of-record conditions, and test examples. The 2026-11-07 capture of the same URL is an index to ten variant pages; it contains no variant-specific instructions. Its shorter default render does not establish repeal, deprecation, current SDK behavior, account eligibility, or compliance of any merchant's implementation. See [[stripe]] and [[co-badged-cards]].

## Key takeaways

- **Choice and eligibility, as captured 2026-05-01:** The guide says to display available networks clearly and equally, honor the cardholder's selected network for payment confirmation or saved credentials, and allow changes when saved payment details are updated. Its table covers online EEA businesses able to process Cartes Bancaires when the card is co-badged and currency is EUR; in-person France for eligible Cartes Bancaires; and in-person Germany for eligible Girocard. Stripe directs account-specific applicability to sign-in. These are the guide's dated descriptions, not a current compliance determination.
- **Hosted interfaces, as captured 2026-05-01:** Stripe says Checkout, Payment Links, Elements and Terminal show a selector when the applicability criteria are met and the interfaces are configured as described. A sandbox may show online Cartes Bancaires choice even when the merchant has not enabled it, so the sandbox display does not prove live eligibility. Other integrations remain the implementer's responsibility.
- **Connect condition:** The May guide's extra `onBehalfOf` instruction applies to Connect platforms using `on_behalf_of` with separate charges and transfers or destination charges, with the merchant of record determining applicability; the merchant of record can be the platform or connected account. The setting's location differs by variant: Elements group for Web Payment Element created without an Intent, Web Card Element and Express Checkout Element; `paymentRequest` for Payment Request Button; `IntentConfiguration` for Payment Sheet and Embedded Mobile Payment Element; and the Card Element variant for Mobile Card Element. It is not a blanket requirement for every Connect transaction.
- **Web Card Element:** The Combined variant needs `hideIcon: false` or `undefined`; the Split variant needs `showIcon: true`. The Card Element cannot detect transaction currency, so its dropdown may appear outside EUR and another network may process if the selected one cannot. Card Element choice is incompatible with Sources: the dropdown may appear, but Stripe says it will not honor the selected network. If using `preferredNetwork`, enable icons and do not override the network at confirmation. The former custom `networkschange` choice path is described as deprecated in the May guide in favor of the Card Element dropdown.
- **Mobile variants, as captured 2026-05-01:** Payment Sheet, Embedded Payment Element, Customer Sheet and Card Element support selection under their respective configurations. The guide gives iOS 23.22.1+ and Android 20.37.4+ as the baseline for these variants. For a Mobile Card Element Connect flow using `on_behalf_of`, it places `onBehalfOf` on the Card Element variant and gives higher minimums of iOS 23.27.1+ and Android 20.42.0+; the Payment Sheet and Embedded Payment Element paths use `IntentConfiguration`. `preferredNetworks` supplies defaults when the cardholder does not choose.
- **Terminal:** The May guide names WisePad 3 and Stripe Reader S700/S710 as supporting selection when applicable. Tap to Pay on iPhone instead requires the integration to collect the network choice and pass `requested_priority` before the tap.
- **Verification examples:** The May guide shows co-badged test card numbers, tokens, PaymentMethod IDs, and a `charge.payment_method_details.card.network` example for identifying the processing network. These are test and example data, not proof of live merchant enablement, a completed payment, or successful network routing.

## Detail locators

- Regulation description, three choice requirements and regional table: May raw lines 8–26. Hosted UI and sandbox qualifications: lines 61–69.
- Checkout/Payment Links and Web Payment Element: May raw lines 71–123. Web Card Element icon modes, currency, Sources, default network and deprecated event path: lines 125–176.
- Payment Request Button and Express Checkout Element, including conditional Connect placement: May raw lines 178–230.
- Payment Sheet, Embedded Payment Element and Customer Sheet: May raw lines 232–378. Mobile Card Element and its higher Connect SDK minimums: lines 380–406.
- Terminal and processing-network lookup: May raw lines 415–448. Test cards, tokens, PaymentMethods and simulated reader: lines 450–475.

## Related

- [[co-badged-cards]] — source-qualified network choice and provider comparison

## Raw Sources

- [[raw/stripe-co-badged-cards-compliance-2025|Stripe full co-badged guide, captured 2026-05-01]] — historical factual instructions and examples.

## Related raw API references

- [[raw/stripe-co-badged-cards-compliance-2026-11-07|Stripe co-badged variant index, captured 2026-11-07]] — navigation only; the linked variant pages were not part of this four-file evidence set.
- [Checkout and Payment Links](https://docs.stripe.com/co-badged-cards-compliance.md?type=checkout-payment-links)
- Web: [Payment Element](https://docs.stripe.com/co-badged-cards-compliance.md?type=web-elements&ui=payment-element), [Express Checkout Element](https://docs.stripe.com/co-badged-cards-compliance.md?type=web-elements&ui=express-checkout-element), [Card Element](https://docs.stripe.com/co-badged-cards-compliance.md?type=web-elements&ui=card-element), [Payment Request Button Element](https://docs.stripe.com/co-badged-cards-compliance.md?type=web-elements&ui=payment-request-button-element)
- Mobile: [Payment Sheet](https://docs.stripe.com/co-badged-cards-compliance.md?type=mobile-elements&mobile-ui=payment-sheet), [Payment Element](https://docs.stripe.com/co-badged-cards-compliance.md?type=mobile-elements&mobile-ui=payment-element), [Customer Sheet](https://docs.stripe.com/co-badged-cards-compliance.md?type=mobile-elements&mobile-ui=customer-sheet), [Card Element](https://docs.stripe.com/co-badged-cards-compliance.md?type=mobile-elements&mobile-ui=card-element)
- [Terminal](https://docs.stripe.com/co-badged-cards-compliance.md?type=terminal)
