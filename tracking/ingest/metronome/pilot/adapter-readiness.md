# Metronome Model Adapter Readiness

Checked: 2026-07-14

Command:

```bash
/Users/tengtao/gstack/.agents/skills/gstack/bin/gstack-model-benchmark \
  --prompt "unused, dry-run" \
  --models claude,gpt,gemini \
  --dry-run
```

## Result

| Adapter | State | Detail |
| --- | --- | --- |
| Claude | Not ready | No Claude authentication found; requires an interactive `claude` login or `ANTHROPIC_API_KEY`. |
| GPT | Ready | Codex adapter is authenticated. |
| Gemini | Not ready | Gemini CLI is not installed on `PATH`. |

The dry run sent no prompts and incurred no model cost. The available gstack adapter set covers Claude, GPT, and Gemini; it does not provide DeepSeek or MiniMax adapters. Those providers require a separate compatible runtime or adapter before they can participate in this benchmark.

No paid benchmark has been run. An explicit provider choice is required before a real model call.
