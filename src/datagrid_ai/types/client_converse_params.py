# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .tool_name import ToolName
from .tool_param import ToolParam

__all__ = [
    "ClientConverseParams",
    "PromptInputItemList",
    "PromptInputItemListContentInputMessageContentList",
    "PromptInputItemListContentInputMessageContentListInputText",
    "PromptInputItemListContentInputMessageContentListInputFile",
    "PromptInputItemListContentInputMessageContentListInputSecret",
    "PromptInputItemListContentInputMessageContentListInputKnowledge",
    "PromptInputItemListContentInputMessageContentListInputPage",
    "AgentRouting",
    "AgentRoutingAuto",
    "AgentRoutingManual",
    "AgentRoutingManualTarget",
    "AgentRoutingManualTargetAgentConfigWithID",
    "AgentRoutingManualTargetAgentConfigWithIDCorpus",
    "AgentRoutingManualTargetAgentConfigWithIDCorpusCorpusKnowledgeItem",
    "AgentRoutingManualTargetAgentConfigWithIDCorpusCorpusPageItem",
    "AgentRoutingManualTargetAgentConfigWithIDDisabledTool",
    "AgentRoutingManualTargetAgentConfigWithIDMcpServer",
    "AgentRoutingManualTargetAgentConfigWithIDTool",
    "Config",
    "ConfigAgentTool",
    "ConfigCorpus",
    "ConfigCorpusCorpusKnowledgeItem",
    "ConfigCorpusCorpusPageItem",
    "ConfigDisabledAgentTool",
    "ConfigDisabledTool",
    "ConfigMcpServer",
    "ConfigTool",
    "Text",
    "User",
]


class ClientConverseParams(TypedDict, total=False):
    prompt: Required[Union[str, Iterable[PromptInputItemList]]]
    """A text prompt to send to the agent."""

    agent_id: Optional[str]
    """The ID of the agent that should be used for the converse.

    When omitted and a `conversation_id` is provided, the conversation's existing
    agent assignments are preserved. When omitted without a `conversation_id`, a new
    conversation is created with the default agent.
    """

    agent_routing: Optional[AgentRouting]
    """Determines how the API routes the converse request to an agent."""

    chat_mode: Optional[Literal["auto", "full_agent", "light_agent", "llm_router"]]
    """Controls how the agent processes the request for this turn.

    Matches the chat mode selector in the Datagrid web app: **Execute**
    (`full_agent`), **Extended** (`light_agent`), **Ask** (`llm_router`). When set
    to `auto`, the router jointly predicts the best agent and concrete mode
    (`full_agent` / `light_agent` / `llm_router`) per message. When set to a
    concrete mode, that mode is used directly. When omitted, the mode is determined
    by the `agent_model` in `config`.
    """

    config: Optional[Config]
    """Override the agent config for this converse call.

    This is applied as a partial override.
    """

    conversation_id: Optional[str]
    """The ID of the present conversation to use.

    If it's not provided - a new conversation will be created.
    """

    current_view_content: Optional[str]
    """
    A datagrid file URI pointing to content the user is currently viewing on screen
    (e.g., a web page, document, or dashboard rendered as markdown). The agent uses
    this context to resolve ambiguous queries like 'what is this about?' or 'review
    this'. The content is automatically summarized and made available to the agent.
    """

    generate_citations: Optional[bool]
    """Determines whether the response should include citations.

    When enabled, the agent will generate citations for factual statements.
    """

    generate_title: Optional[bool]
    """Determines whether generated_title metadata should be included.

    Defaults to false. generated_title is emitted only when this flag is explicitly
    true.
    """

    include_steps: Optional[bool]
    """
    When set to false, tool call and reasoning step events are omitted from SSE
    streams. Non-streaming responses always include the tool_calls and reasoning
    fields (as null when empty).
    """

    secret_ids: Optional[SequenceNotStr[str]]
    """Array of secret ID's to be included in the context.

    The secret value will be appended to the prompt but not stored in conversation
    history.
    """

    stream: Optional[bool]
    """Determines the response type of the converse.

    Response is the Server-Sent Events if stream is set to true.
    """

    text: Optional[Text]
    """
    Contains the format property used to specify the structured output schema
    (`text.format`). Structured output is supported for all `agent_model` values and
    `chat_mode` settings when `text.format` is provided (same JSON Schema mechanism
    everywhere). **Ask** in the web app maps to `chat_mode` `magpie-2.5-flash`;.
    """

    user: Optional[User]
    """User information override for converse calls.

    All fields are optional - only provided fields will override the default user
    information.
    """


