---
title: "Classic Platforms legal arrangements verification"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/verification-process/legal-arrangements"
raw_files:
  - "adyen/docs/classic-platforms/verification-process/legal-arrangements/2026-09-15.md"
tags: [adyen, classic-platforms, verification, legal-arrangements, account-holders]
---

## Overview

This Classic Adyen for Platforms guide (last modified 2021-07-27; captured 2026-09-15) describes collection and verification of an account holder's contractual legal arrangement when it conducts business on behalf of another entity. It explicitly directs new implementations to a different integration guide. This page uses the **Classic Account API v6** and Classic account-holder codes; it does not define modern Adyen for Platforms Legal Entity Management API resources. See [[adyen-classic-platforms]] and [[adyen]].

## Key takeaways

- For applicable Classic account holders, the page names association, partnership, sole proprietorship and trust arrangements. The dated support list is association **US for both holder and association**, partnership **Australia/Singapore**, sole proprietorship **Singapore**, and trust **Australia/Singapore**. Except for association, the arrangement's establishment country may differ from the holder's operating country (raw lines 35–60). This is a captured support statement, not current availability or legal advice.
- Hosted onboarding is described as collecting requirements by default. A platform using its own onboarding UI must collect the extra information and send it through **API version 6**. Failing to declare arrangements can lead to **blocked payouts and account suspensions** (raw lines 28–33).
- The UI collects arrangement identity and registration details, plus other associates, partners or trust members as applicable; an Australian trust needs a proving document. The detailed per-type fields and conditional automatic checks are at raw lines 62–128. Adyen may request a proving document if automatic verification fails (raw line 128).
- To send data, update an existing Classic account holder through `POST /updateAccountHolder`, using `accountHolderCode` and `accountHolderDetails.legalArrangements` with arrangement reference, type and relevant entity/member details (raw lines 130–147, 238–252, 343–355, 386–400). Requests are **asynchronous**: the API response is not the final verification result. `ACCOUNT_HOLDER_CREATED`/`ACCOUNT_HOLDER_UPDATED` and `ACCOUNT_HOLDER_VERIFICATION` notifications carry update/check status and Adyen-generated arrangement/entity codes used in later updates or uploads (raw lines 529–534).
- Upload a proving document only for an Australian trust or when automatic verification failed and Adyen required one. The text calls for `CONSTITUTIONAL_DOCUMENT`, the relevant `legalArrangementCode`, and Base64 content; member identity documents may also be required under an `legalArrangementEntityCode`. Upload processing is likewise asynchronous and needs the verification notification for its final result (raw lines 566–601).

## Material source tensions

- The association support rule says both account holder and association must operate and be established in the **US**, and the general rule exempts associations from cross-country establishment (raw lines 55, 60). The association collection tab nonetheless says its establishment country **can differ** from the holder's operating country (raw line 72). Do not infer cross-country association support from that sentence.
- The support list says sole proprietorship is supported in **Singapore** (raw line 57), while its API example uses an **Australian** address (raw lines 343–383). Treat the payload as illustrative, not evidence of Australian support.
- The upload instructions require `legalArrangementCode` (raw lines 575–579), but the shown `/uploadDocument` payload has `accountHolderCode`, type and filename without that code (raw lines 583–597). The sample does not establish that the stated code can be omitted.
- The trust example introduction calls the added members a business settlor and individual protector (raw line 388); the individual payload labels its `legalArrangementMembers` role `Trustee` (raw lines 484–490). Rely on the per-type requirements and actual member role data, not the example caption, for that distinction.

## Detail locators

- Per-arrangement required collection fields and region-specific trust document: raw lines 62–128. The sample request bodies for association, partnership, sole proprietorship and trust occupy raw lines 134–527; their placeholder and test values are not a live onboarding or verification outcome.
- Verification webhooks and generated codes: raw lines 529–564. Conditional document upload and verification notification: raw lines 566–601.

## Related

- [[adyen-classic-platforms]] — Classic platform model and source route.
- [[adyen]] — provider context.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/verification-process/legal-arrangements/2026-09-15|Classic Platforms legal arrangements check, captured 2026-09-15]]
