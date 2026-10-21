---
title: "Adyen Marketplaces: Manage transfer instruments"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/manage-transfer-instruments"
raw_files:
  - "adyen/docs/marketplaces/manage-transfer-instruments/2026-09-15.md"
tags: [adyen, marketplaces, platforms, transfer-instruments, payouts]
---

## Overview

This 2023-modified, 2026-09-15-captured **Marketplaces / Adyen for Platforms** guide treats a transfer instrument as a resource representing an **external bank account** for funds sent to or received from outside the marketplace. It separates **users’ bank accounts** from the marketplace company’s **payout accounts**, which are transfer instruments connected to its **liable account** for settlement to its own bank. A resource response or valid status is not proof that a payout reached a bank. [[adyen-platforms]]

## API management and verification

- The guide lists Legal Entity Management API and Customer Area credential/role prerequisites. Its requirement table names `Manage LegalEntities via API`, `Balance Platform BCL Legal Entity role`, `Manage account holders & legal entities`, and `Merchant manage bank accounts` for payout-account management. See [[raw/adyen/docs/marketplaces/manage-transfer-instruments/2026-09-15|raw lines 28–46]]. The table is formatting-imperfect, so confirm actual grants before relying on an operation.
- A user transfer instrument is created with `POST /transferInstruments`, `type: bankAccount`, the `legalEntityId` of the entity contractually related to the platform and owning that bank account (the individual owner for a sole proprietorship), and a bank-account object whose identification fields depend on bank location. The example uses a **TEST** Legal Entity Management **v3** endpoint and language-specific SDK versions; later GET/PATCH/DELETE examples use **TEST v4**. These are examples, not live configuration. See [[raw/adyen/docs/marketplaces/manage-transfer-instruments/2026-09-15|raw lines 48–58, 60–341, 377–529, 549–815, 839–985]].
- Creation returns a unique transfer-instrument `id`; the example response shows `sendToTransferInstrument` **requested true, allowed false, verificationStatus pending**. Creation and update instructions both say to inspect `problems` for bank-verification issues. A 200 update response retains the same ID so existing payout schedules and transfers can continue targeting it, but check verification status and actual transfer outcome separately. See [[raw/adyen/docs/marketplaces/manage-transfer-instruments/2026-09-15|raw lines 344–375, 816–837]].
- GET by ID returns bank-account and verification details per the guide; PATCH by ID sends only fields being modified, with bank-location-specific `accountIdentification`. See [[raw/adyen/docs/marketplaces/manage-transfer-instruments/2026-09-15|raw lines 377–559]].

## Versioned `type` wording conflict

The separately pinned [[source-adyen-docs-marketplaces-onboard-users-onboarding-versions|Marketplaces onboarding-versions guide]] says its v4 `/transferInstruments` **`type` field** distinguishes IBAN from a local account (related raw line 134). This management guide instead labels the instrument's top-level `type` **`bankAccount`** (raw lines 52–58), with `usLocal` or `iban` under `bankAccount.accountIdentification.type` in its **TEST v3 create** and **TEST v4 update** examples (raw lines 67–80, 566–577). The two dated pages do not resolve whether the migration sentence names a different field path or a version-specific request shape. Use the API Explorer operation for the exact LEM version before constructing a request; neither example proves a live or verified instrument.

## Deletion and payout-account boundary

- `DELETE /transferInstruments/{id}` is **not undoable**. Re-adding the same bank account requires a **new transfer instrument**, and future scheduled or on-demand payouts that still target the deleted ID **fail**. See [[raw/adyen/docs/marketplaces/manage-transfer-instruments/2026-09-15|raw lines 839–987]].
- Customer Area in this guide manages **only the marketplace’s own payout accounts**, not user transfer instruments. A company payout account is usable when its status is **valid** after verification. For rotation, the guide says to add the replacement first, update managed/custom schedules and on-demand references, verify the new instrument is receiving funds, then delete the old one; edits take effect instantly. See [[raw/adyen/docs/marketplaces/manage-transfer-instruments/2026-09-15|raw lines 989–1018]]. A displayed status or planned rotation does not establish bank receipt.

## Detail locators

- Resource identity, ownership classes, API/Customer Area roles and create inputs: [[raw/adyen/docs/marketplaces/manage-transfer-instruments/2026-09-15|raw lines 15–58]].
- TEST v3 creation examples and pending capability response: [[raw/adyen/docs/marketplaces/manage-transfer-instruments/2026-09-15|raw lines 60–375]].
- TEST v4 GET/PATCH examples, unchanged ID and bank-verification problems: [[raw/adyen/docs/marketplaces/manage-transfer-instruments/2026-09-15|raw lines 377–837]].
- DELETE consequences and company payout-account Customer Area/rotation flow: [[raw/adyen/docs/marketplaces/manage-transfer-instruments/2026-09-15|raw lines 839–1018]].

## Related

- [[adyen-platforms]] — modern Platforms resource and payout context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/manage-transfer-instruments/2026-09-15|Manage transfer instruments (captured 2026-09-15)]]
