---
title: "Braintree Server SDK"
type: concept
category: technology
tags: [braintree, server-sdk, checkout, transactions, vault, subscriptions, webhooks]
---

## Braintree Server SDK

Braintree server SDKs connect a merchant backend to the Braintree Gateway. Client SDKs collect or approve a payment method and return a payment-method nonce or vaulted token; the server SDK uses that identifier for transaction, vault, subscription, and related gateway operations. A server SDK does not render checkout or establish that a payment method is enabled for a merchant or buyer.

## Shared Integration Model

The independently retained Node, PHP, and Ruby packages expose the same broad boundary through language-specific APIs:

- generate client tokens for browser or native SDK initialization;
- create and manage customers and vaulted payment methods;
- authorize transactions, submit them for settlement, partially settle, void, and refund;
- process PayPal and Venmo instruments returned by supported client integrations;
- create and manage plans and subscriptions; and
- verify and parse signed webhook notifications.

Exact methods, credential rules, transport behavior, supported runtime versions, and release changes remain package-qualified. Evidence from one language SDK must not be attributed to another without confirming it in that package's retained source.

## Checkout and Credential Boundary

Merchant backends must calculate trusted amounts and decide fulfillment from server-side state. A nonce is a short-lived processing input, while a vaulted token identifies a reusable payment method subject to product and merchant eligibility. Immediate settlement submission is optional; merchants can also authorize first and submit later.

Both retained SDKs support merchant API-key credentials and OAuth access tokens for ordinary gateway calls. The PHP implementation additionally makes the webhook boundary explicit: verification requires public/private API keys, so an access token alone is insufficient for webhook parsing.

## Versioned Evidence

- `braintree@3.39.0` at SHA `7a9270aaf31eb87819add64a768652243f90007c` is the retained Node.js baseline.
- `braintree_php@6.37.0` at SHA `0f53ece38397c9fed05b94620634a5a23ef8ee48` is the retained PHP baseline.
- `braintree@4.40.0` at SHA `1217992763cc13f33dbd8b6c51ad2ae058ddd2a8` is the retained Ruby baseline.

The Node and PHP baselines expose `preferredPaymentMethodToken` during client-token generation; the Ruby `4.40.0` client-token signature does not. All three warn that legacy Venmo SDK parameters are unsupported in favor of Pay with Venmo. This confirms the broad gateway contract while also demonstrating why optional fields must remain package-qualified. Current enablement and client experience still require client-SDK and product documentation evidence.

## Related

- [[source-braintree-settlement-batch-summary-generate-node]] - Node.js date-scoped settlement batch summary reporting with single-custom-field grouping examples and callback or Promise access to summary records

- [[source-braintree-merchant-account-create-node]] - Node.js merchant-account creation examples covering individual/business identity, bank-oriented funding, terms acceptance, master-merchant association, callback arguments and a Promise-resolved result value, without establishing universal onboarding eligibility

- [[source-braintree-merchant-account-find-node]] - Node.js single merchant-account lookup by ID through `gateway.merchantAccount.find()`, with callback arguments and separate response-object and not-found routes

- [[source-braintree-merchant-account-all-node]] - Node.js merchant-account collection retrieval through `gateway.merchantAccount.all()`, with callback `forEach` consumption and displayed `currencyIsoCode` access, without importing account-creation or update behavior

- [[source-braintree-merchant-account-update-node]] - Node.js merchant-account update example using an account identifier, an individual first-name change and a `result.success` callback check, with a separate not-found route and no inferred wider update effects

- [[source-braintree-merchant-account-create-for-currency-node]] - Braintree Node.js currency-specific merchant-account creation for Braintree Auth merchants, with callback and Promise result handling plus unsupported-currency validation routes

- [[source-braintree-document-upload-create-node]] - Node.js document-upload creation with an `EvidenceDocument` kind and file-stream example, preserving the displayed result-variable mismatch and no inference that upload creation submits dispute evidence

- [[source-braintree-credit-card-verification-search-node]] - Node.js credit-card-verification search by verification, customer, card, payment-method, billing-address or creation-time criteria, with callback iteration, qualified timezone behavior and a preserved policy-based result-limitation notice

- [[source-braintree-search-results-node]] - Node.js search-result consumption through version-qualified no-callback object-mode streams or callback-provided `each` iteration, with lazy-fetch race behavior, maximum-count guidance and transaction-versus-other-search caps

- [[source-braintree-customer-search-node]] - Node.js customer search through `gateway.customer.search()`, with callback `response.each()` consumption, raw routes for filter examples and operator restrictions, the preserved results-limitation notice, and the unavailable all-customers Node call

