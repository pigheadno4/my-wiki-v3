---
title: "Adyen Bank Transfer via KCP iOS Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bank-transfer-kcp/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bank-transfer-kcp/ios-drop-in/2026-09-15.md"
tags: [adyen, kcp, bank-transfer, ios, drop-in, south-korea]
---

## Overview

This [[adyen]] guide adds **Bank Transfer via KCP** to an existing iOS Drop-in Sessions or Advanced integration. It states method-specific setup, request/configuration conditions and a testing-credential limitation, while linking to the main integration for ordinary flow behavior. See [[adyen-online-payments]] and [[adyen-ios-sdk]]. This 2026-09-15 snapshot does not prove current merchant eligibility or successful bank authorization/settlement.

## Key takeaways

- **Sessions** requires an existing iOS Drop-in Sessions integration, **Checkout API v68 or later**, and adding KCP bank transfer in Customer Area. It states no additional method-specific `/sessions` parameters or configuration. This section does not separately spell out a redirect-handling requirement; it points to the base Sessions guide, so absence of a method-specific line is not evidence that no redirect occurs. See raw lines 25–46.
- **Advanced** requires an existing iOS Drop-in Advanced integration, redirect handling for `action.type: redirect`, and Customer Area method addition. It says no additional KCP configuration or `/payments` parameters. The page gives no Advanced Checkout API minimum. These are KCP add-on statements, not permission to omit base-flow request or action handling. See raw lines 54–76.
- Under “Test and go live,” both flow sections say **there are no KCP bank-transfer testing credentials** because bank transfer has to be authorized with a **Public Identification Certificate**, also called a “Digital Signature for individuals.” The page gives no specific live-enablement instruction or final payment-result/webhook process. This does not establish absence of a TEST environment, authorize simulated certificate use or indicate that a redirect means funds settled. See raw lines 48–52 and 78–82.

## Detail locators

- **Sessions v68+ and Customer Area prerequisite:** raw lines 25–34.
- **Sessions no-extra-fields/configuration statements:** raw lines 36–46.
- **Advanced redirect and setup prerequisites:** raw lines 54–64.
- **Advanced no-extra-fields/configuration statements:** raw lines 66–76.
- **No testing credentials and PIC reason:** raw lines 48–52 and 78–82.

## Related

- [[adyen-online-payments]]
- [[adyen-ios-sdk]]
- [[source-adyen-docs-payment-methods-bank-transfer-kcp]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bank-transfer-kcp/ios-drop-in/2026-09-15|KCP iOS Drop-in guide — captured 2026-09-15]]
