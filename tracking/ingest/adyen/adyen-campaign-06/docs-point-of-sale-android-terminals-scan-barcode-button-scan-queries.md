# Fixed retrieval answers — docs-point-of-sale-android-terminals-scan-barcode-button-scan

## Query 1: Which Android terminals support the scan button, and where does the barcode go?

**Purpose and scope.** This dated Adyen guide covers a physical scan button on S1E Barcode, S1E2L, S1F2L and S1U2 Android payment terminals with barcode scanners. The button path is available in Terminal API or standalone integrations after Customer Area enablement.

**Capability and prerequisites.** Pressing the button activates the terminal scanner. If a scan succeeds, the terminal pastes the barcode text into an input box in an Android barcode-scanner app installed on that same terminal. The app needs an input text field to process the content.

**Warnings.** The page does not say that the button sends a Terminal API scan response to an off-device POS. Its separate single-scan and batch-scan links are navigation to other workflows. The named model list is a 2026-09-15 captured, 2025-02-06 modified snapshot; it does not prove current hardware availability, account configuration, app handling, scan success or payment execution.

**Retrieval route.** Catalog pending: [[source-adyen-docs-point-of-sale-android-terminals-scan-barcode-button-scan]] → [[adyen-android-terminals]] → [[raw/adyen/docs/point-of-sale/android-terminals/scan-barcode/button-scan/2026-09-15]]. Use raw lines 15–31 for models, input destination and app prerequisite; lines 57–60 for separate Terminal API navigation.

## Query 2: How is the scan button configured, and what do beep, separator, prefix and software-keyboard options require?

**Purpose and scope.** The guide describes Customer Area device settings for the named scanner-equipped Android terminals, with optional text-format and input-mode settings.

**Capability and prerequisites.** At In-person payment > Device settings > Device > Barcode scanner, add the setting, enable the barcode scanner button, and save. Scope can be company, merchant, store or terminal. Merchant POS Terminal Management Admin can configure any level; Merchant POS Terminal Management can configure merchant level and lower. An optional beep signals successful scanning. New line is the default separator; Custom accepts a chosen separator character.

**Warnings.** Prefix and software-keyboard event mode require Adyen Support enablement. For a prefix, provide the characters to prepend. In keyboard mode, the terminal emits barcode characters as individual keyboard events and the receiving Android app must listen for those events. This mode is distinct from pasting into a text input. The snapshot does not establish that Support has enabled it for a specific account or that a deployed app processes the events correctly.

**Retrieval route.** Catalog pending: [[source-adyen-docs-point-of-sale-android-terminals-scan-barcode-button-scan]] → [[adyen-android-terminals]] → [[raw/adyen/docs/point-of-sale/android-terminals/scan-barcode/button-scan/2026-09-15]]. Use raw lines 27–31 for role/hardware requirements and 33–55 for the exact configuration and Support-enabled options.
