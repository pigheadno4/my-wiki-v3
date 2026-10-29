---
title: "Bancontact Mobile Android Drop-in v5.0.0 | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-mobile/android-drop-in/2026-09-15.md"
tags: [adyen, bancontact, mobile, android, drop-in]
---

## Overview

This 2026-09-15-captured page is the **Bancontact Mobile Android Drop-in** add-on for an existing Android Drop-in integration. It describes itself as the **v5.0.0** guide (released October 2023) and points earlier versions to a separate guide. Although the heading shortens the name to “Bancontact,” the page description identifies Bancontact **mobile**; do not substitute this for Bancontact card or the earlier-version app/QR instructions (raw lines 5–21, 75–79).

## Key takeaways

- Both **Sessions** and **Advanced** flows require an existing Android Drop-in integration at minimum **v5.0.0** and Bancontact added in Customer Area. The base `/sessions` and `/payments` steps remain in their respective integration guides (raw lines 23–49).
- The page says Bancontact needs **no additional fields** in `/sessions` for Sessions or `/payments` for Advanced, and **no additional Drop-in configuration** in either flow. The Sessions path proceeds to create the checkout session; Advanced launches and shows Drop-in (raw lines 41–67). This short add-on does not itself describe app-switch/QR action handling, a return/details call, result codes or a completed authorization. The absence of extra method-specific settings here should not be read as a complete standalone payment flow.
- The guide says **Bancontact Mobile has no test platform** and historically recommends a EUR 0.01 live penny test. That recommendation is documentation, not evidence that a live test was performed or that this merchant is enabled; it should not override the separate live-operation checks and the main integration flow (raw lines 69–73).

## Detail locators

- Mobile identity, v5.0.0 scope and earlier-version pointer: raw lines 5–21.
- Sessions/Advanced prerequisites and no-extra-fields/configuration: raw lines 23–67.
- No test platform and live penny-test recommendation: raw lines 69–73.
- Main Android Drop-in, webhook and API navigation: raw lines 75–79.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-bancontact|Bancontact card/mobile overview]]
- [[source-adyen-docs-payment-methods-bancontact-bancontact-mobile-android-drop-in-earlier-versions|Android Drop-in earlier versions]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/android-drop-in/2026-09-15|Bancontact Mobile Android Drop-in, fetched 2026-09-15]]
