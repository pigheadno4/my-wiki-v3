---
title: "PayPal Payouts Overview"
type: source
date_ingested: 2026-04-16
original_format: webpage
raw_files:
  - "paypal-payouts-overview.md"
  - "paypal-payouts-standard.md"
  - "paypal-payouts-integrate-api.md"
  - "paypal-payouts-customize-api.md"
  - "paypal-payouts-test-go-live.md"
  - "paypal-payouts-large-batch.md"
  - "paypal-payouts-file-validation-errors.md"
  - "paypal-payouts-web.md"
  - "paypal-payouts-web-customize.md"
  - "paypal-payouts-reports.md"
  - "paypal-payouts-search-transactions.md"
  - "paypal-payouts-view-transaction-activities.md"
  - "paypal-payouts-settlement-transaction-reports.md"
  - "paypal-payouts-login-with-paypal.md"
  - "paypal-payouts-venmo.md"
  - "paypal-payouts-sdk.md"
  - "paypal-payouts-webhooks.md"
  - "paypal-payouts-currency-conversion.md"
  - "paypal-payouts-country-feature.md"
  - "paypal-payouts-payment-processing.md"
  - "paypal-payouts-fees.md"
  - "paypal-payouts-troubleshooting.md"
  - "paypal-payouts-faq.md"
  - "paypal-payouts-overview-2025.md"
  - "paypal-payouts-product-overview.md"
  - "paypal-payouts-setup.md"
  - "paypal-payouts-plan.md"
  - "paypal-payouts-web-ui.md"
  - "paypal-payouts-large-batch-2025.md"
  - "paypal-payouts-api-2025.md"
  - "paypal-payouts-web-ui-customize.md"
  - "paypal-payouts-customize-api-2025.md"
  - "paypal-payouts-aac-2025.md"
  - "paypal-payouts-track-item-2025.md"
  - "paypal-payouts-cancel-reverse-2025.md"
  - "paypal-payouts-unclaimed-2025.md"
  - "paypal-payouts-reports-logs-2025.md"
  - "paypal-payouts-test-values-2025.md"
  - "paypal-payouts-sdk-2025.md"
  - "paypal-payouts-countries-features-2025.md"
tags: [paypal, payouts, disbursements, mass-payments, standard-payouts, advanced-payouts, hyperwallet, enterprise]
---

## Summary

Overview of PayPal's two payout tiers — Standard Payouts and Advanced Payouts — for sending money to multiple recipients (vendors, gig workers, disbursements).

## Key Takeaways

- **Standard Payouts**: self-serve, single program, email/phone/PayPal ID recipients, 96 countries, 20+ currencies
- **Advanced Payouts**: enterprise-grade, 240+ countries, 50+ currencies, multiple payment rails, personalized onboarding

## Feature Comparison

| Feature | Standard | Advanced |
| --- | --- | --- |
| Pay with PayPal and Venmo | ✓ | ✓ |
| API integration | ✓ | ✓ |
| Web-upload integration | ✓ | ✓ |
| File-transfer integration | ✓ | ✓ |
| Manage a single payout program | ✓ | |
| Self-serve onboarding | ✓ | |
| PayPal-managed experience | ✓ | |
| Detailed payout history | ✓ | |
| Pay with bank account or debit card | | ✓ |
| Pay with prepaid/virtual card or eGift card | | ✓ |
| Pay with check or cash at pickup | | ✓ |
| Multiple programs with one integration | | ✓ |
| Personalized onboarding | | ✓ |
| Drop-in UI integration | | ✓ |
| Pay portal or embedded experience | | ✓ |
| 1099 tax reporting | | ✓ |
| Detailed payee and transaction reporting | | ✓ |
| Multilingual payee support | | ✓ |
| **Currencies** | 20+ | 50+ |
| **Countries and regions** | 96 | 240+ |

## Payouts Web (Browser Upload)

- **Max 5,000 payments per file**; enable via account manager or 1-888-221-1161 (not self-serve)
- Browser UI: Money → Send Money → Make a Mass Payment → Browse CSV
- Duplicate detection: 30-day window (same as API)
- PayPal holds full payout amount + fees until status = Processed; declined items released back to balance
- Transaction statuses: Submitted → Processed / Completed

### CSV columns (10)

