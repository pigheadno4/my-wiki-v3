# PayPo Web chooser worker retrieval queries

## Q1 — Purpose and scope

**Query:** What is the PayPo for Web page, and what does it establish about a Web integration?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paypo-web.md` → `raw/adyen/docs/payment-methods/paypo/web/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/paypo/web`; full pinned raw `raw/adyen/docs/payment-methods/paypo/web/2026-09-15.md`, `# PayPo for Web` lines 15–17 and `### How do you want to integrate?` lines 19–27. This is a route chooser, not a payment request specification or evidence of a real transaction or live merchant eligibility.

## Q2 — Child and base integration routes

**Query:** Which PayPo Web child guides and main Sessions/Advanced routes are linked?

**Expected route:** Same root → Adyen index → online-payments concept → PayPo Web chooser source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path: Drop-in child route lines 21–23, Components/Redirect child route lines 25–27, and `## See also` main integration links lines 29–36. Build the selected base Web integration before adding PayPo; follow its method-specific child guide for fields, redirect, capture and testing. The chooser supplies no direct lifecycle rule.
