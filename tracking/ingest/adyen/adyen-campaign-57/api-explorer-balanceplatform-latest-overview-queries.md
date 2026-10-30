# C57 fixed query answers: Configuration API v2 overview

Canonical source route: [[source-adyen-api-explorer-balanceplatform-latest-overview]] — https://docs.adyen.com/api-explorer/balanceplatform/latest/overview
Pinned raw: [[raw/adyen/api-explorer/balanceplatform/latest/overview/2026-09-15]] (captured 2026-09-15).

## Q1

The capture calls this **Configuration API v2** and says it manages a balance platform and can create account holders, balance accounts, cards and business accounts (raw lines 5–7). Separately, its endpoint table lists account-holder, balance-account and balance-platform routes (lines 42–60), plus payment-instrument/card, grant account/offer and other resource routes (lines 61–94, 95–137). It lists **no business-account endpoint** (lines 39–137). Every request requires an API key; the page directs platform/marketplace integrations to their Customer Area setup and Issuing integrations to their Balance Platform Customer Area, and illustrates `X-API-Key` (lines 9–20). It lists no request schema, required body properties, operation-specific roles, or conditional field matrix. Thus the only general request prerequisite established here is the API key, plus environment-specific key generation for LIVE (lines 30–35).

## Q2

No response bodies, status codes or error schemas appear in this overview; its endpoint table has only method/path/summary (raw lines 37–137). Labels such as initiate/complete association (lines 83–88), approve pending transfer limits (lines 106–111), delete sweep/setting/device/association (lines 49–53, 114–118, 131–137), and create top-up/payout schedule (lines 96–105) are navigation only. They cannot prove approval, verification, propagation, deletion effects, executed payout, transfer booking or bank receipt. The captured version is **v2**, with `/bcl/v2` TEST base (lines 22–35) and a separately stated LIVE base and live key (lines 30–32); the `latest` page path does not prove any newer version or current availability. Operation-level references and live integration evidence are needed for broader claims.
