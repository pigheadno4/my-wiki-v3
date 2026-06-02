---
title: "PayPal JS SDK v5 vs v6: Multi-Country Switching & Pay Later Messaging"
type: analysis
date_created: 2026-05-07
tags: [paypal, javascript-sdk, jsv5, jsv6, react, npm, multi-country, cross-border, pay-later, messaging, performance, spa, ssr, runtime-configuration]
---

## Summary

Architectural comparison of PayPal JS SDK v5 (npm `@paypal/react-paypal-js` v8.x) vs JS SDK v6 (npm v9.x) for multi-country sites that need to switch currency, locale, and Pay Later messaging without page reloads. v6's runtime configuration model eliminates the full script reload that v5 requires on every country switch.

## Core architectural difference

### v5: Load-time configuration

All config is baked into the script URL as query params. The script tag IS the configuration:

```html
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&currency=USD&locale=en_US&components=messages,buttons&enable-funding=paylater"></script>
```

The SDK reads params from `document.currentScript.src` at load time — they are **frozen** once the script loads. Changing currency, locale, or components requires removing the script tag and loading a new one with different URL params.

### v6: Runtime configuration

The script is a **static, param-free loader** — same file regardless of country, currency, or use case:

```html
<script async src="https://www.paypal.com/web-sdk/v6/core"></script>
```

All configuration happens through JavaScript API calls after the script loads:

- `createInstance({ locale })` — SDK initialization
- `findEligibleMethods({ currencyCode })` — eligibility check (API call)
- `createPayPalMessages({ buyerCountry, currencyCode })` — messaging config

## React package comparison: v8.x vs v9.x

### Architecture

```
v8.x (SDK v5):
PayPalScriptProvider
  options={{ clientId, currency, intent, locale }}
  → Loads: <script src="...?client-id=X&currency=USD">
  → usePayPalScriptReducer() ← dispatch("resetOptions") to reload script
  → <PayPalButtons />  <PayPalMessages />

v9.x (SDK v6):
PayPalProvider
  clientId={...}  locale="fr-FR"  pageType="checkout"
  → Loads: <script src=".../web-sdk/v6/core">  (static)
  → createInstance() internally
  → useEligibleMethods({ currencyCode })  ← runtime
  → usePayPalMessages({ buyerCountry, currencyCode })
  → <PayPalOneTimePaymentButton />  <paypal-message />
```

### Component mapping

| v8.x | v9.x | Notes |
|---|---|---|
| `PayPalScriptProvider` | `PayPalProvider` | Different props shape |
| `options={{ clientId, currency }}` | `clientId={...}` (no currency prop) | Currency moved to hooks |
| `usePayPalScriptReducer` | `usePayPal` | No dispatch/reducer pattern |
| `dispatch("resetOptions")` | Change props / re-call hooks | No manual reload needed |
| `PayPalButtons` | `PayPalOneTimePaymentButton` | One component per payment type |
| `PayPalMessages` | `usePayPalMessages` hook + `<paypal-message>` | Hook + web component |
| `PayPalCardFieldsProvider` | `PayPalCardFieldsProvider` | Similar, different import path |
| `createOrder` returns `orderId` string | `createOrder` returns `{ orderId }` object | Breaking change |
| `deferLoading={true}` | Pass `undefined` clientId, set later | Different deferred pattern |
| N/A | `eligibleMethodsResponse` prop | SSR pre-fetch (new in v9) |
| N/A | `useEligibleMethods()` | Explicit eligibility (new in v9) |

### Import path change

```typescript
// v8.x
import { PayPalScriptProvider, PayPalButtons, PayPalMessages } from "@paypal/react-paypal-js";

// v9.x
import { PayPalProvider, PayPalOneTimePaymentButton, usePayPalMessages } from "@paypal/react-paypal-js/sdk-v6";
```

## Country/currency switching

### v5/v8.x: `resetOptions` = full SDK reload

