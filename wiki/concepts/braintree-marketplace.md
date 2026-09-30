---
title: "Braintree Marketplace"
type: concept
category: technology
tags: [braintree, marketplace, sub-merchants, merchant-accounts]
---

## Overview

Retrieval route for Braintree Marketplace documentation about sub-merchant accounts. The linked sources are collected snapshots; they do not establish current product availability or merchant eligibility. Use each source's raw page for operation details and qualifications.

## Article-level product orientation

- [[source-braintree-marketplace-article-overview]] - article-level route for the marketplace owner/provider model, transaction splitting, service fees, identity-verification orientation, US-domicile and special-approval conditions, incompatibilities, and core terminology; distinct from the developer-guide overview and Node procedures, and not proof of current Marketplace support or merchant eligibility. This article says Marketplace is incompatible with Braintree recurring billing, while [[source-braintree-marketplace-guide-testing-go-live-node]] tells applicable Marketplace integrations to recreate recurring-billing plans or settings in production; the collected documents do not resolve the contradiction, so do not infer Marketplace recurring-billing support.

## Developer-guide orientation

- [[source-braintree-marketplace-guide-overview]] - developer-guide orientation for the Marketplace owner/provider model, US-domicile and special-approval conditions, PayPal/recurring-billing/shopping-cart incompatibilities, core terminology, and routes to onboarding, confirmation, service-fee transaction creation and held-funds guidance; distinct from the article overview and Node operation pages, and not proof of current Marketplace availability or eligibility. This overview's recurring-billing incompatibility conflicts with [[source-braintree-marketplace-guide-testing-go-live-node]], which tells applicable Marketplace integrations to recreate recurring-billing plans or settings in production; the collected documents do not resolve the contradiction, so do not infer Marketplace recurring-billing support.

## Model and onboarding

In the collected Node.js onboarding guide, the master merchant creates a merchant account for each sub-merchant and then confirms its creation. Individual information is always required; a registered company additionally supplies business information while remaining tied to an individual. A valid creation result may still show `pending`, not completed onboarding. The guide says Braintree does not verify bank details and may hold funds after a disbursement exception until those details are corrected. New merchants seeking a Marketplace solution are directed to Sales; this snapshot does not prove current availability or eligibility. [[source-braintree-marketplace-guide-onboarding-node]]

- [[source-braintree-marketplace-guide-confirmation-node]] - Node.js route for the post-verification approval-or-decline webhook confirmation step, returned account-state examples, validation-error navigation, and follow-up boundary; not account-creation, complete-onboarding, or current-availability proof.

Related routes: [[braintree-server-sdk]] for Node gateway integration context and [[braintree-webhooks]] for notification context. Neither substitutes for the onboarding guide's raw page.

## Article-level onboarding

- [[source-braintree-marketplace-article-onboarding]] - article-level route for applicant and business information collection, API rather than Control Panel submission, Braintree verification and status webhook, marketplace support and legal responsibilities, funding-destination qualifications, and merchant-agreement acceptance; distinct from the Node.js procedure and not proof of current Marketplace availability or eligibility.

## Sub-merchant account maintenance

The collected Node.js update guide uses `gateway.merchantAccount.update()` to identify an existing sub-merchant account and submit only the `individual`, `business`, or `funding` attributes being changed; omitted attributes remain unchanged, and a missing account routes to `notFoundError`. Individual details remain required for every sub-merchant, while business details are optional additional information for registered businesses. The funding section controls where Braintree disburses settled funds, but update success does not prove that funds were disbursed. The guide masks sensitive output by returning only the last four digits of SSNs and bank account numbers after successful updates. New merchants seeking a marketplace solution are directed to Sales, so this snapshot does not prove current availability or eligibility. [[source-braintree-marketplace-guide-update-node]]

## Sandbox and production testing

- [[source-braintree-marketplace-guide-testing-go-live-node]] - Node.js route for sandbox sub-merchant confirmation-webhook simulations and separate production credentials, settings, server environment switch, client-token boundary, and limited real-payment production checks. Its recurring-billing instructions conflict with [[source-braintree-recurring-billing-overview]]; do not infer Marketplace recurring-billing support.

## Marketplace transaction processing

- [[source-braintree-marketplace-article-processing]] - article-level route for service-fee allocation, whole-transaction escrow and 30-day guidance, escrow-sensitive refund limits, and master-merchant refund and chargeback responsibility; distinct from generic transaction processing and not evidence of current Marketplace availability or eligibility.

## Transaction creation with service fees

- [[source-braintree-marketplace-guide-create-node]] - Node.js route for creating a transaction attributed to a successfully onboarded sub-merchant, allocating a required service fee to the master merchant, and locating the guide's device-data, held-funds, refund, verification-account and master-account charge constraints; the collected snapshot does not prove current Marketplace availability or merchant eligibility.

## Marketplace funding

The collected funding article says Marketplace transactions should disburse to the master merchant's bank account and the sub-merchant's funding source within 1-3 business days after gateway settlement unless held in escrow, with each party receiving at most one deposit per day. Escrow requires holding and releasing the entire transaction, including service fees; partial disbursements require separate transactions. The bank route accepts only checking accounts. Venmo funding destinations are no longer supported for new merchants, while the described legacy flow gives an unmatched recipient 30 days to create an account and sends no disbursement-exception webhook if the recipient does not act, requiring manual follow-up. The article calls disbursement-exception webhooks the only way a merchant will be notified of sub-merchant disbursement problems and says integrating them into the Marketplace workflow is vital. These webhooks report failures only because banks and Venmo do not confirm successful disbursements; therefore timing, descriptors, and absence of an exception webhook are not proof that an individual deposit arrived. New merchants seeking a marketplace solution are directed to Sales, so this snapshot does not prove current availability or eligibility. [[source-braintree-marketplace-article-funding]]
