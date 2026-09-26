---
title: "GitHub: Adyen/adyen-web"
type: source
date_ingested: 2026-07-26
date_updated: 2026-09-22
original_format: github-repo
raw_files:
  - "github/adyen/adyen-web/snapshots/2026-09-22-386715e/manifest.json"
  - "github/adyen/adyen-web/supplements/2026-09-22-386715e-542cc72c/manifest.json"
  - "github/adyen/adyen-web/snapshots/2026-09-22-0d1e033/manifest.json"
  - "github/adyen/adyen-web/supplements/2026-09-22-0d1e033-6cf5ddf4/manifest.json"
  - "github/adyen/adyen-web/snapshots/2026-09-14-b29934f/manifest.json"
  - "github/adyen/adyen-web/supplements/2026-09-14-b29934f-d296b082/manifest.json"
  - "github/adyen/adyen-web/snapshots/2026-09-14-f10995d/manifest.json"
  - "github/adyen/adyen-web/supplements/2026-09-14-f10995d-55e9e1ba/manifest.json"
  - "github/adyen/adyen-web/snapshots/2026-09-14-b989173/manifest.json"
  - "github/adyen/adyen-web/supplements/2026-09-14-b989173-20c08eb4/manifest.json"
  - "github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/manifest.json"
  - "github/adyen/adyen-web/snapshots/2026-08-09-c98ea8a/manifest.json"
  - "github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/manifest.json"
tags: [adyen, checkout, web-sdk, cards, 3d-secure, github-repository]
---

## Overview

`Adyen/adyen-web` contains Adyen's browser checkout SDK. It provides an all-in-one Drop-in and individually mounted payment-method Components, plus shared handling for sessions, payment actions, analytics, risk data, localization, and accessibility. This cumulative page begins with package-qualified release `@adyen/adyen-web@6.41.0` and records history through `@adyen/adyen-web@6.45.2` at exact SHA `386715eebb31dd703168ecdecb1477b3311f85cf`, preserving the 6.45.1 do-not-use warning and subsequent fix.

Repository: <https://github.com/Adyen/adyen-web>

## Evidence boundary

The newest ingested release is `@adyen/adyen-web@6.45.2`, SHA `386715eebb31dd703168ecdecb1477b3311f85cf`. The architecture baseline through 6.45.0 and the 6.45.1 regression history below remain preserved.

> [!warning] Do not use 6.45.1
> The collected upstream release notes warn of a payment-action handling bug and direct users to 6.45.2. Recording this release preserves evidence; it is not an upgrade recommendation.

- The ingested snapshots and supplements cover version-qualified implementation from `@adyen/adyen-web@6.41.0` through `@adyen/adyen-web@6.45.2`. They do not replace current Adyen integration guidance or prove that a payment method is enabled for a merchant.
- Drop-in and Components are presentation and client-orchestration surfaces. Payment-method availability still comes from backend responses, merchant configuration, shopper context, and regional or product eligibility.
- Stories are retained as intended integration scenarios. Tests were excluded by collection policy, so test-only behavior is outside this capsule.
- PayPal Fastlane support in this repository depends on `@paypal/paypal-js`; these snapshots describe Adyen's adapter and configuration surface, not the delegated PayPal runtime.

## Grounding excerpts

> "Adyen Web provides you with the building blocks to create a checkout experience for your shoppers"
>
> `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/README.md:7`

> "With this integration, installments configuration must be defined when you create the session."
>
> `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/Card/Card.tsx:107-113`

> "Credit: Should render CtP and installments"
>
> `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/Card/stories/Card.stories.tsx:303-310`

> "Only render component if we have a valid acsURL & postMessageDomain."
>
> `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/ThreeDS2/components/Challenge/PrepareChallenge3DS2.tsx:74-84`

> "The iframe now has no role."
>
> `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/Card/components/CardInput/a11y.docs.mdx:15-28`

## Integration surfaces and architecture

### 6.43.0 grounding

