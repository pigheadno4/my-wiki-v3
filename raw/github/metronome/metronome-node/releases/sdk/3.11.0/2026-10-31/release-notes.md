## [3.11.0](https://github.com/Metronome-Industries/metronome-node/compare/v3.10.0...v3.11.0) (2026-10-27)

<!-- metronome-sdk-release-descriptions:start -->

Adds public billing and notification capabilities, including quantity-based balances, subscription controls, and custom pricing units.

### Features

* Support `SPEND` and `QUANTITY` access types when creating commits and credits, filtering balances, and configuring threshold notifications; expose quantity consumption on invoice line items. ([94d646e](https://github.com/Metronome-Industries/metronome-node/commit/94d646ee3194043ffb43969b8c3c8427b6760ee1)) ([ad105dd](https://github.com/Metronome-Industries/metronome-node/commit/ad105dd2fbdc4070780c698c244c3d6be261d023)) ([ea3d22d](https://github.com/Metronome-Industries/metronome-node/commit/ea3d22d19cfd91bc3117198f7119bf40ea9a6245))
* Rename billable metrics with `client.v1.billableMetrics.update()`. ([397c698](https://github.com/Metronome-Industries/metronome-node/commit/397c698847c8a53967ff15bd3d5e13b6870aa046))
* Rename subscriptions through contract edits and read subscription product custom fields. ([d70f181](https://github.com/Metronome-Industries/metronome-node/commit/d70f1816637cc8d58e32d0cf4be5554e1ade67b5)) ([fd04231](https://github.com/Metronome-Industries/metronome-node/commit/fd042312940b00a4383e015b67715cd7a6fb0fa5))
* Read credit creation timestamps from the `created_at` response field. ([a4da635](https://github.com/Metronome-Industries/metronome-node/commit/a4da635743879c1fed4639efbe713e409a92324e))
* Create and archive custom pricing units with `client.v1.pricingUnits.create()` and `.archive()`. ([7ead972](https://github.com/Metronome-Industries/metronome-node/commit/7ead9720f8be01f28c6b7da6ea5a8d7b601add74))
* Manage offset lifecycle notifications and list system notification types through `client.v2.notifications`; use `client.v2.notifications.offset.edit()` to enable or disable system notifications. ([6b55f3b](https://github.com/Metronome-Industries/metronome-node/commit/6b55f3b7012d1900b982b52ec23171376e82cc4d))
* Create package usage-statement schedules with `day: 'CUSTOM_DATE'`. ([b85fd25](https://github.com/Metronome-Industries/metronome-node/commit/b85fd25840c9ae29bef80c0c8e7d02c9a3d616d7))
* Configure the duration, rate type, and rollover fraction of commits created by prepaid balance thresholds. ([8f85b7a](https://github.com/Metronome-Industries/metronome-node/commit/8f85b7a9314c0b8504bc93b58cc6454214688c6f))
* Allow composite products to incorporate spend from other composite products with `include_composite_spend`. ([7d52216](https://github.com/Metronome-Industries/metronome-node/commit/7d5221641c04235a9d1038c0eefdc9864a608def))
* Prevent duplicate manual balance entries with `uniqueness_key`. ([99ad4d1](https://github.com/Metronome-Industries/metronome-node/commit/99ad4d196ad2d4f625fe79e8485cff0c0b73e776))
* Include historical commit invoices when listing invoices with `include_historical_commit_invoices`. ([01e7deb](https://github.com/Metronome-Industries/metronome-node/commit/01e7deba3e1752da3e80ed9f90fce13aaf9c78d7))

### Documentation

* Clarify that archiving an already-archived threshold notification succeeds. ([ccf9401](https://github.com/Metronome-Industries/metronome-node/commit/ccf94013629b3cb73a2e9be269a0444dec77215b))
* Update support portal links in contract documentation. ([bc0121a](https://github.com/Metronome-Industries/metronome-node/commit/bc0121a57fd9b11bd571c76ab1bc9f235ae56d74))

### Breaking changes

* `client.v1.contracts.list()` and `client.v2.contracts.list()` now return cursor-paginated pages. Iterate with `for await (const contract of client.v2.contracts.list(params))` to retrieve every contract, or use `page.getNextPage()` after awaiting the first page. Replace removed `ContractListResponse` type imports with `ContractsBodyCursorPageCursorField` (v1) or `ContractV2sBodyCursorPageCursorField` (v2). ([4134a04](https://github.com/Metronome-Industries/metronome-node/commit/4134a0497996d5462782515080b916cccd8d5039))
* Recurring commit and credit response models now require `anchor_date`, and subscription response models require `created_at`. Add these timestamps to typed fixtures or mocks you construct. ([d66b0d7](https://github.com/Metronome-Industries/metronome-node/commit/d66b0d7fcdd2f8e60a6bca77e0b09d9ca73f1072)) ([01e7deb](https://github.com/Metronome-Industries/metronome-node/commit/01e7deba3e1752da3e80ed9f90fce13aaf9c78d7))
* The `@metronome/mcp` server source and installation instructions have been removed from this repository. Existing published versions remain available; consumers who need that server should pin an existing version while arranging a replacement. ([c2464b0](https://github.com/Metronome-Industries/metronome-node/commit/c2464b02b4317650f637be5ef2903458443d9b31))

<!-- metronome-sdk-release-descriptions:end -->