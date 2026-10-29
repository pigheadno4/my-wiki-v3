# IRIS overview retrieval checks

## Q1 — Purpose and limits

Query: What does Adyen's IRIS page cover, and can its mandatory-use statement or bank list be treated as current legal or merchant-eligibility proof?

Expected route: `wiki/index.md` PSP Indexes line 10 → `wiki/adyen-index.md` line 2610 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-iris.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/iris/2026-09-15.md` `# IRIS` lines 15–29. Expected answer: 2026-09-15-captured Greek-bank IRIS method overview; it states mandatory use for merchants with business in Greece, but that is a dated page assertion; its bank list is dated November 2025. Neither establishes current law or account enablement.

## Q2 — Gateway, onboarding and operations

Query: If a merchant integrates IRIS through Adyen, which party must they contract with and use for refunds, and what onboarding and payment-operation limits does the page describe?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-iris.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/iris/2026-09-15.md` lines 26–41 and `## How do you want to integrate?` lines 43–61. Expected answer: contract with a Greek IRIS acquiring bank; Adyen is gateway; bank handles refunds/cancellations because Adyen route does not support them. Bank/DIAS registration uses Annex A and five-digit Merchant Identifier, item 5 RI0; verify extra connectivity forms with bank. The GR/EUR Redirect matrix crosses recurring, Adyen-side refunds (including partial and multiple partial refunds), separate captures, partial captures, multiple partial captures, and chargebacks. It does not state that all captures are unsupported. Warning: do not read Adyen refund crosses as a ban on bank-side refunds or infer current live eligibility from chooser links.
