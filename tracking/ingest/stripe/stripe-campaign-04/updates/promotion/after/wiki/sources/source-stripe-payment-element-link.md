---
title: "Stripe Docs — Link in the Payment Element"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/link/payment-element-link"
raw_files:
  - "stripe-payments-link-payment-element-link-2026-11-07.md"
  - "stripe-payment-element-link-2025.md"
tags: [stripe, link, payment-element, prefill, autofill, accelerated-signup, defaultValues]
---

## Summary

Stripe documents Link in the browser Payment Element, including email collection, account authentication and enrollment, field prefill and sandbox testing.

## Integration Options

The default Payment Element integration includes a Link prompt in the card form. The merchant controls Link in Payment Methods settings. Customers already logged in to Link can autofill details saved with another business.

| Option | When | How |
| --- | --- | --- |
| **Pass email (recommended)** | The merchant already has the customer's email | Pass it through `defaultValues.billingDetails.email` when creating the Payment Element. Returning Link customers can authenticate in the payment form and use saved details. |
| **Collect in Payment Element** | The customer enters an email in the payment form | This route needs no code changes. A customer who has enrolled can use saved details. An unenrolled customer who selects a supported payment method is prompted to save their details and can choose whether to enroll. |

Name and address are optional in the billing-details example.

```js
elements.create('payment', { defaultValues: { billingDetails: { name, email, address } } })
```

## Accelerated sign-up

By default, Link expands the sign-up fields and can prefill email and phone to make enrollment easier. Configure this under Settings → Payment Methods → Link or in Connected Accounts settings. The behavior depends on customer country, can be limited or disabled by local privacy laws, and allows the customer to opt out.

## Prefill tool

Stripe enables the separate prefill tool by default when Link is enabled. Disable it under Link settings → Features in the Dashboard without changing code. It detects customer fields on the same checkout page as the Link-enabled Payment Element when Stripe customer data has yet to be supplied programmatically. The scan description calls the parameter `defaultValue`, while the browser code examples use `defaultValues`.

During sign-up, Link can prefill email, phone and name. The page-scanning tool holds detected values temporarily in local session memory without persisting them in cookies, local storage or another service. Link stores prefilled data for account creation only after the customer acts and consents. For returning login, Link uses the email to prompt one-time passcode authentication and stores no page data from that flow.

## Sandbox OTP codes

Create sandbox Link accounts with any valid email. Treat them as effectively public because they are tied to the publishable key. Keep real user data out of them.

| Code | Sandbox authentication result |
| --- | --- |
| `000001` | Invalid code |
| `000002` | Expired code |
| `000003` | Maximum attempts exceeded |
| Any other six digits | Successful authentication |

The separate [[source-stripe-checkout-link|Checkout guide]] documents the same sandbox code outcomes. These codes exercise Link account authentication. Payment confirmation and settlement have separate evidence requirements.

## Funding and domain registration

- **2026-05-08 capture** describes credit cards, debit cards and qualified US bank account purchases as the only supported choices and explicitly links to domain registration. It describes additional funding sources as using the same settlement time and guarantees as card and bank account payments.
- **2026-11-07 capture** lists the same three choices without exclusivity and drops the registration sentence. The separate [[raw/stripe-payments-payment-methods-pmd-registration-2026-11-07|November domain-registration overview]] expressly includes Link in Elements and Checkout's embeddable payment form and routes to the Dashboard and API variants. See [[source-stripe-pmd-registration]] for the registration route. The Payment Element guide's wording change leaves that independently documented prerequisite in scope.
- **2026-11-07 capture** describes the same transaction settlement time and processing behavior for additional funding sources as for card and bank account payments. Both captures describe automatic support without integration changes. The dated phrasing establishes the guide's comparison. Market-specific eligibility, contractual guarantees and actual funds availability require separate evidence.

## CDN Assets

- `raw/assets/stripe-link-in-payment-element.png` — Payment Element with Link prompt (430 KB)

## Related Pages

- [[stripe-link]] — Link concept page, including browser Payment Element
- [[source-stripe-checkout-link]] — Link with Checkout, including its sandbox testing
- [[source-stripe-pmd-registration]] — Domain registration for Elements and embeddable Checkout
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-link-payment-element-link-2026-11-07]] — 2026-11-07 full webpage capture (117 lines)
- [[raw/stripe-payment-element-link-2025]] — 2026-05-08 full webpage capture (116 lines)
