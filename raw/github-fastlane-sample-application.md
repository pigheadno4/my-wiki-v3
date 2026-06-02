<!-- Repo: https://github.com/paypal-examples/fastlane-sample-application -->
<!-- Commit SHA: bd9ba8cabede84c59919fe08791e9cec048a22c1 -->
<!-- Date reviewed: 2026-04-13 -->
<!-- Detail directory: raw/github-fastlane-sample-application/ -->
<!-- Files saved (read directly from these paths):
  raw/github-fastlane-sample-application/README.md
  raw/github-fastlane-sample-application/server/.env.example
  raw/github-fastlane-sample-application/server/node/src/server.js
  raw/github-fastlane-sample-application/server/shared/views/checkout.html
  raw/github-fastlane-sample-application/server/shared/views/checkout-flexible.html
  raw/github-fastlane-sample-application/client/html/src/init-fastlane.js
  raw/github-fastlane-sample-application/client/html/src/init-fastlane-flexible.js
  raw/github-fastlane-sample-application/server/python/server.py
  raw/github-fastlane-sample-application/server/java/src/main/java/com/fastlane/paypalsample/sample/ServerController.java
  raw/github-fastlane-sample-application/client/vue/src/views/CheckoutView.vue
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from https://github.com/paypal-examples/fastlane-sample-application at commit SHA bd9ba8cabede84c59919fe08791e9cec048a22c1, then save any newly discovered files into raw/github-fastlane-sample-application/ preserving their repo-relative paths -->

# Fastlane Sample Application

Official PayPal demo repo for Fastlane integration. Supports 3 client frameworks (HTML, Vue, Angular) × 6 server languages (Node.js, Python, Ruby, PHP, Java, .NET) = 18 Codespaces configurations.

Two integration patterns:
- **Quick Start** — `FastlanePaymentComponent` (pre-built UI, less code)
- **Flexible** — `FastlaneCardComponent` + custom billing form (more control)

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/github-fastlane-sample-application/README.md` | Repo overview, Quick Start vs Flexible feature comparison, Codespaces links table |
| `raw/github-fastlane-sample-application/server/.env.example` | All required env vars: PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET, DOMAINS, PAYPAL_MERCHANT_ID, PAYPAL_BN_CODE |
| `raw/github-fastlane-sample-application/server/node/src/server.js` | Node.js server: getClientToken(), getAccessToken(), getAuthAssertionToken(), createOrder(), renderCheckout(), Express routes |
| `raw/github-fastlane-sample-application/server/shared/views/checkout.html` | Quick Start HTML template: email section, shipping section, payment section with #payment-component div |
| `raw/github-fastlane-sample-application/server/shared/views/checkout-flexible.html` | Flexible HTML template: adds separate billing section, #selected-card + #card-component divs |
| `raw/github-fastlane-sample-application/client/html/src/init-fastlane.js` | Quick Start JS: full Fastlane SDK init, email lookup/auth flow, FastlanePaymentComponent, checkout submit |
| `raw/github-fastlane-sample-application/client/html/src/init-fastlane-flexible.js` | Flexible JS: FastlaneCardComponent, showCardSelector(), memberHasSavedPaymentMethods state, getPaymentToken({ billingAddress }) |
| `raw/github-fastlane-sample-application/server/python/server.py` | Python Flask server: same 3-token pattern (client token, access token, auth assertion) + /transaction endpoint |
| `raw/github-fastlane-sample-application/server/java/src/main/java/com/fastlane/paypalsample/sample/ServerController.java` | Java Spring Boot controller: client token, access token, create order endpoints |
| `raw/github-fastlane-sample-application/client/vue/src/views/CheckoutView.vue` | Vue 3 Quick Start checkout: Composition API, same Fastlane SDK flow in Vue component |
