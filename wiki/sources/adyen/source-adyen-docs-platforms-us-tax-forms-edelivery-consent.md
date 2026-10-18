---
title: "Register consent for paperless delivery of tax forms (US only) | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/us-tax-forms-edelivery-consent"
raw_files:
  - "adyen/docs/platforms/us-tax-forms-edelivery-consent/2026-09-15.md"
tags: [adyen, platforms, us-tax-forms, 1099-k, electronic-delivery, consent]
---

## Overview

This [[adyen]] for Platforms guide, captured 2026-09-15, explains how a US platform checks and registers a user's preference for **electronic-only delivery of Form 1099-K** through the Legal Entity Management API. Its stated filing/mail context is US-based users to whom Adyen pays out directly. Consent to paperless delivery transfers electronic delivery and continued-access responsibility to the platform; it is not evidence that a form was filed, generated, delivered or received. See [[adyen-platforms]].

## Key takeaways

- In the page's stated US direct-payout context, Adyen describes filing Form 1099-K with the IRS and printing/mailing it to each associated legal entity's Adyen-registered address. To avoid Adyen print/mail charges for electronic-only delivery, the platform must obtain **express user consent** and register it with Adyen. A consenting platform then provides electronic delivery and ongoing access to the forms when available. The page does not extend this procedure to every US user or to other tax forms. [Raw: lines 19–23, 43, 217]
- The prerequisites are an Adyen for Platforms integration and LEM API key; the page says no webhook is needed for these endpoints. The platform must present the user's preference in its client UI, including rights and continuous-access information under the referenced IRS rules, and comply with applicable electronic-delivery requirements. The IRS link is an external authority route, not proof of current compliance. [Raw: lines 25–41]
- The guide says to check the existing preference **before loading the preferences page**, show it to the user, and call Adyen when the user allows or revokes consent. It describes API-only checking and registration, unavailable through Customer Area. Use the account holder's legal-entity ID: individual legal entity for a sole proprietor, organization legal entity for an organization. [Raw: lines 47–72, 231–244]
- The check endpoint is `POST /legalEntities/{id}/checkTaxElectronicDeliveryConsent`. Its `US1099k` response is a boolean, defaulting to `false`; `true` signifies a registered electronic-delivery preference and the platform's delivery/access responsibility. The registration endpoint is `POST /legalEntities/{id}/setTaxElectronicDeliveryConsent` with `US1099k` in the request; the worked request sets `true`. Although the workflow mentions revocation, this page does not show a `false` registration request or its response. A `200 No Content` in the worked registration indicates that request succeeded, not form delivery. [Raw: lines 68–72, 217–221, 231–266, 458–460]
- To avoid Adyen print/mail charges for a year's electronic-only forms, the page gives a registration deadline of **December 31, 11:59 p.m. Eastern Time in that tax year**. This is a dated provider-document rule; confirm current requirements and tax/legal obligations with authoritative sources before implementation. [Raw: lines 33–45]

## Detail locators

- US direct-payout, mailed-form and platform electronic-delivery scope: raw lines 19–23.
- Platform/LEM credential and no-webhook prerequisites; UI, IRS and deadline: raw lines 25–45.
- Check-before-display, allow/revoke workflow, API-only and legal-entity identity: raw lines 47–72 and 231–266.
- `US1099k` response/default and delivery condition: raw lines 217–221.
- SDK examples are versioned and TEST-environment illustrations: raw lines 76–215 (check) and 268–456 (set); use their own current API references for implementation.
- Registration response and updated UI: raw lines 458–460. The page has an apparent `1009-K` typo at line 49; the title, surrounding text and endpoint field say `1099-K`.

## Related

- [[adyen-platforms]] — platform integration context
- [Provide tax forms (US only)](https://docs.adyen.com/platforms/us-tax-forms) — linked delivery/access guide
- [IRS Publication 1179](https://www.irs.gov/forms-pubs/about-publication-1179) — linked external requirement route, not assessed here

## Raw Sources

- [[raw/adyen/docs/platforms/us-tax-forms-edelivery-consent/2026-09-15|Adyen Platforms US tax-form e-delivery consent — collected 2026-09-15]]
