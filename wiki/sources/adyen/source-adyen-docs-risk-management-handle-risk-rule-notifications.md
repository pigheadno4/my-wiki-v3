---
title: "Adyen Fraud Results in API Responses and Webhooks"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/handle-risk-rule-notifications"
raw_files:
  - "adyen/docs/risk-management/handle-risk-rule-notifications/2026-09-15.md"
tags: [adyen, risk-management, fraud, api-responses, webhooks]
---

## Overview

This Adyen risk-management snapshot explains how to configure fraud and risk-rule results in online-payment API responses and Standard webhooks. Returning fraud results is off by default. Enabling and formatting the additional data changes response and webhook payloads; it does not itself change a payment or risk decision. See [[adyen]], [[adyen-risk-management]], and [[adyen-webhooks]].

## Key takeaways

- The documented prerequisites are an online-payments integration, enabled risk management, configured and enabled webhooks, and the appropriate Customer Area roles for webhook/response or risk-setting changes. Details about custom risk rules and `fraudRiskLevel` require Protect premium. This snapshot does not establish premium entitlement or live configuration for a particular account.
- After **Developers > Additional data > Risk > Fraud result** is enabled, the API response carries risk information in `additionalData` and triggered-rule details in `fraudResult`; the webhook carries both risk information and fraud results in `additionalData`. Keep the API response and webhook object paths distinct.
- Option 1 uses one format for all triggered risk-check lines. Option 2 additionally enables **Change risk result format for custom rules** so triggered custom rules are represented separately. Option 3 is a separate, optional Standard-webhook **Include Risk Data** setting that adds the custom `riskdata` fields and values from the request to webhook `additionalData`; it affects webhooks only.
- `fraudResultType` can be `GREEN`, `AMBER`, or `RED`; for Protect premium, `AMBER` denotes a transaction sent to case management for manual review. The listed `fraudRiskLevel` classification is tied to the premium machine-learning fraud-risk rule. These values report risk evaluation or review state, not payment authorization or finality.
- The page provides rule-name and score-value references and examples for each option. Some webhook code blocks omit commas between adjacent `additionalData` properties (for example, lines 119–120 and 212–215), so treat them as illustrative payload shapes rather than valid JSON fixtures.

## Detail locators

- Purpose, default-off behavior, prerequisites, role split, and premium limitation: lines 15–36.
- Enabling Fraud result and response-versus-webhook object placement: lines 38–60. The settings matrix and option prerequisites: lines 62–94.
- Option 1 one-format webhook and API examples: `## Option 1: One format for all risk checks`, lines 95–183. Option 2 custom-rule split and examples: lines 184–284.
- Option 3 webhook-only custom `riskdata` fields and example: lines 285–330. Rule-name/action/premium reference: lines 331–371.

## Related

- [[adyen]] — provider context.
- [[adyen-risk-management]] — Protect configuration and reciprocal source route.
- [[adyen-webhooks]] — Standard webhook delivery and handling concept.

## Raw Sources

- [[raw/adyen/docs/risk-management/handle-risk-rule-notifications/2026-09-15|Adyen fraud results in API responses and webhooks (2026-09-15)]]
