---
title: "Adyen Docs: Live endpoints"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/live-endpoints"
raw_files:
  - "adyen/docs/development-resources/live-endpoints/2026-09-15.md"
tags: [adyen, api-access, live-endpoints, environments, networking]
---

## Overview

This unversioned [[adyen]] documentation snapshot explains the test-versus-live endpoint structure for online payments, how to obtain and use a company-specific live URL prefix, and the extra configuration required for location-based live endpoints. It also records Adyen's MTU and connection-keepalive recommendations.

The page is endpoint and network configuration guidance, not proof of current account eligibility, endpoint availability, correct production configuration, request acceptance, or successful payment execution.

## Key takeaways

- API endpoints differ between test and live accounts and also depend on whether requests use SOAP, JSON, or FORM. Live endpoints are provisioned automatically and are shown with configured data centres and prefixes under **Developers** > **API URLs** in the live Customer Area.
- The documented URL templates distinguish Checkout API from Classic Payments API. Their live forms use a company-specific prefix; the page says libraries and plugins must receive that live URL prefix for live transactions. Each company account receives a unique hostname, which Adyen describes as enabling merchant-specific routing and alternative routing during infrastructure problems.
- Location-based live endpoints require contacting Adyen Support. For Drop-in or Components, web integrations that load client-side scripts and stylesheets must use a region-specific resource URL matching the endpoint region, and the component `environment` must also match that region when going live.
- The stated prerequisites are an online-payments integration, the roles required by the APIs in use, a live account, a live-environment API key, and the go-live checklist. This snapshot does not establish that any particular account has those prerequisites.
- Adyen strongly recommends an MTU of 1500 bytes for network interfaces connecting to its endpoints because larger values can cause connectivity and stability problems. For persistent HTTP connections, it says to enable both TCP and HTTP keepalive; inactive keepalive connections time out after 60 seconds, so it recommends a shorter client-side HTTP keepalive timeout, for example 30 to 50 seconds.

> [!warning] Environment and region boundary
> Do not substitute a test endpoint, generic hostname, or unmatched regional client configuration for the live endpoint and prefix shown for the company account. Location-specific setup, current API versions, credential permissions, production readiness, and observed request outcomes require their own verification.

> [!warning] Snapshot version conflict
> Raw line 62 labels its example as Checkout API v69, while the displayed URL path uses `/checkout/v72/payments`. The snapshot does not resolve which version was intended; verify the intended API version and production URL for the current integration and company account rather than normalizing either value.

## Detail locators

- **Endpoint purpose, environment and data-format distinction:** raw lines 15-25.
- **Online-payments, role and live-setup prerequisites:** raw lines 27-37.
- **Where live endpoints, data centres and prefixes appear:** raw lines 39-43.
- **Location-based endpoint enablement and matching web-resource and component environments:** raw lines 45-52.
- **Live URL prefix composition, Customer Area route, and unresolved v69 label versus v72 URL path in the example:** raw lines 54-62.
- **Checkout and Classic Payments test/live endpoint templates:** raw lines 64-86.
- **Company-specific hostname and routing rationale:** raw lines 88-90.
- **MTU recommendation:** raw lines 92-94.
- **TCP and HTTP keepalive plus timeout behavior:** raw lines 96-107.

## Related

- Company: [[adyen]]
- Concept: [[adyen-api-access]]

## Related raw API references

- [[raw/adyen/docs/development-resources/api-credentials/roles/2026-09-15|API credential roles]]
- [[raw/adyen/docs/online-payments/web-best-practices/2026-09-15|Web best practices]]
- [[raw/adyen/docs/online-payments/build-your-integration/sessions-flow/2026-09-15|Sessions flow]]
- [[raw/adyen/docs/online-payments/build-your-integration/advanced-flow/2026-09-15|Advanced flow]]

## Raw Sources

- [[raw/adyen/docs/development-resources/live-endpoints/2026-09-15|Adyen Docs — Live endpoints (2026-09-15)]]
