# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .tool_name import ToolName

__all__ = ["ToolParam"]


class ToolParam(TypedDict, total=False):
    name: Required[ToolName]
    """The unique identifier for a tool."""

    connection_id: Optional[str]
    """The ID of the connection to use for the tool."""
