<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/facebook-login -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Facebook Login
slug: /docs/guides/paypal-commerce-ios/facebook-login/
createTime: '2025-04-02T00:40:02.098Z'
updateTime: '2025-04-02T00:40:02.132Z'
---



# Facebook Login

If you would like to include Facebook login in your app, then you will need to set up a few things.
- Add your Facebook App ID to the Commerce Panel under[General Settings](https://commerce.paypal.com/).
- Add your Facebook App ID to your**Info.plist**using the keyFacebookAppID.
- Add the Facebook URL scheme to your**Info.plist**:
- In Xcode, select your Target.
- Under URL Types, add a new type (**+**button).
- In the URL Scheme field, enter the scheme provided by Facebook (e.g.fb1234567890).


- Updates to**Info.plist**.
- Add or update theLSApplicationQueriesSchemesarray. It should includefbauth2. For example:




### xml
```xml
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>fbapi</string>
    <string>fb-messenger-api</string>
    <string>fbauth2</string>
    <string>fbshareextension</string>
</array>
```

- NSAppTransportSecurityallows us to securely communicate with Facebook in iOS 9+.


### xml
```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSExceptionDomains</key>
    <dict>
        <key>cloudfront.net</key>
        <dict>
            <key>NSExceptionRequiresForwardSecrecy</key>
            <false/>
            <key>NSIncludesSubdomains</key>
            <true/>
        </dict>
        <key>facebook.com</key>
        <dict>
            <key>NSIncludesSubdomains</key>
            <true/>
            <key>NSExceptionRequiresForwardSecrecy</key>
            <false/>
        </dict>
        <key>fbcdn.net</key>
        <dict>
            <key>NSIncludesSubdomains</key>
            <true/>
            <key>NSExceptionRequiresForwardSecrecy</key>
            <false/>
        </dict>
        <key>akamaihd.net</key>
        <dict>
            <key>NSIncludesSubdomains</key>
            <true/>
            <key>NSExceptionRequiresForwardSecrecy</key>
            <false/>
        </dict>
    </dict>
</dict>
```
