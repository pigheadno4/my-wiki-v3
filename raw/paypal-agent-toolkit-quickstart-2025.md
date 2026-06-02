<!-- Source URL: https://docs.paypal.ai/developer/tools/ai/agent-toolkit-quickstart -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent toolkit quickstart guide

PayPal's agent toolkit supports the integration of PayPal APIs into AI agent workflows using <a href="https://aws.amazon.com/bedrock/" target="_blank">Amazon Bedrock</a>, <a href="https://www.crewai.com/" target="_blank">CrewAI</a>, <a href="https://www.langchain.com/" target="_blank">LangChain</a>, <a href="https://modelcontextprotocol.io/introduction/" target="_blank">Model Context Protocol (MCP)</a>, <a href="https://github.com/openai/openai-agents-python/" target="_blank">OpenAI's Agents SDK</a>, and <a href="https://sdk.vercel.ai/" target="_blank">Vercel's AI SDK</a>. This guide provides a step-by-step process for setting up the server, building a basic conversational front-end interface using Next.js, and testing the integration.

> **Note:** For a complete list of the tools that PayPal's agent toolkit includes, see the <a href="https://www.paypal.ai/tools/agent-tools-ref/" target="_blank">agent tools reference</a>.

## Key features

The agent toolkit from PayPal enables you to:

- **Integrate with PayPal APIs** to access orders, invoices, subscriptions, shipment tracking, transaction details, and dispute management through pre-built functions.
- **Develop with your preferred tools**, including:
  - AI agent frameworks, such as <a href="https://aws.amazon.com/bedrock/" target="_blank">Amazon Bedrock</a>, <a href="https://www.crewai.com/" target="_blank">CrewAI</a>, <a href="https://www.langchain.com/" target="_blank">LangChain</a>, <a href="https://modelcontextprotocol.io/introduction/" target="_blank">Model Context Protocol (MCP)</a>, <a href="https://github.com/openai/openai-agents-python/" target="_blank">OpenAI's Agents SDK</a>, and <a href="https://sdk.vercel.ai/" target="_blank">Vercel's AI SDK</a>
  - Multiple languages, including TypeScript and Python
- **Build custom agent capabilities** to extend core PayPal features and connect with other toolkits to create multi-step agent workflows.

## Agents for commerce

When you implement AI agents strategically, you can:

- Provide consistent customer support.
- Deliver personalized product recommendations.
- Create smoother payment processes.

The key is finding the right balance between efficient automation and the human touch that customers value. Keep human oversight in areas where personal judgment matters most, while letting AI handle repetitive tasks.

These examples are for a fictional online coffee bean store, but they illustrate some of the ways that any seller might use agents.

<Accordion title="Examples of agent types for an online store">
  | Agent type              | Purpose                                                          | Key capabilities                                                                                                                                                                                                                                                                                   |
  | ----------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Customer support        | Handle common customer inquiries and support requests.           | - Answer product questions, such as coffee origins, roast levels, or flavor profiles. <br /> - Process order status inquiries. <br /> - Explain shipping policies and timeframes. <br /> - Handle basic troubleshooting for website or order issues.                                               |
  | Product recommendation  | Help customers discover coffee beans that suit their preferences | - Ask questions about taste preferences, such as acidity, body, and flavor notes. <br /> - Consider brewing methods, such as French press, espresso, or pour-over. <br /> - Suggest complementary products, such as filters or brewing equipment. <br /> - Track and learn from customer patterns. |
  | Order processing        | Streamline the purchase process and handle order-related tasks.  | - Guide customers through checkout. <br /> - Process shipping address validation. <br /> - Handle inventory checks and back-order information. <br /> - Provide shipping cost estimates and delivery timeframes.                                                                                   |
  | Shipping                | Automate processing of end-to-end shipping capabilities.         | - Search open orders and generate shipping labels. <br /> - Print shipping labels. <br /> - Share shipping tracking information with customers and partners. <br /> - Interact with a returns agent to generate return shipping labels.                                                            |
  | Returns and exchanges   | Facilitate smooth return and exchange processes.                 | - Process return requests and generate return labels. <br /> - Explain return policies and eligibility. <br /> - Process refunds or store credits. <br /> - Gather feedback about reasons for returns.                                                                                             |
  | Subscription management | Handle coffee subscription services and recurring orders.        | - Process subscription sign-ups and modifications. <br /> - Handle requests to pause or resume a subscription. <br /> - Manage delivery frequency changes. <br /> - Process subscription cancellations with retention options.                                                                     |
