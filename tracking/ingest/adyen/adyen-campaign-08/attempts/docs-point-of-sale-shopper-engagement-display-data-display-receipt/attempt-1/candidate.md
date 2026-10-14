---
title: "Show a virtual receipt on the terminal | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/display-data/display-receipt"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/display-data/display-receipt/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, display-request, virtual-receipt]
---

## Overview

This Adyen Docs guide shows how a merchant POS app can place a **virtual purchase overview** on a supported payment terminal display **before** the payment starts, optionally with a QR code. It uses a Terminal API `DisplayRequest` carrying Base64-encoded receipt XML and is separate from `PaymentRequest`, `PrintRequest`, any actual payment outcome, and legal/tax receipt obligations. See [[adyen]], [[adyen-pos-shopper-engagement]], and [[adyen-terminal-api]].

## Key takeaways

- The virtual receipt has scrollable lines. A landscape terminal shows a QR code beside lines; a portrait terminal uses a QR screen with a proceed button before the line screen. The page says the display request does **not time out**: the receipt stays until another request, such as payment or standby display, replaces it. This is display persistence, not a payment hold, Terminal API session guarantee, or shopper acceptance signal.
- Build XML with a compatible `<screen name>` XSLT and receipt content, Base64-encode the XML, then put it in `DisplayRequest.DisplayOutput[0].OutputContent.OutputXHTML` with `OutputFormat=XHTML`, `Device=CustomerDisplay` and `InfoQualify=Display`. The message header uses ProtocolVersion `3.0`, `MessageClass=Device`, `MessageCategory=Display`, `MessageType=Request`, and per-terminal unique `ServiceID` within the prior 48 hours plus `SaleID` and `POIID`. The JSON and Java examples illustrate this display operation, not a version-pinned SDK contract.
- Screen names are model- and layout-dependent. The table distinguishes a QR-capable XSLT from non-QR, M400-specific and auto-scroll variants; images and per-line icons/subtitles are SFO1-only. A `<qrcodeblock>` is ignored when the chosen screen name cannot show QR. Consult the raw model table and steps before choosing a template: their model sets differ for the auto-scroll variant (the steps name SFO1 while the table does not), so the page alone does not resolve all model/template compatibility.
- `DisplayResponse.OutputResult.Response.Result=Success` reports success of the display request. Failure may include `AdditionalResponse` and `ErrorCondition`; the sample incompatible-model failure is `NotAllowed`. Adyen always checks whether the XML parses; XSD validation occurs **only when Support has enabled it for the account**. XML parse or optional XSD failures return `MessageFormat`, with XSD details in the terminal log. Passing these checks does not validate monetary totals, tax/legal content, QR destinations, shopper identity or payment execution.
- The example's membership QR payload, item lines, discounts, taxes and amount values are illustrative POS-supplied content, not a verified loyalty integration, shopper authorization, privacy consent, encryption, or financial record. Base64 is the transport encoding described here; the page gives no personal-data or QR security policy.

## Detail locators

- `Show a virtual receipt on the terminal` and visual examples, pinned raw lines 15–41: pre-payment purpose, no-timeout/override behavior, scrollable and QR layouts.
- `Receipt XML file`, lines 43–67: XML-to-Base64 requirement, supported content elements, model/XSLT table and SFO1-only fields.
- `Example XML file`, lines 69–205: illustrative QR and POS item/tax/total payload; currency symbol display note. Its sample figures and QR URL are not operational requirements.
- `Make a display request for a virtual receipt`, lines 207–359: template/model directions, header and `DisplayOutput` fields, JSON/Java examples, Success and failure response fields.
- `XML validation`, lines 361–403: unconditional parsing, account-enabled XSD check, Support activation and error/log details.
- `See also`, lines 405–409: standby, QR and image guides are navigation only.

## Related

- [[adyen-pos-shopper-engagement]] — main shopper-facing terminal interaction hub.
- [[adyen-terminal-api]] — Terminal API message family; Display and Payment have separate results.
- [[source-adyen-docs-point-of-sale-basic-tapi-integration-generate-receipts]] — separate payment-receipt generation route, not established by this pre-payment display guide.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/display-data/display-receipt/2026-09-15|Adyen virtual-receipt display guide, fetched 2026-09-15]]
