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

    - **API keys with "All Teamspaces" access** (`scopeLevel: "account"`): the
      teamspace selected by the `Datagrid-Teamspace` header, when that teamspace
      lives under the same account as the key's home teamspace.
    - **API keys with "Selected Teamspaces" access** (`scopeLevel: "org"`): the
      teamspace selected by the `Datagrid-Teamspace` header, when it is on the key's
      teamspace list. A key whose list holds only its home teamspace ignores the
      header.
    - For either kind of key, the key's home teamspace (the one it was created in)
      when the header is absent.
    - **JWT callers**: the `Datagrid-Teamspace` header when present (and the user is
      a member), otherwise the user's default teamspace.
    """

    object: Literal["identity"]

    teamspaces: List[IdentityTeamspace]
    """All teamspaces the authenticated user is a member of."""

    user_id: str
    """The ID of the authenticated user."""
