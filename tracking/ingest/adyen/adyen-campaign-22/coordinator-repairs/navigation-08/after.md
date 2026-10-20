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
