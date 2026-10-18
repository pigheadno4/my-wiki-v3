# Retrieval probes — Capital Terms of Service

Q1. What must a platform generate, present and record before Adyen pays out a Capital grant, and who signs for an organization?

Forward route: [[adyen-index]] → [[adyen-capital]] → `## Sources` → [[source-adyen-docs-capital-terms-of-service]] → [[raw/adyen/docs/capital/terms-of-service/2026-09-15]].

Expected answer: Capital ToS can be accepted before or after an offer but before grant payout; determine required types for the main legal entity, generate `adyenCapital` with the chosen language/format, present the decoded document, then PATCH actual acceptance against its `termsOfServiceDocumentId` using an authorized individual signer's `acceptedBy` ID. A user may have multiple required documents. Raw locators: lines 19–23, 117–145, 180–219, 429–440; `## 2`–`## 5`.

Q2. Does a test Terms-of-Service response or completed acceptance establish a Capital grant payout or live capability state?

Forward route: [[adyen-index]] → [[adyen-capital]] → `## Sources` → [[source-adyen-docs-capital-terms-of-service]] → [[raw/adyen/docs/capital/terms-of-service/2026-09-15]].

Expected answer: No. The guide says test status returns only `adyenForPlatformsAdvanced` under default configuration; live returns actual required types. Its three-type status JSON is illustrative. Its `2_902` webhook example uses `sendToTransferInstrument`, not a Capital `receiveGrants` observation. Acceptance can be read back by main entity, signer, type and record ID, but the page's statement that required acceptance enables `receiveGrants` is not evidence of an actual grant offer, disbursement or funds receipt. Raw locators: lines 19, 63–115, 119–135, 443–445, 589–613; `## 1`, `## 2`, `## 6`.
