---
title: "Adyen POS NFC tag reading and writing"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/nfc-tags"
raw_files:
  - "adyen/docs/point-of-sale/nfc-tags/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, nfc, card-acquisition]
---

## Overview

Adyen's NFC tag guide describes identifying a presented tag by UID and type, reading and writing tag memory, and reading or incrementing MIFARE Ultralight AES counters through Terminal API CardAcquisition requests. Tags can include cards, phones, or bracelets; the examples cover loyalty, access, and stored value. These are terminal interactions, and a successful CardAcquisitionResponse or a terminal's optional green check mark is not evidence of payment authorization. The UID is an identifier for lookup in the merchant's system, not proof that a person or balance is valid.

## Key takeaways

- A Terminal API integration and a terminal model compatible with the chosen NFC tag are prerequisites. Adyen says Support creates the NFC configuration after receiving the tag type, access keys if used, and any dedicated Android app UI-hiding requirement. Hardware, tag, software, and app availability are conditional on the guide's captured matrix; the snapshot does not establish a particular terminal's current capability.
- The request Base64-encodes an Operation JSON object in SaleData.SaleToPOIData and uses a Service-class CardAcquisition message. NFCReadUID returns NFC.uid and NFC.variant. NFCRead and NFCWrite take tag-specific sector, application/file, or page data and authentication conditions. Inspect NFC.status as well as the overall response. ExpectedUid on a write prevents writing to a different presented tag by returning WRONG_CARD; an empty or omitted value is ignored. An empty write NFCData returns identity without writing.
- The requirements section says MIFARE DESFire writing and MIFARE Ultralight memory reading/writing are Android-terminal-only in this snapshot. The same guide says Engage can read/write only unlocked Ultralight C pages and cannot authenticate those tags; see the eligibility conflict below. Ultralight READ returns four consecutive pages (16 bytes) even if fewer pages were requested, so the returned data can include pages beyond the requested range.
- Only Ultralight AES has the three independent 24-bit counter registers described here; the guide limits their read/write to Android terminals on software version 134 or later. A write increments a counter; it cannot set or decrease its total. NFC.data on a counter-write response is the increment amount, not the new total. Page and counter operations cannot share one NFCData array.
- A multi-request Session begins with Session.Type Begin, carries the same Session.Id through subsequent operations, and ends with Session.Type End. In both single operations and a finished session, send EnableService with AbortTransaction to stop the loading screen. Optional DisplayOutput changes the displayed icon/message; its Approved/Declined icon is a display choice, not a payment decision.
- Hiding Adyen's UI is an optional Support-enabled configuration for a dedicated Android app processing stored-value or identity cards, limited here to S1E, S1E2L, S1F2, and S1U2 on software 1.114+. If a regular payment card is presented in that configured NFC flow, BLOCK_CARD means the card cannot be used with that app; it does not mean the card itself is blocked. Ordinary card acquisition remains unaffected.

> [!warning] Ultralight terminal eligibility conflict
> The requirements say MIFARE Ultralight read/write is Android-terminal-only (raw lines 38–42), while the supported-products matrix marks several Engage models capable of MIFARE Ultralight and Ultralight C (2141–2175); the guide also limits Engage Ultralight C read/write to unlocked pages because those terminals cannot authenticate the tag (2165). The matrix does not establish which operation works for each model. Preserve both statements and verify the exact tag variant, read/write operation, terminal model, and installed software with Adyen before relying on this snapshot.

> [!warning] Raw example and format conflicts
> The session table labels a timeout Session.Timeout (raw lines 1833–1834), while its JSON example uses TimeoutMs (1840–1845). Counter response prose calls AdditionalResponse a Base64 string decoded to JSON (1512 and 1704), while the displayed responses contain URL-style key/value data (1537 and 1729). The broad Ultralight introduction says no keys (1204), while variant tables require or default authentication keys for Ultralight C/AES (1218–1225). Verify the applicable API contract and actual terminal response before implementing these points.

## Detail locators

- Requirements, Support setup, device/tag limitations, and basic flow: raw lines 30–62; complete model-by-tag matrix: 2141–2182.
- UID request and response; CardAcquisition headers, optional TotalAmount with a required CardAcquisitionTransaction object, and service closure: 64–231.
- Classic, DESFire, and Ultralight read requests/responses, NFC.data/status, auth conditions, and Ultralight four-page overread: 233–805, especially 713–728.
- Tag-specific writes, ExpectedUid and empty-write semantics: 807–1388. Check example page labels against request and response near 1300–1330 rather than inferring page results.
- Ultralight AES counters, limits, little-endian values, separate page/counter requests, and errors: 1390–1798. The write response reports the increment, not the resulting stored total (1704–1709).
- Multi-request Session lifecycle and final EnableService request: 1800–2089. UI hiding, BLOCK_CARD scope, and unaffected regular card acquisition: 2091–2139.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — Terminal API message and card-acquisition boundary.
- [[source-adyen-docs-point-of-sale-card-acquisition]] — general acquisition and finish/cancel flow; this NFC guide adds tag-specific operations and device constraints.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/nfc-tags/2026-09-15|Adyen Docs: NFC tags reading and writing (2026-09-15 snapshot)]]
