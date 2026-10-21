---
title: "Adyen for Platforms UI components"
type: concept
category: technology
tags: [adyen, platforms, ui-components, onboarding, reporting]
---

## Definition

Adyen for Platforms UI components are embeddable libraries for platform user flows before, during, and after payment. The 2026-09-15 overview includes bank-instrument, Checkout, transaction, payout, report, dispute, payment-link, and Capital views. A platform backend validates the user and creates a role-bearing authentication session; the client initializes the component with that token. [[source-adyen-docs-platforms-components-overview]]

## Evidence boundary

Component availability depends on product, region, user role, and each child guide. Business-financing components have narrower regional availability, and the snapshot's cashout/Capital-update roadmap is future-looking. Component rendering, a session token, or a displayed status does not establish a completed payment, transfer, bank receipt, dispute outcome, or financing grant.

## Sources

- [[source-adyen-docs-marketplaces-components-overview-during-payment]] — 2026-09-15 short Marketplace-path during-payment navigation page linking Checkout components and the component library; no implementation or outcome proof.


- [[source-adyen-docs-marketplaces-components-overview-before-payment]] — 2026-09-15 Marketplace before-payment Onboarding component hub linking Individual Legal Entity, Terms of Service and Transfer Instrument child guides; card text is navigation, not verification or payout proof.


- [[source-adyen-docs-marketplaces-components-overview-after-payment]] — 2026-09-15 Marketplace after-payment component hub linking Transactions, Payouts, Reports, Disputes, Pay by Link and Capital child guides; navigation does not prove financial or dispute outcomes.


- [[source-adyen-docs-marketplaces-build-user-dashboards]] — 2026-09-15 Marketplace-path Platform Experience dashboard hub routing Transactions, Payouts, Reports, Disputes and Pay by Link child component guides.


- [[source-adyen-docs-marketplaces-components-overview-before-payment-terms-of-service-component]] — 2026-09-15 Marketplace Accept/Manage Terms of Service component overview for LEM v3/v4 entities; 4.0.x integration details are a placeholder pointing to 3.32.x, with other onboarding API steps still required.


- [[source-adyen-docs-marketplaces-components-overview-before-payment-individual-legal-entity-component]] — 2026-09-15 Marketplace Individual Legal Entity onboarding-component overview for LEM v3/v4 entities, Create/Manage Individual functions and API-only-flow boundaries; captured v4.0.x section lacks integration steps and refers to v3.32.x.


- [[source-adyen-docs-marketplaces-components-overview-after-payment-capital-component]] — 2026-09-15 Marketplace-path Capital Overview/Offer UI guide for required disclosures, eligible offer/action/status and term-sheet views; credit-after-information versus approval-and-signature wording conflicts.


- [[source-adyen-docs-marketplaces-components-overview-before-payment-transfer-instrument-component]] — 2026-09-15 Marketplace Configuration/Management bank-instrument UI guide for LEM v3/v4, legal-entity/role-scoped onboarding sessions, conditional US/CA property and submission events; other onboarding and verification outcomes remain separate.


- [[source-adyen-docs-marketplaces-components-overview-after-payment-reports-component]] — 2026-09-15 Marketplace Platform Experience Reports Overview guide for account-holder-scoped Payout report CSV access, automatic-payout coverage limits, UTC filters, session role and versioned UI customization.


- [[source-adyen-docs-marketplaces-components-overview-after-payment-pay-by-link-component]] — 2026-09-15 Marketplace-path Platform Experience Pay by Link component guide for portal link management, role/store setup, link states and split-routing boundary.


- [[source-adyen-docs-marketplaces-components-overview-after-payment-payouts-component]] — 2026-09-15 Marketplace-path Platform Experience Payouts Overview/Details guide for role-scoped automatic-payout reporting, account/UTC+0 filters, report-coverage limits and versioned integration; UI is not bank-receipt proof.


