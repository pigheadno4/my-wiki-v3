---
title: "Adyen MB WAY for Android integration router"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mb-way/android"
raw_files:
  - "adyen/docs/payment-methods/mb-way/android/2026-09-15.md"
tags: [adyen, mb-way, android, integration-router, online-payments]
---

## Overview

This 2026-09-15-captured Adyen page is a short router for adding MB WAY to an Android app. It points to separate Android Drop-in and Components child guides and to the main Sessions and Advanced integration guides. It does not itself give request fields, SDK versions, return handling, eligibility, or payment outcomes. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Integration choices:** The page offers an Android Drop-in guide, described as an all-in-one UI solution, and an Android Components guide, described as using `MBWayComponent` to handle the redirect to MB WAY. Those are navigation descriptions; the linked child guides must be read for implementation behavior. [Raw: lines 19–27]
- **Main integration prerequisite:** It instructs readers to create the main integration before adding MB WAY, then links the Android Drop-in and Components guides for both Sessions and Advanced server-side flows. No particular flow is selected by this router. [Raw: lines 29–36]
- **Scope limit:** The page provides no method-specific payload, version minimum, authorization/capture result, or test/live instructions. Do not infer any of these from its directory title or child-link labels; route such questions to fully read child guides or the separately approved [[source-adyen-docs-payment-methods-mb-way]] overview, with attribution. [Raw: lines 15–36]

## Detail locators

- Page purpose and two Android integration choices: pinned raw lines 15–27.
- Main-integration instruction and four Sessions/Advanced platform links: pinned raw lines 29–36.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-mb-way]] — approved method overview for distinct Web and mobile shopper journeys; those facts are not established by this Android router.

## Raw Sources

- [[raw/adyen/docs/payment-methods/mb-way/android/2026-09-15|MB WAY Android router, captured 2026-09-15]]
