import { useState, useRef, useEffect } from "react";
import {
  PayPalScriptProvider,
  PayPalButtons,
  PayPalMarks,
  PayPalMessages,
  FUNDING,
  usePayPalScriptReducer,
} from "@paypal/react-paypal-js";

// ── SDK options ────────────────────────────────────────────────────────────
// Scope: non-US merchant account targeting US buyers (cross-border)
// buyer-country is sandbox-only — remove when using a production client-id
const PAYPAL_OPTIONS = {
  clientId: "test",
  buyerCountry: "US",           // sandbox only
  currency: "USD",
  components: "messages,buttons,funding-eligibility,marks",
  enableFunding: "paylater",    // required for non-US merchant accounts
};

const AMOUNT = "150.00";

// ── Shared order callbacks ─────────────────────────────────────────────────
function createOrder(data, actions) {
  return actions.order.create({
    purchase_units: [{ amount: { currency_code: "USD", value: AMOUNT } }],
  });
}

function onApprove(data, actions) {
  return actions.order.capture().then((details) => {
    alert("Payment captured! Transaction ID: " + details.id);
  });
}

function onError(err) {
  console.error("PayPal error:", err);
  alert("Something went wrong. Check console for details.");
}

// ── PaymentWall ────────────────────────────────────────────────────────────
function PaymentWall() {
  const [{ isResolved }] = usePayPalScriptReducer();
  const [selected, setSelected] = useState(null);   // "paypal" | "paylater"
  const [paypalEligible, setPaypalEligible] = useState(null);    // null = unknown
  const [payLaterEligible, setPayLaterEligible] = useState(null);

  // Once we know eligibility for both, pre-select the first eligible option
  useEffect(() => {
    if (paypalEligible === null || payLaterEligible === null) return;
    if (selected !== null) return;  // already selected
    if (paypalEligible) setSelected("paypal");
    else if (payLaterEligible) setSelected("paylater");
  }, [paypalEligible, payLaterEligible, selected]);

  if (!isResolved) {
    return <p className="loading">Checking payment options…</p>;
  }

  const noneEligible = paypalEligible === false && payLaterEligible === false;

  return (
    <div className="payment-wall">
      {/* ── PayPal row ── */}
      <PayPalButtons
        fundingSource={FUNDING.PAYPAL}
        style={{ color: "gold", shape: "rect", layout: "vertical" }}
        createOrder={createOrder}
        onApprove={onApprove}
        onError={onError}
        // children renders when ineligible — we use it to track eligibility
        // and keep the row hidden
        onInit={() => setPaypalEligible(true)}
      >
        {/* ineligible fallback — signal to hide the row */}
        <IneligibleSignal onIneligible={() => setPaypalEligible(false)} />
      </PayPalButtons>

      {paypalEligible && (
        <div className={`payment-row ${paypalEligible ? "" : "hidden"}`}>
          <label className="radio-label">
            <input
              type="radio"
              name="payment-method"
              value="paypal"
              checked={selected === "paypal"}
              onChange={() => setSelected("paypal")}
            />
            <span className="mark">
              <PayPalMarks fundingSource={FUNDING.PAYPAL} />
            </span>
            <span className="label-text">PayPal</span>
          </label>
          {selected === "paypal" && (
            <div className="panel">
              <PayPalButtons
                fundingSource={FUNDING.PAYPAL}
                style={{ color: "gold", shape: "rect", layout: "vertical" }}
                createOrder={createOrder}
                onApprove={onApprove}
                onError={onError}
              />
            </div>
          )}
        </div>
      )}

      {/* ── Pay Later row ── */}
      {/* Eligibility probe — renders nothing visible, just checks eligibility */}
      <div style={{ display: "none" }}>
        <PayPalButtons
          fundingSource={FUNDING.PAYLATER}
          style={{ color: "blue", shape: "rect", layout: "vertical" }}
          createOrder={createOrder}
          onApprove={onApprove}
          onError={onError}
          onInit={() => setPayLaterEligible(true)}
        >
          <IneligibleSignal onIneligible={() => setPayLaterEligible(false)} />
        </PayPalButtons>
      </div>

      {payLaterEligible && (
        <div className="payment-row">
          <label className="radio-label">
            <input
              type="radio"
              name="payment-method"
              value="paylater"
              checked={selected === "paylater"}
              onChange={() => setSelected("paylater")}
            />
            <span className="mark">
              <PayPalMarks fundingSource={FUNDING.PAYLATER} />
            </span>
            <span className="label-text">Pay Later</span>
            {/* Inline message alongside label — buyerCountry set at provider level */}
            <span className="label-message">
              <PayPalMessages
                style={{ layout: "text", logo: { type: "none" }, text: { color: "black", size: 12 } }}
                amount={parseFloat(AMOUNT)}
                placement="payment"
                buyerCountry="US"
              />
            </span>
          </label>
          {selected === "paylater" && (
            <div className="panel">
              <PayPalButtons
                fundingSource={FUNDING.PAYLATER}
                style={{ color: "blue", shape: "rect", layout: "vertical" }}
                createOrder={createOrder}
                onApprove={onApprove}
                onError={onError}
              />
              {/* Message below button — PAY_LATER_BUTTON context */}
              <div className="panel-message">
                <PayPalMessages
                  amount={parseFloat(AMOUNT)}
                  placement="payment"
                  buyerCountry="US"
                  contextualComponents="PAY_LATER_BUTTON"
                />
              </div>
            </div>
          )}
        </div>
      )}

      {noneEligible && (
        <p className="no-options">No PayPal payment options available for this session.</p>
      )}
    </div>
  );
}

// ── IneligibleSignal ───────────────────────────────────────────────────────
// PayPalButtons renders `children` when isEligible() === false.
// We use this to fire a callback so parent knows the option is ineligible.
function IneligibleSignal({ onIneligible }) {
  const called = useRef(false);
  useEffect(() => {
    if (!called.current) {
      called.current = true;
      onIneligible();
    }
  }, [onIneligible]);
  return null;
}

// ── App ────────────────────────────────────────────────────────────────────
export default function App() {
  return (
    <PayPalScriptProvider options={PAYPAL_OPTIONS}>
      <div className="checkout-card">
        <h1>Complete your order</h1>
        <p className="subtitle">
          Demo — non-US merchant / US buyers (cross-border)
        </p>

        <div className="order-summary">
          <span className="item">Demo Product × 1</span>
          <span className="price">${AMOUNT}</span>
        </div>

        <div className="section-title">Pay with</div>
        <PaymentWall />
      </div>
    </PayPalScriptProvider>
  );
}
