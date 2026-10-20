---
title: "Adyen Issuing: UI component libraries overview"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/components-overview"
raw_files:
  - "adyen/docs/issuing/components-overview/2026-09-15.md"
tags: [adyen, issuing, components, onboarding, transactions]
---

## Overview

This 2026-09-15-captured Issuing-path overview introduces Adyen's prebuilt UI components for a platform's user interface. It lists a **Transfer Instrument** component before payment for bank-account management and verification flows, and a **Transactions** component after payment for transaction filtering, export and detail views. The page is a component catalog and simplified integration outline; it does not establish a completed bank-account verification, payment or refund.

## Key takeaways

- The stated platform fit is an embeddable UI plus a backend API layer able to initialize components. The simplified flow starts with a logged-in user: the platform server validates the user, creates an authentication session/token carrying required user roles, then the client instantiates the component with that token. Individual integration guides may add conditions. See raw lines 23–26 and 56–74.
- The Transfer Instrument listing says users can add, update or delete bank accounts and use instant verification or document upload while viewing verification status. The Transactions listing says users can filter/export transactions by account or date and view fees, IDs and refunds. These are listed component functions, not evidence of any particular verification or payment outcome. See raw lines 40–54.
- The page says components are **generally available for users operating in countries and regions where Adyen for Platforms is supported**. This is a dated component-scope statement and does not itself establish Issuing availability or eligibility for any platform. The captured browser minima are Chrome 98, Safari 15.4 and Firefox 94; use the raw for those version details. See raw lines 76–88.

## Detail locators

- Catalog purpose, fit and listed before/after-payment components: [[raw/adyen/docs/issuing/components-overview/2026-09-15|raw lines 15–54]].
- Server/client session flow and integration steps: [[raw/adyen/docs/issuing/components-overview/2026-09-15|raw lines 56–74]].
- Dated region and browser statements: [[raw/adyen/docs/issuing/components-overview/2026-09-15|raw lines 76–88]].

## Related

- [[adyen-issuing]] — Issuing balance-platform model and source catalog.
- [[adyen]] — provider context.
- [[source-adyen-docs-issuing-components-overview-before-payment-transfer-instrument-component]] — narrower Transfer Instrument integration guide.

## Raw Sources

- [[raw/adyen/docs/issuing/components-overview/2026-09-15|Build your interface with UI component libraries (captured 2026-09-15)]]
