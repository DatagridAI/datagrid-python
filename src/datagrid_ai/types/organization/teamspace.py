# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Teamspace"]


class Teamspace(BaseModel):
    id: str

    access: Optional[Literal["open", "closed"]] = None
    """Open teamspaces allow all organization members to join without admin approval.

    Access for users who join this way is limited to conversations with agents in
    this teamspace.

    Closed teamspaces require admin approval to join.
    """

    created_at: Optional[datetime] = None
    """The ISO string for when the teamspace was created."""

    name: Optional[str] = None
    """The name of the teamspace"""
