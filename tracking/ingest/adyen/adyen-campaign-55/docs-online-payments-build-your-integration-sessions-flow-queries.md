# C55 Sessions worker query audit

Target stem: `source-adyen-docs-online-payments-build-your-integration-sessions-flow`
Canonical URL: https://docs.adyen.com/online-payments/build-your-integration/sessions-flow
Pinned raw: `raw/adyen/docs/online-payments/build-your-integration/sessions-flow/2026-09-15.md`
SHA-256: `2a4f52965f5d49bdcc9b3a3d274ad4e65e2d4b274dbbd9e5669fbfa0ed04fe29`

## Q1

**Question:** In a Sessions integration, which actor creates the session, who handles shopper actions, and what evidence should update the order?

**Answer:** The merchant payment server calls `/sessions`; Web Drop-in/Components or the native client use the session response's `id` and `sessionData` to render and handle the shopper flow. A client result code can inform the shopper about current status. The merchant webhook server receives the asynchronous `AUTHORISATION` event, whose `merchantReference` connects it to the order. The optional GET session-result status is fixed in the response and must not be polled for updates. Locators: raw lines 64–95, 738–759, 1666–1678, 1682–1694, 1879–1895; native correspondence at 3672–3690, 6218–6255 and 10053–10067.

## Q2

**Question:** When can a Sessions amount be updated, and what redirect or version conditions change the client flow?

**Answer:** Checkout API v72+ supports updating the session amount: create with `payable: false`, PATCH the server-side amount and original session data, pass the refreshed `sessionData` to the client, then set `payable: true` only at the final amount because it cannot be updated afterward. The Web guide's event table says `onSubmit` is required for amount updates, while its procedure calls `beforeSubmit`; this is an unresolved snapshot conflict, not a universal callback recipe. For a Web redirect, the return URL carries `sessionId` and `redirectResult`; submit the result when the shopper returns, otherwise rely on the webhook. React Native Drop-in v1 and Components v1/v2 are explicitly Advanced-only, while this page shows Sessions for React Native Drop-in v2. Locators: raw lines 482–488, 895–903, 1514–1570, 1621–1664, 8830–8838.
