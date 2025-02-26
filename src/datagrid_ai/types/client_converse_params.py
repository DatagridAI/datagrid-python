# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .agent_tools import AgentTools

__all__ = ["ClientConverseParams", "Config"]


class ClientConverseParams(TypedDict, total=False):
    prompt: Required[str]
    """The input prompt."""

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

    stream: bool
    """Determines the response type of the converse.

    Response is the Server-Sent Events if stream is set to true.
    """


class Config(TypedDict, total=False):
    agent_model: Literal["magpie-1", "mapgie-1.1"]
    """The version of Datagrid's agent brain."""

    agent_tools: Optional[List[AgentTools]]
    """Array of the agent tools to enable.

    If not provided - default tools of the agent are used. If empty list provided -
    none of the tools are used. If null provided - all tools are used.
    """

    knowledge_ids: Optional[List[str]]
    """Array of Knowledge IDs the agent should use during the converse.

    If not provided - default settings are used. If null provided - all available
    knowledge is used.
    """

    llm_model: Literal[
        "gemini-1.5-flash-001",
        "gemini-1.5-flash-002",
        "gemini-2.0-flash-001",
        "gemini-1.5-pro-001",
        "gemini-1.5-pro-002",
        "chatgpt-4o-latest",
        "gpt-4",
        "gpt-4-turbo",
        "gpt-4o",
        "gpt-4o-mini",
    ]
    """The LLM used to generate responses."""

    system_prompt: str
    """Directs your AI Agent's operational behavior."""
