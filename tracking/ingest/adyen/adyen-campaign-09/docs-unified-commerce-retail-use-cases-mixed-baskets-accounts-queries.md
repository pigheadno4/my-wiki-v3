# Fixed retrieval checks: mixed-basket account structures

## Q1 — Purpose and scope

**Query:** What problem does Adyen's mixed-basket account-structures page address, and what does it not establish about ownership or funds?

**Expected answer:** It compares account/store configurations for an order containing online and in-store items in a merchant integration with both ecommerce and in-person payment channels. The choice affects payment-request count, payment-method setup, sale attribution and reconciliation. It advises discussing the options with Adyen. It does not identify legal sellers or merchant-of-record roles, payout recipients, settlement accounts, tax treatment, or a complete funds flow; an order is not automatically one payment.

**Raw locators:** `# Account structures for mixed baskets`, lines 15–21; `## Requirements`, lines 23–31; four account-structure sections, lines 33–95. **Canonical retrieval route:** [[source-adyen-docs-unified-commerce-retail-use-cases-mixed-baskets-accounts]] → [[raw/adyen/docs/unified-commerce/retail-use-cases/mixed-baskets-accounts/2026-09-15|pinned raw]].

## Q2 — Payment-request and reconciliation choices

**Query:** How do the four documented structures change authorization, capture, method configuration and reconciliation?

**Expected answer:** With one merchant account and no stores, authorize the full mixed-basket amount and make separate partial captures if fulfillment times differ; ecommerce/POS transactions are not separated in reconciliation. With separate ecommerce and POS merchant accounts, submit two payment requests, each through its account and configured methods, with separate reconciliation. With one combined account plus POS stores, submit two requests through that account; online methods are account-level, in-store methods are POS-store-level, and the channels are distinguishable in the same reconciliation file. With one combined account plus both ecommerce and POS stores, submit two requests through the account, using each store's methods and reconciling within that account. None of those structures alone proves capture completion, one legal entity or a settlement destination.

**Raw locators:** `## One merchant account without stores`, lines 33–45; `## Separate merchant accounts`, lines 47–61; `## One merchant account with POS stores`, lines 63–78; `## One merchant account with ecommerce and POS stores`, lines 80–95. **Canonical retrieval route:** [[source-adyen-docs-unified-commerce-retail-use-cases-mixed-baskets-accounts]] → [[raw/adyen/docs/unified-commerce/retail-use-cases/mixed-baskets-accounts/2026-09-15|pinned raw]].
