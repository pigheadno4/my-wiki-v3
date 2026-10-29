# C44 PayBright Android retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-paybright-android`

Full pinned raw path: `raw/adyen/docs/payment-methods/paybright/android/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-paybright-android]]` → `[[raw/adyen/docs/payment-methods/paybright/android/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** Does this Android page support a new PayBright integration?

**Answer path:** The page is a chooser (raw `## How do you want to integrate?`, lines 21–35). Its line 19 explicitly says Adyen will not accept new PayBright integrations after the Affirm acquisition. Child links and base-guide navigation do not prove new merchant availability, deployment or a completed payment.

## Q2 — central routes and warnings

**Query:** Where should an existing Android PayBright integration go next, and which flow assumption is unsafe?

**Answer path:** Raw lines 23–27 route to Android Drop-in, and lines 29–33 route to the Redirect Component. Line 35 links base Android Sessions guides. The linked [[source-adyen-docs-payment-methods-paybright-android-drop-in]] says its method-specific requirement is Advanced, so the chooser's Sessions links must not be used as a universal PayBright flow requirement. Read the selected child guide for actual request and lifecycle behavior.
