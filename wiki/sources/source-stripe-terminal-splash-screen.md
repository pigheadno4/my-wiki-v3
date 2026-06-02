---
title: "Stripe Terminal: Configure Custom Splash Screen"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-splash-screen-2025.md"
tags: [stripe, stripe-terminal, configurations, fleet, splash-screen, readers]
---

## Summary

Set a custom default screen per reader type via Dashboard or Configuration API. Same account→location hierarchy as other configurations. Must be configured per reader type — no single image for all types.

## Key Details

**Image requirements**: JPG/PNG < 2MB; GIF < 4MB. Crop JPG/PNG to exact resolution; GIF scales automatically. If GIF fails to upload (even under 4MB), reduce frame count by 50%.

**Reader resolutions**:

| Reader | Resolution | GIF |
| --- | --- | --- |
| S700/S710 | 1080×1920 | ✓ |
| WisePOS E | 720×1280 | ✓ |
| Verifone P400 | 320×480 | – |
| WisePad 3 | 320×240 | – (PNG only; auto black & white) |

**Propagation**: mobile readers → on next SDK connection; smart readers → within 10 minutes.

**API flow**:
1. Upload image via Files API: `files.create({ purpose: 'terminal_reader_splashscreen' })`
2. Create/update Configuration: set `splashscreen: 'file_...'` under the device key (`stripe_s700`, `stripe_s710`, `bbpos_wisepos_e`, `bbpos_wisepad3`, `verifone_p400`)

## Raw Sources

- [[stripe-terminal-splash-screen-2025]] — verbatim webpage content (Dashboard flows + Node.js API samples)
