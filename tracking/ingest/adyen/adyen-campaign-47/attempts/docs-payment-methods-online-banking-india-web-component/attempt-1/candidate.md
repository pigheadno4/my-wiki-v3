---
title: "Online Banking India Web Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-india/web-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-india/web-component/2026-09-15.md"
tags: [adyen, online-banking-india, web, components, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds Online Banking India to an **existing Web Components** integration. It separates Sessions and Advanced server-side flows, covering redirect prerequisites, importing and initializing `OnlineBankingIN`, Advanced `/payments` fields, and test/live setup. It is a method-specific add-on, not a complete base integration or proof of current availability or successful live payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** existing Web Components Sessions flow, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and Online Banking India added in Customer Area are listed as prerequisites. No method-specific parameters are needed when creating `/sessions` (raw lines 23–40).
- **Advanced:** existing Web Components Advanced flow, redirect handling and Customer Area method setup are prerequisites. The requirement row literally says Checkout API “**v or later**,” with the version number missing; do not infer the Advanced minimum from the Sessions row or from the v72 sample (raw lines 84–93, 144–173).
- Both flows say to import `OnlineBankingIN` from `@adyen/adyen-web` and add no method-specific configuration parameters (raw lines 44–58, 97–111). Both initialization snippets spell the constructor `newOnlineBankingIN`, although the import and prose use `OnlineBankingIN`; the snippets are therefore **not copy-ready** as written. Check the actual SDK/base guide for executable syntax (raw lines 62–76, 115–129).
- Advanced `/payments` marks `paymentMethod.issuer` (shopper-selected issuing bank) and `browserInfo` required. The example uses `paymentMethod.type: onlinebanking_IN`, issuer `CBI`, INR and a website returnUrl; these are example values, not proof that this issuer or a merchant account is currently enabled (raw lines 131–173).
- The page points testing to the MyStore demo with India selected and says a live Customer Area request is needed before accepting live Online Banking India payments. It does not itself show actual redirect completion or final authorization handling; follow the linked base integration guides for those steps (raw lines 78–82, 564–568).

## Detail locators

- Sessions requirements and no extra session parameters: raw `## Sessions flow Component` lines 23–40.
- Sessions import, no extra configuration, and initializer caveat: raw lines 42–76.
- Advanced requirements, including incomplete version text: raw `## Advanced flow Component` lines 84–93.
- Advanced import/configuration/initializer: raw lines 95–129; Advanced request fields and v72 examples: raw lines 131–562.
- Testing and live request gates: raw lines 78–82 and 564–568.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-india]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-india/web-component/2026-09-15|Online Banking India Web Component guide, captured 2026-09-15]]