- [[source-braintree-search-fields-node]] - Node.js search-field categories and operators, including the 255-character text limit and distinct non-time versus time-range boundary semantics

- [[source-braintree-address-find-node]] - Node.js lookup of one address by customer ID plus address ID, with `err`/`address` callback evidence, separate response-object navigation, and a shared customer-or-address not-found route

- [[source-braintree-payment-method-revoke-node]] - limited-release Node.js revocation of a payment-method grant, deleting the granted version from the receiving merchant's Vault without importing the separate payment-method deletion cascade

- [[source-braintree-payment-method-update-node]] - Node.js stored-payment-method updates by token, including shared or replacement billing-address behavior, PayPal/default-method restrictions, card verification with the AVS-update transaction/CVV rejection condition, and nonce-association and precedence rules

- [[source-braintree-payment-method-grant-node]] - limited-release Node.js Grant API route for giving another Braintree merchant controlled access to one customer payment method through a recipient access token and returned nonce

- [[source-braintree-subscription-retry-charge-node]] - Node.js manual retry of a past-due subscription charge, with the explicit example amount, displayed success access, and separate transaction-settlement submission route

- [[source-braintree-subscription-search-node]] - Node.js subscription search through `gateway.subscription.search()`, with callback and stream result consumption, qualified filter-example routes, the preserved results-limitation policy notice, and no reconstructed SDK version from the damaged rendering

- [[source-braintree-payment-method-create-node]] - Node.js existing-customer payment-method creation with required customer ID and nonce, default and billing-address behavior, payment-type limits on duplicate rejection, card-verification and Premium Fraud Management Tools guidance, and nonce-versus-raw-card precedence

- [[source-braintree-discount-all-node]] - Node.js `gateway.discount.all()` collection retrieval in callback form, with returned items accessed through `result.discounts`; the page does not establish discount creation or application behavior, and its recurring-billing See Also route is Ruby documentation

- [[source-braintree-add-on-all-node]] - Node.js `gateway.addOn.all()` collection retrieval in callback and Promise forms, with returned items accessed through `result.addOns`; linked response and recurring-billing references are Ruby routes, and the page does not establish add-on creation or application behavior

- [[source-braintree-plan-create-node]] - Node.js `gateway.plan.create()` reference with the merchant recurring-billing enablement prerequisite, required-input examples, and two add-on/discount creation routes; it does not establish subscription creation or effects on existing subscriptions

- [[source-braintree-plan-find-node]] - Node.js single-plan ID lookup through `gateway.plan.find()` in callback and Promise forms, with the missing-plan error route and no inferred result fields

- [[source-braintree-plan-update-node]] - Node.js plan updates by ID, including the destructive modification-token omission warning, add-on/discount add-update-remove routes, qualified override details, and the trial-period billing-day effect, without establishing propagation to existing subscriptions

- [[source-braintree-credit-card-delete-node]] - Node.js token-based credit-card deletion through `gateway.creditCard.delete()`, with an error-only callback and Braintree's qualified PCI SAQ D warning plus recommended payment-method alternative

- [[source-braintree-credit-card-find-node]] - Node.js token-based credit-card lookup through `gateway.creditCard.find()`, with callback arguments and Braintree's qualified PCI SAQ D warning plus recommended payment-method alternative

- [[source-braintree-credit-card-expiring-between-node]] - Node.js credit-card date-range retrieval through `gateway.creditCard.expiringBetween()`, with callback and incomplete stream examples plus unspecified boundary and timezone semantics

- [[source-braintree-credit-card-update-node]] - Node.js stored-credit-card update by token, with the qualified PCI SAQ D advisory, conditional card-verification scope, callback example, and nonce-versus-raw-card recommendation and precedence

- [[source-braintree-credit-card-create-node]] - Node.js `creditCard.create()` reference with a raw-card callback example, the qualified PCI SAQ D advisory and payment-method recommendation, and nonce-versus-raw-card precedence guidance

- [[source-braintree-plan-all-node]] - Node.js retrieval of the Plan-object collection through `gateway.plan.all()` in callback and Promise forms, without plan-creation, subscription-behavior, or enablement claims

- [[source-braintree-address-delete-node]] - Node.js customer-address deletion by customer ID plus address ID, including removal of that address from billing or shipping references on Vault payment methods and the not-found error route

- [[source-braintree-address-create-node]] - Node.js Vault address creation with required customer association, gateway-generated customer-scoped address IDs, the 50-address-per-customer limit, callback example, and not-found error route