class PromptInputItemListContentInputMessageContentListInputText(TypedDict, total=False):
    """A text input to the model."""

    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class PromptInputItemListContentInputMessageContentListInputFile(TypedDict, total=False):
    """A file input to the model."""

    file_id: Required[str]
    """The ID of the file to be sent to the model."""

    type: Required[Literal["input_file"]]
    """The type of the input item. Always `input_file`."""


class PromptInputItemListContentInputMessageContentListInputSecret(TypedDict, total=False):
    """A secret input to the model."""

    secret_id: Required[str]
    """The ID of the secret to be sent to the model."""

    type: Required[Literal["input_secret"]]
    """The type of the input item. Always `input_secret`."""


class PromptInputItemListContentInputMessageContentListInputKnowledge(TypedDict, total=False):
    """A knowledge reference input to the model.

    This references knowledge by ID. The knowledge will be made accessible to the agent, and will be included in the prompt provided to the agent. The position of this reference relative to other text of the input impact the agent's interpretation.
    """

    knowledge_id: Required[str]
    """The ID of the knowledge to be referenced."""

    type: Required[Literal["input_knowledge"]]
    """The type of the input item. Always `input_knowledge`."""


class PromptInputItemListContentInputMessageContentListInputPage(TypedDict, total=False):
    """A page reference input to the model.

    This references a page by ID. The page, and all knowledge under it, will be made accessible to the agent, and a reference to the page will be included in the prompt provided to the agent. The position of this reference relative to other text of the input will impact the agent's interpretation.
    """

    page_id: Required[str]
    """The ID of the page to be referenced."""

    type: Required[Literal["input_page"]]
    """The type of the input item. Always `input_page`."""


PromptInputItemListContentInputMessageContentList: TypeAlias = Union[
    PromptInputItemListContentInputMessageContentListInputText,
    PromptInputItemListContentInputMessageContentListInputFile,
    PromptInputItemListContentInputMessageContentListInputSecret,
    PromptInputItemListContentInputMessageContentListInputKnowledge,
    PromptInputItemListContentInputMessageContentListInputPage,
]


class PromptInputItemList(TypedDict, total=False):
    """
    A message input to the model with a role indicating instruction following `agent` role are presumed to have been generated by the model in previous interactions.
    """

    content: Required[Union[str, Iterable[PromptInputItemListContentInputMessageContentList]]]
    """Text, file or secret input to the agent."""

    role: Required[Literal["user"]]
    """The role of the message input. Always `user`."""

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class AgentRoutingAuto(TypedDict, total=False):
    """The API automatically selects the best agent from the entire Teamspace."""

    mode: Required[Literal["auto"]]
    """The API selects the best agent from the entire Teamspace."""


class AgentRoutingManualTargetAgentConfigWithIDCorpusCorpusKnowledgeItem(TypedDict, total=False):
    knowledge_id: Required[str]
    """The ID of the knowledge to include in the corpus."""

    type: Required[Literal["knowledge"]]
    """The type of the corpus item. Always 'knowledge' for knowledge items."""


class AgentRoutingManualTargetAgentConfigWithIDCorpusCorpusPageItem(TypedDict, total=False):
    page_id: Required[str]
    """The ID of the page to include in the corpus."""

    type: Required[Literal["page"]]
    """The type of the corpus item. Always 'page' for page items."""


AgentRoutingManualTargetAgentConfigWithIDCorpus: TypeAlias = Union[
    AgentRoutingManualTargetAgentConfigWithIDCorpusCorpusKnowledgeItem,
    AgentRoutingManualTargetAgentConfigWithIDCorpusCorpusPageItem,
]

AgentRoutingManualTargetAgentConfigWithIDDisabledTool: TypeAlias = Union[ToolName, ToolParam]


class AgentRoutingManualTargetAgentConfigWithIDMcpServer(TypedDict, total=False):
    server_id: Required[str]

    credential_id: Optional[str]


AgentRoutingManualTargetAgentConfigWithIDTool: TypeAlias = Union[ToolName, ToolParam]


