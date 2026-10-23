# C30 VX820 Duet manual retrieval checks

## Q1 — Main purpose and prerequisites

**Question:** What does the historical VX820 Duet manual hub cover, and what setup steps does its quickstart name?

**Answer:** It is a VX820 Duet payment-terminal getting-started hub (raw lines 15–17) captured 2026-09-15 and last modified 2021-03-25 (raw lines 2, 11). Its quickstart names connecting the power supply cable and Duet base, connecting the base to the Internet through ETH, placing paper, conducting a device security inspection and boarding (raw lines 23–32). The components list identifies the VX820 PED, Duet printer base, power supply, privacy shield, Ethernet dongle and paper roll (raw lines 40–47). Route: [[index]] → [[adyen-index]] → [[adyen-payment-terminals]] → [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-duet-user-manual]] → [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx820-duet-user-manual/2026-09-15]].

## Q2 — Material boundary or failure

**Question:** What can go wrong with cabling or Internet access, and does this hub establish current transaction support for VX820 Duet?

**Answer:** The page warns that a cable in the wrong port, such as Ethernet in RS232, might severely damage the device (raw line 34). A top-bar exclamation means it holds data that failed to synchronize with Adyen because outgoing Internet access was absent (raw line 38). It also says new terminals of this type cannot be ordered (raw line 19). The separately captured eVo deprecation table explicitly groups VX820 and VX820 Duet, listing 29 March 2024 as “No more transactions” (deprecation raw lines 32–35); the separate migration section says that after 31 March 2024 it will no longer be possible to make transactions through a classic library (deprecation raw line 52). The quickstart is no proof of live processing, synchronization recovery or settlement. Route: [[index]] → [[adyen-index]] → [[adyen-payment-terminals]] → [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx820-duet-user-manual]] → [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx820-duet-user-manual/2026-09-15]].
