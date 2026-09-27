# Braintree C18 execution notes

Status: COMPLETE. Exact ten-page manifest approved and initialized 2026-09-27.
Runtime started `2026-09-27T08:10:35Z` and completed
`2026-09-27T08:54:50Z`: **44m15s wall clock**. Concurrent worker/reviewer
windows overlap; the journal does not provide reliable per-stage durations,
so the elapsed span must not be divided into invented stage costs.

The ten sources cover Control Panel credentials, search, users/roles, custom
fields and Vault overview/create/update/card verification. The batch held
1,194 file lines, compared with C17's 666. Five first reviews approved; five
requested narrow corrections. All retries used targeted review, with no new
full review, rejection, invalid handoff or raw-hash change. There were 15
worker starts, ten full reviews and five targeted reviews. The fixed query
audit passed 20/20 questions; one post-promotion cross-page password-minimum
gap needed independently reviewed paired warnings and evidence links.

The practical improvement target is first-pass precision: choose quotes that
cover each retained consequential boundary; scope user/admin actions narrowly;
and declare every fully read opposing raw when a source states a cross-page
conflict. These checks belong in existing worker/reviewer handoffs, not a new
registry or testing layer. Catalog/count aggregation and the single close
validation remained coordinator-owned. See `quality-audit.md` and
`query-audit-a.md` through `query-audit-e.md` for evidence.

C18 stops here. Commit/push, collection and another campaign require separate
authorization.
