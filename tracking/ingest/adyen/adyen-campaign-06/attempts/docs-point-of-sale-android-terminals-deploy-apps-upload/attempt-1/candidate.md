---
title: "Adyen Android terminal app and certificate upload"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals/deploy-apps/upload"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/deploy-apps/upload/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, app-upload, certificates, management-api]
---

## Overview

This Adyen guide describes uploading a signed Android app APK, and an optional certificate when the app requires one, for Adyen-provided Android payment terminals. Upload lets Adyen sign and convert the app to a terminal-handled format; subsequent installation or removal is a separate action using terminal-action API requests, profiles or Customer Area scheduling. It applies to Terminal API or standalone in-person integrations with Android payment terminals. [[adyen]] [[adyen-android-terminals]] [[adyen-terminal-management]]

## Key takeaways

- The merchant can upload via Customer Area or the Management API. API use requires an API credential, API key and Management API—Android files read and write role; a cloud Terminal API integration may reuse its existing API key subject to that role. Customer Area upload requires Merchant POS Terminal Management Admin. If its Upload app button is absent, the guide directs the merchant to Adyen Support for enablement.
- Before app upload, create a signed APK. The guide instructs V1 (Jar Signature) selection when minSdkVersion is 23 or earlier, with V2 also recommended; when later than 23 it recommends V2. For API upload, POST the APK as multipart file to /companies/{companyId}/androidApps; file is required and description optional. This snapshot lists 700 MB test and 200 MB live APK limits. Keep the returned app id for later API scheduling. The displayed curl and SDK samples are examples with their own library versions, not a current contract guarantee.
- In Customer Area, Processing means Adyen is signing/converting the app and may take up to an hour; Error and Invalid have distinct troubleshooting routes in the raw. Ready means that conversion is finished and the app is ready for installation. It does not mean installed, merchant-approved, reviewed, deployed to a particular terminal or payment-tested.
- If an app needs a certificate, upload it separately and replace it before expiry. Customer Area accepts .pem or .cert; the API body accepts .CRT or .PEM multipart file plus required name and optional description at /companies/{companyId}/androidCertificates. The API certificate file limit is 100 KB. Save the returned certificate id for later API scheduling. This dated guide says installing certificates on P630 and M450 is not yet supported.
- Live Management API requests for Android apps/certificates are subject to rate limits. Customer Area stores at most 50 versions of one app: uploading a new version at that limit automatically deletes the oldest upload. Apps older than two years and not installed on any terminal are also automatically deleted. The guide assigns the merchant full responsibility and liability for consequences of uploading, installing or running third-party apps.

## Detail locators

- Upload-versus-install purpose, deployment routes and third-party liability: pinned raw lines 15–25.
- Integration, roles, live rate limits, version limit and P630/M450 certificate restriction: pinned raw lines 27–39.
- Signed APK preparation and conditional signing advice: pinned raw lines 41–58.
- Customer Area upload and status meanings: pinned raw lines 60–90.
- Management API app upload body, test/live limits, versioned sample code and returned id: pinned raw lines 92–256.
- Optional certificate, formats, role-dependent upload, API fields/size, sample code and returned id: pinned raw lines 258–444.
- Automatic oldest-version and unused-app deletion: pinned raw lines 446–451.

## Related

- [[adyen-android-terminals]] — Android terminal app and model hub.
- [[adyen-terminal-management]] — Management API fleet administration and role boundary.
- [[adyen-terminal-api]] — in-person payment messaging, distinct from Management API file upload.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/deploy-apps/upload/2026-09-15|Adyen upload apps and certificates guide, fetched 2026-09-15]]
