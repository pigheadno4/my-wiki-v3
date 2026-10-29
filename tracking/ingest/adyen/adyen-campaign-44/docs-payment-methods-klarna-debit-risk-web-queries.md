# Klarna Debit Risk Web retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-klarna-debit-risk-web`
**Full pinned raw:** `raw/adyen/docs/payment-methods/klarna-debit-risk/web/2026-09-15.md`
**Verified locators:** `# Klarna Debit Risk for Web`, lines 15–17; `### How do you want to integrate?`, lines 19–27; `## See also`, lines 29–36.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-klarna-debit-risk-web.md` → pinned raw.
**Answer boundary:** This short Web page chooses between Debit Risk Drop-in and Components guides. It does not provide the method's request schema, SDK version, redirect outcome or merchant eligibility. Use the separate Debit Risk overview for the online-banking/non-guaranteed-settlement qualification.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** Drop-in chooser lines 21–23; Components Redirect chooser lines 25–27; main integration prerequisite and Sessions/Advanced route list lines 29–36.
**Answer boundary:** Create the main Web integration first, then follow the Debit Risk Web Drop-in or Web Components method guide. The chooser links to main Sessions and Advanced guides for both Web UI paths. The Components label mentions Redirect, but this page gives no return-processing steps or completed-payment result. Debit Risk settlement and chargeback behavior belongs to the method overview, not this navigation page.
