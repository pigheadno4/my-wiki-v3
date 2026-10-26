# Q1 — Purpose, scope and limits

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-android-sdk.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-duitnow-android-component.md` → pinned raw.

This 2019-modified, 2026-09-15-captured source adds DuitNow to existing **Android Components** Sessions and Advanced integrations (raw `adyen/docs/payment-methods/duitnow/android-component/2026-09-15.md:6-29,135-142`). Its Sessions table states minimum version 5.0.0, while the Advanced requirements table states no minimum (raw lines 27-30,137-142). It does not provide a complete base integration, establish current method enablement or prove a successful transaction. No QR/action outcome or webhook sequence is documented here; the Advanced section supplies only request examples (raw lines 173-200,401-413).

# Q2 — Central capability, prerequisites and warnings

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-android-sdk.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-duitnow-android-component.md`. Online-payment retrieval can also pass through `wiki/concepts/adyen-online-payments.md`.

Both branches require an existing Android Components integration and Support-assisted addition of DuitNow in Customer Area (raw `adyen/docs/payment-methods/duitnow/android-component/2026-09-15.md:25-30,137-142`). Sessions needs no extra DuitNow session parameters or Component configuration and uses `InstantPaymentComponent` with `duitnow`, via Compose or View examples (raw lines 32-132). Advanced likewise says no specific configuration and shows an illustrative MYR `/payments` request with `paymentMethod.type: duitnow` (raw lines 144-200). The Compose snippet includes a stray `Component` line and several language examples omit request construction, so examples are not turnkey implementations (raw lines 83-110,202-399). Test guidance calls for real details and small amounts; live acceptance requires Support addition in live Customer Area (raw lines 401-407).
