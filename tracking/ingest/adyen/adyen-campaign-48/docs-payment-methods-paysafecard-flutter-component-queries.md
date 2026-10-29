# Retrieval checks — PaySafeCard Flutter Component

## Q1 — purpose and scope

**Query:** What does the PaySafeCard Flutter Component documentation add to an existing Adyen integration, and does it prove that a merchant account can accept a live PaySafeCard payment now?

**Expected:** Route `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard-flutter-component.md` → `raw/adyen/docs/payment-methods/paysafecard/flutter-component/2026-09-15.md`. Answer that this captured page is a method-specific Flutter Components add-on for existing Sessions or Advanced integrations (raw lines 15–23), not a complete standalone guide. It documents a live Customer Area Support step (raw lines 282, 621); the snapshot does not prove present merchant enablement or live execution.

## Q2 — central capability, prerequisites and warnings

**Query:** For PaySafeCard in Flutter Components, what differs between Sessions and Advanced flows, what redirect and account setup are required, and which source examples or links need caution?

**Expected:** Use the same root/provider/concept/source/raw route, canonical stem `https://docs.adyen.com/payment-methods/paysafecard/flutter-component`. Sessions requires an existing Flutter Components Sessions flow, Checkout API v68+, redirect handling and PaySafeCard setup in Customer Area; add `shopperReference` to `/sessions` (raw lines 25–44). Advanced requires an existing Flutter Components Advanced flow, redirect handling and Customer Area setup; add `shopperReference` to `/payments` (raw lines 284–310). Both say no extra method configuration (raw lines 270–272, 298–300). Advanced response example has `RedirectShopper` and `action.type: redirect`, not a final-success proof (raw lines 597–611). Test code, test Customer Area and Support-mediated live setup are at raw lines 274–282 and 613–621. Warn that the two Integration type links say `integration=Drop-in` despite describing Components, and the Sessions row points to an Advanced-flow base guide (raw lines 31, 292), and that the Sessions curl sample lacks a line continuation between `-X POST` and `-d` (raw lines 50–66); library snippets are abbreviated (raw lines 84–87, 262–265). Example NL/EUR and test endpoints are illustrative, not universal market or live eligibility claims.

**Cross-page flow qualification:** The approved [[source-adyen-docs-payment-methods-paysafecard|PaySafeCard overview]] labels Payment flow **Direct** (its pinned raw `raw/adyen/docs/payment-methods/paysafecard/2026-09-15.md` lines 25–27), whereas this Flutter child explicitly requires redirect handling in both flow requirements and illustrates `RedirectShopper` with `action.type: redirect` (child pinned raw lines 31–33, 292–293, 597–611). Preserve both captured descriptions; the overview label does not erase the child's redirect step or prove current account behavior.
