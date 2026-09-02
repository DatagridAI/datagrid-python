# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HandleMcpOAuthCallbackResponse"]


class HandleMcpOAuthCallbackResponse(BaseModel):
    oauth_configured: Literal[True]
    """
    Always true when the endpoint returns success; the flow only completes if the
    token exchange succeeded.
    """

    object: Literal["mcp_oauth_callback"]

    tools_synced: bool
    """
    True if Datagrid automatically re-synced the MCP server's tool manifest after
    the OAuth exchange. False if the caller lacks organization-edit permissions or
    the sync itself failed.
    """

    message: Optional[str] = None
    """Human-readable outcome.

    Optional product copy — branch on `oauth_configured` and `tools_synced` rather
    than matching this text.
    """
