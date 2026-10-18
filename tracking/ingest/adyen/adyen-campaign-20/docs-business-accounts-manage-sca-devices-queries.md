# Query checks — Manage SCA devices

## Q1 — Purpose and prerequisites

**Query:** What does this Business Accounts guide let a platform do with SCA devices, and which credential role is required?

**Answer:** In this 2022-modified, 2026-09-15-captured guide, an already registered SCA device can be listed for a specified business account, associated with additional payment instruments through a client authentication challenge, or deregistered from a specified business account. The API credential needs Bank SCA Webservice Role. The guide does not establish current availability or a successful operation for a particular user.

**Evidence:** Raw lines 15–31 state purpose and role; lines 33–45 specify the list; lines 260–266 start the association; lines 904–922 specify removal. Route: [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-manage-sca-devices]] → [[raw/adyen/docs/business-accounts/manage-sca-devices/2026-09-15]].

## Q2 — Material boundary, failure and conflict

**Query:** Can one device authenticate for several business accounts, what blocks association, and does deleting it remove every association?

**Answer:** The guide permits up to five payment instruments per association request and says each instrument can link to only one device. The POST returns sdkInput for a client challenge; the PATCH must use the same device ID and instrument IDs with the resulting sdkOutput. The documented 422 'Device limit reached' means one or more IDs is already linked, calling for inspection and deregistration before retry. 'Challenge not found' usually involves a mismatch between the challenge's client device and PATCH device ID or wrong-device sdkOutput. DELETE takes both device ID and paymentInstrumentId; multiple business-account associations require a separate request for each account. The GET section's SDK code samples invoke registration rather than GET, so they conflict with its prose/curl and are not reliable GET templates.

**Evidence:** Raw lines 260–266 and 474–579 describe the association and challenge; lines 817–817 describe readback; lines 835–902 describe errors; lines 904–922 and 1075 describe deletion and 204. The GET mismatch is at lines 33–55 versus 58–220. Route: [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-manage-sca-devices]] → [[raw/adyen/docs/business-accounts/manage-sca-devices/2026-09-15]].
