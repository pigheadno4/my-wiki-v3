# Clearpay Flutter Drop-in worker retrieval queries

## Q1 — Purpose and scope

**Query:** What does the Clearpay Flutter Drop-in guide add to an integration, and which server-side flows does it cover?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-clearpay-flutter-drop-in.md` → `raw/adyen/docs/payment-methods/clearpay/flutter-drop-in/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/clearpay/flutter-drop-in`; full pinned raw `raw/adyen/docs/payment-methods/clearpay/flutter-drop-in/2026-09-15.md`, `# Clearpay Flutter Drop-in` lines 15–23, `## Sessions flow Drop-in` lines 25–36, and `## Advanced flow Drop-in` lines 209–219. It adds Clearpay to existing Flutter Drop-in Sessions/Advanced flows. The Sessions requirement's base-guide link points to an Advanced URL despite its Sessions label; it does not change the section's flow identity. No current eligibility or execution proof follows.

## Q2 — Capability, prerequisites and warnings

**Query:** What request fields, redirect, capture/refund and discount conditions does the captured guide state?

**Expected route:** Same root → Adyen index → online-payments concept → Clearpay Flutter Drop-in source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path, Sessions request table lines 40–53, Advanced table/sample lines 229–255, redirect example lines 308–322, `## Capture the payment` lines 124–143, `## Refunds and cancellations` lines 145–154, `## Discounts` lines 156–190, and `## Test and go live` lines 192–207 (repeated for Advanced at 326–413). Preserve API v68+ for Sessions, redirect handling, shopper/address/item fields, 13-day production versus one-day test expiry, cancellation of an uncaptured payment, refund after capture, and conditional multiple partial captures. The Advanced example includes `paymentMethod.type: clearpay` although its table omits that row. The discount sample contains ellipsis and a missing comma, so it is illustrative rather than copy-ready JSON.
