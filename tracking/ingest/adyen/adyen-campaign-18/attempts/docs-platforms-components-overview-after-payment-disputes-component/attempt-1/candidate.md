---
title: "Dispute components | Adyen Docs"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/components-overview/after-payment/disputes-component"
raw_files:
  - "adyen/docs/platforms/components-overview/after-payment/disputes-component/2026-09-15.md"
tags: [adyen, platforms, components, disputes, chargebacks]
---

## Overview

This 2026-09-15 Adyen for Platforms guide covers the Disputes Overview and Dispute Management Platform Experience components for a platform's user portal. It describes viewing chargebacks, Requests for Information (RFIs), and fraud alerts, plus accepting or defending eligible chargebacks through a component UI. See [[adyen]], [[adyen-platforms]], and [[adyen-platform-components]].

## Key takeaways

- The Overview component lists disputes for a balance account and period, with Chargebacks, Fraud alerts, and Ongoing & closed tabs, filters, and a Management detail view. The Management component can accept a chargeback or submit a defense reason and evidence; the components make the needed Adyen API calls (raw lines 60–91, 132–167). Displayed state or a successful component request does not by itself prove a final dispute outcome or funds recovery.
- This requires an Adyen for Platforms integration, a Balance Platform API key with **Disputes Component: Manage**, a server-created Session authentication token scoped to the linked account holder and `product: platform`, and client initialization. From library v1.6.0, include that role in the session policy to enable processing disputes (raw lines 44–56, 245–299, 355–502).
- Account holders can view disputes created in this component on or after May 22, 2025. Action or submitted-defense-document access requires both being the sole non-liable account holder in the original payment splits and receiving at least one `BalanceAccount` split in the payment or capture. The page limits document and image sizes/formats and says refunds are unsupported (raw lines 52–56). These are component access boundaries, not a redefinition of underlying dispute or split rules.
- Accepting a chargeback confirms the disputed amount will not return to the balance account. Defending sends evidence to card schemes for review; Pending means issuer review, not a win. An RFI has no funds withdrawn at that stage, while a chargeback means funds have been or soon will be withdrawn. Some payment-method disputes are not defendable and start/end Lost (raw lines 148–152, 193–236).
- Features and guidance depend on the library version; supported countries, browsers, languages, and customization belong to the relevant version/library context. The initialization table marks `availableTranslations` deprecated (raw lines 36–38, 55–56, 355–399, 887–907).

## Detail locators

- Balance-account, time-period, payment-method, and dispute-reason filters: raw lines 93–130.
- Undefended/Accepted/Pending/Won/Lost chargeback states and Unresponded/Responded/Expired RFI states: raw lines 193–236.
- Server Session authentication request and policy, installation, initializers, callbacks, and mounting: raw lines 245–502. `onDisputeAccept` and `onDisputeDefend` indicate successful requests, not final scheme adjudication.
- Optional localization, appearance, custom field data, and supported language list: raw lines 506–907.

## Related

- [[adyen-platform-components]]
- [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/docs/platforms/components-overview/after-payment/disputes-component/2026-09-15|Pinned Adyen dispute components guide]]
