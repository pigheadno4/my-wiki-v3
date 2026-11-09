---
title: "Stripe Declines"
type: concept
category: technology
tags: [stripe, declines, card-declines, radar, fraud, issuer-declines, adaptive-acceptance, payment-failure, outcome, network-codes, retries]
---

## Overview

Stripe surfaces three types of payment failure, each requiring different handling. The key API field is the `Charge.outcome` object, which identifies the failure type and reason regardless of the payment method.

## Three Failure Types

| Type | `outcome.type` | `network_status` | Who decides |
| --- | --- | --- | --- |
| Issuer decline | `issuer_declined` | `declined_by_network` | Card issuer / payment provider |
| Blocked payment | `blocked` | `not_sent_to_network` | Stripe Radar or Adaptive Acceptance |
| Invalid API call | `invalid` in a separate example | `not_sent_to_network` in that example | Invalid-call category; the guide does not establish a universal malformed-request or wrong-CVC mapping |

Non-card payment methods use the same decline structure and response codes.

## The `outcome` Object

Fields on `Charge.outcome`:

| Field | Description |
| --- | --- |
| `type` | `issuer_declined`, `blocked`, or `invalid` |
| `network_status` | `declined_by_network` or `not_sent_to_network` |
| `reason` | Specific reason (e.g. `expired_card`, `highest_risk_level`) |
| `advice_code` | What to do next (e.g. `do_not_try_again`, `confirm_card_data`) |
| `network_decline_code` | Raw network code (e.g. `"54"` = expired card) |
| `network_advice_code` | Network-level advice |
| `risk_level` | `normal`, `elevated`, or `highest` |
| `seller_message` | Human-readable explanation |

## Issuer Declines

