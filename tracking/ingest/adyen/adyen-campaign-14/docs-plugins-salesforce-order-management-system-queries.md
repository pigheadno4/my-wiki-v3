# Fixed retrieval checks — docs-plugins-salesforce-order-management-system

## Q1 — Purpose, scope, and what not to infer

**Query:** What is the Adyen Salesforce OMS page about, and what must not be inferred from it?

**Answer:** It is an overview of Adyen's Salesforce OMS package for order/fulfillment payment management alongside Salesforce Commerce Cloud payment solutions, distinct from the SFCC storefront SFRA and Composable integrations. It lists modification capabilities, optional OOBO and setup navigation, not an installed package, merchant entitlement, transaction result, settlement or bank receipt. It does not supply an independent OMS payment-method matrix, operator roles or credential scopes. The 2023-10-13 last-modified metadata conflicts with a V3 August 2024 release row; do not treat the support table as current verification. Evidence: raw lines 10, 15–43, 45–56, 58–88. Canonical route after concept promotion: [[adyen-index]] → [[adyen-salesforce-order-management-system]] → ## Sources → [[source-adyen-docs-plugins-salesforce-order-management-system]] → [[raw/adyen/docs/plugins/salesforce-order-management-system/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** Which OMS payment actions and starting conditions does this overview describe?

**Answer:** It lists full/partial captures during fulfillment and initiation of full/partial refunds; full void/authorization reversal of authorized payments; and, after partial capture and full order cancellation, cancellation of only the uncaptured remainder. Optional OOBO handles credit-card authorization on behalf of shoppers and OOBO with Pay by Link is linked for payment links. Get-started asks for Adyen live-payment preparation and a test account, permits sandbox setup while awaiting live credentials, then routes to SFCC go-live and releases/upgrades. The page names V2/V3 support levels/dates but has inconsistent metadata; verify the applicable release. It does not describe final order-state transitions or prove any capture, refund, payment or payout. Evidence: raw lines 23–43, 45–72. Canonical route after concept promotion: [[adyen-index]] → [[adyen-salesforce-order-management-system]] → ## Sources → [[source-adyen-docs-plugins-salesforce-order-management-system]] → [[raw/adyen/docs/plugins/salesforce-order-management-system/2026-09-15]].
