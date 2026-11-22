---
title: "Stripe Link"
type: concept
category: technology
tags: [stripe, link, digital-wallet, payment-network, instant-bank-payments, klarna, pix, upi, stablecoins, bnpl, recurring]
---

## Definition

Link is Stripe's payment network — a digital wallet and checkout accelerator that saves customers' payment details once and autofills them across all Link-enabled merchants. Beyond card saving, Link automatically surfaces alternative payment methods (Instant Bank Payments, Klarna, Pix, UPI, Stablecoins) for eligible customers with zero merchant integration.

## Integration Paths

Two paths produce different PaymentMethod types:

| Path | PM type | When to use |
| --- | --- | --- |
| **Link as payment method** (recommended) | `link` | Works with dynamic payment methods; no extra config |
| **Link in card-specific integration** | `card` + `card.wallet.type = 'link'` | When you need card brand / last 4 |

**Key rules**:

- **Manual routing.** The May guide uses `payment_method_types` and the November guide uses `allowed_payment_method_types`. In each dated recipe, including `link` selects standalone Link even alongside `card`. For card-specific Link, include `card` and omit `link`. See [[source-stripe-link-payment-integrations]] for the request, response and version distinctions, and [[source-stripe-instant-bank-payments]] for the separate `us_bank_account` precedence rule.
- **Standalone restrictions.** The guide describes blended pricing and excludes IC+. November explicitly excludes extended authorization, incremental authorization and overcapture. The guide directs affected integrations to the card-specific route, where payment-specific feature eligibility still applies.
- **Backup payment source.** Standalone Link suggests a backup when the customer has multiple eligible saved methods. Link retries with it if the customer approves it and the first attempt fails. Card-specific Link offers no checkout backup.
- **Non-card Link PMs in card integration** (e.g., IBP): fixed values — brand=`link`, last4=`0000`, exp=`12/2040`, funding=`unknown`; show "Link" label to customers instead of these values.

Dashboard denotes Link payments as `type=link` for the standalone integration or `type=card` with `brand=link` for the card-specific integration. In the November US [[source-stripe-link-payment-methods|funding guide]], the Charge group field is `payment_method_details.link.funding_source_group` for standalone Link or `payment_method_details.card.wallet.link.funding_source_group` for card-specific Link. UPI and Pix share `lfsg_002`. These two reporting signals leave the exact underlying method and payment success unverified.

## Funding Methods

Cards, US bank accounts, [[stripe-instant-bank-payments|Instant Bank Payments]], Klarna, and other BNPLs. The Instant Bank Payments guides describe a two-day settlement timeline to the Stripe balance and a guarantee for bank-initiated ACH returns. A customer-initiated bank dispute debits the amount and dispute fee.

