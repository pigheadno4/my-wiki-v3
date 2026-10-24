# Retrieval queries — docs-payment-methods-kakaopay-android-component

## Q1 — Android setup and flow prerequisites

**Query:** How is KakaoPay added to Android Components under Sessions versus Advanced flow?

**Answer:** Both are add-ons to existing Android Components, requiring KakaoPay in Customer Area and redirect-action handling. Sessions specifically lists Checkout API v68+ and gets method `kakaopay` from `checkoutSession`; Advanced selects `kakaopay` from `/paymentMethods` and does not independently restate the v68+ minimum. Both use the `instant` module and `InstantPaymentComponent`, with `components-compose` when using Compose. The no-extra-request-parameters language covers the base `/sessions` or `/payments` path, not recurring. Raw lines 23–125 and 378–478.

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-kakaopay-android-component]] → [[raw/adyen/docs/payment-methods/kakaopay/android-component/2026-09-15]].

## Q2 — recurring token and outcome boundary

**Query:** Does Kakao confirmation immediately provide a reusable token, and what changes for later token payments?

**Answer:** No. For token creation, the server adds `storePaymentMethod: true` and `shopperReference` to `/payments`; the shopper signs into Kakao and confirms the recurring transaction. The guide says `recurring.token.created` with `storedPaymentMethodId` arrives **when the initial payment has settled**. Future `/payments` calls include that ID, the shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel` chosen as `Subscription` or `UnscheduledCardOnFile` by interval. The page does not make a redirect or API response proof of authorization, settlement or token creation. Its recurring snippets vary in `returnUrl` presence and example amount, so no single snippet is complete universal authority. Raw lines 132–167, 171–365, 484–519 and 523–717; live Customer Area request at lines 368–376 and 720–728.

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-kakaopay-android-component]] → [[raw/adyen/docs/payment-methods/kakaopay/android-component/2026-09-15]].
