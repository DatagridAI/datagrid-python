# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .agent_tools import AgentTools

__all__ = ["AgentToolItem"]


class AgentToolItem(BaseModel):
    name: AgentTools

    connection_id: Optional[str] = None
    """The ID of the connection to use for the tool."""
