# Fixed retrieval answers — docs-point-of-sale-user-manuals-nyc1-with-dock

## Query 1: How do I connect the NYC1 reader through its dock or Bluetooth, and what charges in each mode?

**Purpose and scope.** This guide covers a separate NYC1 card reader controlled by an Android or iOS POS app on a mobile device. The dock charges the reader and supports a USB path between the reader and mobile device. It is not an Android payment terminal that runs the POS app on the terminal.

**Capability and prerequisites.** First inspect reader and dock for correct, untampered delivery. Charge the reader in the dock for at least 1.5 hours, using the supplied region-specific 12V/1.5A PD adapter. For USB, connect the dock power port to that adapter and the dock data port to the mobile device, place the reader in the dock, and allow the POS app's USB connection prompt. This arrangement charges the reader and mobile device. For Bluetooth, power the dock, enable Bluetooth, open the POS app, select the reader by serial number and confirm pairing by pressing the reader power button twice. The dock still charges the reader, but it does not charge the mobile device in Bluetooth mode. Initiate pairing in the POS app, not in system Bluetooth settings.

**Warnings and limits.** A mobile device connects to only one reader at a time, although it may have several paired readers. Bluetooth disconnects after five minutes of inactivity while the pair remains; a new payment reconnects to the last paired reader and may take longer while it wakes. Away from the dock, use the supplied USB-C cable and a 5V DC, 1A charger for the reader's non-replaceable battery. The mobile device needs Wi-Fi or cellular connectivity for payments.

**Retrieval route.** Catalog pending: [[source-adyen-docs-point-of-sale-user-manuals-nyc1-with-dock]] → [[adyen-mobile-card-readers]] → [[raw/adyen/docs/point-of-sale/user-manuals/nyc1-with-dock/2026-09-15]]. See raw lines 53–85, 89–169, 171–177, 219–230 and 350–369.

## Query 2: What physical safety, PIN and update restrictions matter for the NYC1 with dock?

**Purpose and scope.** These are physical reader and dock operations from the NYC1 user guide, with US-specific PIN identification and mode-specific update behavior. They do not establish account eligibility, app implementation, or successful payment execution.

**Capability and prerequisites.** Check tamper-evident packing, serial numbers on box and reader, and, when Customer Area access exists, the order serial and carrier delivery record; inspect reader and dock for tampering. In the US, an NYC1 device detail without a model indicates PIN support, while model NYC1-SCR indicates no PIN support. When supported, PIN entry appears on the mobile device at a randomized screen position. Reader, Bluetooth and dock software updates are initiated from the POS app's device view; keep the app open and do not switch apps until completion.

**Warnings.** Stop using a reader with a tamper indication, including white first and last LEDs, and contact Adyen Support immediately. A failed inspection also requires immediate Support contact. Bluetooth-functionality updates are available only through an active Bluetooth connection; the guide's table gives estimated durations, not a guaranteed service window. If a Bluetooth-dependent update fails for lack of a connection, follow the displayed reset instructions before retrying. The reader must be powered with the supplied dock adapter while docked; reader-only charging uses the supplied cable and a 5V DC, 1A charger.

**Retrieval route.** Catalog pending: [[source-adyen-docs-point-of-sale-user-manuals-nyc1-with-dock]] → [[adyen-mobile-card-readers]] → [[raw/adyen/docs/point-of-sale/user-manuals/nyc1-with-dock/2026-09-15]]. See raw lines 62–79 for inspection; 190–217 for PIN; 219–257 for power; 259–311 for updates; 340–377 for tamper and troubleshooting.
