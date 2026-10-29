---
title: "Adyen PayPo iOS Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo/ios-component"
raw_files:
  - "adyen/docs/payment-methods/paypo/ios-component/2026-09-15.md"
tags: [adyen, paypo, ios, component, redirect, capture]
---

## Overview

This 2026-09-15-captured Adyen guide adds PayPo to an existing iOS Components integration, separately for Sessions and Advanced flows. Its examples use PL/PLN and the Advanced method type `paypo`. It covers request additions, redirect action, a short preauthorization offer window, full capture, and test/live setup. It does not establish current merchant eligibility, executed payment success or live enablement. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions flow:** Requires an existing iOS Sessions Components integration, Checkout API v68 or later, and PayPo in Customer Area. The `/sessions` table marks shopperName with first and last names and shopperEmail required; billing and delivery addresses are listed without required marks. The sample uses PL/PLN (pinned raw lines 25–73).
- **Advanced flow:** Requires an existing iOS Advanced Components integration, handling the additional `action.type=redirect`, and PayPo in Customer Area. Its `/payments` table marks `paymentMethod.type=paypo`, shopperName and shopperEmail required; billing and delivery addresses are unmarked. The sample response is `RedirectShopper` with a GET redirect action, which is a next shopper step rather than final authorization (lines 468–523, 894–908).
- Both sections say PayPo needs no added configuration parameters. The initialization prose and Swift snippets refer to a `None` class, and the Advanced requirement's linked URL selects Drop-in despite the Components wording; see warning below (lines 423–452, 476–507).
- Before authorization, the payment offer/link remains available for up to **72 hours**. When the shopper accepts, the status becomes Authorised and the shopper's **30-day** term to pay PayPo begins at authorization, not at capture. The merchant must capture after authorization; only the **full authorized amount** can be captured. Automatic capture can be configured for immediate execution after authorization when adding PayPo in the live Customer Area. The page says merchant funding follows capture without waiting for the shopper to finish paying PayPo (lines 391–421, repeated 910–940).
- The test flow provides required sample names/email and verification code 123456. Live PayPo acceptance requires a request in the live Customer Area (lines 454–466, 942–954).

> [!warning] Component example and base link
> Both iOS Component initialization sections literally say to use a `None` class and show `None.self`/`None(...)` in Swift (raw lines 431–450, 488–505). The captured page does not explain that class or give a PayPo-specific replacement; do not treat the snippet as a verified runnable Component recipe. The Advanced “iOS Components integration” requirement links to an `integration=Drop-in` URL (line 476), while its action link uses Components (line 477). Verify the intended Components base flow before implementation.

## Detail locators

- Sessions prerequisites and `/sessions` fields/examples: pinned raw lines 15–389.
- First capture/offer lifecycle, configuration, Component snippet and test/live: lines 391–466.
- Advanced requirements, configuration, Component snippet and `/payments` fields/examples: lines 468–908.
- Advanced capture/offer lifecycle and test/live: lines 910–954.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-paypo]] — PayPo method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/ios-component/2026-09-15|PayPo iOS Component guide, captured 2026-09-15]]
