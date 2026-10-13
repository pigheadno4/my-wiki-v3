# Fixed retrieval checks — Adyen POS penalty box

## 1. Purpose, scope, and boundary

**Query:** What problem does the POS penalty box address, and what should it not be confused with?

**Answer:** It addresses a card application's unavailable **payment-network route**, especially where multi-application cards might otherwise choose a local method by default (raw lines 19–34). Adyen's platform and then the terminal temporarily mark the affected application. This is distinct from a broken local POS-terminal LAN, Wi-Fi, cloud WebSocket, credential issue, generic request circuit breaker, or proof that a payment was authorized. The page is a dated 2022-last-modified snapshot fetched in 2026.

**Route:** [[index]] → [[adyen-index]] → [[adyen-terminal-api]] → [[source-adyen-docs-point-of-sale-error-scenarios-penalty-box]] → [[raw/adyen/docs/point-of-sale/error-scenarios/penalty-box/2026-09-15]] (catalog promotion pending).

## 2. Routing, test outcome, and warnings

**Query:** What happens to a penalized application, and how is the test scenario interpreted?

**Answer:** On an authorization attempt the terminal learns the platform application state and temporarily marks it. It checks offline EMV, then Store and Forward; if offline is unavailable and another application exists, it chooses that application. A single-branded card attempts authorization in case the outage has cleared, then conditional offline processing. No alternative and no offline path means decline (raw lines 32–48). On a test terminal/card, suffix 158 creates an initial decline and a four-hour test-terminal penalty; the response is Failure/Refusal with explanatory 235 AID banned and ERROR (lines 50–101, 142–143). POS code may use `ErrorCondition`, not `refusalReason`/`message`; no automatic retry of an unresolved payment is authorized by this page (line 101). An optional test webhook check expects `AUTHORISATION success=false`, reason `Application banned` (lines 135–140).

**Route:** [[index]] → [[adyen-index]] → [[adyen-terminal-api]] → [[source-adyen-docs-point-of-sale-error-scenarios-penalty-box]] → [[raw/adyen/docs/point-of-sale/error-scenarios/penalty-box/2026-09-15]] (catalog promotion pending).