class AgentRoutingManualTargetAgentConfigWithID(TypedDict, total=False):
    agent_id: str
    """The ID of the agent to use for routing."""

    agent_model: Union[
        Literal["magpie-1.1", "magpie-1.1-flash", "magpie-2.0", "magpie-2.5", "magpie-2.5-flash", "llm-only"], str, None
    ]
    """The agent model determines the processing mode for Converse requests.

    The Datagrid web app exposes **Ask**, **Extended**, and **Execute** as Converse
    **`chat_mode`** (`llm_router`, `light_agent`, `full_agent`). The values below
    set **`config.agent_model`** (model tier and tool limits)—use both fields when
    mirroring in-app behavior.

    **Execute** (full tool use, planning, and multi-step reasoning; aligns with
    **Execute** in the web app / `full_agent`):

    - `magpie-2.0` — Default. Full agent model with proactive planning and
      reasoning.
    - `magpie-2.5` — Beta. Latest full-agent model — faster, more adaptable, and
      built to handle a broader range of real-world tasks.
    - `magpie-1.1` — Previous-generation full agent model.

    **Extended** (search-focused; aligns with **Extended** in the web app /
    `light_agent`; not **Ask**):

    - `magpie-1.1-flash` — Fast model optimized for RAG use cases. Only supports the
      `semantic_search` tool. A 400 error will be returned if other tools are
      specified.

    **Direct LLM** (no tool execution; **`agent_model` only**—**Ask** in the web app
    is `chat_mode: llm_router`, not `magpie-1.1-flash`):

    - `llm-only` — Runs a direct LLM conversation with no planning or tool calls. A
      400 error will be returned if tools are specified.

    Can also accept any custom string value for future model versions.
    """

    corpus: Optional[Iterable[AgentRoutingManualTargetAgentConfigWithIDCorpus]]
    """Array of corpus items the agent should use during the converse.

    When omitted, all knowledge is used.
    """

    custom_prompt: Optional[str]
    """Use custom prompt to instruct the style and formatting of the agent's response"""

    disabled_tools: Optional[SequenceNotStr[AgentRoutingManualTargetAgentConfigWithIDDisabledTool]]
    """Array of the agent tools to disable.

    Disabling is performed after the 'agent_tools' rules are applied. For example,
    agent_tools: null and disabled_tools: [data_analysis] will enable everything but
    the data_analysis tool. If nothing or [] is provided, nothing is disabled and
    therefore only the agent_tools setting is relevant.
    """

    knowledge_ids: Optional[SequenceNotStr[str]]
    """Deprecated, use corpus instead.

    Array of Knowledge IDs the agent should use during the converse. When omitted,
    all knowledge is used.
    """

    llm_model: Union[
        Literal[
            "gemini-3-pro-preview",
            "gemini-3.1-pro-preview",
            "gemini-3-flash-preview",
            "gemini-2.5-pro",
            "gemini-2.5-pro-preview-05-06",
            "gemini-2.5-flash",
            "gemini-2.5-flash-preview-04-17",
            "gemini-2.5-flash-native-audio-preview-12-2025",
            "gemini-2.5-flash-lite",
            "gpt-5",
            "gpt-5.1",
            "gemini-2.0-flash-001",
            "gemini-2.0-flash",
            "gemini-1.5-pro-001",
            "gemini-1.5-pro-002",
            "gemini-1.5-flash-002",
            "gemini-1.5-flash-001",
            "chatgpt-4o-latest",
            "gpt-4o",
            "gpt-4",
            "gpt-4-turbo",
            "gpt-4o-mini",
        ],
        str,
        None,
    ]
    """The LLM used to generate responses."""

    mcp_servers: Optional[Iterable[AgentRoutingManualTargetAgentConfigWithIDMcpServer]]
    """Registered MCP servers to enable for this agent."""

    planning_prompt: Optional[str]
    """
    Define the planning strategy your AI Agent should use when breaking down tasks
    and solving problems
    """

    system_prompt: Optional[str]
    """Directs your AI Agent's operational behavior."""

    temperature: Optional[float]
    """Sampling temperature for model output.

    Lower values are more deterministic; higher values are more diverse.
    """

    tools: Optional[SequenceNotStr[AgentRoutingManualTargetAgentConfigWithIDTool]]
    """Array of the agent tools to enable.

    If not provided, or null is provided - default tools of the agent are used. If
    empty list provided - none of the tools are used. When connection_id is set for
    a tool, it will use that specific connection instead of the default one.

    **Structured outputs (Converse):** All `agent_model` values support JSON Schema
    constrained responses via **`text.format`** on the Converse request.

    **Tool availability by agent model** (aligned with in-app **Execute** /
    **Extended** / direct LLM; see Converse `chat_mode` for **Ask** vs
    `agent_model`):

    - **Execute** (`magpie-2.0`, `magpie-2.5`, `magpie-1.1`): All tools below are
      available.
    - **Extended** (`magpie-1.1-flash`): Only `semantic_search` is supported.
      Requests specifying other tools will be rejected with a 400 error.
    - **Direct LLM** (`llm-only`): No tools are executed. Requests specifying tools
      will be rejected with a 400 error.

    Knowledge management tools:

    - data_analysis: Answer statistical or analytical questions like "Show my
      quarterly revenue growth"
    - semantic_search: Search knowledge through natural language queries.
    - agent_memory: Agents can remember experiences, conversations and user
      preferences.
    - schema_info: Helps the Agent understand column names and dataset purpose.
      Avoid disabling
    - table_info: Allow the AI Agent to get information about datasets and schemas
    - create_dataset: Agents respond with data tables

    Actions:

    - calendar: Allow the Agent to access and make changes to your Google Calendar
    - schedule_recurring_message_tool: Eliminate busywork such as: "Send a summary
      of today's meetings at 5pm on workdays"

    Data processing tools:

    - data_classification: Agents handle queries like "Label these emails as high,
      medium, or low priority"
    - data_extraction: Helps the agent understand data from other tools. Avoid
      disabling
    - image_detection: Extract information from images using AI
    - pdf_extraction: Extraction of information from PDFs using AI

    Enhanced response tools:

    - connect_data: Agents provide buttons to import data in response to queries
      like "Connect Hubspot"
    - download_data: Agents handle queries like "download the table as CSV"

    Web tools:

    - web_search: Agents search the internet, and provide links to their sources
    - fetch_url: Fetch URL content
    - company_prospect_researcher: Agents provide information about companies
    - people_prospect_researcher: Agents provide information about people
    """


