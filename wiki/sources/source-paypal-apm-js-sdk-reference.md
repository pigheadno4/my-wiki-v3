---
title: "JS SDK Reference for Payment Fields (APM Reference)"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-js-sdk-reference.md"
tags: [paypal, apm, javascript-sdk, payment-fields, reference]
---

## Overview

Reference for JS SDK query parameters and `paypal.Buttons()` options used in APM payment field integrations.

Source URL: <https://developer.paypal.com/docs/checkout/apm/reference/js-sdk-params-payment-fields/>

Last updated: 2025-05-14

## `paypal.FUNDING.*` Constants

| Constant | APM | Status |
| --- | --- | --- |
| `paypal.FUNDING.BANCONTACT` | Bancontact | Active |
| `paypal.FUNDING.EPS` | eps | Active |
| `paypal.FUNDING.IDEAL` | iDEAL | Active |
| `paypal.FUNDING.BLIK` | BLIK | Active |
| `paypal.FUNDING.MYBANK` | MyBank | Active |
| `paypal.FUNDING.P24` | Przelewy24 | Active |
| `paypal.FUNDING.APPLEPAY` | Apple Pay | Active |
| `paypal.FUNDING.GIROPAY` | giropay | **Sunset Jun 30, 2024** |
| `paypal.FUNDING.SOFORT` | Sofort | **Sunset Apr 18, 2024** |

> [!warning] Notable absences
> Trustly, Multibanco are not listed in the funding constants table. iDEAL is listed but not Trustly despite both being active bank redirect APMs.

## Key SDK Constraints

- **APMs support vertical layout only**: `style.layout: 'vertical'`
- **`enable-funding` accepts comma-separated values**: `enable-funding=ideal,bancontact`
- **`paypal.Buttons().isEligible()`** — check eligibility before rendering

### `isEligible()` pattern

```javascript
paypal.getFundingSources().forEach(function(fundingSource) {
  var button = paypal.Buttons({ fundingSource: fundingSource });
  if (button.isEligible()) {
    button.render('#paypal-button-container');
  }
});
```

## Raw Sources

- [[paypal-apm-js-sdk-reference]] — verbatim reference page with funding constants table and code samples

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview
