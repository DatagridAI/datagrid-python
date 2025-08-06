# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .agent_tools import AgentTools

__all__ = ["AgentToolItemParam"]


class AgentToolItemParam(TypedDict, total=False):
    name: Required[AgentTools]

    connection_id: str
    """The ID of the connection to use for the tool."""
