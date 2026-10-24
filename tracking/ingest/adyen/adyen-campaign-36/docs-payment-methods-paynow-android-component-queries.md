# docs-payment-methods-paynow-android-component — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is a PayNow-specific **Android Components** add-on for existing Sessions and Advanced integrations (source-adyen-docs-payment-methods-paynow-android-component; raw lines 15–25, 137–145). It gives `InstantPaymentComponent` setup and an Advanced `qrCode` action prerequisite, but no QR expiry, scan-to-webhook lifecycle, completed-payment response or current merchant eligibility proof (raw lines 43–125, 137–247). A displayed or scanned code alone cannot establish an authorized or settled bank payment.

Q2. What are its central capability, prerequisites and warnings?

Sessions requires Checkout API v68+, PayNow added in Customer Area, and an existing Android Components integration; no extra PayNow `/sessions` parameters or Component configuration are specified (raw lines 29–41, 66–76). Advanced requires the existing Android Components flow and `action.type: qrCode` handling; the page shows `paynow` selection and says no additional PayNow configuration or ordinary `/payments` fields (raw lines 139–145, 170–180, 189–237). Compose uses `instant` plus `components-compose` and a per-screen/session reset key, but `YOUR_VERSION` supplies no SDK minimum (raw lines 49–64, 90–99, 153–168, 195–204). Live acceptance needs Support addition in live Customer Area, while the page warns against test Customer Area payments because bank transfers there are not reversible and bank funds are deducted; its live penny-test text is source guidance, not an instruction to execute a financial operation (raw lines 127–135, 239–247).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paynow-android-component]] → [[raw/adyen/docs/payment-methods/paynow/android-component/2026-09-15]].
