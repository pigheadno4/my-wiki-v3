# Fixed retrieval checks — Adyen Manage your balances

## Q1 — Purpose, scope, and non-inference

**Question:** What balances and money movements does this guide cover, and what should initiating a top-up or transfer not be taken to prove?

**Expected answer:** It describes a merchant account's pending balance, refund reserve, next payout amount, deposit and negative refund allowance, plus allotment of increases, Customer Area top-ups, and same-company/legal-entity merchant-account transfers. Adyen fixes deposit and negative-refund-allowance amounts. A generated top-up is not received funds: the page says funds are added when Adyen receives the payment. A request or example does not prove a particular transfer occurred or an external bank payout arrived. The automatic behavior described is allocation and reserve-threshold adjustment, not automatic sourcing of new funds.

**Raw locators:** Introduction lines 17–32; `Fund allotment` lines 34–70; `Top up your account` lines 84–90; API example/response lines 152–187.

**Canonical wiki route:** [[adyen-index]] → [[adyen-account-structure]] → [[source-adyen-docs-account-manage-your-balances]].

## Q2 — Central capability, prerequisites, and warnings

**Question:** How are incoming funds allotted, who can manage or transfer them, and what constraints and field units apply?

**Expected answer:** A balance increase enters pending first, then is allotted after settlement. Top-up reasons can direct funds to reserve or deposit, or offset a negative payable amount; reserve funding above threshold raises that threshold. Without a reason, and for increases from processed payments or transfers, the priority is negative pending/next payout, mandatory deposit, reserve threshold, then pending/next payout. A transfer requires two merchant accounts under the same company and legal entity with a common processing currency. The general Customer Area requirements table offers `Merchant financial` or `Manage key financial tasks`, but the transfer-specific Customer Area section states `Merchant financial`; the API requires `Balance control API - Balances management`. In `POST /balanceTransfers`, `amount.value` is in minor units and the currency/source/destination/type are required; `reference` is optional. The response and activity-log/report routes are separate from bank-arrival evidence.

**Raw locators:** `Fund allotment` lines 36–68; `Requirements` lines 72–82; `Transfer funds between accounts` lines 107–150 and response lines 173–187; activity log lines 189–201.

**Canonical wiki route:** [[adyen-index]] → [[adyen-account-structure]] → [[source-adyen-docs-account-manage-your-balances]] → [[raw/adyen/docs/account/manage-your-balances/2026-09-16|pinned raw snapshot]].
