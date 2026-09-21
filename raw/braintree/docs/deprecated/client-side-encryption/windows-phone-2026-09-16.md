<!-- Source URL: https://developer.paypal.com/braintree/docs/deprecated/client-side-encryption/windows-phone -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Windows Phone
slug: /docs/deprecated/client-side-encryption/windows-phone/
createTime: '2025-04-02T01:33:31.007Z'
updateTime: '2025-04-02T01:33:31.024Z'
---



# Windows Phone


**NOTE**
The integration method outlined below is deprecated. [Learn more about upgrading to the Braintree SDKs.](/braintree/docs/reference/general/upgrade) 


## Installation

There are a couple of ways to use the Windows Phone client encryption library.
### Windows Phone class library

To import the Windows Phone class library, follow the following steps.
- Clone the[source code](https://github.com/braintree/braintree_windows_phone_encryption)from Github.
- Import the Braintree Windows Phone class library into your solution.
- Add the library as a project dependency and make sure to reference the library.


### Source code

[github](https://github.com/braintree/braintree_windows_phone_encryption)|[tgz](https://github.com/braintree/braintree_windows_phone_encryption/tarball/master)|[zip](https://github.com/braintree/braintree_windows_phone_encryption/zipball/master)
## Integration examples

[github](https://github.com/braintree/braintree_windows_phone_encryption_examples)|[tgz](https://github.com/braintree/braintree_windows_phone_encryption_examples/tarball/master)|[zip](https://github.com/braintree/braintree_windows_phone_encryption_examples/zipball/master)
## Bugs

If you run into a bug,[contact us](/braintree/help)or create an issue on the[GitHub issue tracker](https://github.com/braintree/braintree_windows_phone_encryption/issues).
## Quick start example

```language-dotnet
using System;
using BraintreeEncryption.Library; namespace BraintreeExample
{ class Program { static void Main(string[] args) { var braintree = new Braintree("your-client-side-encryption-key"); var encryptedCreditCardNumber = braintree.Encrypt("4111111111111111"); var encryptedCvv = braintree.Encrypt("111"); var encryptedExpirationDate = braintree.Encrypt("01/2014"); } } }
}
```
