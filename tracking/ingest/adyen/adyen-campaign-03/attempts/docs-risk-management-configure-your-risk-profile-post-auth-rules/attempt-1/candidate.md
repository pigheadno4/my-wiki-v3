---
title: "Adyen Post-authorization Risk Rules"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/configure-your-risk-profile/post-auth-rules"
raw_files:
  - "adyen/docs/risk-management/configure-your-risk-profile/post-auth-rules/2026-09-15.md"
tags: [adyen, risk-management, post-authorization, avs, cvc, liability-shift]
---

## Overview

This Adyen Docs snapshot describes built-in post-authorization risk rules that evaluate information returned after card-scheme and issuer authorization, including AVS address checks, CVC checks, and liability-shift status. The rules influence the later risk evaluation; an issuer authorization has already occurred before they run. See [[adyen]] and [[adyen-risk-management]]. The documented prerequisites are an online payments integration, enabled risk management, and a Customer Area user with **Merchant change risk settings** or **Risk admin** role.

## Key takeaways

- All post-authorization rules are disabled by default. The page warns that enabling AVS or CVC mismatch rules can increase declines because shoppers may enter address or CVC details incorrectly. Its Adyen Uplift Optimize and Smart Payment Messaging settings are recommendations, not mandatory prerequisites.
- The built-in **AVS**, **CVC**, and **Liability shift status blocked** rules are configured in the risk profile's **Block** section. The separate **Liability shift status allowed** rule is enabled in **Allow**. These are risk-rule actions after authorization, not a way to change the issuer's earlier authorization decision or guarantee payment completion.
- The AVS rule checks shopper-entered billing address against the issuer's address; the CVC rule checks the verification code after issuer authorization. The CVC rule does not trigger on recurring transactions, because this page says it runs only on the initial transaction. Liability-shift rules test whether shift occurred; the liability-shift rule does not trigger for recurring merchant-initiated transactions with **ContAuth** shopper interaction.
- These post-authorization AVS, CVC, and liability-shift rules cannot be linked to Dynamic 3D Secure because they run after authorization. A matched enabled rule *can* be part of control traffic for false-positive analysis; this is a possibility, not a guarantee for every match. Protect premium offers more specific custom post-authorization rules, but the page does not make premium a prerequisite for these built-in rules.
- The raw lists exact block conditions for AVS, CVC, and liability-shift checks, including a CVC option that also covers missing code or an issuer unable to check it. Those settings can materially change which transactions are blocked and should be assessed against the chosen risk profile.

## Detail locators

- Opening and `## Requirements`, raw lines 15–30 — post-authorization signals, integration/risk/role prerequisites, Dynamic 3DS and ContAuth limits.
- `## How it works`, raw lines 32–49 — disabled default, decline warning, control-traffic possibility, premium custom route, and AVS/CVC/liability-shift rule meanings.
- `## Configure a post-authorization rule`, raw lines 51–77 — Customer Area Block path and exact AVS/CVC/liability-shift options.
- `## Enable a post-authorization rule`, raw lines 79–106 — separate Block and liability-shift Allow enablement paths.

## Related

- [[adyen]] — provider page.
- [[adyen-risk-management]] — Protect risk-profile concept.
- [[source-adyen-docs-risk-management-avs-checks]] — separate AVS guidance.
- [[source-adyen-docs-risk-management-configure-your-risk-profile-custom-rules]] — premium custom-rule route.

## Raw Sources

- [[raw/adyen/docs/risk-management/configure-your-risk-profile/post-auth-rules/2026-09-15|Adyen Docs — Post-authorization rules (2026-09-15 snapshot)]]
