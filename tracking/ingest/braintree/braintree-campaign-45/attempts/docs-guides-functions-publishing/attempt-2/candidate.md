---
title: "Braintree Functions Packaging and Publishing"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/functions/publishing"
raw_files:
  - "braintree/docs/guides/functions/publishing-2026-09-16.md"
tags: [braintree, functions, packaging, publishing, cli]
---

## Overview

This captured [[braintree|Braintree]] website page is a documentation preview explaining that Function deployments are private by default and that, to share a Function with other users, it must be packaged and published to Braintree's function ecosystem. It documents a CLI-driven metadata prompt and an illustrative versioned publish command. The snapshot does not establish current Functions availability, merchant or account eligibility, an exact CLI/package/runtime version, a client/server SDK placement, a deployment environment, successful publication, or payment execution. It is website documentation rather than GitHub implementation or release-history evidence.

## Key takeaways

- The page says Function deployments are private by default. For the stated condition of sharing a Function with other users, it requires packaging and publishing to Braintree's function ecosystem.
- Packaging is shown through `btfns package .` and an interactive metadata prompt. The illustrated fields include name, developer website, support email, description and logo; treat those fields as example-page detail, not a complete package schema or proof that packaging succeeded.
- Publishing is illustrated with `btfns publish . -v 1.0.0`, followed by example output naming `https://btfns.co` and a Function URL. The literal version, host and success output are examples, not guarantees of current endpoint ownership, environment, availability or successful publication.
- The raw page metadata records creation and update timestamps on 2025-04-01, while the immutable snapshot was fetched on 2026-09-16. Neither timestamp establishes current product state or later history.

## Detail locators

- **Preview availability and inquiry route:** `AVAILABILITY`, raw lines 17–18.
- **Private-by-default deployment and sharing condition:** introduction, raw lines 20–21.
- **Packaging metadata prompt:** `Package Your Function`, raw lines 22–36.
- **Versioned publish example and illustrative output:** `Publish to Braintree`, raw lines 38–48.
- **Captured page history metadata:** frontmatter `createTime` and `updateTime`, raw lines 5–10; fetch date, raw line 2.

## Related

- [[braintree]]
- [[braintree-payment-platform]] — main provider concept route for the collected Braintree Functions documentation previews.
- [[source-braintree-docs-guides-functions-cli-reference]] — related CLI-reference navigation.

## Raw Sources

- [[raw/braintree/docs/guides/functions/publishing-2026-09-16|Braintree Functions Packaging and Publishing (2026-09-16 snapshot)]]
