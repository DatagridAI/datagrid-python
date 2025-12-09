# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .tool import Tool
from .._models import BaseModel

__all__ = ["Agent"]


class Agent(BaseModel):
    id: str
    """Unique identifier for the agent"""

    agent_model: Union[Literal["magpie-1.1", "magpie-1.1-flash", "magpie-1", "magpie-2.0"], str]
    """The version of Datagrid's agent brain.

    - magpie-1.1 is the default and most powerful model.
    - magpie-1.1-flash is a faster model useful for RAG usecases, it currently only
      supports semantic_search tool. Structured outputs are not supported with this
      model.
    - Can also accept any custom string value for future model versions.
    - Magpie-2.0 our latest agentic model with more proactive planning and reasoning
      capabilities.
    """

    created_at: datetime
    """The ISO string for when the agent was created"""

    custom_prompt: Optional[str] = None
    """Use custom prompt to instruct the style and formatting of the agent's response"""

    description: Optional[str] = None
    """The description of the agent"""

    knowledge_ids: Optional[List[str]] = None
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
    ]
    """The LLM used to generate responses."""

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
