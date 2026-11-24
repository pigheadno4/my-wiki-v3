---
title: "Stripe Terminal: Manage Locations and Zones"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/fleet/locations-and-zones"
raw_files:
  - "stripe-terminal-locations-and-zones-2025.md"
tags: [stripe, stripe-terminal, locations, zones, fleet, connect, connection-token]
---

## Summary

The May 1, 2026 guide describes creating and administering Terminal Locations and optional zones through its combined Dashboard and API variants. The November 7 capture is an index with Dashboard and API links. Operational details below come from the May capture.

## Locations and Zones (May 2026)

Register each reader to a Location before accepting payments. Multiple readers can share a Location. In the Dashboard, provide a name and a valid address so the reader uses the region’s configuration. A Location’s country is fixed after creation. For a different country, create a new Location and re-register the affected readers.

Dashboard zones are optional and can nest. A Location can belong to one zone at most. The May API variant supports creating and updating Locations and directs zone creation and modification to the Dashboard.

**Dashboard deletion prerequisites.** Remove associated readers before deleting their Location. To delete a zone, first clear the Locations under it. The guide allows moving Locations with readers to another zone. When deleting a Location as part of that cleanup, remove its readers first. See May raw lines 80–95.

## Required Address Fields (May 1, 2026)

The country groups and Beta labels below are from May raw lines 25–30. The November variant index supplies no updated country or Beta status.

| Required fields | Countries named by the guide |
| --- | --- |
| `line1`, `city`, `state`, `postal_code`, `country` | Australia, Canada, Italy, Japan (Beta), Spain, United States |
| `line1`, `city`, `postal_code`, `country` | Austria, Belgium, Czech Republic, Denmark, Estonia (Beta), Finland, France, Germany, Hungary (Beta), Latvia (Beta), Liechtenstein (Beta), Lithuania (Beta), Luxembourg, Malaysia, Netherlands, New Zealand, Norway, Poland (Beta), Portugal, Romania (Beta), Slovakia (Beta), Sweden, Switzerland, United Kingdom |
| `line1`, `postal_code`, `country` | Bulgaria (Beta), Croatia (Beta), Cyprus (Beta), Ireland, Malta (Beta), Singapore, Slovenia (Beta) |
| `line1`, `country` | Gibraltar (Beta) |

## Connect and Connection Tokens (May 2026)

- **Direct charges.** Create the Location with `Stripe-Account`. Only the connected account authenticated in the request can access these Locations.
- **Destination charges.** The platform owns the Locations. A platform can store an optional connected-account reference in Location `metadata` when it needs the association.
- **ConnectionToken.** The optional server-side `location` parameter scopes the token to smart readers assigned to that Location. Omitting it applies no Location filter. The parameter has no effect on Bluetooth reader discovery. The reader registration requirement remains separate.

## Related Pages

- [[stripe]] — company page
- [[stripe-terminal#Locations|Stripe Terminal Locations]] — physical sites and reader grouping
- [[source-stripe-terminal-register-readers]] — reader registration to a Location

## Raw Sources

- [[stripe-terminal-locations-and-zones-2025]] — May 1, 2026 full webpage, including Dashboard workflows and Node.js API examples

## Related raw API references

- [[raw/stripe-terminal-fleet-locations-and-zones-2026-11-07|November 7, 2026 Dashboard and API variant index]] — navigation to separately linked variants
