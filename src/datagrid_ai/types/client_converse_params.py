# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .agent_tools import AgentTools

__all__ = [
    "ClientConverseParams",
    "PromptInputItemList",
    "PromptInputItemListContentInputMessageContentList",
    "PromptInputItemListContentInputMessageContentListInputText",
    "PromptInputItemListContentInputMessageContentListInputFile",
    "Config",
]


class ClientConverseParams(TypedDict, total=False):
    prompt: Required[Union[str, Iterable[PromptInputItemList]]]
    """A text prompt to send to the agent."""

    agent_id: str
    """The ID of the agent that should be used for the converse.

    If both agent_id and conversation_id aren't provided - the new agent is created.
    """

    config: Config
    """The config that overrides the default config of the agent for that converse."""

    conversation_id: str
    """The ID of the present conversation to use.

    If it's not provided - a new conversation will be created.
    """

    generate_citations: bool
    """Determines whether the response should include citations.

    When enabled, the agent will generate citations for factual statements.
    """

    stream: bool
    """Determines the response type of the converse.

    Response is the Server-Sent Events if stream is set to true.
    """


class PromptInputItemListContentInputMessageContentListInputText(TypedDict, total=False):
    text: Required[str]
    """The text input to the model."""

    type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


class PromptInputItemListContentInputMessageContentListInputFile(TypedDict, total=False):
    file_id: Required[str]
    """The ID of the file to be sent to the model."""

    type: Required[Literal["input_file"]]
    """The type of the input item. Always `input_file`."""


PromptInputItemListContentInputMessageContentList: TypeAlias = Union[
    PromptInputItemListContentInputMessageContentListInputText,
    PromptInputItemListContentInputMessageContentListInputFile,
]


class PromptInputItemList(TypedDict, total=False):
    content: Required[Union[str, Iterable[PromptInputItemListContentInputMessageContentList]]]
    """Text or file input to the agent."""

    role: Required[Literal["user"]]
    """The role of the message input. Always `user`."""

    type: Literal["message"]
    """The type of the message input. Always `message`."""


class Config(TypedDict, total=False):
    agent_model: Literal["magpie-1", "magpie-1.1", "magpie-1.1-flash"]
    """The version of Datagrid's agent brain."""

    agent_tools: Optional[List[AgentTools]]
    """Array of the agent tools to enable.

    If not provided - default tools of the agent are used. If empty list provided -
    none of the tools are used. If null provided - all tools are used.

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

    custom_prompt: str
    """Use custom prompt to instruct the style and formatting of the agent's response"""

    knowledge_ids: Optional[List[str]]
    """Array of Knowledge IDs the agent should use during the converse.

    If not provided - default settings are used. If null provided - all available
    knowledge is used.
    """

    llm_model: Literal[
        "gemini-1.5-flash-001",
        "gemini-1.5-flash-002",
        "gemini-2.0-flash-001",
        "gemini-2.0-flash",
        "gemini-2.5-flash-preview-04-17",
        "gemini-2.5-flash",
        "gemini-1.5-pro-001",
        "gemini-1.5-pro-002",
        "gemini-2.5-pro-preview-05-06",
        "gemini-2.5-pro",
        "chatgpt-4o-latest",
        "gpt-4",
        "gpt-4-turbo",
        "gpt-4o",
        "gpt-4o-mini",
    ]
    """The LLM used to generate responses."""

    system_prompt: str
    """Directs your AI Agent's operational behavior."""
