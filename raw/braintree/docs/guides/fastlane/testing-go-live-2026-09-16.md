<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/fastlane/testing-go-live -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Test your Integration
slug: /docs/guides/fastlane/testing-go-live/
createTime: '2025-04-02T01:57:28.539Z'
updateTime: '2025-04-02T01:57:28.563Z'
---



# Test your Integration

Here are some of the integration testing checklist that you can use to test the use-cases and ensure that integration works as expected.


#### Testing Guest Payers


- **New Email Address:**: Provide a**new email address**not associated with a sandbox Fastlane account.
- **Ensure the opt-in toggle is ON:**Go through the checkout process using one of the[card numbers](https://developer.paypal.com/braintree/docs/guides/fastlane/testing-go-live#test-cards)available for testing. Be sure that the**opt-in toggle is in the “on” state**.
- **Any phone number for sandbox:**You can enter any valid phone number (No SMS will be sent in Sandbox mode). + Upon completing the transaction, a Fastlane profile will be created to test subsequent transactions as a Fastlane member.
- When you complete the transaction, a Fastlane profile is created that can be used for testing subsequent transactions as a Fastlane member.

| Payment Integration Use-case | Feature | Payment Integration Result |
| --- | --- | --- |
| - When the buyer enters the email, they are recognized as NOT having a PayPal account or a Fastlane profile.
- FastlanePaymentComponent`renders card fields and the consent toggle.
- The Buyer completes the order. | - Consent Toggle OFF (Opts out of Fastlane) | - The buyer’s Fastlane profile is not created​.
- Payment completed successfully. |
| - Enter email, the buyer is not recognized as having a PayPal account or a Fastlane profile.
- FastlanePaymentComponentshould render card fields and the consent toggle.
- Ensure the consent toggle is in the On position.
- Complete the order. | - Consent Toggle ON (Opts out of Fastlane). | - The buyer's Fastlane profile should be created.​
- The payment should be completed successfully. |


#### Testing Fastlane Members

Before you test the guest payers, ensure you have follow the below instructions :


- **Create a Fastlane Member profile:**Go through the previous step and register a new Fastlane account. Be sure to remember the email address used when you created the account so that you can use it for additional testing.
- **OTP for testing:**When the authentication modal appears and you are prompted for a one-time password (OTP) use 111111 to trigger a successful authentication and any other 6-digit number to simulate a failed authentication.
- **Test updating payment method and shipping addresses to existing Fastlane Profiles:**Make sure that you test the payer’s ability to update shipping addresses and cards associated with their profile.

| Payment Integration Use-case | Feature | Payment Integration Result |
| --- | --- | --- |
| - When the buyer enters the email, they are recognized as having a Fastlane profile.
- OTP flow will be triggered to authenticate the buyer.
- Buyer's address and funding instrument are pre-populated after successful OTP entry. | Happy Path | - Complete the order.
- The payment should be completed successfully​. |
| - Enter email, the buyer is recognized as having a Fastlane profile.
- OTP flow will be triggered to authenticate the buyer.
- Cancel the OTP by clicking the “x” or entering an incorrect code.
- TheFastlanePaymentComponentshould render the card fields with no consent toggle. | OTP Failed or Cancelled | - Complete the order.
- The payment should be completed successfully. |
| - Enter email, the buyer is recognized as having a Fastlane profile.
- OTP flow will be triggered to authenticate the buyer.
- Should see shipping address and card information pre-populated based on returned profile information after successful OTP entry.
- Click the change address to invoke address selector UI.
- Select "Add new address" and enter a new address in the address selector UI. | New Address | - Complete the order.
- New address will be added to the buyer's Fastlane profile. |
| - Enter email, the buyer is recognized as having a Fastlane profile.
- OTP flow will be triggered to authenticate the buyer.
- Should see shipping address and card information pre-populated based on returned profile information after successful OTP entry.
- Click the change card link to invoke card selector UI.
- Select "Add new card" and enter a new card in the card selector UI. | New Card | - Complete the order.
- New card will be added to the buyer's Fastlane profile. |
| - Enter email, the buyer is recognized​ as having a Fastlane profile​.
- OTP flow will be triggered to authenticate the buyer.
- Should see shipping address and card information pre-populated based on returned profile information after successful OTP entry​.
- Click the change shipping address to invoke address selector UI​ viashowAddressSelector().
- Select another address from the list. | Change Address | - Complete the order.
- The payment should be completed successfully.​ |
| - Enter email, the buyer is recognized​ as having a Fastlane profile​.
- OTP flow will be triggered to authenticate the buyer.
- Should see shipping address and card information pre-populated based on returned profile information after successful OTP entry.​
- Will click the change link to invoke card selector UI​ viashowCardSelector().
- Select another card from the list. | Change Card | - Complete the order.
- The payment should be completed successfully​. |
| - Enter email, the buyer is recognized​ as having a Fastlane profile.
- OTP flow will be triggered to authenticate the buyer.
- Should see shipping address pre-populated based on returned profile information after successful OTP entry.
- The payment component should render card fields to capture a new card. | No Card or Card of unsupported brand | - Complete the order.
- The payment should be completed successfully​.
- New card should be added to the buyer's Fastlane profile. |
| - OTP flow will be triggered to authenticate the buyer.
- No address is returned in the profile object.
- Shipping address collection form should be rendered.
- Enter a new address.
- Should see card pre-populated based on returned profile information after successful OTP entry. | No Address or Address in unsupported region | - Complete the order.
- The payment should be completed successfully​.
- New shipping address should be added to the buyer's Fastlane profile. |


#### PayPal members without a Fastlane Profile

There is no need to test the integration as Fastlane integration for PayPal members is same.

Refer to [advanced options](https://developer.paypal.com/braintree/docs/guides/fastlane/advanced-option#paypal-members-without-a-fastlane-profile) for more information.


#### Test Cards

| Card Number | Brand |
| --- | --- |
| 4005519200000004 | Visa |
| 4012000033330026 | Visa |
| 5555 5555 5555 4444 | Visa |
| 378282246310005 | Mastercard |
| 378282246310005 | American Express |

Explore: [Troubleshooting and FAQ](/braintree/docs/guides/fastlane/faq)

