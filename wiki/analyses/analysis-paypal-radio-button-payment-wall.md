---
title: "PayPal Radio Button Payment Wall: PayPal + Pay Later with Funding Eligibility (Non-US Merchant, US Buyers)"
type: analysis
date_created: 2026-04-16
tags: [paypal, pay-later, radio-button, payment-wall, funding-eligibility, marks, standalone-buttons, js-sdk, bnpl, messaging, cross-border, us]
---

## Overview

A radio button payment wall lets buyers select a payment method before a button is shown. This guide covers how to integrate **PayPal** and **Pay Later** as two separate radio button options for a **non-US merchant account targeting US buyers**, with:

- Pay Later message shown **alongside the radio label** (before selection) to surface the offer early
- Pay Later message shown **below the Pay Later button** (after selection) using `contextualComponents: 'PAY_LATER_BUTTON'`
- Pay Later button styled **blue** to visually distinguish it from the PayPal button (gold)
- Funding eligibility gating so ineligible options are never shown

**Scope:** Non-US merchant account, US buyers, USD. Requires PayPal approval for cross-border messaging (limited release) — contact your PayPal account manager before going live. See [[analysis-paypal-pay-later-fr-integration-guide]] for the approval process details.

> **Key difference from US merchant integration:** Because the merchant account is not US-based, `data-pp-buyercountry="US"` must be added to **every** `data-pp-message` element, and `enable-funding=paylater` must be present in the SDK URL. Without these, Pay Later messages will not render and the Pay Later button may not appear.

## Prerequisites

- Non-US PayPal Business account with an existing Checkout integration
- PayPal approval for cross-border messaging (limited release)
- Orders REST API integration

## SDK Script Tag

One `<script>` tag. `enable-funding=paylater` is required for a non-US merchant account — without it the Pay Later button will not render. `marks` provides logo images next to radio labels. `funding-eligibility` enables `isEligible()`:

```html
<script
  src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages,buttons,funding-eligibility,marks&currency=USD&enable-funding=paylater"
></script>
```

## HTML Structure

Each payment method row is **hidden by default** and revealed only when eligibility is confirmed. Pay Later has two message placements: one in the radio label area (always visible when the row is shown) and one inside the button panel (visible after selection). Both carry `data-pp-buyercountry="US"`.

```html
<!-- ── PayPal row ──────────────────────────────────────────────── -->
<div id="row-paypal" class="payment-row" style="display: none;">
  <label>
    <input type="radio" name="payment-method" value="paypal" />
    <span id="mark-paypal"></span>   <!-- PayPal mark rendered here -->
    <span>PayPal</span>
  </label>
  <!-- Button panel: hidden until radio selected -->
  <div id="panel-paypal" class="payment-panel" style="display: none;">
    <div id="button-paypal"></div>
  </div>
</div>

<!-- ── Pay Later row ──────────────────────────────────────────── -->
<div id="row-paylater" class="payment-row" style="display: none;">
  <label>
    <input type="radio" name="payment-method" value="paylater" />
    <span id="mark-paylater"></span>  <!-- Pay Later mark rendered here -->
    <span>Pay Later</span>
    <!-- Message alongside the radio label — surfaces the offer before selection -->
    <div
      data-pp-message
      data-pp-placement="payment"
      data-pp-amount="150.00"
      data-pp-buyercountry="US"
      data-pp-style-layout="text"
      data-pp-style-logo-type="none"
      data-pp-style-text-color="black"
      data-pp-style-text-size="12"
    ></div>
  </label>
  <!-- Button panel: hidden until radio selected -->
  <div id="panel-paylater" class="payment-panel" style="display: none;">
    <div id="button-paylater"></div>
    <!-- Message below the button, coordinated with PAY_LATER_BUTTON context -->
    <div
      data-pp-message
      data-pp-placement="payment"
      data-pp-amount="150.00"
      data-pp-buyercountry="US"
      data-pp-contextualcomponents="PAY_LATER_BUTTON"
    ></div>
  </div>
</div>
```

> **Why two messages?**
>
> - **Radio label message** (`logo-type: none`) — shows "Pay in 4 installments of $X" before the buyer selects Pay Later, helping them understand the offer upfront without cluttering the label.
> - **Panel message** (`contextualComponents: PAY_LATER_BUTTON`) — shows Pay Later messaging below the button after selection, coordinating visually with the blue Pay Later button. `PAY_LATER_BUTTON` suppresses the logo since the button itself carries the brand.

## JavaScript — Eligibility Check and Rendering

