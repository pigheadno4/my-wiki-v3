# Fixed retrieval checks — Hosted Onboarding bank document

Q1. What is this source's purpose and scope, and what must not be inferred?
- Expected: A 2026-09-15 Adyen Hosted Onboarding page for uploading a bank document after automatic bank-account verification cannot complete. The notice says automated document checks were then available only in Australia, France, the UK and US, and may evolve. Fast document feedback is separate from final bank-account/legal-entity verification, capability enablement, current geographic availability, payout readiness or bank receipt. The page does not define API/onboarding-version or consent behavior beyond this hosted flow.
- Raw locators: `raw/adyen/docs/platforms/verification-requirements/upload-bank-document/2026-09-15.md:15-24`, `:57-79`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-platforms-verification-requirements-upload-bank-document.md` → `[[adyen-platforms]]`.

Q2. What upload criteria, exceptions and review warnings matter?
- Expected: The bank-account holder's name must match the legal-entity name on record; document needs account number/IBAN, recent issue date normally within 12 months with exceptions, and bank-issued evidence. PDF/JPEG/JPG/PNG, one file at a time, maximum 4 MB. Checks and deposits have extra criteria in the linked requirements guide; an online-banking screenshot need not show issue date but must show name/account/bank identity. A warning permits replacement or manual review through Use this document; accepted upload/Continue is not final verification. Reject altered, illegible, wrong-origin/type files; accepted Greek/Singapore document examples do not extend automated-check country availability.
- Raw locators: `raw/adyen/docs/platforms/verification-requirements/upload-bank-document/2026-09-15.md:26-55`, `:66-79`, `:88-129`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-platforms-verification-requirements-upload-bank-document.md` → `[[adyen-platforms]]`.
