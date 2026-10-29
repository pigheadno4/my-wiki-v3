# Q1 — Purpose, scope and non-inference

What does the captured Online banking Slovakia iOS Component page cover, and can its snippets be used as a complete iOS integration or proof of live acceptance?

Expected answer: At canonical https://docs.adyen.com/payment-methods/online-banking-slovakia/ios-component, the 2026-09-15-captured page is an iOS-titled method add-on with Sessions and Advanced Components sections (full pinned raw/adyen/docs/payment-methods/online-banking-slovakia/ios-component/2026-09-15.md, heading line 15 and lines 25–147). It is internally mixed: Android prerequisites/redirect links, a Kotlin configuration fragment and incomplete Swift initializers. It does not prove a complete valid iOS recipe, current merchant enablement, or a successful payment. The approved [[source-adyen-docs-payment-methods-online-banking-slovakia]] overview supplies dated SK/EUR and bank-redirect context (its pinned raw lines 23–31). Route [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-slovakia-ios-component]] → [[raw/adyen/docs/payment-methods/online-banking-slovakia/ios-component/2026-09-15]].

# Q2 — Request and platform/version warnings

Which Sessions and Advanced requirements and fields does this child state, and what source defects must qualify an iOS implementation answer?

Expected answer: Sessions requirements say existing Android Components Sessions, Checkout API v68+, redirect handling and Customer Area setup; no extra /sessions method parameters. The optional setConfig row and Kotlin sample use placeholder value, while the Swift OnlineBankingComponent initializer has blank configuration (raw lines 25–89). Advanced again says Android Components and redirect/Customer Area setup; its Checkout API minimum says only “v or later,” so no Advanced number is established. It says no extra method configuration, though the Swift initializer has a blank argument (raw lines 99–137). Advanced /payments marks paymentMethod.issuer required; the examples use onlineBanking_SK, issuer cs, EUR 1000 and an HTTPS returnUrl, all examples rather than an exhaustive bank list or iOS callback rule (raw lines 139–459). Both test/live sections say real details/small amounts, test Customer Area status and method addition for live acceptance (raw lines 91–97, 461–467). Do not silently transfer Android links/Kotlin, invent a valid setConfig value, or treat Sessions v68 as Advanced minimum. Route same root/provider/concept/source/raw chain and consult the iOS base guide plus active API/SDK contract.

Canonical URL stem: https://docs.adyen.com/payment-methods/online-banking-slovakia/ios-component
Full pinned raw path: raw/adyen/docs/payment-methods/online-banking-slovakia/ios-component/2026-09-15.md