The card issuer's systems evaluate spending habits, balance, card data (expiry, address, CVC) and decline if criteria aren't met. Stripe surfaces the result as a [Stripe decline code](https://docs.stripe.com/declines/codes) and optionally a [network decline code](https://docs.stripe.com/declines/network-codes).

**Most common card decline causes**: insufficient funds, incorrect card data, suspected fraud. Most declines come back as `generic_decline` — the exact reason is opaque, and card issuers only discuss specifics with their cardholders.

### Network Codes

For issuer-declined card charges, network code fields can be null when Stripe receives no card-network response; Stripe/Radar blocks that were not sent to the network are a separate category. The November 7, 2026 guide's field descriptions call these 2–4 digit card-network codes, interpreted by card brand:

| Field | Description |
| --- | --- |
| `network_decline_code` | Network decline code; meaning varies by card network |
| `network_advice_code` | Network guidance for managing the decline; Mastercard calls this MAC (Merchant Advice Code) |

> [!warning] Contradiction
> The May 9 capture attributed both codes to the issuing bank; November's field descriptions attribute them to the card network, while its introduction still says the issuer provides the two code types. This wording does not verify any specific response's origin or mapping. See [[source-stripe-card-declines]].

### `advice_code` and Retry Behavior

| `advice_code` | Captured advice | Action |
| --- | --- | --- |
| `do_not_try_again` | Do not reuse this card for the same transaction; advice, not a universal API-enforced ban | See decline code; customer may need issuer help |
| `try_again_later` | Issuer declined; the card can be retried, without a documented temporary-cause diagnosis | Ask customer to try again; if later attempts decline, contact issuer |
| `confirm_card_data` | Some supplied card data is wrong | Customer should validate card info |

For charges that permit retries, Stripe recommends at most **eight** retries; card networks impose attempt limits, and issuers might treat additional attempts as possible fraud. This is guidance for eligible charges, not permission to retry every decline.

### Reducing Card Declines

- Collect CVC + postal code at checkout
- Implement [[stripe-3d-secure]] in supported countries
- For `generic_decline`/`do_not_honor`: check CVC and AVS results
- FSA/HSA cards restricted to eligible merchant categories
- Cross-country IP/card mismatch might suggest possible unauthorized use; travel can explain it, so this signal alone does not establish the issuer's decline reason
- Global customer base → consider local Stripe accounts per region

### Programmatic Handling

- `PaymentIntent.last_payment_error.decline_code` — specific decline reason
- Iterate attempted charges → inspect `failure_message`
- Webhook `payment_intent.payment_failed` → monitor failed attempts

**On-session**: prompt customer to retry or use a different payment method.
**Off-session**: notify customer to return and update payment method; SCA may require `authentication_required` handling.

```json
outcome: {
  network_decline_code: "54",
  network_status: "declined_by_network",
  reason: "expired_card",
  advice_code: "confirm_card_data",
  type: "issuer_declined"
}
```

## Blocked Payments

Stripe says a Radar-blocked payment does not obtain card-issuer authorization through Stripe and that Stripe has not charged or withdrawn the amount. For some card types, the customer might nevertheless see an issuer authorization for the amount on a statement, typically removed by the issuer within a few days. These captures do not establish whether the issuer temporarily reserves available balance; a statement authorization is not proof of a Stripe charge.

**Blocked by Radar rule or high risk score:**

```json
outcome: {
  network_status: "not_sent_to_network",
  reason: "highest_risk_level",
  advice_code: "do_not_try_again",
  risk_level: "highest",
  type: "blocked"
}
```

**Blocked by Adaptive Acceptance** (IC+ pricing only — avoids excessive retry penalties and low-probability network costs):

```json
outcome: {
  network_status: "not_sent_to_network",
  reason: "low_probability_of_authorization",
  advice_code: "do_not_try_again",
  risk_level: "normal",
  type: "blocked"
}
```

**Allow list**: To unblock a legitimate payment, find it in the Dashboard and click **Add to allow list**. This overrides all matching Radar rules for future attempts — it does not retry the current payment.

## Invalid API Calls

The May Node and November curl examples submit a declined-test PaymentMethod and show a possible `incorrect_cvc` `card_error` response. Separately, the guides show a Charge `outcome.type = "invalid"` example and say invalid API calls typically do not produce a Dashboard payment, though a payment may appear in some cases. They do not show that the same incorrect-CVC request produced the invalid Charge outcome, or that every malformed request maps to it.

```json
{
  "error": {
    "code": "incorrect_cvc",
    "message": "Your card's security code is incorrect.",
    "type": "card_error"
  }
}
```

## Network Decline Codes

The May 9, 2026 [[source-stripe-network-decline-codes]] capture maps raw codes to Stripe decline/failure codes for seven payment-method groupings: ACH Direct Debit, Australia BECS, Bacs (ADDACS/ARUDD/AUDDIS), Cash App Pay, New Zealand BECS, Canadian PAD, and SEPA Direct Debit. Bank-debit next steps such as collecting a mandate, obtaining new account details, or contacting a customer belong to the matching method/code row. The `generic_could_not_process` rows do not share one universal next step; the SEPA row says contact Support, while AU BECS, Bacs, and Canadian PAD examples only say payment failed.

The November 7 capture adds 13 card-network or processor tables, including Visa, Cartes Bancaires, UnionPay, Mastercard and American Express. Those tables give **raw code and explanation**, not a Stripe `decline_code` or `advice_code` mapping. Meanings and retry language are network-specific: Visa `05` and UnionPay `05` differ, and Mastercard MAC combinations can say retry later or do not retry. JCB International `85` is explicitly not declined; Amex also has approval-labelled rows. Use the named network table and the actual transaction fields before deciding an outcome or next action. The detailed tables remain in [[source-stripe-network-decline-codes]].

## Decline Codes Reference

Stripe uses its own decline codes that expand on issuer codes; optional `advice_code`, network codes, and LPM charge outcome reasons are separate fields. The May and November card/LPM tables and code-specific next steps are in [[source-stripe-decline-codes]].

**Codes to mask from customers** (show as `generic_decline`): `fraudulent`, `lost_card`, `stolen_card`, `merchant_blacklist`

**Deprecated decline-code labels in the May and November reference tables**: `do_not_try_again`, `try_again_later`. This reference page does not establish that these exact names migrated to `advice_code`; consult the separate card-declines guidance for advice-field behavior.

**LPM decline-code table**: the May capture had 19 rows and 19 distinct names; the November capture has 29 rows and 27 distinct names because three Klarna outcomes share `klarna_payment_declined`. Several names, including `expired_card`, `processing_error`, and `insufficient_funds`, also appear in the card table, but their LPM outcome reasons and handling differ. See [[source-stripe-decline-codes]] for the complete row-specific messages.

## Related Concepts

- [[stripe-authorization-boost]] — Adaptive Acceptance and network token strategies to reduce issuer declines
- [[stripe-3d-secure]] — 3DS authentication to pre-validate high-risk payments
- [[disputes]] — what happens after a disputed charge

## Sources

- [[source-stripe-declines-overview]] — Stripe declines overview page
