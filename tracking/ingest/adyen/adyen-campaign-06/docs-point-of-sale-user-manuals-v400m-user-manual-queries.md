# Fixed retrieval answers — docs-point-of-sale-user-manuals-v400m-user-manual

## 1. Can a merchant order a new V400m, and what does this manual say about existing units?

**Purpose and scope:** The 2026-09-15 Adyen V400m manual is a device setup and care source. Its discontinuation notice is a dated website statement, not a live stock or repair-service check.

**Capability:** The notice says V400m terminals are no longer available for new orders and that Adyen repairs existing units until April 2029. It recommends S1F2 or S1F4 Pro instead. Existing-unit setup runs through device inspection, charging, network connection, store boarding and connection diagnostics.

**Prerequisites and warnings:** Do not infer present stock, regional ordering eligibility, or a binding repair commitment from this snapshot. Inspect the delivered unit and tamper tape, compare serial numbers with the box and available Customer Area order, and contact Adyen Support immediately if a check fails. Boarding can take up to 30 minutes, and the option may await the next synchronization.

**Retrieval route:** [[source-adyen-docs-point-of-sale-user-manuals-v400m-user-manual]] → `V400m user manual`, `Get started`, and `Inspect the terminal` in [[raw/adyen/docs/point-of-sale/user-manuals/v400m-user-manual/2026-09-15|pinned raw]]. Payment-terminal hardware hub and catalog promotion are pending.

## 2. What network, SIM, diagnostics and maintenance conditions does the manual give for an existing V400m?

**Purpose and scope:** This is a physical-terminal operations guide for V400m, not proof of a merchant's current connectivity or payment state.

**Capability:** The terminal can connect over Wi-Fi; the manual describes cellular failover when internet access fails. After boarding, network changes require a passcode. For an old or defective physical SIM, power off, remove the battery and open the tray without metal tools. Use PSP connection diagnostics for Adyen-platform access and Terminal API plus Endpoints checks when integrated with a POS; skip that POS check for standalone use. The manual also covers menu credentials, power, battery care and Totals reporting.

**Prerequisites and warnings:** Units boarded before 2022 may lack an activated SIM subscription. A successful diagnostic does not prove payment authorization or settlement. Do not put a faulty battery in a terminal return package; reset of Totals starts a new reporting period, though the immediately previous period's report remains accessible. Menu structure may differ before software 1.90. The optional Bluetooth Ethernet base has a separate setup guide.

**Retrieval route:** [[source-adyen-docs-point-of-sale-user-manuals-v400m-user-manual]] → `Connect to your network`, `Replace physical SIM card`, `Test the payments platform connection`, `Test the POS system connection`, and `Maintain battery performance` in [[raw/adyen/docs/point-of-sale/user-manuals/v400m-user-manual/2026-09-15|pinned raw]]. Payment-terminal hardware hub and catalog promotion are pending.
