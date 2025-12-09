# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolDef"]


class ToolDef(BaseModel):
    """The `Tool` object represents a tool that can be used by agents."""

    description: str
    """A detailed description of what the tool does."""

    label: str
    """The display name of the tool."""

    name: str
    """The unique identifier name used to reference the tool."""

    object: Literal["tool"]
    """The object type, which is always `tool`."""
