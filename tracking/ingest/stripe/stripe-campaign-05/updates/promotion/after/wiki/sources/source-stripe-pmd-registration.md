---
title: "Stripe Docs — Register domains for payment methods"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payments/payment-methods/pmd-registration
raw_files:
  - "stripe-pmd-registration-2025.md"
tags: [stripe, domain-registration, apple-pay, google-pay, link, amazon-pay, klarna, paypal, elements, checkout]
---

## Summary

The May 8, 2026 expanded guide covers registering every web domain that displays an applicable payment method in Elements or Checkout's embeddable form. Register each top-level domain and subdomain that displays the method, including `www` when used. Once registered, the domain is ready for other applicable methods enabled later.

## Payment methods and test/live scope

The May guide lists Apple Pay (registration required), Amazon Pay, Google Pay, Klarna, Link and PayPal (May lines 8–19). The November 7 overview uses Link, Apple Pay and Google Pay as examples and links to the Dashboard and API guide variants.

- For the Web Apple Pay path in this guide, Stripe handles merchant validation and the merchant needs no Apple Merchant ID or certificate signing request (CSR). The separate native iOS flow requires an Apple Merchant ID and a Stripe-provided CSR. [[source-stripe-apple-pay|Apple Pay integration paths]]
- Register the domains for testing, either directly in a sandbox or by registering in live mode, which also registers them in sandboxes. Register the domains in live mode before launch. For local testing, the May guide suggests an HTTPS tunnel such as ngrok (May lines 21–27).

## Dashboard and API registration

In **Payment method domains** in the Dashboard, add a new domain, enter its name and save. Repeat for each domain. Direct charges on connected accounts use the API, as described below (May lines 29–48).

The May PaymentMethodDomain API can create, retrieve, list, disable and re-enable domains. The Node.js examples below show create and disable, with the domain ID supplied for the update.

```js
// Register
stripe.paymentMethodDomains.create({ domain_name: 'example.com' })

// Disable
stripe.paymentMethodDomains.update('{{ID}}', { enabled: false })
```

Disabling a domain stops affected payment methods from appearing on it in Elements or Checkout's embeddable form. The Dashboard row actions also allow disable and re-enable (May lines 55–61 and 86–106).

## iframe origin and registration

- For Elements in an iframe, match the top-level origin. Same origin means the same protocol, full host and port.
- The May guidance allows a cross-origin iframe on Safari 17 or later with the `allow="payment"` attribute. Apple Pay in that iframe also requires registering the iframe source domain.
- If the top-level domain and iframe source domain differ, register both on the associated Stripe account (May lines 50–54 and 81–84).

## Connect account and credentials

Register the domain on the Stripe account that runs the charge. These are the May guide's account and API credential routes (May lines 35–37 and 109–131).

| Charge type | Registration account and API credentials |
| --- | --- |
| Direct charges | Register on the connected account. Use the API with the platform secret key and `Stripe-Account` set to the connected account ID. The platform Dashboard does not manage these connected-account domains. |
| Destination charges and separate charges and transfers | Register on the platform account. Use the platform secret key and omit `Stripe-Account`. |

## Related Pages

- [[stripe-wallets]] — wallet eligibility and web integration
- [[stripe-link]] — Link integration paths
- [[stripe-checkout]] — Checkout UI modes and separate hosted checkout domain settings
- [[source-stripe-apple-pay]] — separate Web and native Apple Pay setup
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-pmd-registration-2025|Domain registration, captured 2026-05-08]] — full 132-line guide, including Dashboard and API procedures.

## Related raw API references

- [[raw/stripe-payments-payment-methods-pmd-registration-2026-11-07|Domain registration selector, captured 2026-11-07]] — variant navigation links for Dashboard and API. The lead names Link, Apple Pay and Google Pay as examples in Elements and Checkout's embeddable form.
