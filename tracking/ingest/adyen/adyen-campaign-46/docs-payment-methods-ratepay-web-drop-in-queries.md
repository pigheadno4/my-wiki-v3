# Fixed retrieval queries — Ratepay Web Drop-in

## Q1 — Identity and scope

**Query:** What does Adyen's Ratepay Web Drop-in guide cover, and what cannot be inferred from it?

**Expected:** This is the 2026-09-15-captured Ratepay Web Drop-in integration guide at `https://docs.adyen.com/payment-methods/ratepay/web-drop-in`. It adds Ratepay to an existing Web Drop-in and covers Open Invoice and Direct Debit, client/server request steps and subsequent results and modifications. It does not establish current merchant enablement, live eligibility, or actual payment success. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ratepay-web-drop-in.md` → `raw/adyen/docs/payment-methods/ratepay/web-drop-in/2026-09-15.md`. Evidence: raw `# Ratepay Drop-in integration` lines 15–33; `## Test and go live` lines 2449–2455.

## Q2 — Method differences and lifecycle

**Query:** What prerequisites, fields, and capture/refund rules does the Ratepay Web Drop-in guide give for Open Invoice versus Direct Debit, and are its Direct Debit examples internally consistent?

**Expected:** Existing Web Drop-in plus Ratepay in the test Customer Area; Web v6 import is at raw lines 35–41. `/paymentMethods` combinations AT/EUR, DE/EUR, NL/EUR (v3.22.1+), CH/CHF; Open Invoice `ratepay`, Direct Debit `ratepay_directdebit` (v5.13.0+), Direct Debit unavailable in CH (raw lines 43–61, 961–967). Both need shopper identity/contact, DOB, billing address, Ratepay fingerprint and `lineItems`; differing delivery address is conditional, and Direct Debit adds bank country, IBAN, owner (raw lines 21–25, 279–304, 968–979). The Direct Debit table says `ratepay_directdebit`, while its curl and repeated SDK examples use `ratepay` (raw lines 967, 1002–1004, 1317–1319); no corrected payload or runtime success is proven. An Authorised result still precedes shipment and capture; manual capture and invoice trigger apply specifically to Open Invoice. Partial capture needs amount and invoice line data; unused balance is manually cancelled; multiple partial captures need Support setup and yield separate invoices. Uncaptured payments can be cancelled, captured ones refunded; partial refund includes capture reference when multiple captures exist and invoice data for Open Invoice (raw lines 2311–2413). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ratepay-web-drop-in.md` → pinned raw.
