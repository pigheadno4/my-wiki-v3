<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/response-parameters/ -->
<!-- Fetched: 2026-04-13 -->

---
title: 3D Secure response parameters
slug: /docs/checkout/advanced/customize/3d-secure/response-parameters/
createTime: '2024-05-11T03:20:05.527Z'
updateTime: '2025-12-10T13:51:11.004Z'
---


# 3D Secure response parameters

You can see the response of the 3D Secure flow by viewing the liability_shift , enrollment_status , and authentication_status fields in the payload your server returns to your client.

If you've integrated with the JavaScript SDK, you receive the liability_shift parameter only.



## Supported parameters 
### liability_shift
liability_shift signals whether the issuing bank may accept liability for the transaction.

You can find liability_shift in the payload your server returns to your client. This is a client and server-side parameter.

| Response | Description | Recommended action |
| --- | --- | --- |
| POSSIBLE | Liability might shift to the card issuer. | Continue with authorization. |
| NO | Liability is with the merchant. | Do not continue with authorization. |
| UNKNOWN | The authentication system isn't available. | Do not continue with authorization. Request the cardholder to retry. |

### enrollment_status
enrollment_status shows whether the card type and issuing bank are ready to complete a 3D Secure authentication. This is a server-side parameter.

| Response | Description |
| --- | --- |
| Y | Card type and issuing bank are ready to complete a 3D Secure authentication. |
| N | Card type and issuing bank are not ready to complete a 3D Secure authentication. |
| U | System is unavailable at the time of the request. |
| B | System has bypassed authentication. |

### authentication_status
authentication_status indicates the result of the authentication challenge. This is a server-side parameter.

| Response | Description |
| --- | --- |
| Y | Successful authentication. |
| N | Failed authentication |
| R | Rejected authentication. |
| A | Attempted authentication. |
| U | Unable to complete authentication. |
| C | Challenge required for authentication. |
| I | Information only. |
| D | Decoupled authentication. |

### Recommended action
Based on the results of enrollment_status and authentication_status , liability_shift response is returned. The liability_shift response determines how you might proceed with authentication.

| enrollment_status | authentication_status | liability_shift | Recommended action |
| --- | --- | --- | --- |
| Y | Y | POSSIBLE | Continue with authorization. |
| Y | N | NO | Do not continue with authorization. |
| Y | R | NO | Do not continue with authorization. |
| Y | A | POSSIBLE | Continue with authorization. |
| Y | U | UNKNOWN | Do not continue with authorization. Request cardholder to retry. |
| Y | U | NO | Do not continue with authorization. Request cardholder to retry. |
| Y | C | UNKNOWN | Do not continue with authorization. Request cardholder to retry. |
| Y |  | NO | Do not continue with authorization. Request cardholder to retry. |
| N |  | NO | Continue with authorization. |
| U |  | NO | Continue with authorization. |
| U |  | UNKNOWN | Do not continue with authorization. Request cardholder to retry. |
| B |  | NO | Continue with authorization. |
|  |  | UNKNOWN | Do not continue with authorization. Request cardholder to retry. |



## Deprecated parameters 
**Note:** If you integrated 3D Secure beforeJune 2020, the liabilityShifted , authenticationStatus , and AuthenticationReason parameters continue to work on the server but are no longer supported.

| liabilityShifted | authenticationStatus | AuthenticationReason | Reason | Next steps |
| --- | --- | --- | --- | --- |
| undefined | undefined | undefined | You have not required 3D Secure for the buyer or the card network did not require a 3D Secure. | You can continue with authorization and assume liability. If you prefer not to assume liability, ask the buyer for another card. |
| true | YES | SUCCESSFUL | Buyer successfully authenticated using 3D Secure. | Buyer authenticated with 3D Secure and you can continue with the authorization. |
| false | ERROR | ERROR | An error occurred with the 3D Secure authentication system. | Prompt the buyer to re-authenticate or request for another form of payment. |
| false | NO | SKIPPED_BY_BUYER | Buyer was presented the 3D Secure challenge but chose to skip the authentication. | Do not continue with current authorization. Prompt the buyer to re-authenticate or request buyer for another form of payment. |
| false | NO | FAILURE | Buyer may have failed the challenge or the device was not verified. | Do not continue with current authorization. Prompt the buyer to re-authenticate or request buyer for another form of payment. |
| false | NO | BYPASSED | 3D Secure was skipped as authentication system did not require a challenge. | You can continue with the authorization and assume liability. If you prefer not to assume liability, ask the buyer for another card. |
| false | NO | ATTEMPTED | Card is not enrolled in 3D Secure. Card issuing bank is not participating in 3D Secure. | Continue with authorization as authentication is not required. |
| false | NO | UNAVAILABLE | Issuing bank is not able to complete authentication. | You can continue with the authorization and assume liability. If you prefer not to assume liability, ask the buyer for another card. |
| false | NO | CARD_INELIGIBLE | Card is not eligible for 3D Secure authentication. | Continue with authorization as authentication is not required. |

In scenarios where liabilityShifted was either false or undefined , you can complete the payment at your own risk, meaning that the liability of any chargeback has not shifted from the merchant to the card issuer.



## Next steps 

### Test in PayPal Sandbox
A self-contained, virtual testing environment


### Go live
Move from PayPal's production environment to go live.
