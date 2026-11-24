---
title: "Stripe Terminal: Apps on Devices — Prepare for App Review"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
canonical_url: "https://docs.stripe.com/terminal/features/apps-on-devices/app-review"
original_format: webpage
raw_files:
  - "stripe-terminal-features-apps-on-devices-app-review-2026-11-07.md"
  - "stripe-terminal-apps-on-devices-app-review-2025.md"
tags: [stripe, stripe-terminal, apps-on-devices, app-review, p2pe, verifone]
---

## Summary

Stripe's app review process for [[stripe-terminal-apps-on-devices|Apps on Devices]] varies by use case. Before deployment, Stripe requires manual review for apps from users of its Point-to-Point Encryption (P2PE) solution and all apps intended for Verifone devices. The May 1 and November 7, 2026 captures describe the same review paths and timing. November adds an app allowlist instruction.

## Automated Approval

The guide lists three qualifying cases.

- The app runs on Stripe readers without P2PE. You can limit compatible device types to Stripe readers such as the S700/S710.
- The app is intended only for development and testing on a DevKit. You can limit compatible device types to DevKit readers such as the S700/S710 DevKit.
- You re-upload an APK that Stripe previously reviewed and approved.

The November guide routes the compatible-device setting to [Dashboard upload](https://docs.stripe.com/terminal/features/apps-on-devices/submit.md?dashboard-or-api=dashboard#upload-your-app).

## Manual Review Process

Stripe reviews the submitted device asset version. The developer supplies instructions with the submission. During review Stripe installs the app on a Terminal smart reader and follows those instructions, focusing on the payment collection UI. Stripe approves the app for deployment and notifies the developer if the reviewer finds no issues.

Stripe typically reviews apps within two working days from submission. Most submissions receive a review within five working days. Exceptional cases can take longer, and incomplete information can delay a review or cause a submission to fail. These estimates create no obligation for Stripe or its affiliates.

Stripe can reject the app if reviewers cannot follow the instructions, features might put payment information at risk, or technical defects prevent a full review.

## App Review Guidelines

These guidelines apply to all apps deployed on Stripe Terminal devices regardless of review path.

- Stripe encourages platforms to build a multi-tenant app with per-business configuration to avoid individual app submissions.
- Use the Terminal reader running the app to collect sensitive card and PIN information. The app must omit UI for manual entry of PINs, authentication values, or payment information.
- During development and testing, accept sandbox payments on a DevKit so Stripe can review with a physical Terminal test card. If live payments are necessary, accept a minimal charge such as 1 USD or its equivalent in another currency.
- Use the DevKit before review to fix defects that prevent installation, crash the app before payment UI interaction, or prevent reader discovery or connection.
- Provide self-contained instructions with login information if applicable, a fixed authentication code valid indefinitely if applicable, the route to the payment UI, and a full test walkthrough. Reviewer credentials must prevent access to sensitive information and functionality with side effects, such as placing a real food order.
- The November 7, 2026 guide instructs developers to allowlist `65.87.144.8/32–65.87.144.11/32` for the app.

## Related Sources

- [[source-stripe-terminal-apps-on-devices-build]] — DevKit development and testing
- [[source-stripe-terminal-apps-on-devices-submit]] — upload, submission, and review status
- [[source-stripe-terminal-apps-on-devices-deploy-dashboard]] — Dashboard deployment and progressive rollout after approval
- [[source-stripe-terminal-apps-on-devices-deploy-api]] — API deployment after approval

## Raw Sources

- [[raw/stripe-terminal-features-apps-on-devices-app-review-2026-11-07]] — full guide captured November 7, 2026
- [[stripe-terminal-apps-on-devices-app-review-2025]] — full guide captured May 1, 2026
