---
title: "Adyen partner API application information"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/partners/application-information"
raw_files:
  - "adyen/docs/partners/application-information/2026-09-15.md"
tags: [adyen, partners, application-info, api, integration-metadata]
---

## Overview

This 2023-08-17-last-modified, 2026-09-15-captured page describes **`applicationInfo` metadata in Adyen API requests** from technology partners and service partners/system integrators. “Application information” here means product or integrator identity sent with requests, **not** a partner-program application form or approval review. Adyen says the metadata supports payout tracking, performance insights, operational support and understanding partnership type. See [[adyen-partners]] and [[adyen]].

## Key takeaways

- **Where and why:** The page says partners are required to include `applicationInfo` in API requests, giving Checkout `/payments`, `/sessions` and in-person IPP requests as examples. It warns that omitting the metadata limits Adyen's troubleshooting support. These examples do not themselves specify endpoint required-property validation, prove a partner is approved, grant merchant-account permissions or establish payment/payout results.
- **Role-dependent identity:** A **technology partner** owns the branded product/platform used by merchants or other partners; its table marks `applicationInfo.externalPlatform.name` required and `applicationInfo.merchantApplication.name` optional. A **service partner or SI** integrates a third-party product for merchants; its table marks `applicationInfo.externalPlatform.integrator` required. The example companies and product names are illustrative, not actual applicant or merchant identities.
- **Value discipline:** The guide lists up-to-40-character values starting with a letter/number and using letters, digits, dashes, underscores and spaces; it says formatting must remain consistent across requests. It recommends optional platform and merchant-application version/name fields. The raw phrase “between up to 40 characters” does not state a clear minimum length, so do not infer one.
- **Ownership boundary:** Partner identification in `applicationInfo` does not make that entity the legal merchant of record, seller, API credential holder, shopper payee or recipient of a particular payout. Those depend on the actual contract, merchant account and payment flow, none of which this page specifies.

## Detail locators

- Lines 15–24: `applicationInfo` purpose and stated operational benefits.
- `## Partnership type`, lines 26–31: technology partner versus service partner/SI definitions.
- `## Send application information`, lines 33–39: object placement, endpoint examples and troubleshooting warning.
- `### Technology partner`, lines 41–94: required platform name, optional merchant-application name and test payment example.
- `### Service partner or system integrator (SI)`, lines 96–149: required integrator name and test payment example.
- `### Field value requirements` and `## Optional application information fields`, lines 151–170: character/consistency rules and recommended optional version fields.

## Related

- [[adyen-partners]] — partner integration concept; partnership application and approval are separate.
- [[source-adyen-docs-partners]] — partner-program landing page and application route.
- [[source-adyen-docs-partners-integration-checklist]] — partner technical readiness checklist.

## Raw Sources

- [[raw/adyen/docs/partners/application-information/2026-09-15|Partner API application information, captured 2026-09-15]]
