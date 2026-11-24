---
title: "Stripe Terminal: Configurations Overview"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/fleet/configurations-overview"
raw_files:
  - "stripe-terminal-configurations-2025.md"
tags: [stripe, stripe-terminal, configurations, fleet, locations, splash-screen, tipping]
---

## Summary

The Terminal Configuration object controls reader settings such as splash screens, tipping and offline mode. The May 1, 2026 capture contains a combined Dashboard and API guide. The November 7 capture provides links to the two variants.

## Configuration Hierarchy (May 2026)

Stripe provisions an account default for the fleet. A Location configuration overrides individual settings for readers there, and every setting without a Location override inherits the account default. The default cannot be applied directly to a Location. May describes zone configuration as a private preview. Dashboard or API changes could take up to ten minutes to reach target readers in the May guide.

## Dashboard Operations (May 2026)

Use **Manage locations** to edit the account’s default configuration or create, edit and delete a local configuration. The May **Delete an existing configuration** workflow says deleting a local configuration through the Dashboard returns that Location’s readers to their account defaults within ten minutes (May raw lines 81–94).

## API Operations (May 2026)

- **Account default lookup.** The prose links to Retrieve, but the worked example calls `configurations.list({ is_account_default: true })`. The separate November List reference documents the optional `is_account_default` filter. The Retrieve reference describes retrieval of a single Configuration object. See May raw lines 100–112 and the November List reference lines 41–42.
- **Create and assign.** The example creates a Configuration and sets the object ID in the Location’s `configuration_overrides` using `locations.update`. See May raw lines 114–143.
- **Update and delete.** The May API variant gives separate `configurations.update` and `configurations.del` operations. The separate November API Delete reference documents deletion of one Configuration, with reader fallback timing left unspecified. See May raw lines 145–174 and the November Delete reference lines 5–7 and 24–41.

## Related Pages

- [[stripe]] — company page
- [[stripe-terminal-hardware-orders#Configurations|Terminal Hardware Orders and Configurations]] — fleet configuration context
- [[source-stripe-terminal-locations-and-zones]] — Terminal Location management

## Raw Sources

- [[stripe-terminal-configurations-2025]] — May 1, 2026 full webpage (Dashboard workflows and Node.js examples)

## Related raw API references

- [[raw/stripe-terminal-fleet-configurations-overview-2026-11-07|November 7, 2026 Dashboard and API variant index]] — navigation to separately linked variants
- [[raw/stripe-api-terminal-configuration-list-2026-11-07|November 7, 2026 List Configurations]] — account-default filter, lines 41–42
- [[raw/stripe-api-terminal-configuration-retrieve-2026-11-07|November 7, 2026 Retrieve Configuration]] — single-object lookup, lines 5–7
- [[raw/stripe-api-terminal-configuration-delete-2026-11-07|November 7, 2026 Delete Configuration]] — deletion, lines 5–7 and 24–41