| # | Field | Notes |
| --- | --- | --- |
| 1 | Recipient identifier | Email, phone (Venmo), PayerID, or Venmo handle |
| 2 | Payment amount | Localized format; comma-separator currencies → enclose in double quotes |
| 3 | Currency | 3-letter code, case-insensitive; one per file |
| 4 | Customer ID | Optional; max 30 chars, no spaces |
| 5 | Note to recipient | Optional (PayPal), required (Venmo); max **400 chars** |
| 6 | Recipient Wallet | PAYPAL or VENMO (default: PAYPAL) |
| 7 | social_feed_privacy | Venmo only; PUBLIC / FRIENDS_ONLY / PRIVATE (default) |
| 8 | holler_url | Venmo only, deprecated; max 151 chars |
| 9 | logo_url | Venmo only; max 2000 chars, 1024×1024px square |
| 10 | Purpose | Optional; GOODS default; same 9 values as Large Batch |

## FAQ Highlights

- **Recipients pay no fees** — only the sender pays
- **$20k individual limit is raiseable** by contacting account representative or Customer Service
- **No conversion for ARS, BRL, MYR** (Argentina, Brazil, Malaysia)
- **Cancel only works on Unclaimed status** payments; API: Cancel unclaimed payout item endpoint
- **Unconfirmed recipient email** blocks payment until recipient confirms; appears in account within minutes after confirmation

> [!warning] Country count discrepancy
> FAQ says "156 countries, 23 currencies"; country feature page lists 96 countries. FAQ may count territories separately or may be outdated. Country feature page (updated 2025-05-08) is likely authoritative.

## Troubleshooting

- **Wrong email/phone**: PayPal **cannot reverse** funds for incorrect addresses — only remedy is to wait 30 days for unclaimed return, then resend to correct address
- **Missing email**: ask recipient to log into PayPal directly (may be in spam)
- **Unclaimed**: funds auto-returned after 30 days; view in transaction history

## Fees

