<!-- Source URL: https://developer.paypal.com/braintree/docs/deprecated/client-side-encryption/android-library -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Android
slug: /docs/deprecated/client-side-encryption/android-library/
createTime: '2025-04-01T22:05:49.201Z'
updateTime: '2025-04-01T22:05:49.219Z'
---



# Android


**NOTE**
The integration method outlined below is deprecated. [Learn more about upgrading to the Braintree SDKs.](/braintree/docs/reference/general/upgrade) 


## Installation

There are a couple of ways to use the Android client encryption library.
### Jar file

Download[encryption-2.0.0.jar](http://search.maven.org/remotecontent?filepath=com/braintreepayments/encryption/2.0.0/encryption-2.0.0.jar) SHA1: 864740734e9806aae1914d461600a4cb88ee5331 
### Android library project (SDK r6 or higher)


**NOTE**
This assumes you are using Eclipse as your development IDE.


- Clone the[source code](https://github.com/braintree/braintree_android_encryption)on github.
- Import the Braintree Android library project into your Eclipse workspace.
- Go to your project’s properties.
- Under Android, Library section, add the Braintree Android library project.


### Source code

[github](https://github.com/braintree/braintree_android_encryption)|[tgz](https://github.com/braintree/braintree_android_encryption/tarball/master)|[zip](https://github.com/braintree/braintree_android_encryption/zipball/master)
## Integration examples

[github](https://github.com/braintree/braintree_android_encryption_examples)|[tgz](https://github.com/braintree/braintree_android_encryption_examples/tarball/master)|[zip](https://github.com/braintree/braintree_android_encryption_examples/zipball/master)
## Bugs

If you run into a bug,[contact us](/braintree/help)or create an issue on the[GitHub issue tracker](https://github.com/braintree/braintree_android_encryption/issues).
## Quick start example

```language-java
import com.braintreegateway.encryption.Braintree; public class BraintreeExample { public static void main(String[] args) { Braintree braintree = new Braintree("your-client-side-encryption-key"); String encryptedCreditCardNumber = braintree.encrypt("4111111111111111"); String encryptedCvv = braintree.encrypt("111"); String encryptedExpirationDate = braintree.encrypt("01/2014"); }
}
```
