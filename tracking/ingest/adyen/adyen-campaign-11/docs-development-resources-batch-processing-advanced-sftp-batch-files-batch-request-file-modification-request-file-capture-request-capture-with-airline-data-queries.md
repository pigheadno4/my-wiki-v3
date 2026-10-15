# SFTP airline-data capture request retrieval checks

## Q1 — Purpose, scope, and non-inference

**Query:** Does this airline-data page create a new authorisation or show a successful capture, and what can its example actually establish?

**Expected route:** `[[adyen-index]]` → `[[adyen-batch-processing]]` → `[[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-modification-request-file-capture-request-capture-with-airline-data]]`; pinned raw `# Capture with airline data` lines 14–18, `### Airline` lines 24–28, and sample lines 51–65.

**Expected answer:** This is a batch request-file guide for appending airline sub-lines to a Capture request. The sample has an `FH` file type of `Modification`, an `L` transaction type of `Capture`, and an `SL,1,Capture` record followed by airline fields. The body says the airline sub-lines may also accompany authorisations, but the page does not document a new authorisation here. The sample is not an ACK, result file, webhook, capture success, or settlement proof.

## Q2 — Central capability, prerequisites, warnings

**Query:** Which airline records become necessary when airline data is supplied, and which counters or numbers must not be mistaken for payment references?

**Expected route:** Same source; raw `### Airline` lines 24–65, `### AirlineLeg` lines 67–111, and `### AirlinePassenger` lines 113–153. The source entry has an unread navigation link to the dedicated capture-request field guide for the Capture reference and amount/exponent schema.

**Expected answer:** Airline data itself is optional for capture; once included, the file needs at least one leg and at least one passenger sub-line. `SL` sub-line numbers increment within the parent line, while leg and passenger identifiers separately start at 1 and increment; the airline ticket number and file sequence are other distinct values. The sample's Capture sub-line shows a numeric value followed by `100,2,EUR`, but this page does not define that numeric value's PSP-reference role or the full Capture requiredness schema. Do not use an airline ticket, counter, or other example field as the authorisation/capture reference without the dedicated guide. Airline format/character limits are linked out, and the page gives no processing outcome.
