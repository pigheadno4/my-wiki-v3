---
title: "Stripe Terminal: Hardware Orders and Returns"
type: concept
category: technology
tags: [stripe, stripe-terminal, hardware, fleet, orders, returns, api]
---

## Definition

Stripe sells pre-certified Terminal readers directly via the Dashboard or Hardware Orders API. Readers come loaded with Stripe payment applications and encryption keys. Orders can be placed, tracked, and returned through the Dashboard or API.

## Ordering

- **Dashboard**: Terminal → Shop; up to **10,000 units per order**
- **Hardware Orders API**: preview, in public preview (requires Account Manager + monthly invoice billing)
- Pricing varies by country; view in Dashboard or stripe.com/terminal/devices
- Volume discounts: contact sales
- Connect platforms can ship directly to connected account addresses

## Order Statuses

| Status | Meaning |
| --- | --- |
| Pending | Received; cancelable for at least 30 minutes |
| Ready to ship | Preparing; no longer cancelable |
| Shipped | Tracking available |
| Delivered | Delivered |
| Canceled | Canceled |
| Undeliverable | Could not be delivered |

## Shipping

- Physical addresses only (no PO boxes)
- Standard/express/priority options by country
- Freight auto-selected for large quantity orders
- Cutoff times vary by country (US: 11am ET, EU: 11am CET, APAC: 11am AET, JP: 3:30pm JST)
- Signature required above country-specific thresholds (e.g. 500 USD in US, 400 EUR in most EU)

## Self-Service Returns (33 countries)

Available in: AT, AU, BE, BG, CA, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GI, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK, US.

- 30-day window from purchase; original packaging + accessories required
- Shipping fees refunded on **first return only** (subsequent returns: 0 shipping refund)
- Refund: up to **10 days** for credit cards after package received at Stripe distribution facility
- Flow: Hardware Orders → select order → Return items (available on Shipped or Delivered orders)
- Outside supported countries: click Contact support on the order page

## User Permissions

| Action | Admin/Dev/Analyst/Terminal Specialist | Support Specialist | View Only |
| --- | --- | --- | --- |
| Place/cancel orders | ✓ | ✗ | ✗ |
| View orders | ✓ | ✓ | ✓ |
| Self-service return | ✓ | ✓ | ✗ |

## Hardware Orders API (Preview)

Beta header required: `Stripe-Version: 2026-04-22.dahlia;terminal_hardware_orders_beta=v5`

**Flow**: retrieve SKUs (`/v1/terminal/hardware_skus?country=US`) → retrieve shipping methods → (optional) preview → create order.

- SKUs and shipping methods are country-specific and can become `unavailable` — query dynamically, don't hardcode
- Preview endpoint validates order and shows tax totals without creating it
- International phone numbers: escape `+` as `%2B`
- Monthly invoices during preview; email configurable in Dashboard

**Webhooks**: `terminal.hardware_order.created`, `.canceled`, `.ready_to_ship`, `.shipped`, `.delivered`, `.undeliverable`

**Test helpers** (sandbox only): `/v1/test_helpers/terminal/hardware_orders/:id/mark_ready_to_ship`, `/ship`, `/deliver`, `/mark_undeliverable`

**API version**: v5 (current); v1–v3 deprecated. v4 added `ready_to_ship` status and preview endpoint.

## Tax

- Tax IDs configurable in Terminal settings; applied to hardware orders
- Non-US orders generate tax invoices (viewable in hardware orders section)
- Italian tax invoices: Italian Tax Portal

## Configurations

Terminal Configuration objects control reader settings (splash screen, tipping, offline mode, etc.) in a two-level hierarchy:

- **Account level**: default, applies to all readers fleet-wide
- **Location level**: overrides account default for readers at that location

Locations inherit account defaults unless overridden. Changes propagate within **10 minutes**. Zone-level configurations are in private preview.

API: `configurations.list({ is_account_default: true })`, `configurations.create(...)`, `locations.update(locationId, { configuration_overrides: 'tmc_...' })`. Deleting a location config reverts it to the account default.

See [[source-stripe-terminal-configurations]] for full Dashboard flows and API samples.

**Admin menu passcode**: default is `07139` (change it). Same account→location hierarchy. 5-digit numeric only; 10-min propagation. API field: `reader_security[admin_menu_passcode]`. View: Super Admin/Admin/Terminal Specialist/Developer; Modify: Super Admin/Admin/Terminal Specialist. See [[source-stripe-terminal-admin-menu-passcode]].

## Reader Registration

Readers must be registered to a Location before accepting payments. Any user with write permissions can register.

**Smart readers** — 3 methods:

| Method | Physical reader required | Batch limit | Constraint |
| --- | --- | --- | --- |
| Registration code (pairing code) | Yes | 1 | None |
| Serial number | No | 10 | Must be ordered by the account |
| Order number | No | All in order | Must be ordered by the account/sub-accounts |

**Mobile readers** (M2, Chipper 2X BT, WisePad 3): register at SDK connect time via `locationId` in `BluetoothConnectionConfiguration`. Can reuse `reader.locationId` for last-used location.

See [[source-stripe-terminal-register-readers]] for full Dashboard flows and code samples.

## Warranty

- **Coverage**: 1-year limited warranty on Terminal readers; excludes cables and accessories
- **Readers**: claim via Dashboard (Readers → overflow menu → Start warranty claims); enter serial number(s), upload images/description, submit with shipping address
- **Docks**: claim via Stripe Support (not Dashboard)
- **Review**: within 48 business hours; one shipping address per claim (submit multiple claims for multiple locations)
- **Replacement warranty**: carries over remaining period; minimum 3 months if less than 3 months remain

See [[source-stripe-terminal-warranty-claims]] for full claim flow.

## Sources

- [[source-stripe-terminal-order-and-return-readers]] — primary source: ordering, statuses, returns, shipping table, permissions, Hardware Orders API
- [[source-stripe-terminal-warranty-claims]] — warranty: 1-year coverage, claim flow, replacement warranty carryover
- [[source-stripe-terminal-register-readers]] — reader registration: 3 smart reader methods, mobile reader locationId at connect time
- [[source-stripe-terminal-configurations]] — configurations: hierarchy (account→location), 10-min propagation, API CRUD, zone preview
- [[source-stripe-terminal-admin-menu-passcode]] — admin menu passcode: default 07139, change for security, same hierarchy, view/modify permission tiers
- [[source-stripe-terminal-splash-screen]] — splash screen: per-reader-type, image specs (JPG/PNG <2MB, GIF <4MB), resolutions table, WisePad 3 PNG/B&W only, Files API upload flow
- [[source-stripe-terminal-offline-mode-config]] — offline mode configuration: enable/disable via Configuration object, 10-min propagation
- [[source-stripe-terminal-reboot-time]] — reboot time window: default midnight, custom window via `reboot_window`, staggered reboots, crosses-midnight logic
- [[source-stripe-terminal-tipping-config]] — on-reader tips configuration: 3 tip types, `tipping.{currency}` API field, smart_tip_threshold, 10-min propagation
- [[source-stripe-terminal-wifi-config]] — WiFi network config: remote push to smart readers, 3 security types, no credential validation, EAP-TLS via Files API
- [[source-stripe-terminal-cellular-config]] — cellular config: S710 only, WiFi fallback, monthly billing if enabled any time, `cellular.enabled` API field
- [[source-stripe-terminal-monitor-readers]] — monitor readers: Dashboard readers list, smart reader health/connectivity details, 30-day event log (public preview)
