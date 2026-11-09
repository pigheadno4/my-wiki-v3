---
title: "Stripe: ACH SEC Codes Overview"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/payments/ach-direct-debit/sec-codes
raw_files:
  - "stripe-payments-ach-direct-debit-sec-codes-2026-11-07.md"
  - "stripe-ach-sec-codes-2025.md"
tags: [stripe, ach, us-bank-account, sec-codes, mandates, nacha, web, ccd, ppd, tel]
---

## Summary

Standard Entry Class (SEC) codes describe how a customer or business authorized an ACH transaction. Nacha defines the codes, and the captured Stripe guide says a business is responsible for indicating the appropriate code and retaining suitable authorization evidence. The November 7, 2026 capture still describes four supported codes: WEB, CCD, PPD, and TEL. TEL is labeled **private preview** in that capture; this does not establish access for any particular Stripe account.

The documentation presents mandate and rule information as general guidance and points readers to a professional for obligations specific to their situation. Its examples do not establish that a transaction or mandate complies with Nacha or applicable law.

## Codes and Defaults

When no mandate collection method is specified, the captured guide says Stripe defaults to WEB for consumer bank accounts and CCD for business bank accounts.

| Code | Captured use and boundary |
| --- | --- |
| WEB (Internet Initiated or Mobile Entry) | Consumer debit initiated on the internet or mobile; refunds for WEB transactions use PPD |
| CCD (Corporate Credit or Debit Entry) | Business-to-business payments; applies to charges on PaymentMethods with `account_holder_type=company`, regardless of authorization type |
| PPD (Prearranged Payment and Deposit) | Consumer standing or single-entry authorization in writing, signed or otherwise authenticated; provide the customer a copy |
| TEL (Telephone-Initiated Entry) | Consumer authorization by phone; November guide labels it private preview and limits it to single entries, not standing or recurring transactions |

## PPD Mandate and Examples

The captured guide says PPD authorization must include information required for online mandates, be in writing and signed or otherwise authenticated, and be copied to the customer. To initiate a PPD debit, it directs creation of a mandate with **offline customer acceptance** and a `us_bank_account` mandate option `collection_method=paper`. The November PaymentIntent and SetupIntent **confirmation examples** use curl, with `mandate_data[customer_acceptance][type]=offline`, an `accepted_at` timestamp, and `payment_method_options[us_bank_account][mandate_options][collection_method]=paper`. The May 2 capture showed corresponding Node examples. This is an example-language change, not evidence that the SDK path was deprecated or that the example timestamp is a general constant.

See new raw:25-49 and old raw:24-82 for the full authorization wording and examples. PPD offline acceptance does not itself confer TEL preview access or replace TEL's separate authorization conditions.

## TEL: November 7 Private Preview Guidance

The November capture says to contact Stripe Support if initiating consumer bank debits authorized over the telephone. Its **private preview** label does not establish merchant eligibility or enabled account access.

For a single TEL entry, the guide allows either of these relationship routes:

- A direct existing merchant-customer relationship through a written goods or services agreement, **or** a purchase from that merchant within the past two years.
- No direct existing relationship, **if the customer initiated the telephone call to the merchant**.

A relationship only with an affiliate does not satisfy the direct existing-relationship route. The guide excludes standing authorization and recurring transactions from TEL entries.

The guide requires commercially reasonable procedures to verify customer identity and routing-number validity. Before initiating the debit, it requires explicit oral authorization containing information required for online mandates plus a customer inquiry telephone number. Authorization must be captured by an audio recording of the customer's oral authorization, subject to applicable call-recording law, **or** by written notice provided before the first bank-account debit. The page supplies sample oral wording and says a single-entry written-notice flow should indicate the delivery method; it does **not** prescribe that sample as a verbatim script. See new raw:55-82 and old raw:88-115.

> [!warning] Contradiction: the prior wiki summary described TEL as private beta, required an existing relationship without the customer-initiated-call alternative, and called the sample wording a required script. The November capture calls TEL private preview and expressly includes the alternative and required authorization content. Preview status is a captured label, not a guarantee of access.

## Related Pages

- [[stripe-ach-direct-debit]] — ACH Direct Debit concept
- [[source-stripe-ach-direct-debit]] — broader ACH Direct Debit source
- [[stripe]] — provider

## Raw Sources

- [[raw/stripe-payments-ach-direct-debit-sec-codes-2026-11-07|November 7 SEC codes capture]] — current captured label, curl PPD examples, and TEL conditions
- [[raw/stripe-ach-sec-codes-2025|May 2 SEC codes capture]] — earlier wording and Node PPD examples
