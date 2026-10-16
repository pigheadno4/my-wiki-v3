# Fixed retrieval checks — docs-plugins-cegid-retail-y2-troubleshooting

## Q1 — Purpose, scope, and what not to infer

**Query:** What does the Cegid Retail Y2 troubleshooting page address, and what does it not prove?

**Answer:** It gives condition-specific checks for CPOS setup, PSP/merchant references, referenced refunds, DRV/DCPP paths, Global Blue, MOTO, TLS/Open Failed, local terminal URL, and Tap to Pay 403/903/store routing. It is a 2023-modified page captured 2026-09-15, not a live incident trace, verified fix, payment result, safe retry plan or generic cloud-network guide. Error examples and log payloads do not prove a particular payment was authorized. Evidence: raw lines 11, 15–35, 37–217. Canonical route: [[adyen-index]] → [[adyen-cegid-retail-y2]] → ## Sources → [[source-adyen-docs-plugins-cegid-retail-y2-troubleshooting]] → [[raw/adyen/docs/plugins/cegid-retail-y2/troubleshooting/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** How should one diagnose the main CPOS and Tap to Pay symptoms while preserving version and communication conditions?

**Answer:** A missing PSP reference calls for the payment-method **Authorisation number** setting; missing transaction ID or malformed reference calls for register allocation and number-length checks. Referenced refunds need **D:CP,RR**, not **D:CP,NR**. Following a changed install path, check DCPP/DRV log paths; Legacy Mode is suggested for pre-v18 Global Blue mapping, and CPOS handles MOTO without the Cegid Distant selling switch. CPOS v2.1.14 TLS 1.3 plus old Windows 10 can cause Open Failed; the page suggests a later plugin or Windows 22H2+. Only for local communication and unresponsive terminals, inspect the EPT `https://YOUR_DEVICE_IP:8443/nexo` URL. Tap to Pay 403 has stated connector URL/API-key causes; 903 is generic, prompting client-key and merchant-method checks. Store misrouting may stem from missing `storeID` or stale `/sessions` configuration; changes take effect at a new session, normally after 24 hours, without a manual reset method in this snapshot. None authorizes blind retry or proves a fix, and API keys should not be exposed through diagnostic sharing. Evidence: raw lines 37–113, 115–158, 199–217. Canonical route: [[adyen-index]] → [[adyen-cegid-retail-y2]] → ## Sources → [[source-adyen-docs-plugins-cegid-retail-y2-troubleshooting]] → [[raw/adyen/docs/plugins/cegid-retail-y2/troubleshooting/2026-09-15]].
