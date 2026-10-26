# Bizum Web chooser retrieval checks

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-bizum-web]]`.

## Q1. What is its purpose and scope, and what cannot be inferred?

The canonical stem `source-adyen-docs-payment-methods-bizum-web` is a 2026-09-15 Web chooser for adding Bizum through Drop-in or the Redirect/Components child route (`raw/adyen/docs/payment-methods/bizum/web/2026-09-15.md:15-27`). It also points to four base Web Sessions/Advanced guides (`:29-36`). The chooser gives no method-specific request, version, merchant eligibility, live setup or payment-outcome rule; child and base guides are separate authority (`:19-36`).

## Q2. What are the central capability, prerequisites, and warnings?

The page offers an all-in-one Web Drop-in route and a Web Components route described as using Redirect (`raw/adyen/docs/payment-methods/bizum/web/2026-09-15.md:19-27`). It says to create the main integration first and lists Web Drop-in Sessions, Components Sessions, Drop-in Advanced and Components Advanced guides (`:29-36`). These routes are navigation, not proof that their implementation requirements are interchangeable or that a payment can be completed for a merchant (`:19-36`).
