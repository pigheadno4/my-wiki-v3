# Fixed retrieval answers — docs-point-of-sale-managing-terminals-board-terminal

## Query 1: Is assigning a terminal to a store enough to start taking payments, and how is it manually boarded?

**Purpose and scope.** The dated Adyen guide covers physical terminal registration for an assigned store in an integrated Terminal API or standalone setup. Assignment precedes boarding; the guide treats the terminal as ready for payments only after boarding.

**Capability and prerequisites.** The merchant account or store must have at least one payment method configured. Staff switch on the device, connect it to the internet if prompted, and use the display to confirm or select the intended store. Non-Android devices show Board the terminal and may show one or multiple stores; Android devices ask for language and can show a store confirmation or selection control. If the displayed store is wrong and cannot be changed on the device, reassign the terminal in Customer Area before boarding. The guide says boarding can take up to 30 minutes and the device may reboot.

**Warnings.** The guide's absent Board the terminal button on a non-Android device can mean it is already boarded; after a recent reassignment it advises waiting for platform synchronization, on average three hours, before retrying. An assignment request or store listing alone does not prove the physical device finished boarding, has the intended store active, or completed a payment. Current account, model and device state require live checks.

**Retrieval route.** Catalog pending: [[source-adyen-docs-point-of-sale-managing-terminals-board-terminal]] → [[adyen-terminal-management]] → [[raw/adyen/docs/point-of-sale/managing-terminals/board-terminal/2026-09-15]]. Use raw lines 15–37 for prerequisites and scope, 39–77 for both manual device procedures.

## Query 2: How does OTP boarding work, and what happens when a boarded terminal moves stores?

**Purpose and scope.** OTP boarding is an enabled physical-device workflow for eligible integrated terminals still in company or merchant inventory; standalone terminals use manual boarding. The merchant system performs Management API calls after staff read the device's OTP or barcode.

**Capability and prerequisites.** The terminal must run software 1.94 or later, have network access, and use an account/store with a configured payment method. Adyen Account Manager or Support must enable OTP boarding. The API credential/key needs Management API — Terminal actions read and Management API - Reassign terminal to an entity roles. Staff scan the barcode or enter the displayed OTP; the system calls GET /terminals with otpQuery to find the terminal id, then POST /terminals/{terminalId}/reassign with the intended unique store id. The guide says that assignment in this flow triggers automatic boarding and configuration download.

**Warnings.** If a previously boarded OTP terminal is moved to a different store, reassign it; otherwise it continues processing payments over the old store. Staff initiate Settings > Configuration > Reassign device on the terminal before the OTP-driven system calls. The device reboots, and when WebSockets are disabled reassignment can take up to three hours. This is distinct from the guide's general boarding duration. Versioned code examples and an API response do not prove that a real terminal has switched stores or executed a payment.

**Retrieval route.** Catalog pending: [[source-adyen-docs-point-of-sale-managing-terminals-board-terminal]] → [[adyen-terminal-management]] → [[raw/adyen/docs/point-of-sale/managing-terminals/board-terminal/2026-09-15]]. Use raw lines 25–37 for eligibility/roles, 79–103 and 270–300 for OTP steps/IDs, and 302–313 for reassignment risk and timing.
