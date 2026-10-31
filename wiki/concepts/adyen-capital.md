---
title: "Adyen Capital"
type: concept
category: technology
tags: [adyen, capital, platforms, business-financing]
---

## Definition

Adyen Capital is a separate embedded business-financing product for eligible platform or marketplace users. Adyen's 2026-09-15 landing page describes proactive offers presented through APIs or low-code components, possible funding to a balance account or transfer instrument, daily repayment based on a fixed percentage of Adyen-processed volume, and a fixed fee. These are product descriptions in a dated snapshot, not a financing offer or evidence of a particular user's funding or repayment. [[source-adyen-docs-capital]]

## Evidence boundary

The landing page lists supported regions with specific inclusions and exclusions and points to separate integration, resource, lifecycle and reporting guides. It does not establish current jurisdiction or user eligibility, verification/capability status, approved terms, acceptance, grant execution, amount owed, debt completion, bank receipt or legal characterization. Keep Capital distinct from ordinary payment settlement, a user bank payout, Issuing and Business accounts.

## Sources

- [[source-adyen-api-explorer-capital-webhooks-latest-post-balanceplatform-grants-updated]] — 2026-09-15-captured Capital incoming grant-updated webhook reference with grant balance, recipient and status fields; disbursement/repayment are illustrative triggers, while `2xx` acceptance is not funding or repayment proof.


- [[source-adyen-api-explorer-capital-webhooks-latest-post-balanceplatform-capital-dynamicoffer-created]] — 2026-09-15-captured account-holder dynamic-offer creation event with range, validity and repayment-term fields; offer creation is separate from formal-offer selection, grant acceptance and funding.


- [[source-adyen-api-explorer-capital-webhooks-latest-post-balanceplatform-grants-created]] — 2026-09-15-captured Capital grant-created webhook schema for offer/grant-account IDs, principal/fee/total, optional destination and status/actions; creation alone is not disbursement or receipt proof.


- [[source-adyen-api-explorer-capital-webhooks-latest-post-balanceplatform-balanceaccountholder-capitaloffer-created]] — 2026-09-15-captured Capital static-offer-created webhook contract for an account holder, with optional amount, fee, contract type, validity and repayment terms; an offer is separate from grant acceptance or disbursement.


- [[source-adyen-api-explorer-capital-webhooks-latest-overview]] — 2026-09-15-captured Capital webhooks v1 catalog for static/dynamic-offer creation and grant creation/update; event listing supplies no payload or funding-transfer outcome.


- [[source-adyen-api-explorer-transfers-latest-post-grants]] — 2026-09-15-captured Transfers API v4 TEST `POST /grants` reference for requesting payout of a selected Capital offer, with grant/status readback; a 200 or Pending grant is not final disbursement or repayment proof, and the 404 payment wording is mismatched.


- [[source-adyen-api-explorer-transfers-latest-get-grants]] — 2026-09-15-captured Transfers API v4 TEST `GET /grants` list contract for optional counterparty-holder filter, grant/offer/account IDs, balances and statuses; title and 404 wording conflict with the grant-list body, and a read is not disbursement or repayment proof.


- [[source-adyen-api-explorer-balanceplatform-latest-get-grantoffers]] — 2026-09-15-captured Balance Platform API `/bcl/v2` test-server GET grant-offer list contract for required `accountHolderId`; query description conflicts with account-holder wording, and generic payment-instrument error examples are not offer-specific evidence.


- [[source-adyen-docs-marketplaces-compliance-financial-products-user-interface-capital-requirements]] — 2023-modified, 2026-09-15-captured Marketplace Capital-specific UI guideline for offers, KYC/terms, insights/security and Ireland precontract disclosures; not legal advice or grant proof.


- [[source-adyen-docs-marketplaces-components-overview-after-payment-capital-component]] — 2026-09-15 Marketplace-path Platform Experience Capital component guide for conditional financing offers, required actions, grant status and repayment display; UI does not prove funding or repayment.


- [[source-adyen-docs-capital-keeping-records]] — 2024-modified, 2026-09-15-captured Capital service-record retention and categories, with API-only UI screenshot exception and UK/Ireland vulnerability-record scope; not legal advice or retention proof.


- [[source-adyen-docs-capital-get-grant-offers]] — 2026-09-15 Capital offer-choice hub comparing dynamic amount ranges with static fixed amount-term offers, conditional counts and pilot variable 90/180/360-day repayment terms; no offer or funding outcome.


