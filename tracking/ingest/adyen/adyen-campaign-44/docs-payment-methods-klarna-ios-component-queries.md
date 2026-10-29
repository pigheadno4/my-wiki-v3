# Klarna iOS Component retrieval checks

## Q1 — What does this guide cover, and what should the reader not infer?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-klarna-ios-component]]` → `[[raw/adyen/docs/payment-methods/klarna/ios-component/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-klarna-ios-component`. Full pinned raw path: `raw/adyen/docs/payment-methods/klarna/ios-component/2026-09-15.md`. Raw lines 15–45 frame an existing iOS Components integration with Customer Area Klarna setup, Sessions or Advanced flow, and default `/sessions` for v5.0.0+. Raw lines 1498–1553 show versioned Component setup. It does not prove method eligibility, shopper approval, capture, settlement or live execution.

## Q2 — Which prerequisites, transitions and warnings are central?

Use the same root/provider/concept/source/raw route. Raw lines 49–60 and 763–774 require invoice-line totals/descriptions and matching country; the email note concerns dispute defense; merchant attachment data is conditional and prohibited in TEST. Raw lines 1555–1571 require manual capture within 90 days unless immediate capture and shipping within 24 hours permit live configuration; raw lines 2017–2048 distinguish `received` from final `CAPTURE` webhook. Raw lines 2123–2130 use a separate `/capture` partial-capture example; raw lines 2132–2177 put recurring token creation after settlement and identify a Pay Now sample. Raw lines 2246–2273 supply live-test refusal conditions. The SE/SEK request examples' `en_US` locale conflicts with the table's locale-match instruction (lines 55/75–76 and 769/779–799).
