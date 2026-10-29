# Alma Android retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-alma-android`
**Full pinned raw:** `raw/adyen/docs/payment-methods/alma/android/2026-09-15.md`
**Verified locators:** `# Alma for Android`, lines 15–17; `### How do you want to integrate?`, lines 19–27; `## See also`, lines 29–36.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-alma-android.md` → pinned raw.
**Answer boundary:** This is an Android integration chooser, not a method outcome guide. It does not establish request fields, version requirements, account eligibility, completed redirect or payment result.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** Drop-in chooser lines 21–23; Components/InstantPaymentComponent chooser lines 25–27; main-integration prerequisite and Sessions/Advanced links lines 29–36.
**Answer boundary:** Choose Android Drop-in or Components, and create the corresponding main Sessions/Advanced integration before adding Alma. The Components route names InstantPaymentComponent for redirect handling. The links are navigation only; child guides carry method-specific setup and return details.
