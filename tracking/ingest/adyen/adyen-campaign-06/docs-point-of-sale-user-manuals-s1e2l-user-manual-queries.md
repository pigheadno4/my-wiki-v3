# Fixed retrieval checks — docs-point-of-sale-user-manuals-s1e2l-user-manual

## Query 1: What does the S1E2L manual require for first use and cellular fallback?

**Purpose and scope:** This is the S1E2L payment-terminal operating manual captured 2026-09-15, with source metadata last modified 2024-12-16. It covers physical inspection, charging, language/network setup and store confirmation. The separate Android-terminals overview lists S1E2L in a dated model table; neither source establishes present-day account/device eligibility.

**Capability and prerequisites:** Inspect the shipping seal, serial numbers and terminal for tampering, contacting Support immediately if a check fails. First setup charges the battery at least four hours, connects the terminal to the network and confirms the displayed store. If the store screen is missing, the manual says wait for the next synchronization (on average three hours) and try again. The S1E2L page describes Wi-Fi and cellular failover; it notes that a terminal boarded before 2022 might not have an active SIM if there was no SIM subscription then.

**Warnings and do not infer:** The eSIM statement is conditional and historical. It does not prove that this merchant's SIM is active, that every outage is recoverable, or that any payment succeeds. The page does not provide current regional availability, Android/firmware certification or an account-specific live setup result. A failed physical inspection requires Support escalation.

**Retrieval route:** [[index]] → [[adyen-index]] → [[adyen-android-terminals]] → [[source-adyen-docs-point-of-sale-user-manuals-s1e2l-user-manual]] → `[[raw/adyen/docs/point-of-sale/user-manuals/s1e2l-user-manual/2026-09-15]]`, raw lines 30–99. The C06 source/index link is pending coordinator promotion.

## Query 2: What are S1E2L battery, menu-passcode, totals and airplane-mode limits?

**Purpose and scope:** The manual is an operator guide for this device model. It describes staff menu gates and device maintenance, not shopper PIN capability or a settlement ledger.

**Capability and prerequisites:** Adyen asks for its supplied USB-C cable and region-specific plug. Long storage can harm the battery; inspect stored batteries periodically. For battery failure, the page points to a separate return/replace guide and says to dispose of a faulty battery under local rules and omit it from the terminal return package because of leakage/thermal-discharge risk. Menu actions have distinct gates: some Settings views need no passcode, Network/Configuration/Apps/power and software-version actions need Admin & Settings, Transactions actions need their passcode, and a refund also needs the Refunds passcode. The Totals report covers amounts since reset; reset begins a new period. Airline airplane mode needs Support enablement and turns off Wi-Fi, Bluetooth and cellular until switched off.

**Warnings and do not infer:** The menu's standalone and MOTO/MKE options do not establish that these transactions are enabled for this merchant or prove shopper PIN support. The report is terminal totals, not confirmed settlement. The linked return/replace and battery-management guides must be read for their full procedure. Airplane mode disables connectivity; do not treat it as an offline-payment authorization method. Current device, region, software and payment eligibility require separate verification.

**Retrieval route:** [[index]] → [[adyen-index]] → [[adyen-android-terminals]] → [[source-adyen-docs-point-of-sale-user-manuals-s1e2l-user-manual]] → raw lines 115–152, 154–258. The page links to return/replace, menu access and kiosk guides for detail beyond this read.
