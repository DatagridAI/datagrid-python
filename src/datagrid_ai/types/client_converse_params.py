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
    "Config",
    "ConfigAgentTool",
    "ConfigDisabledAgentTool",
    "ConfigDisabledTool",
    "ConfigTool",
    "Text",
]


class ClientConverseParams(TypedDict, total=False):
    prompt: Required[Union[str, Iterable[PromptInputItemList]]]
    """A text prompt to send to the agent."""

    agent_id: Optional[str]
    """The ID of the agent that should be used for the converse."""

    config: Optional[Config]
    """Override the agent config for this converse call.

    This is applied as a partial override.
    """

    conversation_id: Optional[str]
    """The ID of the present conversation to use.

    If it's not provided - a new conversation will be created.
    """

    generate_citations: Optional[bool]
    """Determines whether the response should include citations.

    When enabled, the agent will generate citations for factual statements.
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


ConfigAgentTool: TypeAlias = Union[ToolName, ToolParam]

ConfigDisabledAgentTool: TypeAlias = Union[ToolName, ToolParam]

ConfigDisabledTool: TypeAlias = Union[ToolName, ToolParam]

ConfigTool: TypeAlias = Union[ToolName, ToolParam, ToolParam]


class Config(TypedDict, total=False):
    agent_model: Optional[Literal["magpie-1.1", "magpie-1.1-flash", "magpie-1"]]
    """The version of Datagrid's agent brain.

    - magpie-1.1 is the default and most powerful model.
    - magpie-1.1-flash is a faster model useful for RAG usecases, it currently only
      supports semantic_search tool. Structured outputs are not supported with this
      model.
    """

    agent_tools: Optional[Iterable[ConfigAgentTool]]
    """Deprecated, use tools instead"""

    custom_prompt: Optional[str]
    """Use custom prompt to instruct the style and formatting of the agent's response"""

    disabled_agent_tools: Optional[Iterable[ConfigDisabledAgentTool]]
    """Deprecated, use disabled_tools instead"""

    disabled_tools: Optional[Iterable[ConfigDisabledTool]]
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
            "gemini-2.5-pro",
            "gemini-2.5-pro-preview-05-06",
            "gemini-2.5-flash",
            "gemini-2.5-flash-preview-04-17",
            "gemini-2.5-flash-lite",
            "gpt-5",
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

    planning_prompt: Optional[str]
    """
    Define the planning strategy your AI Agent should use when breaking down tasks
    and solving problems
    """

    system_prompt: Optional[str]
    """Directs your AI Agent's operational behavior."""

    tools: Optional[Iterable[ConfigTool]]
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
