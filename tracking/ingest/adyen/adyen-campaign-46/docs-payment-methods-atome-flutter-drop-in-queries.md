# Fixed retrieval queries — Atome Flutter Drop-in

## Q1 — Identity and scope

**Query:** What does the Atome Flutter Drop-in guide add, and what does it not prove?

**Expected:** The captured guide at `https://docs.adyen.com/payment-methods/atome/flutter-drop-in` adds Atome-specific instructions to an existing Flutter Drop-in Sessions or Advanced integration. It covers request fields, MY/MYR and SG/SGD, redirect, partial-refund amount and test/live setup. It is not proof of current eligibility or a successful live payment; the main integration guide supplies generic steps. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-atome-flutter-drop-in.md` → `raw/adyen/docs/payment-methods/atome/flutter-drop-in/2026-09-15.md`. Evidence: raw `# Atome Flutter Drop-in` lines 15–23, `## Sessions flow Drop-in` lines 25–52, `## Advanced flow Drop-in` lines 768–801.

## Q2 — Flow prerequisites and warnings

**Query:** How do Atome Flutter Sessions and Advanced request paths differ, and what caveats apply to redirect, samples and live setup?

**Expected:** Sessions needs existing Flutter Drop-in, Checkout API v68+, redirect handling and Support contact; `/sessions` requires shopper name, email, phone, billing address, line items and MY/MYR or SG/SGD country/currency, with conditional delivery address (raw lines 29–52). Advanced needs existing Flutter Drop-in, redirect handling and Atome setup; `/payments` adds `type=atome` and corresponding fields; its requirements table does not repeat the API v68 gate (raw lines 768–801). Both say no extra Atome configuration (raw lines 734–736, 782–784). The Sessions integration link is labeled Sessions but targets `advanced-flow` (raw line 33). Both curl examples miss continuation after `-X POST` before `-d`; Sessions JSON repeats `countryCode` (raw lines 63–78, 812–813). An example labeled successful has `RedirectShopper` and redirect `action`, not proof of authorization or capture (raw lines 1518–1530). Partial refund specifies amount; sandbox account needs Adyen contact and separate account per country; live setup requires Support (raw lines 1534–1560). The related overview excludes portable electronics and states automatic capture after authorization; this child page does not restate those facts (`wiki/sources/adyen/source-adyen-docs-payment-methods-atome.md`). Route: root → provider index → `wiki/concepts/adyen-online-payments.md` → source page → pinned raw.
