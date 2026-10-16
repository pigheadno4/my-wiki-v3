# Fixed queries — Platforms account-holder status

## Q1 — purpose, scope, and what must not be inferred

**Query:** What does account-holder status represent, and does active state alone prove verified capabilities or completed financial operations?

**Answer:** It is overall account-holder standing. The guide describes active after onboarding and verification, suspended as temporarily disabling the resource and blocking payouts, and closed as permanently disabling the resource and its capabilities. Balance accounts and payment instruments have their own statuses; inactive is payment-instrument-only. An active label alone is not the complete verification/capability record, and none of these statuses proves an authorization, settlement, payout or bank receipt. Raw: `raw/adyen/docs/platforms/account-holder-status/2026-09-15.md:17-38`. Canonical route: `[[source-adyen-docs-platforms-account-holder-status]]` → `[[adyen-platforms]]`.

## Q2 — central transitions, prerequisites, and warnings

**Query:** Who can change status, what inherits an Adyen action, and how does status affect payment splits?

**Answer:** The platform can update status through Configuration API, while Adyen may suspend/close for risk, fraud or terms; only Adyen reverses its own suspension, and closed is not editable. Adyen suspension affects related balance accounts; closure also closes related payment instruments; reason-dependent inheritance may extend to account holders sharing a legal entity. Reason tables are guidelines because payout/pay-in capability blocks and inheritance vary case by case. Payment processing is not directly changed by account-holder status: after settlement, a suspended holder with pay-ins allowed receives a split in their balance account, whereas blocked pay-ins or closure route it to the liable account holder's Reserved Incorrect Splits Account. This routing description is not individual settlement proof. The page routes actual suspend/reactivate/close steps to Manage account holders and provides no exact credential-role or propagation-time rule. Raw: `raw/adyen/docs/platforms/account-holder-status/2026-09-15.md:19-23,40-93`. Canonical route: `[[source-adyen-docs-platforms-account-holder-status]]` → `[[adyen-platforms]]`.
