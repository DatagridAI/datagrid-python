# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["McpServer", "Metadata", "ManagedByApp"]


class Metadata(BaseModel):
    """Safe subset of server metadata exposed to API consumers."""

    last_synced_at: Optional[str] = None

    oauth_configured: Optional[bool] = None

    requires_oauth: Optional[bool] = None

    tool_count: Optional[int] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ManagedByApp(BaseModel):
    """Present when the MCP server is provisioned and managed by an installed app.

    Managed servers are read-only through this API.
    """

    app_name: Optional[str] = None
    """The display name of the app that manages the MCP server.

    Falls back to app_uuid when the app installation is not known to this teamspace.
    """

    app_uuid: Optional[str] = None
    """The UUID of the app that manages the MCP server."""


class McpServer(BaseModel):
    id: str

    authorization_secret_id: Optional[str] = None
    """
    Secret ID containing the full Authorization header value used for this
    registered MCP server.
    """

    base_url: str

    created_at: datetime

    icon_url: Optional[str] = None

    metadata: Optional[Metadata] = None
    """Safe subset of server metadata exposed to API consumers."""

    name: str

    object: Literal["mcp_server"]

    protocol_version: Optional[str] = None

    status: str

    transport: str

    updated_at: datetime

    managed_by_app: Optional[ManagedByApp] = None
    """Present when the MCP server is provisioned and managed by an installed app.

    Managed servers are read-only through this API.
    """
