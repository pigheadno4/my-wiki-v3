# Fixed retrieval checks: docs-platforms-in-person-payments-surcharge

## Q1 — Purpose, scope and compliance boundary

**Query:** What does the Adyen for Platforms in-person surcharge guide cover, where is the surcharge booked, and which restrictions should a platform check before use?

**Expected answer:** The 2023-modified, 2026-09-15-captured guide covers passing payment-acceptance costs to a customer on in-person payments and booking the surcharge amount. The platform needs agreements with users on acceptance-fee charging. The surcharge books to the platform liable balance account by default; split instructions can send it to a user's balance account. The page's dated availability list is Australia, Canada, Europe, Great Britain, New Zealand and the US, subject to integration/hardware method limits and current eligibility. The platform must validate legal, regional and card-scheme requirements; Adyen does not automate global compliance. The page gives EEA-issued consumer cards in the EEA and US debit cards as disallowed examples. It bars surcharge on authorization adjustments or overcaptures because the amount cannot exceed what was shown at sale. Mobile lacks the Adyen confirmation screen in this snapshot, but customer disclosure remains required. Do not infer merchant of record, legal ownership, current account eligibility or completed funds movement.

**Evidence locators:** `raw/adyen/docs/platforms/in-person-payments/surcharge/2026-09-15.md:15-50`, `:77-97`. **Canonical route:** `[[adyen]]` → `[[adyen-platforms]]` → `[[source-adyen-docs-platforms-in-person-payments-surcharge]]` → pinned raw.

## Q2 — Method choice, precedence, DCC and reconciliation

**Query:** How do configured and dynamic surcharges interact, what are the terminal/DCC limits, and how should actual surcharge credit be tracked?

**Expected answer:** Configuration-based surcharge uses rules on payment attributes and applies an amount automatically. Dynamic surcharge uses platform or third-party calculation, optionally with card acquisition, and sends the amount in the payment request. Standalone terminals support configured surcharges only. Both methods can coexist, and a request-supplied surcharge amount overrides configuration, including an intended zero amount. DCC and a surcharge cannot both apply to one transaction: below terminal v1.112 the guide recommends avoiding both configurations on one terminal; at v1.112+ it says DCC is skipped for a positive surcharge. With extra surcharge data enabled, AUTHORISATION webhooks include `extraCostsCurrency` and minor-unit `extraCostsValueSurcharge`. For fund tracking, match each surcharge split's actual incoming transfer-created/updated states with its booked transaction, then reconcile the recommended PAR/SDR Surcharge Amount column and BPAR/BPSR surcharge lines. The page says a Surcharge split in a payment request or split configuration generates a separate incoming transfer. A test AUTHORISATION event or received/authorised transfer is not proof of booked credit, payout or bank receipt.

**Evidence locators:** `raw/adyen/docs/platforms/in-person-payments/surcharge/2026-09-15.md:54-75`, `:99-120`, `:161-186`, `:189-191`, `:259-261`, `:343-345`, `:444-489`, `:491-501`. **Canonical route:** `[[adyen]]` → `[[adyen-platforms]]` → `[[source-adyen-docs-platforms-in-person-payments-surcharge]]` → pinned raw.
