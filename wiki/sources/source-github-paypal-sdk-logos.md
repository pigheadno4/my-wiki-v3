---
title: "GitHub: paypal/paypal-sdk-logos"
type: source
date_ingested: 2026-04-16
original_format: github-repo
raw_files:
  - "github-paypal-sdk-logos.md"
tags: [paypal, logos, svg, apm, payment-methods, icons, sdk]
---

## Summary

PayPal's official logo library for payment method icons used in the PayPal JS SDK. Contains SVG assets for 37+ payment methods in black/white/default/color variants, plus React/JSX components for programmatic rendering. The CDN SVGs (`cdn/2.3.3/`) are directly usable assets.

## CDN SVG Access

Base URL: `https://www.paypalobjects.com/js-sdk-logos/2.3.3/`

Pattern: `{method}-{color}.svg` — e.g.:
- `https://www.paypalobjects.com/js-sdk-logos/2.3.3/paypal-default.svg`
- `https://www.paypalobjects.com/js-sdk-logos/2.3.3/ideal-black.svg`
- `https://www.paypalobjects.com/js-sdk-logos/2.3.3/applepay-mark.svg`

Local copies in `raw/github-paypal-sdk-logos/cdn/2.3.3/` (117 SVG files).

## Payment Methods with Logos

| Method | Variants |
| --- | --- |
| paypal | default, black, white, blue, mark, monochrome + rebrand |
| venmo | default, black, white, blue + rebrand |
| applepay | default, black, white, mark |
| card | default, black, white + rebrand variants |
| credit | default, black, white, blue, mark, DE variants + rebrand |
| ideal | default, black, white |
| bancontact | default, black, white + rebrand mark |
| eps, blik, boleto, giropay, multibanco, mybank, oxxo, p24, payu, satispay, sepa, sofort, trustly, wechatpay, mercadopago, paidy, itau | default, black, white |
| amex, visa, mastercard, discover, diners, maestro, jcb, cup, elo, hiper, cb_nationale | single color |
| pp (PayPal mark) | default, black, white, blue + rebrand |

## Usage (programmatic)

```javascript
import { PayPalLogo, LOGO_COLOR } from '@paypal/sdk-logos';
import { node, html } from '@krakenjs/jsx-pragmatic/src';

// Vanilla JS
PayPalLogo({ logoColor: LOGO_COLOR.WHITE }).render(html());

// React
(<PayPalLogo logoColor={LOGO_COLOR.BLUE} />).render(react({ React }));
```

## LOGO_COLOR Constants

`BLUE`, `BLACK`, `WHITE`, `MONOCHROME`, `DEFAULT`

## Related Pages

- [[paypal]] — company page
- [[paypal-apm]] — APM overview (many of these methods)
- [[apple-pay]] → [[paypal-apple-pay]] — Apple Pay via PayPal

## Raw Sources

- [[github-paypal-sdk-logos]] — stub file pointing to cdn/2.3.3/ SVGs and src/ constants
