# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .tool_name import ToolName
from .tool_param import ToolParam

__all__ = [
    "AgentUpdateParams",
    "Corpus",
    "CorpusCorpusKnowledgeItem",
    "CorpusCorpusPageItem",
    "DisabledTool",
    "McpServer",
    "Tool",
]


class AgentUpdateParams(TypedDict, total=False):
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

    corpus: Optional[Iterable[Corpus]]
    """Array of corpus items the agent should use during the converse.

    When omitted, all knowledge is used.
    """

    custom_prompt: Optional[str]
    """Use custom prompt to instruct the style and formatting of the agent's response"""

    description: Optional[str]
    """The description of the agent"""

    disabled_tools: Optional[SequenceNotStr[DisabledTool]]
    """Array of the agent tools to disable.

    Disabling is performed after the 'agent_tools' rules are applied. For example,
    agent_tools: null and disabled_tools: [data_analysis] will enable everything but
    the data_analysis tool. If nothing or [] is provided, nothing is disabled and
    therefore only the agent_tools setting is relevant.
    """

    emoji: Optional[str]
    """The emoji of the agent"""

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

    mcp_servers: Optional[Iterable[McpServer]]
    """Registered MCP servers to enable for this agent."""

    name: Optional[str]
    """The name of the agent"""

    planning_prompt: Optional[str]
    """
    Define the planning strategy your AI Agent should use when breaking down tasks
    and solving problems
    """

    system_prompt: Optional[str]
    """Directs your AI Agent's operational behavior."""

    tools: Optional[SequenceNotStr[Tool]]
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


class CorpusCorpusKnowledgeItem(TypedDict, total=False):
    knowledge_id: Required[str]
    """The ID of the knowledge to include in the corpus."""

    type: Required[Literal["knowledge"]]
    """The type of the corpus item. Always 'knowledge' for knowledge items."""


class CorpusCorpusPageItem(TypedDict, total=False):
    page_id: Required[str]
    """The ID of the page to include in the corpus."""

    type: Required[Literal["page"]]
    """The type of the corpus item. Always 'page' for page items."""


Corpus: TypeAlias = Union[CorpusCorpusKnowledgeItem, CorpusCorpusPageItem]

DisabledTool: TypeAlias = Union[ToolName, ToolParam]


class McpServer(TypedDict, total=False):
    server_id: Required[str]

    credential_id: Optional[str]


Tool: TypeAlias = Union[ToolName, ToolParam]