```javascript
// ── Shared order logic ────────────────────────────────────────────────────
function createOrder(data, actions) {
  return actions.order.create({
    purchase_units: [{
      amount: {
        currency_code: 'USD',
        value: '150.00'  // Update to actual cart total
      }
    }]
  });
}

function onApprove(data, actions) {
  return actions.order.capture().then(function(details) {
    console.log('Order captured:', details);
    // Redirect to confirmation page
  });
}

function onError(err) {
  console.error('PayPal error:', err);
}

// ── Helper: wire all radio inputs to show/hide panels ─────────────────────
function bindRadioToggle(value, panelId) {
  document.querySelectorAll('input[name="payment-method"]')
    .forEach(function(radio) {
      radio.addEventListener('change', function() {
        // Collapse all panels
        document.querySelectorAll('.payment-panel')
          .forEach(function(panel) { panel.style.display = 'none'; });
        // Expand the selected method's panel
        if (this.value === value) {
          document.getElementById(panelId).style.display = 'block';
        }
      });
    });
}

// ── PayPal button (gold — default) ────────────────────────────────────────
(function() {
  var paypalButton = paypal.Buttons({
    fundingSource: paypal.FUNDING.PAYPAL,
    style: {
      color: 'gold',   // default; explicit for clarity
      shape: 'rect',
      layout: 'vertical',
    },
    createOrder: createOrder,
    onApprove: onApprove,
    onError: onError
  });

  if (paypalButton.isEligible()) {
    document.getElementById('row-paypal').style.display = 'block';
    paypal.Marks({ fundingSource: paypal.FUNDING.PAYPAL })
      .render('#mark-paypal');
    paypalButton.render('#button-paypal');
    bindRadioToggle('paypal', 'panel-paypal');
  }
  // Not eligible → row stays hidden, option never shown
})();

// ── Pay Later button (blue — distinct from PayPal gold) ───────────────────
(function() {
  var payLaterButton = paypal.Buttons({
    fundingSource: paypal.FUNDING.PAYLATER,
    style: {
      color: 'blue',   // distinguishes from PayPal gold button
      shape: 'rect',
      layout: 'vertical',
    },
    createOrder: createOrder,
    onApprove: onApprove,
    onError: onError
  });

  if (payLaterButton.isEligible()) {
    document.getElementById('row-paylater').style.display = 'block';
    paypal.Marks({ fundingSource: paypal.FUNDING.PAYLATER })
      .render('#mark-paylater');
    payLaterButton.render('#button-paylater');
    bindRadioToggle('paylater', 'panel-paylater');
  }
  // Not eligible → row stays hidden, option never shown
})();

// ── Pre-select first eligible row ─────────────────────────────────────────
var firstRadio = document.querySelector(
  '.payment-row:not([style*="display: none"]) input[type="radio"]'
);
if (firstRadio) {
  firstRadio.checked = true;
  firstRadio.dispatchEvent(new Event('change'));
}
```

## React Integration (`@paypal/react-paypal-js`)

Install the package:

```bash
npm install @paypal/react-paypal-js
```

### Key components used

| Component | Purpose |
| --- | --- |
| `<PayPalScriptProvider>` | Loads the SDK once at the app root — replaces the `<script>` tag |
| `<PayPalButtons>` | Renders a button for a specific `fundingSource`; internally calls `isEligible()` |
| `<PayPalMarks>` | Renders the payment method logo image |
| `<PayPalMessages>` | Renders Pay Later messaging |
| `usePayPalScriptReducer` | Hook to read SDK loading state (`isPending`, `isResolved`, `isRejected`) |
| `FUNDING` | Exported constants — `FUNDING.PAYPAL`, `FUNDING.PAYLATER` |

### Provider setup

`PayPalScriptProvider` accepts camelCase versions of all SDK URL parameters. Place it at the app root, not inside the checkout component:

```jsx
import { PayPalScriptProvider } from "@paypal/react-paypal-js";

const PAYPAL_OPTIONS = {
  clientId: "YOUR_CLIENT_ID",
  buyerCountry: "US",          // sandbox only — remove in production
  currency: "USD",
  components: "messages,buttons,funding-eligibility,marks",
  enableFunding: "paylater",   // required for non-US merchant accounts
};

export default function App() {
  return (
    <PayPalScriptProvider options={PAYPAL_OPTIONS}>
      <CheckoutPage />
    </PayPalScriptProvider>
  );
}
```

### Eligibility handling

`<PayPalButtons>` internally calls `isEligible()`. When ineligible it renders its `children` prop instead of the button — use this to detect and hide the radio row:

