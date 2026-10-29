# Fixed queries — Online banking Slovakia Android chooser

## Q1 — purpose, scope and limits

**Query:** What is the captured Online banking Slovakia Android page for, and what does it not establish?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/online-banking-slovakia/android` is a 2026-09-15-captured **navigation chooser** for Android Drop-in and Components child guides and main integration guides. It is not an API recipe or proof of current merchant eligibility, SDK minimum, redirect completion or successful payment. The method overview `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-slovakia.md` holds SK/EUR method-level context (full pinned `raw/adyen/docs/payment-methods/online-banking-slovakia/android/2026-09-15.md`, `# Online banking Slovakia for Android` lines 15–17; `### How do you want to integrate?` lines 19–27). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-slovakia-android.md`.

## Q2 — chooser routes and prerequisites

**Query:** Which Android implementation routes and base integration guides does the captured Slovakia page list?

**Expected answer:** Its chooser links **Drop-in** as the all-in-one Android UI path and **Components** via `OnlineBankingSKComponent`, described as handling the redirect (pinned `raw/adyen/docs/payment-methods/online-banking-slovakia/android/2026-09-15.md`, `### How do you want to integrate?` lines 19–27). It says to create the main integration first, then lists Android Drop-in and Components main guides under both **Sessions** and **Advanced** flows (`## See also` lines 29–36). These links are routes; they do not supply child-guide request fields or account entitlement. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-slovakia-android.md`.