```typescript
const [{ options }, dispatch] = usePayPalScriptReducer();

function onCountryChange(country) {
  // RELOADS the entire SDK script with new URL params
  // All child components unmount → remount
  dispatch({
    type: "resetOptions",
    value: {
      ...options,
      currency: countryConfig[country].currency,
      locale: countryConfig[country].locale,
    },
  });
}

// What happens internally:
// 1. Old <script src="...?currency=USD&locale=en_US"> removed
// 2. New <script src="...?currency=EUR&locale=fr_FR"> injected
// 3. isPending → true (all buttons disappear)
// 4. Script loads, parses, initializes
// 5. isPending → false → isResolved
// 6. All components re-render from scratch
// Total: ~1-3s of blank state
```

### v6/v9.x: props change → no script reload

```typescript
function App() {
  const [country, setCountry] = useState("US");
  const { currency, locale, buyerCountry } = countryConfig[country];

  return (
    <PayPalProvider
      key={locale}  // force remount only when locale changes
      clientId={CLIENT_ID}
      components={["paypal-payments", "paypal-messages"]}
      locale={locale}
    >
      <CheckoutPage currency={currency} buyerCountry={buyerCountry} />
    </PayPalProvider>
  );
}

function CheckoutPage({ currency, buyerCountry }) {
  // Currency change = just a new eligibility check (API call only)
  const { eligiblePaymentMethods, isLoading } = useEligibleMethods({
    currencyCode: currency,
  });

  const { handleFetchContent } = usePayPalMessages({
    buyerCountry,
    currencyCode: currency,
  });

  if (isLoading) return <Skeleton />;

  return (
    <>
      {eligiblePaymentMethods?.isEligible("paylater") && (
        <PayLaterOneTimePaymentButton {...} />
      )}
      <paypal-message ref={handleFetchContent} amount={150} />
    </>
  );
}
```

> [!warning] React remount behavior
> Using `key={locale}` on `PayPalProvider` forces React to unmount and remount the entire subtree when locale changes. This triggers `createInstance()` again. When only currency changes (same locale), React re-renders without remount — hooks re-run but the SDK instance is reused.

## Pay Later messaging: cross-border configuration

### v5: `buyerCountry` per element

```html
<!-- Every message div needs buyerCountry repeated -->
<div data-pp-message data-pp-placement="product" data-pp-amount="150.00" data-pp-buyercountry="FR" />
```

```javascript
paypal.Messages({ amount: 150, placement: 'product', buyerCountry: 'FR' }).render('.pp-message');
```

### v6: `buyerCountry` per instance

```javascript
// Set once at the messages instance level
const messagesInstance = sdkInstance.createPayPalMessages({
  buyerCountry: "FR",
  currencyCode: "EUR",
});

// Each element just needs fetchContent
await messagesInstance.fetchContent(document.querySelector('paypal-message'));
```

### React v9.x hook

```typescript
const { handleFetchContent, handleCreateLearnMore } = usePayPalMessages({
  buyerCountry: "FR",
  currencyCode: "EUR",
});

return <paypal-message ref={handleFetchContent} amount={150} />;
```

| Aspect | v5 | v6 |
|---|---|---|
| Element | `<div data-pp-message>` | `<paypal-message>` custom Lit component |
| buyerCountry scope | Per-element (`data-pp-buyercountry` on each div) | Per-instance (`createPayPalMessages({ buyerCountry })`) |
| Render API | `paypal.Messages({...}).render('.selector')` | `messagesInstance.fetchContent(element)` |
| Learn More modal | Auto-attached | Explicit `createLearnMore()` or `auto-bootstrap` attribute |
| Auto-bootstrap | Not available | `<paypal-message auto-bootstrap>` — no JS needed for basic rendering |
| Caching | None | Local, CDN, and site caching for faster visibility |

## Performance: operation cost breakdown

| Operation | What happens | Estimated latency | When required |
|---|---|---|---|
| v5 script reload | Network fetch JS bundle + parse + initialize + render | ~1-3s (even if cached, re-parse + re-init) | Every currency/locale change |
| v6 `createInstance()` | SDK initialization, component loading, internal setup | ~200-500ms | Every locale change |
| v6 `findEligibleMethods()` | API call to PayPal → server evaluates eligibility | ~300-800ms | Every currency change |
| v6 `createPayPalMessages()` | Local instance creation | ~10-50ms | Every buyerCountry or currency change |
| v6 `fetchContent(element)` | API call — fetches promotional content for amount/currency/country | ~200-500ms each | Every re-render |
| v6 `createLearnMore(element)` | Local modal attachment | ~10ms | After fetchContent |

