# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Connection"]


class Connection(BaseModel):
    id: str
    """The connection identifier, which can be referenced in the API endpoints."""

    connector_id: str
    """The connector ID of the third-party service this connection authenticates with."""

    created_at: datetime
    """The ISO string for when the connection was created."""

    name: str
    """The name of the connection."""

    object: Literal["connection"]
    """The object type, which is always `connection`."""

    teamspace_id: str
    """The teamspace ID that owns this connection."""

    updated_at: datetime
    """The ISO string for when the connection was last updated."""

    valid: Optional[bool] = None
    """Whether the connection authentication is valid."""

    value: Optional[str] = None
    """The authentication value of the connection."""
