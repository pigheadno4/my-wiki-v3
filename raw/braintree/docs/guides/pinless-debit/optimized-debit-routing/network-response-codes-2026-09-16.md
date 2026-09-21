<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/pinless-debit/optimized-debit-routing/network-response-codes -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Network Response Codes
slug: /docs/guides/pinless-debit/optimized-debit-routing/network-response-codes/
createTime: '2025-04-02T02:05:19.338Z'
updateTime: '2025-04-02T02:05:19.390Z'
---



## Network response codes

In addition to the[processor response code](/braintree/docs/reference/response/transaction/ruby#processor_response_code)and text, some transaction objects include a[network response code](/braintree/docs/reference/response/transaction/ruby#network_response_code)and text.

These network response values are the raw responses that the card network may return, and when present they can provide additional detail about why a request was approved or declined. However, this information is supplemental to the processor response code. Consider the processor response code to be the source of truth.

Each card network has distinct response codes:


- [Accel](#card-network-accel)
- [NYCE](#card-network-nyce)
- [Pulse](#card-network-pulse)
- [Star, Star Acces](#card-network-star-star-access)
- [Maestro](#card-network-Maestro)

| Card Network | Code | Text |
| --- | --- | --- |
| Accel | 000 | Approved |
| Accel | 001 | Approved with identification |
| Accel | 002 | Approved for partial amount |
| Accel | 003 | Approved (VIP) |
| Accel | 100 | Do not honor (general denial) |
| Accel | 101 | Expired card |
| Accel | 102 | Suspected fraud |
| Accel | 103 | Card acceptor contact acquirer |
| Accel | 104 | Restricted card |
| Accel | 105 | Card acceptor call acquirer's security department |
| Accel | 106 | Allowable PIN tries exceeded |
| Accel | 107 | Refer to card issuer |
| Accel | 108 | Refer to card issuer's special condition |
| Accel | 109 | Invalid merchant |
| Accel | 110 | Invalid amount |
| Accel | 111 | Invalid card number |
| Accel | 112 | PIN data required |
| Accel | 113 | Unacceptable fee |
| Accel | 114 | No account of type requested |
| Accel | 115 | Requested function not supported (invalid transaction) |
| Accel | 116 | Insufficient funds |
| Accel | 117 | Incorrect PIN |
| Accel | 118 | No card record |
| Accel | 119 | Transaction not permitted to cardholder |
| Accel | 120 | Transaction not permitted to terminal |
| Accel | 121 | Exceeds withdrawal amount limits |
| Accel | 122 | Security violation |
| Accel | 123 | Exceeds withdrawal limit frequency |
| Accel | 124 | Violation of law |
| Accel | 126 | Invalid PIN block |
| Accel | 127 | PIN length error |
| Accel | 128 | PIN key synchronization error |
| Accel | 129 | Suspected counterfeit card |
| Accel | 130 | Transaction failed OFAC check |
| Accel | 131 | Check not acceptable |
| Accel | 180 | Limit exceeded due to cash back amount |
| Accel | 181 | Enter lesser amount |
| Accel | 182 | Institution not supported by switch |
| Accel | 183 | Balances not available for inquiry |
| Accel | 184 | Resubmission in violation of network rules |
| Accel | 185 | Stop Payment on check (shared branch only) |
| Accel | 200 | Do not honor |
| Accel | 201 | Expired card-Denial advice |
| Accel | 202 | Suspected fraud |
| Accel | 203 | Card acceptor contact acquirer |
| Accel | 204 | Restricted card |
| Accel | 205 | Card acceptor call acquirer's security department |
| Accel | 206 | Allowable PIN tries exceeded |
| Accel | 207 | Special conditions |
| Accel | 208 | Lost card |
| Accel | 209 | Stolen card |
| Accel | 210 | Suspected counterfeit card |
| Accel | 211 | Invalid card number |
| Accel | 214 | No account of type requested |
| Accel | 216 | Insufficient funds |
| Accel | 217 | Incorrect PIN |
| Accel | 400 | Accepted |
| Accel | 600 | Accepted |
| Accel | 601 | Not able to trace back to original transaction |
| Accel | 800 | Accepted |
| Accel | 880 | Key Change rejected-check value mismatch |
| Accel | 881 | Key Change rejected-local system problem |
| Accel | 882 | Key Change rejected-key change in progress |
| Accel | 883 | Declined-incorrect institution identifier |
| Accel | 900 | Accepted |
| Accel | 907 | Card issuer or switch inoperative |
| Accel | 908 | Transaction destination cannot be found for routing |
| Accel | 909 | System malfunction |
| NYCE | 00 | Approved or completed successfully |
| NYCE | 01 | Function not available-refer to card issuer |
| NYCE | 02 | Refer to card issuer's special conditions |
| NYCE | 03 | Invalid merchant or terminal |
| NYCE | 05 | Do not honor |
| NYCE | 07 | Capture card, special conditions (bad delay) |
| NYCE | 10 | Partial Approval |
| NYCE | 12 | Invalid transaction |
| NYCE | 13 | Invalid amount |
| NYCE | 14 | Invalid card number (no such number) |
| NYCE | 15 | Cardholder not on file |
| NYCE | 24 | File update not supported by receiver (only in 03xx) |
| NYCE | 25 | Unable to locate record on file (only in 03xx) |
| NYCE | 26 | Duplicate file update record, no action (only in 03xx) |
| NYCE | 27 | File update field edit error (only in 03xx) |
| NYCE | 28 | File update record locked out (only in 03xx) |
| NYCE | 29 | File update not successful, contact acquirer (only in 03xx) |
| NYCE | 30 | Format error, Data Element 044 (additional response data) contains bit # in e |
| NYCE | 31 | Bank not supported by switch |
| NYCE | 33 | Expired card, capture |
| NYCE | 34 | Suspected fraud, capture |
| NYCE | 38 | Allowable PIN tries exceeded, capture |
| NYCE | 39 | No credit account |
| NYCE | 40 | Requested function not supported |
| NYCE | 41 | Lost card, capture |
| NYCE | 42 | Invalid account |
| NYCE | 43 | Stolen card, capture |
| NYCE | 44 | Lost/stolen card, no capture |
| NYCE | 51 | Insufficient funds |
| NYCE | 52 | No checking account |
| NYCE | 53 | No savings account |
| NYCE | 54 | Expired card |
| NYCE | 55 | Incorrect PIN |
| NYCE | 56 | No card record |
| NYCE | 57 | Transaction not permitted to cardholder |
| NYCE | 58 | Transaction not permitted to terminal |
| NYCE | 59 | Suspected fraud |
| NYCE | 61 | Exceeds withdrawal amount limit |
| NYCE | 62 | Restricted card |
| NYCE | 63 | Security violation (may also be a chargeback) |
| NYCE | 65 | Exceeds withdrawal frequency limit |
| NYCE | 67 | Hard capture, permanent restraint |
| NYCE | 75 | Allowable number of PIN tries exceeded |
| NYCE | 76 | Key synchronization error (NYCE) |
| NYCE | 81 | Issuer-requested stand-in |
| NYCE | 89 | Card Verification Value (all CVx, ICVx, dCVx routines) validation failed (no pickup) suspected counterfeit card |
| NYCE | 90 | Processor not signed on |
| NYCE | 91 | Card issuer unavailable |
| NYCE | 92 | Financial institution or intermediate network unknown for routing |
| NYCE | 94 | Duplicate transaction |
| NYCE | 96 | System malfunction |
| NYCE | N0 | Authorization life cycle unacceptable |
| NYCE | N1 | Authorization life cycle expired |
| NYCE | RD | RMS reject (due to risk scoring) |
| NYCE | S9 | Expiration date mismatch |
| NYCE | SA | Inactive card |
| NYCE | SD | Account closed |
| NYCE | SP | Invalid AVS |
| NYCE | T7 | Partial Approval, cash-back not allowed |
| NYCE | TA | ARQC validation failed for ICC chip card |
| Pulse | 00 | Approved or completed successfully |
| Pulse | 01 | Refer to card issuer |
| Pulse | 02 | Refer to card issuer (special condition) |
| Pulse | 03 | Invalid merchant |
| Pulse | 04 | Pick up card (no fraud) |
| Pulse | 05 | Do not honor |
| Pulse | 07 | Pick up card special conditions |
| Pulse | 10 | Approved for partial amount |
| Pulse | 12 | Invalid transaction |
| Pulse | 13 | Invalid amount |
| Pulse | 14 | Invalid card number (no such number) |
| Pulse | 15 | No such issuer |
| Pulse | 19 | Re-enter transaction |
| Pulse | 20 | Invalid response |
| Pulse | 23 | Unacceptable transaction fee |
| Pulse | 30 | Format error (may also be a reversal) |
| Pulse | 31 | Bank not supported by switch |
| Pulse | 33 | Expired card pick-up |
| Pulse | 34 | Suspected fraud pick-up |
| Pulse | 35 | Card acceptor contact acquirer pick-up |
| Pulse | 36 | Restricted card pick-up |
| Pulse | 37 | Card acceptor call acquirer security pick-up |
| Pulse | 38 | Allowable PIN tries exceeded pick-up |
| Pulse | 39 | No credit account |
| Pulse | 40 | Requested function not supported |
| Pulse | 41 | Lost card pick up |
| Pulse | 42 | No universal account |
| Pulse | 43 | Stolen card pick up |
| Pulse | 44 | No investment account |
| Pulse | 51 | Insufficient funds |
| Pulse | 52 | No checking account |
| Pulse | 53 | No savings account |
| Pulse | 54 | Expired card |
| Pulse | 55 | Incorrect PIN |
| Pulse | 56 | No card record |
| Pulse | 57 | Transaction not permitted to cardholder |
| Pulse | 58 | Transaction not permitted to terminal (may also be a chargeback) |
| Pulse | 59 | Suspected fraud |
| Pulse | 60 | Card acceptor contact acquirer |
| Pulse | 61 | Exceeds withdrawal amount limit |
| Pulse | 62 | Restricted card |
| Pulse | 63 | Security violation (may also be a chargeback) |
| Pulse | 65 | Exceeds withdrawal frequency limit |
| Pulse | 66 | Card acceptor call acquirer security |
| Pulse | 67 | Hard capture pick-up |
| Pulse | 75 | Allowable number of PIN tries exceeded |
| Pulse | 76 | Key synchronization error |
| Pulse | 78 | Customer not eligible for POS |
| Pulse | 79 | Invalid Digital Signature |
| Pulse | 80 | Stale dated transaction |
| Pulse | 88 | Information not on file |
| Pulse | 89 | Card verification value (CVV) or iCVV verification failed (no pick-up) |
| Pulse | 90 | Cutoff in progress |
| Pulse | 91 | Issuer or switch is inoperative |
| Pulse | 92 | Financial institution or intermediate network unknown for routing |
| Pulse | 93 | Transaction cannot be completed violation of law |
| Pulse | 94 | Duplication transaction |
| Pulse | 95 | Reconcile error |
| Pulse | 96 | System malfunction |
| Pulse | N0 | Authorization life cycle unacceptable |
| Pulse | N1 | Authorization life cycle expired |
| Pulse | R3 | Approved with overdraft protection |
| Pulse | R4 | Invalid CVC3/ATC/dCVV |
| Pulse | S5 | PIN not selected |
| Pulse | S6 | PIN already selected |
| Pulse | S8 | Allowable PAN tries exceeded - denial |
| Pulse | S9 | Expiration date mismatch |
| Pulse | SA | Inactive card |
| Pulse | SB | Expiration date mismatch (card pickup) |
| Pulse | SC | Item suspected for stop pay |
| Pulse | SD | Account closed |
| Pulse | SE | Ineligible account |
| Pulse | SF | Item submitted more than two times |
| Pulse | SG | No account on file - absolute |
| Pulse | SH | Unable to locate |
| Pulse | SI | General denial |
| Pulse | SJ | Item settled via ACH |
| Pulse | SK | Cross-reference card not found |
| Pulse | SL | Category limit exceeded |
| Pulse | SM | Transaction limit exceeded |
| Pulse | SN | Daily limit exceeded |
| Pulse | SO | Monthly limit exceeded |
| Pulse | SQ | PIN Key Synch Error |
| Pulse | SR | Bad CVV2 |
| Pulse | SS | Stop payment order |
| Pulse | ST | Revocation of authorization order |
| Pulse | SV | Stop recurring payments |
| Pulse | T3 | Lost card (no pickup) |
| Pulse | T4 | Closed account |
| Pulse | T5 | Dormant account |
| Pulse | T6 | Special conditions (no pickup) |
| Pulse | T7 | Purchase only approval for purchase with cash back transactions |
| Pulse | T9 | Insufficient funds for fees |
| Pulse | TA | ARQC validation failed for contactless Chip data rules |
| Pulse | TB | Unsafe PIN |
|  |  |  |
| Star, Star Acces | 00 | Approved |
| Star, Star Acces | 01 | Refer to Card Issuer |
| Star, Star Acces | 02 | Refer to Card Issuer, special condition |
| Star, Star Acces | 03 | Invalid merchant |
| Star, Star Acces | 04 | Pick-up |
| Star, Star Acces | 05 | Do not honor |
| Star, Star Acces | 06 | Error/General Denial |
| Star, Star Acces | 07 | Pick-up card, special conditions |
| Star, Star Acces | 08 | Honor w/ID |
| Star, Star Acces | 09 | Request in progress |
| Star, Star Acces | 10 | Approved for partial Amount |
| Star, Star Acces | 11 | Transaction approved (VIP) |
| Star, Star Acces | 12 | Invalid Transaction |
| Star, Star Acces | 13 | Invalid amount |
| Star, Star Acces | 14 | Invalid card number (no such number) |
| Star, Star Acces | 15 | No such issuer |
| Star, Star Acces | 16 | Approved |
| Star, Star Acces | 19 | Re-enter transaction |
| Star, Star Acces | 20 | Invalid response |
| Star, Star Acces | 23 | Unacceptable transaction fee |
| Star, Star Acces | 24 | File update not supported by |
| Star, Star Acces | 25 | Unable to locate record on file |
| Star, Star Acces | 26 | Duplicate file update record |
| Star, Star Acces | 27 | File update edit error |
| Star, Star Acces | 28 | File update file locked out |
| Star, Star Acces | 29 | File update not successful, contact acquirer |
| Star, Star Acces | 30 | Format error |
| Star, Star Acces | 31 | Bank not supported by switch |
| Star, Star Acces | 33 | Expired card (capture) |
| Star, Star Acces | 34 | Suspected fraud (capture) |
| Star, Star Acces | 35 | Card acceptor contact acquirer (capture) |
| Star, Star Acces | 36 | Restricted card (capture) |
| Star, Star Acces | 37 | Card acceptor, call acquirer security (capture) |
| Star, Star Acces | 38 | Allowable PIN tries exceeded (capture) |
| Star, Star Acces | 39 | No credit account |
| Star, Star Acces | 40 | Requested function not supported |
| Star, Star Acces | 41 | Lost card |
| Star, Star Acces | 42 | No universal account |
| Star, Star Acces | 43 | Stolen card (capture) |
| Star, Star Acces | 44 | No investment account |
| Star, Star Acces | 51 | Not sufficient funds |
| Star, Star Acces | 52 | No checking account |
| Star, Star Acces | 53 | No savings account |
| Star, Star Acces | 54 | Expired card |
| Star, Star Acces | 55 | Incorrect PIN |
| Star, Star Acces | 56 | No card record |
| Star, Star Acces | 57 | Transaction not permitted to cardholder |
| Star, Star Acces | 58 | Transaction not permitted to terminal |
| Star, Star Acces | 59 | Suspected fraud |
| Star, Star Acces | 60 | Card acceptor contact acquirer |
| Star, Star Acces | 61 | Exceeds ATM withdrawal or POS purchase amount limit |
| Star, Star Acces | 62 | Restricted card |
| Star, Star Acces | 63 | Security violation |
| Star, Star Acces | 65 | Exceeds withdrawal frequency limit |
| Star, Star Acces | 66 | Card acceptor call Acquirer's security department |
| Star, Star Acces | 67 | Hard capture |
| Star, Star Acces | 68 | Late Response |
| Star, Star Acces | 75 | Allowable PIN tries exceeded |
| Star, Star Acces | 76 | Key sync error* |
| Star, Star Acces | 78 | Cardholder not eligible for POS |
| Star, Star Acces | 80 | Private use (Stale dated transaction) |
| Star, Star Acces | 82 | Count exceeds limit (valid only for VisaNet issuers) |
| Star, Star Acces | 84 | Time for preauthorization reached (Only valid for Interlink issuers) |
| Star, Star Acces | 85 | Additional authentication required |
| Star, Star Acces | 86 | Cannot verify PIN (valid only for VisaNet issuers) |
| Star, Star Acces | 87 | Duplicate |
| Star, Star Acces | 88 | Information not on file |
| Star, Star Acces | 89 | Card Validation failure (CVC/CVV) |
| Star, Star Acces | 90 | STAR SE/W platform: Cutoff in progress (or) STAR NE platform: Card Validation failure (CVC/CVV)-Track 2 |
| Star, Star Acces | 91 | Issuer inoperative/unavailable |
| Star, Star Acces | 92 | FI cannot be found for routing * |
| Star, Star Acces | 93 | Transaction cannot be completed |
| Star, Star Acces | 94 | Duplicate transaction |
| Star, Star Acces | 95 | Reconcile error |
| Star, Star Acces | 96 | System malfunction |
| Star, Star Acces | 98 | Card Validation failure (CVC2/CVV2)-Trackless Transactions |
| Star, Star Acces | 99 | Card Validation failure (CVC3/CVV3) |
| Star, Star Acces | A1 | Invalid voucher ID |
| Star, Star Acces | A2 | Invalid authorization number |
| Star, Star Acces | K2 | Special reply for SE/W token lookup |
| Star, Star Acces | K3 | Token lookup failure |
| Star, Star Acces | R4 | CVC3/dCVV failure |
| Star, Star Acces | S7 | Unmatched voucher information |
| Star, Star Acces | S9 | Expiration date mismatch - no capture |
| Star, Star Acces | SA | Inactive Card |
| Star, Star Acces | SB | Expiration date mismatch capture card |
| Star, Star Acces | SC | Item suspected for stop pay |
| Star, Star Acces | SD | Acct closed |
| Star, Star Acces | SE | Ineligible account |
| Star, Star Acces | SF | Item submitted more than two times |
| Star, Star Acces | SG | No acct on file |
| Star, Star Acces | SH | Unable to locate |
| Star, Star Acces | SI | General Denial |
| Star, Star Acces | SM | Transaction limit exceeded |
| Star, Star Acces | SP | Special conditions (no capture) |
| Star, Star Acces | SR | Card validation (CVC2/CVV2) Failure (or) 3-D Secure (MC Secure Code AAV/VISA CAVV) Failure |
| Star, Star Acces | T3 | Lost card (no capture) |
| Star, Star Acces | T4 | Closed account |
| Star, Star Acces | T5 | Dormant account |
| Star, Star Acces | T6 | Special conditions/CV Threshold reached |
| Star, Star Acces | T7 | ATC Failure |
| Star, Star Acces | T8 | ARQC Validation Failure |
| Star, Star Acces | TA | ARQC Validation Failure |
| Star, Star Acces | TG | ATC Failure |
| Star, Star Acces | TS | Suspected Fraud |
| Star, Star Acces | VC | Risk Block (country code blocking) |
| Maestro | 00 | Approved or completed successfully |
| Maestro | 01 | Refer to card issuer |
| Maestro | 04 | Capture card |
| Maestro | 05 | Do not honor |
| Maestro | 10 | Partial Approval |
| Maestro | 12 | Invalid transaction |
| Maestro | 13 | Invalid amount |
| Maestro | 14 | Invalid card number |
| Maestro | 15 | Invalid issuer |
| Maestro | 30 | Format error |
| Maestro | 41 | Lost card |
| Maestro | 43 | Stolen card |
| Maestro | 51 | Insufficient funds/over credit limit |
| Maestro | 54 | Expired card |
| Maestro | 55 | Invalid PIN |
| Maestro | 57 | Transaction not permitted to issuer/cardholder |
| Maestro | 58 | Transaction not permitted to acquirer/terminal |
| Maestro | 61 | Exceeds withdrawal amount limit |
| Maestro | 62 | Restricted card |
| Maestro | 63 | Security violation |
| Maestro | 65 | Exceeds withdrawal count limit |
| Maestro | 70 | Contact card issuer |
| Maestro | 71 | PIN not changed |
| Maestro | 75 | Allowable number of PIN tries exceeded |
| Maestro | 76 | Invalid/nonexistent "To Account" specified |
| Maestro | 77 | Invalid/nonexistent "Fron Account" specified |
| Maestro | 78 | Invalid/nonexistent account specified(general) |
| Maestro | 79 | "Life cycle (Mastercard use only for 0210 messages)" |
| Maestro | 81 | Domestic Debit Transaction Not Allowed (Regional use only) |
| Maestro | 82 | "Policy (Mastercard use only for 0210 messages)" |
| Maestro | 83 | "Fraud/Security (Mastercard use only for 0210 messages)" |
| Maestro | 84 | Invalid Authorization Life Cycle |
| Maestro | 85 | Not declined |
| Maestro | 86 | PIN validation not possible |
| Maestro | 87 | Purchase Amount only, no cash back allowed |
| Maestro | 88 | Cryptograpic failure |
| Maestro | 89 | Unacceptable PIN - Transaction declined - Retry |
| Maestro | 91 | Authorization platform or issuer system inoperative |
| Maestro | 92 | Unable to route transaction |
| Maestro | 94 | Duplicate transmission detected |
| Maestro | 96 | System Error |

