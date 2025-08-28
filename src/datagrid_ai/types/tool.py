# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .tool_name import ToolName

__all__ = ["Tool"]


class Tool(BaseModel):
    name: ToolName

    connection_id: Optional[str] = None
    """The ID of the connection to use for the tool."""
