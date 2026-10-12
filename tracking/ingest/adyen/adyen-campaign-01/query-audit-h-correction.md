# Adyen C01 query audit H — targeted correction verification

Job: `docs-online-payments-3d-secure-authorize-mpidata` (manifest position 40)

Review scope: targeted verification of the coordinator-applied source warning and Step 2 locator change only. No full raw or page reread; the previously approved purpose, scope, qualifications, routes, and unchanged prose remain outside this correction review.

## Evidence

- Manifest pin: `raw/adyen/docs/online-payments/3d-secure/authorize-mpidata/2026-09-15.md`, SHA-256 `c35fa6617aa89330f6b7723dba39c9da7d8670e9ab633bd720156389aeb17dbd`.
- Fresh SHA-256: `c35fa6617aa89330f6b7723dba39c9da7d8670e9ab633bd720156389aeb17dbd`; evidence is unchanged.
- Diff against the accepted attempt-1 candidate is limited to:
  1. a `Snapshot field-name conflict` warning at canonical source lines 37–38; and
  2. an expanded Step 2 detail locator at line 42.
- The warning matches the affected raw context: the Step 2 field table names `threeDS2RequestData.threeDSRequestorChallengeInd` at raw line 72; the co-badged guidance names `threeDSRequestorChallengeInd` at raw line 85; the Cartes Bancaires sample instead uses `threeDS2RequestData.challengeIndicator` at raw lines 121–123.
- The correction does not infer equivalence, normalize either field, or promote the sample to a current contract. It directs verification against the Checkout schema for the intended API version.

## Residual fixed-query verdict

**PASS within targeted correction scope.** The concrete query, “Which `threeDS2RequestData` JSON property should I send for the Cartes Bancaires challenge indicator?”, can no longer be answered from this snapshot as though it established one unambiguous property. The source now exposes the internal field-name conflict at the detail-retrieval route and preserves the required current-schema/version verification boundary.

No residual material issue remains from audit H's position-40 finding. No raw, concept, suggestion, provider index, company count, log, or aggregate catalog change is required by this correction. Aggregate close work remains deferred.
