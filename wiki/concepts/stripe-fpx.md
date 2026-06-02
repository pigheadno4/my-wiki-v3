---
title: "FPX (Stripe)"
type: concept
category: technology
tags: [stripe, fpx, malaysia, myr, bank-redirect, authenticated, brn]
---

## Definition

FPX (Financial Process Exchange) is Malaysia's dominant online bank redirect payment method, operated by PayNet Group (Bank Negara Malaysia + 11 major banks). API enum: `fpx`. Customer-authenticated two-step auth (SMS or scanner), immediate notification.

**Currency**: MYR only. **Customers**: Malaysia only. **Business**: MY only.

**BRN required**: Businesses must provide their Business Registration Number to process FPX and receive payouts.

## Payment Flow

1. Customer selects FPX at checkout
2. Selects bank → redirected to bank's online portal
3. Enters bank credentials
4. Completes 2-step authorization (scanner or SMS)
5. Immediate payment confirmation
6. Optional return to merchant site

## Key Properties

- **Confirmation**: Customer-authenticated, immediate notification
- **Recurring**: No — single-use only
- **Disputes**: No chargebacks (customer authenticates with bank)
- **Refunds**: Up to 60 days; async ~1 week; `refund.updated`/`refund.failed` webhooks; refund can fail (returned to Stripe balance)
- **Payout timing**: 5 business days
- **Checkout restrictions**: Not in subscription or setup mode; ECE: not supported

## vs EPS

| | FPX | EPS |
| --- | --- | --- |
| Country | Malaysia only | Austria only |
| Currency | MYR | EUR |
| BRN required | Yes | No |
| Refund window | 60 days | 180 days |
| Refund processing | ~1 week (async) | Standard |
| Payout | 5 business days | Standard |

## Integration

**Checkout**: `payment_method_types: ['fpx']`, `myr`. **Mandatory confirmation page** required: must display transaction date/time, amount, seller order no., FPX transaction ID, buyer bank name, status — all from Charge object.

**FPX balance**: settles separately from other funds → may produce 2 payouts/day. Use `source_type: 'fpx'` for Connect payouts/transfers.

**18 supported banks**: affin_bank, alliance_bank, ambank, bank_islam, bank_muamalat, bank_rakyat, bsn, cimb, hong_leong_bank, hsbc, kfh, maybank2e, maybank2u, ocbc, public_bank, rhb, standard_chartered, uob.

**Amount limits** (Elements legacy): min RM2, max RM30,000.

## Sources

- [[source-stripe-fpx]] — primary source: properties, flow, BRN requirement, disputes, refunds
- [[source-stripe-fpx-accept-payment]] — integration guide: Checkout + Elements legacy, confirmation page requirements, bank reference, FPX balance/payouts
