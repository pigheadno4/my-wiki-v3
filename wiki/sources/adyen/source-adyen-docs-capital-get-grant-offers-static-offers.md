---
title: "Static financing offers | Adyen Capital"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/get-grant-offers/static-offers"
raw_files:
  - "adyen/docs/capital/get-grant-offers/static-offers/2026-09-15.md"
tags: [adyen, capital, offers, financing, pilot]
---

## Overview

This 2026-09-15 [[adyen]] Capital guide describes listing, reading and receiving creation webhooks for predefined static financing offers tied to an account holder. It labels variable 90/180/360-day repayment terms **limited-availability pilot** and directs platforms to ask Adyen for access. See [[adyen-capital]] for the product route. An offer object or creation webhook is not proof of user acceptance, grant request approval, disbursement, repayment or present country/account eligibility.

## Key takeaways

- Based on processing history, an eligible user **may** receive up to nine predefined offers with fixed financing amounts and term choices of 90, 180 and 360 days. The variable-term options are described as pilot access requiring an Adyen contact. The guide does not promise nine offers or eligibility for a particular account holder or region. Its sample labels `estimatedDays` as 90/180/360 but shows `maximumDays` of 120/270/450, so distinguish estimated term from loan maximum rather than calling them the same fixed deadline. [Raw: lines 19–24, 66–73, 79–349]
- Prerequisites stated here are a Platforms integration supporting Capital; a Balance Platform API key with both `Balance Platform Capital Configuration` and `Balance Platform Capital Grant Initiation` roles; the user's `getGrantOffers` capability; and adherence to Capital compliance guidance for UI/marketing/processes. Listing roles/capability does not itself prove effective access or approval. Offers are described as valid seven days; after expiry a new offer is generated **if** the account holder still qualifies, with possible amount changes. [Raw: lines 26–37]
- `GET /grantOffers?accountHolderId=...` lists offers for the receiving account holder and also returns static offers created by the dynamic-offers flow. Per-offer fields include offer ID, `startsAt`/`expiresAt`, minor-unit amount/fee, `contractType=loan` in this guide, repayment basis points deducted from incoming net volume, estimated/max term and a minimum 30-day repayment threshold. The JSON numbers and EUR examples are TEST illustrations, not financing terms for another user. [Raw: lines 39–75, 77–352]
- `GET /grantOffers/{id}` retrieves a specified offer, and the `balancePlatform.balanceAccountHolder.capitalOffer.created` webhook announces new static offers with account-holder/offer IDs and terms; an offer must be accepted before `expiresAt`. **Example inconsistency:** the single-offer GET requests ID `0000000000000001` but its shown response has ID `0000000000000003`. Do not use those sample IDs as proof of a successful matching lookup. [Raw: lines 354–468]
- The next-step navigation points separately to Capital Terms of Service acceptance and making a grant/disbursement request. Reading or displaying an offer is earlier than those steps; the captured page does not show executed funding, booked grant or bank receipt. [Raw: lines 470–482]

## Detail locators

- Pilot qualification and high-level offer count/terms: raw lines 19–24.
- Integration, credential roles, capability, expiry/regeneration and compliance prerequisite: raw lines 26–37.
- Account-holder list endpoint and field definitions, including estimated versus maximum term and minor-unit money: raw lines 39–73; TEST example: raw lines 75–352.
- Specific-offer GET ID mismatch: raw lines 354–405.
- Offer-created webhook, acceptance-before-expiry and separate terms/grant next steps: raw lines 408–482.

## Related

- [[adyen-capital]] — Capital offer/grant evidence boundary
- [Dynamic offers](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/) — linked alternate offer flow
- [Capital Terms of Service](https://docs.adyen.com/capital/terms-of-service) — separate acceptance step
- [Make a grant request](https://docs.adyen.com/capital/make-grant-request) — separate funding request step

## Raw Sources

- [[raw/adyen/docs/capital/get-grant-offers/static-offers/2026-09-15|Adyen Capital static financing offers — collected 2026-09-15]]
