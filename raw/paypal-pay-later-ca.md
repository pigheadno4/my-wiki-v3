<!-- Source URL: https://developer.paypal.com/docs/checkout/pay-later/ca/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Pay Later (CA)
slug: /docs/checkout/pay-later/ca/
createTime: '2025-10-31T07:23:03.355Z'
updateTime: '2026-03-06T09:41:40.466Z'
---

# Pay Later (CA)

Get paid in full at checkout while giving your customers the flexibility to pay in installments over time with no late fees.

![Pay Later CA hero](assets/paypal-pay-later-au-hero.png)

# Pay Later products in Canada

Pay in 4 only. First payment due at time of transaction; subsequent payments every 2 weeks.

| Product | Number of payments | Due | Purchase amount |
| ------- | ------------------ | --- | --------------- |
| Pay in 4 | 4 | Every 2 weeks (biweekly) | $30 to $1,500 CAD |

![Pay in 4 overview CA](assets/paypal-pay-later-ca-how-it-works.png)

# Eligibility

Eligible if you:
- Are a Canada-based PayPal merchant
- Have a Canada-facing website
- Transact in Canadian dollars (CAD)
- Have a one-time payment integration
- Abide by the PayPal Acceptable Use Policy
- Do not edit Pay Later messages with additional marketing content
- **Do not create, display, or host your own Pay Later content** — integrate only official PayPal-provided code

**Not eligible:**
- Reference Transaction and Recurring Payment integrations
- Website Payments Standard (WPS) integrations

# Enable multilingual support

Canada requires bilingual support (English + French).

## Pay Later buttons

Include `components=messages,buttons&enable-funding=paylater` and set `locale`:

| Language | Parameter |
| -------- | --------- |
| English | `locale=en_CA` |
| French | `locale=fr_CA` |

```html
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&components=messages,buttons&enable-funding=paylater&locale=en_CA" data-namespace="PayPalSDK"></script>
```

## Pay Later messaging

Set `data-pp-language` on the message div:

| Language | Parameter |
| -------- | --------- |
| English | `data-pp-language="en-CA"` |
| French | `data-pp-language="fr-CA"` |

```html
<div
  data-pp-message
  data-pp-style-layout="text"
  data-pp-style-logo-type="inline"
  data-pp-style-text-color="black"
  data-pp-amount="AMOUNT"
  data-pp-language="en-CA">
</div>
```