```jsx
import {
  PayPalButtons,
  PayPalMarks,
  PayPalMessages,
  FUNDING,
  usePayPalScriptReducer,
} from "@paypal/react-paypal-js";

function PaymentWall() {
  const [{ isResolved }] = usePayPalScriptReducer();
  const [selected, setSelected] = useState(null);
  const [paypalEligible, setPaypalEligible]   = useState(null); // null = unknown
  const [payLaterEligible, setPayLaterEligible] = useState(null);

  // Pre-select first eligible row once both are resolved
  useEffect(() => {
    if (paypalEligible === null || payLaterEligible === null) return;
    if (selected !== null) return;
    if (paypalEligible) setSelected("paypal");
    else if (payLaterEligible) setSelected("paylater");
  }, [paypalEligible, payLaterEligible, selected]);

  if (!isResolved) return <p>Checking payment options…</p>;

  return (
    <div className="payment-wall">

      {/* ── PayPal row ── */}
      {/* Hidden probe — detects eligibility without showing a button */}
      <div style={{ display: "none" }}>
        <PayPalButtons
          fundingSource={FUNDING.PAYPAL}
          onInit={() => setPaypalEligible(true)}
          createOrder={createOrder} onApprove={onApprove} onError={onError}
        >
          {/* children renders when ineligible */}
          <IneligibleSignal onIneligible={() => setPaypalEligible(false)} />
        </PayPalButtons>
      </div>

      {paypalEligible && (
        <div className="payment-row">
          <label>
            <input type="radio" name="payment-method" value="paypal"
              checked={selected === "paypal"}
              onChange={() => setSelected("paypal")} />
            <PayPalMarks fundingSource={FUNDING.PAYPAL} />
            <span>PayPal</span>
          </label>
          {selected === "paypal" && (
            <div className="panel">
              <PayPalButtons
                fundingSource={FUNDING.PAYPAL}
                style={{ color: "gold", shape: "rect", layout: "vertical" }}
                createOrder={createOrder} onApprove={onApprove} onError={onError}
              />
            </div>
          )}
        </div>
      )}

      {/* ── Pay Later row ── */}
      <div style={{ display: "none" }}>
        <PayPalButtons
          fundingSource={FUNDING.PAYLATER}
          onInit={() => setPayLaterEligible(true)}
          createOrder={createOrder} onApprove={onApprove} onError={onError}
        >
          <IneligibleSignal onIneligible={() => setPayLaterEligible(false)} />
        </PayPalButtons>
      </div>

      {payLaterEligible && (
        <div className="payment-row">
          <label>
            <input type="radio" name="payment-method" value="paylater"
              checked={selected === "paylater"}
              onChange={() => setSelected("paylater")} />
            <PayPalMarks fundingSource={FUNDING.PAYLATER} />
            <span>Pay Later</span>
            {/* Inline message alongside label */}
            <PayPalMessages
              style={{ layout: "text", logo: { type: "none" }, text: { color: "black", size: 12 } }}
              amount={150.00}
              placement="payment"
              buyerCountry="US"
            />
          </label>
          {selected === "paylater" && (
            <div className="panel">
              <PayPalButtons
                fundingSource={FUNDING.PAYLATER}
                style={{ color: "blue", shape: "rect", layout: "vertical" }}
                createOrder={createOrder} onApprove={onApprove} onError={onError}
              />
              {/* Message below button */}
              <PayPalMessages
                amount={150.00}
                placement="payment"
                buyerCountry="US"
                contextualComponents="PAY_LATER_BUTTON"
              />
            </div>
          )}
        </div>
      )}

    </div>
  );
}

// Renders when PayPalButtons is ineligible — fires callback then returns null
function IneligibleSignal({ onIneligible }) {
  const called = useRef(false);
  useEffect(() => {
    if (!called.current) { called.current = true; onIneligible(); }
  }, [onIneligible]);
  return null;
}
```

### React-specific notes

| Topic | Detail |
| --- | --- |
| SDK URL params | Use camelCase in `options`: `clientId`, `enableFunding`, `buyerCountry` — the provider converts them to query params automatically |
| `buyerCountry` | Same cross-border requirement as vanilla JS — pass it in both `PAYPAL_OPTIONS` and as a prop on each `<PayPalMessages>` |
| Eligibility probe | `<PayPalButtons>` doesn't expose `isEligible()` directly — use a hidden probe + `children` ineligible fallback to detect it |
| `onInit` | Fires when the button initialises successfully (i.e. is eligible) — use this alongside the `children` fallback to set eligibility state |
| `forceReRender` | Pass `forceReRender={[amount]}` to `<PayPalButtons>` if the order amount changes dynamically — triggers a full button re-render |
| `usePayPalScriptReducer` | Use `isResolved` to gate rendering — avoids flashing "no options" before the SDK finishes loading |
| Do not nest `PayPalScriptProvider` | Place it once at the app root, not inside the payment wall component |

