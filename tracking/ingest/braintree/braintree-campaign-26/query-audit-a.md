# C26 fixed query audit — Group A

- Analysis end (UTC): `2026-10-02T11:07:32Z`
- Final handoff (UTC): `2026-10-02T11:08:17Z`
- Verdict: **PASS (4/4 questions; 2/2 manifest hashes)**

## auth-client-side-ios-v7

- Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-auth.md` → `wiki/sources/braintree/source-braintree-auth-client-side-ios-v7.md` → `raw/braintree/docs/guides/braintree-auth/client-side/ios/v7-2026-09-16.md`. The source has not yet been added directly to the coordinator-owned Braintree source catalog; the concept route is complete.
- Hash: `12d4e8844845bcb67ee7675b6a32bad55c3191b3676b97671cfdac9744236207` = C26 manifest — **PASS**.
- Q1 — “Where is the iOS v7 Auth client-side connect guide?”
  - Object/action match: iOS v7 Braintree Auth client-side Connect guide / locate the guide — **MATCH**.
  - Direct answer: `https://developer.paypal.com/braintree/docs/guides/braintree-auth/client-side/ios/v7`; pinned raw path above.
  - Exact locator: raw lines 1, 6-9, 14 — **PASS**.
- Q2 — “What client flow, responsibilities and qualifications does this variant state?”
  - Object/action match: iOS v7 client Connect sequence / state client, Braintree and server responsibilities plus qualifications — **MATCH**.
  - Direct answer: the merchant taps **Connect with Braintree**; the app opens a server-supplied `connect_url` in `SFSafariViewController`; Braintree authorizes and redirects to the `redirect_uri`; the server performs the OAuth exchange and redirects to a custom URL scheme captured by the app. The app registers an observer and dismisses Safari on the return event. Braintree Auth is labeled closed beta. The historical certificate notice says the mobile certificates were set to expire 2026-03-30, names iOS SDK `6.17.0+` as the upgrade floor, and warns traffic from affected older app versions would fail. Preserve the security conflict: prose claims the application-delegate handler ensures a trusted source, but the displayed handler only posts the received `url` and returns `true`; it does not visibly inspect `url` or `sourceApplication`. The server must not put sensitive data in the custom URL because other apps can intercept custom schemes.
  - Exact locator: availability lines 17-18; certificate conditions lines 21-24; responsibility split lines 26-33; server-provided URL and Safari presentation lines 45-67; observer/dismissal lines 69-102; custom-scheme configuration lines 104-125; trust prose/code conflict lines 127-140; interception warning lines 142-145 — **PASS**.

## auth-client-side-android-v5

- Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-auth.md` → `wiki/sources/braintree/source-braintree-auth-client-side-android-v5.md` → `raw/braintree/docs/guides/braintree-auth/client-side/android/v5-2026-09-16.md`. The source has not yet been added directly to the coordinator-owned Braintree source catalog; the concept route is complete.
- Hash: `d8e0665f78f4ee2c238a8cbae6e435ee0ee762eb1846eeaa75b3899b2f93c9b4` = C26 manifest — **PASS**.
- Q1 — “Where is the Android v5 Auth client-side connect guide?”
  - Object/action match: Android v5 Braintree Auth client-side Connect guide / locate the guide — **MATCH**.
  - Direct answer: `https://developer.paypal.com/braintree/docs/guides/braintree-auth/client-side/android/v5`; pinned raw path above.
  - Exact locator: raw lines 1, 6-9, 14 — **PASS**.
- Q2 — “What client flow, responsibilities and qualifications does this variant state?”
  - Object/action match: Android v5 client Connect sequence / state client, Braintree and server responsibilities plus qualifications — **MATCH**.
  - Direct answer: the merchant taps **Connect with Braintree**; the app opens the server-supplied `connect_url` through an Android `Intent`; Braintree authorizes and redirects to the `redirect_uri`; the server performs the OAuth exchange and redirects to `/merchant-connected`, which the app's manifest `IntentFilter` captures to launch its activity. The snapshot labels Braintree Auth closed beta. Its historical certificate notice says certificates were set to expire 2026-03-30, names Android SDK `4.45.0+` or `5.0.0+` as upgrade targets, and warns traffic from affected older versions would fail. It separately says future Android SDK versions will require verified Intent Filters; this is not evidence that the displayed snapshot already enforces verification.
  - Exact locator: availability lines 17-18; certificate conditions lines 21-24; responsibility split lines 26-33; button example lines 36-53; activity/`IntentFilter` configuration lines 55-76; future-verification qualification lines 78-79; server URL and `/merchant-connected` return lines 82-86 — **PASS**.

## Shared bounded checks

- Raw gap sweep: one filename-bounded sweep of `raw/braintree/docs/guides/braintree-auth/client-side/` found the assigned iOS v7 and Android v5 raws plus the separate JavaScript v3 sibling. No missing same-topic raw was found.
- Extra reads: none. The JavaScript sibling was outside Group A. The Android source's related OAuth-flow raw remained navigation-only because both assigned raws directly state the server-owned exchange and are sufficient for the fixed questions.
- Reciprocal checks: `wiki/index.md` routes to `wiki/braintree-index.md`; that index routes to `[[braintree-auth]]`; the concept links both assigned source pages; each source links back to `[[braintree-auth]]` and to its exact raw. Direct Braintree-index/company catalog insertion is deferred coordinator-owned aggregation and is not counted as a retrieval failure.
- Final verdict: **PASS**.
