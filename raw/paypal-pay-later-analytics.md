<!-- Source URL: https://developer.paypal.com/docs/checkout/pay-later/customize/analytics/ -->
<!-- Fetched: 2026-04-14 -->

---
title: Analytics
slug: /docs/checkout/pay-later/customize/analytics/
createTime: '2025-11-03T08:04:30.675Z'
updateTime: '2026-03-06T09:30:38.694Z'
---

# Pay Later messaging analytics

Integrate analytics events into Pay Later messaging using the JavaScript SDK v6 callback properties.

## Events

| Event | Trigger |
| ----- | ------- |
| `onRender` | After each message renders into the DOM |
| `onClick` | After a user selects the message |
| `onApply` | After a user selects the Apply button/link in the pop-up modal |

**Note:** Event handlers added to HTML override attributes from the JavaScript API.

## JS API version

```javascript
paypal.Messages({
    amount: 500,
    pageType: 'product-details',
    style: { layout: 'text', logo: { type: 'primary', position: 'top' } },
    onRender: () => { console.log('render') },
    onClick: () => { console.log('click') },
    onApply: () => { console.log('apply') }
}).render('.pp-message');
```

## Inline HTML attribute version

```html
<div
  data-pp-message
  data-pp-onrender="console.log('Callback called on render')"
  data-pp-onclick="console.log('Callback called on click')"
  data-pp-onapply="console.log('Callback called on apply')"
></div>
```

Inline HTML attributes: `data-pp-onrender`, `data-pp-onclick`, `data-pp-onapply`.
