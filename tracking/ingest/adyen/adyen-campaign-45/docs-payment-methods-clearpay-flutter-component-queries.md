# Clearpay Flutter Components retrieval checks

## Q1 — What integration does this page cover, and what cannot it establish?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-clearpay-flutter-component]]` → `[[raw/adyen/docs/payment-methods/clearpay/flutter-component/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-clearpay-flutter-component`. Full pinned raw path: `raw/adyen/docs/payment-methods/clearpay/flutter-component/2026-09-15.md`. Raw lines 15–34 and 207–217 describe an existing Flutter Components Sessions/Advanced add-on requiring Clearpay setup and redirect handling. GB/GBP examples do not prove live eligibility, transaction success or capture.

## Q2 — Which request, lifecycle and example qualifications matter?

Use the same root/provider/concept/source/raw route. Sessions requires Checkout API v68+ (32); both tables require shopper name/email/reference, country code, both addresses and line items, with optional phone (44–51/233–240). No extra Clearpay configuration parameters are specified (114–118/219–223); the Advanced example uses `paymentMethod.type: clearpay` and returns a redirect action (251–320), not authorization. Capture is account-configured, due within 13 days; noncapture cancels and refunds the first installment, and test manual capture is due within one day (124–130/326–332). Partial capture normally cancels remainder unless Support enables multiple partial captures; cancel before capture, refund after capture (132–152/334–354). Warn that both Components base links go to Advanced Drop-in (31/215), discount arithmetic/JSON conflict (156–188/358–390) and curl continuation omission (60–61/249–250). Sandbox and live-request routes are at 190–205/392–407.
