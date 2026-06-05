# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .identity_teamspace import IdentityTeamspace

__all__ = ["Identity"]


class Identity(BaseModel):
    current_teamspace_id: str
    """The teamspace ID this request is scoped to.

    Resolution depends on the caller type:

    - **Org-scoped API keys** (default): always the teamspace the key was minted in.
      The `Datagrid-Teamspace` header is ignored.
    - **Account-scoped API keys** (`scopeLevel: "account"`): the teamspace selected
      by the `Datagrid-Teamspace` header, when that teamspace lives under the same
      account as the key. Falls back to the key's home teamspace when the header is
      absent.
    - **JWT callers**: the `Datagrid-Teamspace` header when present (and the user is
      a member), otherwise the user's default teamspace.
    """

    object: Literal["identity"]

    teamspaces: List[IdentityTeamspace]
    """All teamspaces the authenticated user is a member of."""

    user_id: str
    """The ID of the authenticated user."""
