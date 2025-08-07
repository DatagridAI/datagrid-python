# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .agent_tools import AgentTools
from .agent_tool_item_param import AgentToolItemParam

__all__ = [
    "ClientConverseParams",
    "PromptInputItemList",
    "PromptInputItemListContentInputMessageContentList",
    "PromptInputItemListContentInputMessageContentListInputText",
    "PromptInputItemListContentInputMessageContentListInputFile",
    "PromptInputItemListContentInputMessageContentListInputSecret",
    "Config",
    "ConfigAgentTool",
    "Text",
]


class ClientConverseParams(TypedDict, total=False):
    prompt: Required[Union[str, Iterable[PromptInputItemList]]]
    """A text prompt to send to the agent."""

    agent_id: Optional[str]
    """The ID of the agent that should be used for the converse.

    If both agent_id and conversation_id aren't provided - the new agent is created.
    """

    config: Optional[Config]
    """The config that overrides the default config of the agent for that converse."""

    conversation_id: Optional[str]
    """The ID of the present conversation to use.

    If it's not provided - a new conversation will be created.
    """

    generate_citations: Optional[bool]
    """Determines whether the response should include citations.

    When enabled, the agent will generate citations for factual statements.
    """

    secret_ids: Optional[List[str]]
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
    Contains the format property used to specify the structured output schema.
    Structured output is currently only supported by the default agent model,
    magpie-1.1.
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


class PromptInputItemListContentInputMessageContentListInputSecret(TypedDict, total=False):
    secret_id: Required[str]
    """The ID of the secret to be sent to the model."""

    type: Required[Literal["input_secret"]]
    """The type of the input item. Always `input_secret`."""


PromptInputItemListContentInputMessageContentList: TypeAlias = Union[
    PromptInputItemListContentInputMessageContentListInputText,
    PromptInputItemListContentInputMessageContentListInputFile,
    PromptInputItemListContentInputMessageContentListInputSecret,
]


class PromptInputItemList(TypedDict, total=False):
    content: Required[Union[str, Iterable[PromptInputItemListContentInputMessageContentList]]]
    """Text, file or secret input to the agent."""

    role: Required[Literal["user"]]
    """The role of the message input. Always `user`."""

    type: Literal["message"]
    """The type of the message input. Always `message`."""


ConfigAgentTool: TypeAlias = Union[AgentTools, AgentToolItemParam]


class Config(TypedDict, total=False):
    agent_model: Optional[Literal["magpie-1", "magpie-1.1", "magpie-1.1-flash"]]
    """The version of Datagrid's agent brain."""

    agent_tools: Optional[Iterable[ConfigAgentTool]]
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
        ]
    ]
    """The LLM used to generate responses."""

    system_prompt: Optional[str]
    """Directs your AI Agent's operational behavior."""


class Text(TypedDict, total=False):
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
