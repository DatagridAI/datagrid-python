# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .tool import Tool
from .._models import BaseModel

__all__ = ["Agent", "Corpus", "CorpusCorpusKnowledgeItem", "CorpusCorpusPageItem", "McpServer"]


class CorpusCorpusKnowledgeItem(BaseModel):
    knowledge_id: str
    """The ID of the knowledge to include in the corpus."""

    type: Literal["knowledge"]
    """The type of the corpus item. Always 'knowledge' for knowledge items."""


class CorpusCorpusPageItem(BaseModel):
    page_id: str
    """The ID of the page to include in the corpus."""

    type: Literal["page"]
    """The type of the corpus item. Always 'page' for page items."""


Corpus: TypeAlias = Union[CorpusCorpusKnowledgeItem, CorpusCorpusPageItem]


class McpServer(BaseModel):
    base_url: str

    credential_id: Optional[str] = None

    name: str

    object: Literal["agent_mcp_server"]

    server_id: str

    status: str

    last_synced_at: Optional[datetime] = None

    tool_count: Optional[int] = None


class Agent(BaseModel):
    id: str
    """Unique identifier for the agent"""

    agent_model: Union[
        Literal["magpie-1.1", "magpie-1.1-flash", "magpie-2.0", "magpie-2.5", "magpie-2.5-flash", "llm-only"], str
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

    corpus: Optional[List[Corpus]] = None
    """Array of corpus items the agent should use during the converse.

    When omitted, all knowledge is used.
    """

    created_at: datetime
    """The ISO string for when the agent was created"""

    custom_prompt: Optional[str] = None
    """Use custom prompt to instruct the style and formatting of the agent's response"""

    description: Optional[str] = None
    """The description of the agent"""

    emoji: Optional[str] = None
    """The emoji of the agent"""

    knowledge_ids: Optional[List[str]] = None
    """Deprecated, use corpus instead.

    Array of Knowledge IDs the agent should use during the converse. When omitted,
    all knowledge is used.
    """

    llm_model: Union[
        Literal[
            "gemini-3.5-flash",
            "gemini-3.1-flash-lite",
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
    ]
    """The LLM used to generate responses.

    Deprecated Gemini 2.0 Flash ids are accepted for backward compatibility and
    automatically run as gemini-3.1-flash-lite.
    """

    mcp_servers: List[McpServer]
    """Registered MCP servers enabled for this agent."""

    name: str
    """The name of the agent"""

    object: Literal["agent"]
    """The object type, always 'agent'"""

    planning_prompt: Optional[str] = None
    """
    Define the planning strategy your AI Agent should use when breaking down tasks
    and solving problems
    """

    system_prompt: Optional[str] = None
    """Directs your AI Agent's operational behavior."""

    tools: List[Tool]
    """Tools that this agent can use."""
