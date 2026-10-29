# C44 Klarna Android Component retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-klarna-android-component`

Full pinned raw path: `raw/adyen/docs/payment-methods/klarna/android-component/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-klarna-android-component]]` → `[[raw/adyen/docs/payment-methods/klarna/android-component/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What does Adyen's Klarna Android Component page cover, and what can it establish about merchant availability?

**Answer path:** Raw opening lines 15–21 identify an add-on to an existing Android Components integration, scoped to v5.0.0+; earlier versions have another guide. `## Requirements` lines 23–39 specifies both Sessions and Advanced base flows and Customer Area addition. This page does not establish country/currency eligibility, a particular merchant's method enablement, or successful live payment; use the linked Klarna overview and base-flow guides for their own scopes.

## Q2 — central capability, prerequisites and warnings

**Query:** Which extra request fields and Component configuration does this Android guide require, and what test/live boundaries remain?

**Answer path:** `## API reference` lines 41–49 says no additional **Klarna-specific** fields for Sessions `/sessions` or Advanced `/payments`; `## Klarna Configuration` lines 51–67 says no extra Component configuration and routes each flow back to its base integration. These statements do not erase base API requirements. `## Test and go live` lines 69–96 calls for test data/status checks and a live checklist, with optional name/address; live testing can yield `Refused` and “Option Not Available.” GBP 1 for Pay over time is only an example of a minimum. A test status or checklist is not capture/settlement proof.
