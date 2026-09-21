<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/functions/publishing -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Packaging and Publishing
slug: /docs/guides/functions/publishing/
createTime: '2025-04-01T22:01:25.402Z'
updateTime: '2025-04-01T22:01:25.434Z'
---



# Packaging and Publishing


**AVAILABILITY**
We're building functions with the same proven expertise and rock solid foundations you expect from Braintree. Take a look at our documentation preview to get a jump start on what you'll make with functions. Email [functions-requests@braintreepayments.com](mailto:functions-requests@braintreepayments.com) to learn more.

By default, deployments of functions are private. In order to share your function with other users
you must package and publish to Braintree's function ecosystem.
## Package Your Function

To package your function, define a few more pieces of metadata within you function's configuration.
Use our CLI to go through an interactive prompt to set the metadata about your package.
### bash
```bash

$ btfns package .
> Name: MyPublicFunction
> Developer Website: https://yourwebsite.com
> Support E-mail: support@yourwebsite.com
> Description: My function.
> Logo: /path/to/logo.png
    
```

## Publish to Braintree


### bash
```bash

$ btfns publish . -v 1.0.0
Publishing MyPublicFunction @ 1.0.0 to https://btfns.co
...
> Success .... https://btfns.co/user/MyPublicFunction
```
