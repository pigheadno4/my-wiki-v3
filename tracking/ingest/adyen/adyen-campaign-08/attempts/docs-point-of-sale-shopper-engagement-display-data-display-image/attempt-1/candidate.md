---
title: "Show an image on the terminal | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/display-data/display-image"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/display-data/display-image/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, display-request, images]
---

## Overview

This Adyen Docs guide describes showing a POS-supplied advertisement, offer or other image on a payment terminal's customer display through a Terminal API **Device/Display** request. The image file is Base64-encoded and supplied as `MessageRef`/`Image` display content. This is a nonfinancial display operation; showing an image does not establish a payment, legal receipt, shopper response or marketing consent. See [[adyen]], [[adyen-pos-shopper-engagement]], and [[adyen-terminal-api]].

## Key takeaways

- The page names PNG, JPEG, GIF and BMP image files for Base64 conversion. It says the terminal decodes received images only and does not run or store them. This is a description of the terminal's handling in the captured guide, not a statement that the POS-supplied content is privacy-safe or that any remote destination is trustworthy. The guide shows a truncated illustrative Base64 string and does not specify a Data URI prefix, image dimensions, resolution or payload-size limit.
- Build a Terminal API message header with ProtocolVersion `3.0`, `MessageClass=Device`, `MessageCategory=Display`, `MessageType=Request`, `SaleID`, `POIID` and a `ServiceID` unique per terminal for the prior 48 hours. The one-item `DisplayRequest.DisplayOutput` array targets `CustomerDisplay` with `InfoQualify=Display`; its `OutputContent` uses `OutputFormat=MessageRef`, `PredefinedContent.ReferenceID=Image` and `OutputText[0].Text` containing the Base64 image. The sample `POIID` names V400m, but the page gives no supported-model matrix or current device-eligibility guarantee.
- `MinimumDisplayTime` is described as the number of seconds the image is shown. If omitted, the page says the image remains until another request replaces it, such as payment, another image or standby display. This behavior does not imply a Terminal API session or a completed shopper action.
- A decode error means the image will not be shown. In the single-item response example, `DisplayResponse.OutputResult[0].Response.Result=Success` indicates the display request succeeded for that item. `OutputResult` is an array, not a single response object; the guide does not establish any payment result, authorization, print receipt or legal/tax content from display success.

## Detail locators

- `Show an image on the terminal`, pinned raw lines 15–35: intended display use, file formats, replacement/timing behavior, visual layouts and terminal decode-only claim.
- `Make a display request for an image`, lines 37–64: Base64 conversion, Device/Display header and one-item `DisplayOutput` fields.
- Request example, lines 66–102: `MessageRef`/`Image` and truncated example Base64 in `OutputText.Text`; sample terminal ID is not a support list.
- Result handling, lines 104–128: decode-error no-display condition and single-item `OutputResult` response array.
- `See also`, lines 130–134: virtual receipt, standby and QR guides are navigation only.

## Related

- [[adyen-pos-shopper-engagement]] — primary terminal interaction concept.
- [[adyen-terminal-api]] — message context; display and payment have separate outcomes.
- [[source-adyen-docs-point-of-sale-shopper-engagement-display-data-display-receipt]] — Base64 XML virtual-receipt route with different fields.
- [[source-adyen-docs-point-of-sale-shopper-engagement-display-data-display-qr-code]] — barcode/QR display route with different output format.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/display-data/display-image/2026-09-15|Adyen image-display guide, fetched 2026-09-15]]
