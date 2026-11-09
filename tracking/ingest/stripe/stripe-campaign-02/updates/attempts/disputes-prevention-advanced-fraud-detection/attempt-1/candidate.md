---
title: "Stripe — Advanced Fraud Detection"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/disputes/prevention/advanced-fraud-detection
raw_files:
  - "stripe-disputes-prevention-advanced-fraud-detection-2026-11-07.md"
  - "stripe-disputes-advanced-fraud-detection-2026.md"
tags: [stripe, radar, fraud, stripe-js, advanced-fraud-detection, device-fingerprint, hcaptcha, mobile-sdk]
---

## Summary

Stripe's November 7, 2026 guide describes device and activity signals collected through Stripe.js and the iOS and Android SDKs for fraud detection. It explains collection scope, stated privacy uses, and how a business can disable advanced signals on its own site or app. Disabling them increases fraud risk and does not stop all Stripe-managed or authentication-related data collection.

## Risk Factors and Collection

**Device characteristics** cover browser, screen, and device configurations that may indicate anomalous behavior. **Activity indicators** include mouse activity, time spent on pages, and patterns such as pasted card numbers that can help distinguish bots from legitimate shoppers. These signals feed Stripe fraud systems such as Radar and are sent periodically to `m.stripe.com`. Stripe describes Radar as built in without additional setup, but the guide does not guarantee a particular fraud outcome.

Stripe recommends loading Stripe.js throughout the shopping experience, not just at checkout, to provide a richer set of activity signals. On pages where Stripe.js loads, it **can** load hCaptcha; businesses seeking to opt out of that integration should contact Stripe Support. This is conditional, not a statement that hCaptcha appears on every page or session.

Stripe says page contents are collected only where they correspond to Stripe Elements input fields; for example, an email can be collected for Link signup and login if the Element has an email field. Stripe says this page-content information is not saved. Activity risk factors are scoped to one shopping session on one site or app and are not linked across separate sessions, sites, or apps. These claims should not be broadened to all data on the page or all Stripe data.

For mobile apps, the iOS and Android SDKs collect advanced risk factors when an SDK object is instantiated and transmit them to Stripe during a tokenization request. Stripe says the advanced risk-factor data is used for fraud detection and security rather than advertising, is not rented or sold to advertisers, and is retained while useful for those purposes, with restricted internal access. Its privacy and cookie policies provide the broader disclosures.

## Disable Advanced Fraud Detection

Stripe says businesses can disable collection of **advanced fraud detection risk factors** on their own websites and apps, at increased fraud risk, particularly card testing. This setting does not stop collection on Stripe domains such as Stripe Checkout, events from customer interactions with Stripe-managed Elements fields, or basic device information sent to the issuer for 3D Secure 2 authentication. It is not a full data-collection opt-out or a PCI-compliance guarantee. The guide separately says omitting Stripe.js entirely adds fraud risk and shifts PCI responsibilities to the business.

| Platform | Captured option and version condition |
| --- | --- |
| Stripe.js script tag | Set the `advancedFraudSignals` query parameter to `false`. |
| Stripe.js pure ES module | With the latest Stripe.js module, use the `pure` export and call `loadStripe.setLoadParameters({ advancedFraudSignals: false })`. The November prose retains this option even though its displayed example changed. |
| iOS SDK | Version 19.1.1 or later; configure `StripeAPI.setAdvancedFraudSignalsEnabled(false)`. |
| Android SDK | Version 14.4.0 or later; set `Stripe.advancedFraudSignalsEnabled = false` **before instantiating or accessing any Stripe SDK object**. |

The May capture displayed this pure-module example:

```javascript
import { loadStripe } from "@stripe/stripe-js/pure";

loadStripe.setLoadParameters({ advancedFraudSignals: false });
const stripePromise = await loadStripe("<<YOUR_PUBLISHABLE_KEY>>");
```

The November capture instead displays this literal HTML example:

```html
<script src="https://js.stripe.com/endive/stripe.js?advancedFraudSignals=false"></script>
```

The capture alone does not establish whether the `/endive/stripe.js` URL is a general production integration path. The continued prose still lists **both** the script-tag query parameter and pure-module `setLoadParameters` options; changing the example does not demonstrate removal or deprecation of the module option.

## Related Pages

- [[stripe-radar]] — Radar concept, including advanced fraud detection scope
- [[stripe]] — provider overview
- [[source-stripe-radar-optimize-risk-factors]] — separate guide on risk-factor optimization

## Raw Sources

- [[raw/stripe-disputes-prevention-advanced-fraud-detection-2026-11-07|Stripe advanced fraud detection, 2026-11-07 capture]] — current captured guide and HTML example
- [[raw/stripe-disputes-advanced-fraud-detection-2026|Stripe advanced fraud detection, 2026-05 capture]] — earlier guide and pure-module example
