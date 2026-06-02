---
title: "PayPal Donate SDK"
type: source
date_ingested: 2026-04-17
original_format: webpage
raw_files:
  - "paypal-donate-sdk.md"
tags: [paypal, donate, sdk, nonprofit, buttons, popup]
---

## Summary

Integration guide for the PayPal Donate SDK — renders a Donate button that opens a pop-up overlay on the merchant's page (no redirect to PayPal). Accepts standard PayPal Donate button parameters.

## Key takeaways

- SDK script: `https://www.paypalobjects.com/donate/sdk/donate-sdk.js`
- Pop-up experience: donor stays on the merchant's page throughout
- Eligibility: log into `paypal.com/donate/buttons/` — if you can create a Donate button, you're eligible

## Account type determines parameter

| Account type | Parameter |
| --- | --- |
| Business | `hosted_button_id` (from sandbox/live dashboard) |
| Personal | `business` (email or PayerID) |

## Integration

```html
PayPal.Donation.Button({
  env: 'sandbox',                   // remove or set to 'production' for live
  hosted_button_id: 'YOUR_ID',      // or: business: 'email@example.com'
  image: { src: '...gif', title: '...', alt: '...' },
  onComplete: function(params) { }  // fires after donation completes
}).render('#paypal-donate-button-container');
```

## `onComplete` callback fields

| Field | Description |
| --- | --- |
| `tx` | Transaction ID |
| `st` | Transaction status |
| `amt` | Amount |
| `cc` | Currency code |
| `cm` | Custom message |
| `item_number` | Configurable field |
| `item_name` | Value donor selects |

## Multiple buttons

Create additional container divs and call `.render('#container-2')` for each additional button on the same page.

## Go live

Replace sandbox `hosted_button_id` with live value; change `env` to `'production'` or remove it.

## Related pages

- [[paypal-payment-links]] — PayPal Payment Links concept (alternative for simple payment collection)
- [[paypal]] — PayPal company overview

## Raw Sources

- [[paypal-donate-sdk]] — verbatim Donate SDK integration guide