AgentRoutingManualTarget: TypeAlias = Union[str, AgentRoutingManualTargetAgentConfigWithID]


class AgentRoutingManual(TypedDict, total=False):
    """The API selects the best agent from the specific list you provide."""

    mode: Required[Literal["manual"]]
    """The API selects the best agent from the specific list you provide."""

    targets: Required[SequenceNotStr[AgentRoutingManualTarget]]
    """Limit the selection pool to these specific agents.

    Each item may be an agent ID string or an inline agent config object.
    """


AgentRouting: TypeAlias = Union[AgentRoutingAuto, AgentRoutingManual]

ConfigAgentTool: TypeAlias = Union[ToolName, ToolParam]


class ConfigCorpusCorpusKnowledgeItem(TypedDict, total=False):
    knowledge_id: Required[str]
    """The ID of the knowledge to include in the corpus."""

    type: Required[Literal["knowledge"]]
    """The type of the corpus item. Always 'knowledge' for knowledge items."""


class ConfigCorpusCorpusPageItem(TypedDict, total=False):
    page_id: Required[str]
    """The ID of the page to include in the corpus."""

    type: Required[Literal["page"]]
    """The type of the corpus item. Always 'page' for page items."""


ConfigCorpus: TypeAlias = Union[ConfigCorpusCorpusKnowledgeItem, ConfigCorpusCorpusPageItem]

ConfigDisabledAgentTool: TypeAlias = Union[ToolName, ToolParam]

ConfigDisabledTool: TypeAlias = Union[ToolName, ToolParam]


class ConfigMcpServer(TypedDict, total=False):
    server_id: Required[str]

    server_label: Required[str]
    """A unique label to identify this MCP server. Used for tool namespacing."""

    server_url: Required[str]
    """The HTTPS URL of the MCP streamable HTTP endpoint."""

    type: Required[Literal["inline_mcp"]]
    """The type of MCP server configuration.

    Use 'inline_mcp' for server configs passed directly in the request.
    """

    authorization: Optional[str]
    """
    Value sent in the `Authorization` header when calling the MCP server (e.g.,
    'Bearer <token>').
    """

    credential_id: Optional[str]

    server_description: Optional[str]
    """Optional description of what this MCP server provides."""


