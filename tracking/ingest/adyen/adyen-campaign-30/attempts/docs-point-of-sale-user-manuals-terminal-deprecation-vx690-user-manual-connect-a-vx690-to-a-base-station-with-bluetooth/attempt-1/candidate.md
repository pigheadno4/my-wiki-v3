---
title: "Adyen VX690 Bluetooth base-station pairing (historical)"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/connect-a-vx690-to-a-base-station-with-bluetooth"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/connect-a-vx690-to-a-base-station-with-bluetooth/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, vx690, bluetooth, deprecation]
---

## Overview

This 2019-modified, 2026-09-15-captured [[adyen]] VX690 guide describes connecting the legacy terminal to a Bluetooth base station that uses Ethernet for its network connection. It is a model-specific setup procedure in the terminal-deprecation subtree. The separate [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation|eVo deprecation table]] lists VX690 under **29 March 2024 "No more transactions"**; this historical pairing guide does not establish current terminal support, boarding or payment execution. See [[adyen-payment-terminals]].

## Key takeaways

- **Network and reset preconditions:** The guide requires a DHCP network and instructs the operator to remove existing terminal Wi-Fi profiles through Admin-menu Wi-Fi reset. A PIN may be requested. The reset restarts the terminal; do not treat profile removal as a harmless scan. The base must be powered by mini USB and connected to the network through its ETH-marked Ethernet port. See pinned raw lines 18–35. The Admin-menu key is shown as an image; consult the raw image for its physical identity rather than inferring a label from its filename.
- **Pairing and status:** In the Admin menu, the historical path scans for a base, uses the base's pairing button to make it discoverable, selects the base by serial number, sets the connection and checks **Connection Status**. The stated connected indication is `Ethernet/BT` = `Connected`. These are guide steps and an expected local display, not observed pairing or payment readiness. See pinned raw lines 39–49.
- **One-to-one handling advice:** The guide says a paired terminal should remain paired with its base and advises labeling terminal/base pairs when several exist to avoid mixing them. See pinned raw line 37.

## Detail locators

- DHCP, Wi-Fi-profile removal, restart, power and Ethernet prerequisites: pinned raw lines 18–35.
- Base-station pairing menu path, serial selection, connection setting and status display: pinned raw lines 39–49.
- Persistent-pairing and multi-device labeling advice: pinned raw line 37.

## Related

- [[adyen-payment-terminals]] — physical-terminal and model context.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — separate dated eVo terminal cutoff.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx690-user-manual/connect-a-vx690-to-a-base-station-with-bluetooth/2026-09-15|VX690 Bluetooth-base guide, captured 2026-09-15]]