- Sender pays fees at transaction time
- ~**2% variable** fee; domestic and international caps differ by country
- Funding account must hold total payout amount **plus fees** in sending currency
- **Individual payout max**: $20,000 USD (US) or local currency equivalent (other countries)
- **Total batch maximum**: unlimited
- Full fee schedule: [PayPal Merchant Fees](https://www.paypal.com/us/webapps/mpp/merchant-fees#paypal-payouts)

## Payment Processing & Payout Record Statuses

- Existing PayPal/Venmo account holders receive payment **instantly**
- Non-account holders get notification + signup link; **30 days** to claim or funds returned
- PayPal sends summary email per payout

### 10 payout record statuses

| Status | Meaning |
| --- | --- |
| New | Request received |
| Pending | Processing; funds reserved |
| Success | Credited to recipient |
| Unclaimed | No PayPal account; 30-day claim window active |
| Refunded | Recipient issued refund back to sender |
| Failed | Failed; **funds NOT deducted** from sender |
| On Hold | Under review |
| Blocked | Blocked |
| Denied | Denied; **funds NOT deducted** from sender |
| Returned | Claim window expired or sender cancelled |

## Country & Feature Support (96 countries)

4 feature tiers:

| Tier | Merchant can send? | Local currency? | Local language? |
| --- | --- | --- | --- |
| Fully localized | ✓ | ✓ | ✓ |
| Send, receive, and withdraw in local currency | ✓ | ✓ | — |
| Send, receive, and withdraw | ✓ | — | — |
| Receive and withdraw | ✗ | — | — |

**Merchant cannot send payouts to**: India (IN), Mexico (MX) — receive and withdraw only.

**Cross-border only** (no domestic payouts): Colombia (CO), Monaco (MC).

**China**: Country code is `C2` (not `CN`) — PayPal China Platform for cross-border payments settling in CNY.

Full country table in [[paypal-payouts-country-feature]].

## Currency Conversion

### Automatic conversion (21 currencies)

AUD, CAD, EUR, MXN, GBP, USD, CHF, SEK, PLN, NOK, HUF, DKK, CZK, ILS, HKD, NZD, IDR, PHP, JPY, SGD, TWD

**Zero-digit currencies** (no decimal places in amount): HUF, JPY, TWD

### Exclusions (no conversion)

- **Asia**: China, India, South Korea, Taiwan, Thailand, Turkey — conversion not available
- **Caribbean** (15 countries) + **Latin America** (17 countries): USD only; recipients withdraw in local currency from their bank

### Restrictions

| Country | Currency | Rule |
| --- | --- | --- |
| Brazil | BRL | In-country PayPal accounts only; non-Brazilian recipients get converted to primary currency + PayPal spread fee |
| Malaysia | MYR | MYR only between Malaysian users; no cross-border MYR exchange |

## Webhook Events (11)

**PAYOUTSBATCH webhooks contain no item-level information** — use HATEOAS links from the webhook response to get item details.

| Event | Trigger |
| --- | --- |
| PAYMENT.PAYOUTSBATCH.DENIED | Batch denied |
| PAYMENT.PAYOUTSBATCH.PROCESSING | Batch entered processing |
| PAYMENT.PAYOUTSBATCH.SUCCESS | Batch completed successfully |
| PAYMENT.PAYOUTS-ITEM.BLOCKED | Item blocked |
| PAYMENT.PAYOUTS-ITEM.CANCELED | Item canceled |
| PAYMENT.PAYOUTS-ITEM.FAILED | Item failed |
| PAYMENT.PAYOUTS-ITEM.HELD | Item held |
| PAYMENT.PAYOUTS-ITEM.REFUNDED | Item refunded |
| PAYMENT.PAYOUTS-ITEM.RETURNED | Item returned (unclaimed after 30 days) |
| PAYMENT.PAYOUTS-ITEM.SUCCEEDED | Item succeeded |
| PAYMENT.PAYOUTS-ITEM.UNCLAIMED | Item unclaimed |

## Payouts REST SDK

Available in Java, PHP, Python, .NET. Handles OAuth 2.0 token acquisition and API updates automatically.

| Language | Install |
| --- | --- |
| PHP | `composer require paypal/paypal-payouts-sdk ~1.0.0` |
| Python | `pip install paypal-payouts-sdk` |
| Java | Maven: `com.paypal.sdk:payouts-sdk:1.0.0` |
| .NET | `dotnet add package PayoutsSdk --version 1.0.0` |

Environment: `SandboxEnvironment` for testing, `LiveEnvironment` for production. GitHub: [PHP](https://github.com/paypal/Payouts-PHP-SDK) | [Python](https://github.com/paypal/Payouts-Python-SDK) | [Java](https://github.com/paypal/Payouts-Java-SDK) | [.NET](https://github.com/paypal/Payouts-DotNet-SDK)

## Payouts to Venmo

**US only.** 40M+ Venmo users. Note is required for all Venmo payouts; message appears in recipient's feed inheriting their privacy settings.

| Field | Values |
| --- | --- |
| `recipient_wallet` | `Venmo` (note: capital V, unlike `PAYPAL` which is all-caps) |
| `recipient_type` | `PHONE`, `EMAIL`, or `USER_HANDLE` (Venmo handle) |

Supported across all 3 integration methods:

- **API**: set `recipient_wallet: Venmo`, `recipient_type`, and `receiver`
- **Payouts Web**: add Recipient Wallet column with `Venmo`; note required
- **Large Batch**: use `PAYOUT_VENMO` row type with phone number

Unregistered recipients get a text to create a Venmo account and claim the payout.

> [!info] Venmo handle support
> `USER_HANDLE` recipient type is a newer addition — allows sending directly to a Venmo username rather than phone/email.

## Assisted Account Creation (AAC) — Log in with PayPal for Payouts

AAC lets customers log in/sign up via PayPal; merchant receives payer ID + email. **Payer IDs are the most reliable recipient identifier** for payouts.

- Requires account manager to enable identity services + register return URLs
- Works with all 3 integration methods (API, Large Batch, Payouts Web)

### Integration

**Client-side**: `paypal.PayoutsAAC.render()` using Zoid cross-domain library; supports vanilla JS, React, Angular. Props: `env`, `clientId`, `merchantId`, `pageType` (signup/login), `onLogin`.

**Server-side** (2 calls):

1. `POST /v1/identity/openidconnect/tokenservice` — exchange auth code for access token
2. `GET /v1/oauth2/token/userinfo?schema=openid` — get email + payer ID

SDK: Node (`paypal-rest-sdk`), Python (`paypalrestsdk`)

## Settlement & Transaction Detail Reports

**Approved merchants only** — requires PayPal account manager approval.

### Payouts T-codes

| T-code | Meaning |
| --- | --- |
| T0001 | Mass Payment — successful |
| T0104 | Mass Payment batch fee |
| T1105 | Account hold released (processing complete) |
| T1114 | Mass Payment reversal |
| T1115 | Mass Payment refund |
| T1503 | Temporary hold on funds during processing |

T1503 → T1105 lifecycle: hold placed when batch starts, released when complete. Declined payments do **not** appear in either report.

Both reports accessible via PayPal UI (Activity → All Reports → Transactions) or PayPal Secure FTP Server.

## Transaction Activity Error Codes (42)

Full error/reason code table in [[paypal-payouts-view-transaction-activities]]. Key entries:

| Code | Error | Note |
| --- | --- | --- |
| 1002 | INSUFFICIENT_FUNDS | Add funds to PayPal balance |
| 1005 | PENDING_RECIPIENT_NON_HOLDING_CURRENCY_PAYMENT_PREFERENCE | Recipient reviewing credits in this currency — check back |
| 3769 | CLOSED_MARKET | Account can't receive from other countries |
| 14765 | RECEIVER_UNREGISTERED | No account; signup link sent; 30-day claim window |
| 14766 | RECEIVER_UNCONFIRMED | Unconfirmed email/phone; funds returned after 30 days |
| 14776 | TRANSACTION_DECLINED_BY_TRAVEL_RULE | Retry as new batch |
| 14800 | POS_LIMIT_EXCEEDED | POS cumulative spending limit exceeded |
| 14801 | UNVERIFIED_RECIPIENT_NOT_SUPPORTED | Account restricted to verified recipients only |

## Reporting

- **Transaction Finder**: Activity → All Reports → Activity download → search icon; filter by Transaction type = **Mass payments**, date range, currency; results show Date/Type/Name/Subject/Gross/Fees/Net; downloadable
- **Activities Download Report**: full transaction history for any period in the **last 3 years**; Activity → All Reports → Activity download → Create Report

### Payouts Web Customization

- **Currency conversion**: preview shown before sending — includes fees + exchange rate; separate file per currency
- **Activity export**: downloadable CSV and TXT files include exchange rate, fee, and total in both currencies
- **Payout approvals** (maker-checker): Account Settings → Account access → Manage users → Manage Approvals; **one user cannot both initiate and approve a payout**

> [!info] Note length difference
> Payouts Web note max: **400 chars**. Large Batch `ITEM_LEVEL_NOTE` max: **1000 chars**. API `note` field should be verified separately.

## Large Batch (SFTP / DropZone)

Recommended for >15,000 payouts. No upper limit on recipients. Files processed in chunks of up to 500,000 records.

### Transport

| Environment | SFTP endpoint | Port |
| --- | --- | --- |
| Sandbox | `dropzone.es-ext.paypalcorp.com` | 22 |
| Production | `dropzone.paypal.com` | 22 |

### File format

- CSV (`.csv` or `.csv.gz`); UTF-8 encoding required; one currency per file
- Naming: `pp_payouts_<epoch_time>_<reference_name>.<format>`
  - `reference_name`: alphanumeric + `_` `-` only; max 63 chars
  - Future timestamps must be within 7 days of upload time

### CSV structure

Line 1 — summary: `PAYOUT_SUMMARY,TOTAL_AMOUNT,CURRENCY,COUNT,EMAIL_SUBJECT,EMAIL_MESSAGE`

Lines 2+ — items: `PAYOUT|PAYOUT_VENMO,RECIPIENT,AMOUNT,CURRENCY,UNIQUE_REF_ID,NOTE,[SOCIAL_FEED_PRIVACY],[HOLLER_URL],[LOGO_URL],[PURPOSE]`

- `UNIQUE_REF_ID`: alphanumeric + `_` `-`; max 30 chars
- `ITEM_LEVEL_NOTE` / `EMAIL_MESSAGE`: max 1000 chars; `EMAIL_SUBJECT`: max 256 chars
- `PURPOSE` values: AWARDS, PRIZES, DONATIONS, **GOODS** (default), SERVICES, REBATES, CASHBACK, DISCOUNTS, NON_GOODS_OR_SERVICES
- Venmo `SOCIAL_FEED_PRIVACY`: PUBLIC, FRIENDS_ONLY, **PRIVATE** (default)

### Acknowledgment reports

| Report | Meaning |
| --- | --- |
| ACK | Validation passed; processing begins |
| NACK | Validation failed; errors listed per line |
| DUPS | Duplicate filename detected |

NACK triggered if content matches a file sent within 7 days (overridable by account manager).

### Processing reports

| Report | Trigger | Filename pattern |
| --- | --- | --- |
| Part File | After each 500k-record chunk | `..._1_350.csv` |
| Out / Interim | After all chunks complete | `..._OUT.csv` |
| Final | 31 days after Interim | `..._FINAL.csv` |

Report columns: `REF_ID, PAYOUT_ITEM_ID, TRANSACTION_ID, RECIPIENT_NAME, RECIPIENT, CURRENCY_CODE, PAYOUT_AMOUNT, FEE, TOTAL, TRANSACTION_STATUS, ERROR_ENUM, ERROR_MESSAGE, TIME_PROCESSED, TIME_CLAIMED`

**Unclaimed payouts returned to sender after 30 days.**

> [!info] EMAIL_SUBJECT character limit discrepancy
> Large Batch page says max 256 chars; file validation errors page says 255. The errors page is likely authoritative as it defines the enforced validation limit.

### File validation error codes (28)

DUPLICATE_REF_ID, EMAIL_MESSAGE_EXCEEDED_MAX_SIZE, EMAIL_SUBJECT_EXCEEDED_MAX_SIZE, ENCODING_ERROR, FILE_EMPTY_OR_CORRUPT, FILE_NOT_FOUND, FILE_SIZE_ERROR, GZ_FILE_CORRUPT_ERROR, INVALID_CURRENCY, INVALID_FILE_FORMAT, INVALID_FILE_NAME, INVALID_FIRST_COLUMN, INVALID_REF_ID_FORMAT, INVALID_SUMMARY_LINE_POSITION, MANDATORY_COLUMN_MISSING, MULTI_CURRENCY_NOT_SUPPORTED, MULTIPLE_SUMMARY_RECORDS, PAYOUT_AMOUNT_INVALID_FORMAT, PAYOUT_AMOUNT_NON_POSITIVE, SANDBOX_LIMIT_ERROR, SCHEDULED_TIME_ERROR, SUMMARY_AMOUNT_INVALID_FORMAT, SUMMARY_AMOUNT_NON_POSITIVE, SUMMARY_AND_PAYOUT_MATCH_CONFLICT, SUMMARY_LINES_NON_INTEGER, SUMMARY_LINES_NON_POSITIVE, SUMMARY_MISSING, TOTAL_PAYMENTS_MISMATCH, INVALID_PURPOSE

## Testing & Go Live

- **Simulation**: JSON pointer in `items[0]/note` (ERRPYO*/POSPYO*) or path parameter (`/v1/payments/payouts/ERRPYO015`)
- **POST rate limit**: 400 calls; HTTP 429 = RATE_LIMIT_REACHED; avoid polling, cache OAuth tokens
- **Webhook gotcha**: failed payout webhooks contain no error object — must `GET` the item to get error details
- **Batch status test values**: ERRPYOB001 → SUCCESS, ERRPYOB002 → PENDING, ERRPYOB003 → PROCESSING, ERRPYOB004 → DENIED
- **Go live**: change base URL from `api-m.sandbox.paypal.com` → `api-m.paypal.com`; swap to live credentials; update JS SDK client ID

### Notable error codes

| Code | Meaning |
| --- | --- |
| SENDER_EMAIL_UNCONFIRMED | Sender email not confirmed |
| INSUFFICIENT_FUNDS | Insufficient PayPal balance |
| RECEIVER_YOUTH_ACCOUNT | Recipient has youth account |
| RECEIVER_COUNTRY_NOT_ALLOWED | Recipient country blocked |
| TRANSACTION_DECLINED_BY_TRAVEL_RULE | Travel rule compliance block |
| CIP_NOT_VERIFIED | Sender identity not verified |
| CLOSED_MARKET | Cross-country market closed |
| NON_HOLDING_CURRENCY | Currency not held in balance |
| REGULATORY_BLOCKED / REGULATORY_PENDING | Regulatory compliance hold |

## API Customization

- **Show batch details**: `GET /v1/payments/payouts/{payout_batch_id}?fields=batch_header` — filter to batch header only; `batch_status: ACKNOWLEDGED`
- **Idempotency**: retry 5xx with same `PayPal-Request-Id`; two simultaneous requests with same header → first wins, second fails
- **Duplicate prevention**: `sender_batch_id` dedup window = **30 days**; duplicate rejected with HATEOAS link to original; 5xx retries with same `sender_batch_id` are safe
- **Currency conversion response**: includes `currency_conversion.from_amount` / `to_amount` + `fees`; `funding_source: BALANCE`

## API Integration

- **Endpoint**: `POST /v1/payments/payouts`
- **Max 15,000 payments per API call**
- **One currency per batch** — separate API call required for each currency
- Response: HTTP 201 + `payout_batch_id` with `batch_status: PENDING`; poll `GET /v1/payments/payouts/{payout_batch_id}` for item-level details

### Request structure

```json
{
  "sender_batch_header": {
    "sender_batch_id": "unique-id",
    "recipient_type": "EMAIL",
    "email_subject": "...",
    "email_message": "..."
  },
  "items": [{
    "amount": { "value": "9.87", "currency": "USD" },
    "receiver": "recipient@example.com",
    "sender_item_id": "item-001",
    "recipient_wallet": "PAYPAL"
  }]
}
```

### Key field rules

- `recipient_type`: EMAIL, PHONE, or PAYPAL_ID. Item-level overrides batch-level; if no batch-level, each item must define its own
- `recipient_wallet`: PAYPAL or VENMO; Venmo requires U.S. mobile number + `note`
- Currency: set per item; one currency per batch call; automatic conversion available for some currencies

## Standard Payouts Detail

- **Currency count**: 24 (overview page says "20+" — Standard page is more specific)
- **Access**: requires manual approval from PayPal; sandbox testing available while pending
- **Prerequisites**: PayPal business account + confirmed identity + confirmed email + linked bank account + sufficient PayPal balance
- **Funded from**: PayPal balance (not charged to card/bank at send time)
- **Venmo**: US + USD only; requires U.S. mobile number; mobile only
- **Currency flexibility**: some currencies sent via automatic conversion without holding that balance; others require manual balance transfer first

### Three integration options

| Option | Description |
| --- | --- |
| API integration | Initiate payout requests via Payouts API |
| Large Batch | Create and upload payout files to a secure FTP server |
| Payouts Web | Create and upload payout files via browser |

> [!info] Currency count
> Overview page says "20+ currencies"; Standard Payouts page (updated 2025-11-25) says "24 currencies". 24 is the more specific and likely correct value.

## Related Pages

- [[paypal]] — company page
- [[paypal-payouts]] — payouts concept page

## Raw Sources

- [[paypal-payouts-overview]] — verbatim PayPal Payouts overview page
- [[paypal-payouts-standard]] — Standard Payouts detail: 24 currencies, prerequisites, 3 integration options, Venmo constraints, currency flexibility
- [[paypal-payouts-integrate-api]] — API integration guide: POST /v1/payments/payouts, 15k limit, batch structure, recipient_type precedence, one currency per call
- [[paypal-payouts-customize-api]] — Customize: show batch details, idempotency, 30-day sender_batch_id dedup, currency conversion response shape
- [[paypal-payouts-test-go-live]] — Test & go live: ERRPYO*/POSPYO* trigger codes, POST rate limit 400, webhook no-error-object gotcha, go-live URL swap
- [[paypal-payouts-large-batch]] — Large Batch: SFTP DropZone, >15k payouts, 500k records/part, CSV format, ACK/NACK/DUPS, 30-day unclaimed return, 31-day Final report
- [[paypal-payouts-file-validation-errors]] — 28 file validation error codes for Large Batch CSV uploads
- [[paypal-payouts-web]] — Payouts Web: 5k limit, 10-column CSV, browser upload flow, 30-day dedup, hold-until-processed behavior
- [[paypal-payouts-web-customize]] — Payouts Web customize: currency conversion preview, CSV/TXT activity export, maker-checker payout approvals
- [[paypal-payouts-reports]] — Reports index: search transactions, view activity, Settlement and Transaction Details reports
- [[paypal-payouts-search-transactions]] — Search transactions: Transaction Finder (Mass payments filter), Activities Download (3-year history)
- [[paypal-payouts-view-transaction-activities]] — Transaction activities: 30-day default, BatchLog.txt details, 42 error/reason codes
- [[paypal-payouts-settlement-transaction-reports]] — Settlement & Transaction Detail reports: approved merchants only, 6 T-codes, T1503→T1105 hold lifecycle, declined payments excluded
- [[paypal-payouts-login-with-paypal]] — AAC (Log in with PayPal for Payouts): payer ID acquisition, Zoid SDK, 2-step server-side OAuth, Node/Python support
- [[paypal-payouts-venmo]] — Payouts to Venmo: US only, 40M users, PHONE/EMAIL/USER_HANDLE recipient types, note required, all 3 integration methods
- [[paypal-payouts-sdk]] — Payouts REST SDK: Java/PHP/Python/.NET, handles OAuth automatically, install commands + environment setup
- [[paypal-payouts-webhooks]] — Payouts webhook events: 3 batch + 8 item events; PAYOUTSBATCH has no item info (use HATEOAS links)
- [[paypal-payouts-currency-conversion]] — Currency conversion: 21 automatic currencies, 3 zero-digit currencies, exclusions (6 Asia + 32 Caribbean/LatAm), Brazil/Malaysia restrictions
- [[paypal-payouts-country-feature]] — Country & feature support: 96 countries, 4 tiers, India/Mexico receive-only, China C2 code, Colombia/Monaco cross-border only
- [[paypal-payouts-payment-processing]] — Payment processing: instant for existing accounts, 30-day unclaimed window, 10 payout record statuses
- [[paypal-payouts-fees]] — Fees: ~2% variable, country-specific caps, $20k individual max, unlimited batch total, sender pays at transaction time
- [[paypal-payouts-troubleshooting]] — Troubleshooting: no reversal for wrong email/phone (wait 30 days), resend to corrected address, spam folder tip
- [[paypal-payouts-faq]] — FAQ: recipients pay no fees, $20k limit raiseable, ARS/BRL/MYR no conversion, cancel = unclaimed only, unconfirmed email blocks payment
- [[paypal-payouts-overview-2025]] — docs.paypal.ai tier comparison: PayPal (96 countries, 20+ currencies, self-serve) vs Enterprise/Hyperwallet (240+ countries, 50+ currencies, prepaid cards, check/cash, 1099 tax reporting, multilingual)
- [[paypal-payouts-product-overview]] — docs.paypal.ai product overview: 96 countries, 24 currencies, 3 integration patterns (Web UI/SFTP/API), 4-step flow diagram, $20k individual limit/unlimited batch, business approval required, recipients pay no fees
- [[paypal-payouts-setup]] — Setup guide: SFTP DropZone endpoints (dropzone.paypal.com port 22, sandbox dropzone.es-ext.paypalcorp.com), 48h onboarding, SSH/password auth; API sandbox: create Merchant app + webhook; live: identity+email+bank verify then request activation
- [[paypal-payouts-plan]] — Integration pattern decision guide: Web UI (low freq, no-code) vs SFTP/DropZone (high volume batch) vs API (high freq, automation); payout methods: PayPal + Venmo
- [[paypal-payouts-web-ui]] — Web UI CSV guide: max 5000 rows, 9-field format, one currency per file, decimal comma for EUR/BRL (quote-wrap), note required for Venmo, Holler URL deprecated, 9 purpose values, 30-day duplicate warning
- [[paypal-payouts-large-batch-2025]] — Large-batch SFTP guide (docs.paypal.ai): 15k+ recipients, file naming `pp_payouts_{epoch}_{name}.csv`, PAYOUT_SUMMARY first row, 3 ACK reports, 3 stage reports, 31-day Final report, 26 error codes; ⚠️ email subject 255 chars here vs 256 in Web UI doc
- [[paypal-payouts-api-2025]] — Payouts API guide (docs.paypal.ai): POST /v1/payments/payouts, 400 req/min rate limit, sender_batch_id idempotency, recipient_type (EMAIL/PHONE/USER_HANDLE/PAYPAL_ID), Venmo US-only, test simulation via note field or path param
- [[paypal-payouts-web-ui-customize]] — Web UI customization: local currency payouts (one file per currency, conversion preview at review step); approval flow setup (maker-checker, creator cannot approve own payout)
- [[paypal-payouts-customize-api-2025]] — Payouts API customization (docs.paypal.ai): currency conversion response shape (currency_conversion.from_amount/to_amount/exchange_rate per item); fields query param for batch_header-only response; sender_batch_id 30-day dedup; PayPal-Request-Id idempotency (simultaneous duplicates → first wins)
- [[paypal-payouts-countries-features-2025]] — Countries & supported features (docs.paypal.ai): 96 countries with full country-code table; 4 feature tiers; Brazil=Fully localized; India/Mexico=Receive+withdraw only; China C2/Colombia/Monaco cross-border only; country restrictions: BRL/MYR/CNY/COP/EUR; **20** auto-conversion currencies (dropped TWD vs older page's 21); Caribbean 15 + LatAm 17 exclusions; Venmo US-only

> [!warning] Auto-conversion currency count discrepancy
> This page (docs.paypal.ai 2026) lists **20** currencies for automatic conversion — Taiwan dollar (TWD) is absent. The older `paypal-payouts-currency-conversion.md` listed 21 including TWD. The newer page is likely authoritative.

- [[paypal-payouts-sdk-2025]] — Payouts SDK (docs.paypal.ai): Java (Maven 1.1.1) + Python only (drops PHP/.NET); SandboxEnvironment/LiveEnvironment; create batch (Java 5 items via IntStream, Python 2 items); track: PayoutsGetRequest with page/pageSize/totalRequired (max 1000/page); GitHub refs for Java+Python
- [[paypal-payouts-test-values-2025]] — Payouts API test values (docs.paypal.ai): 5 operations; Create batch: POSPYO001/003 positive, 16 negative via note/sender_batch_id (ERRPYO013 triggers via sender_batch_id for Venmo note missing); Track: ERRPYOB001-004; Show details: 32 negative path params; Cancel: ERRPOI001/ERRPYO004/007-009; Show item: 31 negative; case-sensitive
- [[paypal-payouts-reports-logs-2025]] — Reports & transaction logs (docs.paypal.ai): Activity report (customizable fields, 3yr history); Settlements report (sent+refunded, excludes declined, needs approval); Transaction details report (all, excludes declined, needs approval); 6 T-codes; transaction log CSV/TXT download with FX rate; 42 error/reason codes (HTTP 400/403/429/504 + numeric 1000–14802) including gaming codes (9500-9502)
- [[paypal-payouts-unclaimed-2025]] — Handle unclaimed payouts (docs.paypal.ai): 3 causes (wrong details, unverified email, unaccepted payment); track via Activity report; resolve: wrong→cancel+resend, correct→notify recipient; 3 best practices; 30-day auto-return
- [[paypal-payouts-cancel-reverse-2025]] — Cancel/reverse payouts (docs.paypal.ai): cancel only UNCLAIMED items; Dashboard (Activity→Transactions search) or API (POST /v1/payments/payouts-item/{id}/cancel, empty body); cancel response → RETURNED + errors object; no reversal for wrong email/phone if claimed; 30-day auto-return for unclaimed
- [[paypal-payouts-track-item-2025]] — Track payout item status (docs.paypal.ai): GET /v1/payments/payouts-item/{id}; 9 transaction_status values (SUCCESS/FAILED/PENDING/UNCLAIMED/RETURNED/ONHOLD/BLOCKED/REFUNDED/REVERSED); REVERSED is web-upload-only; response includes sender_batch_id

> [!info] Status count update
> This page lists 9 `transaction_status` values for payout items including REVERSED (web-upload only). The existing summary table shows 10 payout record statuses (includes "New" and "Denied" which may be batch-level only). The two sets may represent different scopes (item-level API vs. dashboard display).

- [[paypal-payouts-aac-2025]] — AAC (docs.paypal.ai): payouts_aac.js SDK; PayoutsAAC.render() props (env/clientId/merchantId/pageType/onLogin); React driver + Angular kebab-case; server-side: tokenservice then userinfo?schema=openid; Node (paypal-rest-sdk) + Python (paypalrestsdk); requires PayPal to enable identity services + 3 scopes (email, verification, payer ID)