- [[source-adyen-docs-capital-webhook-types]] — 2026-09-15 Capital webhook taxonomy for account-holder offers, grant lifecycle, grant-related transfer subtype/direction and booked transaction correlation; event families are distinct evidence grains.


- [[source-adyen-docs-capital-download-offers]] — 2026-09-15 Customer Area Capital CSV export guide for eligible account-holder offer ranges, daily generation, seven-day validity, role/region conditions and file columns; export is not an accepted offer or funded grant.


- [[source-adyen-docs-capital-additional-financing]] — 2026-09-15 pilot Capital renewal conditions versus a new grant after full repayment, including age/repayment/currency/offer gates, renewed ToS, fee/principal mechanics and UI/API paths with divergent minimum wording.


- [[source-adyen-docs-capital-pricing-and-eligibility]] — 2024-modified, 2026-09-15-captured Capital fee prohibition alongside broader Platforms fee notices and eligibility-criteria review; dated guideline, not approved pricing or user eligibility.


- [[source-adyen-docs-capital-reporting-to-adyen]] — 2024-modified, 2026-09-15-captured Capital-platform immediate notification, conditional quarterly Adyen-product complaints reporting and UK/Ireland aggregate vulnerability totals/annual patterns; not legal advice or submission proof.


- [[source-adyen-docs-capital-customer-service-support]] — 2024-modified, 2026-09-15-captured Capital-route financial-products support guideline for platform first/second-line ownership, accessible/free channels, 24/7 critical-notification intake and UK/Ireland vulnerable-customer measures; not legal advice or performance proof.


- [[source-adyen-docs-capital-get-grant-balances]] — 2022-modified, 2026-09-15-captured Capital GET routes for account-holder grant lists, individual grant balances/status/renewal fields and grant-account aggregate balances/limits; examples are not live debt or disbursement proof.


- [[source-adyen-docs-capital-manage-disbursements]] — 2026-09-15 Capital post-disbursement GET/PATCH guide for distinct grant/disbursement IDs, repayment basis-points configuration and region-limited unscheduled-repayment account details; examples are not funding proof.


- [[source-adyen-docs-capital-customer-complaints]] — 2024-modified, 2026-09-15-captured financial-services complaint identification, handling, escalation and UK/Ireland additions under Capital; dated guidance, not legal advice or case-resolution proof.


- [[source-adyen-docs-capital-get-grant-offers-static-offers]] — 2026-09-15 pilot-qualified Capital static-offer list/detail/webhook guide for account-holder offers, seven-day validity and conditional renewal; examples have estimated/max-term and request/response-ID differences, and offers are not funded grants.


- [[source-adyen-docs-capital-make-grant-request]] — 2026-09-15 Capital POST /grants and disbursement-update guide for offer/ToS/capability gates, recipient selection, asynchronous Requested response and separate grant/transfer/transaction evidence.


- [[source-adyen-docs-capital-user-interface]] — 2023-modified, 2026-09-15-captured Capital UI, country disclosure, terms/consent and information-access guideline; dated guidance, not accepted-grant or legal-compliance proof.


- [[source-adyen-docs-capital-webhook-types-fund-transfers-webhooks]] — 2026-09-15 Capital transfer/transaction webhook examples for grant credits, scheduled repayment and two-leg unscheduled collection/repayment; successful-only samples contain status/event-type/sign/date conflicts and are not bank-receipt or debt-completion proof.


- [[source-adyen-docs-capital-renew-grant]] — 2026-09-15 pilot guide for partially repaid grant renewal, minimum/offer and renewed-ToS gates, prior/subsequent IDs, asynchronous request and separate grant/transfer/payout observations.


- [[source-adyen-docs-capital-vulnerable-users]] — 2026-09-15 UK/Ireland Capital staff guidance for recognizing vulnerability, consent-sensitive tailored support and factual privacy-aware records; expressly not legal advice or proof of compliant service.


- [[source-adyen-docs-capital-terms-of-service]] — 2026-09-15 Capital grant ToS guide covering required document types, `adyenCapital` generation, authorized signer acceptance and acceptance-record readback before grant payout.


- [[source-adyen-docs-capital-get-grant-offers-dynamic-offers]] — 2026-09-15 pilot Capital API guide from holder-specific dynamic ranges through informational calculation to a static formal offer, with expiry, role/capability and rate limits; offer creation does not prove grant acceptance or funding.


- [[source-adyen-docs-capital-collect-user-data]] — 2026-09-15 Capital API guide for country/entity-dependent higher-amount KYC, hosted/API-only collection and separate capability/grant verification; threshold wording differs within the page.


