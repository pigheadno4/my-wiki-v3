---
title: "Adyen EPS Android integration chooser"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/eps/android"
raw_files:
  - "adyen/docs/payment-methods/eps/android/2026-09-15.md"
tags: [adyen, eps, android, drop-in, components, navigation]
---

## Overview

This 2026-09-15 EPS for Android page is a route selector: it points to the Android Drop-in or `EPSComponent` method guides and to the corresponding base Sessions and Advanced integration guides. It contains no EPS-specific API fields, SDK minimum, bank eligibility or payment-result procedure. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Choose Android Drop-in for the all-in-one UI route, or Android Components for `EPSComponent`; the Components link says that Component handles the redirect to EPS. The linked child guides supply the method setup and qualifications.
- The page says to create the main integration before adding EPS and links all four base combinations: Drop-in or Components with Sessions or Advanced. The links identify navigation routes only; this chooser does not itself state a Checkout API version, redirect callback sequence, issuer list, recurring setup or actual account/payment outcome.

## Detail locators

- Page identity and Android Drop-in/Components choices: pinned raw lines 15–27. Base integration prerequisite and four Sessions/Advanced guides: lines 29–36.

## Related

- [[adyen-online-payments]] — main provider payment integration concept
- [[source-adyen-docs-payment-methods-eps]] — EPS method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/eps/android/2026-09-15|EPS Android chooser, captured 2026-09-15]]
