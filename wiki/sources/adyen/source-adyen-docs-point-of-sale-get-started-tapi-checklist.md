---
title: "Adyen Docs: Terminal API integration checklist"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/get-started/tapi-checklist"
raw_files:
  - "adyen/docs/point-of-sale/get-started/tapi-checklist/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, test-integration, go-live]
---

## Overview

This Adyen checklist guides a merchant building and testing a Terminal API point-of-sale integration with Adyen-provided terminals, from test-account structure and architecture choice through terminal setup, transaction/reconciliation tests, and a live-account application. Its linked detail pages carry implementation specifics. The checklist is a test-to-live route, not proof that a particular merchant account, payment method, terminal, acquirer response, or SDK version is enabled or working. See [[adyen-terminal-api]].

## Key takeaways

- Begin with an Adyen test account and plan company, merchant-account, and optional store structure. The page says the live account structure must be set up again, while the test structure should reflect the planned live structure. Merchant-account and store creation have their own request/confirmation steps. See **1. Set up your Adyen test account**.
- Scope a Terminal API architecture before implementation: local POS-to-terminal communication or cloud communication through Adyen's platform. The checklist says to always consult Adyen before building cloud integration. Standalone terminals are a separate no-integration option; mobile solutions require Terminal API plus the appropriate POS Mobile SDK. Select payment features and security needs; E2EE is described as default, while P2PE needs Adyen notice and different terminal software. See **2. Scope your integration**.
- Order test terminal(s) and a test card, then configure test terminals at the chosen company, merchant, store, or terminal level. An integrated solution needs Terminal API enabled; add the payment methods and features in scope and assign terminals to a store. Some features require Support help. The page's terminal ordering timeline is a dated checklist claim, not a delivery guarantee. See **3. Order test payment terminals** and **4. Prepare your terminals**.
- A test account includes a default API credential for authenticated flows. Additional users and API credentials are optional in the test setup; the page recommends a further credential, or separate POS/ecommerce credentials, when going live. For the chosen local or cloud path, use its correct endpoint/IP and authentication; cloud is given as an API-key example. No specific credential-role matrix or SDK release is established by this checklist. See **5. Set up your integration**.
- Test happy and failure paths, including timeouts and connection problems, simulated acquirer declines, card types/CVM, POS- and terminal-initiated cancellations, referenced/unreferenced refunds, and only the payment methods/features actually added. Test error handling and settlement reconciliation; Store IDs or DCC reporting fields require a Support request in the described workflow. These are test tasks, not a guarantee of live acquirer behavior. See **6. Test your integration**.
- After testing, the checklist says the merchant must apply for a live account and sign the contract before taking the integration live. Test completion alone is not go-live authorization. See **Going live**.

## Detail locators

- **Requirements** — test-account sign-up and Get started pre-reading.
- **1. Set up your Adyen test account** — company/merchant/store structure, requests, and live recreation.
- **2. Scope your integration** — local versus cloud, consultation warning, standalone/mobile distinctions, payment-feature scoping, and E2EE/P2PE choice.
- **3. Order test payment terminals** — test device and card selection and dated delivery estimate.
- **4. Prepare your terminals** — settings inheritance, Terminal API enablement, method/feature configuration, and store assignment.
- **5. Set up your integration** — optional users/credentials, default test credential, local/cloud endpoints and authentication, network guidance, terminal inspection/boarding.
- **6. Test your integration** — transaction, failure, acquirer-response simulation, method/feature, troubleshooting, and reconciliation checks.
- **Going live** — live-account application and signed-contract prerequisite.

## Related

- [[adyen]]
- [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/get-started/tapi-checklist/2026-09-15|Adyen Docs — Terminal API integration checklist (2026-09-15)]]
