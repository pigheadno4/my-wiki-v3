# Fixed retrieval checks: click-and-collect landing page

## Q1 — Purpose and scope

**Query:** What does this Adyen click-and-collect page define, and what does it not prove about payment?

**Expected answer:** It defines a retail service in which customers order or buy online and collect at a physical store, then serves as a landing page for variations. It does not specify authorization, capture, refund execution, merchant account, legal seller/MOR, settlement or funds flow. The page's convenience and same-day pickup wording is descriptive, not a fulfillment promise for a given merchant.

**Raw locators:** `# Click and collect`, lines 15–25. **Canonical retrieval route:** [[source-adyen-docs-unified-commerce-retail-use-cases-click-and-collect]] → [[raw/adyen/docs/unified-commerce/retail-use-cases/click-and-collect/2026-09-15|pinned raw]].

## Q2 — Scenario routes without imported behavior

**Query:** Which click-and-collect variants does the page route to, and how should their order/fulfillment labels be used?

**Expected answer:** It routes to reserve online and try in store before buying; buy online and pick up with possible item removal/refund or an additional store purchase; and buy online with assistant pickup. These are navigation labels for separate scenario guides. The landing page does not itself say how any variant's payment is authorized, captured, refunded or settled; use the specific reviewed scenario source for those mechanics and conditions.

**Raw locators:** variation list, lines 21–25; `## Next steps`, lines 27–39. **Canonical retrieval route:** [[source-adyen-docs-unified-commerce-retail-use-cases-click-and-collect]] → [[raw/adyen/docs/unified-commerce/retail-use-cases/click-and-collect/2026-09-15|pinned raw]].
