---
title: "Dynamic financing offers | Adyen Capital"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/get-grant-offers/dynamic-offers"
raw_files:
  - "adyen/docs/capital/get-grant-offers/dynamic-offers/2026-09-15.md"
tags: [adyen, capital, dynamic-offers, grant-offers, financing]
---

## Overview

This [[adyen]] Capital guide, captured 2026-09-15, explains a three-step API flow from a **dynamic amount range** through an informational preliminary calculation to a **static formal offer** for a selected amount and repayment term. Variable 90/180/360-day terms are expressly in a **limited-availability pilot** requiring access through an Adyen contact. These offer states are distinct from Terms of Service acceptance, grant initiation, disbursement and repayment. See [[adyen-capital]].

## Key takeaways

- A Capital-supporting Adyen for Platforms integration, a Balance Platform API key with Capital Configuration and Grant Initiation roles, and the user's `getGrantOffers` capability are listed. The platform must follow Capital compliance guidance and build a UI for selecting an amount within the user's range. The page gives no country list or proof that any specific account holder qualifies or has pilot access. [Raw: lines 19–49]
- `GET /dynamicOffers?accountHolderId=...` can return **up to three** dynamic offers based on processing history, each with its own range and repayment term; `financingType` currently supports `businessFinancing`. The response describes minimum/maximum amount, `startsAt`/`expiresAt`, contract type and estimated/maximum term days. Higher amounts are described as **typically** associated with longer terms, not guaranteed. The selected amount must remain in that user's returned range, though the UI may apply custom increments. A dynamic offer is described as valid for seven days; after expiry a new one is generated only **if the holder still qualifies**, possibly with a changed range. [Raw: lines 24–28, 40–47, 62–101]
- When the user selects an amount/term, `POST /dynamicOffers/{dynamicOfferId}/calculate` uses an amount in minor units and currency matching the dynamic offer. The UI must display preliminary selected amount, daily repayment basis points, 30-day threshold, fees, estimated/maximum term and validity period. This calculation is **informational only and cannot initiate a grant**. The captured rate limit is 120 requests/minute in Test and Live, counting failures. [Raw: lines 156–210]
- After user confirmation, `POST /dynamicOffers/{dynamicOfferId}/grantOffer` with in-range amount and matching currency creates a static offer with definitive terms for UI review; the page calls it a formal, legally binding offer. The returned **static offer ID**, separate from the dynamic-offer ID, is used in the later grant request. This endpoint's captured Test/Live limit is 30 requests/minute including failed requests. A created static offer, or a webhook announcing one, does not prove the user accepted terms, that a grant was approved or that money moved. [Raw: lines 246–301, 338–343, 395–408, 455–467]
- Dynamic and static creation have distinct webhook types and payload grains. The examples are TEST illustrations, not a live user's offer: the static-offer request example submits `EUR 500000` minor units while the displayed response shows `EUR 250000`; do not use that pair as a verified request/response amount mapping. [Raw: lines 271–335, 338–453]

## Detail locators

- Pilot, prerequisites, rates, amount range and seven-day conditional replacement: raw lines 19–49.
- Dynamic-offer GET fields and illustrative TEST range payload: raw lines 51–154.
- Preliminary calculation request/fields, informational boundary and rate: raw lines 156–244.
- Static offer request, definitive terms/ID, rate and inconsistent example amounts: raw lines 246–335.
- Dynamic versus static creation webhooks and separate Terms/grant next steps: raw lines 338–467.

## Related

- [[adyen-capital]] — Capital offer and grant lifecycle context
- [Manage user capabilities](https://docs.adyen.com/capital/manage-user-capabilities) — linked capability prerequisite
- [Capital Terms of Service](https://docs.adyen.com/capital/terms-of-service) — subsequent acceptance route
- [Make grant request](https://docs.adyen.com/capital/make-grant-request/) — subsequent grant/disbursement route

## Raw Sources

- [[raw/adyen/docs/capital/get-grant-offers/dynamic-offers/2026-09-15|Adyen Capital dynamic financing offers — collected 2026-09-15]]
