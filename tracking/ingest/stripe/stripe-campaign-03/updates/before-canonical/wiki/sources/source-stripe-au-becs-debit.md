---
title: "Stripe: Australia BECS Direct Debit Payments"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-au-becs-debit-2025.md"
tags: [stripe, au-becs, becs, australia, aud, bank-debit, mandates, disputes]
---

## Summary

Reference page for Australia BECS Direct Debit on Stripe. AU-only bank debit requiring a mandate (DDR). Covers settlement, disputes, mandates, refunds, debit notification emails, and statement descriptors. API enum: `au_becs_debit`.

## Key Details

**Limits**: 10,000 AUD per transaction and 10,000 AUD per week for new users.

**Settlement**: T+2 payment success and funds available; cutoff 18:30 Australia/Melbourne. Funds debited from customer's account at T+0.

**Disputes**: up to 7 years, "no questions asked"; final and uncontestable. Stripe sends `charge.dispute.created` + `charge.dispute.closed` simultaneously.

**Mandates (DDR)**: Direct Debit Requests require account holder name, BSB number, account number + mandate Service Agreement. Customer can cancel at any time via bank or merchant → new mandate required.

Mandate event: `mandate.updated` fires when canceled or permanently failed → `status` becomes `inactive`.

**Debit notification emails**: BECS scheme advises (not mandatory) notifying customer when mandate established and before each debit. Default Stripe email sent day before debit. Custom emails: turn off Stripe emails, trigger on `payment_intent.processing`. Should include last 4 digits of account, amount, contact info, debit date. Suggested lead time: 14 calendar days (not mandatory).

**Refunds**: 90-day window; 3–5 business days to process. Labeled as credit (not refund) on bank statement. Risk of double-credit if refund issued while dispute in flight.

**Statement descriptors**: two fields: merchant name (statement descriptor) + lodgement reference (first 9 alphanumeric chars + unique ID). Dynamic override via `statement_descriptor` on PaymentIntent. Connect `on_behalf_of` changes descriptor source to connected account.

**Test credentials**: BSB `000000`, account `000123456`.

**Product support**: Connect, Checkout, Payment Links, Subscriptions, Invoicing, Elements (not Express Checkout Element).

**Billing Retries** (private preview): auto-retry for insufficient funds on subscription or one-off invoices.

## Raw Sources

- [[stripe-au-becs-debit-2025]] — verbatim webpage content; reuses 3 generic flow SVGs from `raw/assets/stripe-acss-debit-*.svg`
