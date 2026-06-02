<!-- Source URL: https://docs.stripe.com/apple-pay/best-practices -->
<!-- Fetched: 2026-05-07 -->

# Apple Pay Best Practices

Follow these best practices to make the most of your Apple Pay integration.

You can verify if your customer has set up Apple Pay on their device within your app or on your website. Check out the [iOS SDK](https://docs.stripe.com/apple-pay.md) or [Payment domain registration](https://docs.stripe.com/payments/payment-methods/pmd-registration.md) documentation.

In a normal checkout flow, your customers usually need to enter their card information, billing and shipping address, email, or phone number. With Apple Pay, customers can provide this information by authorizing a payment with Touch ID, or by double-clicking the side button of their Apple Watch.

Apple Pay can help boost metrics like conversion rate, new user acquisition, and purchase frequency, while reducing risk and the overall cost of payment acceptance. Consider implementing the following best practices to further improve the checkout experience for your customers using Apple Pay.

## Implement an express checkout

After implementing an express checkout, [Indiegogo](https://www.indiegogo.com/) saw their conversion rate increase by 250%.

You can provide your app users and website visitors with more opportunities to make a purchase by adding Apple Pay to product detail pages, product list views, or search results pages. As Apple Pay enables new and existing customers to make a purchase with a single tap you can convert more prospects into actual customers.

- For customers who have set up Apple Pay, display the **Apple Pay** button on product detail pages, product list view pages, or on search results pages.
- Ask the customer for all mandatory information about their order (for example, size, color, quantity, and so on) before showing the Apple Pay button.
- Never display the Apple Pay button in a disabled state. Instead, highlight incomplete product selections if the customer selects the Apple Pay button before completing them.
- If you already display an **Express Checkout** button in your checkout, consider replacing it with the Apple Pay button to help avoid user confusion.

## Remove or move registration until after the purchase is complete

Apple Pay enables customers to seamlessly create new accounts after making their first purchase. By postponing the option to create an account until after the transaction, customers are more likely to complete their purchase.

- For Apple Pay–ready customers, remove any mandatory sign-up from the beginning of the payment process.
- Don’t request any customer information that Apple Pay provides during the payment request (for example, customer name or address information).
- Only request the information you need as part of the transaction request. For example, don’t request a shipping address if you’re not shipping anything (for example, services, digital goods).
- Request any additional information needed to create an account (for example, password) on the payment confirmation page, after the payment is complete.

## Default to Apple Pay

[Wish](https://www.wish.com/) conducted an A/B test to measure the impact on conversion rates for new users who are Apple Pay–ready. Defaulting to Apple Pay yielded 2X higher conversion rate increase.

If your customer is on an Apple Pay-enabled device, consider offering Apple Pay as the default payment method. This can boost your checkout conversion for both new and existing users.

- For new customers that have Apple Pay set up on their device, skip the payment method selection page in the checkout flow so they can complete their purchase quickly.
- Pre-select Apple Pay in the payment method selector to reduce the number of steps a customer needs to perform.
- Show the Apple Pay button for a stronger call to action.

## Offer to set up Apple Pay within your app or website

The Apple Pay API allows you to identify customers with an Apple Pay-capable device who haven’t added a card to Wallet yet. You can then offer these users the opportunity to set up Apple Pay from within your app.

You might consider displaying a **Set Up Apple Pay** button:

- Next to any other payment options on the payment method selection page during checkout for capable devices
- Next to any other payment options on the payment method management page in the customer’s account settings
- In any messages to your users that request they add or update their payment information (for example, emails prompting them to update expired card information)

If you already support other payment methods that give the option to set up an account during the checkout process, always display a **Set Up Apple Pay** button for capable devices.

## Communicate Apple Pay acceptance

After you’ve integrated Apple Pay as a supported payment method, let your Apple Pay-ready customers know. You might also want to consider setting it as the default payment method in your app or website.

- Add the Apple Pay mark next to other payment marks in your checkout.
- When you add support for Apple Pay to your app or website, use a banner or additional messaging before the checkout process to announce that you now accept Apple Pay.
- When you add support for Apple Pay to your app or website, announce it through your marketing channels (email, notification, social media, and so on).
- Make the banner or additional messaging actionable so that your customers can start using Apple Pay in your app or website with only a tap. If you don’t have this capability, let your customers know how they can start using Apple Pay.
- Update the screenshots and description of your Apple Pay-ready app within the App Store to reflect Apple Pay acceptance.

## Apple Pay Certificate Renewal

Apple sends notifications to the team agent of the Apple Developer Account at 30 days, 15 days, and 7 days prior to the upcoming expiration date of the certificate. The certificate is valid for 25 months from activation. You’ll need to generate a new certificate and activate it before your current one expires to avoid any disruptions.

Go to the [iOS certificate settings](https://dashboard.stripe.com/settings/ios_certificates) in the Dashboard, click **Add new application**, and follow the guide there.

Download a new CSR from Stripe for creating the new certificate, and never use the older CSR that you downloaded from Stripe. Upload the new certificate to Stripe before activating it on the Apple Developer Account. Apple uses the new public key to encrypt the Apple Pay token approximately 5 minutes after you click **Activate** in the portal. Make sure you have both the old and new certificate in the Stripe Dashboard before activating the new certificate so that either of the certificates can be used during transition.

You don’t need to update your app after you’ve replaced the certificate. We recommend running an Apple Pay transaction with test API keys to make sure the integration is working as expected.

## Always test on updates to your Apple Pay integration

Before applying changes that update your integration or switch your Apple Merchant ID, verify that you’re able to create tokens and use them to complete payments successfully.

## Best practice for Apple Pay recurring transaction

If you accept Apple Pay payments, we recommend configuring the Apple Pay interface to return a merchant token to enable merchant initiated transactions (MIT) such as recurring and deferred payments and automatic reloads. Merchant tokens (MPANs) connect your business with your customer’s Apple Wallet payment method, so they work across multiple devices and keep payment information active in a new device even when its removed from a lost or stolen device. See [ApplePay merchant tokens](https://docs.stripe.com/apple-pay/merchant-tokens.md?pay-element=ece) for integration details and [Apple Pay Recurring Transactions](https://docs.stripe.com/apple-pay/apple-pay-recurring.md) for direct API integration recommendations to prevent recurring authorization failures due to cryptogram expiration.

## See also

- [Accept Apple Pay](https://docs.stripe.com/apple-pay.md?platform=ios#accept)
- [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md)
