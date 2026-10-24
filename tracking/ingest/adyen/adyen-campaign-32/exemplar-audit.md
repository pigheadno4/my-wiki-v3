# Adyen C32 coordinator full-read exemplars

**PASS** — 2026-10-24. Three predetermined manifest samples, including the longest page. The coordinator independently read complete pinned content, then compared final promoted source entries and both query answers. Canonical catalog gaps are closed at campaign close.

| Pinned raw | Full lines | Result |
| --- | ---: | --- |
| `raw/adyen/docs/payment-methods/google-pay/2026-09-15.md` | 113 | PASS |
| `raw/adyen/docs/payment-methods/paypal/web-component/express-checkout/2026-09-15.md` | 1973 | PASS |
| `raw/adyen/docs/payment-methods/apple-pay/web-component/2026-09-15.md` | 505 | PASS |

Google Pay retains regional/local-entity network conditions, Interac authorization/capture statement without settlement proof, DPAN/FPAN and conditional 3DS/liability wording, Visa outside-EU/UK opt-in and additional-data condition, JCB omission versus mention, PCI Level 1 self-decryption boundary and navigation-only channel links. Final source and Q1/Q2 include the independently reviewed correction; no material final-sample failure.

PayPal Express raw was fully read in untruncated ranges 1–700, 701–1400 and 1401–1973. Final source and answers retain Web v5.59.0+, Sessions sessionId versus Advanced server pspReference, current paymentData replacement on every update, tax/delivery amount handling, initial address callback versus unchanged-amount statement, errors/rejections, Advanced-only review and delayed details submission, malformed details examples, recommended consent, zero-value/tokenize token exceptions and metadata/body chronology conflict. Code is illustrative; shopper/lightbox completion is not authorization/capture/settlement proof.

Apple Pay raw was read completely; a truncated long-table output was repaired with an untruncated 171–280 read before comparison. Final source and answers retain Sessions/Advanced roles and setup differences, Adyen/own-certificate merchant-validation split, availability before mounting, versioned browser/iframe and recurring gates, shopper authorization versus payment result, order-tracking callback/sample conflict and flow timing, capabilities and snippet limits, live domain/role/generic-method/firewall conditions. Routine tables remain at verified raw locators.

All three final comparisons pass; no expanded sample was triggered. Source facts remain historical snapshot statements. No provider, wallet, token, key, certificate or payment operation was performed.
