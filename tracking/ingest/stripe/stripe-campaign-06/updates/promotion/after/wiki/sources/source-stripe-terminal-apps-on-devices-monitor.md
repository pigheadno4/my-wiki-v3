---
title: "Stripe Terminal: Apps on Devices — Monitor Your Deployment"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
canonical_url: "https://docs.stripe.com/terminal/features/apps-on-devices/monitor"
original_format: webpage
raw_files:
  - "stripe-terminal-features-apps-on-devices-monitor-2026-11-07.md"
  - "stripe-terminal-apps-on-devices-monitor-2025.md"
tags: [stripe, stripe-terminal, apps-on-devices, deploy, monitoring, dashboard]
---

## Summary

Both the May 1 and November 7, 2026 guides describe using the Stripe Dashboard after deploying an Android app to Stripe SmartPOS Android devices. Use the Dashboard to monitor progress, investigate deployment issues, and deploy a new app if needed.

## May 2026 Dashboard workflow

In the Dashboard, go to **Terminal → Software**, select the app, then select the release version under **App info**. The May guide describes deployment status and reader counts for the selected release.

| Status | Meaning |
| --- | --- |
| Pending | The device has yet to check the Terminal backend for updates. |
| Served | The app reached the device. The device will attempt to install it at the next reboot. |
| Installed | The app successfully installed on the device. |
| Failed | An error occurred during the installation attempt. |

The November guide retains the general guidance to monitor deployments in the Dashboard. The specific path, counts, and status definitions above come from the May capture.

## Related Pages

- [[stripe-terminal-apps-on-devices]] — deployment and app lifecycle
- [[source-stripe-terminal-apps-on-devices-troubleshooting]] — troubleshoot deployment and runtime issues

## Raw Sources

- [[raw/stripe-terminal-features-apps-on-devices-monitor-2026-11-07]] — November 7, 2026 high-level monitoring and troubleshooting guidance
- [[stripe-terminal-apps-on-devices-monitor-2025]] — May 1, 2026 Dashboard workflow and deployment status table
