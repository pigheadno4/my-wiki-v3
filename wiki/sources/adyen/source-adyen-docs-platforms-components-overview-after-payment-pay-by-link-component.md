---
title: "Adyen Platform Experience Pay by Link components"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/components-overview/after-payment/pay-by-link-component"
raw_files:
  - "adyen/docs/platforms/components-overview/after-payment/pay-by-link-component/2026-09-15.md"
tags: [adyen, platforms, components, pay-by-link, portal]
---

## Overview

This 2026-09-15 Adyen for Platforms guide describes the Platform Experience Pay by Link Overview and Details components for a platform's user portal. They let a user create, view, share, filter, and deactivate payment links, with settings for terms and themes. Features can differ by library version, so the page asks integrators to select a version. The components manage portal interaction and link state; payment processing, split booking and settlement require their own evidence. See [[adyen]], [[adyen-platforms]] and [[adyen-platform-components]].

## Key takeaways

- **Access and setup:** The guide requires an Adyen for Platforms integration, a Balance Platform API key for the Session authentication API, and component roles assigned by Adyen: View, View PII, Manage Links, and Manage Settings for their respective actions. The server creates a scoped POST /sessions token with allowed origin, account-holder resource, roles and product platform; the front end installs or embeds the Platform Experience library and passes a session creation/refresh callback. Live origins require HTTPS. Role and session examples are implementation guidance, not proof that a particular platform has access.
- **Store, terms and expiry:** An account holder needs at least one associated store; the store must be linked to a business line with payByLink or eCommerce sales channel. Store selection is required when creating a link, though one store is auto-selected. The user's terms and conditions URL and compliance confirmation are required before the first link; link details cannot be changed after creation. Links remain searchable in the component list for up to 90 days. User-set expiry can be up to 70 days; absent a setting, the page says 24-hour automatic expiry. The component does not send email automatically.
- **Scope and split boundary:** Overview lists Active/Payment pending and Inactive/Completed/Expired link statuses, with store/date/status/type/reference/ID filters; Details shows link and shopper information and can copy or expire an active link. Payment pending means a started but unconfirmed transaction. Completed describes the link's required payment processing, but is not settlement or beneficiary-funds proof. Existing store split configuration governs how a shopper payment is distributed; without it, the page says all funds go to the liable balance account by default. The component does not change split logic.
- **Customization and version caveats:** Terms and theme are per-store in these components and do not apply to links created through API or Customer Area; merchant/company settings otherwise carry through. Optional fieldsConfig can prefill or lock/hide creation fields, but hidden required fields still validate, and individual address subfields cannot be hidden. The page marks availableTranslations deprecated, gives test as the default environment, and describes package or CDN setup with version-specific SRI hashes. Its screenshots, example session, and callbacks demonstrate UI configuration, not a live payment outcome.

## Detail locators

- Identity, version warning, role matrix and core limitations/setup: pinned raw lines 15-65.
- Overview, link status meanings and filters: pinned raw lines 69-156; Details/actions: lines 158-179.
- Creation steps and immutable link details; terms/theme setup: pinned raw lines 182-235.
- Server session, role policy and origin: pinned raw lines 237-319; library installation and SRI: lines 321-364.
- Initialization, callbacks, deprecated field, environment and component placement: pinned raw lines 366-583.
- Localization, CSS, fieldsConfig validation and supported languages: pinned raw lines 584-863.

## Related

- [[adyen-platform-components]] — Platform Experience component concept and reciprocal source route.
- [[adyen-platforms]] — parent platform context.

## Raw Sources

- [[raw/adyen/docs/platforms/components-overview/after-payment/pay-by-link-component/2026-09-15|Adyen Pay by Link components, captured 2026-09-15]]
