---
title: "Adyen Bank Transfer via KCP iOS Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bank-transfer-kcp/ios-component"
raw_files:
  - "adyen/docs/payment-methods/bank-transfer-kcp/ios-component/2026-09-15.md"
tags: [adyen, bank-transfer, kcp, ios, component, redirect]
---

## Overview

This 2026-09-15 Adyen page describes Bank Transfer via KCP-specific additions to an existing iOS Components integration, with separate Sessions and Advanced paths. Both paths initialize `InstantPaymentComponent` for `kcp_banktransfer` and require redirect handling. It does not document a complete integration or establish a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- For Sessions, the page requires an existing iOS Components Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and adding Bank Transfer via KCP in the Customer Area. It says no additional KCP parameters are needed in the base `/sessions` request and no additional method configuration is needed. The Swift example obtains the method from the session context, makes the session the component delegate, and calls `initiatePayment()`.
- For Advanced, the page requires an existing iOS Components Advanced integration, redirect handling, and the Customer Area method addition. It says no additional KCP configuration or base `/payments` parameters are needed. Its Swift example makes `self` the component delegate before calling `initiatePayment()`. The Advanced prerequisite text says “iOS Components integration,” but its linked URL uses `integration=Drop-in`; treat that link as a source inconsistency, not a different stated integration requirement. The page does not give the Advanced path a Checkout API minimum.
- Under both “Test and go live” headings, the page says there are no KCP bank-transfer testing credentials because authorization requires a Public Identification Certificate, also called “Digital Signature for individuals.” It gives no certificate acquisition procedure, test transaction, live enablement confirmation, or final payment-result instructions.

## Detail locators

- Sessions prerequisites: pinned raw lines 25–36; base request/configuration: lines 38–48; initialization code: lines 50–70.
- Sessions testing statement: lines 72–74.
- Advanced prerequisites and mismatched link: lines 76–86; configuration and initialization: lines 88–113; base payment request: lines 115–119; repeated testing statement: lines 121–123.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-bank-transfer-kcp]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bank-transfer-kcp/ios-component/2026-09-15|Bank Transfer via KCP iOS Component, 2026-09-15]]
