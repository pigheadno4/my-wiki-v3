# Fixed retrieval answers — docs-point-of-sale-android-terminals-deploy-apps-profiles

## Query 1: How do Android profiles choose terminals and app versions?

**Purpose and scope.** This dated Adyen guide covers Customer Area profiles for apps installed on Adyen Android payment terminals in Terminal API or standalone integrations. It does not describe merchant-phone Mobile SDK deployment.

**Capability and prerequisites.** A user with Merchant POS Terminal Management Admin role first uploads an app to the company account and waits until it shows Ready. In Devices > Terminal apps > Profiles, the user defines applicability by selected stores, countries/regions, terminal models, or merchant accounts, then selects a Ready app and explicit version. Matching new, replacement, or migrated terminals can receive the app on boarding; later version choices flow to matching terminals when their configuration updates.

**Warnings and limits.** The detailed condition editor includes merchants even though the opening summary lists only store, country/region and model. If no condition is selected, the profile applies to all terminals in the company account. Two profiles cannot have the same set of conditions. A scoped example for S1E terminals in US stores does not establish current regional/model availability or app compatibility.

**Retrieval route.** Catalog pending: [[source-adyen-docs-point-of-sale-android-terminals-deploy-apps-profiles]] → [[adyen-android-terminals]] → [[raw/adyen/docs/point-of-sale/android-terminals/deploy-apps/profiles/2026-09-15]]. See raw lines 15–35 for purpose/role, 64–89 for conditions and default scope, and 91–105 for Ready/version selection.

## Query 2: When do profile changes install or uninstall apps, and what happens if I deploy manually or by API?

**Purpose and scope.** Profiles are part of Android terminal configuration. This answer concerns profile-driven on-terminal app state, not API request success or payment execution.

**Capability and prerequisites.** A terminal that is not boarded receives matching profile apps when boarded. A boarded terminal applies profile changes after its maintenance call; the changes can install or uninstall apps. Updating an already installed app while it is open closes the app. Editing profile conditions, changing an app version, adding an app, or removing an app requires saving the change in Customer Area.

**Warnings.** The guide says that app or certificate deployment via API calls or manually through Customer Area overwrites apps installed on a terminal based on its profile. It does not establish how long that override persists or the live state of an individual terminal. A profile save or Ready app status is not proof that installation, removal, app review, or a payment succeeded. Check actual device state and detailed deployment sources before operational action.

**Retrieval route.** Catalog pending: [[source-adyen-docs-point-of-sale-android-terminals-deploy-apps-profiles]] → [[adyen-android-terminals]] → [[raw/adyen/docs/point-of-sale/android-terminals/deploy-apps/profiles/2026-09-15]]. See raw lines 53–62 for board/maintenance/overwrite behavior and 107–122 for profile edit controls.