## Message Placement Summary

| Placement | `data-pp-` config | Visible when |
| --- | --- | --- |
| Alongside radio label | `buyercountry: US`, `logo-type: none`, `placement: payment` | Pay Later row is eligible (always visible in row) |
| Below Pay Later button | `buyercountry: US`, `contextualComponents: PAY_LATER_BUTTON` | Buyer selects Pay Later radio |

## Eligibility Flow

```text
SDK loads (enable-funding=paylater present)
    │
    ├─ PAYPAL.isEligible()?
    │       yes → show row, render gold mark + gold button
    │       no  → row stays hidden
    │
    └─ PAYLATER.isEligible()?
            yes → show row, render Pay Later mark + blue button + label message
            no  → row stays hidden

Buyer selects radio
    └─ collapse all panels → expand selected panel
            PAYPAL selected   → show gold button
            PAYLATER selected → show blue button + panel message (PAY_LATER_BUTTON)
```

## Button Color Reference

| Button | `style.color` | Rationale |
| --- | --- | --- |
| PayPal | `gold` (default) | PayPal's recommended color; highest recognition and conversion |
| Pay Later | `blue` | PayPal's first alternative; distinct from gold, still on-brand |

Valid color values: `gold`, `blue`, `silver`, `white`, `black`.

## Why `isEligible()` Is the Right Gate

| Mechanism | What it does | Sufficient alone? |
| --- | --- | --- |
| `enable-funding=paylater` in SDK URL | Tells SDK to attempt loading Pay Later for non-US merchant | No — enables eligibility check, does not guarantee it passes |
| `paypal.Buttons(...).isEligible()` | Per-session runtime check: does this buyer/amount/account qualify? | Yes — definitive gate |

Always call `isEligible()` before rendering. Never show a radio row for a button that may not render.

## Key Rules

| Rule | Detail |
| --- | --- |
| PayPal approval required | Cross-border messaging is **limited release** — must be approved before going live |
| `enable-funding=paylater` | **Required** for non-US merchant accounts — Pay Later button will not render without it |
| `data-pp-buyercountry="US"` | **Required** on every `data-pp-message` element — messages will not render for non-US merchants without it |
| `funding-eligibility` component | Required in `components=` for `isEligible()` to work |
| `marks` component | Required in `components=` to use `paypal.Marks()` |
| `messages` component | Required in `components=` for `data-pp-message` elements |
| Gate radio row on `isEligible()` | Never show a radio option for a button that won't render |
| One SDK load per page | All components in a single `<script>` tag |
| `message` inside `Buttons()` | **US merchants + US buyers only** — not applicable here; use standalone `data-pp-message` with `buyercountry` instead |
| No content modification | Cannot translate, resize, recolor, or modify Pay Later message text |
| Dynamic amount update | Set `data-pp-amount` attribute directly; SDK auto-re-renders — do not call `render()` again |

## Relevant Wiki Pages

- [[paypal-checkout]] — Base Checkout integration
- [[paypal-pay-later]] — Pay Later product details by country
- [[analysis-paypal-pay-later-fr-integration-guide]] — Cross-border messaging approval process and FR-specific example

## Sources

- [[source-paypal-checkout-standalone-buttons]] — `isEligible()`, `paypal.FUNDING.*`, radio button + Marks pattern, `enable-funding`; `paypal.Marks({ fundingSource: paypal.FUNDING.PAYLATER })` confirmed to render a Pay Later mark (verified via sandbox demo)
- [[source-paypal-checkout-display-payment-methods]] — Radio button payment wall structure, show/hide toggle
- [[source-paypal-checkout-display-funding-source]] — `fundingSource` values, Pay Later localisation table
- [[source-paypal-pay-later]] — Pay Later messaging, `data-pp-*` attributes, `contextualComponents` values, cross-border `buyerCountry`
- [[source-paypal-checkout-messaging-with-buttons]] — US-only scope confirmation for `message` inside `Buttons()`
- [[source-paypal-react-paypal-js-readme]] — `@paypal/react-paypal-js`: `PayPalScriptProvider`, `PayPalButtons`, `PayPalMarks`, `PayPalMessages`, `usePayPalScriptReducer`, `FUNDING` constants
