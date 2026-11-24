---
title: "Stripe Terminal: Configure Custom Splash Screen"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/fleet/splash-screen"
raw_files:
  - "stripe-terminal-splash-screen-2025.md"
tags: [stripe, stripe-terminal, configurations, fleet, splash-screen, readers]
---

## Summary

The 2026-05-01 [[stripe|Stripe]] Terminal guide covers the custom screen shown when a reader is ready to accept payments. Set it per reader type in the Dashboard or Configuration API. A location-specific screen overrides the account default, and locations without one inherit it. The 2026-11-07 capture supplies Dashboard and API variant links. The implementation guidance below comes from May.

## Key Details

**Dashboard** — Select the location and its configuration, edit or override the **Splash screen** row for the exact reader type, upload the image, and save and apply the change. Configure each reader type separately.

**Image requirements** — Use JPG or PNG below 2 MB and crop to the exact reader resolution. Where GIF is supported, use a file below 4 MB. GIFs scale automatically. If an under-limit GIF fails to upload, the guide suggests halving the frame count and repeating as needed.

**Reader resolutions**:

| Reader | Resolution | GIF |
| --- | --- | --- |
| S700/S710 | 1080×1920 | ✓ |
| WisePOS E | 720×1280 | ✓ |
| Verifone P400 | 320×480 | – |
| WisePad 3 | 320×240 | – (PNG only, automatically converted to black and white and slightly repositioned) |

**Splash-screen update timing** — The May guide says the screen updates on SDK connection for mobile readers and within 10 minutes for smart readers.

**Configuration API**

1. Upload the image through the Files API with `purpose: 'terminal_reader_splashscreen'`.
2. Create or update a Configuration with the returned file ID as `splashscreen` under the matching device key (`stripe_s700`, `stripe_s710`, `bbpos_wisepos_e`, `bbpos_wisepad3`, `verifone_p400`). Stripe provisions the account default configuration.

## Related

- [[stripe-terminal-hardware-orders]] — fleet configuration hierarchy and reader-specific settings
- [[stripe-terminal]] — reader features and fleet management

## Raw Sources

- [[raw/stripe-terminal-splash-screen-2025|2026-05-01 custom splash screen guide]] — full Dashboard and Configuration API routes

## Related raw API references

- [[raw/stripe-terminal-fleet-splash-screen-2026-11-07|2026-11-07 custom splash screen variant index]] — navigation to Dashboard and API variants
