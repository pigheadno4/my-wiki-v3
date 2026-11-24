---
title: "Stripe Terminal: Configure Reboot Time Window"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
canonical_url: "https://docs.stripe.com/terminal/fleet/reboot-time"
original_format: webpage
raw_files:
  - "stripe-terminal-reboot-time-2025.md"
tags: [stripe, stripe-terminal, configurations, fleet, reboot]
---

## Summary

The May 1, 2026 guide documents a default midnight reboot every 24 hours for smart readers. A custom window uses the reader's registered location time zone. Readers reboot at random times within the configured window to stagger disruptions.

## Dashboard and API

- From the location details page, edit **Reboot time** under **Local configurations** or **Inherited configurations**. From **Manage locations**, choose **Edit configuration** from the location's overflow menu, then choose **Edit** or **Override** for **Reboot time**. Create a configuration first if one does not exist. Select the start and end times, then choose **Update** and **Apply changes**.
- To set the window through the API, create or update a Configuration with `reboot_window`. Supply two distinct integers from 0 through 23 as `start_hour` and `end_hour`. If the start is lower than the end, both are on the same day. If the start is higher, the window crosses midnight. For example, 15 to 3 means 3 p.m. to 3 a.m.
- The May Dashboard guide says Stripe sets the window within 10 minutes. If the reader has already rebooted that day, the window takes effect during the next period.

The separate November 7, 2026 Configuration API [create](https://docs.stripe.com/api/terminal/configuration/create.md?query=reboot_window) and [update](https://docs.stripe.com/api/terminal/configuration/update.md?query=reboot_window) references list `reboot_window` as optional for readers that support customized reboot times.

## Related Pages

- [[stripe-terminal-hardware-orders]] — Terminal fleet and reader settings
- [[source-stripe-terminal-configurations]] — account and location configuration hierarchy

## Raw Sources

- [[stripe-terminal-reboot-time-2025]] — full Dashboard and API guide captured May 1, 2026

## Related raw API references

- [[raw/stripe-terminal-fleet-reboot-time-2026-11-07]] — November 7, 2026 navigation index for the [Dashboard](https://docs.stripe.com/terminal/fleet/reboot-time.md?dashboard-or-api=dashboard) and [API](https://docs.stripe.com/terminal/fleet/reboot-time.md?dashboard-or-api=api) variants
