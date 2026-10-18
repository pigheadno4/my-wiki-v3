# Query checks — Adyen Business Accounts OAuth flow

## Q1 — actor, purpose and prerequisites
**Question:** Who uses the captured OAuth flow to access an Adyen Business Account holder's data, and what are its required stages?
**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-oauth-flow]] → [[raw/adyen/docs/business-accounts/oauth-flow/2026-09-15]].
**Expected answer:** A third-party provider after Adyen open-banking onboarding seeks explicit holder consent (raw lines 19–26). The client redirects the holder through `/bankoauth/authorize` with requested scope, PKCE S256 and state; the holder returns an authorization code (lines 28–45, 51–85). The server exchanges it through `/token` with code verifier and Basic client authentication, then uses the access token in a separate `POST /consents` request for `consentId` (lines 96–123, 150–183). This is open-banking Business Account access, distinct from Adyen Partner OAuth merchant delegation and the external-individual verification route.

## Q2 — consent failure and token boundaries
**Question:** Does a returned access token or `consentStatus: received` prove approved consent or payment initiation, and what expiry/retry cautions apply?
**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-oauth-flow]] → [[raw/adyen/docs/business-accounts/oauth-flow/2026-09-15]].
**Expected answer:** No. The account holder's approval is separately required (raw line 152), and the illustrated consent response is merely `received` (lines 183–205). Payment initiation depends on actual granted scope/consent (lines 32–45, 63–67). Authorization code expires after five minutes (line 85), access token defaults to 24 hours (lines 125–131), and refresh tokens rotate and are one-time-use; losing one requires redirecting the holder again (lines 131, 148). The page conflicts on refresh expiry timing: immediate on use versus a short grace period (lines 131 and 237), so it cannot establish a reliable retry grace window. Its consent table states up to 90 days and 10 uses/day (lines 154–162).
