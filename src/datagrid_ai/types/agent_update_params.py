# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from .agent_tools import AgentTools
from .agent_tool_item_param import AgentToolItemParam

__all__ = ["AgentUpdateParams", "AgentTool"]


class AgentUpdateParams(TypedDict, total=False):
    agent_model: Optional[Literal["magpie-1", "magpie-1.1", "magpie-1.1-flash"]]
    """The version of Datagrid's agent brain."""

    agent_tools: Optional[Iterable[AgentTool]]
    """Array of the agent tools to enable.

    If not provided - default tools of the agent are used. If empty list provided -
    none of the tools are used. If null provided - all tools are used. When
    connection_id is set for a tool, it will use that specific connection instead of
    the default one.

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

    custom_prompt: Optional[str]
    """Use custom prompt to instruct the style and formatting of the agent's response"""

    description: Optional[str]
    """Description of the agent"""

    disabled_agent_tools: Optional[List[AgentTools]]
    """Array of the agent tools to disable.

    Disabling is performed after the 'agent_tools' rules are applied. For example,
    agent_tools: null and disabled_agent_tools: [data_analysis] will enable
    everything but the data_analysis tool. If nothing or [] is provided, nothing is
    disabled and therefore only the agent_tools setting is relevant.
    """

    knowledge_ids: Optional[List[str]]
    """Array of Knowledge IDs the agent should use during the converse.

    If not provided - default settings are used. If null provided - all available
    knowledge is used.
    """

    llm_model: Optional[
        Literal[
            "gemini-1.5-flash-001",
            "gemini-1.5-flash-002",
            "gemini-2.0-flash-001",
            "gemini-2.0-flash",
            "gemini-2.5-flash-preview-04-17",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-1.5-pro-001",
            "gemini-1.5-pro-002",
            "gemini-2.5-pro-preview-05-06",
            "gemini-2.5-pro",
            "chatgpt-4o-latest",
            "gpt-4",
            "gpt-4-turbo",
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-5",
        ]
    ]
    """The LLM used to generate responses."""

    name: str
    """The name of the agent"""

    planning_prompt: Optional[str]
    """
    Define the planning strategy your AI Agent should use when breaking down tasks
    and solving problems
    """

    system_prompt: Optional[str]
    """Directs your AI Agent's operational behavior."""


AgentTool: TypeAlias = Union[AgentTools, AgentToolItemParam]
