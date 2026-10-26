# Q1 — Purpose, scope and limits

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-android-sdk.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-blik-android-drop-in-earlier-versions.md` → pinned raw.

This 2026-09-15 capture is headed **BLIK Drop-in v4.x.x integration** and covers a historical Android Drop-in BLIK-with-code redirect flow; its table says v3.8.0+ is required (raw `adyen/docs/payment-methods/blik/android-drop-in/earlier-versions/2026-09-15.md:15-26`). It does not establish behavior of current Android SDK versions, merchant enablement, settlement, or One Click tokenization. The prerequisite hyperlink is mislabeled for this scope because it encodes `platform=iOS` and `integration=Components`; verify the actual Android Drop-in base guide (raw line 25). Source stem: `source-adyen-docs-payment-methods-blik-android-drop-in-earlier-versions`.

# Q2 — Central capability, prerequisites and warnings

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-android-sdk.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-blik-android-drop-in-earlier-versions.md`. Online-payment retrieval also routes via `wiki/concepts/adyen-online-payments.md`.

Discovery uses PL/PLN and a minor-unit amount; Drop-in passes `paymentComponentData.paymentMethod` to the server, whose `/payments` request prose additionally asks for `returnURL` up to 1024 characters, though code examples omit it (raw `adyen/docs/payment-methods/blik/android-drop-in/earlier-versions/2026-09-15.md:28-73,75-359`). A `RedirectShopper` response provides the action, but its example URL contains a PayPal-named path despite BLIK (raw lines 361-387). On app return, pass `actionComponentData.details` to `/payments/details`; its `resultCode` can inform the frontend, while an asynchronous `AUTHORISATION` webhook reports outcome. `Pending`/`Received` are nonfinal (raw lines 389-444). TEST names BLIK code `999000`; live acceptance requires adding BLIK in live Customer Area (raw lines 446-456).
