# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .mcp_server import McpServer

__all__ = ["ListMcpServersResponse"]


class ListMcpServersResponse(BaseModel):
    data: List[McpServer]

    object: Literal["list"]
