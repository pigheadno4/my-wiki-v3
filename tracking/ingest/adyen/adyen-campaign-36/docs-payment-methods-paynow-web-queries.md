# docs-payment-methods-paynow-web — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is a PayNow **Web integration chooser** routing to Drop-in and Components child pages plus Web Sessions/Advanced main guides (source-adyen-docs-payment-methods-paynow-web; raw lines 15–36). It does not itself define QR creation/scanning, API or SDK versions, current merchant eligibility, test/live behavior or a final payment outcome (raw lines 19–36). The Components description is grammatically incomplete, so it does not identify an implementation class (raw line 27).

Q2. What is its central capability, prerequisite and warning?

It presents Drop-in as the all-in-one Web UI choice and separately links a Components child guide (raw lines 21–27). It says to build the main integration first and lists Sessions and Advanced base guides for both Web UI options (raw lines 29–36). The child guides are required for method-specific setup or outcome semantics; this navigation page is not payment-processing proof (raw lines 19–36).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paynow-web]] → [[raw/adyen/docs/payment-methods/paynow/web/2026-09-15]].
