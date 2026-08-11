---
title: "PayPal Payouts"
type: concept
category: technology
tags: [paypal, payouts, disbursements, mass-payments, standard-payouts, advanced-payouts]
---

## PayPal Payouts

PayPal Payouts is a product for sending money to multiple recipients simultaneously — vendors, gig workers, affiliates, or anyone requiring mass disbursements. It comes in two tiers: Standard and Advanced.

## Two Tiers

### Standard Payouts

- Requires manual access approval from PayPal (sandbox available while pending)
- Single payout program; self-serve once approved
- Recipients identified by email, phone number, or PayPal ID
- Funded from PayPal balance
- Integration options: API, Large Batch (FTP), Payouts Web (browser upload)
- 96 countries, 24 currencies
- PayPal/Venmo payout rails; Venmo is US + USD only, requires U.S. mobile number
- Currency flexibility: automatic conversion for some currencies; others require manual balance transfer

### Advanced Payouts

- Enterprise-grade, personalized onboarding
- Multiple payout programs under one integration
- Additional payment rails: bank/debit card, prepaid/virtual card, eGift card, check, cash at pickup
- Drop-in UI or embedded pay portal integration
- 240+ countries, 50+ currencies
- 1099 tax reporting, detailed payee/transaction reporting, multilingual payee support

## Fees

Sender pays at transaction time. ~2% variable + country cap (domestic ≠ international). Individual max: $20,000 USD. Batch total: unlimited. Funding account must hold payout amount + fees.

## Payment Processing

Instant for existing PayPal/Venmo accounts. Non-accounts get 30-day claim window then returned. Item-level `transaction_status` values (9, via API): SUCCESS, FAILED, PENDING, UNCLAIMED, RETURNED, ONHOLD, BLOCKED, REFUNDED, REVERSED (web-upload only). Failed and Returned: **no funds deducted** from sender.

**Cancel**: only UNCLAIMED items can be cancelled — via dashboard (Activity → Transactions search) or API (`POST /v1/payments/payouts-item/{id}/cancel`, empty body `{}`). Cancel response shows `transaction_status: RETURNED`.

**API rate limit**: 400 POST requests/minute (`RATE_LIMIT_REACHED` = HTTP 429).

The exact REST-contract baseline at `90e8041` confirms four Payouts 1.9 operations: create a batch, retrieve a batch, retrieve an item, and cancel an unclaimed item. Its recipient wallet enum includes PayPal and Venmo. Contract presence does not establish account approval or regional availability. See [[source-github-paypal-rest-api-specifications]].

## Country Support

96 countries across 4 tiers. **Merchant cannot send payouts to India or Mexico** (receive/withdraw only). Colombia and Monaco: cross-border only. China uses country code `C2` (not `CN`).

## Currency Conversion

**20 currencies** support automatic conversion (docs.paypal.ai 2026 — dropped TWD vs older docs listing 21). **Zero-digit currencies** (no decimals): HUF, JPY. Exclusions: China, India, South Korea, Taiwan, Thailand, Turkey (no conversion); 15 Caribbean + 17 LatAm countries (USD only — recipients withdraw locally). Restrictions: Brazil (BRL in-country only), Malaysia (MYR between Malaysian users only).

> [!info] Currency count discrepancy
> Older docs listed 21 auto-conversion currencies including TWD. The 2026 docs.paypal.ai page lists 20 (no TWD). The newer page is likely authoritative.

## Webhooks (11 events)

3 batch-level (`PAYMENT.PAYOUTSBATCH.*`): DENIED, PROCESSING, SUCCESS. 8 item-level (`PAYMENT.PAYOUTS-ITEM.*`): BLOCKED, CANCELED, FAILED, HELD, REFUNDED, RETURNED, SUCCEEDED, UNCLAIMED. **Batch webhooks contain no item info** — use HATEOAS links for item details.

## REST SDK

Available in Java and Python (docs.paypal.ai 2026 — PHP and .NET covered in older SDK page only). Java version bumped to `1.1.1` in 2026 docs. Handles OAuth 2.0 automatically. Install: `pip install paypal-payouts-sdk` (Python), Maven `com.paypal.sdk:payouts-sdk:1.1.1` (Java).

## Venmo Payouts

US only; note required; message in recipient's Venmo feed. `recipient_type`: PHONE, EMAIL, or USER_HANDLE. `recipient_wallet: "Venmo"` (capital V). Supported across API, Payouts Web, and Large Batch.

## Assisted Account Creation (AAC)

Log in with PayPal for Payouts — lets customers authenticate via PayPal; merchant receives payer ID + email. **Payer IDs are the most reliable recipient identifier.** Requires account manager enablement. Works with all 3 integration methods.

## API Integration (Standard)

- **Endpoint**: `POST /v1/payments/payouts`
- **Max 15,000 items per call**
- **One currency per batch** — separate call per currency
- `recipient_type`: EMAIL, PHONE, or PAYPAL_ID; item-level overrides batch-level
- `recipient_wallet`: PAYPAL or VENMO
- Response includes `payout_batch_id`; poll for item-level status

## Payouts Web (Browser)

- Max **5,000 payments** per file; enable via account manager
- 10-column CSV uploaded through PayPal UI (Money → Send Money → Make a Mass Payment)
- Note to recipient: max 400 chars (required for Venmo)
- 30-day duplicate detection; hold on full amount + fees until Processed

## Large Batch (SFTP)

For >15,000 payouts; no upper limit. SFTP upload to PayPal DropZone server.

- Sandbox: `dropzone.es-ext.paypalcorp.com:22`; Production: `dropzone.paypal.com:22`
- CSV file, one currency, UTF-8; parts processed up to 500k records each
- Acknowledgment: ACK (pass) / NACK (fail) / DUPS (duplicate filename)
- Reports: Part File (per chunk) → Out/Interim (all complete) → Final (31 days later)
- Unclaimed payouts returned to sender after **30 days**

## Idempotency & Deduplication

- Retry 5xx failures with same `PayPal-Request-Id` header
- Two simultaneous requests with same header → first processed, second rejected
- `sender_batch_id` dedup window: **30 days** — duplicate rejected with HATEOAS link to original
- Safe to retry 5xx with same `sender_batch_id`

## Use Cases

- Marketplace seller disbursements
- Gig economy worker payments
- Affiliate or referral payouts
- Insurance claim disbursements
- Survey or research participant payments

## Key Players

- [[paypal]] — Payouts product owner

## Sources

- [[source-paypal-payouts-overview]] — Standard vs Advanced feature comparison, country/currency coverage, all integration guides, error codes, reporting, AAC
- [[source-github-paypal-rest-api-specifications]] — exact-SHA Payouts 1.9 operation and schema contract
