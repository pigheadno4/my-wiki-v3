# Fixed retrieval checks — Walley for Web

## Q1 — Purpose and limits

**Query:** What does the captured Walley Web page itself document, and does it establish current availability or a payment result?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-walley-web.md` → `raw/adyen/docs/payment-methods/walley/web/2026-09-15.md`.

**Answer:** It is a Web chooser for separate Walley Drop-in and Components child guides, plus general Web UI integration links. It does not state method-specific fields, eligibility, geography, B2C/B2B selection, authorization or capture behavior. Its captured links do not prove present merchant activation or an executed payment.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/walley/web`; full pinned raw `raw/adyen/docs/payment-methods/walley/web/2026-09-15.md`, `# Walley for Web` lines 15–17 and `## How do you want to integrate?` lines 19–29.

## Q2 — UI route choices

**Query:** Where does this page direct a website implementer for Walley Drop-in versus Components, and what base guides does it link?

**Expected route:** Same root → Adyen index → online-payments concept → Walley Web source → pinned raw.

**Answer:** The Drop-in child is the all-in-one website UI at `/payment-methods/walley/web-drop-in`; the Components child is a prebuilt Component at `/payment-methods/walley/web-component`. The final line links the general Web Drop-in and Components Sessions-flow guides. Follow the chosen child and base guide for behavior; this chooser does not supply an implementation recipe.

**Evidence locator:** Same canonical stem and full pinned raw path; child links at raw lines 21–27 and main integration links at line 29.
