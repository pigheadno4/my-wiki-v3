# api-explorer-recurring-latest-post-scheduleaccountupdater fixed retrieval check

Read log: entire pinned raw lines 1–172 read as one numbered, untruncated contiguous range. SHA-256 verified: 23e0dcf1ff3bedc19b01b8b60bf9777b61d53138025925718269e15a1aa7fdba.

Canonical source: [[source-adyen-api-explorer-recurring-latest-post-scheduleaccountupdater]] — https://docs.adyen.com/api-explorer/Recurring/latest/post/scheduleAccountUpdater

- Q1: For `Recurring/latest/post/scheduleAccountUpdater`, what purpose, API/version and object identity does this captured page establish, and what central required/conditional inputs or prerequisites govern its use?
  - Answer: Captured Recurring TEST v68 `POST /scheduleAccountUpdater` schedules Account Updater using card details or a recurring-detail reference plus shopper reference (5–14). `merchantAccount` and call `reference` are table-required; `card` or the two-reference pair is conditionally needed (18–34). The prose says all card subfields are mandatory, while the table marks them optional and the card example omits some (9, 23–30, 38–50); this snapshot cannot settle an exact card-field minimum. It does not separately state body requiredness.
- Q2: For `Recurring/latest/post/scheduleAccountUpdater`, what does the documented response or failure establish, and which lifecycle, deletion/propagation, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?
  - Answer: HTTP 200 with `result: Success` establishes successful scheduling, with a request `pspReference`; otherwise `result` holds an error message (61–70). A token-data example has 422 “RecurringShopper not found” (162–172); the 400/401/403/422/500 tables are at 73–140. No completed card update, token propagation, notification, payment authorization/capture/settlement, deletion or retry timing is established. The only listed server is TEST Recurring/v68 (13–14), not evidence of LIVE/current availability or Checkout behavior.
