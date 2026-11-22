---
title: "Stripe Docs — Build a custom checkout page that includes Link"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/link/add-link-elements-integration"
raw_files:
  - "stripe-payments-link-add-link-elements-integration-2026-11-07.md"
  - "stripe-add-link-elements-integration-2025.md"
tags: [stripe, link, payment-element, contact-details-element, link-authentication-element, address-element, react, custom-checkout, manual-capture]
---

## Summary

The November 7, 2026 guide covers custom web [[stripe-elements|Elements]] checkout with [[stripe-link|Link]] and a server-created PaymentIntent. It documents React and HTML+JS paths for email, shipping, prefill, confirmation, capture, saved-data redisplay and later reuse. The May 8, 2026 capture remains the reference for the earlier [[stripe-link-authentication-element|Link Authentication Element]] and Ephemeral Key examples.

## November 7, 2026 — Setup and Email Choices

The server creates the PaymentIntent and sends its scoped client secret to the browser's shared Elements group. For dynamic payment methods, enable Link in Dashboard payment method settings and omit `payment_method_types`. Initialize Stripe.js with a publishable key. The guide requires HTTPS for live acceptance and direct loading from `js.stripe.com` in the HTML flow, shown with the Endive script. See November raw lines 20–62, 173–199 and 243–261.

- **Pass a known email to the Payment Element.** This is the guide's preferred path when the email is already available. `defaultValues.billingDetails.email` starts Link authentication at the payment step. Other prefill fields are optional. The guide shows `paymentElement.update({ defaultValues: ... })` on field blur for same-page entry. This path omits shipping collection.
- **Collect email in the Payment Element.** Use this option when checkout does not already collect email. An unenrolled customer who chooses a supported method sees a Link signup prompt. For a checkout that also needs shipping, see the separate contact path.
- **Use Contact Details Element for a separate email and Link authentication field.** Use React `ContactDetailsElement` or Stripe.js `elements.create('contactDetails')`, then optional shipping [[stripe-address-element|Address Element]], then Payment Element. The contact field can appear once on an earlier checkout page. If the email matches an existing Link account, Link sends a one-time phone code and successful authentication makes saved addresses and payment methods available for autofill. Prefill with `defaultValues.email` starts authentication and the React `onChange` or Stripe.js `change` example reads `event.value.email`.

Shipping mode follows the contact field and precedes the Payment Element, which detects available address data and collects additional billing details as needed. The shipping address is passed on payment submission. `onChange` or `change` exposes address updates and `defaultValues` prefills the address. See November raw lines 107–170, 416–617 and 619–945.

### React sample identifiers

- **Contact field.** November setup and shipping use `ContactDetailsElement`. Its confirmation example still imports and renders `LinkAuthenticationElement`, and its redisplay snippet imports it. The retained `@stripe/react-stripe-js@7.0.0` root exports separately map these names to `contactDetails` and `linkAuthentication`. The examples establish distinct identifiers. The guide leaves its minimum React package version unspecified. See November raw lines 432–475, 790–825, 962–1016 and 1204–1234 and [[source-github-react-stripe-js|the retained React package baseline]].
- **Shipping field.** Both captures' React setup prose names `ShippingAddressElement`. Their standard Elements and PaymentIntent shipping examples use `AddressElement` from `@stripe/react-stripe-js` with `mode: 'shipping'`. `ShippingAddressElement` is a distinct Checkout Sessions component from `@stripe/react-stripe-js/checkout`. See May raw lines 425–427 and 795–833, November raw lines 432–434 and 790–825, and [[stripe-address-element#API Path Differences|Address Element API path differences]].

## Payment Status, Capture and Fulfillment

Client-side `stripe.confirmPayment({ elements, confirmParams: { return_url } })` uses the shared Elements group. The browser can visit an intermediate authorization page before reaching `return_url`, and `redirect: 'if_required'` changes the default redirect behavior. The return page can look up status with `payment_intent` and `payment_intent_client_secret`. Use the server's `payment_intent.succeeded` webhook for fulfillment and handle `payment_intent.payment_failed` for failed payments.

