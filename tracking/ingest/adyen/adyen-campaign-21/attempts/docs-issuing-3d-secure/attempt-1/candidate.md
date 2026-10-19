---
title: "Adyen Issuing: Enroll cards in 3D Secure"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/3d-secure"
raw_files:
  - "adyen/docs/issuing/3d-secure/2026-09-15.md"
tags: [adyen, issuing, 3d-secure, authentication, sca]
---

## Overview

This Adyen Issuing guide (last modified and captured 2026-09-15) describes enrolling **Adyen-issued cards** for cardholder authentication during online payments. Adyen acts on the **issuer** side here; the processing merchant's **acquirer** appears separately in the guide's transaction-scope and exemption discussion. 3D Secure authentication is a step before the separate Issuing payment **authorisation** decision, not proof of an authorised or captured payment. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- **Conditional enrollment:** The captured guide says enroll an issued card in 3D Secure when **both** conditions hold: cards are issued within the EEA or UK, and they can be used for online payments within the EEA or UK. It frames the purpose as two-factor cardholder authentication under PSD2/SCA. The Issuing integration's API credential needs the **Bank SCA Webservice Role** to enroll cards. These dated statements are source scope, not a current legal determination for a particular program.
- **Issuer-side methods:** The guide offers password plus one-time password (OTP), using cardholder mobile phone and password data, or out-of-band (OOB) authentication after registering an eligible cardholder device. An enrolled OTP cardholder is prompted for password and phone OTP; an enrolled OOB cardholder completes the challenge in the platform's secure application with a passcode or biometrics. Enrollment and a completed challenge are different events.
- **Challenge versus payment outcome:** The page explicitly says not all EEA/UK online payments trigger 3D Secure. When an online payment is out of PSD2 SCA scope or exempt, Adyen does not require the OTP/password or OOB challenge and the payment proceeds to **authorisation**. Skipping a challenge is not an authorisation approval, and a passed authentication does not itself establish capture or settlement.
- **Scope and exemptions:** The page lists cards issued outside the EEA/UK, an **acquirer** based outside the EEA/UK, merchant-initiated recurring/subscription transactions (**excluding the initial setup transaction**), and MOTO as out of scope. It separately lists possible in-scope exemptions: low value, secure corporate virtual-card payment, and low-risk transaction risk analysis. Adyen may apply exemptions or the acquirer may request them; the guide directs readers to their Adyen contact to check applicability. Its EUR 30 / cumulative EUR 100 low-value thresholds are part of this dated snapshot, not a universal live rule.

## Detail locators

- Dated issuer-card enrollment conditions and SCA factor framing: pinned raw lines 19–32.
- Issuing integration role and OTP versus OOB enrollment methods: pinned raw lines 34–46.
- Challenge-free payments proceeding to separate authorisation: pinned raw lines 48–52.
- Out-of-scope issuer/acquirer geography, MIT initial-transaction exception, and MOTO: pinned raw lines 54–61.
- Conditional exemptions and low-value thresholds: pinned raw lines 63–69.

## Related

- [[source-adyen-docs-issuing-3d-secure-password-otp]] — card authentication data, OTP delivery and authentication outcomes.
- [[source-adyen-docs-issuing-payment-stages]] — later authorisation reservation and capture/debit stages.

## Raw Sources

- [[raw/adyen/docs/issuing/3d-secure/2026-09-15|Adyen Issuing 3D Secure enrollment, captured 2026-09-15]]
