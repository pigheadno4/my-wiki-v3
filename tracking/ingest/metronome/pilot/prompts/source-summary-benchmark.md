# Metronome Source-Summary Benchmark Prompt

You are evaluating one model as a candidate for the logical `cheap_ingester` role.

## Assignment

Read the assigned Metronome raw Markdown file completely, from the first line through the final line. Process only that file. Return one JSON object and do not edit repository files.

The coordinator will provide:

- `job_id`: the immutable pilot job identifier
- `raw_path`: one path from `tracking/ingest/metronome/pilot/benchmark-set.json`
- `canonical_url`: the canonical documentation URL represented by that raw file

## Required JSON shape

```json
{
  "job_id": "pilot-job-id",
  "raw_path": "repository-relative raw path",
  "canonical_url": "https://docs.metronome.com/...",
  "title": "Concise source-page title",
  "grounding_quotes": [
    {
      "line_start": 1,
      "line_end": 1,
      "text": "exact verbatim text from those lines",
      "supports": "short description of the claim this quote grounds"
    }
  ],
  "overview": "Two to four source-grounded sentences.",
  "key_takeaways": ["source-grounded takeaway"],
  "details": [
    {
      "heading": "descriptive section heading",
      "facts": ["source-grounded fact"]
    }
  ],
  "suggested_tags": ["metronome"],
  "suggested_metronome_concepts": ["metronome-prefixed concept slug"],
  "proposed_raw_link": "[[raw/metronome/path-without-md|collection-date snapshot]]",
  "unsupported_claim_self_check": []
}
```

## Quality gates

- Include 3–5 grounding quotes.
- Every quote must match the specified one-based raw line range exactly, including multi-line text joined with newline characters.
- Every overview sentence, takeaway, and detail must be supported by the assigned file.
- Use only Metronome-specific concept suggestions; do not create generic cross-provider concepts in this task.
- The raw link must be path-qualified and omit the `.md` extension inside the wikilink target.
- Put any claim you cannot support in `unsupported_claim_self_check`; do not include it in the overview, takeaways, or details.

The JSON is a draft artifact, not a canonical wiki page. The coordinator performs the concept audit and decides whether to promote or repair it.

When the coordinator supplies deterministic validation errors, correct only those errors while re-reading the assigned raw file. Do not copy or infer facts from the error messages.

## Prohibited actions

- Do not edit files.
- Do not read or summarize multiple raw pages.
- Do not use web search or outside knowledge.
- Do not update company, index, log, comparison, analysis, or generic concept pages.
- Do not infer Stripe acquisition history, pricing, limits, API behavior, or product positioning unless the assigned raw file states it.
- Do not wrap the JSON in Markdown fences or add prose before or after it.