- [[source-adyen-docs-marketplaces-components-overview-after-payment-transactions-component]] — 2026-09-15 Marketplace-path Platform Experience Transactions Overview/Details guide for account-holder-scoped sessions, balance-account views, first-100 CSV export and role-gated refund requests; UI status is not final refund proof.


- [[source-adyen-docs-marketplaces-components-overview-after-payment-disputes-component]] — 2026-09-15 Marketplace Disputes Overview/Management component guide for account-holder-scoped views and conditional chargeback defense/acceptance, with version, split-access, upload and refund limits.


- [[source-adyen-docs-marketplaces-checkout-components]] — 2026-09-15 Marketplace-path Web Components/Sessions checkout guide for payment-server, client and webhook roles, redirect handling and test-to-live conditions; UI/session result is not split booking or payout proof.


- [[source-adyen-docs-marketplaces-components-overview]] — 2026-09-15 Marketplace UI component-suite inventory, including legal-entity/Terms of Service before-payment routes, server role-bearing sessions, regional/product limits and future cashout/Capital-update roadmap; UI is not outcome proof.


- [[source-adyen-docs-issuing-components-overview-after-payment-transactions-component]] — 2026-09-15 Issuing-path copy of the Platform Experience Transactions Overview/Details guide; its stated prerequisite is Adyen for Platforms, with platform-scoped session and role-gated refunds.


- [[source-adyen-docs-platforms-build-user-dashboards]] — 2026-09-15 Platform Experience user-dashboard hub linking Transactions, Payouts, Reports, Disputes and Pay by Link component guides; inventory, not operation proof.


- [[source-adyen-docs-platforms-components-overview-before-payment]] — 2026-09-15 before-payment onboarding-components navigation hub linking the Transfer Instrument guide; child pages own integration and verification detail.


- [[source-adyen-docs-platforms-components-overview-after-payment]] — 2026-09-15 after-payment Platform Experience hub linking Transactions, Payouts, Reports, Disputes, Pay by Link and Capital child guides; navigation, not financial-outcome proof.


- [[source-adyen-docs-platforms-components-overview-after-payment-reports-component]] — 2026-09-15 Platform Experience Reports Overview guide for scoped Payout report downloads, automatic-payout coverage limits, session roles and optional dashboard customization.


- [[source-adyen-docs-platforms-components-overview-after-payment-capital-component]] — 2026-09-15 Capital UI component guide for disclosure, offer/action/status and term-sheet views with version and eligibility limits; screens do not prove grant funding or repayment.


- [[source-adyen-docs-platforms-components-overview-before-payment-transfer-instrument-component]] — Transfer Instrument Configuration/Management, LEM v3/v4 and legal-entity-scoped onboarding session (2026-09-15).


- [[source-adyen-docs-platforms-components-overview-after-payment-payouts-component]] — 2026-09-15 Platforms payout-reporting component guide for balance-account overview/details views, scoped session role and payout-report coverage/version limits; displayed net payout is not independent bank-receipt proof.


- [[source-adyen-docs-platforms-components-overview-after-payment-transactions-component]] — Transactions Overview/Details data, role-gated refunds, session setup, and CSV limits (2026-09-15).


- [[source-adyen-docs-platforms-components-overview-after-payment-pay-by-link-component]] — 2026-09-15 Platform Experience guide to role-gated Pay by Link portal components, store/terms setup, link state, versioned integration and unchanged payment split routing.


- [[source-adyen-docs-platforms-components-overview]] — 2026-09-15 Platforms component-suite overview for the inventory, session integration, availability boundaries, and dated roadmap.

- [[source-adyen-docs-platforms-components-overview-during-payment]] — 2026-09-15 short Platforms during-payment navigation page pointing to Checkout components and their dedicated integration guide.


- [[source-adyen-docs-platforms-components-overview-after-payment-disputes-component]] — 2026-09-15 Platforms Disputes Overview/Management component guide for account-holder-scoped viewing and conditional chargeback actions, with version, access, evidence and refund limits.


## Related

- [[adyen-platforms]] — parent platform context.
