<!-- Source URL: https://developer.paypal.com/limited-release/sdk-pay-later-messaging-cross-border/ -->
<!-- Fetched: 2026-04-14 -->

---
title: Pay later cross-border messaging
slug: /limited-release/sdk-pay-later-messaging-cross-border/
createTime: '2024-08-15T07:56:48.671Z'
updateTime: '2024-09-23T16:19:55.250Z'
---

# Pay later cross-border messaging

## Overview

Cross-border messaging lets non-country merchants promote Pay Later offers to buyers of a specific country by including the `buyerCountry` parameter in message configuration.

## Eligibility

Requires PayPal approval (limited release). Supported countries:

| Country | Consumer base requirement | Supported currency |
| ------- | ------------------------- | ------------------ |
| AU | Website for AU consumers | AUD |
| DE | Website for DE consumers | EUR |
| ES | Website for ES consumers | EUR |
| FR | Website for FR consumers | EUR |
| IT | Website for IT consumers | EUR |
| UK | Website for UK consumers | GBP |
| US | Website for US consumers | USD |

Must also meet standard Pay Later eligibility criteria for the target country.

## Integration

Add `buyerCountry` / `data-pp-buyercountry` to each message:

**Inline HTML:**
```html
<div
  data-pp-message
  data-pp-placement="product"
  data-pp-amount="500.00"
  data-pp-buyercountry="US"
/>
```

**JavaScript:**
```javascript
paypal.Messages({
  amount: 500,
  placement: 'product',
  buyerCountry: 'US',
}).render('.pp-message');
```

`data-pp-buyercountry` values: `AU`, `DE`, `ES`, `FR`, `GB`, `IT`, `US`

**Note:** Must sell in the supported currency for the target country. Some messages may include legal disclosure that only customers of that country are eligible.

**Content restriction**: Cannot translate, resize font, change color/weight, or modify content in any way. Cannot post on social media without PayPal written authorization. Stricter than standard Pay Later content rules.
