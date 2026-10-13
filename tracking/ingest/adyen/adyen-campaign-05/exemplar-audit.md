# Adyen C05 coordinator full-read exemplars

- PASS — make-a-payment: all 311 raw lines and promoted source fully read. Preconditions, protocol/service/payment header, ServiceID versus merchant reference and terminal transaction ID, decimal amount, authorization/Partial response, async cloud delivery, status-check recommendation and test-only triggers retained.
- PASS — raw-acquirer-responses: all 203 raw lines read in untruncated chunks and promoted source fully read. Optional merchant opt-in and refusalReasonRaw placement, mandatory no-code-on-volatile-raw-string warning, mapped ErrorCondition/refusalReason/message, row-specific Customer Area statuses/actions, duplicate-check qualifier, scheme/context and no universal outcome/retry preserved.
- PASS — configuration-based surcharge: all 243 raw lines and promoted source fully read. Management API roles/scopes, terminal firmware gates/hardware exclusions, first-match configurations, minor-unit fees, unsupported commercial checks on Mobile/offline, disclosure/single tap, and MOTO/MKE double-charge opt-out retained; source snapshot is not current legal eligibility.

All three exemplars pass with no material partial/fail; no quality-audit expansion. Exhaustive structural checks remain required before closure.