ConfigTool: TypeAlias = Union[ToolName, ToolParam]


class Config(TypedDict, total=False):
    """Override the agent config for this converse call.

    This is applied as a partial override.
    """

    agent_model: Union[
        Literal["magpie-1.1", "magpie-1.1-flash", "magpie-2.0", "magpie-2.5", "magpie-2.5-flash", "llm-only"], str, None
    ]
    """The agent model determines the processing mode for Converse requests.

    The Datagrid web app exposes **Ask**, **Extended**, and **Execute** as Converse
    **`chat_mode`** (`llm_router`, `light_agent`, `full_agent`). The values below
    set **`config.agent_model`** (model tier and tool limits)—use both fields when
    mirroring in-app behavior.

    **Execute** (full tool use, planning, and multi-step reasoning; aligns with
    **Execute** in the web app / `full_agent`):

    - `magpie-2.0` — Default. Full agent model with proactive planning and
      reasoning.
    - `magpie-2.5` — Beta. Latest full-agent model — faster, more adaptable, and
      built to handle a broader range of real-world tasks.
    - `magpie-1.1` — Previous-generation full agent model.

    **Extended** (search-focused; aligns with **Extended** in the web app /
    `light_agent`; not **Ask**):

    - `magpie-1.1-flash` — Fast model optimized for RAG use cases. Only supports the
      `semantic_search` tool. A 400 error will be returned if other tools are
      specified.

    **Direct LLM** (no tool execution; **`agent_model` only**—**Ask** in the web app
    is `chat_mode: llm_router`, not `magpie-1.1-flash`):

    - `llm-only` — Runs a direct LLM conversation with no planning or tool calls. A
      400 error will be returned if tools are specified.

    Can also accept any custom string value for future model versions.
    """

    agent_tools: Optional[SequenceNotStr[ConfigAgentTool]]
    """Deprecated, use tools instead"""

    corpus: Optional[Iterable[ConfigCorpus]]
    """Array of corpus items the agent should use during the converse.

    When omitted, all knowledge is used.
    """

    custom_prompt: Optional[str]
    """Use custom prompt to instruct the style and formatting of the agent's response"""

    disabled_agent_tools: Optional[SequenceNotStr[ConfigDisabledAgentTool]]
    """Deprecated, use disabled_tools instead.

    If not provided - no tools are disabled.
    """

    disabled_tools: Optional[SequenceNotStr[ConfigDisabledTool]]
    """Array of the agent tools to disable.

    Disabling is performed after the 'agent_tools' rules are applied. For example,
    agent_tools: null and disabled_tools: [data_analysis] will enable everything but
    the data_analysis tool. If nothing or [] is provided, nothing is disabled and
    therefore only the agent_tools setting is relevant.
    """

    knowledge_ids: Optional[SequenceNotStr[str]]
    """Deprecated, use corpus instead.

    Array of Knowledge IDs the agent should use during the converse. When omitted,
    all knowledge is used.
    """

    llm_model: Union[
        Literal[
            "gemini-3-pro-preview",
            "gemini-3.1-pro-preview",
            "gemini-3-flash-preview",
            "gemini-2.5-pro",
            "gemini-2.5-pro-preview-05-06",
            "gemini-2.5-flash",
            "gemini-2.5-flash-preview-04-17",
            "gemini-2.5-flash-native-audio-preview-12-2025",
            "gemini-2.5-flash-lite",
            "gpt-5",
            "gpt-5.1",
            "gemini-2.0-flash-001",
            "gemini-2.0-flash",
            "gemini-1.5-pro-001",
            "gemini-1.5-pro-002",
            "gemini-1.5-flash-002",
            "gemini-1.5-flash-001",
            "chatgpt-4o-latest",
            "gpt-4o",
            "gpt-4",
            "gpt-4-turbo",
            "gpt-4o-mini",
        ],
        str,
        None,
    ]
    """The LLM used to generate responses."""

    mcp_servers: Optional[Iterable[ConfigMcpServer]]
    """**BETA**: This feature is in beta and the schema may change.

    Array of MCP (Model Context Protocol) server configurations to enable for this
    converse call. Each MCP server provides additional tools that the agent can use
    during the conversation.

    Datagrid handles the full MCP lifecycle automatically: `initialize`,
    `notifications/initialized`, then `tools/list` / `tools/call` with
    `MCP-Session-Id` and `MCP-Protocol-Version` headers.
    """

    planning_prompt: Optional[str]
    """
    Define the planning strategy your AI Agent should use when breaking down tasks
    and solving problems
    """

    system_prompt: Optional[str]
    """Directs your AI Agent's operational behavior."""

    temperature: Optional[float]
    """Sampling temperature for model output.

    Lower values are more deterministic; higher values are more diverse.
    """

    tools: Optional[SequenceNotStr[ConfigTool]]
    """Array of the agent tools to enable.

    If not provided, or null is provided - default tools of the agent are used. If
    empty list provided - none of the tools are used. When connection_id is set for
    a tool, it will use that specific connection instead of the default one.

    **Structured outputs (Converse):** All `agent_model` values support JSON Schema
    constrained responses via **`text.format`** on the Converse request.

    **Tool availability by agent model** (aligned with in-app **Execute** /
    **Extended** / direct LLM; see Converse `chat_mode` for **Ask** vs
    `agent_model`):

    - **Execute** (`magpie-2.0`, `magpie-2.5`, `magpie-1.1`): All tools below are
      available.
    - **Extended** (`magpie-1.1-flash`): Only `semantic_search` is supported.
      Requests specifying other tools will be rejected with a 400 error.
    - **Direct LLM** (`llm-only`): No tools are executed. Requests specifying tools
      will be rejected with a 400 error.

    Knowledge management tools:

    - data_analysis: Answer statistical or analytical questions like "Show my
      quarterly revenue growth"
    - semantic_search: Search knowledge through natural language queries.
    - agent_memory: Agents can remember experiences, conversations and user
      preferences.
    - schema_info: Helps the Agent understand column names and dataset purpose.
      Avoid disabling
    - table_info: Allow the AI Agent to get information about datasets and schemas
    - create_dataset: Agents respond with data tables

    Actions:

    - calendar: Allow the Agent to access and make changes to your Google Calendar
    - schedule_recurring_message_tool: Eliminate busywork such as: "Send a summary
      of today's meetings at 5pm on workdays"

    Data processing tools:

    - data_classification: Agents handle queries like "Label these emails as high,
      medium, or low priority"
    - data_extraction: Helps the agent understand data from other tools. Avoid
      disabling
    - image_detection: Extract information from images using AI
    - pdf_extraction: Extraction of information from PDFs using AI

    Enhanced response tools:

    - connect_data: Agents provide buttons to import data in response to queries
      like "Connect Hubspot"
    - download_data: Agents handle queries like "download the table as CSV"

    Web tools:

    - web_search: Agents search the internet, and provide links to their sources
    - fetch_url: Fetch URL content
    - company_prospect_researcher: Agents provide information about companies
    - people_prospect_researcher: Agents provide information about people
    """