</Accordion>

## Best practices

To have the best integration experience, use these tips:

- **Sandbox environment:** Always use the sandbox environment for initial testing to avoid real transactions.
- **API keys:** Keep your client ID, client secret, and API keys secure. Do not hard-code them in your source files.
- **Environment variables:** Use environment variables to manage sensitive data.
- **Error handling:** Implement error handling to ensure reliable integration.
- **System prompts:** Use well-defined system prompts to control the behavior of the agent.

## 1. Set up your environment

To prepare for an integration, set up your environment first.

### Python

Before you start, confirm that you have the prerequisites:

- Python 3.11 or higher
- pip (Python package manager)
- A <a href="https://developer.paypal.com/home/" target="_blank">PayPal developer</a> account for API credentials

1. Set up a Python virtual environment.

```bash theme={null}
# Step 1: Create a virtual environment
python -m venv venv

# Step 2: Activate the virtual environment
# On MacOS or Linux:
source venv/bin/activate
# For Windows:
# venv\Scripts\activate
```

2. Install the required dependencies.

```bash theme={null}
pip install -r requirements.txt
```

> **Note:** For details about dependencies for a specific platform and the requirements.txt file, see the section for that platform on this page.

3. Install the agent toolkit.

```bash theme={null}
pip install paypal-agent-toolkit
```

### TypeScript

1. Download and install Node.js version 18 or later from the official <a href="https://nodejs.org/en/" target="_blank">Node.js</a> website.
2. To install the agent toolkit, run `npm install @paypal/agent-toolkit`, or download the package from the <a href="https://github.com/paypal/agent-toolkit/" target="_blank">GitHub repo</a>.
3. Get your PayPal account's <a href="https://developer.paypal.com/api/rest/#link-getclientidandclientsecret/" target="_blank">client ID and secret</a> from <a href="https://developer.paypal.com/dashboard/" target="_blank">PayPal Developer Dashboard</a>. You'll need them to configure this library.

## 2. Integrate

PayPal's agent toolkit supports <a href="https://aws.amazon.com/bedrock/" target="_blank">Amazon Bedrock</a>, <a href="https://www.crewai.com/" target="_blank">CrewAI</a>, <a href="https://www.langchain.com/" target="_blank">LangChain</a>, <a href="https://modelcontextprotocol.io/introduction/" target="_blank">Model Context Protocol (MCP)</a>, <a href="https://github.com/openai/openai-agents-python/" target="_blank">OpenAI's Agents SDK</a>, and <a href="https://sdk.vercel.ai/" target="_blank">Vercel's AI SDK</a>. It works with LLM providers that support function calling and is compatible with TypeScript and Python.

For integration steps, see the section for your AI platform:

