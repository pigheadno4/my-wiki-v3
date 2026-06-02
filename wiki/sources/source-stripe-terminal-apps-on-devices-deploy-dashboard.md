---
title: "Stripe Terminal: Apps on Devices — Deploy Your App in the Dashboard"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-apps-on-devices-deploy-dashboard-2025.md"
tags: [stripe, stripe-terminal, apps-on-devices, deploy, deploy-groups, progressive-deployment, dashboard]
---

## Summary

How to set up deploy groups, deploy approved APKs, and use progressive rollouts via the Stripe Dashboard.

## Key Details

**Deployment behavior**: app is sent immediately after deploy action; device reboots to install. Devices auto-reboot every 24h to apply updates. Manual reboot triggers immediate update check.

**Deploy groups**: group readers by Location. One default deploy group per device type (auto-catches unassigned locations). Platforms with direct charges can add Connected Account locations to their deploy groups.

**Three deploy entry points** (all require approved app version):
1. Deploy group details page → Deploy → New deployment
2. Software tab → select apps → Deploy
3. App details page → Deploy version

Rules: cannot deploy an older version (must always be newer than current). Failed install after 3 attempts → user can postpone to maintain payments.

**Share apps across accounts** (contact sales): one owner account manages uploads; other accounts find and deploy by app ID. Avoids package name conflicts and duplicate reviews.

**Deploy group best practices** (Alpha → Beta → General):
- **Alpha**: internal devkits/internal production devices
- **Beta**: small sample of real user locations
- **General**: all remaining (use default deploy group to avoid manual assignment)

**Progressive deployments**: staged percentage rollout within a deploy group. Predefined or custom plan. Percentages are fixed after plan creation. Predefined plans start at 0% — must manually advance. Pausing stops further rollout but doesn't interrupt in-progress downloads/installs. Stages don't auto-advance and don't persist between plans.

## Raw Sources

- [[stripe-terminal-apps-on-devices-deploy-dashboard-2025]] — verbatim webpage content
