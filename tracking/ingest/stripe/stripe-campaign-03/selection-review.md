# Stripe S03 proposed 100-page review

**PREPARED ONLY — exact-scope and provider-contract approval pending.**

S02 was committed and verified on origin/main as `8c514ce6ea1f6dd5e8ab9ddde9a9e3073d747864`. This next round selects 100 disjoint raw URL identities in canonical URL order, from `https://docs.stripe.com/payments/advanced/discounts` through `https://docs.stripe.com/payments/konbini`. All are in Payments.

The 100 comparisons map to **101 existing source summaries**. One dynamic line-items raw comparison maps to two summaries; both must be fully read and independently reviewed. This is 100 raw pages, not 101 raw pages, and no source updates are pre-authorized.

Queue accounting: 512 original changed identities minus 150 already reviewed in S01/S02 = **362 currently unreviewed**. If this proposed review completes, **262** remain. All **4,265 new candidates** remain deferred. These figures describe review coverage, not pages already ingested.

Full-read workload: 99,233 new words / 14,263 lines and 396,042 old words / 70,130 lines, plus all 101 current summaries and full diffs. Metadata counts do not establish semantic changes.

Proposed controls: ten shared rolling child slots across workers/reviewers/auditors; gpt-6-sol medium workers and different gpt-6-sol high first reviewers; complete numbered old/new/source/diff reads, 3–5 new quotes and located old evidence; 200 actual fixed answers; at most three attempts; coordinator-only tracking writes. Canonical updates require a later exact proposal and approval.

Fixed coordinator audits: standard `payments-jp-installments`, largest new raw `payments-klarna`, ordinary sample `payments-advanced-discounts`. Any material partial/fail expands audits to all100.

The two-summary unit must use five pinned files and per-source findings; activation must adapt the single-source S02 runtime before dispatch. No runtime, semantic review, collection, raw modification, canonical edits or S03 publication has started.

Source-before pin refreshes from the original queue: 0. Activation must revalidate all raw/old/diff/source and aggregate pins. Historical count/catalog repair and the S02 outside-scope counterpart remain separate.

Review [proposal](proposal.json), [exact manifest](manifest.proposed.json), [provider contract](dispatch-contract.proposed.md), [fixed queries](proposed-queries.md), [activation context](activation-context.proposed.json) and [preflight](preflight-validation.json).

