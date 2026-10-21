---
title: "Adyen Marketplaces onboarding versions and v2-to-v4 update"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/onboard-users/onboarding-versions"
raw_files:
  - "adyen/docs/marketplaces/onboard-users/onboarding-versions/2026-09-15.md"
tags: [adyen, marketplaces, platforms, onboarding, versioning, verification]
---

## Overview

This 2025-modified, 2026-09-15-captured **Marketplaces / Adyen for Platforms** guide explains onboarding versions spanning Legal Entity Management (LEM) API, Hosted onboarding and KYC checks, then gives **v2-to-v4** update steps for hosted and API-only onboarding. It recommends updating but says immediate update is not required and describes advance notice before a version sunset. The page contains an unresolved **v4-versus-v3 latest-stable wording conflict**, so its version claims are dated source statements, not a current-version determination. [[adyen-platforms]]

## Version and sunset boundaries

- A new onboarding version can contain breaking changes in LEM API, Hosted onboarding or KYC checks, and need not change all three. The page calls some newly required existing data points and verification-error strings **non-breaking**, while a breaking API change gets a new LEM version. It says API changes are backward but not forward compatible. See [[raw/adyen/docs/marketplaces/onboard-users/onboarding-versions/2026-09-15|raw lines 19–47]].
- Older versions may remain usable without new updates until a sunset. The page says Adyen gives approximately **6–12 months** notice before sunset; after a specified LEM API sunset date, that version is unusable. Both API-only and hosted integrations must update before their API version sunsets. Release candidates are preview API-only and subject to change. See [[raw/adyen/docs/marketplaces/onboard-users/onboarding-versions/2026-09-15|raw lines 31, 51–67]].
- The top calls **v4** the latest stable onboarding version (raw line 19) and the update steps use LEM **v4** (raw lines 69–77); a later hosted-only sunset paragraph calls **v3** the latest stable (raw line 67). The capture does not reconcile this conflict.

## v2-to-v4 migration

- Updating involves Adyen-contact discussion, a server move to LEM v4, feature review, testing and a separate go-live step. For users onboarded in an older version, newly available verification deadlines do **not** automatically attach to capabilities already invalid there; ToS acceptance is described as backfilled, but new capability requests require additional ToS documents. Version update alone does **not immediately trigger** new verification checks; the page says those start when a user changes data or has a required data review. See [[raw/adyen/docs/marketplaces/onboard-users/onboarding-versions/2026-09-15|raw lines 69–88]].
- Hosted onboarding built on LEM v2 continues there until the integration update, after which it automatically uses LEM v4. Hosted and API-only implementations must handle required-review notifications, verification deadlines, new error/webhook shape, required data and validation changes, business-line `service` replacing deprecated `capability`, and source-of-funds inputs for issuing/business accounts. The API-only list also points to transfer-instrument changes and optional components. See [[raw/adyen/docs/marketplaces/onboard-users/onboarding-versions/2026-09-15|raw lines 90–146]].
- `sendToTransferInstrument` verification is described at **both transfer-instrument and associated legal-entity levels**. The hosted section says a verified instrument can work independently of another instrument’s verification state; the API-only section qualifies that user capability status appears only at legal-entity level until a data update or required review. These statements are specific to the migration descriptions and do not prove a given transfer can execute. See [[raw/adyen/docs/marketplaces/onboard-users/onboarding-versions/2026-09-15|raw lines 102–104, 128–130]].
- The page asks teams to contact Adyen to enable all new features in **TEST**, then test major integration features and error handling before go-live (raw lines 148–150). This is preparation, not proof of live activation, KYC approval or financial outcomes.

## Transfer-instrument wording conflict

This update guide says the new `/transferInstruments` **`type` field** specifies IBAN versus local account (raw line 134). The separately pinned [[source-adyen-docs-marketplaces-manage-transfer-instruments|Marketplaces transfer-instrument guide]] says the top-level `type` is **`bankAccount`** and bank-location-specific identification is inside `bankAccount.accountIdentification` ([[raw/adyen/docs/marketplaces/manage-transfer-instruments/2026-09-15|related raw lines 52–58, 72–76]]). These captured descriptions do not identify one unambiguous versioned request shape; use the matching LEM API Explorer operation/version before implementation.

## Detail locators

- Version model, compatibility, release candidates and sunset: [[raw/adyen/docs/marketplaces/onboard-users/onboarding-versions/2026-09-15|raw lines 19–67]].
- Update steps, older-user deadlines/ToS and delayed verification reruns: [[raw/adyen/docs/marketplaces/onboard-users/onboarding-versions/2026-09-15|raw lines 69–88]].
- Hosted versus API-only v4 work and TEST enablement: [[raw/adyen/docs/marketplaces/onboard-users/onboarding-versions/2026-09-15|raw lines 90–150]].

## Related

- [[adyen-platforms]] — modern Platforms onboarding and verification context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/onboard-users/onboarding-versions/2026-09-15|Marketplaces onboarding versions (captured 2026-09-15)]]
