# Fixed retrieval answers — docs-point-of-sale-android-terminals-deploy-apps-upload

## Query 1: How do I upload an Android terminal app, and does Ready mean it is deployed?

**Purpose and scope.** This dated guide covers signed APK upload to Adyen for Android payment terminals in Terminal API or standalone in-person integrations. Upload precedes a separate installation step.

**Capability and prerequisites.** Prepare a signed APK. For Customer Area upload, use Devices > Terminal apps > Apps with the Merchant POS Terminal Management Admin role; ask Adyen Support if Upload app is absent. For Management API upload, use an API credential and key with Management API—Android files read and write; POST a required multipart APK file to /companies/{companyId}/androidApps, with optional description. A cloud Terminal API key may be reused only if it has the required role. The snapshot lists 700 MB test and 200 MB live maximum APK sizes. Save the returned app id if scheduling an install or uninstall through API.

**Warnings and limits.** Processing means Adyen is signing and converting the app; Ready means this conversion has finished and the app is ready for installation. An install must then be scheduled or performed by an API action, profile or Customer Area route. Ready alone is not evidence of installation on a terminal, app review or approval, certification, merchant eligibility or successful payment execution. The guide lists separate Error and Invalid recovery routes. Live Android-file Management API requests are rate-limited. A 51st uploaded version deletes the oldest of the 50 stored versions automatically; an unused app older than two years is also deleted automatically. The merchant accepts full responsibility and liability for third-party app consequences.

**Retrieval route.** Catalog pending: [[source-adyen-docs-point-of-sale-android-terminals-deploy-apps-upload]] → [[adyen-android-terminals]] → [[raw/adyen/docs/point-of-sale/android-terminals/deploy-apps/upload/2026-09-15]]. Use raw lines 15–39 for scope/roles/warnings, 41–58 for signing, 60–112 for upload and status, 255–256 for id, and 446–451 for storage deletion.

## Query 2: When and how is an Android terminal app certificate uploaded, and what restrictions apply?

**Purpose and scope.** The same guide treats certificates as optional app dependencies: upload a certificate if the app requires one, and replace it before its validity period expires. Certificate upload and terminal installation are separate.

**Capability and prerequisites.** Customer Area upload uses the Certificates tab and a .pem or .cert file. Management API upload uses an API credential and key with the Android files read/write role; POST /companies/{companyId}/androidCertificates with required multipart .CRT or .PEM file and name, optional description, and a 100 KB maximum file size. Save the returned certificate id for later API scheduling of installation or removal.

**Warnings and limits.** The 2026-09-15 guide says certificate installation on P630 and M450 terminals is not yet supported. It also subjects live Android-file Management API requests to rate limits. A certificate showing Ready in Customer Area is an upload status, not proof of installation on a terminal or successful secure communication. Check current hardware, role, account, and API conditions before a live operation.

**Retrieval route.** Catalog pending: [[source-adyen-docs-point-of-sale-android-terminals-deploy-apps-upload]] → [[adyen-android-terminals]] → [[raw/adyen/docs/point-of-sale/android-terminals/deploy-apps/upload/2026-09-15]]. Use raw lines 27–39 for roles and hardware limits, 258–299 for certificate conditions/body, and 443–444 for the returned id.