class Text(TypedDict, total=False):
    """
    Contains the format property used to specify the structured output schema (`text.format`).
    Structured output is supported for all `agent_model` values and `chat_mode` settings when `text.format` is provided (same JSON Schema mechanism everywhere). **Ask** in the web app maps to `chat_mode` `magpie-2.5-flash`;.
    """

    format: object
    """
    The converse response will be a JSON string object, that adheres to the provided
    JSON schema.

    ```javascript
    const exampleJsonSchema = {
      $id: "movie_info",
      title: "movie_info",
      type: "object",
      properties: {
        name: {
          type: "string",
          description: "The name of the movie",
        },
        director: {
          type: "string",
          description: "The director of the movie",
        },
        release_year: {
          type: "number",
          description: "The year the movie was released",
        },
      },
      required: ["name", "director", "release_year"],
      additionalProperties: false,
    };

    const response = await datagrid.converse({
      prompt: "What movie won best picture at the 2001 oscars?",
      text: { format: exampleJsonSchema },
    });

    // Example response: "{ "name": "Gladiator", "director": "Ridley Scott", "release_year": 2000 }"
    const parsedResponse = JSON.parse(response.content[0].text);
    ```
    """


class User(TypedDict, total=False):
    """User information override for converse calls.

    All fields are optional - only provided fields will override the default user information.
    """

    email: Optional[str]
    """Override the user's email for this converse call."""

    first_name: Optional[str]
    """Override the user's first name for this converse call."""

    last_name: Optional[str]
    """Override the user's last name for this converse call."""
