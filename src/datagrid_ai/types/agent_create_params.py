# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .tool_param import ToolParam

__all__ = ["AgentCreateParams", "DisabledTool", "Tool"]


class AgentCreateParams(TypedDict, total=False):
    agent_model: Union[Literal["magpie-1.1", "magpie-1.1-flash", "magpie-1", "magpie-2.0"], str, None]
    """The version of Datagrid's agent brain.

    - magpie-1.1 is the default and most powerful model.
    - magpie-1.1-flash is a faster model useful for RAG usecases, it currently only
      supports semantic_search tool. Structured outputs are not supported with this
      model.
    - Can also accept any custom string value for future model versions.
    - Magpie-2.0 our latest agentic model with more proactive planning and reasoning
      capabilities.
    """

    custom_prompt: Optional[str]
    """Use custom prompt to instruct the style and formatting of the agent's response"""

    description: Optional[str]
    """The description of the agent"""

    disabled_tools: Optional[List[DisabledTool]]
    """Array of the agent tools to disable.

    Disabling is performed after the 'agent_tools' rules are applied. For example,
    agent_tools: null and disabled_tools: [data_analysis] will enable everything but
    the data_analysis tool. If nothing or [] is provided, nothing is disabled and
    therefore only the agent_tools setting is relevant.
    """

    knowledge_ids: Optional[SequenceNotStr[str]]
    """Array of Knowledge IDs the agent should use during the converse.

    When ommited, all knowledge is used.
    """

    llm_model: Union[
        Literal[
            "gemini-3-pro-preview",
            "gemini-2.5-pro",
            "gemini-2.5-pro-preview-05-06",
            "gemini-2.5-flash",
            "gemini-2.5-flash-preview-04-17",
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

    name: Optional[str]
    """The name of the agent"""

    planning_prompt: Optional[str]
    """
    Define the planning strategy your AI Agent should use when breaking down tasks
    and solving problems
    """

    system_prompt: Optional[str]
    """Directs your AI Agent's operational behavior."""

    tools: Optional[List[Tool]]
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


DisabledTool: TypeAlias = Union[
    Literal[
        "data_analysis",
        "semantic_search",
        "agent_memory",
        "schema_info",
        "table_info",
        "create_dataset",
        "find_files",
        "read_file_contents",
        "file_analysis",
        "calendar",
        "email",
        "schedule_recurring_message_tool",
        "procore",
        "egnyte",
        "notion",
        "slack",
        "microsoft_teams",
        "sharepoint",
        "drive",
        "fieldwire",
        "webbrowser",
        "pdf_manipulation",
        "pdf_generator",
        "acc",
        "docusign",
        "webflow",
        "hubspot",
        "nec",
        "github",
        "trimble_project_site",
        "trimble",
        "linkedin",
        "google_docs",
        "google_slides",
        "google_sheets",
        "avoma",
        "content_writer",
        "code_tool",
        "data_classification",
        "data_extraction",
        "image_detection",
        "attachment_extraction",
        "pdf_extraction",
        "pdf_page_info",
        "youtube_video_analysis",
        "calculate",
        "pdf_form_filling",
        "image_generator",
        "video_generator",
        "connect_data",
        "download_data",
        "web_search",
        "fetch_url",
        "company_prospect_researcher",
        "people_prospect_researcher",
    ],
    str,
    ToolParam,
]

Tool: TypeAlias = Union[
    Literal[
        "data_analysis",
        "semantic_search",
        "agent_memory",
        "schema_info",
        "table_info",
        "create_dataset",
        "find_files",
        "read_file_contents",
        "file_analysis",
        "calendar",
        "email",
        "schedule_recurring_message_tool",
        "procore",
        "egnyte",
        "notion",
        "slack",
        "microsoft_teams",
        "sharepoint",
        "drive",
        "fieldwire",
        "webbrowser",
        "pdf_manipulation",
        "pdf_generator",
        "acc",
        "docusign",
        "webflow",
        "hubspot",
        "nec",
        "github",
        "trimble_project_site",
        "trimble",
        "linkedin",
        "google_docs",
        "google_slides",
        "google_sheets",
        "avoma",
        "content_writer",
        "code_tool",
        "data_classification",
        "data_extraction",
        "image_detection",
        "attachment_extraction",
        "pdf_extraction",
        "pdf_page_info",
        "youtube_video_analysis",
        "calculate",
        "pdf_form_filling",
        "image_generator",
        "video_generator",
        "connect_data",
        "download_data",
        "web_search",
        "fetch_url",
        "company_prospect_researcher",
        "people_prospect_researcher",
    ],
    str,
    ToolParam,
    ToolParam,
]
