---
title: "Stripe Billing — Migrate to Stripe Tax"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-billing-taxes-migration-2026.md"
tags: [stripe, billing, subscriptions, tax, stripe-tax, migration, automatic-tax]
---

## Summary

Guide for migrating existing Stripe Billing subscriptions to Stripe Tax. Two paths: automated Dashboard tooling or manual API/Dashboard. Key pitfall: `tax_behavior` on prices is immutable once set.

## Path 1: Automated tooling (Dashboard)

Go to Dashboard → `/tax/migrations`:
- Removes manual tax rates (up to 5 business days, email notification)
- No prorations — updates take effect at start of next billing cycle
- Wait a few days between runs

**Eligible**: active, not already auto-taxed, sufficient address, `tax_behavior` set on price.

**Excluded** (must update manually): subscription schedules, destination charges / separate charges & transfers, test subscriptions.

## Path 2: Manual migration

### Step 1: Check customer tax location

`stripe.customers.retrieve(id, { expand: ['tax'] })` → check `customer.tax.automatic_tax`:

| Status | Meaning | Action |
|---|---|---|
| `supported` | Ready | None |
| `unrecognized_location` | Address invalid for tax | Update `customer.address` |
| `not_collecting` | Address recognized, no registration | Add tax registration for jurisdiction |
| `failed` | Stripe error | Retry |

### Step 2: Update products

Set `tax_code` on products. If not set, uses Dashboard default.

### Step 3: Update prices

Set `tax_behavior` (`exclusive` or `inclusive`). **IMMUTABLE once set** — must create new price if change needed.

### Step 4: Update subscriptions

**No existing tax rates:**
```js
stripe.subscriptions.update(id, { automatic_tax: { enabled: true } })
```

**With existing tax rates:**
```js
stripe.subscriptions.update(id, {
  automatic_tax: { enabled: true },
  items: items.map(i => ({ id: i.id, tax_rates: '' })),  // clear item tax_rates
  default_tax_rates: '',  // clear subscription-level tax_rates
  proration_behavior: 'none'
})
```

**With subscription schedules:** remove `automatic_tax[enabled]=false` from all phases; set `default_settings.automatic_tax.enabled=true`. Must pass ALL phases when updating schedule.

**To avoid prorations (schedule approach):**
- Create schedule from subscription
- Phase 1: current period with existing tax rates
- Phase 2: next period with `automatic_tax.enabled=true` + `tax_rates: []`

### Step 5: Confirm

Create preview invoice → check `automatic_tax.status`:
- `complete` → check `tax`, `total_tax_amounts`, per-line `tax_amounts`
- `requires_location_inputs` → update customer address
- `failed` → retry or contact support

## Related pages

- [[stripe-tax]] — concept page (updated)
- [[source-stripe-billing-taxes-collect]] — collecting taxes guide
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-billing-taxes-migration-2026]] — verbatim Stripe docs webpage (405 lines)
