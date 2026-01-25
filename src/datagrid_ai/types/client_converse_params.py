# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
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
    "Config",
    "ConfigAgentTool",
    "ConfigCorpus",
    "ConfigCorpusCorpusKnowledgeItem",
    "ConfigCorpusCorpusPageItem",
    "ConfigDisabledAgentTool",
    "ConfigDisabledTool",
    "ConfigTool",
    "Text",
    "User",
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
    Structured output is not supported only supported by the default agent model,
    magpie-1.1 and magpie-2.0.
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


ConfigAgentTool: TypeAlias = Union[
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
        "planner",
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

ConfigDisabledAgentTool: TypeAlias = Union[
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
        "planner",
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

ConfigDisabledTool: TypeAlias = Union[
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
        "planner",
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

ConfigTool: TypeAlias = Union[
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
        "planner",
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


class Config(TypedDict, total=False):
    """Override the agent config for this converse call.

    This is applied as a partial override.
    """

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

    agent_tools: Optional[List[ConfigAgentTool]]
    """Deprecated, use tools instead"""

    corpus: Optional[Iterable[ConfigCorpus]]
    """Array of corpus items the agent should use during the converse.

    When omitted, all knowledge is used.
    """

    custom_prompt: Optional[str]
    """Use custom prompt to instruct the style and formatting of the agent's response"""

    disabled_agent_tools: Optional[List[ConfigDisabledAgentTool]]
    """Deprecated, use disabled_tools instead.

    If not provided - no tools are disabled.
    """

    disabled_tools: Optional[List[ConfigDisabledTool]]
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
            "gemini-3-flash-preview",
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

    planning_prompt: Optional[str]
    """
    Define the planning strategy your AI Agent should use when breaking down tasks
    and solving problems
    """

    system_prompt: Optional[str]
    """Directs your AI Agent's operational behavior."""

    tools: Optional[List[ConfigTool]]
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
    """
    Contains the format property used to specify the structured output schema.
    Structured output is not supported only supported by the default agent model, magpie-1.1 and magpie-2.0.
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