`capture_method: 'manual'` requests authorization only. A successful authorization reaches `requires_capture`. Capture an authorized Link payment within seven days or Stripe automatically cancels the authorization. You can cancel the PaymentIntent or capture the full authorized amount or less. See November raw lines 954–1101 and May raw lines 966–1127.

## Saved-Data Redisplay and Future Link Payments

- **Redisplay in November.** Create a server-side `CustomerSession` with Payment Element redisplay enabled and a PaymentIntent for the same `customer_account` (customer-configured Accounts v2) or `customer` (Customers v1). Initialize browser Elements with the PaymentIntent `clientSecret` and separate `customerSessionClientSecret`. The Link guide says that when more than one method is saved, it displays the three most recently used saved cards alongside the customer's Link-saved methods. See November raw lines 1136–1256 and [[stripe-saved-payment-methods]].
- **Future reuse in both captures.** The guide limits saving a Link payment method to future off-session payments or subscriptions. Attach it to the customer-configured Account or Customer with `setup_future_usage=off_session`. The later PaymentIntent uses the matching identity and resulting PaymentMethod ID and confirms with `off_session=true`. If customer authentication is required while the customer is absent, that confirmation returns an error. See November raw lines 1258–1332 and May raw lines 1314–1412.

The November guide describes Accounts v2 as generally available to Connect users and in public preview to other Stripe users, with a preview API version required for preview participants. It directs those users to enable **Reusable payment methods for Global Payouts** under Dashboard **Account previews and features**. Its manual-capture and redisplay PaymentIntent examples set `automatic_payment_methods[enabled]=true` where May showed explicit `link` and `card` lists. The future-reuse examples enable automatic methods in both captures.

## Testing and Data Disclosure

The November testing section lists credit cards, debit cards and qualified US bank account purchases. It says added funding sources use the same settlement time and processing behavior without integration changes. Sandbox OTP and 3DS2 examples simulate outcomes. Keep real user data out of sandbox Link accounts. The guide assigns the business responsibility for disclosures and necessary rights and consents for Elements data collection. See November raw lines 1103–1134 and 1334–1336.

## May 8, 2026 — Historical Integration

- The separate email/authentication field was Link Authentication Element. Use the May React `LinkAuthenticationElement` and Stripe.js `linkAuthentication` examples, with the optional shipping Address Element before Payment Element. The May capture also shows the early-page contact field, `event.value.email`, and prefill-triggered authentication, including `elements.create('linkAuthentication', { defaultValues: { email } })`. Its pass-in Payment Element example uses `defaultValues.billingDetails` with email required for that path and name, phone and address optional.
- May's HTML examples used the Dahlia script. Its saved-data examples used an Ephemeral Key and `customerOptions`, the `elements_customers_beta_1` flag and `2026-04-22.dahlia` version examples. May called `automatic_payment_methods` optional for dynamic methods and gave separate manual-listing advice for future-use Setup Intents. November routes the Setup Intents topic to the future payments guide.
- May's testing section explicitly required domain registration, limited support to cards and qualified US bank account purchases, and described added funding sources using the same settlement time and guarantees. November omits the registration sentence in this integration guide and uses different funding wording. See [[source-stripe-pmd-registration|the separate domain registration source]] and the November variant index below.
- Historical asset names appear in the May capture under `assets/`: `stripe-link-in-payment-element.png`, `stripe-link-payment-flow-diagram.svg`, `stripe-link-lape-unregistered.png`, `stripe-link-collect-email-returning.png`, `stripe-link-with-elements.png`, `stripe-link-prefill-pe-new-user.png`, `stripe-link-prefill-lae-new-user.png`, `stripe-link-appearance-example.png` and `stripe-link-customer-saved-data.png`.

## Related Pages

- [[stripe-link]] — Link concept and custom checkout routes
- [[source-stripe-payment-element-link]] — Link in the Payment Element
- [[source-stripe-elements-link]] — earlier Link Authentication Element guide
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-link-add-link-elements-integration-2026-11-07|November 7, 2026 full capture (1,344 lines)]]
- [[raw/stripe-add-link-elements-integration-2025|May 8, 2026 full capture (1,424 lines)]]

## Related raw API references

- [[raw/stripe-payments-payment-methods-pmd-registration-2026-11-07|Domain registration variant index (2026-11-07)]] — Dashboard and API documentation links.