- [[source-adyen-docs-capital-compliance-guidelines]] — 2022-modified, 2026-09-15-captured Capital compliance-guidelines overview for conditional material review and topic routes, including France-specific guidance; not legal advice or compliance proof.

- [[source-adyen-docs-capital-french-intermediary]] — 2026-09-15 Capital-specific France/French-user ORIAS intermediary-registration guide for director capacity, category, Adyen mandate, post-approval disclaimer and renewal; not legal advice or registration proof.


- [[source-adyen-docs-capital-marketing-user-communication]] — 2023-modified, 2026-09-15-captured Capital collateral scope, Adyen pre-approval/resubmission and country-specific provider-disclosure guideline; not legal advice or approved-material proof.



- [[source-adyen-docs-capital-repayment]] — 2026-09-15 Capital guide to scheduled net-capture reserve/deduction, negative-day release and conditional unscheduled repayment through per-disbursement bank details (Europe/UK/US; component library 1.4.0+); mechanisms do not prove booked repayment or debt completion.


- [[source-adyen-docs-capital-get-started]] — 2022-modified, 2026-09-15-captured Capital scoping, component/API-only build, test and separately configured live roadmap with dated prerequisite links.


- [[source-adyen-docs-capital-manage-access]] — 2023-modified, 2026-09-15-captured Capital Customer Area and API credential role guide, including view-only Capital base role, BCL/conditional PCI access and Capital configuration/initiation role descriptions; listed roles do not prove live authorization.


- [[source-adyen-docs-capital-grant-lifecycle-and-status]] — 2026-09-15 Capital grant-initiation/management status reference and API/webhook observation route; its Cancelled/Pending booking boundary conflicts internally, and status definitions do not prove any specific grant or bank receipt.

- [[source-adyen-docs-capital-webhook-types-capital-webhooks]] — 2026-09-15 Capital dynamic/static-offer and grant-status webhook reference separating offer, grant, grant-account and balance-account identifiers from separate fund-transfer booking evidence.



- [[source-adyen-docs-capital-account-structure-resources]] — 2026-01-02-modified Capital resource map for user/legal-entity/transfer-instrument roles, non-funds per-currency grant accounts and per-paid-grant references (captured 2026-09-15).


- [[source-adyen-docs-capital-how-capital-works]] — 2026-09-15 Capital guide to dated eligibility minima, underwritten offers, per-grant Terms, balance-account-first disbursement, fee/repayment structure and pilot subsequent financing.


- [[source-adyen-docs-platforms-compliance-financial-products-user-interface-capital-requirements]] — 2023-modified, 2026-09-15-captured Capital-specific UI guideline for offer/terms/KYC presentation, user insights, security and Ireland precontract notices; dated guidance is not legal advice or funding proof.


- [[source-adyen-docs-capital-integration-checklist]] — 2022-modified, 2026-09-15-captured Capital setup checklist for platform prerequisites, account/credential roles, component versus API-only paths and separate test/live checks; it is not proof of eligibility, accepted terms or disbursement.


- [[source-adyen-docs-capital-manage-user-capabilities]] — 2026-09-15 account-holder getGrantOffers/receiveGrants requirements and requested, allowed, enabled and verification-state management before separate offer/grant steps.


- [[source-adyen-docs-capital-reporting-and-reconciliation]] — 2026-09-15 Capital guide for webhook and balance-platform-report repayment joins, sales-date timing, principal/fee columns and grant-balance confirmation; report rows alone do not establish final debt or bank receipt.


- [[source-adyen-docs-platforms-components-overview-after-payment-capital-component]] — 2026-09-15 Capital Overview/Offer component guide for dated disclosure and eligibility/term/status UI; application, signature and screen state are not grant/debt proof.

- [[source-adyen-docs-capital-capital-components]] — 2026-09-15 Capital Overview/Offer component guide for provider disclosures, supported-region financing screens, variable terms, grant status and term-sheet fields; UI state is not funded-grant or repayment proof.


- [[source-adyen-docs-capital-integration-steps-components]] — 2026-09-15 Capital Overview/Offer component integration guide for account-holder-scoped session role, getGrantOffers prerequisite, versioned UI states/callbacks and balance-account-only component payout path.



- [[source-adyen-docs-capital]] — 2026-09-15 Capital product overview for eligible-user financing, dated regions, proactive offers, volume-linked repayment and child-guide routes.

## Related

- [[adyen-financial-products]] — umbrella product family.
- [[adyen-platforms]] — platform context.
