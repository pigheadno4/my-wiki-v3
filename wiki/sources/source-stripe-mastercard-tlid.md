---
title: "Stripe: Mastercard Transaction Link ID (TLID)"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-mastercard-tlid-2025.md"
tags: [stripe, mastercard, tlid, cit, mit, network-transaction-id, compliance]
---

## Summary

Mastercard is introducing a Transaction Link ID (TLID) requirement in 2026, linking CITs and MITs. Stripe handles TLID storage and propagation automatically.

## Key Details

**TLID**: 22-char alphanumeric case-sensitive identifier (A-Z, a-z, 0-9, `-`, `_`). Links authorization and clearing messages. Runs in parallel with NTID (no NTID changes).

**Timeline**:
- **June 2, 2026**: must retain TLIDs from CITs that store card credentials + Account Status Inquiry (ASI) requests
- **October 23, 2026**: must send the retained TLID with all subsequent MITs as "economically related TLID"

**Stripe handling**: stores TLIDs for all businesses automatically; populates on MITs if Stripe processed the original CIT. For CITs before June 2, 2026 → sends TLID from earliest authorized MIT after that date.

## Raw Sources

- [[stripe-mastercard-tlid-2025]] — verbatim webpage content
