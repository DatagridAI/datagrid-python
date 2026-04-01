# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .identity_teamspace import IdentityTeamspace

__all__ = ["Identity"]


class Identity(BaseModel):
    current_teamspace_id: str
    """
    The teamspace ID this request is scoped to (derived from the API key or the
    Datagrid-Teamspace header).
    """

    object: Literal["identity"]

    teamspaces: List[IdentityTeamspace]
    """All teamspaces the authenticated user is a member of."""

    user_id: str
    """The ID of the authenticated user."""
