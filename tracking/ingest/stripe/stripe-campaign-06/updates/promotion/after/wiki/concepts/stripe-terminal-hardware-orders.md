---
title: "Stripe Terminal: Hardware Orders and Returns"
type: concept
category: technology
tags: [stripe, stripe-terminal, hardware, fleet, orders, returns, api]
---

## Definition

Stripe sells pre-certified Terminal readers loaded with its payment applications and encryption keys. Use the Dashboard to place and track orders or initiate eligible returns. The Hardware Orders API preview documents ordering and retrieval. The Dashboard order routes to Stripe Support when self-service returns are unavailable.

## Ordering

- **Dashboard** — Terminal → Shop. The guides specify up to **10,000 of each item in a single order**.
- **Hardware Orders API** — The guides describe sales-assessed preview access. Required conditions include a Stripe Account manager, agreement to monthly invoice billing and acknowledgment of possible timely integration updates.
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

## Self-Service Returns

The 2026-11-07 Dashboard self-service list covers 32 countries: AT, AU, BE, BG, CA, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK, US. It covers eligible Dashboard orders placed and shipped within the listed scope. The 2026-05-01 list had 33 and included `GI`, which remains in the shipping table. Follow the Dashboard order's **Contact support** route when self-service is unavailable.

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

The 2026-11-07 guide documents `Stripe-Version: 2026-10-28.endive;terminal_hardware_orders_beta=v5`. The 2026-05-01 guide used `Stripe-Version: 2026-04-22.dahlia;terminal_hardware_orders_beta=v5`. Configure the matching version on webhook endpoints as described by each guide.

**Flow**: retrieve SKUs (`/v1/terminal/hardware_skus?country=US`) → retrieve shipping methods → (optional) preview → create order.

- Use the `country` filter to retrieve available SKUs and shipping methods, and query availability dynamically. The shipping method must be available in the destination country. All SKUs and shipping methods in an order share a provider.
- Preview endpoint validates order and shows tax totals without creating it
- International phone numbers: escape `+` as `%2B`
- Monthly invoices during preview; email configurable in Dashboard

Both guides list six order-state webhooks: `terminal.hardware_order.created`, `.canceled`, `.ready_to_ship`, `.shipped`, `.delivered`, `.undeliverable`. For accounts with Hardware Orders API preview access, the November guide adds `terminal.hardware_order_device.registered` and `terminal.hardware_order_device.registration_failed` after automatic registration attempts. Their `data.object` is a Hardware Order Device, with device ID, serial number and hardware order relationship for correlation.

**Test helpers** (sandbox only): `/v1/test_helpers/terminal/hardware_orders/:id/mark_ready_to_ship`, `/ship`, `/deliver`, `/mark_undeliverable`

**Preview version** — Both captured guides pair their API version with beta v5 and mark v1–v3 deprecated. The v4 changelog adds `ready_to_ship` and the preview endpoint. It warns of duplicate shipped events when v3 and v4 webhooks run in the same mode and maps v4 `ready_to_ship` to v3 `shipped`.

## Tax

- Tax IDs configurable in Terminal settings; applied to hardware orders
- Non-US orders generate tax invoices (viewable in hardware orders section)
- Italian tax invoices: Italian Tax Portal

## Configurations

Terminal Configuration objects control reader settings (splash screen, tipping, offline mode, etc.) in a two-level hierarchy:

- **Account level**: default, applies to all readers fleet-wide
- **Location level**: overrides account default for readers at that location

The May 2026 configuration guide describes setting-level inheritance from the Stripe-provisioned account default. Dashboard or API changes can take up to ten minutes. The May guide lists zone configuration as private preview. In its Dashboard workflow, deleting a local configuration returns readers to their account defaults within ten minutes. The 2026-05-01 [[source-stripe-terminal-splash-screen|splash-screen guide]] scopes splash updates to SDK connection for mobile readers and up to ten minutes for smart readers.

May API examples use `configurations.list({ is_account_default: true })`, `configurations.create(...)` and `locations.update(locationId, { configuration_overrides: 'tmc_...' })`, and show separate configuration update and deletion operations. The account-default fallback above is documented in the Dashboard workflow.

