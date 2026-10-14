---
title: "Show a QR code on the terminal | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/display-data/display-qr-code"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/display-data/display-qr-code/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, display-request, qr-code]
---

## Overview

This Adyen Docs guide explains how a merchant POS app shows a scannable QR code, with optional header and footer, on a payment terminal's customer display. The QR may link to loyalty signup, an app, an offer or a webshop in the examples. This is a Terminal API **Device/Display** operation for merchant-supplied content, not a QR wallet payment, proof of a scan, or evidence of enrollment or payment. See [[adyen]], [[adyen-pos-shopper-engagement]], and [[adyen-terminal-api]].

## Key takeaways

- For `OutputContent.OutputBarcode.BarcodeValue`, the page says a URL alone can be supplied as a plain text string; content beyond a URL is URL-encoded first. This QR-display route does **not** instruct the merchant to Base64-encode receipt XML. Its sample text, URL and loyalty call-to-action are examples, not a validation of the destination, identity, consent, currency, expiry or any resulting action.
- The Terminal API header uses ProtocolVersion `3.0`, `MessageClass=Device`, `MessageCategory=Display`, `MessageType=Request`, `SaleID`, `POIID` and a `ServiceID` unique for that terminal over the prior 48 hours. `DisplayRequest.DisplayOutput` is an **array**. Its QR item targets `CustomerDisplay` with `InfoQualify=Display`, `OutputFormat=BarCode`, `OutputBarcode.BarcodeType=QRCode`, and the barcode value. Optional text items use `OutputFormat=Text`: the first text item is interpreted as header and the second as footer. A separate `OutputResult` entry corresponds to each display item in array order.
- The page says `MinimumDisplayTime` sets how long the QR screen is shown. If omitted, the QR remains until another request such as payment or standby display replaces it. `ResponseRequiredFlag` defaults to `true` when absent for QR and text elements; the response then reports whether each element was shown. That is display status, not a shopper scan, wallet outcome, financial authorization, consent record or completed loyalty action.
- The three-item example returns `DisplayResponse.OutputResult[0]`, `[1]` and `[2]` for QR, header and footer respectively, each with `Response.Result=Success`. A client must inspect the matching array item rather than treating `OutputResult` as a single object or assuming every element succeeded. The page does not give a terminal-model support matrix or a current deployment/device guarantee; images illustrate portrait, small portrait and landscape appearances.

## Detail locators

- `Show a QR code on the terminal`, pinned raw lines 15–29: content examples, optional header/footer, duration/replacement and visual layouts.
- `Make a display request for a QR code`, lines 31–49: URL-encoding for richer content versus plain URL value, with illustrative string.
- Header and QR output tables, lines 51–89: Device/Display message header, per-terminal ServiceID, `DisplayOutput` array, QR format/type/value, duration and response flags, optional text-item ordering.
- Request and response examples, lines 91–184: three `DisplayOutput` items and index-matched `OutputResult` array with example Success values.
- `See also`, lines 186–190: virtual receipt, image and standby guides are navigation only.

## Related

- [[adyen-pos-shopper-engagement]] — main terminal interaction concept.
- [[adyen-terminal-api]] — Device/Display message context, distinct from payment messages.
- [[source-adyen-docs-point-of-sale-shopper-engagement-display-data-display-receipt]] — separate Base64 XML virtual-receipt route; a QR block there has different formatting.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/display-data/display-qr-code/2026-09-15|Adyen QR-display guide, fetched 2026-09-15]]
