## 26.15.0 2026-10-19

### CryptoOnramp (Alpha)
* [Changed] Apple Pay card previews now include the card funding type (Credit, Debit, or Prepaid), falling back to Card when unavailable, matching Link's formatting.
* [Changed] Renamed `CryptoOnrampCoordinator.fulfillKYCRequirement(from:)` to `fulfillKYCRequirements(from:)` and `FulfillKYCRequirementResult` to `FulfillKYCRequirementsResult`.

### Identity
* [Changed] Test-mode verification sessions now upload placeholder document and selfie images instead of users' images.

