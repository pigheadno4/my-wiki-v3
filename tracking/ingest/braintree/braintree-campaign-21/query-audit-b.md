# Braintree C21 fixed query audit — Group B

Analysis completed: `2026-09-29T14:51:48Z`
Scope: exactly four predetermined questions for Venmo and PayPal Credit. The two manifest-pinned raw pages were read completely; no claim below infers current support from the 2026-09-16 collection snapshot.

## Venmo

**Actual route:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-payment-methods.md` → `wiki/sources/braintree/source-braintree-payment-methods-venmo.md` → `raw/braintree/articles/guides/payment-methods/venmo-2026-09-16.md`

1. **Question:** Where is Braintree's Venmo payment-method guide?
   - **Object/action match:** Braintree's merchant-checkout Venmo payment-method guide; it is not a route for accepting payment inside the Venmo app, in-person collection, or Venmo peer-to-peer transfers.
   - **Direct answer:** The dedicated wiki source is `source-braintree-payment-methods-venmo`; it routes to the pinned raw guide whose canonical URL is `https://developer.paypal.com/braintree/articles/guides/payment-methods/venmo`.
   - **Exact raw locator:** source-URL metadata, line 1; `# Venmo`, lines 14-18; `## Availability`, lines 21-49.
   - **Verdict:** **PASS**

2. **Question:** What prerequisites, customer flow and limitations does this page itself state?
   - **Object/action match:** Prerequisites, checkout/vaulting customer flow, and limits stated by this Braintree Venmo merchant guide—not generic Venmo-app commerce or current compatibility.
   - **Direct answer:** The page limits the merchant product to certain business models: it excludes in-person goods/services, receiving payment for goods/services through the Venmo app, and Venmo-user P2P transactions. Otherwise the merchant must use a US business entity and a listed compatible SDK line (Android v5, iOS v6, or JavaScript v3). It gives customer minimums of Venmo app 9.1.0 for iOS apps, 9.13.0 for Android apps, 7.5.0 for iOS/Android mobile browsers, and 8.12.0 for desktop browsers, plus Android 6.0 or iOS 12.0 minimums on mobile. At merchant checkout, a customer pays from a Venmo account using a Venmo balance or saved payment method; vaulting the token supports later transactions without another Venmo-app authorization/app switch. Sandbox setup requires accepting Venmo's terms; production setup requires enabling Venmo and creating a Venmo Profile. The page permits voids and full or partial refunds but requires refunds within 180 days of the initial sale. These snapshot statements do not prove present availability, enablement, approval, or compatibility.
   - **Exact raw locator:** checkout and funding, lines 14-18; merchant availability, lines 21-49; customer versions/OS, lines 52-76; refunds/voids, lines 98-102; vaulting, lines 105-109; setup and production profile, lines 112-155.
   - **Verdict:** **PASS**

## PayPal Credit

**Actual route:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-payment-methods.md` → `wiki/sources/braintree/source-braintree-payment-methods-paypal-credit.md` → `raw/braintree/articles/guides/payment-methods/paypal-credit-2026-09-16.md`

3. **Question:** Where is PayPal Credit documented in Braintree?
   - **Object/action match:** Braintree's deprecated PayPal Credit credit-line guide; it is not the separate PayPal Pay Later offers guide or generic PayPal checkout documentation.
   - **Direct answer:** The dedicated wiki source is `source-braintree-payment-methods-paypal-credit`; it routes to the pinned raw guide whose canonical URL is `https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal-credit`. The raw page immediately marks itself deprecated and redirects readers to the separate Pay Later offers guide.
   - **Exact raw locator:** source-URL metadata, line 1; `# PayPal Credit` and opening `IMPORTANT`, lines 14-18.
   - **Verdict:** **PASS**

4. **Question:** What offer identity, eligibility and integration boundaries does this page itself state?
   - **Object/action match:** Identity, eligibility, customer flow, and setup boundaries for the deprecated PayPal Credit offering—not terms or availability for successor Pay Later offers.
   - **Direct answer:** The page calls PayPal Credit an instant, reusable credit line selected at checkout: customers may pay over time while the merchant receives 100% up front and pays the normal PayPal transaction fee. It states availability for merchants selling to US or UK customers, with USD only for US customers and GBP only for UK customers; UK merchants need FCA authorization and should check with Sales or an Account manager. The customer selects PayPal Credit, applies, accepts PayPal terms, and receives a credit decision, with use subject to credit approval. Easy Payments (US) and Instalments (UK) are separately named customizable PayPal Credit financing options that require contacting Braintree about pricing and qualifications. Enabling PayPal Credit requires changes to an existing PayPal setup, with full integration instructions delegated to developer docs. Most importantly, the page is deprecated and points to a separate Pay Later offers guide, so it is not evidence of current support or successor-offer terms.
   - **Exact raw locator:** deprecation redirect, lines 17-18; offer identity and merchant-funding statement, line 22; country/currency and UK FCA eligibility, lines 25-31; application and credit approval, lines 36-42; named financing options and qualification contact, lines 47-53; existing-PayPal-setup boundary, lines 58-60.
   - **Verdict:** **PASS**

## Shared gap sweep, extra reads, and link checks

- **Bounded filename/content sweep:** searched `raw/braintree/**/*.md` once for filenames containing `venmo`, `paypal-credit`, or `pay-later`, and for content containing the exact terms `Venmo`, `PayPal Credit`, or `Pay Later`. The sweep found the pinned articles plus distinct Pay Later, Venmo SDK/GraphQL, Venmo One Touch, reporting, and in-person QR material. None was needed to answer questions explicitly limited to what each pinned page itself states. The distinct hits do not broaden merchant-checkout Venmo into payment receipt through the Venmo app, and do not merge deprecated PayPal Credit into Pay Later.
- **Extra full reads:** none. Neither source page lists a related raw API reference; the two complete pinned raw reads answered all four fixed questions, and the sweep exposed no conflict that had to be resolved for these page-scoped answers.
- **Reciprocal/link checks:** `wiki/index.md` links to `braintree-index`; `wiki/braintree-index.md` links to `braintree-payment-methods` and both dedicated sources; the concept links to both sources; each source links back to the concept and to its exact pinned raw path. Both raw paths exist. Their SHA-256 values match the manifest (`58020f72...f3cb` for Venmo; `a4737a40...3b9c` for PayPal Credit).
