# Fixed retrieval checks — docs-point-of-sale-user-manuals-nyc1

## Query 1: How does an NYC1 reader work with an Android or iOS POS app, and how should staff connect it?

**Purpose and scope:** NYC1 is a separate mobile card reader; the POS app on the Android or iOS mobile device starts the transaction and displays the screens, while the shopper taps, inserts, swipes or presents a wallet at the reader. This manual describes reader operation, not an Android app running on an Adyen payment terminal or an online-checkout SDK integration.

**Capability and prerequisites:** Pair over Bluetooth from the POS app, select the reader by serial (or barcode on iOS), and confirm by pressing the reader power button twice and accepting the pairing prompt. The mobile device connects to only one reader at a time but can retain multiple pairings. A USB-C link is only described for Android devices with USB host mode and POS-app USB permission. The mobile device needs Wi-Fi or cellular access when payments cannot proceed because of network connectivity. The guide instructs a physical/security inspection before use.

**Warnings and do not infer:** Do not pair through the mobile OS settings; those settings are used to forget a pairing. The manual does not set mobile OS minimums, SDK versions, all-country availability or current merchant eligibility. The manual labels a green reader LED as “Transaction is approved”; a connection or local setup step does not establish payment outcome, and this manual does not establish settlement or a particular backend record. If physical/tamper checks fail or tamper LEDs appear, stop using the reader and contact Adyen Support.

**Retrieval route:** [[index]] → [[adyen-index]] → proposed [[adyen-mobile-card-readers]] → [[source-adyen-docs-point-of-sale-user-manuals-nyc1]] → `[[raw/adyen/docs/point-of-sale/user-manuals/nyc1/2026-09-15]]`, especially raw lines 47–126 and 297–324. The concept and C06 source/index routes await coordinator promotion.

## Query 2: What do the NYC1 manual's PIN, power, update and repair/return statements actually establish?

**Purpose and scope:** This is a 2026-09-15 snapshot of a NYC1 reader user guide. It gives staff operational steps and a US-specific PIN model distinction; it does not provide a repair or return process.

**Capability and prerequisites:** In the US, the app labels a PIN-capable reader `NYC1` without a model, while `NYC1-SCR` is unsuitable for PIN. Supported PIN entry appears on the mobile device in a randomly placed pad. The guide asks for at least 1.5 hours' initial charging and specifies the supplied USB-C cable and a 5V DC, 1A charger; the battery is not replaceable. Mandatory reader/Bluetooth updates need the POS app kept open, prevent other mobile-device use while running, and reboot/reconnect the reader afterward. Bluetooth updates require an active Bluetooth link.

**Warnings and do not infer:** Do not extend the US PIN label rule to every region or NYC1 device. Update durations in the table are estimates. A nonreplaceable battery does not define a merchant self-repair or Adyen return policy; the manual only directs failed inspection/tamper cases to Support and mentions an Orders & returns Customer Area screen for serial/delivery verification. Current country support, OS minimum, warranty, repair, replacement, payment security certification and successful payment execution require separate evidence.

**Retrieval route:** [[index]] → [[adyen-index]] → proposed [[adyen-mobile-card-readers]] → [[source-adyen-docs-point-of-sale-user-manuals-nyc1]] → raw lines 147–258 for PIN/power/updates, 47–62 and 287–324 for inspection/tamper. The dock and Android/iOS build pages are linked navigation only from this read.
