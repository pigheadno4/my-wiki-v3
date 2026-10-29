---
title: "Adyen PaySafeCard iOS Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/ios-component"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/ios-component/2026-09-15.md"
tags: [adyen, paysafecard, ios, components, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds PaySafeCard to an **existing iOS Components integration**, separately for Sessions and Advanced server-side flows. It gives method-specific request, Component, redirect, and test/live steps and links to main integration guides for shared steps. The TEST examples are illustrative and do not establish current market availability, account enablement, a completed payment, or live operation. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions prerequisites:** An existing iOS Components Sessions integration must use **Checkout API v68 or later**, handle a `redirect` action, and have PaySafeCard added in Customer Area. The PaySafeCard-specific `/sessions` table marks `shopperReference` required as the merchant's unique shopper reference. The NL/EUR request and app-scheme `returnUrl` are TEST examples, not a general eligibility or return-URL contract (pinned raw lines 25–69).
- **Advanced prerequisites and request:** The page requires an existing iOS Components Advanced integration, redirect handling, and Customer Area setup. Its method-specific `/payments` table also marks `shopperReference` required. The Advanced requirements do **not** repeat the Sessions table's v68 minimum. The Advanced integration link is labeled Components but its URL selects `integration=Drop-in`; the action and payment links select Components. Resolve the base-guide route accordingly (lines 308–355).
- **Component behavior:** Both flows say no extra PaySafeCard configuration is needed and initialize `InstantPaymentComponent` after finding `.other("paysafecard")`. In the shown Sessions Swift snippet, `component.delegate = session`; in Advanced, `component.delegate = self`. Each snippet then calls `initiatePayment()` (lines 270–295, 320–345).
- **Redirect and examples:** The Advanced example response is `RedirectShopper` with `action.type=redirect`; it is a next shopper action rather than proof of authorization. The Advanced sample `/payments` bodies include `shopperReference` but do not show a `paymentMethod` object, while the method is selected by the Component. Do not treat those abbreviated server examples as a complete request contract or infer that a full payment never needs method data. The curl samples also omit a shell continuation between `-X POST` and `-d` (lines 357–378, 642–656; Sessions sample lines 50–69).
- **Test and live:** The page gives a **test** 16-digit code, `0000 0000 0990 3417`, and routes test status checks to the test Customer Area payment list. Before live acceptance, it says to contact Adyen Support to add PaySafeCard in the live Customer Area. Its Support hyperlink itself uses a test Customer Area URL; it is not evidence that live enablement has occurred (lines 298–306, 658–666).

## Detail locators

- Sessions requirements and `shopperReference` table: pinned raw lines 25–46; TEST session/server examples: lines 48–267.
- Sessions no-extra-configuration, Component and test/live steps: lines 270–306.
- Advanced requirements, Component and `/payments` table: lines 308–355; TEST server examples: lines 357–640.
- Advanced redirect action and test/live steps: lines 642–666.

## Related

- [[adyen-online-payments]] — provider online-payments concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/ios-component/2026-09-15|PaySafeCard iOS Component guide, captured 2026-09-15]]
