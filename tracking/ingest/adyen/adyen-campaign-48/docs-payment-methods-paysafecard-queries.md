# Fixed queries — PaySafeCard overview

## Q1 — purpose and scope

**Query:** What does the captured PaySafeCard overview establish, and which conclusions would be overreach?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/paysafecard` is a 2026-09-15-captured overview of a prepaid online method, with capability and country/currency tables, a conditional Customer Data Exchange link for EU gambling KYC, and platform integration routes. Marketing claims about safety/leadership are source claims. The snapshot does not establish current market or account availability, KYC compliance, live payment success, or a full recurring/refund implementation (full pinned `raw/adyen/docs/payment-methods/paysafecard/2026-09-15.md`, `# PaySafeCard` lines 15–27, `## Customer Data Exchange` lines 29–31). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard.md`.

## Q2 — matrix, KYC condition, geography and warnings

**Query:** Which flow and lifecycle marks does the captured table give, when does Customer Data Exchange enter, and how should the country/currency table be read?

**Expected answer:** The matrix labels PaySafeCard Prepaid and gift cards, **Direct** flow, International/Multiple; it checks recurring and refunds and crosses partial/multiple partial refunds, separate/partial/multiple partial captures, and chargebacks (`raw/adyen/docs/payment-methods/paysafecard/2026-09-15.md`, capability table lines 25–27). These are page marks, not current entitlements or a complete recipe. Customer Data Exchange **can** be used in EU countries **where gambling-customer KYC is required** to prevent acquiring funds from an anonymous shopper (`## Customer Data Exchange`, lines 29–31); this does not by itself prove compliance. The country table has literal country/currency pairs, repeats Belgium and Ireland, and labels UK/UAE as `countryCode` values (raw `## Supported countries/regions and currencies` lines 33–86); do not silently normalize or treat it as a current API validation/availability guarantee. The chooser routes Web, iOS, Android, React Native, Flutter, and API-only, while See also links are general navigation (lines 88–131). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard.md`.
