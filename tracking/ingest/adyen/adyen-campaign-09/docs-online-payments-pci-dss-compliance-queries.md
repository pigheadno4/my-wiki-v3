# Fixed retrieval checks: Adyen online-payments PCI DSS route

## Q1 — Purpose and scope

**Query:** What does this Adyen online-payments PCI DSS page establish about PCI DSS v4.0.1 and merchant responsibility?

**Expected answer:** It is a short guidance and navigation page for PCI DSS v4.0.1. It describes cardholder-data security scope and says PCI DSS applies to entities accepting credit cards or involved in payment processing. Merchants must meet the requirements applicable to their situation. The page routes to Adyen's fuller compliance guide for requirements and documentation; it does not assign an SAQ to any specific integration or prove merchant compliance.

**Raw locators:** title, scope and full-guide route, lines 15–21; responsibility, line 29; next-step routes, lines 31–43. **Canonical retrieval route:** [[adyen-pci-dss-compliance]] → [[source-adyen-docs-online-payments-pci-dss-compliance]] → [[raw/adyen/docs/online-payments/pci-dss-compliance/2026-09-15|pinned raw]].

## Q2 — Conditional ecommerce requirements

**Query:** What quarterly scanning and payment-page script-security conditions does this page describe, and can those statements be applied to every merchant?

**Expected answer:** For a merchant eligible to demonstrate compliance through SAQ A, the page says a quarterly vulnerability scan of part of the online-payments system is required in addition to SAQ A. If the merchant is not SAQ A eligible and certain conditions apply, it says measures are required against risks from scripts and iframe elements loaded on Web online-payment pages. Those are conditional statements in a dated Adyen snapshot, not a determination of a merchant's current SAQ, exact scope, or compliance status. Use the full guide and dedicated scanning and script-security routes for detail.

**Raw locators:** ecommerce conditions, lines 23–29; dedicated next steps, lines 31–43. **Canonical retrieval route:** [[adyen-pci-dss-compliance]] → [[source-adyen-docs-online-payments-pci-dss-compliance]] → [[raw/adyen/docs/online-payments/pci-dss-compliance/2026-09-15|pinned raw]].
