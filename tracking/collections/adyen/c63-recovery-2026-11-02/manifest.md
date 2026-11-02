# Adyen C63 bounded API Explorer recovery collection

Collection approved 2026-11-02; collection complete. No ingestion or publication.

- 37 selected gap items resolved to exact official URLs; 37 HTTP200 responses.
- 10 Checkout pages recovered with complete-body structural screens and retained exact response bytes. This is not semantic source review.
- All27 stub retries still title-only; excluded, no replacement raw generated.
- Existing Adyen raw/wiki hashes unchanged; concurrent unrelated PayPal changes preserved. New raw dated2026-11-02, no accepted snapshot overwritten.
- Officialcatalog used only to resolve approved method/path labels; duplicated API prefix fixups logged; parentheses preserved. No other catalogtargets fetched.

| Operation | New raw | SHA256 |
| --- | --- | --- |
| GET `/paymentLinks/{linkId}` | `raw/adyen/api-explorer/Checkout/latest/get/paymentLinks/(linkId)/2026-11-02.md` | 62af562da42c9693cf7e838d57d88d2ac3c0f61c9a1329ee1846ce4e815fc5ed |
| PATCH `/paymentLinks/{linkId}` | `raw/adyen/api-explorer/Checkout/latest/patch/paymentLinks/(linkId)/2026-11-02.md` | 03b90577ce74421a6fc95664f1d1eddf24fd2d9f76f3141203b898d202351736 |
| POST `/payments/{paymentPspReference}/amountUpdates` | `raw/adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/amountUpdates/2026-11-02.md` | cd42a877e1e466e6cbe93d64848ae445c3bed512e8acfbeb694f407f89e32ef8 |
| POST `/payments/{paymentPspReference}/cancels` | `raw/adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/cancels/2026-11-02.md` | 47769a8dd8a2fe576152af9d8192dd3215db304a5da924b0acf5588b38160965 |
| POST `/payments/{paymentPspReference}/captures` | `raw/adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/captures/2026-11-02.md` | 71adcf931a095f99c744b9304982848deb78e38d94fb621bff63643167f51888 |
| POST `/payments/{paymentPspReference}/refunds` | `raw/adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/refunds/2026-11-02.md` | 77f36cfcce69b0b454cfd025ef6bcaa45cc1e7cde983732dee7757e08eae012b |
| POST `/payments/{paymentPspReference}/reversals` | `raw/adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/reversals/2026-11-02.md` | be29efb0f2b8c446bf84e4447441a55ecf627cf88413173de721c77f42548f38 |
| GET `/sessions/{sessionId}` | `raw/adyen/api-explorer/Checkout/latest/get/sessions/(sessionId)/2026-11-02.md` | 2f1a6f3529630c1f4c1c7eedff80c98f359566232c4418b0c2c6b530e58ceb07 |
| PATCH `/sessions/{sessionId}` | `raw/adyen/api-explorer/Checkout/latest/patch/sessions/(sessionId)/2026-11-02.md` | c01a5662ef1e94675fba2d6554c08246f030024a34b76fcf843574a1da7f0016 |
| DELETE `/storedPaymentMethods/{storedPaymentMethodId}` | `raw/adyen/api-explorer/Checkout/latest/delete/storedPaymentMethods/(storedPaymentMethodId)/2026-11-02.md` | f00389e08cefc3bcdaa5708deca0cba7f776663e1975b1d3fadd68135fccfde7 |

Evidence: page-results.json, summary.json, url-resolution.json and per-response headers/status/body. Separate exact ingestion approval required.
