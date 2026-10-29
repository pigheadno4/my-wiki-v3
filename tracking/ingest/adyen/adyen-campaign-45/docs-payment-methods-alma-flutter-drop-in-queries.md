# Alma Flutter Drop-in retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-alma-flutter-drop-in`
**Full pinned raw:** `raw/adyen/docs/payment-methods/alma/flutter-drop-in/2026-09-15.md`
**Verified locators:** `# Alma Flutter Drop-in`, lines 15–23; `## Sessions flow Drop-in`, line 25; `## Advanced flow Drop-in`, line 98; redirect example lines 170–184.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-alma-flutter-drop-in.md` → pinned raw.
**Answer boundary:** This is a method add-on for existing Flutter Drop-in, with TEST examples and Customer Area steps. It does not prove current account availability, completed redirect return or final payment success.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** Sessions requirements and optional field table lines 29–48; app-scheme return placeholder line 64; Advanced requirements and optional installment count lines 102–128; HTTPS return example line 144; redirect response 170–184; test/live lines 186–190.
**Answer boundary:** Sessions requires Flutter Drop-in and Checkout API v68+, while Advanced requires redirect action handling. The Sessions setup row directs contacting Support, whereas Advanced says add Alma in Customer Area; Sessions' base integration link points to Advanced. Method tables leave phone, email and addresses unmarked; Advanced optional installment count selects 3/4 or omission lets the shopper choose. No extra method configuration is stated. Sessions uses `adyencheckout://your.package.name` while Advanced uses HTTPS, without a shown completed return. Both curl examples split `-X POST` and `-d` without continuation (lines 52–58, 132–138), so they are not verified copy-ready.
