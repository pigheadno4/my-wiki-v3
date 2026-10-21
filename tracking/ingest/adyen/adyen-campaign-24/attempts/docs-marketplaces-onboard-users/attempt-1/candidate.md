---
title: "Adyen Marketplaces: Onboard and verify users"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/onboard-users"
raw_files:
  - "adyen/docs/marketplaces/onboard-users/2026-09-15.md"
tags: [adyen, marketplaces, platforms, onboarding, verification]
---

## Overview

This 2024-modified, 2026-09-15-captured **Marketplaces / Adyen for Platforms** page compares **Hosted onboarding** with **API-only onboarding** for collecting user verification information. The user’s legal-entity type and operating country determine required data; collection timing depends on the verification type, and Adyen starts verification after receiving information. Neither UI completion nor resource creation on this page establishes completed verification or enabled payment/payout capabilities. [[adyen-platforms]]

## Onboarding routes

- In **Hosted onboarding**, Adyen hosts the user-facing flow and UI while the marketplace makes Legal Entity Management API and Configuration API calls to create and customize required resources. The hosted page includes an Adyen Terms of Service acceptance step. The listed entity types are Organization, Individual, Sole proprietorship and **Trust only in Australia/New Zealand**. See [[raw/adyen/docs/marketplaces/onboard-users/2026-09-15|raw lines 31–50]].
- Hosted onboarding has its own **dated operating-country list** (raw lines 52–94). The optional instant-bank-account verification path is narrower still: availability is limited by the country **and** Individual/Organization matrix at raw lines 96–127. The described bank-login flow is a conditional feature, not proof a particular user’s bank account is verified. See [[raw/adyen/docs/marketplaces/onboard-users/2026-09-15|raw lines 52–127]].
- Hosted ID-document autofill and organization decision-maker guidance/invites are stated as **onboarding v3 or v4** features. Autofill accepts ID documents with **Latin characters**; users confirm extracted details before submission. Decision-maker invite asks the added person to provide their own verification information through an emailed link. These steps do not themselves mean a decision-maker passed checks. See [[raw/adyen/docs/marketplaces/onboard-users/2026-09-15|raw lines 135–166]].
- In **API-only onboarding**, the marketplace builds the UI, collects user data, and submits it using LEM and Configuration APIs. The page says this route can onboard users in Adyen for Platforms’ supported countries/regions. An optional Onboarding component can collect data and create the relevant resource, removing the need for the marketplace to make that particular resource-creation API call itself. See [[raw/adyen/docs/marketplaces/onboard-users/2026-09-15|raw lines 168–172]].

## Scope boundary

The `Requirements` heading says a base Adyen for Platforms integration has no additional requirements, limitations or preparations (raw line 29); the same page still requires collection of country/entity/verification-type-dependent user information (raw lines 19–25). Read that sentence as an integration-preparation statement, not a waiver of KYC data or proof of verification approval. The two onboarding routes and the instant-bank-verification matrix have different coverage; do not generalize the hosted list to API-only or the instant-bank feature to every hosted user.

## Detail locators

- Verification factors, base-integration wording and Hosted/API-only distinction: [[raw/adyen/docs/marketplaces/onboard-users/2026-09-15|raw lines 15–50]].
- Hosted operating-country list and bank-login verification matrix: [[raw/adyen/docs/marketplaces/onboard-users/2026-09-15|raw lines 52–127]].
- Versioned ID autofill, decision-maker flows and API-only/components route: [[raw/adyen/docs/marketplaces/onboard-users/2026-09-15|raw lines 135–172]].

## Related

- [[adyen-platforms]] — modern Platforms onboarding and capability context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/onboard-users/2026-09-15|Onboard and verify users (captured 2026-09-15)]]
