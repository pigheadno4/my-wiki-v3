---
title: "Adyen Marketplace dispute components"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/components-overview/after-payment/disputes-component"
raw_files:
  - "adyen/docs/marketplaces/components-overview/after-payment/disputes-component/2026-09-15.md"
tags: [adyen, marketplaces, platforms, components, disputes]
---

## Overview

This 2026-09-15 Marketplace-path [[adyen]] guide describes the Disputes Overview and Dispute Management [[adyen-platform-components|Platform Experience components]] for a platform user's portal. They show chargebacks, Requests for Information (RFIs), fraud alerts and dispute status, and let an eligible user accept or defend a chargeback with evidence. The components handle the related Adyen API calls, while marketplace chargeback-split configuration remains unchanged (raw lines 25–40, 60–70, 132–167).

## Key takeaways

- **Access and limitations:** An Adyen for Platforms integration and Balance Platform API key with **Disputes Component: Manage** role are required for Session authentication; the Adyen contact assigns that credential role (raw lines 44–56). Account holders can view disputes created in the component on or after May 22, 2025. Action or submitted-defense-document access requires both that the account holder is the sole non-liable account holder referenced by original-payment splits **and** that it received at least one `BalanceAccount` split in the corresponding payment or capture. These are component-access conditions, not general chargeback ownership rules. The page limits documents to 2 MB and listed PDF/image formats, image files to 10 MB and listed image formats, and says refunds are unsupported (lines 52–54).
- **Views and scope:** Overview offers Chargebacks, Fraud alerts and Ongoing & closed tabs for a selected balance account/time period; filters include balance account, opening time, payment method and reason. The time filter uses the selected balance account's timezone and defaults to the last 30 days (raw lines 60–130). Management shows a selected dispute's status, reason/code, dates and references, normally in an Overview modal but optionally on a separate page (lines 132–152). A component display does not change the marketplace's split-chargeback logic (line 70).
- **Action and outcome:** Accepting a chargeback confirms its disputed amount will not return to the balance account. Defending submits a reason and supporting evidence to card schemes for review; it does not guarantee a win (raw lines 148–167). An RFI does not withdraw funds at that stage and need not become a chargeback, whereas a chargeback means funds have been or soon will be withdrawn. `Pending` means the issuer is reviewing a defense; `Won` and `Lost` are later statuses, and some payment-method disputes are never defendable and start/end `Lost` (lines 193–236).
- **Session and version:** The platform backend creates the Session authentication token with `allowOrigin`, `product: platform`, and account-holder-scoped `policy.resources`, then sends the entire session object to the front end for refresh and component initialization. Live `allowOrigin` supports HTTPS only. From library v1.6.0, the session policy must include **Disputes Component: Manage** to let users process disputes (raw lines 240–310). The library's `onSessionCreate` callback refreshes authentication; `onDisputeAccept` and `onDisputeDefend` concern successful component requests, not scheme adjudication (lines 353–503). Version, language, browser and country support must be checked for the integration; `availableTranslations` is deprecated (lines 36–38, 55–56, 355–399, 887–904).
- **Customization:** Optional locale, CSS and `dataCustomization` allow additional fields, icons, links and buttons. Custom keys should start with an underscore, retrieval callbacks should retain received data, and custom translations must be supplied for applicable locales; the detailed field schema and examples are at raw lines 504–904.

## Detail locators

- Credential/access constraints, upload limits and refund exclusion: raw lines 44–56.
- Tab purposes, balance-account timezone/filter values and Management flow: raw lines 60–167.
- RFI/chargeback status and defense boundaries: raw lines 193–236.
- Server Session API, v1.6.0 role, front-end installation/init/callbacks: raw lines 240–503; customization and language table: lines 504–904.

## Evidence boundary

This is a version-dependent embedded UI guide. A session token, rendered dispute, successful defense-submission callback or `Pending` status does not prove a final dispute outcome, returned funds or payout. The access rule depends on specific original-payment/capture splits; the component does not override those split rules. The document/image size wording overlaps for image formats, so apply the relevant upload category and version guidance rather than assuming a universal size for every file (raw lines 52–54). It is separate from Classic Platforms dispute tooling.

## Related

- [[adyen-platform-components]] — parent embedded-component concept.
- [[adyen-platforms]] — modern Marketplace/Platforms model.

## Raw Sources

- [[raw/adyen/docs/marketplaces/components-overview/after-payment/disputes-component/2026-09-15|Pinned Marketplace dispute-component guide, captured 2026-09-15]]
