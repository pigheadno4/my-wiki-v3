# Fixed retrieval answers — docs-point-of-sale-user-manuals-v400m-with-bt-base

## 1. How should a new V400m be connected to its Bluetooth Ethernet base?

**Purpose and scope:** The pinned 2026-09-15 manual is a V400m device setup guide for a Bluetooth base station, not a general Terminal API or mobile-reader setup guide.

**Capability:** The base carries Ethernet LAN access to the V400m while docked or undocked and charges it while docked. For first setup, inspect the shipment and terminal, charge the battery, temporarily connect the terminal to Wi-Fi, board it to the selected store, and only then dock and pair with the base. The base gets software from the terminal; docking before boarding can leave the base stuck. Power the base, use its marked LAN port, match its serial number during Bluetooth pairing, and verify terminal/base IP addresses. If the POS uses local communications, update it to the terminal's Bluetooth IP address.

**Prerequisites and warnings:** The manual says boarding can take up to 30 minutes, or the boarding option may await a later synchronization. DHCP assignment and a POS restart may take additional time. Do not treat pairing as evidence of a completed payment. A failed tamper or serial check calls for immediate Adyen Support contact.

**Retrieval route:** [[source-adyen-docs-point-of-sale-user-manuals-v400m-with-bt-base]] → `Get started`, `Inspect the terminal`, and `Set up the base station and the Bluetooth connection` in [[raw/adyen/docs/point-of-sale/user-manuals/v400m-with-bt-base/2026-09-15|pinned raw]]. The payment-terminal hardware hub and provider catalog route are pending coordinator promotion.

## 2. What does the manual say about diagnostics, access and upkeep after boarding?

**Purpose and scope:** These are V400m on-device operating and care instructions from a dated manual. A Successful status reports the corresponding diagnostic result at test time; it does not establish continued connectivity or current model availability.

**Capability:** The manual separates PSP connection diagnostics from integrated POS Terminal API and endpoint diagnostics; the POS check is skipped for standalone use. Device info and Diagnostics need no passcode, while Network, Software, Configuration and Power require Admin & Settings credentials; transaction and refund actions have their own passcode conditions. The terminal can display/print/reset a Totals report and reprint a transaction receipt from History.

**Prerequisites and warnings:** A Successful PSP connection status reports platform connectivity at that test time; for an integrated POS, Successful Terminal API and Endpoints statuses report those checks at their test times. They do not establish continued connectivity, payment authorization or settlement. Resetting Totals starts a new period and removes the previous period's totals from the current display, while the immediately previous report remains accessible. Inspect stored batteries for damage, and do not return a faulty battery in the terminal package because of leakage and thermal-discharge risk. Cellular failover and menus have version/date qualifications, including possible inactive SIM subscriptions on terminals boarded before 2022.

**Retrieval route:** [[source-adyen-docs-point-of-sale-user-manuals-v400m-with-bt-base]] → `Test the payments platform connection`, `Test the POS system connection`, `Payment terminal menus`, `Maintain battery performance`, and `View, print, and reset totals` in [[raw/adyen/docs/point-of-sale/user-manuals/v400m-with-bt-base/2026-09-15|pinned raw]]. The provider catalog route is pending coordinator promotion.