See [[source-stripe-terminal-configurations]] for full Dashboard flows and API samples.

**Admin menu passcode.** The May 2026 guide recommends a secure custom five-digit numeric passcode for smart readers and describes location overrides of the account default. Its Dashboard steps say Stripe applies a new passcode within 10 minutes. Super Administrator, Administrator and Terminal Specialist can view and modify passcodes in the Dashboard. Developer can view passcodes. The May Configuration API uses `reader_security[admin_menu_passcode]` on create or update. See [[source-stripe-terminal-admin-menu-passcode]] for the dated toggle and inheritance ambiguity and the November Dashboard/API variant index.

## Reader Registration

Readers must be registered to a Location before accepting payments. Any user with write permissions can register.

**Smart readers** — 3 methods:

| Method | Physical reader required | Batch limit | Constraint |
| --- | --- | --- | --- |
| Registration code (pairing code) | Yes | 1 | None |
| Serial number | No | 10 | May documents an order-account condition. November restricts unrelated transfers and distinguishes platform-led registration from connected-account self-registration. See the dated serial-registration conditions in [[source-stripe-terminal-register-readers#Smart Reader Registration Methods]]. |
| Order number | No | Select readers from the order | Order belongs to the account or a connected account. |

The 2026-11-07 [[source-stripe-terminal-order-and-return-readers|hardware orders guide]] documents preregistering eligible smart readers to one Terminal Location per order. The Location remains editable until serial numbers become available. To split an order across Locations, register readers individually by serial number once their numbers become available. The [[source-stripe-terminal-register-readers|reader registration guide]] documents the same-account requirement and automatic registration at fulfillment as Stripe assigns serial numbers. It also provides the Dashboard flows and code samples.

**Mobile readers.** M2, Chipper 2X BT and WisePad 3 register at connect time. The documented iOS and Android variants pass `locationId` in `BluetoothConnectionConfiguration`. React Native passes it to `connectReader`. Reuse `reader.locationId` from discovery for the last Location.

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
- [[source-stripe-terminal-register-readers]] — May and November 2026 guides for smart-reader registration, Connect permissions, order pre-registration and SDK-specific mobile Location assignment.
- [[source-stripe-terminal-configurations]] — May 2026 account and Location hierarchy, Dashboard and API operations, propagation and zone preview. November links Dashboard and API variants.
- [[source-stripe-terminal-admin-menu-passcode]] — May 2026 smart-reader passcode hierarchy, Dashboard roles and timing, toggle ambiguity and Configuration API field, plus the November Dashboard/API index.
- [[source-stripe-terminal-splash-screen]] — splash screen: per-reader-type, image specs (JPG/PNG <2MB, GIF <4MB), resolutions table, WisePad 3 PNG/B&W only, Files API upload flow
- [[source-stripe-terminal-offline-mode-config]] — May 2026 guide for toggling offline mode in Dashboard and applying the location changes, or configuring it through the API. The Dashboard guide gives a reader-setting propagation bound of 10 minutes.
- [[source-stripe-terminal-reboot-time]] — May 2026 guide for the midnight default, staggered reboots within the registered location's local window, and distinct `reboot_window` hours from 0 through 23. A higher start hour schedules the end on the next day.
- [[source-stripe-terminal-tipping-config]] — on-reader tips configuration: 3 tip types, `tipping.{currency}` API field, smart_tip_threshold, 10-min propagation
- [[source-stripe-terminal-wifi-config]] — May 2026 smart-reader WiFi setup, including user network selection, three security types, no credential validation at configuration time and EAP-TLS via Files API. The November capture indexes the Dashboard and API variants.
- [[source-stripe-terminal-cellular-config]] — May 2026 fleet cellular settings for S710, including Location activation, `cellular.enabled` and per-reader calendar-month billing, plus the November Dashboard/API index.
- [[source-stripe-terminal-monitor-readers]] — monitor readers: Dashboard readers list, smart reader health/connectivity details, 30-day event log (public preview)
