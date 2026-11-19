---
title: "Stripe — Flexible Payment Features Beta-to-GA Migration"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-flexible-features-migration-2026.md"
tags: [stripe, incremental-authorization, overcapture, extended-authorization, multicapture, migration, ic-plus]
---

## Summary

Migration guide for four IC+ flexible payment features moving from private beta to general availability. Documents API parameter name changes, new mandatory request steps, and behavioral differences. For new integrations, see each feature's dedicated guide.

## Breaking Changes by Feature

### Incremental Authorization

| | Before (beta) | After (GA) |
| --- | --- | --- |
| Request param | `request_incremental_authorization_support: true` (optional) | `request_incremental_authorization: 'if_available'` **(mandatory)** |
| Response field | `incremental_authorization_supported: true/false` | `incremental_authorization.status: 'available'/'unavailable'` |

Increment endpoint (`increment_authorization`) unchanged.

### Overcapture

| | Before (beta) | After (GA) |
| --- | --- | --- |
| Request param | None (didn't exist) | `request_overcapture: 'if_available'` **(new mandatory step)** |
| Response | No status field | `overcapture.status` + `overcapture.maximum_amount_capturable` |

Capture endpoint unchanged.

### Extended Authorization

| | Before (beta) | After (GA) |
| --- | --- | --- |
| Request param | None (didn't exist) | `request_extended_authorization: 'if_available'` **(new mandatory step)** |
| Response | `capture_before` sometimes absent | `capture_before` always present; `extended_authorization.status: 'enabled'/'disabled'` |

Capture endpoint unchanged.

### Multicapture

| | Before (beta) | After (GA) |
| --- | --- | --- |
| Request param | None | `request_multicapture: 'if_available'` **(new mandatory step)**; requires `multicapture_migrate_to_ga_from_beta` API version header during transition |
| `final_capture: false` on full amount | Silently captured and succeeded | **Returns HTTP 400 error** |
| Non-final capture webhook | `charge.captured` | `charge.updated` |
| Final capture webhook | `charge.captured` | `charge.captured` (unchanged) |
| Uncaptured funds refund | Created | **Not created** when `final_capture: true` |

## Combining Overcapture + Incremental Auth

Can request both at creation. Strategy:
1. If desired capture ≤ `overcapture.maximum_amount_capturable` → overcapture directly
2. If desired capture > max → use incremental auth first, then capture

## Related Pages

- [[stripe-incremental-authorization]] — incremental auth concept page
- [[stripe-overcapture]] — overcapture concept page
- [[stripe-extended-authorization]] — extended auth concept page
- [[stripe-multicapture]] — multicapture concept page

## Raw Sources

- [[stripe-flexible-features-migration-2026]] — verbatim migration guide (549 lines)
