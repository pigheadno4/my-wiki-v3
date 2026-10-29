# Fixed queries — PaySafeCard Web Component

## Q1 — purpose and limits

**Query:** What does the captured PaySafeCard Web Component page add, and what does it leave to the base integration?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/paysafecard/web-component` is a 2026-09-15-captured method add-on to existing Web Components Sessions and Advanced flows. It marks shopperReference for each flow, describes redirect handling, and links main integration guides; it is not a complete, current, enabled or live-tested recipe (full pinned `raw/adyen/docs/payment-methods/paysafecard/web-component/2026-09-15.md`, `# PaySafeCard Web Component` lines 15–23, Sessions lines 25–47, Advanced lines 310–352). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard-web-component.md`.

## Q2 — fields, redirect, live setup and source conflicts

**Query:** What PaySafeCard-specific Sessions/Advanced Web Components requirements and caveats apply?

**Expected answer:** Sessions requires existing Web Components Sessions flow, Checkout API v68+, redirect handling, Customer Area setup and `shopperReference` in `/sessions`; it imports/initializes `Redirect` and says no extra PaySafeCard configuration is needed (child `raw/adyen/docs/payment-methods/paysafecard/web-component/2026-09-15.md`, lines 25–47, 270–298). Advanced requires existing Web Components Advanced flow, redirect handling, Customer Area setup and `shopperReference` in `/payments`; response `action.type` is `redirect` (child lines 310–352, 639–653). Both sections use test-only code and direct live merchants to Support for Customer Area enablement (lines 300–308, 655–663). **Cross-page warning:** the PaySafeCard overview `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard.md`, pinned `raw/adyen/docs/payment-methods/paysafecard/2026-09-15.md` lines 25–27, labels the flow Direct; preserve this against the child redirect requirements rather than silently reconciling. **Example warnings:** `type:paysafecard` is unquoted/undefined, Web Sessions example uses app-style returnUrl, both curl examples omit `-X POST` to `-d` continuation, and Advanced payment request examples omit `paymentMethod` (child lines 53–68, 296–298, 340–342, 354–637). These snippets are not a complete executable request. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard-web-component.md`.
