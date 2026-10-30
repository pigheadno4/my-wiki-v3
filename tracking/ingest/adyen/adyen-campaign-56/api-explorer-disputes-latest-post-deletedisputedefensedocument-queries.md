# api-explorer-disputes-latest-post-deletedisputedefensedocument fixed retrieval check

Read log: entire pinned raw lines 1–119 read as one numbered, untruncated contiguous range. SHA-256 verified: d46b7a6d6ab6aeb9dd4b3ec4a9761b81b3780501631b81df70d58a4040f6c8c1.

Canonical source: [[source-adyen-api-explorer-disputes-latest-post-deletedisputedefensedocument]] — https://docs.adyen.com/api-explorer/Disputes/latest/post/deleteDisputeDefenseDocument

- Q1: For `Disputes/latest/post/deleteDisputeDefenseDocument`, what purpose, API/version and object identity does this captured page establish, and what central required/conditional inputs or prerequisites govern its use?
  - Answer: TEST Disputes API `DisputeService/v30` `POST /deleteDisputeDefenseDocument` deletes a specific earlier-supplied defense document (5–10). The request table requires document-type code, dispute-assigned PSP reference and merchant account code (14–19). `DefenseMaterial` is an example value, not a stated full enum (21–30). Whole-body requiredness is not separately stated.
- Q2: For `Disputes/latest/post/deleteDisputeDefenseDocument`, what does the documented response or failure establish, and which lifecycle, deletion/propagation, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?
  - Answer: The 200 body requires `disputeServiceResult.success` and may include `errorMessage`; the example has `success: true` (31–41, 108–119). This establishes request/service success for deleting that document, not propagation timing, defense acceptance, a won dispute or payment outcome. The page lists 400/401/403/422/500 errors but no error examples or retry contract (44–106). Its only listed server is TEST v30 (9–10), not proof of LIVE/current availability.
