# Japanese convenience stores via econtext retrieval checks

## Q1 — Purpose and proof boundary

Query: What does Adyen's econtext Konbini overview cover, and does receiving a voucher prove that a payment was completed or that a merchant is currently eligible?

Expected route: `wiki/index.md` line 10 → `wiki/adyen-index.md` line 2716 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-econtext-konbini.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/econtext-konbini/2026-09-15.md` `# Japanese convenience stores` lines 15–23 and `#### How to pay at convenience stores` lines 32–42. Expected answer: a 2026-09-15-captured method overview for Japanese convenience-store payments through econtext, with store and shopper journey, expiry, capability matrix and integration routes. Voucher display or ticket issue occurs before later in-store cash payment, so it does not prove payment completion; the snapshot does not prove current merchant/store eligibility.

## Q2 — Store condition, cash journey and limits

Query: How do 7-Eleven and other Japanese convenience stores differ, what details must the shopper provide and when is cash paid, and what expiry/capability conditions are stated?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-econtext-konbini.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/econtext-konbini/2026-09-15.md` lines 23–30, `#### How to pay at convenience stores` lines 32–47, and `## How do you want to integrate?` lines 49–67. Expected answer: 7-Eleven alone is marked local-entity-required and uses a redirect to its voucher page; other listed stores show the voucher on the merchant site. Shopper supplies full name, phone and email, later gives reference/phone at the store for a ticket, pays cash and receives a receipt. The offer stays open up to seven days by default, adjustable via Support. Matrix says JP/JPY, 7-Eleven Redirect versus other stores Additional action, and no recurring/refunds/separate captures/chargebacks in either row. Web/API-only/Pay by Link are routes, not child-guide request recipes.
