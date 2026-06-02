<!-- Source URL: https://docs.stripe.com/building-with-ai -->
<!-- Fetched: 2026-04-20 -->

# Build on Stripe with AI

Use AI in your Stripe integration workflow.

You can use AI agents to assist in the building of Stripe integrations. We provide a set of tools and best practices if you use LLMs during development.

## Install the Stripe MCP server

Stripe’s Model Context Protocol (MCP) server defines a set of [tools](https://docs.stripe.com/mcp.md#tools) that AI agents can use to interact with the Stripe API and search our knowledge base.

See [install instructions](https://docs.stripe.com/mcp.md).

## Install agent skills

[Agent skills](https://agentskills.io/home) are instructions that agents can follow to create more accurate integrations. Stripe has a catalog of skills that instruct agents on best Stripe integration practices. They’re available from different marketplaces, as well hosted at [https://docs.stripe.com/.well-known/skills/index.json](https://docs.stripe.com/.well-known/skills/index.json.md).

#### npx

Run this in your project folder. Note that manually added skills don’t auto-update, so you’ll need to pull updates yourself.

```bash
npx skills add https://docs.stripe.com --yes
```

#### Claude Code

Run this in your project folder.

```bash
claude /plugin install stripe@claude-plugins-official
```

#### Cursor

Install the [Stripe plugin](https://cursor.com/marketplace/stripe) from the Cursor marketplace.

## Use AI developer platforms

Agent-assisted coding platforms let you create apps and websites by describing what you want to an LLM. These platforms can also help you build a payments integration without writing code.

Some platforms, such as [Base44](https://base44.com/), [Manus](https://manus.ai/), [Replit](https://replit.com/), and [v0](https://v0.app/), provide custom Stripe integrations so you can try Stripe without creating an account. If you’re building an agent-assisted developer platform, you can offer a similar experience with [claimable sandboxes](https://docs.stripe.com/sandboxes/claimable-sandboxes.md).

## Plain text docs

You can access all of our documentation as plain text Markdown files by adding `.md` to the end of any URL. For example, you can find the plain text version of this page at <https://docs.stripe.com/building-with-ai.md>.

This helps AI tools and agents consume our content and allows you to copy and paste the entire contents of a doc into an LLM. This format is preferable to scraping or copying from our HTML and JavaScript-rendered pages because:

- Plain text contains fewer formatting tokens.
- Content that isn’t rendered in the default view (for example, it’s hidden in a tab) of a given page is rendered in the plain text version.
- LLMs can parse and understand markdown hierarchy.

We also host an [/llms.txt file](https://docs.stripe.com/llms.txt.md) which instructs AI tools and agents how to retrieve the plain text versions of our pages. The `/llms.txt` file is an [emerging standard](https://llmstxt.org/) for making websites and content more accessible to LLMs.

## VS Code AI Assistant

If you’re a Visual Studio Code user, you can install the [Stripe VS Code extension](https://docs.stripe.com/stripe-vscode.md) to access our AI Assistant.

With the Stripe AI Assistant, you can:

- Get immediate answers about the Stripe API and products
- Receive code suggestions tailored to your integration
- Ask follow-up questions for more detailed information
- Access knowledge from the Stripe documentation and the Stripe developer community

To get started with the Stripe AI assistant:

1. Make sure you have the Stripe VS Code extension installed.
1. Navigate to the Stripe extension UI
1. Under **AI Assistant** click **Ask a question**.
   - If you’re a Copilot user, this opens the Copilot chat where you can @-mention `@stripe`. In the input field, talk to the Stripe-specific assistant using `@stripe` followed by your question.
   - If you’re not a Copilot user, it opens a chat UI where you can talk to the Stripe LLM directly.

## See also

- [Stripe CLI](https://docs.stripe.com/stripe-cli.md)
- [Stripe for Visual Studio Code](https://docs.stripe.com/stripe-vscode.md)
