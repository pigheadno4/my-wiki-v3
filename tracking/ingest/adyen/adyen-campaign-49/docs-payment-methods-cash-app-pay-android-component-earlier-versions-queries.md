# Cash App Pay Android Component earlier-versions retrieval checks

## Q1 — version, flow and scope

Query: What does the captured Cash App Pay Android Component earlier-versions guide require, and does it establish the current Android flow or live enablement?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-pay-android-component-earlier-versions.md` → `raw/adyen/docs/payment-methods/cash-app-pay/android-component/earlier-versions/2026-09-15.md` lines 14–81. Canonical stem: `/payment-methods/cash-app-pay/android-component/earlier-versions`.

Expected answer: This is captured v4.x.x guidance. The requirements demand an existing Advanced Android Components integration with minimum version 4.12.0, Recurring tokens life cycle events webhook, Customer Area method addition and Recurring details additional data. The opening Sessions link and latest-version dependency/base links do not override that captured requirement or prove current compatibility. Configure the Component return URL and Activity IntentFilter. The page does not prove live merchant enablement.

## Q2 — payment outcome, token and example boundaries

Query: What is required to handle a Cash App Pay Android Component payment and later token payments, and when is the result final?

Expected route: same root/provider/concept/source/raw chain; verify raw lines 83–250 and 600–645, with token request examples at 252–597. Canonical stem: `/payment-methods/cash-app-pay/android-component/earlier-versions`.

Expected answer: Collect `cashapp` Component state, submit `/payments` server-side with the return URL, and handle `/payments/details` plus asynchronous webhook outcomes. `Received` is nonfinal until AUTHORISATION; manual capture remains necessary if configured. With shopper permission, a save-details choice or configured storage supplies `storePaymentMethod` and `shopperReference`; enable digital-wallet token information for $cashtag in details, use the stored payment method ID for later `ContAuth` token payments, and remove the token after `recurring.token.disabled`. The source has `setStorePaymentMethod` casing and `merchantRreference` sample typos, a curl snippet in a JSON fence, and TEST v68/v72 examples that do not prove current API version, payment success or live readiness.
