# Metronome Campaign 04 Retrospective

Status: `complete`

## Outcome

Campaign 04 approved all five jobs with no terminal rejection. Five invalid attempts were retained:

- Three candidates copied a `.md` fetch URL into source frontmatter instead of the manifest's canonical URL.
- One candidate returned extra top-level fields and omitted required fixed-schema content.
- One candidate omitted quote locations.

The existing validator rejected every malformed result before review or promotion. The retry loop then isolated each failure while unrelated jobs continued.

## Root cause

The trusted job state already contained the canonical URL and the validator already enforced all three boundaries. However, the generated worker order and persisted `input.json` omitted the canonical URL and did not carry a literal result contract. Native dispatch therefore depended on manually restating values and schema requirements in prose. That handoff gap, rather than routing tier or validator weakness, explains the deterministic failures.

## Minimal correction

Future worker orders now carry:

- the trusted `canonical_url`;
- the exact allowed top-level result keys;
- the required quote keys; and
- three short preflight assertions covering those fields.

The coordinator should pass the generated order directly to the worker. Historical attempts remain unchanged as evidence.

## Deliberate non-goals

- No new model classifier or routing tier.
- No new campaign state, journal, retry, or monitoring behavior.
- No weakening or duplication of Sol review.
- No migration of completed campaign artifacts.

## Next-campaign check

Run another bounded campaign using the same routing and review flow. Treat fewer mechanical schema retries as evidence that the handoff improved; continue to judge content quality through full Sol review rather than schema compliance alone.
