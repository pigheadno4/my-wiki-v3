---
title: "Adyen Wallets India API-only redirect (historical guide)"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wallets-india/api-only"
raw_files:
  - "adyen/docs/payment-methods/wallets-india/api-only/2026-09-15.md"
tags: [adyen, wallets-india, api-only, redirect, online-payments, historical]
---

## Overview

This [[adyen]] guide, metadata last modified **2019-09-06** and captured 2026-09-15, adds **Wallets India** to an existing merchant-built **API-only/Advanced Web** integration using Checkout API **v68 or later**. It says to add the method in the **test Customer Area** before setup (raw lines 15–26). Its main route is [[adyen-online-payments]]. These historical instructions do not establish current wallet/issuer eligibility, live activation or a completed payment.

## Key takeaways

- The merchant's form shows Wallets India and an issuer list, then passes the shopper-selected **issuer ID** to its server. The four named IDs are **examples**, while `/paymentMethods` is the page's route to the complete available list; it recommends a dynamic form because issuers change and may be offline, with a top-ten-plus-more UI as advice (raw lines 28–49). For method discovery it specifies `countryCode: IN`, `channel: Web/iOS/Android`, and **any supported** `amount.currency` (INR is only the example). The issuer list sits under `paymentMethod.type: wallet_IN` (raw lines 51–57).
- The server `/payments` request is described as carrying `paymentMethod.type: wallet_IN` and **`paymentMethod.issuer` selected by the shopper** (raw lines 59–64). Curl, NodeJS JavaScript, Python and Ruby samples show an issuer (raw lines 68–85, 208–235, 278–305, 308–335), whereas Java, PHP, C#, Go and NodeJS TypeScript samples omit it (raw lines 87–205, 238–275, 338–368). Do not copy an omission as a supported issuerless payment path. The curl request is Checkout TEST **v68**; language samples cite their own library versions and mostly TEST environments, with a note that LIVE needs a live endpoint prefix (raw lines 66–368). This page does not establish cross-version compatibility.
- The illustrative `/payments` response gives `RedirectShopper` plus a redirect `action`; the page says to send the shopper to `action.url` (raw lines 371–389). For mobile, default-browser redirection is **strongly recommended** for compatibility/MFA/app-to-app/error handling; for a GET redirect displayed in an app, it recommends SFSafariViewController or Chrome Custom Tabs instead of WebView (raw lines 389–395). After return, the merchant POSTs URL-decoded `redirectResult` in `/payments/details`; that **example uses TEST v72**, unlike the v68 `/payments` example (raw lines 397–425). A return or sample `Authorised` body is not executed authorization.
- For a returned `/payments/details` result, the page lists **Authorised, Cancelled, Pending/Received, Refused** and says Pending/Received requires the **AUTHORISATION webhook** for the final result (raw lines 428–439). If the shopper never returns, it directs the merchant to the webhook, with `AUTHORISATION success=false/true` examples (raw lines 441–446). The table's “funds in 3 days” for Authorised is a dated provider statement, not evidence of settlement, payout or bank receipt in a specific transaction.
- **TEST conflict:** the page says to add the method in test Customer Area and displays TEST API examples, but its go-live section says “Wallets India currently has no test platform” (raw lines 25–26, 68–85, 397–425, 448–452). Keep this unresolved rather than claiming executable sandbox coverage. Before live acceptance, the page says to request Wallets India in **live Customer Area** (raw lines 448–452); neither request nor a redirect proves enablement or success.

## Detail locators

- API-only minimum v68 and test Customer Area setup: raw lines 15–26.
- Issuer examples, dynamic-list advice and IN/channel/currency discovery fields: raw lines 28–57.
- Server payment fields and versioned language examples, including omitted issuer examples: raw lines 59–368.
- Redirect action, mobile-browser advice, return `/payments/details` TEST v72 illustration: raw lines 371–425.
- Result codes, webhook finality and dated funds claim: raw lines 428–446.
- No-test-platform statement and separate live request: raw lines 448–452.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods]]
- [[source-adyen-docs-online-payments-payments-india-compliance-guide]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/wallets-india/api-only/2026-09-15|Full pinned Wallets India API-only guide]]