## Performance: switching patterns (with 3 message placements)

### Pattern 1: Naive — no caching (v6)

```javascript
async function switchCountry(country) {
  const { currency, locale, buyerCountry } = countryConfig[country];

  const sdkInstance = await window.paypal.createInstance({
    clientId: CLIENT_ID,
    components: ["paypal-payments", "paypal-messages"],
    locale,
  });

  const methods = await sdkInstance.findEligibleMethods({ currencyCode: currency });

  const messagesInstance = sdkInstance.createPayPalMessages({ buyerCountry, currencyCode: currency });
  await messagesInstance.fetchContent(document.querySelector('#msg-product'));
  await messagesInstance.fetchContent(document.querySelector('#msg-cart'));
  await messagesInstance.fetchContent(document.querySelector('#msg-checkout'));
}
// Total: ~1.1-2.8s (serial). No better than v5 in practice.
```

### Pattern 2: Cache instances by locale (recommended)

```javascript
const instanceCache = new Map();

async function getOrCreateInstance(locale) {
  if (instanceCache.has(locale)) return instanceCache.get(locale);
  const instance = await window.paypal.createInstance({
    clientId: CLIENT_ID,
    components: ["paypal-payments", "paypal-messages"],
    locale,
  });
  instanceCache.set(locale, instance);
  return instance;
}

async function switchCountry(country) {
  const { currency, locale, buyerCountry } = countryConfig[country];
  const sdkInstance = await getOrCreateInstance(locale);
  const methods = await sdkInstance.findEligibleMethods({ currencyCode: currency });
  // ... render
}
// Cache hit: ~300-800ms. Cache miss: ~500-1300ms.
```

### Pattern 3: Pre-warm top locales at page load

```javascript
async function preWarmInstances() {
  const topLocales = ["en-US", "fr-FR", "en-GB", "de-DE"];
  await Promise.allSettled(
    topLocales.map(async (locale) => {
      const instance = await window.paypal.createInstance({
        clientId: CLIENT_ID,
        components: ["paypal-payments", "paypal-messages"],
        locale,
      });
      instanceCache.set(locale, instance);
    })
  );
}
// Upfront cost: ~500ms (parallel). All subsequent switches: ~300-800ms.
```

### Pattern 4: Maximum parallelism (fastest)

```javascript
async function switchCountry(country) {
  const { currency, locale, buyerCountry } = countryConfig[country];
  const sdkInstance = await getOrCreateInstance(locale);

  const messagesInstance = sdkInstance.createPayPalMessages({
    buyerCountry, currencyCode: currency,
  });

  // Eligibility + all message fetches run simultaneously
  const [methods] = await Promise.all([
    sdkInstance.findEligibleMethods({ currencyCode: currency }),
    Promise.all([
      messagesInstance.fetchContent(document.querySelector('#msg-product')),
      messagesInstance.fetchContent(document.querySelector('#msg-cart')),
      messagesInstance.fetchContent(document.querySelector('#msg-checkout')),
    ]),
  ]);
  // Total: ~300-800ms (limited by slowest API call)
}
```

### Timing comparison

| Pattern | First switch | Repeat (same locale) | UX blank state | Page load cost |
|---|---|---|---|---|
| **v5 resetOptions** | ~2-5s | ~2-5s (full reload again) | Yes — all components unmount | None |
| **v6 Pattern 1 (naive)** | ~1.1-2.8s | ~1.1-2.8s | No | None |
| **v6 Pattern 2 (cached)** | ~500-1350ms | ~300-800ms (cache hit) | No | None |
| **v6 Pattern 3 (pre-warm)** | ~300-800ms | ~300-800ms | No | ~500ms (parallel) |
| **v6 Pattern 4 (full parallel)** | ~300-800ms | ~300-800ms | No | ~500ms if pre-warmed |

