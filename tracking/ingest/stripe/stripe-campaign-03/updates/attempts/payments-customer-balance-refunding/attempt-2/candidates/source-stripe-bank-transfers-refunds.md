---
title: "Stripe: Refund Bank Transfer Payments"
type: source
date_ingested: 2026-05-05
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/customer-balance/refunding"
raw_files:
  - "stripe-payments-customer-balance-refunding-2026-11-07.md"
  - "stripe-bank-transfers-refunds-2025.md"
tags: [stripe, bank-transfers, refunds, customer-balance, payments]
---

## Summary

The November 7, 2026 full guide and the older capture describe three destinations or origins: refund a bank-transfer payment to the customer's bank, refund that payment to the customer's **cash balance**, or return available customer cash balance to the customer's bank. The two bank-directed procedures have different origins and cancellation surfaces. The older capture also includes locally downloaded screenshots and Node examples; the newer capture presents curl examples and CDN images without establishing a new refund capability.

## Payment refund to the customer's bank

Stripe needs destination bank account details. It may already have them from the transfer; when details are missing or ambiguous, Stripe requests them at the email on the Customer object. If the Customer has no email, creating the refund can fail; update the Customer or supply another address with `instructions_email`. Stripe might perform additional checks before processing or requesting bank details. A payment can be refunded up to **180 days after creation**. Each refund, including a partial refund, might incur a fee.

From the payment page, select **Refund**, enter the amount and details, and submit. The November API example creates a Refund using `payment_intent` and optional `instructions_email`:

```bash
curl https://api.stripe.com/v1/refunds \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_intent={{PAYMENTINTENT_ID}}" \
  --data-urlencode "instructions_email=customeremail@example.com"
```

The May capture shows the corresponding `stripe.refunds.create({ payment_intent, instructions_email })` Node example. These are dated examples of the same path, not evidence of client or API removal.

For a **bank-directed payment refund**, the documented Refund states are:

| Event | Refund status |
| --- | --- |
| Created while awaiting bank details | `requires_action` |
| Customer supplies bank details and processing begins | `pending` |
| Successfully paid out to customer | `succeeded` |
| Recipient bank returns funds | `requires_action` again; Stripe asks for corrected details |
| Remains in `requires_action` at the stated timeout | `failed`, with `refund.failed` |
| Canceled before the customer supplies details | `canceled` |

`pending` means processing, not receipt by the customer. Track the Refund in the Dashboard or retrieve its Refund object. `instructions_email` records the recipient address; while waiting for a reply, `next_action.display_details.email_sent` can show the address and send time, which the guide also ties to transition into `requires_action`.

### Cancel this payment refund

Before the customer supplies bank details, cancel the `requires_action` refund on the payment page using **Cancel refund**; if several partial refunds are waiting, select the correct Refund. The November API example is `POST /v1/refunds/{id}/cancel`; the older capture shows `stripe.refunds.cancel({ refund: id })`. Cancellation changes the Refund to `canceled`; with no other refunds, the payment returns to its original pre-refund state.

## Payment refund to customer cash balance

On the payment page, choose **Refund** and then **Customer cash balance** in the **Destination** dropdown. The credit succeeds immediately, is free of charge, and leaves funds available for future payments on the merchant's site. This guide gives a Dashboard procedure for this direction. Neither pinned capture documents a `destination: 'customer_balance'` API argument for it; the `origin: 'customer_balance'` request below is the *reverse* direction. Do not apply the bank-directed `requires_action` lifecycle or possible fee to this immediate credit.

## Return available customer cash balance to the customer's bank

For available cash balance, such as an excess bank transfer, open the Customer's **Cash Balance** row in **Payment methods** and choose **Initiate Refund**. The API example creates a Refund with `origin=customer_balance`, `customer`, `amount`, and `currency`; `instructions_email` can override the Customer's default address:

```bash
curl https://api.stripe.com/v1/refunds \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1099 \
  -d currency=usd \
  -d "customer={{CUSTOMER_ID}}" \
  --data-urlencode "instructions_email=jenny.rosen@example.com" \
  -d origin=customer_balance
```

The older capture gives the same parameters in a Node `stripe.refunds.create` example. The Customer identity and cash-balance origin distinguish this from refunding a PaymentIntent.

### Cancel this cash-balance return

Only an unprocessed return can be canceled, before the customer submits bank account details. The captured guide directs users to the **Dashboard only**: open the Customer's cash-balance details, use the refund row's overflow menu, and select **Cancel**. The refund amount is credited back to available cash balance. The payment-refund cancellation API above is not presented as the interface for this cash-balance return.

## Captured 45-day wording conflict

Both captures say the customer has **45 days from receipt of the request** to submit bank details and that, without a valid response, Stripe cancels the refund and returns funds to customer cash balance. Their bank-refund status table instead says a Refund still in `requires_action` **45 days after creation** becomes `failed`; nearby prose says `refund.failed` fires and the merchant must return the funds outside Stripe. These passages leave the start of the clock, resulting status, and funds destination unresolved. Preserve both dated statements and confirm the actual Refund and ledger state before deciding how to return funds; a created or pending Refund does not prove customer receipt.

## International wires and sandbox

The guide says Stripe does not support automatic refunds or automated refund emails for international **SWIFT** payments. It describes moving unreconciled customer cash balance to the merchant's Stripe account balance, then paying out to the merchant's external bank, collecting the customer's bank details directly, and returning and notifying the customer through a separate method. The refund guide (new raw line 161; old raw line 172) also says to wait for an automatic merchant-balance sweep after **75 days**. That timing conflicts with the November bank-transfer overview (raw/stripe-payments-bank-transfers-2026-11-07.md:144) and the May reconciliation guide (raw/stripe-customer-balance-reconciliation-2025.md:300): those say Stripe **attempts to return** unreconciled funds after 75 days and sweeps them to the merchant's Stripe balance at the **90-day mark only if** it cannot determine the customer's account information. A 75-day merchant-balance credit is therefore not guaranteed by these captures. Check the actual balance and reconciliation state before initiating a payout. This manual return is not a native Stripe SWIFT refund.

The captures list sandbox fixtures for IBAN countries, Japan, Mexico, the United Kingdom, and the United States. In a sandbox, refund instruction emails go only to addresses linked to the Stripe account. The test helper `POST /v1/test_helpers/refunds/{id}/expire` simulates refund expiration in a sandbox; the fixtures and helper do not establish live account eligibility or a live payout outcome.

## Related

- [[stripe]] — company context.
- [[stripe-bank-transfers]] — bank transfer payment and refund context.
- [[stripe-customer-balance]] — cash balance and invoice balance distinction.

## Raw Sources

- [[raw/stripe-payments-customer-balance-refunding-2026-11-07|November 7, 2026 full refund guide]] — full webpage capture fetched 2026-11-07, curl examples and CDN image references (257 lines).
- [[raw/stripe-bank-transfers-refunds-2025|Earlier full refund guide]] — earlier full webpage capture used for the 2026-05-05 ingest, Node examples and five locally downloaded CDN images in `raw/assets/` (270 lines).
