---
title: "Adyen Management API: Update company terminal settings"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/terminalSettings"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/companies/(companyId)/terminalSettings/2026-11-05.md"
tags: [adyen, management-api, terminal-settings, company-accounts]
---

## Overview

The captured Management API `PATCH /companies/{companyId}/terminalSettings` updates payment terminal settings for the company identified by the required path `companyId`. Company settings apply to its terminals unless merchant-account, store or terminal settings override them. The pinned reference lists the v3 TEST server `https://management-test.adyen.com/v3` and says live requests have rate limits, without giving figures here. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- The API credential needs Management API—Terminal settings read and write. Sensitive settings additionally require Management API—Terminal settings Advanced read and write. The reference does not identify every sensitive field in this raw.
- Include the full object containing a parameter to change it, even if other parameters in that object are unchanged. To restore a parameter inherited from the Adyen PSP level, include its full containing object and set the parameter to an empty value or omit it. Objects absent from the PATCH request are not updated. Do not treat an omitted nested parameter and an omitted top-level object as the same operation.
- The optional request body groups cover receipts, connectivity and Terminal API URLs/keys, DCC, gratuities, hardware/home screen, kiosk/localization, MOTO, offline processing, passcodes, pay-at-table, payment, refunds, signature, standalone, store-and-forward, surcharge, Tap to Pay, terminal instructions, timeouts and Wi-Fi profiles. Detailed field rules and units remain in the raw schema. In particular, `connectivity.simcardStatus` is terminal-level only on supported cellular models, despite appearing in this schema.
- Material conditions include contacting Adyen before the first `payment.contactlessCurrency` update for a compliance check; DCC receipt/terms responsibility; full liability for fraudulent or duplicate unreferenced refunds, with Adyen recommending limits and delay; and configured or inherited `storeAndForward.maxAmount`, `maxPayments` and `supportedCardTypes`. Wi-Fi profile entries have required nested `authType`, `bssType`, `ssid` and `wsec`; surcharge configuration entries have required nested `brand` and `currencies`. These are conditional child requirements under optional parents.
- The 200 response describes terminal settings using optional groups. It reports a successful request, not confirmed application on every device, a working Terminal API integration, regulatory approval, payment authorization, capture or settlement. The example responses include other settings beyond the narrow Wi-Fi request examples and are illustrative.

## Detail locators

- Scope, precedence, full-object/reset/omission rules, roles, live rate limits and TEST server: raw lines 5–33.
- Optional request groups and field rules: raw lines 36–196. See DCC (46–47), gratuity limits (48–52), hours (53–56), terminal-only SIM (41–45), MOTO (68–70), encryption key (71–78), contactless currency (104–105), unreferenced refunds (130–134), store-and-forward (145–155), surcharge (156–165), Wi-Fi nested requirements (172–196).
- Wi-Fi request examples: raw lines 198–288. 200 response schema: raw lines 289–454. Error schemas for 400, 401, 403, 422 and 500: raw lines 457–554. Illustrative response examples: raw lines 556–787.
- The pinned reference does not document an idempotency key, per-terminal propagation timing, reversal procedure or payment result for this PATCH.

## Related

- [[adyen-terminal-management]]
- [[adyen-api-access]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/terminalSettings/2026-11-05|Adyen Management API company terminal settings PATCH, captured 2026-11-05]]