### Per-switch-type cost (v6 Pattern 2)

| Switch | Locale changes? | What happens | Cost |
|---|---|---|---|
| Currency only (rare) | No | Hooks re-run | ~300-800ms |
| US → FR | `en-US` → `fr-FR` Yes | Instance cache miss → `createInstance` + eligibility | ~500-1350ms first, ~300-800ms after |
| FR → DE | `fr-FR` → `de-DE` Yes | Instance cache miss → same | ~500-1350ms first, ~300-800ms after |
| FR → BE (same locale) | No | Re-render only | ~300-800ms |

## Browser caching advantage

v5: each config permutation = different script URL = different browser cache entry:

```
https://www.paypal.com/sdk/js?client-id=X&currency=USD&locale=en_US  ← cache entry 1
https://www.paypal.com/sdk/js?client-id=X&currency=EUR&locale=fr_FR  ← cache entry 2
https://www.paypal.com/sdk/js?client-id=X&currency=GBP&locale=en_GB  ← cache entry 3
```

v6: every user worldwide downloads the same file = single cache entry:

```
https://www.paypal.com/web-sdk/v6/core  ← one cache entry for all
```

## SSR support (v9.x exclusive)

v9.x can pre-fetch eligibility on the server, eliminating the client-side API call on first load:

```typescript
// Next.js server component
import { useFetchEligibleMethods } from "@paypal/react-paypal-js/sdk-v6/server";

export default async function CheckoutPage() {
  const eligibility = await useFetchEligibleMethods({
    environment: "sandbox",
    headers: { Authorization: `Bearer ${token}` },
    payload: {
      purchase_units: [{ amount: { currency_code: "EUR", value: "100.00" } }],
    },
  });

  return (
    <PayPalProvider
      clientId={clientId}
      eligibleMethodsResponse={eligibility}  // skip client-side fetch
    >
      <CheckoutForm />
    </PayPalProvider>
  );
}
```

v8.x has no SSR support — eligibility is always resolved client-side after script loads.

## UX recommendations

### Use skeleton loading on locale switch

When `key={locale}` changes and `PayPalProvider` remounts, show a skeleton that preserves layout:

```typescript
function CheckoutPage({ currency, buyerCountry }) {
  const { isLoading } = useEligibleMethods({ currencyCode: currency });

  if (isLoading) {
    return (
      <div>
        <div className="skeleton-button" />
        <div className="skeleton-message" />
      </div>
    );
  }

  return <>{/* actual buttons and messages */}</>;
}
```

### Group EUR countries for cache efficiency

FR, DE, ES, IT all use EUR. Caching `createInstance` per locale means 4 separate instances, but subsequent same-locale switches are free. The first visit to each locale is the only expensive one.

## Recommendations

| Scenario | Best pattern |
|---|---|
| Multi-country SPA (general) | Pattern 2 (lazy cache) — best balance of cost and complexity |
| Frequent country switching (travel/comparison site) | Pattern 3 (pre-warm) + Pattern 4 (parallel) |
| SSR / Next.js | v9.x with `eligibleMethodsResponse` — eliminates initial eligibility latency |
| Single-country site | No switching needed — v6 still wins on async loading and explicit eligibility |

## Sources

- [[source-npm-react-paypal-js-v9]] — v9.x npm README with PayPalProvider, hooks, SSR
- [[source-paypal-react-paypal-js-readme]] — v8.x npm README with PayPalScriptProvider, resetOptions
- [[source-paypal-js-sdk-v6-setup]] — JS SDK v6 setup: createInstance, findEligibleMethods
- [[source-paypal-js-sdk-v5-to-v6-upgrade]] — v5→v6 upgrade guide: script URL → runtime config
- [[source-paypal-pay-later-upgrade-v6]] — Pay Later messaging v5→v6: paypal-message component, fetchContent, auto-bootstrap
- [[source-paypal-pay-later-cross-border]] — Cross-border messaging: buyerCountry parameter, limited release
- [[source-github-paypal-js-v6]] — GitHub paypal/paypal-js monorepo: SDK v6 + React v9 source code
