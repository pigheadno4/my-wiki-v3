# Fixed retrieval answers — docs-point-of-sale-android-terminals-deploy-apps

## 1. What sequence does Adyen describe for deploying an Android app to a payment terminal?

**Purpose and scope:** The 2026-09-15 page is an overview of merchant-created Android app distribution to Adyen Android payment terminals, not a device-specific installation record.

**Capability:** Create an app that meets the separate app requirements, upload it through Customer Area, and let Adyen sign, convert and save it. If the app needs a certificate, upload that separately for signing/saving. Once signed and ready, make the app and applicable certificate available using Management API requests, condition-based Customer Area profiles, or Customer Area scheduling. The page says the app installs and becomes available when the terminal makes an automatic maintenance call.

**Prerequisites and warnings:** Upload and Adyen signing are distinct from terminal availability and installation. A chosen route alone does not prove a maintenance call or successful install. This overview does not specify approval, third-party ownership, version compatibility, credential roles or failures; use its detailed linked guides for those conditions and inspect actual device/action state.

**Retrieval route:** [[source-adyen-docs-point-of-sale-android-terminals-deploy-apps]] → `How it works` and `Next steps` in [[raw/adyen/docs/point-of-sale/android-terminals/deploy-apps/2026-09-15|pinned raw]]. Provider catalog route is pending coordinator promotion.

## 2. Does the page say every app needs a certificate or that a scheduled deployment is already installed?

**Purpose and scope:** This overview distinguishes optional certificate handling, availability scheduling and terminal installation.

**Capability:** Only if an app requires a certificate does the page direct the merchant to upload one. It lists API requests, profiles and Customer Area scheduling as ways to make signed apps/certificates available. Installation is tied to a later automatic maintenance call from the terminal.

**Prerequisites and warnings:** Certificate upload is conditional. A scheduled install, profile match or API request does not by itself prove the app reached a terminal. The overview does not provide approval-state, OS/version, role or third-party-app rules, and it does not show a particular payment or app runtime result.

**Retrieval route:** [[source-adyen-docs-point-of-sale-android-terminals-deploy-apps]] → `How it works`, lines 25–40, in [[raw/adyen/docs/point-of-sale/android-terminals/deploy-apps/2026-09-15|pinned raw]]. Follow the detailed upload, profile, API-action or Customer Area scheduling routes for their own conditions; provider catalog route is pending coordinator promotion.
