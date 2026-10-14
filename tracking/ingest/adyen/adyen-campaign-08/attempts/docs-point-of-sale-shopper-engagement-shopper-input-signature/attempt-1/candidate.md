---
title: "Adyen Terminal API shopper signature input"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/signature"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/shopper-input/signature/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, signature, input]
---

## Overview

Adyen's signature-input guide, captured 2026-09-15, shows a merchant Terminal API Device/Input request that asks a shopper to draw a signature on a payment-terminal display and confirm or cancel. It belongs to [[adyen-pos-shopper-engagement]]: collecting this input does not itself authorize a payment, prove a person's identity, establish enforceable legal consent, or validate the signature.

## Key takeaways

- **Request fields have distinct names.** `SaleToPOIRequest.MessageHeader` uses protocol 3.0, `MessageClass: Device`, `MessageCategory: Input`, `MessageType: Request`, SaleID, POIID and a terminal-scoped ServiceID unique within the last 48 hours. `InputRequest.DisplayOutput` targets `CustomerDisplay` with Text output and `PredefinedContent.ReferenceID: GetSignature`. `InputRequest.InputData` targets `CustomerInput` with `InputCommand: GetConfirmation` and an integer `MaxInputTime` in seconds. ServiceID uniqueness does not establish a safe retry or idempotency guarantee.
- **The display takes two merchant text items.** The first is a header, limited to about 20 characters on a portrait display; the second may be additional text or empty. M400, e280 and e285 ignore additional text, but the page still requires the second item with an empty value for those models. The Java sample later adds `declineAnswer` and `agreeAnswer` despite the two-item prose/table and without defining those variables in the shown sample; use the field instructions and verify generated code before adopting that example. The page does not give a general supported-terminal list.
- **Interpret confirmation and signature separately.** The guide says `InputResult.Response.AdditionalResponse` contains the shopper-provided signature; the example carries URL-encoded `responseData` with a `signature_format` marked `raw`. `InputResult.Input.ConfirmedFlag: true` indicates the shopper selected Confirm; `false` means the shopper selected Cancel. The input is not format-validated, and the merchant system must validate relevant `InputResult.Input` data for its own use. The flags and raw data do not prove legal consent or payment authorization.
- **Timeout and override are failures of this input request.** The prompt remains until input, `MaxInputTime` expiry, terminal Cancel, a cancel-input request, or another POS request. Timeout produces `Failure`/`Cancel` with `message=Screen%20timeout`. A payment request received while signature input is pending overrides it, producing `Failure`/`Busy` and a higher-priority-request message; that does not state the payment's result. Do not treat a missing signature or cancellation as confirmation.

## Detail locators

- Raw `# Ask for a signature`, `## Requirements` and `## How it works` (lines 15–40): purpose, Terminal API prerequisite, confirm/clear UI and prompt-ending events.
- Raw `## Make a Signature input request` tables (lines 48–84): Device/Input header, two text items, model-specific ignored second text, `GetSignature` versus `GetConfirmation`, and timeout field.
- Raw JSON and Java examples (lines 86–168): illustrative 30-second request; Java text-item additions at lines 149–157 conflict with the two-item instruction and show undefined variables.
- Raw response handling (lines 170–215): raw signature in AdditionalResponse, `ConfirmedFlag`, no format validation, timeout, payment override and merchant validation.
- Raw `## See also` (lines 217–221): separate cancellation, input selection and session guides; navigation only.

## Related

- [[adyen-pos-shopper-engagement]] — customer-interaction hub.
- [[adyen-terminal-api]] — Terminal API message and payment boundary.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/shopper-input/signature/2026-09-15|Ask for a signature, fetched 2026-09-15]]
