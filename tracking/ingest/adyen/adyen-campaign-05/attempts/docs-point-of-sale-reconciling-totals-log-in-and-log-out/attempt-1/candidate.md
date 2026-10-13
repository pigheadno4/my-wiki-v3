---
title: "Adyen Terminal API login and logout for totals"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/reconciling-totals/log-in-and-log-out"
raw_files:
  - "adyen/docs/point-of-sale/reconciling-totals/log-in-and-log-out/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, login, logout, operator, shift, terminal-totals]
---

## Overview

This Adyen Docs page describes Terminal API `LoginRequest` and `LogoutRequest` messages for a payment terminal, particularly before retrieving terminal transaction totals or reconciling a balance mismatch. Login can label a change of operator or the start of a shift so totals can be viewed by operator or shift. See [[adyen]] and [[adyen-terminal-api]]. This is a terminal/POS operational state, not operator authentication, terminal clearing, financial settlement, or proof of funds received.

## Key takeaways

- A Terminal API Login request is required before using Terminal API requests to retrieve a terminal's transaction totals or reconcile terminal/POS balance mismatches. The page advises Logout when the operator changes or the shift ends. Its stated integration type is Terminal API with payment terminals; it does not specify a Mobile SDK login procedure.
- The standard request header uses `MessageClass: Service`, `MessageCategory: Login` or `Logout`, and the correct POS `SaleID`, terminal `POIID` and per-terminal unique `ServiceID`. The table states `ServiceID` is 1–10 alphanumeric characters and unique for that `POIID` in the previous 48 hours. The `3.0` header value is the Terminal API protocol version in this guide, not an independently pinned SDK or Checkout API release.
- The Login body requires UTC `DateTime`, `SaleSoftware` identifying the sale system, and two-character `OperatorLanguage`. `OperatorID`, `SaleTerminalData.TotalsGroupID` and `ShiftNumber` are optional identifiers supplied by the POS for operator/group/shift attribution. Login does **not** authenticate the operator; the merchant POS must not treat an `OperatorID` or successful Login as an identity or permission check.
- In `LoginResponse`, `Response.Result: Success` indicates login completed, while `POIStatus` separately indicates whether the terminal is ready for use. After Login, the terminal retains provided values until a new Login is processed for that same terminal or it receives a Logout. The example's software strings, operator name, group and terminal ID are illustrative.
- Logout uses a `MessageCategory: Logout` header and an empty `LogoutRequest`; `LogoutResponse.Response.Result: Success` indicates terminal logout. The page does not say Logout clears transaction counters, settles a batch, changes past totals, or cancels an in-progress payment. Retrieve-totals and mismatch-handling details are on separately linked pages and need their own evidence.

## Detail locators

- Operational purpose, login prerequisite, operator/shift labels and explicit non-authentication warning: `# Log in and log out`, raw lines 15–23. Terminal integration requirement: `## Requirements`, lines 25–31.
- Login header, identity constraints and required/optional body fields: `## Log in to the terminal`, raw lines 33–58. JSON/Java examples: lines 60–126.
- Login result versus `POIStatus` readiness, and retained-value lifetime: raw lines 128–167.
- Logout header, empty body, examples and response result: `## Log out from the terminal`, raw lines 169–254.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — in-person Terminal API message and terminal-state route; versioned GitHub examples are separate.

## Related raw API references

- The raw page links to Terminal API schema, terminal-totals retrieval and balance-mismatch guides. Those destinations are navigation until independently read; see raw lines 35–49, 128, 171–185, 231 and 256–259.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/reconciling-totals/log-in-and-log-out/2026-09-15|Adyen Docs: Log in and log out (2026-09-15 snapshot)]]