- [[source-braintree-address-update-node]] - Node.js customer-scoped Vault address update using customer and address IDs, callback `err`/`result` handling, alternative customer/payment-method update routes, and the missing-address or missing-customer error route

- [[source-braintree-subscription-find-node]] - Node.js single-subscription ID lookup through callback or Promise, with preserved incomplete-prose and results-limitation boundaries plus the missing-subscription error route

- [[source-braintree-subscription-cancel-node]] - Node.js subscription cancellation by ID, including its stated credit-card billing effect, callback and Promise forms, missing-subscription error route, and edit/reactivation limit

- [[source-braintree-customer-update-node]] - Node.js customer updates with unchanged omitted attributes, existing-credit-card versus new-payment-method behavior, billing-address update semantics, default-payment-method selection, verification qualifications, and a retained missing non-card update route

- [[source-braintree-transaction-find-node]] - Node.js transaction-ID lookup through callback or Promise, preserved results-limitation policy notice, missing-transaction error route, and Braintree Marketplace-specific escrow-status example

- [[source-braintree-customer-find-node]] - Node.js single-customer lookup by customer ID, with an explicit evidence gap because the collected Node code block contains no usable invocation example

- [[source-braintree-customer-delete-node]] - Node.js customer deletion by customer ID, with cascading deletion of all associated payment methods and cancellation of all associated recurring billing subscriptions

- [[source-braintree-customer-create-node]] - Node.js customer creation alone or with payment-method and billing-address variants, optional case-insensitive merchant customer IDs, validation and card-verification qualifications, Control Panel-configured custom fields, and retained collected-document gaps

- [[source-braintree-payment-method-find-node]] - Node.js stored payment-method token lookup, preserved results-limitation policy notice, separate PayPal-account callback and Promise examples, and the PayPal-account not-found route

- [[source-braintree-payment-method-nonce-create-node]] - Node.js server-side payment-method nonce creation from a payment-method token, with Braintree's guidance that merchants should only create these nonces server-side for 3D Secure or Checkout with PayPal, plus the missing-payment-method error route

- [[source-braintree-payment-method-delete-node]] - Node.js token-based payment-method deletion, with immediate cancellation of every associated subscription and forfeiture of already-paid remaining days

- [[source-braintree-payment-method-nonce-find-node]] - Node.js non-consuming nonce lookup, returned 3D Secure information, server-side pre-transaction risk-check scope, and missing-nonce error route

- [[source-braintree-transaction-void-node]] - Node.js `transaction.void()` reference for `authorized` and `submitted for settlement` transactions, the cross-document warning that only certain PayPal `settlement pending` transactions are eligible (identified elsewhere as multiple partial settlements), and the if-possible authorization-reversal effect

- [[source-braintree-client-token-generate-node]] - Node.js `clientToken.generate()` reference, including response-token extraction and the customer-ID variant for returning-customer Drop-in saved-payment presentation

- [[source-braintree-transaction-submit-for-settlement-node]] - Node.js `transaction.submitForSettlement()` reference for explicit settlement submission, settlement-amount changes, select-merchant and processor authorization adjustments, and approval-gated Level 2/3 or shipping data at submission

- [[source-braintree-payment-method-nonces]] - Braintree SDK nonce and GraphQL single-use payment-method naming, client/server use routes, and the one-use plus three-hour unused-token lifespan

- [[source-braintree-transaction-refund-node]] - Node.js `transaction.refund()` reference for eligible transaction states, omitted-amount behavior, partial and escrow limits, and processor-decline versus settlement-failure routes

- [[source-braintree-transaction-sale-node]] - current Node.js `transaction.sale()` request guide for payment-source selection, immediate settlement submission, conditional vault storage, risk/fraud supporting-data prerequisites, merchant-account routing, descriptor constraints, and Marketplace escrow

- [[source-braintree-get-started]] - provider guide to the client-token initialization, client-side payment-method nonce, front-end-to-server nonce handoff, and server-side transaction-creation sequence

- [[source-github-braintree-node]] - Node.js server SDK implementation evidence
- [[changelog-github-braintree-node]] - Node.js package release ledger
- [[source-github-braintree-php]] - PHP server SDK implementation evidence
- [[changelog-github-braintree-php]] - PHP package release ledger
- [[source-github-braintree-ruby]] - Ruby server SDK implementation evidence
- [[changelog-github-braintree-ruby]] - Ruby package release ledger
- [[braintree-web-sdk]] - browser tokenization and nonce handoff
- [[braintree-android-sdk]] - native Android nonce handoff
- [[braintree-ios-sdk]] - native iOS nonce handoff
- [[paypal-braintree-integration]] - PayPal client approval and Braintree processing boundary
