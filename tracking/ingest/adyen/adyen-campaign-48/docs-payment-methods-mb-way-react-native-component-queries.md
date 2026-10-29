# MB WAY React Native Component retrieval checks

## Q1 — purpose and flow boundary

Query: Does the 2026-09-15 MB WAY React Native Components guide support Sessions, and what does its Advanced add-on cover?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way-react-native-component.md` → `raw/adyen/docs/payment-methods/mb-way/react-native-component/2026-09-15.md` lines 15–47. Canonical stem: `/payment-methods/mb-way/react-native-component`.

Expected answer: This captured method add-on says React Native Components Sessions flow is unavailable. Its Advanced flow presumes an existing Components integration, await-action handling and Customer Area setup; no extra MB WAY configuration is specified. The Advanced integration-type link is mislabeled Components while selecting Drop-in, so use the matching Components base flow. This is not a complete integration or live-payment proof.

## Q2 — request, pending outcome and test/live conditions

Query: Which MB WAY fields and result handling does the React Native Components Advanced guide require, and what do its examples establish?

Expected route: same root/provider/concept/source/raw chain; verify raw lines 49–123. Canonical stem: `/payment-methods/mb-way/react-native-component`.

Expected answer: The `/payments` table marks `paymentMethod.type: mbway` and `paymentMethod.telephoneNumber` required; `shopperStatement` is listed without a required mark. The TEST v72 example returns `Pending` with `action.type: await`, a waiting state while the shopper completes payment in MB WAY, not final authorization. Its curl sample lacks a continuation after `-X POST`, and its HTTPS returnUrl is an example rather than an app-specific return-path rule or API minimum. Testing permits any phone number and `shopperStatement` suffixes `-c1`, `-c3`, `-c5` on `/payments`; live acceptance requires MB WAY in live Customer Area.
