---
title: "Marketplace US 1099-K paperless-delivery consent"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/us-tax-forms-edelivery-consent"
raw_files:
  - "adyen/docs/marketplaces/us-tax-forms-edelivery-consent/2026-09-15.md"
tags: [adyen, marketplaces, us-tax-forms, 1099-k, electronic-delivery, consent]
---

## Overview

This 2026-09-15 [[adyen]] Marketplace guide describes checking and registering a US user's preference for **electronic-only delivery of Form 1099-K** through Legal Entity Management (LEM) API calls. Its stated context is US-based users to whom Adyen pays out directly. If the user consents to paperless delivery, the marketplace takes responsibility for electronic delivery and continued access when forms become available. A registered preference is not evidence that a form was generated, filed, delivered or received. [[adyen-platforms]]

## Key takeaways

- The captured page describes Adyen filing 1099-K for its US direct-payout users and mailing forms to their legal entities' Adyen-registered addresses. To avoid Adyen's print/mail charges for electronic-only delivery, the marketplace obtains **express user consent** and registers it with Adyen. The stated registration cutoff is **December 31 at 11:59 p.m. Eastern Time in the relevant tax year**. These are dated provider statements, not current tax-law or filing determinations. See raw lines 19–23 and 33–45.
- Preconditions are an Adyen for Platforms marketplace integration and LEM API key; no webhook is needed for the described endpoints. The marketplace must provide a client preference UI with rights/continued-access information and handle electronic form delivery and access. The linked IRS Publication 1179 is an external rules route, not a compliance finding here. See raw lines 25–43.
- The workflow checks the existing setting before loading the preferences page, displays it, then calls Adyen when the user allows or revokes consent. Both check and registration are API-only, unavailable through Customer Area. Use the account holder's legal-entity ID: the owner's individual legal entity for a sole proprietorship or the organization entity for an organization. See raw lines 47–72 and 231–244.
- Check with `POST /legalEntities/{id}/checkTaxElectronicDeliveryConsent`; the `US1099k` response boolean defaults to `false`, while `true` means the marketplace owes electronic delivery/access. Register with `POST /legalEntities/{id}/setTaxElectronicDeliveryConsent`; the worked request sets `US1099k: true`. The narrative mentions revocation but does not show a `false` registration request. A `200 No Content` response is described as successful registration, not proof of form delivery. See raw lines 68–72, 217–221, 231–266 and 458–460.
- The step introduction contains an apparent `1009-K` typo; the title, surrounding statements and `US1099k` field identify the intended 1099-K route. The examples use a TEST endpoint and versioned SDKs, not live filing or delivery evidence. See raw lines 47–49, 76–215 and 268–456.

## Detail locators

- **Direct-payout tax-form and delivery-responsibility scope:** raw lines 15–23.
- **Integration, credentials, no-webhook statement, UI/rights and dated deadline:** raw lines 25–45.
- **Check-before-display workflow and legal-entity ID:** raw lines 47–72 and 231–244.
- **Check response, default, set request and registration result:** raw lines 217–266 and 458–460.
- **TEST/versioned examples:** raw lines 76–215 and 268–456.

## Related

- [[adyen-platforms]]
- [[source-adyen-docs-platforms-us-tax-forms-edelivery-consent|Parallel Platforms-path consent guide]]
- [Provide tax forms (US only)](https://docs.adyen.com/marketplaces/us-tax-forms) — linked delivery guide

## Raw Sources

- [[raw/adyen/docs/marketplaces/us-tax-forms-edelivery-consent/2026-09-15|Adyen Marketplace US e-delivery consent guide — collected 2026-09-15]]
