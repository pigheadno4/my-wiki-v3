---
title: "Adyen Terminal API latest CardReaderAPDU request"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/cardreaderapdu"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/cardreaderapdu/2026-09-15.md"
tags: [adyen, terminal-api, api-explorer, card-reader, apdu]
---

## Overview

This 2026-09-15 snapshot of the Adyen API Explorer **Terminal API latest** `POST /cardreaderapdu` entry describes a CardReaderAPDU request sent to a card chip and its response. It mentions a possible invitation on the CashierInterface or CustomerInterface, but the captured request-body table provides no invitation field. The documented cloud server URLs are TEST `/v1/merchants/{merchantAccount}/devices/{deviceId}/sync` and `/async`; local hosting is shown only as `<local-terminal-IP-address>`. The snapshot does not pin a numbered Terminal API schema version. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- The request-body table marks `APDUClass` (CLA), `APDUInstruction` (INS), `APDUPar1` (P1), and `APDUPar2` (P2) required, all as strings. `APDUData` (Lc + Data) and `APDUExpectedLength` (Le) are optional strings. For a specific card such as a synchronous card, the `APDUClass` description calls for a private value in the ISO 7816-4 D0–FE range. See raw lines 23–31.
- Under `200 Success`, the response-body table requires `Response` and its `Result` (`Success`, `Failure`, or `Partial`), plus `CardStatusWords` (SW1–SW2). `APDUData` and `AdditionalResponse` are optional. The prose says `ErrorCondition` is absent or unused for `Success`, and must be present otherwise, although its table column says “No”; see raw lines 33–47. An HTTP 200 heading therefore does not itself mean the message result succeeded.
- The captured page provides no full Terminal API message envelope, specific caller credential or role, request/response correlation identifier, session rule, length bound, timeout, retry, reversal, or payment outcome. Its cloud URL identifies a merchant account and device path, but the body table supplies no `merchantAccount`, `deviceId`, or `POIID` field. The response concerns APDU message processing and chip status, not payment authorization, capture, reconciliation, settlement, or bank receipt.

## Detail locators

- Servers and environment: raw lines 10–19.
- Request properties and requiredness: raw lines 21–31.
- Response result, error-condition enum, and smartcard status words: raw lines 33–47.

## Related

- [[adyen-terminal-api]] — provider concept and reciprocal source route.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/cardreaderapdu/2026-09-15|Adyen API Explorer CardReaderAPDU raw snapshot]]
