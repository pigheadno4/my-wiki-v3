# Fixed retrieval answers — docs-point-of-sale-android-terminals

## Query 1: What are Adyen Android terminals, and how can payments be started on them?

**Purpose and scope.** The pinned Adyen overview describes Adyen-provided Android payment terminals that run Android apps and accept in-person payments. Its scope is Android terminals used with a Terminal API or standalone integration.

**Capability.** Payments can start from an Android POS app installed on the terminal, a POS app on a different device, or directly on a model that supports standalone operation without a POS app. The terminal-app route is distinct from a merchant phone using Mobile SDK and from the GitHub Adyen Android online-checkout SDK.

**Prerequisites and warnings.** The overview does not say every model supports every initiation mode. A separate POS app is optional only for an eligible standalone model. Model and regional availability must be checked in the live Customer Area; this 2026-09-15 raw snapshot does not prove current eligibility, certification, firmware support or a successful payment.

**Retrieval route.** Catalog entry pending coordinator promotion: [[source-adyen-docs-point-of-sale-android-terminals]] → [[adyen-android-terminals]] → [[raw/adyen/docs/point-of-sale/android-terminals/2026-09-15]]. Use raw lines 19–35 for identity, payment modes and integration scope; lines 46–66 for models and regional warning.

## Query 2: How does an Android app become available on Adyen payment terminals, and which terminal models are listed?

**Purpose and scope.** This is a terminal-app onboarding overview for Adyen-provided Android payment terminals, not an app-store approval or device-certification decision.

**Capability and prerequisites.** The sequence is to check Adyen's linked app requirements, including specifications, permissions and security restrictions on debugging; upload the app to Adyen; then distribute it to terminals on a schedule, with profiles or by API requests. Detailed review, upload, deployment, role and API conditions belong to the linked guides, which this answer has not used as behavioral evidence.

**Warnings.** The dated model table lists AMS1, M450, P630, S1E, S1E Barcode, S1E2L, S1E4Pro, S1F2, S1F2 Barcode, S1F4Pro, S1U2 and SFO1. It gives Android versions and selected hardware attributes, including scanners on some models and a printer on S1F2 and S1F4Pro. S1F2/S1F2 Barcode Android 9 versus 10 depends on region. Adyen explicitly warns that not all listed models are available in all regions and directs readers to live Customer Area. Do not infer current OS/firmware version, inventory, app approval, account eligibility, feature parity or successful deployment from the table.

**Retrieval route.** Catalog entry pending coordinator promotion: [[source-adyen-docs-point-of-sale-android-terminals]] → [[adyen-android-terminals]] → [[raw/adyen/docs/point-of-sale/android-terminals/2026-09-15]]. Use raw lines 37–44 for the sequence, 46–66 for model details and warning, and 78–108 for navigation to detailed app, deployment and feature guides.
