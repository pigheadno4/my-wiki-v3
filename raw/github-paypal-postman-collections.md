<!-- Repo: https://github.com/paypal/postman-collections -->
<!-- Commit SHA: ee698700c9e9164b68226f53266b08c6b3d83557 -->
<!-- Date reviewed: 2026-04-16 -->
<!-- Detail directory: raw/github-paypal-postman-collections/ -->
<!-- Files saved (read directly from these paths):
  raw/github-paypal-postman-collections/README.md
  raw/github-paypal-postman-collections/paypal-postman-lib/README.md
  raw/github-paypal-postman-collections/paypal-postman-lib/src/auth.ts
  raw/github-paypal-postman-collections/paypal-postman-lib/src/utils.ts
  raw/github-paypal-postman-collections/paypal-postman-lib/src/types.ts
  raw/github-paypal-postman-collections/paypal-postman-lib/src/index.ts
  raw/github-paypal-postman-collections/Collections/PayPal_Public_APIs.json
  raw/github-paypal-postman-collections/Collections/PayPal_Checkout_Flows.json
  raw/github-paypal-postman-collections/Collections/PayPal_Partner_APIs.json
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from the repo URL at the commit SHA above, then save any newly discovered files into raw/github-paypal-postman-collections/ preserving their repo-relative paths -->

# PayPal Postman Collections

GitHub: https://github.com/paypal/postman-collections
Postman workspace: https://postman.com/paypal

Backup of PayPal's public Postman collections. Recommended use: fork from postman.com/paypal (stays in sync with updates). Importing JSON directly means no future updates.

## What each file covers

| File | What to find there |
| --- | --- |
| `raw/github-paypal-postman-collections/README.md` | Repo overview, fork vs import guidance, Postman workspace link |
| `raw/github-paypal-postman-collections/paypal-postman-lib/README.md` | Library features, setup instructions, all available functions with usage examples |
| `raw/github-paypal-postman-collections/paypal-postman-lib/src/auth.ts` | OAuth2 token management: needsNewAccessToken, refreshAccessToken, storeAccessToken |
| `raw/github-paypal-postman-collections/paypal-postman-lib/src/utils.ts` | Utilities: isSandbox, getPayPalDebugId, base64Url, getJWT, getAuthAssertionFor |
| `raw/github-paypal-postman-collections/paypal-postman-lib/src/types.ts` | TypeScript type definitions for all library functions |
| `raw/github-paypal-postman-collections/paypal-postman-lib/src/index.ts` | Main library exports |
| `raw/github-paypal-postman-collections/Collections/PayPal_Public_APIs.json` | 80+ API requests: Auth, Orders, Payments, Invoices, Subscriptions, Payouts, Webhooks |
| `raw/github-paypal-postman-collections/Collections/PayPal_Checkout_Flows.json` | Checkout flow sequences: vault (card/PayPal, 3DS/non-3DS), FXaaS, Payment Links |
| `raw/github-paypal-postman-collections/Collections/PayPal_Partner_APIs.json` | Partner/marketplace APIs (1.8MB) |

## Collection structure summary

### PayPal_Public_APIs.json

- **Authorization**: Generate/terminate access token, user info, client token
- **Orders**: Create, confirm, show, update, authorize, capture, 3DS confirm, tracking
- **Payments**: Authorize/reauthorize/void/capture, refund, show details
- **Invoices**: Full CRUD, QR code, send/remind/cancel, record payment/refund, templates
- **Subscriptions**: Products (CRUD), Plans (CRUD + pricing), Subscriptions (full lifecycle)
- **Payouts**: Create batch, show batch/item details, cancel unclaimed item
- **Webhooks**: List events, create/list/show webhook

### PayPal_Checkout_Flows.json

- **Vault flows**: Card (non-3DS + 3DS) and PayPal vault before/during purchase
- **Recurring revenue**: Returning buyer pay with vault, subscription cancel/delete PMT
- **PayPal + Expanded Checkout**: 3DS confirm, authorize/capture, create/show order
- **Currency Exchange (FXaaS)**: Quote, order with FX, order with FX + card
- **Payment Links and Buttons**: Single-item purchase resource creation