| # | Canonical URL | New words | Old words | Existing summaries |
|---|---|---:|---:|---|
| 1 | https://docs.stripe.com/payments/advanced/discounts | 1359 | 1425 | wiki/sources/source-stripe-checkout-add-discounts.md |
| 2 | https://docs.stripe.com/payments/advanced/dynamically-update-amounts | 61 | 924 | wiki/sources/source-stripe-checkout-dynamic-amounts.md |
| 3 | https://docs.stripe.com/payments/advanced/tax | 63 | 13360 | wiki/sources/source-stripe-checkout-collect-taxes.md |
| 4 | https://docs.stripe.com/payments/affirm | 3491 | 2245 | wiki/sources/source-stripe-affirm.md |
| 5 | https://docs.stripe.com/payments/affirm/accept-a-payment | 74 | 8909 | wiki/sources/source-stripe-affirm-accept-payment.md |
| 6 | https://docs.stripe.com/payments/afterpay-clearpay | 2271 | 1513 | wiki/sources/source-stripe-afterpay-clearpay.md |
| 7 | https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment | 89 | 15447 | wiki/sources/source-stripe-afterpay-clearpay-accept-payment.md |
| 8 | https://docs.stripe.com/payments/afterpay-clearpay/site-messaging | 744 | 726 | wiki/sources/source-stripe-afterpay-clearpay-messaging.md |
| 9 | https://docs.stripe.com/payments/alipay | 1614 | 915 | wiki/sources/source-stripe-alipay.md |
| 10 | https://docs.stripe.com/payments/alipay/accept-a-payment | 68 | 6022 | wiki/sources/source-stripe-alipay-accept-payment.md |
| 11 | https://docs.stripe.com/payments/alma | 6393 | 1299 | wiki/sources/source-stripe-alma.md |
| 12 | https://docs.stripe.com/payments/alma/accept-a-payment | 63 | 7844 | wiki/sources/source-stripe-alma-accept-payment.md |
| 13 | https://docs.stripe.com/payments/amazon-pay | 1424 | 968 | wiki/sources/source-stripe-amazon-pay.md |
| 14 | https://docs.stripe.com/payments/amazon-pay/accept-a-payment | 65 | 7510 | wiki/sources/source-stripe-amazon-pay-accept-payment.md |
| 15 | https://docs.stripe.com/payments/amazon-pay/set-up-future-payments | 65 | 5813 | wiki/sources/source-stripe-amazon-pay-set-up-future-payments.md |
| 16 | https://docs.stripe.com/payments/analytics/optimization | 1874 | 1872 | wiki/sources/source-stripe-payments-optimization.md |
| 17 | https://docs.stripe.com/payments/analytics/recommendations | 1013 | 1010 | wiki/sources/source-stripe-payments-recommendations.md |
| 18 | https://docs.stripe.com/payments/au-becs-debit | 2253 | 1967 | wiki/sources/source-stripe-au-becs-debit.md |
| 19 | https://docs.stripe.com/payments/au-becs-debit/accept-a-payment | 72 | 13577 | wiki/sources/source-stripe-au-becs-accept-payment.md |
| 20 | https://docs.stripe.com/payments/au-becs-debit/set-up-payment | 76 | 9707 | wiki/sources/source-stripe-au-becs-set-up-payment.md |
| 21 | https://docs.stripe.com/payments/bacs-debit | 3389 | 2036 | wiki/sources/source-stripe-bacs-direct-debit.md |
| 22 | https://docs.stripe.com/payments/bacs-debit/accept-a-payment | 56 | 7034 | wiki/sources/source-stripe-bacs-accept-payment.md |
| 23 | https://docs.stripe.com/payments/bancontact | 1012 | 523 | wiki/sources/source-stripe-bancontact.md |
| 24 | https://docs.stripe.com/payments/bancontact/accept-a-payment | 65 | 6620 | wiki/sources/source-stripe-bancontact-accept-payment.md |
| 25 | https://docs.stripe.com/payments/bank-debits | 945 | 940 | wiki/sources/source-stripe-bank-debits.md |
| 26 | https://docs.stripe.com/payments/bank-redirects | 832 | 864 | wiki/sources/source-stripe-bank-redirects.md |
| 27 | https://docs.stripe.com/payments/bank-transfers | 2287 | 2063 | wiki/sources/source-stripe-bank-transfers.md |
| 28 | https://docs.stripe.com/payments/bank-transfers/accept-a-payment | 68 | 11478 | wiki/sources/source-stripe-bank-transfers-accept-payment.md |
| 29 | https://docs.stripe.com/payments/billie | 1518 | 1052 | wiki/sources/source-stripe-billie.md |
| 30 | https://docs.stripe.com/payments/billie/accept-a-payment | 71 | 9827 | wiki/sources/source-stripe-billie-accept-payment.md |
| 31 | https://docs.stripe.com/payments/bizum | 1238 | 1053 | wiki/sources/source-stripe-bizum.md |
| 32 | https://docs.stripe.com/payments/bizum/accept-a-payment | 65 | 9385 | wiki/sources/source-stripe-bizum-accept-payment.md |
| 33 | https://docs.stripe.com/payments/blik | 1545 | 854 | wiki/sources/source-stripe-blik.md |
| 34 | https://docs.stripe.com/payments/blik/accept-a-payment | 60 | 6560 | wiki/sources/source-stripe-blik-accept-payment.md |
| 35 | https://docs.stripe.com/payments/blik/save-during-payment | 63 | 4975 | wiki/sources/source-stripe-blik-save-during-payment.md |
| 36 | https://docs.stripe.com/payments/blik/set-up-payment | 63 | 3642 | wiki/sources/source-stripe-blik-set-up-payment.md |
| 37 | https://docs.stripe.com/payments/boleto | 739 | 421 | wiki/sources/source-stripe-boleto.md |
| 38 | https://docs.stripe.com/payments/boleto/accept-a-payment | 64 | 8101 | wiki/sources/source-stripe-boleto-accept-payment.md |
| 39 | https://docs.stripe.com/payments/boleto/set-up-invoices | 3040 | 3061 | wiki/sources/source-stripe-boleto-invoices.md |
| 40 | https://docs.stripe.com/payments/boleto/set-up-subscription | 2772 | 2741 | wiki/sources/source-stripe-boleto-subscription.md |
| 41 | https://docs.stripe.com/payments/build-a-two-step-confirmation | 4535 | 4569 | wiki/sources/source-stripe-two-step-confirmation.md |
| 42 | https://docs.stripe.com/payments/buy-now-pay-later | 1493 | 1480 | wiki/sources/source-stripe-bnpl-overview.md |
| 43 | https://docs.stripe.com/payments/cards | 1405 | 1351 | wiki/sources/source-stripe-cards.md |
| 44 | https://docs.stripe.com/payments/cards/overview | 620 | 650 | wiki/sources/source-stripe-how-cards-work.md |
| 45 | https://docs.stripe.com/payments/cards/surcharge | 1730 | 1858 | wiki/sources/source-stripe-surcharge.md |
| 46 | https://docs.stripe.com/payments/cartes-bancaires | 53 | 489 | wiki/sources/source-stripe-cartes-bancaires.md |
| 47 | https://docs.stripe.com/payments/cash-app-pay | 2468 | 1780 | wiki/sources/source-stripe-cash-app-pay.md |
| 48 | https://docs.stripe.com/payments/cash-app-pay/accept-a-payment | 73 | 14182 | wiki/sources/source-stripe-cash-app-pay-accept-payment.md |
| 49 | https://docs.stripe.com/payments/cash-app-pay/set-up-payment | 67 | 5128 | wiki/sources/source-stripe-cash-app-pay-set-up-payment.md |
| 50 | https://docs.stripe.com/payments/charges-api | 1214 | 1315 | wiki/sources/source-stripe-legacy-apis.md |
| 51 | https://docs.stripe.com/payments/checkout-sessions | 494 | 507 | wiki/sources/source-stripe-checkout-sessions.md |
| 52 | https://docs.stripe.com/payments/checkout/adjustable-quantity | 58 | 712 | wiki/sources/source-stripe-checkout-adjustable-quantities.md |
| 53 | https://docs.stripe.com/payments/checkout/custom-shipping-options | 55 | 1350 | wiki/sources/source-stripe-checkout-dynamic-shipping.md |
| 54 | https://docs.stripe.com/payments/checkout/customization/appearance | 53 | 1742 | wiki/sources/source-stripe-checkout-appearance.md |
| 55 | https://docs.stripe.com/payments/checkout/customization/card-brands | 57 | 542 | wiki/sources/source-stripe-checkout-card-brands.md |
| 56 | https://docs.stripe.com/payments/checkout/customization/product-images | 55 | 780 | wiki/sources/source-stripe-checkout-product-images.md |
| 57 | https://docs.stripe.com/payments/checkout/dynamically-update-line-items | 56 | 1194 | wiki/sources/source-stripe-checkout-custom-shipping-options.md, wiki/sources/source-stripe-checkout-dynamic-line-items.md |
| 58 | https://docs.stripe.com/payments/checkout/how-checkout-works | 63 | 2935 | wiki/sources/source-stripe-how-checkout-works.md |
| 59 | https://docs.stripe.com/payments/checkout/pricing-table | 2439 | 2497 | wiki/sources/source-stripe-pricing-table.md |
| 60 | https://docs.stripe.com/payments/checkout/update-customer | 137 | 83 | wiki/sources/source-stripe-checkout-update-customer.md |
| 61 | https://docs.stripe.com/payments/countries/korea | 1310 | 1241 | wiki/sources/source-stripe-korea-payment-methods.md |
| 62 | https://docs.stripe.com/payments/countries/nigeria | 641 | 600 | wiki/sources/source-stripe-nigeria-payment-methods.md |
| 63 | https://docs.stripe.com/payments/custom/localize-prices/adaptive-pricing | 2191 | 2045 | wiki/sources/source-stripe-adaptive-pricing-elements.md |
| 64 | https://docs.stripe.com/payments/custom/localize-prices/fx-quotes-api | 2063 | 1840 | wiki/sources/source-stripe-fx-quotes-api.md |
| 65 | https://docs.stripe.com/payments/custom/localize-prices/manual-currency-prices | 796 | 871 | wiki/sources/source-stripe-manual-currency-prices.md |
| 66 | https://docs.stripe.com/payments/customer-balance | 1073 | 1049 | wiki/sources/source-stripe-customer-balance.md |
| 67 | https://docs.stripe.com/payments/customer-balance/funding-instructions | 1929 | 2116 | wiki/sources/source-stripe-customer-balance-funding-instructions.md |
| 68 | https://docs.stripe.com/payments/customer-balance/reconciliation | 1933 | 2922 | wiki/sources/source-stripe-customer-balance-reconciliation.md |
| 69 | https://docs.stripe.com/payments/customer-balance/refunding | 1760 | 1838 | wiki/sources/source-stripe-bank-transfers-refunds.md |
| 70 | https://docs.stripe.com/payments/customize-payment-methods | 763 | 418 | wiki/sources/source-stripe-payment-element-customize-payment-methods.md |
| 71 | https://docs.stripe.com/payments/eftpos-australia | 1019 | 665 | wiki/sources/source-stripe-eftpos-australia.md |
| 72 | https://docs.stripe.com/payments/eps | 953 | 476 | wiki/sources/source-stripe-eps.md |
| 73 | https://docs.stripe.com/payments/eps/accept-a-payment | 64 | 7420 | wiki/sources/source-stripe-eps-accept-payment.md |
| 74 | https://docs.stripe.com/payments/existing-customers | 68 | 8170 | wiki/sources/source-stripe-payments-existing-customers.md |
| 75 | https://docs.stripe.com/payments/extended-authorization | 73 | 4419 | wiki/sources/source-stripe-extended-authorization.md |
| 76 | https://docs.stripe.com/payments/finalize-payments-on-the-server | 78 | 13519 | wiki/sources/source-stripe-finalize-payments-server.md |
| 77 | https://docs.stripe.com/payments/flexible-features-migration | 63 | 2101 | wiki/sources/source-stripe-flexible-features-migration.md |
| 78 | https://docs.stripe.com/payments/forwarding-third-party-processors | 1003 | 936 | wiki/sources/source-stripe-forwarding-third-party.md |
| 79 | https://docs.stripe.com/payments/forwarding-token-vault | 951 | 892 | wiki/sources/source-stripe-forwarding-token-vault.md |
| 80 | https://docs.stripe.com/payments/fpx | 994 | 578 | wiki/sources/source-stripe-fpx.md |
| 81 | https://docs.stripe.com/payments/fpx/accept-a-payment | 57 | 3349 | wiki/sources/source-stripe-fpx-accept-payment.md |
| 82 | https://docs.stripe.com/payments/grabpay | 846 | 483 | wiki/sources/source-stripe-grabpay.md |
| 83 | https://docs.stripe.com/payments/grabpay/accept-a-payment | 66 | 5702 | wiki/sources/source-stripe-grabpay-accept-payment.md |
| 84 | https://docs.stripe.com/payments/ideal | 821 | 688 | wiki/sources/source-stripe-ideal.md |
| 85 | https://docs.stripe.com/payments/ideal/accept-a-payment | 77 | 7894 | wiki/sources/source-stripe-ideal-accept-payment.md |
| 86 | https://docs.stripe.com/payments/ideal/save-during-payment | 71 | 11953 | wiki/sources/source-stripe-ideal-save-during-payment.md |
| 87 | https://docs.stripe.com/payments/ideal/set-up-payment | 82 | 11344 | wiki/sources/source-stripe-ideal-set-up-payment.md |
| 88 | https://docs.stripe.com/payments/incremental-authorization | 61 | 6956 | wiki/sources/source-stripe-incremental-authorization.md |
| 89 | https://docs.stripe.com/payments/jp-installments | 679 | 674 | wiki/sources/source-stripe-jp-installments.md |
| 90 | https://docs.stripe.com/payments/jp-installments/accept-a-payment | 67 | 3256 | wiki/sources/source-stripe-jp-installments-accept-payment.md |
| 91 | https://docs.stripe.com/payments/kakao-pay/accept-a-payment | 59 | 1824 | wiki/sources/source-stripe-kakao-pay-accept-payment.md |
| 92 | https://docs.stripe.com/payments/kakao-pay/set-up-future-payments | 59 | 3002 | wiki/sources/source-stripe-kakao-pay-set-up-future-payments.md |
| 93 | https://docs.stripe.com/payments/klarna | 6487 | 1804 | wiki/sources/source-stripe-klarna.md |
| 94 | https://docs.stripe.com/payments/klarna/accept-a-payment | 69 | 22549 | wiki/sources/source-stripe-klarna-accept-payment.md |
| 95 | https://docs.stripe.com/payments/klarna/best-practices | 343 | 338 | wiki/sources/source-stripe-klarna-best-practices.md |
| 96 | https://docs.stripe.com/payments/klarna/compliance | 710 | 566 | wiki/sources/source-stripe-klarna-compliance.md |
| 97 | https://docs.stripe.com/payments/klarna/disputes | 5225 | 5089 | wiki/sources/source-stripe-klarna-disputes.md |
| 98 | https://docs.stripe.com/payments/klarna/set-up-future-payments | 66 | 19920 | wiki/sources/source-stripe-klarna-set-up-future-payments.md |
| 99 | https://docs.stripe.com/payments/klarna/supplementary-purchase-data | 1885 | 2317 | wiki/sources/source-stripe-klarna-supplementary-data.md |
| 100 | https://docs.stripe.com/payments/konbini | 1629 | 791 | wiki/sources/source-stripe-konbini.md |
