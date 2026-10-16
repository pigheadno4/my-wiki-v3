---
title: "Cegid Retail Y2 CPOS troubleshooting"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/cegid-retail-y2/troubleshooting"
raw_files:
  - "adyen/docs/plugins/cegid-retail-y2/troubleshooting/2026-09-15.md"
tags: [adyen, cegid-retail-y2, point-of-sale, troubleshooting]
---

## Overview

Adyen's Cegid Retail Y2 CPOS troubleshooting guide (metadata last modified 2023-10-02; captured 2026-09-15) gives symptom-specific checks for CPOS payment references, refunds, logging, terminal communication and Tap to Pay on iPhone. These are diagnostic/remediation suggestions, not proof that a merchant's issue was fixed or a payment succeeded. The product scope and local-versus-cloud integration boundary are at [[adyen-cegid-retail-y2]].

## Key takeaways

- First check CPOS plugin setup, and Mobile POS or Live Store setup if the issue involves those integrations. Missing registered PSP reference points to the payment method's **Authorisation number** checkbox. Missing `GPE_TRANSACTIONID` points to cash-register **Allocation of transaction number**; malformed merchant reference can impair reconciliation when **Number length** is not greater than the prefix length (raw lines 19–52).
- If an attempted referenced refund defaults to unreferenced, check the EPT **Payment configuration**: **D:CP,RR** enables referenced refunds, while **D:CP,NR** causes unreferenced default. This explains a setting distinction, not refund completion or permission to repeat a payment (raw lines 54–61).
- After a Cegid Retail Y2 upgrade changes the installation path, reinstalling CPOS in the new location may be required; then verify **Logfile DCPP Layer** and **Logfile DRV Layer** paths. For Global Blue receiving `tenderReference` instead of `PSPReference`, the page limits its **Legacy Mode** mapping suggestion to Cegid versions earlier than 18. For unavailable MOTO, it says the CPOS plugin handles that flow and Cegid's **Distant selling** checkbox should not be selected (raw lines 63–91).
- An **Open Failed** error at transaction start may occur with CPOS v2.1.14's TLS 1.3 use on an outdated Windows 10 environment. The page proposes a later plugin version or Windows 22H2+ for that case. If a terminal is unresponsive under **local communications**, verify the register EPT URL `https://YOUR_DEVICE_IP:8443/nexo`; that URL check is local-specific and does not define a cloud endpoint (raw lines 93–113).
- For Tap to Pay on iPhone, a 403 can involve a Cegid `POSSDKY2ConnectorUrl`/`POSSDKApiKey` misconfiguration or API-key structure; the guide gives conditional correction/regeneration advice. The generic 903 calls for checking the web-service user's Client Key and merchant-account payment methods, not an identified single cause. Logs and example payloads at raw lines 123–195 are diagnostics, not authorization evidence; do not disclose credentials in support artifacts (raw lines 115–195).
- If transactions post to a merchant account rather than the intended store, check whether MPOS `storeID` is absent. If a `/sessions` store or merchant-account setting changed, the page says the change takes effect with a new session, normally 24 hours after the original; Cegid then had no manual reset method. Release-note checks are a further diagnostic step, not a proven fix or retry rule (raw lines 199–217).

## Detail locators

- CPOS setup, PSP/merchant references and refund configuration: raw lines 19–61.
- DRV/DCPP logging, Global Blue legacy mapping and MOTO: raw lines 63–91.
- CPOS TLS/Windows and local-terminal URL: raw lines 93–113.
- Tap to Pay 403/903 conditions and example logs: raw lines 115–195.
- MPOS store/session routing and release-note check: raw lines 199–217.

## Related

- [[adyen-cegid-retail-y2]] — Cegid CPOS integration concept and source route.
- [[adyen]] — provider page.

## Raw Sources

- [[raw/adyen/docs/plugins/cegid-retail-y2/troubleshooting/2026-09-15|Cegid Retail Y2 CPOS troubleshooting, captured 2026-09-15]]
