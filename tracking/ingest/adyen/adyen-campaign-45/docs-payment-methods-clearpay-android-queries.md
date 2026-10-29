# Clearpay Android chooser retrieval check

- Canonical source stem: `source-adyen-docs-payment-methods-clearpay-android`.
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-clearpay-android.md` → `raw/adyen/docs/payment-methods/clearpay/android/2026-09-15.md`.

## Q1 — Purpose, scope, and inference limit

**Query:** What is this Clearpay Android page for, and can its choices establish eligibility or payment success?

**Expected:** It is an Android navigation chooser for Drop-in and Components, with main Android integration guide links. It does not provide request fields, country/currency scope, merchant enablement or an outcome. The related Clearpay overview gives GB/GBP scope and distinguishes regional brands. Evidence: pinned raw `# Clearpay for Android` lines 15–17, `### How do you want to integrate?` lines 19–27 and `## See also` lines 29–36.

## Q2 — Central routes and prerequisite

**Query:** Which Android child routes are offered, and what base-integration prerequisite does the chooser state?

**Expected:** Drop-in is labelled an all-in-one Android UI route; Components points to `InstantPaymentComponent` for the Clearpay redirect. The page says to create the main integration before adding Clearpay and links Android Drop-in/Components base guides for both Sessions and Advanced flows. The links are navigation, not child-specific prerequisites or proof of a completed flow; consult the chosen child guide for request, redirect and lifecycle details. Evidence: pinned raw `### How do you want to integrate?` lines 19–27 and `## See also` lines 29–36.