> `tags?: TagProps[];`
>
> [Select item type, line 10](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b989173-20c08eb4/files/packages/lib/src/components/internal/FormFields/Select/types.ts#L10)

> `export const Tag = ({ label, variant = TagVariant.INFO }: Readonly<TagProps>) => {`
>
> [Tag renderer, line 12](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b989173-20c08eb4/files/packages/lib/src/components/internal/Tag/Tag.tsx#L12)

> `// Clicking the input of an open list keeps it open`
>
> [Select button, line 61](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b989173-20c08eb4/files/packages/lib/src/components/internal/FormFields/Select/components/SelectButton.tsx#L61)

> `"@paypal/paypal-js": "10.0.3",`
>
> [Package dependency, line 140](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-14-b989173/files/packages/lib/package.json#L140)

### Established architecture

Drop-in is the all-in-one checkout surface. Components expose one payment method at a time for merchants that need control over layout and orchestration. The UMD bundle registers all Components, while tree-shakable integrations must register the Components they use.

The core resolves API, analytics, image, and translation endpoints from the selected environment. Initialization validates configuration, sets up an optional Checkout Session, builds the payment-method list, and creates shared risk, analytics, resources, localization, and screen-reader modules. A test or live client key must match the selected environment.

The registry maps payment-method transaction variants to native Components. For payment methods without a dedicated registered implementation, the runtime can use the generic redirect Component. Drop-in itself is not registered as a payment-method action Component.

## Sessions and advanced flow

With a Checkout Session, the SDK sends `sessionData` through setup, payment, payment-details, balance, order, cancellation, and donation service calls. Session setup returns the amount, locale, country, and payment methods that initialize the client.

The advanced flow delegates `/payments` to `onSubmit` and `/payments/details` to `onAdditionalDetails`. Responses can create redirect, 3DS2, voucher, QR-code, await, bank-transfer, or external-SDK actions. Redirect completion uses the configured details callback or the active Session; successful and failed terminal responses are routed to `onPaymentCompleted` and `onPaymentFailed`.

Session configuration is authoritative where the backend owns a setting. In `6.41.0`, Card component-level installments are hidden and a warning is emitted because the Sessions backend ignores that local configuration.

## Payment methods, stored methods, and Drop-in

The runtime processes regular and stored payment methods separately. Merchant allow/remove lists filter both groups, and stored methods are restricted to supported types with `Ecommerce` shopper interaction. Stored cards can inherit a funding source by matching their brand against the available card methods.

Drop-in creates and groups instant, stored, regular, and Fastlane elements, filters unavailable methods, tracks the active item, propagates amount changes, and mounts follow-up actions. Its payment-method list uses checked-state accessibility semantics even when the first method is not opened automatically.

## Card behavior

Card uses secured fields for sensitive input and can combine holder name, billing address, storage consent, dual-brand selection, installments, Click to Pay, Korean authentication fields, and Fastlane signup data.

Installments render only when configured options are nonempty, the amount is nonzero, and the card funding source is credit or unspecified. With split card funding sources, retained stories define the expected matrix:

| Funding source | Click to Pay | Installments |
| --- | --- | --- |
| Credit | Yes | Yes |
| Debit | Yes | No |
| Prepaid | No | No |

This is package-version implementation evidence, not a guarantee that a merchant's backend response enables each option.

## 3D Secure 2 and action safety

3DS2 device-fingerprint and challenge flows decode server tokens, create hidden or visible iframes, listen for `postMessage` completion, and enforce timeouts. The challenge path validates both the ACS URL and the origin derived from `threeDSNotificationURL` before rendering. Missing or invalid data is reported through the SDK error path instead of starting a flow that cannot complete.

The exact `6.41.0` release strengthens this boundary by detecting a challenge token whose notification URL lacks a valid domain. It also retains distinct `paymentData` and authorization-token handling between fingerprint, challenge, and redirect-derived flows.

In `6.42.0`, shared 3DS2 iframes accept explicit `allow` and optional `sandbox` attributes. Standard 3DS2 frames allow payment and public-key credential retrieval; an internal Visa passkey path can additionally permit credential creation and apply a constrained sandbox. The controlling `usePasskeyIFrameAttributes` flag is marked internal and requires the merchant-data flow, so this evidence does not establish a general merchant-facing configuration option.

## Accessibility

Secured-field iframes deliberately omit `role="presentation"` so assistive technology can discover their interactive content. The dual-brand selector uses buttons with keyboard handling and `aria-pressed`. A shared screen-reader panel announces validation and status messages through a polite live region, and submission errors are sorted by visual field order before focus moves to the first invalid field.

In `6.41.0`, Drop-in also restores `aria-checked` when `openFirstPaymentMethod` is false and replaces deprecated `keypress` handling with `keydown`.

## Analytics, risk, and sensitive-data boundary

The analytics layer queues component, action, error, and configuration events. Rendered-configuration analytics explicitly omit fields including `data`, holder name, shopper email, email, telephone number, and Click to Pay configuration.

From `6.42.0`, Drop-in emits `paymentListDisplayed` after its elements are created. The event records rendered methods in display order with `fastlane`, `instant`, `stored`, or `regular` display modes, plus methods returned by `/paymentMethods` that Drop-in did not render. Analytics construction is guarded so a reporting failure logs a warning instead of failing checkout rendering.

The optional risk module loads a hidden device-fingerprint iframe, validates the expected message origin, applies a 20-second timeout, and encodes the resulting risk payload. This client evidence does not describe Adyen's server-side risk decisioning.

## PayPal Fastlane dependency

Adyen Web contains a PayPal Fastlane Component and Card signup path. Valid signup configuration can propagate consent and optional phone data into encoded Card payment data. Release `6.41.0` depends on `@paypal/paypal-js@10.0.0`; `6.41.1` raises that dependency to `10.0.2`. The package augments the PayPal namespace with Fastlane types.

That dependency is an evidence boundary: questions about PayPal loader or delegated runtime behavior must also consult the independently collected `paypal/paypal-js` source rather than inferring those details from Adyen's adapter.

## `6.41.1` patch behavior

Release `6.41.1` fixes four narrow client behaviors without changing the broader Drop-in, Components, Sessions, or advanced-flow architecture:

- OpenInvoice error handling now searches and focuses within the current Component container. This prevents one OpenInvoice instance from focusing a matching field in another instance.
- Interactive selectors stop both `keypress` and `keydown` propagation. Pressing Enter while one of these controls is active no longer reaches the root submission handler and submits the payment unintentionally.
- Address formatting no longer trims or collapses whitespace during active input. `InputBase` still applies trimming on blur, avoiding duplicate characters with input method editors while preserving normalized completed values.
- BIN lookup narrows its internal element type to Card and Custom Card elements. This is an internal type-safety improvement, not a new merchant API.

The patch also raises `@paypal/paypal-js` from `10.0.0` to `10.0.2` and `@types/googlepay` from `0.7.10` to `0.7.11`. Delegated runtime behavior remains governed by those independently versioned packages.

## `6.42.0` minor-release behavior

Release `6.42.0` adds the Drop-in payment-list analytics event and the 3DS2 iframe attributes described above. It also fixes partial billing-address handling:

- When the country field is omitted from a partial-address form, the merchant-configured country is retained in form state and normalized to uppercase so country-specific formatting and validation still run.
- US postal codes use exact five-digit or ZIP+4 validation: `12345` or `12345-6789`.
- Country-specific postal formatting is selected from the retained country value rather than falling back to unrestricted formatting.

This is a contained minor release. It changes checkout telemetry, partial-address validation, and internal authentication-frame capabilities without replacing the established Drop-in, Components, Sessions, or advanced-flow architecture.

## `6.43.0` minor-release behavior

Released 2026-08-12 and delta-ingested against 6.42.0. The standard capsule retains 218 unchanged files and two changed package manifests; the approved 14-file supplement supplies the changed Select/Tag implementation, styles, and three stories.

- **Option tags:** internal `SelectItem.tags` accepts an array of labels with optional `info` or `success` styling; omitted variants default to `info`. Labels render literally, not as translation keys. Empty or missing tags render no tag-list node. These are presentation labels, not price, eligibility, or payment-state calculations.
- **Expanded versus collapsed:** options show supporting `secondaryText` below the name, with tags beside the content. The collapsed control shows the selected name and tags, but no supporting text. In filterable controls, selected tags are hidden while the list is open. Code: [list item](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b989173-20c08eb4/files/packages/lib/src/components/internal/FormFields/Select/components/SelectListItem.tsx), [button](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b989173-20c08eb4/files/packages/lib/src/components/internal/FormFields/Select/components/SelectButton.tsx).
- **Interaction correction:** clicking the filterable wrapper toggles the list and focuses the input; clicking the input while open keeps it open. Readonly controls do not attach these click/key handlers. Filtering still checks option names, not tag labels or supporting text; selection still rejects disabled options. Only the click-handler change is new in this delta, not all existing filter/selection behavior.
- **Layout and accessibility boundary:** name/input flex items can shrink and use ellipsis, while collapsed tags are limited to 50% width with overflow hidden. The existing polite result-announcement region gets a dedicated visually-hidden class. This is source/CSS evidence, not browser or screen-reader verification. Non-filterable controls with an ID label themselves through label/value IDs rather than necessarily including tag text in the accessible name.
- **Dependency:** `@paypal/paypal-js` changes from `10.0.2` to `10.0.3`. Do not infer a new Adyen payment capability from that bump; delegated package behavior belongs to [[source-github-paypal-js]]. Public package export mappings remain unchanged.

The [Select story](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b989173-20c08eb4/files/packages/lib/src/components/internal/FormFields/Select/Select.stories.tsx) covers tags, supporting text, long names, disabled options, filterable/non-filterable controls, and validation states. Tag and TagList stories demonstrate the variants and ordered multiple labels; they are examples, not executed tests.

**Migration:** recheck custom styling and any UX relying on supporting text remaining visible after collapse. Do not advertise the internal Select/Tag types as a new top-level merchant configuration API. No broad checkout architecture change or contradiction with earlier version-qualified knowledge was found.

## `6.44.0` minor-release behavior

Released 2026-08-19 and delta-ingested against 6.43.0 at SHA `f10995d33491d8107c01a27dec2bc1fc4d6e28b0`. The standard capsule has 24 modified files, one added file, and 196 unchanged files; the approved supplement adds 40 exact-SHA files. Review covered the assigned current source and supplementary implementation, not the entire upstream repository.

- **Keyboard dispatch:** the shared BaseElement/UIElement path moves from `keypress` to `keydown`, while the merchant callback remains `onEnterKeyPressed`. Without that callback, UIElement retains blur-then-submit behavior. Drop-in avoids submitting from a focused payment-method radio header; Click to Pay isolates its own Enter handling. The secured-field bridge still receives `enterKeyPressed` but dispatches a synthetic `keydown`. CustomCard's callback-only override and Giftcard's balance/payment routing remain distinct. This broadens the migration recorded for earlier releases, rather than asserting every path already migrated in 6.41.0.
- **Dual-brand selection:** the selector removes its bespoke Enter handler, suppresses action-key propagation on keydown, and retains click-based selection using native button activation. Related internal controls remove duplicate keypress handlers. See [[co-badged-cards]].
- **CVC and expiry guidance:** CVC rendering now receives the raw `errorCode` rather than already-translated text. For Amex, `cc.cvc.920` and `cc.cvc.921` resolve to `.amex` variants; other keys remain unchanged. Card and stored-card fields pass brand context, and the secured-field validation bridge applies the same mapping to `errorI18n` while retaining the raw error code. Release notes also report expiry/CVC format guidance in error states. Translation JSONs were not retained in this capsule, so this is not a full multilingual copy audit or a new top-level merchant API.
- **Null inputs and country normalization:** `useForm` normalizes null rules, formatters, default data, and field problems to empty objects, and null schema to an empty array. Address uses an empty address fallback. CardInput reads initial country null-safely and uppercases it before existing partial-address postal rules run. Required-field validation still applies; this is not universal malformed-input acceptance.
- **Screen-reader lifecycle:** the new loading hook announces completion only after loading has started. QRLoader owns its final announcement at a stable parent, avoiding a child-unmount/loading-effect overwrite. The generic accessibility hook no longer clears messages on unmount. Card error reporting passes whether errors were displayed so the no-error branch does not indiscriminately clear messages; this is not general message ownership tracking. Repeated identical nonempty messages get a new render key to trigger a DOM remount.
- **Dependencies and nonchanges:** Preact changes from `10.29.2` to `10.29.7`; the Secured Fields version constant changes from `6.2.1` to `6.3.0`. The external iframe runtime itself was not audited. `@paypal/paypal-js` stays at `10.0.3`. Changed 3DS2 files are formatting-only: the existing passkey iframe capability is not new in this release.

### 6.44.0 grounding

> `onKeyDown={stopPropagationForActionKeys}`
>
> [Dual-brand selector, line 43](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-14-f10995d/files/packages/lib/src/components/Card/components/CardInput/components/DualBrandSelector.tsx#L43)

> `'cc.cvc.920': 'cc.cvc.920.amex',`
>
> [CVC error mapping, line 200](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-14-f10995d/files/packages/lib/src/components/Card/components/CardInput/utils.ts#L200)

> `hasDisplayedErrors: !!sortedErrorList?.length`
>
> [Card screen-reader error reporting, line 46](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-14-f10995d/files/packages/lib/src/components/Card/components/CardInput/useSRPanelForCardInputErrors.ts#L46)

> `export const SF_VERSION = '6.3.0';`
>
> [Secured Fields constant, line 18](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-f10995d-55e9e1ba/files/packages/lib/src/components/internal/SecuredFields/lib/constants.ts#L18)

**Migration:** recheck merchant Enter handlers, nested interactive controls, Amex custom translation keys, null initial form data, lowercase partial-address countries, and loading/error announcements. No incompatible top-level export or broad architecture change was established. No browser, screen-reader, payment, or upstream test suite was executed.

**Mode decision:** the generated full/high recommendation remains recorded. Its security keyword signal matched "security code" (CVC), not evidence of a vulnerability. After supplement-backed source review bounded the changes, the user approved delta mode. Earlier version knowledge remains preserved.

## `6.45.0` review-page checkout and fixes

Released 2026-09-10; full-ingested additively on 2026-09-15 against 6.44.0 at SHA `b29934f6cf5de6e1912039f669b48ae45b75d3fd`. The standard capsule retains 221 files (13 modified, 208 unchanged); the approved 26-file supplement includes implementation, two architecture decisions, and three review-page story files. Full mode reflects a new cross-component payment lifecycle, not removal of earlier knowledge. The classifier's security signal concerns Content Security Policy, not established vulnerability evidence.

### Review and final submission

Core configuration adds `onReview(state, component, reviewDetails)` and `onAction(actionElement)`; both are propagated to Components. `ICore.processPayment(data: PaymentData): void` adds a component-independent Sessions submission path. See [[adyen-review-page-checkout]].

In [UIElement](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b29934f-d296b082/files/packages/lib/src/components/internal/UIElement/UIElement.tsx), submit first checks validity. If `onReview` is set, it optionally retrieves order status using the current order, emits review analytics, calls the callback with payment data and optional order status, then returns without normal payment execution. An order-status lookup failure still invokes review with empty details. Without review, the established payment execution path remains.

In [Core](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-14-b29934f/files/packages/lib/src/core/core.ts), `processPayment` requires a Session and calls its submission method directly. It does not re-run Component validation or `beforeSubmit`. An action creates a Component and requires `onAction` to mount it; a missing Session or action handler reports an implementation error through optional `onError`. An order with remaining balance calls `onOrderUpdated` and returns. Terminal results route to completion/failure callbacks after cleanup; completion does not supply the original payment Component. Cancellation errors are ignored.

**Merchant responsibilities:** preserve required validation and data transformation before final confirmation, prevent repeated or stale submissions, own action mounting/disposal, and implement error and partial-order recovery. This method returns `void`, not a Promise, and has no local in-flight guard. Advanced integrations must continue their own backend `/payments` flow and create returned actions; `processPayment` is not an Advanced API. Configuring `onAction` also intercepts ordinary mounted UIElement payment responses even without review. This does not establish that every additional-details or redirect-return path has changed.

### Buttons and payment-method exceptions

The internal PayButton review flag chooses the translated Continue label before custom text, amount, and zero-value authorization labels, and suppresses the icon. Its secondary amount-label helper is unchanged. Card, BacsDD, stored PayByBankUS, stored PayTo, and Twint pass this flag. A custom button calling normal submit retains the validity/review path; there is no new universal merchant `showReview` API.

| Retained path | 6.45.0 behavior |
| --- | --- |
| Google Pay | Its submit/payment-authorized path calls payment execution directly, bypassing inherited review. |
| Klarna | Widget enabled: direct payment execution and no review label. Widget disabled: inherited submit. |
| Gift card | Initial Redeem is not review; insufficient balance or transaction limit creates/reuses an order and pays before final review. Sufficient-balance confirmation uses inherited submit. |
| PayByBankPix | Hosted stored-payment branch bypasses review; merchant-page redirect still uses inherited submit. |
| Apple Pay, Amazon Pay, PayPal, ANCV | ADR/type comments document exclusions; complete implementations were not retained in this supplement. Do not infer new built-in PayPal review support from the ADR's Advanced-flow discussion. |

The [review stories](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b29934f-d296b082/files/packages/lib/storybook/stories/demos/ReviewPage/review-page-renders.tsx) demonstrate Card and Drop-in with NL Sessions. They retain payment data, session ID and optional order status, then initialize a review-page checkout using the Session ID. Card end digits are separately captured from `onFieldValid`. The [review screen](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b29934f-d296b082/files/packages/lib/storybook/stories/demos/ReviewPage/ReviewPage.tsx) disables confirmation while unready/submitting and mounts actions in a modal. It is an example, not production-complete: it prints the entire payment payload, lacks full error/order recovery and cleanup, and does not close the modal in every failure path. Do not reproduce that payload display in production.

### Donation, CSP, form and rendering changes

- **Donation:** `commercialTxAmount` becomes optional, falling back to checkout amount and then zero; a missing/zero amount still cannot support round-up donation. `processPayment` does not automatically set up Sessions donation presentation. Merchants inspect `askDonation` and construct Donation explicitly. No new `onDonationAvailable` callback is established.
- **Google Pay CSP:** optional `nonce` is forwarded to PaymentOptions and to the Google Pay script attribute when this loader injects it. An already-loaded Google runtime is not modified. This does not generate a nonce, configure CSP headers, or verify the external runtime. See [GooglePayService](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b29934f-d296b082/files/packages/lib/src/components/GooglePay/GooglePayService.ts).
- **Address:** street, house number and city stop silently stripping the former punctuation set; blur validation instead rejects emoji and control/format characters while allowing ordinary punctuation and multilingual text. The Unicode regex includes pictographic, regional-indicator and keycap forms. Older browsers without Unicode property escapes fall back to narrower control-character checks. GB postcode formatting strips invalid characters and caps length at eight before existing postcode validation. This is not a general sanitization/security guarantee. Error key `field.error.invalidCharacters` and analytics code 937 are added; translation coverage was not audited. See [validator utilities](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b29934f-d296b082/files/packages/lib/src/utils/validator-utils.ts).
- **Drop-in:** PaymentMethodDetails retains its vnode in a ref and renders on transition to selected, avoiding repeated component rendering/state resets and render analytics across list re-renders. This is not persistence across reloads. See [implementation](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-14-b29934f/files/packages/lib/src/components/Dropin/components/PaymentMethod/PaymentMethodDetails.tsx).
- **Select:** text/filter-input end spacing grows with mirrored RTL rules; the content gap shrinks and secondary-label color uses the label token. No browser layout validation was performed.
- **Dependencies and maintenance:** PayPal JS 10.0.3 to 10.1.0, Preact 10.29.7 to 10.29.8, Google Pay types 0.7.11 to 0.7.12. Delegated PayPal behavior belongs to [[source-github-paypal-js]]. Strict-null migration tooling/backlog is not proof that the entire library is strict-null clean. The retained README marks v6 active, v5 inactive, v4 EOL August 2026 and v3 EOL October 2025; this is release-qualified documentation, not a live support-policy check.

### Documentation discrepancies and grounding

> [!warning] Contradiction
> The exact-SHA ADR-0004 says `askDonation` requires a cast, but `PaymentCompletedData` and `SessionsResponse` already include it. ADR-0003 describes `core.update` with remaining-order handling, but this `processPayment` branch only calls `onOrderUpdated`. The blanket PayByBankPix exclusion is also broader than its retained branch behavior. See [[adyen-review-page-checkout]]; implementation governs these version-specific details and raw ADRs remain unchanged.

> `if (this.props.onReview) {`
>
> [UIElement, line 261](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b29934f-d296b082/files/packages/lib/src/components/internal/UIElement/UIElement.tsx#L261)

> `public processPayment(data: PaymentData): void {`
>
> [Core, line 371](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-14-b29934f/files/packages/lib/src/core/core.ts#L371)

> `this.options.onOrderUpdated?.({ order });`
>
> [Core, line 403](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-14-b29934f/files/packages/lib/src/core/core.ts#L403)

> `nonce?: string;`
>
> [Google Pay configuration, line 13](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b29934f-d296b082/files/packages/lib/src/components/GooglePay/types.ts#L13)

> `this.commercialTxAmount = donationCampaignProps.commercialTxAmount ?? checkout.options.amount?.value ?? 0;`
>
> [Donation service, line 34](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b29934f-d296b082/files/packages/lib/src/components/Donation/DonationCampaignService.tsx#L34)

No upstream tests, browser, screen-reader, payment, or delegated wallet runtime were executed. Diff test excerpts are source evidence, not executed proof. Full ingestion covers the assigned packet and supplement, not the entire upstream tree.

## `6.45.1` regression and internal refactor

Released 2026-09-16; additive full ingest against 6.45.0. Manual review overrides the generated delta recommendation because public Card/UIElement status-method signatures lose their second argument. The user approved focused reading of all 14 changed retained files, the complete comparison, four exact-SHA supplements and existing wiki history; 207 unchanged files and manifest inventories were checked mechanically. No older knowledge was replaced.

- **Action regression:** upstream explicitly marks this release do not use. In the [UIElement supplement](../../../../raw/github/adyen/adyen-web/supplements/2026-09-22-0d1e033-6cf5ddf4/files/packages/lib/src/components/internal/UIElement/UIElement.tsx), `setElementStatus(status)` and `setStatus(status)` stop forwarding the prior `props` argument. [Card](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-22-0d1e033/files/packages/lib/src/components/Card/Card.tsx) does likewise. Drop-in introduces an `elementRef` declaration and its own status-forwarding override, while its action handler still supplies `{ component: paymentAction }`. These are observed changes, not proof of the precise runtime cause. The base mount algorithm and UIElement action-response routing remain unchanged in the diff.
- **Not type-only:** the complete diff also changes component-reference wiring and form guards. The useForm supplement narrows reducer/action types and changes event-target detection; initial null-default normalization from 6.44.0 remains. No new payment method or replacement for the 6.45.0 review lifecycle is established.
- **Address lookup story:** the rejection example now uses `actions.reject({ errorMessage: 'Something went wrong, try adding manually.' })` rather than a string. Its catch still falls through to `actions.resolve(formattedData)`, so it is not a production-complete error-recovery template. See the [Card story](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-22-0d1e033/files/packages/lib/src/components/Card/stories/Card.stories.tsx).
- **Presentation and maintenance:** release notes report updated link styles; diff hunks show underlining, hover weight and highlight-token changes. Click to Pay wrapper props are reorganized and typed. Runtime dependencies stay at PayPal JS 10.1.0, Preact 10.29.8 and Google Pay types 0.7.12; development dependencies change. Diff-only component/style evidence is not a complete audit of those excluded implementations.

### 6.45.1 grounding

> `DO NOT USE THIS VERSION: Contains a bug with handling payment actions. Upgrade to 6.45.2`
>
> [Release notes](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.45.1/2026-09-22/release-notes.md)

> `public setStatus(status: UIElementStatus): this {`
>
> [Card](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-22-0d1e033/files/packages/lib/src/components/Card/Card.tsx)

> `this.elementRef?.setStatus?.(status);`
>
> [UIElement](../../../../raw/github/adyen/adyen-web/supplements/2026-09-22-0d1e033-6cf5ddf4/files/packages/lib/src/components/internal/UIElement/UIElement.tsx)

**Migration and limits:** follow the upstream warning rather than adapting a production integration to this bad release. No browser, payment-action reproduction, upstream tests or delegated runtime verification was performed. See [[adyen-review-page-checkout]] for preserved lifecycle responsibilities.

## `6.45.2` payment-action rollback fix

Released 2026-09-21; delta-ingested against 6.45.1 after complete reading of ten changed retained files, the complete comparison, four exact-SHA supplemental implementations and cumulative history. The 211 unchanged retained files and manifest inventories were checked mechanically. Delta records a bounded restoration of the established baseline, not a claim that all public types remained compatible with the intervening bad release.

- **Action/status restoration:** [UIElement](../../../../raw/github/adyen/adyen-web/supplements/2026-09-22-386715e-542cc72c/files/packages/lib/src/components/internal/UIElement/UIElement.tsx) restores `setElementStatus(status, props?)` and `setStatus(status, props?)` forwarding. [Card](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-22-386715e/files/packages/lib/src/components/Card/Card.tsx) again forwards props to its primary component while passing only status to Click to Pay. [Drop-in](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-22-386715e/files/packages/lib/src/components/Dropin/Dropin.tsx) removes the new `elementRef` declaration and override; its action handler still supplies the created component through status props. Upstream calls this a fix for payment-action mounting; no single-line root cause or runtime reproduction is established here.
- **Review lifecycle preserved:** the complete UIElement supplement and retained Core, Card, Drop-in and DropinComponent implementations match the 6.45.0 evidence byte-for-byte. `onReview`, `onAction` and Sessions `processPayment` remain; the merchant responsibilities in [[adyen-review-page-checkout]] still apply.
- **Types and form behavior roll back too:** `PaymentData.clientStateDataIndicator` and the `OnChangeData.errors` entry's `error`/`rootNode` fields become required again in TypeScript, and the fingerprint result type returns to its earlier shape. These are not newly mandated server request fields. The useForm event-target guard and reducer optional-access changes are reverted, while null initial-default normalization remains. Integrations adapted specifically to 6.45.1 types should rerun their type checks.
- **Not a complete release rollback:** comparing all 221 retained files directly with 6.45.0 leaves six differing files: root and library package manifests, Card/types.ts (formatting only), ClickToPayHolder, ClickToPayWrapper and Card.stories. The latter three preserve the already-read 6.45.1 changes, including object-shaped address rejection and its catch/resolve caveat. This inventory comparison does not establish equality of excluded upstream files. Runtime dependency versions remain unchanged; library package exports and dependencies are also unchanged versus 6.45.1.

### 6.45.2 grounding

> `Fixed: revert internal changes to remove implicit and explicit any from BaseElement and UIElement to fix issue with payment actions mounting`
>
> [Release notes](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.45.2/2026-09-22/release-notes.md)

> `this.elementRef?.setStatus(status, props);`
>
> [UIElement status forwarding](../../../../raw/github/adyen/adyen-web/supplements/2026-09-22-386715e-542cc72c/files/packages/lib/src/components/internal/UIElement/UIElement.tsx)

> `this.setStatus(paymentAction.props.statusType, { component: paymentAction });`
>
> [Drop-in action handling](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-22-386715e/files/packages/lib/src/components/Dropin/Dropin.tsx)

**Migration and limits:** 6.45.2 is the replacement named by the collected 6.45.1 warning. Recheck action mounting, additional-details completion, custom status handling and TypeScript compilation. No upstream build, tests, browser, payment or delegated runtime execution was performed. Older knowledge remains available and the 6.45.1 warning is not removed.

## `6.41.0` release findings

The release propagates the `healthcare` field to `onBinLookup`, validates the 3DS2 challenge notification domain, and replaces deprecated `keypress` events. It removes several explicit `any` types, prevents misleading component-level installments in Sessions, and fixes Drop-in checked-state accessibility.

These are patch findings. The broader architecture above is the accumulated source present at the same exact SHA.

## Related

- [[adyen-review-page-checkout]] - opt-in review lifecycle and merchant responsibilities from 6.45.0
- [[changelog-github-adyen-web]] — package-qualified release ledger
- [[adyen]] — company and knowledge-status page
- [[co-badged-cards]] — cross-provider card-network choice concept
- [[source-github-paypal-js]] — independent evidence for the delegated PayPal JS dependency

## Raw sources

- [6.45.2 snapshot](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-22-386715e/manifest.json)
- [6.45.2 supplement](../../../../raw/github/adyen/adyen-web/supplements/2026-09-22-386715e-542cc72c/manifest.json)
- [6.45.2 release identity](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.45.2/2026-09-22/manifest.json)
- [6.45.2 release notes](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.45.2/2026-09-22/release-notes.md)
- [6.45.1 to 6.45.2 comparison](../../../../tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.45.1--6.45.2/comparison.json)

- [6.45.1 snapshot](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-22-0d1e033/manifest.json)
- [6.45.1 supplement](../../../../raw/github/adyen/adyen-web/supplements/2026-09-22-0d1e033-6cf5ddf4/manifest.json)
- [6.45.1 release identity](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.45.1/2026-09-22/manifest.json)
- [6.45.1 release notes](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.45.1/2026-09-22/release-notes.md)
- [6.45.0 to 6.45.1 comparison](../../../../tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.45.0--6.45.1/comparison.json)

- [6.45.0 snapshot](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-14-b29934f/manifest.json)
- [6.45.0 supplement](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b29934f-d296b082/manifest.json)
- [6.45.0 release identity](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.45.0/2026-09-14/manifest.json)
- [6.45.0 release notes](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.45.0/2026-09-14/release-notes.md)
- [6.44.0 to 6.45.0 comparison](../../../../tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.44.0--6.45.0/comparison.json)

- [6.44.0 snapshot](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-14-f10995d/manifest.json)
- [6.44.0 supplement](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-f10995d-55e9e1ba/manifest.json)
- [6.44.0 release identity](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.44.0/2026-09-14/manifest.json)
- [6.44.0 release notes](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.44.0/2026-09-14/release-notes.md)
- [6.43.0 to 6.44.0 comparison](../../../../tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.43.0--6.44.0/comparison.json)

- [6.43.0 snapshot](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-14-b989173/manifest.json)
- [6.43.0 supplement](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b989173-20c08eb4/manifest.json)
- [6.43.0 release identity](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.43.0/2026-09-14/manifest.json)
- [6.43.0 release notes](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.43.0/2026-09-14/release-notes.md)
- [6.42.0 to 6.43.0 comparison](../../../../tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.42.0--6.43.0/comparison.json)

- Current snapshot manifest: `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/manifest.json`
- `6.42.0` release manifest: `raw/github/adyen/adyen-web/releases/adyen-web/6.42.0/2026-08-09/manifest.json`
- `6.42.0` release notes: `raw/github/adyen/adyen-web/releases/adyen-web/6.42.0/2026-08-09/release-notes.md`
- `6.41.1` to `6.42.0` comparison: `tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.41.1--6.42.0/comparison.md`
- `6.42.0` source supplement: `raw/github/adyen/adyen-web/supplements/2026-08-09-1e157f8-b6a47e83/manifest.json`
- Current snapshot manifest: `raw/github/adyen/adyen-web/snapshots/2026-08-09-c98ea8a/manifest.json`
- `6.41.1` release manifest: `raw/github/adyen/adyen-web/releases/adyen-web/6.41.1/2026-08-09/manifest.json`
- `6.41.1` release notes: `raw/github/adyen/adyen-web/releases/adyen-web/6.41.1/2026-08-09/release-notes.md`
- `6.41.0` to `6.41.1` comparison: `tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.41.0--6.41.1/comparison.md`
- `6.41.1` source supplement: `raw/github/adyen/adyen-web/supplements/2026-08-09-c98ea8a-4b5b69c5/manifest.json`
- Snapshot manifest: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/manifest.json`
- Release manifest: `raw/github/adyen/adyen-web/releases/adyen-web/6.41.0/2026-07-26/manifest.json`
- Release notes: `raw/github/adyen/adyen-web/releases/adyen-web/6.41.0/2026-07-26/release-notes.md`
- README: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/README.md`
- Core: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/core/core.ts`
- Drop-in: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/Dropin/`
- Card: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/Card/`
- 3DS2: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/ThreeDS2/`
- Analytics: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/core/Analytics/`