- [Amazon Bedrock](#amazon-bedrock)
- [CrewAI SDK](#crewai-sdk)
- [LangChain AI SDK](#langchain-ai-sdk)
- [Model Context Protocol](#model-context-protocol)
- [OpenAI Agents SDK](#openai-agents-sdk)
- [Vercel AI SDK](#vercel-ai-sdk)

For information about setting up the front end for testing any of these integrations, see [Build the front end](#3-build-the-front-end).

### Amazon Bedrock

Complete the following steps to integrate the agent toolkit from PayPal with Amazon Bedrock. Amazon Bedrock passes the agent toolkit as a list of tools.

1. Set your environment variables by creating a .env file in `/typescript/examples/bedrock/`.

```bash theme={null}
# Bedrock Configuration
AWS_ACCESS_KEY_ID=<YOUR_AWS_API_KEY>
AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESS_KEY>

# PayPal Configuration
PAYPAL_CLIENT_ID=<YOUR_PAYPAL_CLIENT_ID>
PAYPAL_SECRET=<YOUR_PAYPAL_SECRET>
```

2. Add <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-templates-and-examples.html/" target="_blank">prompts</a> to `userMessage` in `/typescript/examples/bedrock/index.ts`.

3. Import PayPal's agent toolkit into your code.

> **Note:** Update placeholder values, like `YOUR_PAYPAL_CLIENT_ID` and `YOUR_PAYPAL_SECRET`, with the app credentials from <a href="https://developer.paypal.com/dashboard/" target="_blank">PayPal Developer Dashboard</a>.

```python theme={null}
import { PayPalAgentToolkit, ALL_TOOLS_ENABLED } from '@paypal/agent-toolkit/bedrock';
import { BedrockRuntimeClient, ConverseCommand, Message } from '@aws-sdk/client-bedrock-runtime';

const ppConfig = {
    clientId: process.env.YOUR_PAYPAL_CLIENT_ID || '',
    clientSecret: process.env.YOUR_PAYPAL_SECRET || '',
    configuration: {
        actions: ALL_TOOLS_ENABLED,
        context: {
            sandbox: true,
        }
    }
}

const paypalToolkit = new PayPalAgentToolkit(ppConfig);
```

4. Create a message, and send it to the model.

```python theme={null}
    let messages: Message[] = [
      {
          role: "user",
          content: [{ text: userMessage }],
      }
  ]

  const response = await client.send(
    new ConverseCommand({
        modelId: modelId,
        messages: messages,
        toolConfig: {
            tools: tools
        }
    }),
  );
```

5. Call tools to complete the user's request.

```typescript theme={null}
const reply = response.output?.message;

const toolsCalled = reply.content?.filter((content) => content.toolUse);

if (toolsCalled && toolsCalled.length > 0) {
  const toolResults = await Promise.all(
    toolsCalled.map(async (toolBlock) => {
      const toolCall = {
        toolUseId: toolBlock.toolUse.toolUseId,
        name: toolBlock.toolUse.name,
        input: toolBlock.toolUse.input,
      };
      const result = await paypalToolkit.handleToolCall(toolCall);
      return {
        toolResult: {
          toolUseId: result.toolUseId,
          content: result.content,
        },
      };
    }),
  );
}
```

### CrewAI SDK

Complete the following steps to integrate the agent toolkit from PayPal with CrewAI. CrewAI passes the agent toolkit as a list of tools.

1. Set your environment variables.

> **Note:** Update placeholder values, like `YOUR_PAYPAL_CLIENT_ID` and `YOUR_PAYPAL_SECRET`, with the app credentials from <a href="https://developer.paypal.com/dashboard/" target="_blank">PayPal Developer Dashboard</a>.

```bash theme={null}
# OpenAI Configuration
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
OPENAI_API_VERSION=<YOUR_OPENAI_API_VERSION>

# PayPal Configuration
PAYPAL_CLIENT_ID=<YOUR_PAYPAL_CLIENT_ID>
PAYPAL_SECRET=<YOUR_PAYPAL_SECRET>
```

2. Install CrewAI SDK.

```bash theme={null}
pip install crewai==0.76.2
pip install crewai-tools==0.13.2
pip install setuptools
```

> **Recommended:** Create a file called requirements.txt and add these dependencies to that file: <br />

`paypal-agent-toolkit` <br />
`# CrewAI` <br />
`crewai==0.76.2` <br />
`crewai-tools==0.13.2`

3. Import PayPal Agent toolkit into your code.

> **Note:** Update placeholder values, like `YOUR_PAYPAL_CLIENT_ID` and `YOUR_PAYPAL_SECRET`, with the app credentials from <a href="https://developer.paypal.com/dashboard/" target="_blank">PayPal Developer Dashboard</a>.

```python theme={null}
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import os
from crewai import Agent, Crew, Task

# from dotenv import load_dotenv
from paypal_agent_toolkit.crewai.toolkit import PayPalToolkit
from paypal_agent_toolkit.shared.configuration import Configuration, Context


#uncomment after setting the env file
# load_dotenv()
PAYPAL_CLIENT_ID = os.getenv("YOUR_PAYPAL_CLIENT_ID")
PAYPAL_SECRET = os.getenv("YOUR_PAYPAL_CLIENT_SECRET")
OPENAI_API_VERSION = "2024-02-15-preview"


toolkit = PayPalToolkit(
    client_id=PAYPAL_CLIENT_ID,
    secret=PAYPAL_SECRET,
    configuration=Configuration(
        actions={"orders": {"create": True, "get": True, "capture": True}},
        context=Context(sandbox=True)
    )
)

agent = Agent(
    role="PayPal Assistant",
    goal="Help users create and manage PayPal transactions",
    backstory="You are a finance assistant skilled in PayPal operations.",
    tools=toolkit.get_tools(),
    allow_delegation=False
)

task = Task(
    description="Create an PayPal order for $50 for Premium News service.",
    expected_output="A PayPal order ID",
    agent=agent
)

crew = Crew(agents=[agent], tasks=[task], verbose=True,
    planning=True,)

result = crew.kickoff()
print(result)
```

### LangChain AI SDK

Complete the following steps to integrate the agent toolkit from PayPal with the LangChain AI SDK. LangChain AI SDK passes the agent toolkit as a list of tools.

1. Set your environment variables:

> **Note:** Update placeholder values, like `YOUR_PAYPAL_CLIENT_ID` and `YOUR_PAYPAL_SECRET`, with the app credentials from <a href="https://developer.paypal.com/dashboard/" target="_blank">PayPal Developer Dashboard</a>.

```bash theme={null}
# OpenAI Configuration
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
OPENAI_API_VERSION=<YOUR_OPENAI_API_VERSION>

# PayPal Configuration
PAYPAL_CLIENT_ID=<YOUR_PAYPAL_CLIENT_ID>
PAYPAL_SECRET=<YOUR_PAYPAL_SECRET>
```

2. Install LangChain AI SDK.

```bash theme={null}
pip install langchain==0.3.23
pip install langchain-openai==0.2.2
```

> **Recommended:** Create a file called requirements.txt and add these dependencies to that file: <br />

`paypal-agent-toolkit` <br />
`# LangChain` <br />
`langchain==0.3.23` <br />
`langchain-openai==0.2.2` <br />

3. Import PayPal Agent toolkit into your code.

> **Note:** Update placeholder values, like `YOUR_PAYPAL_CLIENT_ID` and `YOUR_PAYPAL_SECRET`, with the app credentials from <a href="https://developer.paypal.com/dashboard/" target="_blank">PayPal Developer Dashboard</a>.

```python theme={null}
import os
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

from paypal_agent_toolkit.langchain.toolkit import PayPalToolkit
from paypal_agent_toolkit.shared.configuration import Configuration, Context

#uncomment after setting the env file
# load_dotenv()
PAYPAL_CLIENT_ID = os.getenv("YOUR_PAYPAL_CLIENT_ID")
PAYPAL_CLIENT_SECRET = os.getenv("YOUR_PAYPAL_CLIENT_SECRET")
OPENAI_API_VERSION = "2024-02-15-preview"


# --- STEP 1: Setup OpenAI LLM ---
llm = ChatOpenAI(
    temperature=0.3,
    model="gpt-4o",  # or "gpt-3.5-turbo"
)


# --- STEP 2: Setup PayPal Configuration ---
configuration = Configuration(
    actions={
        "orders": {
            "create": True,
            "get": True,
            "capture": True,
        }
    },
    context=Context(
        sandbox=True
    )
)


# --- STEP 3: Build PayPal Toolkit ---
toolkit = PayPalToolkit(client_id=PAYPAL_CLIENT_ID, secret=PAYPAL_CLIENT_SECRET, configuration = configuration)
tools = toolkit.get_tools()



# --- STEP 4: Initialize LangChain Agent ---
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)


# --- STEP 5: Run Agent with Prompt ---
if __name__ == "__main__":
    prompt = "Create an PayPal order for $50 for Premium News service."
    result = agent.run(prompt)
    print("Agent Output:", result)
```

### Model Context Protocol

<a href="https://modelcontextprotocol.io/introduction/" target="_blank">Model Context Protocol (MCP)</a> supports managing and passing relevant information to models with appropriate context, so they operate properly within a given scope. Using this technology, PayPal developed an MCP server to enable merchants to use natural language with their favorite MCP client.

To install the MCP server in a local configuration:

1. Update the configuration file in your favorite MCP client:
   - Open the MCP client.
   - In the configuration settings for the client, locate the external tools or connectors configuration section, and add the PayPal connector configuration that follows this procedure. In Claude, for example, you add this to `~/Claude/claude_desktop_config.json`.

   ```json theme={null}
   {
     "mcpServers": {
       "paypal": {
         "command": "npx",
         "args": ["-y", "@paypal/mcp", "--tools=all"],
         "env": {
           "PAYPAL_ACCESS_TOKEN": "YOUR_PAYPAL_ACCESS_TOKEN",
           "PAYPAL_ENVIRONMENT": "SANDBOX"
         }
       }
     }
   }
   ```

   > **Note:** Update placeholder values, like `YOUR_PAYPAL_CLIENT_ID` and `YOUR_PAYPAL_SECRET`, with the app credentials from <a href="https://developer.paypal.com/dashboard/" target="_blank">PayPal Developer Dashboard</a>. Alternatively, you can set the `PAYPAL_ACCESS_TOKEN` as an environment variable. You also can pass it as an argument using `--access-token` in `args`.<br /><br />Set the `PAYPAL_ENVIRONMENT` to `SANDBOX` for testing or `PRODUCTION` for your production environment.
   - To update the configuration, run:

   ```bash theme={null}
   npm install @paypal/mcp
   ```

2. Test the integration:
   1. Quit and restart the MCP client to apply your changes.
   2. Ask the MCP client to perform one of the supported tasks. For example, ask the MCP client to list your PayPal invoices for the last month.

> **Tip:** If your test doesn't produce the results you expect, try <a href="https://modelcontextprotocol.io/tools/debugging" target="_blank">these ideas from the Model Context Protocol site</a>.

### OpenAI Agents SDK

Complete the following steps to integrate PayPal's agent toolkit with OpenAI's Agents SDK. Agents SDK passes the agent toolkit as a list of tools.

#### Generate OpenAI API keys

Complete the following steps to generate and store your OpenAI keys to use in your integration with PayPal's agent toolkit.

1. Create an <a href="https://platform.openai.com/signup/" target="_blank">OpenAI</a> account, and complete all registration steps.
2. Generate your API keys:
3. Log into OpenAI, and navigate to the <a href="https://platform.openai.com/account/api-keys" target="_blank">API Keys</a> section of your account.
4. Select **Create a new secret key**.
5. Save the generated key securely. You use this key in your `env.local` file for your agent toolkit integration.

#### Complete the OpenAI integration

Complete the following steps to integrate PayPal's agent toolkit with OpenAI's Agents SDK. Agents SDK passes the agent toolkit as a list of tools.

1. Import PayPal's agent toolkit into your code.

> **Note:** Update placeholder values, like `YOUR_PAYPAL_CLIENT_ID` and `YOUR_PAYPAL_SECRET`, with the app credentials from <a href="https://developer.paypal.com/dashboard/" target="_blank">PayPal Developer Dashboard</a>.

```python theme={null}
from paypal_agent_toolkit.openai.toolkit import PayPalToolkit
from paypal_agent_toolkit.shared.configuration import Configuration, Context

configuration = Configuration(
    actions={
        "orders": {
            "create": True,
            "get": True,
            "capture": True,
        }
    },
    context=Context(
        sandbox=True
    )
)

# Initialize toolkit
toolkit = PayPalToolkit(client_id=YOUR_PAYPAL_CLIENT_ID, secret=YOUR_PAYPAL_SECRET, configuration = configuration)
```

2. You can use the agent toolkit's functions and other tools as your integration requires.

```python theme={null}
from agents import Agent

tools = toolkit.get_tools()

agent = Agent(
    name="PayPal Assistant",
    instructions="""
    You're a helpful assistant specialized in managing PayPal transactions:
    - To create orders, invoke create_order.
    - After approval by user, invoke capture_order.
    - To check an order status, invoke get_order_status.
    """,
    tools=tools
)
```

### Vercel AI SDK

Complete the following steps to integrate PayPal's agent toolkit with Vercel's AI SDK. Vercel's AI SDK passes the agent toolkit as a list of tools.

1. Set your environment variables.

> **Note:** Update placeholder values, like `YOUR_PAYPAL_CLIENT_ID` and `YOUR_PAYPAL_SECRET`, with the app credentials from <a href="https://developer.paypal.com/dashboard/" target="_blank">PayPal Developer Dashboard</a>.

```bash theme={null}
# OpenAI Configuration
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
OPENAI_API_VERSION=<YOUR_OPENAI_API_VERSION>

# PayPal Configuration
PAYPAL_CLIENT_ID=<YOUR_PAYPAL_CLIENT_ID>
PAYPAL_SECRET=<YOUR_PAYPAL_SECRET>
```

2. Install Vercel AI SDK.

```bash theme={null}
npm install ai @ai-sdk/openai
```

3. Import PayPal's agent toolkit into your code.

> **Note:** Update placeholder values, like `YOUR_PAYPAL_CLIENT_ID` and `YOUR_PAYPAL_SECRET`, with the app credentials from <a href="https://developer.paypal.com/dashboard/" target="_blank">PayPal Developer Dashboard</a>.

```javascript theme={null}
import { PayPalAgentToolkit } from "@paypal/agent-toolkit/ai-sdk";
const paypalToolkit = new PayPalAgentToolkit({
  clientId: process.env.PAYPAL_CLIENT_ID,
  clientSecret: process.env.PAYPAL_CLIENT_SECRET,
  configuration: {
    actions: {
      invoices: {
        create: true,
        list: true,
        send: true,
        sendReminder: true,
        cancel: true,
        generateQRC: true,
      },
      products: { create: true, list: true, update: true },
      subscriptionPlans: { create: true, list: true, show: true },
      shipment: { create: true, show: true, cancel: true },
      orders: { create: true, get: true },
      disputes: { list: true, get: true },
    },
  },
});
```

4. Use PayPal's agent toolkit's functions and other tools as your integration requires.

```javascript theme={null}
const llm: LanguageModelV1 = getModel(); // The model to be used with ai-sdk
const { text: response } = await generateText({
  model: llm,
  tools: {
    ...paypalToolkit.getTools(),
    // Extend with other tools
  },
  maxSteps: 10,
  prompt: `Create an order for $50 for custom handcrafted item and get the payment link.`,
});
```

## 3. Build the front end

Using the Next.js framework, complete the following tasks.

### Create a Next.js project

If you don't have a Next.js app already, create one.

```typescript theme={null}
npx create-next-app@latest paypal-integration --typescript
cd paypal-integration
npm install
```

### Create a chat interface

Modify app/page.tsx to create a chat interface for interacting with the PayPal agent.

```typescript theme={null}
import React, { useState } from 'react';

const Home: React.FC = () => {
  const [message, setMessage] = useState('');
  const [chat, setChat] = useState<{ sender: 'user' | 'agent'; text: string }[]>([]);
  const handleSendMessage = async () => {
    setChat((prevChat) => [...prevChat, { sender: 'user', text: message }]);
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message }),
    });
    const data = await response.json();
    setChat((prevChat) => [...prevChat, { sender: 'agent', text: data.response }]);
    setMessage('');
  };

  return (
    <div>
      <h1>PayPal Chat Interface</h1>
      <div>
        {chat.map((c, index) => (
          <div key={index} className={c.sender}>
            {c.sender}: {c.text}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={handleSendMessage}>Send</button>
    </div>
  );
};

export default Home;
```

## 4. Test the integration

After you finish the integration, test it by setting up an API route.

Execute this code in `app/api/chat/route.ts`.

```typescript theme={null}
import { NextRequest, NextResponse } from "next/server";
import { openai } from "@ai-sdk/openai";
import { generateText } from "ai";
import { PayPalAgentToolkit } from "@paypal/agent-toolkit/ai-sdk";

const paypalToolkit = new PayPalAgentToolkit({
  clientId: process.env.PAYPAL_CLIENT_ID,
  clientSecret: process.env.PAYPAL_CLIENT_SECRET,
  configuration: {
    actions: {
      orders: { create: true, get: true },
      invoices: { create: true, list: true },
      // Extend with other actions as needed
    },
  },
});

export async function POST(req: NextRequest) {
  try {
    const { message } = await req.json();

    // Define System Prompt for controlling behavior
    const systemPrompt =
      "This is a PayPal agent. You are tasked with handling PayPal orders and providing relevant information.";

    const { text: response } = await generateText({
      model: openai("gpt-4o"),
      tools: paypalToolkit.getTools(),
      maxSteps: 10,
      prompt: message,
      system: systemPrompt,
    });

    return NextResponse.json({ response });
  } catch (error) {
    const errorMessage =
      error instanceof Error ? error.message : "An unknown error occurred";

    return NextResponse.json({ error: errorMessage }, { status: 500 });
  }
}
```

## 5. Start the application

To start the application, execute `npm run dev`, and visit [http://localhost:3000](http://localhost:3000).

## Additional resources

For more information about the concepts covered here, see these additional documents:

- <a href="https://developer.paypal.com/docs/api/overview/" target="_blank">PayPal developer documentation</a>
- <a href="https://github.com/paypal/agent-toolkit/tree/main/typescript/examples/" target="_blank">GitHub examples</a>
- <a href="https://aws.amazon.com/bedrock/" target="_blank">Amazon Bedrock</a>
- <a href="https://www.crewai.com/" target="_blank">CrewAI documentation</a>
- <a href="https://www.langchain.com/" target="_blank">LangChain documentation</a>
- <a href="https://modelcontextprotocol.io/introduction/" target="_blank">Model Context Protocol (MCP)</a>
- <a href="https://github.com/openai/openai-agents-python/" target="_blank">OpenAI Agents SDK</a>
- <a href="https://sdk.vercel.ai/" target="_blank">Vercel AI SDK</a>
