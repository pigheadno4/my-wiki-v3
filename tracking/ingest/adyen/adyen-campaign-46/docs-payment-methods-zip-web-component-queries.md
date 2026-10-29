# Fixed retrieval queries — Zip Web Component

## Q1 — Identity and scope

**Query:** What is the Zip Web Component guide, and what does its AU/AUD example not establish?

**Expected:** The captured guide at `https://docs.adyen.com/payment-methods/zip/web-component` covers adding Zip to existing Web Components Sessions/Advanced flows, server requests, redirect Component, and recurring-token flow. It is not live eligibility, a verified executable recipe, or successful payment evidence. Its AU/AUD request examples do not define all regions; the separate Zip overview lists AU/US and AUD/USD without explicit country-currency pairings. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-zip-web-component.md` → `raw/adyen/docs/payment-methods/zip/web-component/2026-09-15.md`. Evidence: raw `# Zip Component` lines 15–37, `## API reference` lines 39–55, and example lines 61–112; overview `wiki/sources/adyen/source-adyen-docs-payment-methods-zip.md`.

## Q2 — API route, redirect and recurring

**Query:** Which Zip Web Component API and client steps apply, and when is a recurring token available?

**Expected:** Sessions is the default with Components v5.0.0+, while `/payments` is the additional-use-case tab. Both API tables list shopper/contact/address/line-item fields with blank Required cells; image URL is optional and at most 500 characters. `/payments` also has conditional `clickAndCollect=true` (raw lines 43–55, 692–705). Advanced `/payments` responds with an `action` for redirect; `RedirectShopper` is an example, not settlement (raw lines 1386–1399). Web v6 mounts `Redirect` type zip; v5 or earlier uses `checkout.create('zip')` (raw lines 1402–1432). Token creation uses `storePaymentMethod=true` and shopper reference; only after settlement does `recurring.token.created` webhook carry `storedPaymentMethodId`. Future requests use stored ID, same reference, `ContAuth`, `Subscription` or `UnscheduledCardOnFile` (raw lines 1434–1467). The `/payments` curl example contains literal hint markup, so it is not a ready-to-send JSON recipe (raw line 724). Live acceptance needs a Zip request in live Customer Area (raw lines 1667–1673). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-zip-web-component.md` → pinned raw.
