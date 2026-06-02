---
title: "GitHub: paypal/paypal-js"
type: source
date_ingested: 2026-04-13
original_format: github-repo
raw_files:
  - "github-paypal-js.md"
tags: [paypal, javascript-sdk, npm, typescript, loadscript, v5, v6, paypal-js, types, monorepo]
---

## GitHub: paypal/paypal-js

The official PayPal JS SDK monorepo — source of `@paypal/paypal-js` (vanilla JS loader + TypeScript types) and `@paypal/react-paypal-js` (React library, README already ingested separately).

Repo URL: <https://github.com/paypal/paypal-js>

Commit SHA: `f59f94baefea4b2ddb38553669ed0ac4ede86167` | Reviewed: 2026-04-13

## Key Takeaways

### Package scope

| Package | npm | Purpose |
| ------- | --- | ------- |
| `@paypal/paypal-js` | Saved | Vanilla JS async loader + TS types for SDK v5 and v6 |
| `@paypal/react-paypal-js` | Previously ingested | React wrapper (see [[source-paypal-react-paypal-js-readme]]) |
| `@paypal/react-paypal-js-storybook` | Not saved | Storybook docs — out of scope |

### `loadScript(options, PromisePonyfill?)` — implementation details

From `src/load-script.ts`:

- Resolves to `null` in Node/Deno (no `document`)
- **Caching**: if a script tag with identical URL + attributes already exists AND `window.paypal` (or custom namespace) is already set, returns the existing namespace immediately without re-inserting the script
- Automatically sets `data-js-sdk-library="paypal-js"` on the script tag
- Returns `Promise<PayPalNamespace | null>`
- Accepts optional `PromisePonyfill` as second argument for IE 11 compatibility

### `PayPalScriptOptions` type — complete interface

From `types/script-options.d.ts`:

```typescript
interface PayPalScriptOptions {
    // Query parameters
    clientId: string;           // required
    buyerCountry?: string;
    commit?: boolean;
    components?: string[] | string;  // array auto-joined to comma-separated
    currency?: string;
    debug?: boolean | string;
    disableFunding?: string[] | string;
    enableFunding?: string[] | string;
    integrationDate?: string;
    intent?: string;
    locale?: string;
    merchantId?: string[] | string;  // array with >1 items → merchant-id=*, data-merchant-id=
    vault?: boolean | string;

    // Data attributes
    dataClientToken?: string;
    dataCspNonce?: string;
    dataClientMetadataId?: string;
    dataJsSdkLibrary?: string;
    dataMerchantId?: string[] | string;
    dataNamespace?: string;
    dataPageType?: string;
    dataPartnerAttributionId?: string;
    dataSdkIntegrationSource?: string;
    dataUid?: string;
    dataUserIdToken?: string;

    // Script attributes
    crossorigin?: "anonymous" | "use-credentials";

    // Special
    environment?: "production" | "sandbox";
    sdkBaseUrl?: string;        // local development only
}
```

### `merchantId` array handling

When `merchantId` is an array with >1 elements, `loadScript` automatically:
- Sets query param `merchant-id=*` (for edge cache configuration)
- Moves actual values to `data-merchant-id` attribute (comma-separated)

When array has exactly 1 element, passes as normal `merchant-id` query param.

### V6 SDK — new `createInstance()` pattern

From `types/v6/index.d.ts` — SDK v6 introduces a fundamentally different architecture:

```typescript
// 1. Load the core SDK
const paypal = await loadCoreSdkScript({ environment: "sandbox" });

// 2. Create an instance with explicit component selection
const sdkInstance = await paypal.createInstance({
    clientId: "YOUR_CLIENT_ID",
    components: ["paypal-payments", "card-fields"],
    locale: "en-US",
    pageType: "checkout"
});

// 3. Check eligibility before rendering
const eligibility = await sdkInstance.findEligibleMethods();
if (eligibility.isEligible("paypal")) {
    const session = sdkInstance.createPayPalOneTimePaymentSession({ onApprove });
    await session.start({ presentationMode: "popup" }, createOrderFn);
}
```

### V6 components (TypeScript types available)

| Component | Description |
| --------- | ----------- |
| `paypal-payments` | PayPal one-time, save, Pay Later |
| `paypal-guest-payments` | Guest checkout with cards |
| `venmo-payments` | Venmo integration |
| `card-fields` | Customisable card fields |
| `paypal-messages` | Messaging component |
| `paypal-subscriptions` | Subscription handling |
| `paypal-legacy-billing-agreements` | Legacy billing |
| `applepay-payments` | Apple Pay |
| `googlepay-payments` | Google Pay |

Import V6 types from `@paypal/paypal-js/sdk-v6` subpath.

### V6 vs V5 — key architectural difference

| Aspect | V5 (current) | V6 (new) |
| ------ | ------------ | -------- |
| Loading | `loadScript()` | `loadCoreSdkScript()` |
| Namespace | `window.paypal.*` | `paypal.createInstance()` |
| Components | Script tag `components=` param | Explicit array in `createInstance()` |
| Eligibility | `paypal.isFundingEligible()` | `sdkInstance.findEligibleMethods()` |
| Sessions | N/A | `createPayPalOneTimePaymentSession()` etc. |

### `loadCustomScript` utility

Generic script loader — loads any URL, returns `Promise<void>`. Used internally by `loadScript` and exposed for custom use cases.

## Files Saved

| File | Purpose |
| ---- | ------- |
| `packages/paypal-js/README.md` | Full API docs including v6 |
| `packages/paypal-js/src/load-script.ts` | Core loader implementation |
| `packages/paypal-js/src/utils.ts` | Option processing, script insertion utilities |
| `packages/paypal-js/types/script-options.d.ts` | `PayPalScriptOptions` TypeScript interface |
| `packages/paypal-js/types/v6/index.d.ts` | V6 namespace, `createInstance`, component types |
| `packages/paypal-js/types/v6/components/paypal-payments.d.ts` | V6 `paypal-payments` type definitions |
| `packages/paypal-js/types/apis/orders.d.ts` | Orders API TypeScript types |
| `packages/paypal-js/package.json` | Package metadata and export paths |

## Raw Sources

- [[github-paypal-js]] — stub file with repo metadata and file list
- Detail directory: `raw/github-paypal-js/`

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept
- [[paypal-expanded-checkout]] — Expanded Checkout (uses card-fields component)
- [[source-paypal-javascript-sdk-configuration]] — JS SDK script parameters
- [[source-paypal-javascript-sdk-reference]] — JS SDK API reference
- [[source-paypal-react-paypal-js-readme]] — React wrapper package