**Confirmation and settlement.** The [[source-stripe-link-payment-integrations|dated Link integration guide]] describes immediate confirmation and settlement of successful payments to the Stripe balance on the card timeline. The [[source-stripe-klarna-on-link#Merchant funding and payout|Klarna on Link guide]] separately describes issuer-authorized net Stripe-account credit. Later bank payout is a distinct stage. November Instant Bank Payments preserves the customer-bank dispute exception. The separate US funding guidance describes coarse `funding_source_group` reporting on the Charge, with placement varying by integration. For the [[source-stripe-payment-element-link#Funding and domain registration|browser Payment Element route]], May describes the same settlement time and guarantees for additional funding sources. November describes the same settlement time and processing behavior. See the individual payment method for the documented terms.

## Core Properties

- **Manual capture**: Yes
- **Recurring**: Yes
- **Disputes**: Yes (process varies by funding method)
- **Refunds**: 5–10 business days
- **Payment Element**. The captured general Link guides say Payment Element does not support Link for Stripe accounts based in Brazil or Thailand. The separate November Pix on Link guide describes eligible US sellers using Payment Element for on-session BRL payments from Brazilian customers. The buyer's location and BRL presentment are separate conditions. A private-preview request does not confer access or change the account-location restriction. See [[source-stripe-pix-on-link]].

## Link Payment Methods (US-only)

Link automatically presents alternative PMs — [[stripe-instant-bank-payments|Instant Bank Payments]], Klarna, Pix, UPI, Stablecoins — with zero integration. Link handles all routing.

**Klarna on Link**: For eligible US Link customers in Payment Links, Stripe-hosted Checkout and Payment Element. Turning on Link enables Klarna subject to eligibility. Disable it in Link settings under **Pay later with Klarna**. The May and November guides describe immediate net credit to the merchant’s Stripe account after issuer authorization, without waiting for Klarna installments. Express Checkout lists Klarna and Link as separate buttons. See [[source-stripe-klarna-on-link]] for the funding, UI and sandbox test boundaries.

**Pix on Link.** The November 2026 capture describes eligible US businesses, on-session BRL payments, and a 0.50–3,000 USD-equivalent range presented in BRL. The May capture specified one-time, on-session use only, with a 5 BRL minimum. November explicitly documents on-session use. The direct Pix route's November minimum is 0.50 BRL. Businesses in Australia, Canada, the EEA, Singapore, and the UK can request private-preview access. Direct Pix and Pix on Link can appear together as distinct choices. First-time Link users enter name, address, and tax ID. Ebanx is the recipient on the bank statement and separately sends receipts. The seller name appears in `Message to payor`. The November capture quotes customer-paid IOF at 3.5%, subject to change. Stripe calculates it through its partner and provides customer disclosures. Ebanx sends receipts.

November's Pix on Link refund window is 90 days from the original payment, with typical appearance in “your account” within minutes and no bank-credit timeline. Customers file limited disputes with their bank. The seller cannot challenge them, and Stripe debits funds if notified that the payment partner accepted the return. Use [[source-stripe-pix-on-link]] for these route-specific qualifications and the dated May flow. The generic Link timing and direct Pix settlement and refund details do not establish outcomes for this route.

**Stablecoins on Link.** Eligible US businesses must meet onboarding and restricted-business conditions. Customers must be in a supported country. Payment Links, Stripe Checkout and Elements support one-time, on-session USD payments of 1–10,000 USD. Both 2026 captures describe automatic enablement when activating Link on supported integrations. November separately shows an email request-access form and leaves its relationship to enablement unspecified. Customers choose from available wallets, tokens and networks. A completed payment settles in the merchant’s Stripe balance in USD, with Link’s funds guarantee in scope. Refunds return as stablecoins to the original wallet. Disputes are unsupported. Testing uses a funded blockchain testnet wallet. See [[source-stripe-stablecoins-on-link]].

**UPI on Link.** Eligible US businesses use INR presentment for one-time, on-session payments through Payment Links, hosted Checkout, or Elements. May 2026 lists a 1 INR minimum. November lists 0.50 USD equivalent in INR. Both cap payments at 100,000 INR. Desktop uses a QR code and mobile redirects to the selected UPI app. Link can store the virtual payment address. Refunds must be requested within 60 days and can take up to seven business days. Stripe removes funds immediately if the customer’s bank or PSP accepts a return request, which the merchant cannot contest. The separate direct UPI flow has its own minimum and AutoPay mandate. See [[source-stripe-upi-on-link]] for the dated Link geography and product boundaries.

**5 eligibility filters** per session: business eligibility, presentment currency, transaction limits, customer location, recurring/off-session support.

**Customer flow**:

- New: email → PM selected → Link signup + auth → instant confirmation → details saved cross-merchant
- Returning: auto-detected via email/phone/browser cookie → OTP → autofill saved details + shipping

**Disabling**: must turn off Link entirely (removes accelerated checkout + returning customer benefits). Exception: BNPL methods can be configured individually on Link settings page.

> Enabling a PM outside Link disables its Link interface — customers can't save details for faster checkout.

## Custom Checkout Page (Elements Integration)

Full guide (PaymentIntent): [[source-stripe-add-link-elements-integration]] — React + HTML+JS for all three email strategies, shipping, prefill, manual capture (7-day window), submit.

Full guide (SetupIntent / save-and-reuse): [[source-stripe-link-save-and-reuse]] — account and customer setup routes and later off-session payment. The May 2026 guide uses Link Authentication Element for separate email collection. The November 2026 guide documents Contact Details Element for that route, while its React `confirmSetup` sample still uses `LinkAuthenticationElement`.

**Three email strategies**:

1. **Pass email** (recommended if known beforehand): `defaultValues.billingDetails.email` — triggers Link auth at payment step; no shipping collection in this path
2. **Collect in Payment Element**: no code change; Link prompts in-form automatically
3. **Separate contact field**: the May 8, 2026 PaymentIntent guide shows Link Authentication Element, followed by optional Address Element and then Payment Element. The November 7 guide shows Contact Details Element in that sequence. Its React confirmation example still renders `LinkAuthenticationElement`, and its redisplay snippet imports it. See the dated examples in [[source-stripe-add-link-elements-integration]].

**Same-page prefill update**: `paymentElement.update({ defaultValues: ... })` on `onblur` of form fields.

## Link in Hosted and Embedded Checkout

**Dynamic methods.** Both dated guides say to enable Link in Dashboard and omit the manual payment method list. Both separately give manual-list advice for SetupIntents used to save cards. Their manual prose names `card` and `link` and a common line-item currency. The May Node.js example sends `payment_method_types`. The November Ruby example omits the field despite the surrounding manual prose.

**Versioned request boundary.** Checkout Session Create on `2026-09-30.endive` rejects writable `payment_method_types` with HTTP 400. Use the applicable dynamic method or `allowed_payment_method_types` request route, and inspect the computed `payment_method_types` response. The affected PaymentIntent and SetupIntent request fields and deferred Elements options have separate scopes. See [[source-stripe-checkout-link]] and [[source-stripe-link-payment-integrations]].

**Domain registration.** The separate [[source-stripe-pmd-registration|registration guide]] covers Link in Elements and the embeddable Checkout form. The November Link with Checkout capture omits May’s unqualified registration statement.

**PaymentMethod type and pricing.** Link as a payment method returns `PaymentMethod.type=link`. The eligible card-specific path returns `PaymentMethod.type=card` with `card.wallet.type=link`. The Checkout guide compares Link pricing with other card payments. See [[source-stripe-checkout-link#Funding, pricing and settlement|Checkout Link funding and pricing]] for agreement-based Link Group fees and the blended rate and IC+ limits of Link as a payment method.

**Sandbox Link authentication**: `000001` is invalid, `000002` is expired, `000003` exceeds maximum attempts, and every other six-digit code authenticates. Treat accounts tied to publishable keys as if publicly available, and keep real data out. Authentication leaves payment completion unverified.

**Disable**: Change Link individually for each payment method configuration in Dashboard. The change might take a few minutes to take effect.

## Payment Element Integration

The default browser Payment Element shows a Link prompt in its card form, with merchant control in Payment Methods settings. A customer already logged in to Link can autofill details saved with another business. There are two in-form email routes:

1. **Pass email (recommended)**: `elements.create('payment', { defaultValues: { billingDetails: { email } } })` — customer authenticates directly in the payment form; use when email is collected earlier in flow
2. **Collect in Payment Element**: no code changes. When an unenrolled customer selects a supported payment method, the form prompts them to save their details and they can choose whether to enroll.

**Prefill tool**: defaults on when Link is enabled and can be disabled under Link settings → Features. When Stripe customer data has yet to be supplied programmatically, it detects email, phone and name fields on the same page. It holds detected values in local session memory. Returning login uses email for a one-time passcode and stores no page data. Enrollment persists prefilled details only after customer action and consent.

**Accelerated sign-up**: expands sign-up fields by default and can prefill email and phone. Configure under Settings → Payment Methods → Link or in Connected Accounts settings. Customer country and local privacy laws affect availability, and customers can opt out.

For Link in the browser Payment Element, see [[source-stripe-pmd-registration|domain registration]]. The November Payment Element capture omits the registration sentence, while the separate November registration overview expressly includes Link for Elements and Checkout’s embeddable payment form.

## Invoicing (Hosted Invoice Page)

Enabling Link on Stripe's hosted invoice page requires no extra implementation code. In Dashboard, open **Invoice template**, choose **Manage** under **Payment methods**, toggle Link on and save. The May and November 2026 guides document compatibility with the Invoices and Subscriptions APIs and a private URL for viewing, paying and downloading the invoice. Their broad “all of your customers” wording is subject to eligible transactions. The November Invoicing table lists most currencies and locations.

Account defaults apply to newly created invoices and Dashboard can select methods per invoice. In the hosted flow, an existing customer default can still be used when absent from the invoice configuration. In the separately documented API override, include the configured default method type in `payment_method_types` when the customer-configured Account, Customer or associated Subscription has one, or payment fails.

`Invoice.hosted_invoice_url` is null before finalization. The November hosted invoice guide describes expiry 30 days after the due date or, if absent, 30 days after finalization, with a maximum 120-day window. It separately guarantees at least 10 days for links shown in Dashboard or retrieved via API, including after expiration. URL reachability, Link display and autofill leave paid status and settlement to separate evidence. See [[source-stripe-invoicing-link]] for the dated hosted page, payment methods and Invoice object references.

## Mobile Payment Element (iOS / Android / React Native)

The May and November 2026 guides describe a default Link prompt in the card form and autofill for existing users who enrolled at any Link-enabled business. Integrate the Mobile Payment Element with the guide's latest Stripe Mobile SDK, enable Link in the Dashboard, then use an API version with dynamic payment methods on by default or explicitly add `automatic_payment_methods` when creating the PaymentIntent. Optional `defaultBillingDetails` can prefill name, email, and phone. Link authenticates using email and phone. Prefill and authentication are separate from payment confirmation. See [[source-stripe-mobile-payment-element-link]] for the dated default, compatibility, and Android wallet-entry scope.

- **iOS**: `configuration.defaultBillingDetails.email = ...`
- **Android**: `PaymentSheet.BillingDetails(name, email, phone)` in `PaymentSheet.Configuration`
- **React Native**: `initPaymentSheet({ defaultBillingDetails: { name, email, phone } })`

**Sandbox OTP**. The mobile guide says to enter `000000` when prompted. The separate web Payment Element sandbox table reserves `000001` for invalid, `000002` for expired, and `000003` for maximum attempts. Other six-digit web sandbox values succeed, including `000000`. See [[source-stripe-mobile-payment-element-link]] and [[source-stripe-payment-element-link]] for the separate scopes.

### Android `23.19.0` Wallet Entry Contract

`PaymentSheet.LinkConfiguration.Display.WalletButtonHidden` remains Link-enabled but now documents showing its button/row for a detected existing Link user and hiding it otherwise, with automatic verification and inline sign-up retained. In the earlier 23.16.0 through retained 23.18.0 evidence, the documented button/row was hidden regardless; both histories remain version-qualified in [[source-github-stripe-android]] and [[changelog-github-stripe-android]]. This is native Android source evidence, not a change to the web integration paths above. Detection/rendering code and device verification are outside the capsule. `Never` remains distinct from hiding a wallet entry.

## Card Element for Existing Link Integrations

The November Web Elements overview still lists Link saving and autofill with Card Element. Stripe’s May and November 2026 dedicated guides no longer recommend Card Element for Web Elements. May names Link Authentication Element, which the May 27 Dahlia changelog renames to Contact Details Element while documenting both Web Elements creation aliases. The November guide recommends Contact Details Element, Express Checkout Element or Payment Element.

Both single-line and split forms use the documented 90-day Link authentication window. Stripe automatically enables Link for granted-access accounts outside India and can selectively show it in production. An enabled sandbox shows Link in eligible sessions. Use test data only in sandbox Link accounts. The typical 350 × 28 px guidance depends on font, locale, placeholder and icon visibility. Pop-ups need opener communication, which `Cross-Origin-Opener-Policy: same-origin` blocks. Disable via Dashboard or `disableLink: true`.

**Connect.** Direct charges, payment methods created and charged on the connected account, and full Dashboard access permit connected-account settings control. Cloning methods from the platform, destination charges, separate charges and transfers and lack of full Dashboard access leave control for platform transactions with the platform. Settings for payments without the platform are separate. See [[source-stripe-card-element-link]] and the separate [[source-stripe-payment-request-button-link]] Endive cutoff.

## Payment Request Button (Deprecated for Link)

The May 8, 2026 Link guide recommends Link Authentication Element, Express Checkout Element or Payment Element. The November Web Elements overview marks Payment Request Button deprecated and directs existing integrations to Express Checkout Element. The separate November Link guide identifies the cutoff at Stripe.js Endive or later. Earlier Stripe.js versions can use the Element while those versions remain supported. The dedicated guide also names Contact Details Element, formerly Link Authentication Element, and Payment Element as alternatives. See [[source-stripe-payment-request-button-link]].

On supported earlier versions, returning customers can authenticate with an SMS or email code, or skip reauthentication after authenticating on a Link-enabled site within the prior 90 days. Connected accounts accessing the Element through a platform get Link automatically. Platforms manage Link for payments they process. Connected accounts manage independent payments in their own Dashboard.

## Express Checkout Element

The May and November Link guides name six built-in one-click buttons: Link, Apple Pay, Google Pay, PayPal, Klarna and Amazon Pay. The broader Element guide separately covers custom buttons. Stripe sorts eligible methods by customer location and can display newly supported buttons without frontend code changes. An existing Elements instance can be reused. Link requires Wallets enablement and eligible transaction and browser conditions. The separate Klarna button does not expand Klarna funding inside Link. See [[stripe-express-checkout-element]] and [[source-stripe-express-checkout-link]].

```js
stripe.elements({ mode: 'payment', amount, currency }) → create('expressCheckout', options) → mount
```

## Contact Details Element (formerly Link Authentication Element)

The email field collects customer email and starts Link authentication. In the dated PaymentIntent Elements flow, Link sends a recognized customer a one-time phone code and displays saved addresses and payment methods after successful authentication. Both standard Stripe.js creation strings remain documented for the renamed field. The separate Link Signup Element is a beta surface. See [[stripe-link-authentication-element]] and [[source-stripe-elements-link]].

Key: `loader: 'auto'` on Elements instance; `onChange` event fires on input and autofill; `defaultValues.email` prefill starts auth flow immediately.

**Page order**: Link Authentication Element → Address Element (optional) → Payment Element. Can be on different pages — show only once per checkout flow. Supported PMs for Link signup: credit card, debit card, US bank. Domain registration required.

## Link Signup Element: 9.16.0 beta declaration

The retained `@stripe/stripe-js@9.16.0` adds a distinct `linkSignup` Element, not a rename of Link Authentication. Both standard Elements (`create('linkSignup')`, `getElement('linkSignup')`) and Checkout Elements SDK (`createLinkSignupElement`, `getLinkSignupElement`) explicitly require beta access. Optional defaults are string-valued `email`, `name`, and `phone`.

Its typed events are `ready`, `focus`, `blur`, `escape`, `loaderstart`, and `loaderror`, with `on`/`once`/`off`. It inherits the base Element lifecycle but does not declare `change`, `update`, or `getValue`. Do not transfer Link Authentication's email-change or autofill semantics to it. The declarations do not establish enrollment, consent, saved-data behavior, merchant eligibility, or a React wrapper. See [[source-github-stripe-js]] and [[changelog-github-stripe-js]].

### Separately retained React binding: 6.10.0

`@stripe/react-stripe-js@6.10.0` adds beta `LinkSignupElement` to both entrypoints. Standard Elements uses `elements.create('linkSignup', options)`; Checkout Elements calls `createLinkSignupElement(options)`. Checkout Form is explicitly unsupported. The root props use `StripeLinkSignupElementOptions`; the Checkout props substitute `StripeCheckoutLinkSignupElementOptions`. Both expose readiness, focus/blur, escape and loading callbacks, not a typed `onChange`. The existing lifecycle forwards option changes only when the underlying Element exposes `update`, so changing props does not guarantee updated defaults. This separate repository supplies the React evidence missing from the Stripe.js-only declaration record above; it does not verify enrollment or consent behavior. See [[source-github-react-stripe-js]] and [[changelog-github-react-stripe-js]].

## Sources

- [[source-github-stripe-android]] - versioned native Link wallet-button visibility contract at 23.19.0, with prior contract retained
- [[source-github-react-stripe-js]] - beta Link Signup React wrapper and provider restrictions at 6.10.0

- [[source-github-stripe-js]] - version-qualified Link Signup beta contract at 9.16.0

- [[source-stripe-link]] — two PM type paths (link vs card+wallet), Instant Bank Payments exclusive, Thailand/Brazil Payment Element caveat
- [[source-stripe-link-payment-methods]] — Link payment methods (US-only): LPMs, zero integration, 5 eligibility criteria, customer flow, disabling rules
- [[source-stripe-klarna-on-link]] — eligible US Link customers in Payment Links, Hosted Checkout and Payment Element, issuer-authorized net credit to the Stripe account, sandbox fixtures
- [[source-stripe-pix-on-link]] — May and November 2026 captures: eligible US sellers, BRL presentment with dated minimums, private-preview requests, Ebanx and customer-paid IOF, limited disputes, and 90-day refunds
- [[source-stripe-stablecoins-on-link]] — Stablecoins on Link eligibility, November access-interest form, supported surfaces, USD Stripe-balance settlement and original-wallet refunds
- [[source-stripe-upi-on-link]] — eligible US businesses, INR presentment, May and November minimums, 100,000 INR maximum, QR/app approval, saved address, and refund and dispute outcomes
- [[source-stripe-checkout-link]] — May and November 2026 Link with Checkout guides covering hosted and embedded scope, Endive request fields, sandbox authentication and Connect configuration.
- [[source-stripe-elements-link]] — November 7, 2026 Web Elements overview and May 8 PaymentIntent Link Authentication implementation, including the later Contact Details name, email handling, placement and React scope.
- [[source-stripe-express-checkout-link]] — May and November Link in Express Checkout Element guides. Six named built-in buttons, location sorting, eligible display and browser-side mount.
- [[source-stripe-payment-element-link]] — Browser Payment Element email routes, separate accelerated sign-up and prefill controls, sandbox OTP exceptions, and dated funding and registration wording
- [[source-stripe-payment-request-button-link]] — Deprecated Link integration and migration to Express Checkout Element. See the November Stripe.js Endive cutoff and the dated returning-user authentication and Connect settings for supported earlier versions.
- [[source-stripe-card-element-link]] — May and November 2026 Link guidance for existing Card Element integrations. The November Web Elements overview still lists saving and autofill. The dedicated guide no longer recommends Card Element and covers display, authentication, browser and Connect scope, the Contact Details Element rename, and the separate Payment Request Button cutoff.
- [[source-stripe-mobile-payment-element-link]] — May and November 2026 native Link card-form prompt, Android/iOS/React Native optional prefill, dynamic-method enablement choices, and the separate mobile and web sandbox scopes
- [[source-stripe-invoicing-link]] — no extra implementation code to enable Link on Stripe's hosted invoice page, plus invoice-specific eligibility, URL and status boundaries. The dated captures describe compatibility with Invoices and Subscriptions APIs.
- [[source-stripe-link-payment-integrations]] — Link integration paths: PM vs card-integration decision, IC+ caveat, backup payment source, non-card fixed values
- [[source-stripe-add-link-elements-integration]] — May and November 2026 PaymentIntent checkout guides, with dated contact and redisplay examples.
- [[source-stripe-link-save-and-reuse]] — SetupIntent and later off-session payment guide, with dated email collection routes and a November React submit example caveat
- [[source-stripe-link-authentication-element]] — Link Authentication Element: dual-purpose email field, onChange event, prefill behavior
