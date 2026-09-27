# Braintree C19 fixed retrieval audit — Group B

Overall verdict: **PASS (4/4)**. Both manifest SHA-256 pins match the current raw bytes. No repair is required.

## Actual routes

- **Try It Out:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-control-panel.md` → `wiki/sources/braintree/source-braintree-get-started-try-it-out.md` → `raw/braintree/articles/get-started/try-it-out-2026-09-16.md` (full read; SHA-256 `8265ce0b4aa927a816c31be621d4755b267385727ee79ce4694d969245d2cc50`, manifest match).
- **Get Paid:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-payment-platform.md` → `wiki/sources/braintree/source-braintree-get-started-get-paid.md` → `raw/braintree/articles/get-started/get-paid-2026-09-16.md` (full read; SHA-256 `5b144f044badbab170c53322f4160e876644ff63cb2e8d8003bc0b8002b3a3e2`, manifest match).

## Fixed questions

1. **Where is trying Braintree out documented? — PASS**
   - **Object/action match:** Yes — the route reaches the collected **Try It Out** page and its action of testing/exploring Braintree in Sandbox, not a product-specific go-live guide.
   - **Direct answer:** Follow the Try It Out route above. The page identifies the Braintree Sandbox as the test environment, says users can explore the gateway through the Sandbox Control Panel or API, and links to Sandbox signup.
   - **Exact raw locator:** `# Try It Out`, lines 14–16; `## The Braintree sandbox`, lines 19–23.

2. **Which trial, sandbox or production boundaries does this page itself document? — PASS**
   - **Object/action match:** Yes — this asks for the environment boundaries documented by this page itself, not proof of live acceptance.
   - **Direct answer:** Sandbox is “almost identical” to Production but uses test payment methods, test-value-triggered processor responses/webhooks, no dedicated capacity, broader deletion, standard displayed settings, simulated disputes, signup-country location, and a 100,000-active-subscription limit. Production uses real payment methods, bank responses and actual gateway events, dedicated capacity, account-qualified settings/disputes, business-registration location, and unlimited subscriptions. Sandbox options/currencies/features vary by country; Sandbox and Production are unlinked, nothing transfers, and credentials differ. The page only delegates Production integration once the merchant is ready to accept real payments; Sandbox activity is not Production acceptance proof.
   - **Exact raw locator:** `## Sandbox versus production`, lines 26–47; `## Testing currencies`, lines 52–71; `## Switching from sandbox to production`, lines 74–76.

3. **Where is the getting-paid starting guide? — PASS**
   - **Object/action match:** Yes — the route reaches **Get Paid**, whose starting object is an already-settled transaction and whose action is post-settlement funding, not payment acceptance or settlement submission.
   - **Direct answer:** Follow the Get Paid route above. The page begins after settlement and explains movement of funds through the merchant account to the application bank account.
   - **Exact raw locator:** `# Get Paid`, lines 14–18.

4. **What starting action and scope does it describe without implying settlement or funding proof? — PASS**
   - **Object/action match:** Yes — post-settlement funding guidance is kept distinct from accepting a payment, causing settlement, or proving a deposit.
   - **Direct answer:** After a transaction has settled, funds pass through the merchant account to the bank account provided during application; the merchant-account provider manages funding, with Braintree managing it for Braintree Direct. Method/account type controls timing. Credit cards are typically deposited 2–5 business days after settlement, subject to an international-merchant qualification. Aggregated Amex for most US merchants is Braintree-managed with an expected 2–5-business-day window; individual Amex is funded directly by Amex. PayPal disbursement is separate. These are general, qualified routes and timelines—not evidence that any transaction settled or any deposit arrived.
   - **Exact raw locator:** `# Get Paid`, lines 16–18; `## Credit cards`, line 23; `### American Express`, lines 28–30; `## PayPal`, lines 33–35.

## Shared checks

- **Bounded gap sweep:** Searched Braintree raw filenames and content for Sandbox/Production/testing/go-live and funding/disbursement/settlement terms, and inspected each source page's `Related raw API references`. Results included product-specific testing/go-live pages, processor/bank-specific settlement-funding pages, gateway-credential/user-role pages, and the PayPal funding guide. No extra full read was needed: the fixed questions ask what these two selected pages themselves document, both pinned raws answer directly, and adjacent pages would change the object or add delegated detail.
- **Reciprocal links:** PASS. `braintree-index` catalogs both sources; `braintree-control-panel` links to Try It Out and that source links back as its main concept; `braintree-payment-platform` links to Get Paid in its post-settlement section and that source links back as its main concept. Each source's `raw_files` entry and `Raw Sources` link point to its pinned raw.
- **Repair:** None.
