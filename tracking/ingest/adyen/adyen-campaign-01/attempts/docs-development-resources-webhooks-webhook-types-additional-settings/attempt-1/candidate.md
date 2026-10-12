---
title: "Adyen Standard Webhook Additional Settings"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/webhooks/webhook-types/additional-settings"
raw_files:
  - "adyen/docs/development-resources/webhooks/webhook-types/additional-settings/2026-09-15.md"
tags: [adyen, webhooks, standard-webhooks, additional-data, configuration]
---

## Overview

This [[adyen]] documentation page explains how to configure optional additional shopper and transaction information for Standard webhooks. Enabled information is delivered in the webhook's `additionalData` object; the complete setting and field inventory remains in the pinned raw snapshot.

## Key takeaways

- Additional information is optional and configured per webhook in the Customer Area under **Developers > Webhooks**. The page says only some webhooks expose optional additional settings, so availability must not be assumed for every webhook.
- The fields included in `additionalData` depend on the settings selected. The example enables capture-delay and alias settings only; it illustrates the resulting shape rather than guaranteeing those fields for all events.
- Several entries have narrower conditions. For example, the Payment Account Reference and contactless-wallet token settings require a separate **Developers > Additional data** enablement for point-of-sale transactions; ARN is limited to `CAPTURE` and `REFUND` events and is described for reconciliation when Adyen Acquiring is not used for settlement.
- Some entries are payment-, acquirer-, event-, or channel-specific. Use the raw inventory to verify each setting's exact condition and emitted field names instead of treating the catalog as a universal Standard-webhook schema.
- Enabling metadata for 3D Secure payment webhooks may cause a slight delay in webhook receipt.

> [!warning] Configuration and snapshot boundary
> This page documents selectable settings in the captured Customer Area documentation. It does not prove that every setting is available to a particular merchant, webhook, payment method, region, or environment, nor that a configured field will be present on every event.

## Detail locators

- Purpose, `additionalData` delivery, and Customer Area enablement steps: `# Additional settings`, raw lines 17-29.
- Complete setting descriptions and emitted-field inventory: table under `# Additional settings`, raw lines 31-223.
- Point-of-sale secondary-enable conditions: raw lines 40 and 94-96.
- ARN settlement and event qualifications: raw line 49; payment-, acquirer-, and event-specific examples continue throughout raw lines 112-175.
- Metadata webhook-delay warning: raw line 134.
- Example Standard webhook and the statement that emitted fields depend on selected settings: `### Example`, raw lines 225-262.

## Related

- Company: [[adyen]]
- Concept: [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/development-resources/webhooks/webhook-types/additional-settings/2026-09-15|2026-09-15 snapshot — Standard webhook additional settings and emitted-field inventory]]
