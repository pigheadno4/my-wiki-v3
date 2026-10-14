---
title: "Show the standby screen | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/display-data/idle-display"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/display-data/idle-display/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, standby-display]
---

## Overview

This Adyen guide shows how a POS can ask a payment terminal to display its **standby screen**, where the merchant's already configured branded logo normally appears when no other process is running. It recommends a predefined `Idle` display message and documents a narrower XHTML alternative. The operation is a Device/Display terminal interaction, not a payment, refund, terminal-logo upload or evidence that the screen stayed visible for a particular duration. [[adyen]] [[adyen-pos-shopper-engagement]] [[adyen-terminal-api]]

## Key takeaways

- The recommended, generic route sends a Terminal API `DisplayRequest` with `MessageClass: Device`, `MessageCategory: Display`, one `DisplayOutput` item for `CustomerDisplay`, `OutputFormat: MessageRef`, and `PredefinedContent.ReferenceID: Idle`. The page says this route works regardless of terminal model. The header table requires a terminal-scoped `ServiceID` of 1–10 alphanumeric characters unique within the last 48 hours; it does not promise safe retry or general idempotency. See **Switch to the standby screen → Generic - PredefinedContent**, pinned raw lines 21–53.
- The alternative uses `OutputFormat: XHTML` and a Base64-encoded XML string in `OutputXHTML`, with the same Device/Display header and one `CustomerDisplay` output item. The guide limits this route to XHTML-accepting **M400, P400 Plus and V400m** terminals. The sample is not an arbitrary logo-image upload or proof of current firmware/model support. See **Limited - OutputXHTML**, pinned raw lines 144–201.
- For the generic route, the guide tells the merchant to inspect `DisplayResponse.OutputResult.Response.Result: Success`; the limited route also names `OutputResult.Response.Result: Success`. These are display-request results. The page does not define a new payment state, screen lifetime, timeout, priority/preemption sequence, logo asset requirements, or account-specific configuration outcome. See pinned raw lines 119–142 and 234–236.
- The JSON and Java blocks illustrate request construction and a V400m `POIID`. Treat their values as examples, not evidence that a specific terminal or merchant account is configured to show a particular branded logo. See pinned raw lines 54–117 and 173–232.

## Detail locators

- **Show the standby screen; Switch to the standby screen** (pinned raw lines 15–27) — standby/logo purpose, recommended model-independent route and limited XHTML model set.
- **Generic - PredefinedContent** (pinned raw lines 29–142) — Device/Display header, single `DisplayOutput`, `MessageRef`/`Idle` values, JSON/Java examples and success result.
- **Limited - OutputXHTML** (pinned raw lines 144–236) — model limitation, XHTML/Base64 XML field, examples and success result.
- **See also** (pinned raw lines 238–242) — separate virtual-receipt, QR and image display guides.

## Related

- [[adyen-pos-shopper-engagement]] — primary shopper-terminal display route.
- [[adyen-terminal-api]] — separate message architecture and financial operation context.
- [[adyen-terminal-management]] — terminal configuration context; this page does not set the logo asset.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/display-data/idle-display/2026-09-15|Adyen standby-screen display guide, fetched 2026-09-15]]
