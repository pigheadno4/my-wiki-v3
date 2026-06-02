<!-- Source URL: https://developer.paypal.com/docs/log-in-with-paypal/integrate/best-practices/ -->

## <!-- Fetched: 2026-04-16 -->

title: Best practices
slug: /docs/log-in-with-paypal/integrate/best-practices/
createTime: '2024-08-15T06:16:32.214Z'
updateTime: '2025-05-14T15:14:19.794Z'

---

# Best practices

## Session Management

Users who log in with PayPal and choose to remain logged in are recognized for a certain period following the initial log in. Session persistence conveniently eliminates the need for multiple user log ins to your website.

Within that window, the user is recognized at other websites that support Log in with PayPal, but the user is prompted to consent to share information with these subsequent websites.

We recommend that you maintain your own sessions to facilitate a smooth user experience. When an access token is obtained from PayPal for each user, a refresh token is also received. PayPal's refresh tokens are valid for longer than access tokens. You must track session times to determine when to refresh access tokens.

If your website or app includes a native log out feature, we recommend that you refrain from disconnecting the Log in with PayPal session when the user logs out of your site. This eliminates the need to reestablish the connection to PayPal if the user returns to your site within a certain period of time.

## Anti-spam policy

You must agree to our anti-spam policy when offering Log in with PayPal.

You must not automatically sign up Log in with PayPal users to receive email newsletters or regular communication from you. The only time users should receive email from you is after making a purchase, in which case the customer should receive regular and customary email regarding the order confirmation, a receipt, and shipping information. If you wish to send email beyond this level of communication, you're required to explicitly request permission from the user.

## Link existing accounts to avoid duplicates

We recommend that if you already maintain user accounts and you're just starting to support Log in with PayPal, give users the option to link their pre-existing user account with their PayPal account. This link can be established based on information obtained from the their non-financial user attributes obtained from the Log in with PayPal session, such as the user's email address.

We recommend that you scan for duplicate accounts in real time, during the Log in with PayPal user session. However, if scanning for duplicates in real time is not feasible, we recommend that you perform an offline scan and notify users, by email, with a request to reconcile accounts. Linking the two accounts eliminates duplication in you database and allows users to access historical purchase information for purchases completed with their user account.

## Unlinking a PayPal account

If a user elects to discontinue use of Log in with PayPal on your site, we recommend providing those who have linked accounts with the option to unlink their PayPal account from their user account. This option requires that you also provide users with the capability to create a user name and password for your website.

If you decide to discontinue support for the Log in with PayPal feature, you must request user permission to unlink their user account from their PayPal account for users who already linked these accounts. You may need to provide users with the ability to set a user account password during this unlinking process.

## Expedite checkout

To provide an expedient and reliable customer checkout experience, we recommend the following:

### Pre-fill checkout forms

Enable pre-filled checkout forms with the customer information obtained from the Log in with PayPal session.

### Personalize checkout

Don't require customers to re-enter information that PayPal already provides. You can leverage information already obtained from the Log in with PayPal session to personalize the checkout experience. For example, use the customer's ZIP code to calculate shipping charges.

### Account information

On the order confirmation page, display the customer's basic account information. This allows the customer to review information, such as the shipping address, before finalizing the purchase. We also recommend allowing the customer to edit this information.

Since customer information was obtained from the Log in with PayPal session and was not entered directly by the customer, it's especially important that the customer has the opportunity to review and edit this information before making the purchase.

### PayPal as default payment method

Users who log in with PayPal likely want to pay with PayPal. We recommend setting PayPal as the default payment option, or the first payment option, for customers who log in with a PayPal.
