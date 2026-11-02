# C63 coordinator full-read exemplar audit

**PASS** — all three predetermined exemplar sources and answers audited against full raw.

# C63 predetermined coordinator full raw reads

Root personally read model-visible numbered raw ranges, no output truncation:
- GET paymentLinks/(linkId):1–100,101–205,206–290,291–385 (EOF385, no final newline).
- POST payments/(paymentPspReference)/captures:1–100,101–190,191–310,311–420,421–573 (EOF573,no final newline).
- DELETE storedPaymentMethods/(storedPaymentMethodId):1–33.

GET link audit: TEST v72, required linkId only request; response required amount/currency/valueminorunits,id,merchantAccount,reference,status,url. Optional parents and nestedconditionalchildren, extendedfields/historicaldates notuniversalrequests. expiry70daymax/24hdefault, reusablefalse, active/expired/completed/paymentPending async shopperflow. Linkstatus/readback notcapture/settlement/bankreceipt. Payment/reference/link IDs distinct. Tokenstorage defaultdisabled with recurringmodel requirement foraskForConsent/enabled; metadata20pairs20keychars checkout.linkId overwritten; splitsClassicvsbalanceplatformscope; optionalpayment/nestedrequired, min3nonPIIshopperref, address, lineitemBNPL and3DS qualifiers allread. All400/401/403/422/500 schemas/examples read; generic422 returnURLmissing cannotturn optionalresponsefield intoGETrequiredinput. No idempotency/header/securityrecipe/deletion/propagationrule fromthispage. Rawresponse retrieval and detailroute appropriate.

Capture audit: authorizedpayment full/part; unclaimedpartial amount cancelled except enabledANDsupported multiplepartialcaptures. Mostmethodsautomaticdefault, no requestneeded, captureauto doesnotdoublecharge perraw. TESTv72 originalpaymentPSPref path, optionalIdempotencyKeymax64, amountcurrency sameasauthorization andvalue≤authorized, merchantAccountrequired. Optionalreference80; splitClassicaccountCodevsbalanceAccountId, pertypeconditionalaccount/amount/reference, facilitatorconditionalbranches, ESDschemaconditions read. CapturelineItems rows inexplicably sayrefundeditems/partialrefund; preserve scopedwarning no inventedcapture requirement.201contains capturedamount wording butstatusalwaysreceived andintroduction saysCAPTUREwebhookasyncoutcome; distinguishrequestPSPreference fromoriginalpaymentreference. AllrequestJSONbasic/platform/classic andall201responseexamples plus400/401/403/422/500schemas/examplesread; generic422 ReturnURLmissing doesnotestablishcaptureparameter. No settlement/bankreceipt or liveenablementproof; scope exactoperation.

DELETE audit: explicit token can no longerbeusedwithpaymentrequests, APIcredentialrole API tokenise paymentdetails. TESTv72. RequiredstoredPaymentMethodIdpath, merchantAccount/shopperReferencequery, min3nonPIIshopperref.204 actualstatus instruction, noresponsebody/errors/examples/authheader/idempotency/propagationdeadline/financialrollbackclaim. Deletion isdurable statedeffect, notgenericresourceexpiry orpaymentrefund.

Compared finalcanonicalsourcepages, exactquotes, approvedconceptreciprocalroutes and actualoriginalQ1Q2answers against fullraw. Allthree PASS; no materialpartial/fail andnoauditexpansion. Finalsource/answerhashes in exemplar-validation.json mustmatch atclose.
