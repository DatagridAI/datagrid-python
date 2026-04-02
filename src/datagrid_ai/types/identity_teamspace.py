# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IdentityTeamspace", "Permissions"]


class Permissions(BaseModel):
    """The permissions the user holds in this teamspace."""

    role: Literal["owner", "admin", "member", "collaborator", "agents-only", "agent-specific"]
    """The role assigned to the user. Available roles:

    - **owner**: Creator of the teamspace. Full control over the teamspace. Can
      manage all users, settings, and resources.
    - **admin**: Full control over the teamspace. Can manage all users, settings,
      and resources.
    - **member**: Standard member access. Can view and interact with teamspace
      resources. Can invite other members.
    - **collaborator**: Read-only access with ability to comment and provide
      feedback.
    - **agents-only**: Access limited to AI agent interactions within the teamspace.
    - **agent-specific**: Limited access on teamspace level, can only access agents
      that are assigned to the teamspace.
    """

    agent_ids: Optional[List[str]] = None
    """The agent IDs that the user has access to, if the role is agent-specific."""


class IdentityTeamspace(BaseModel):
    permissions: Permissions
    """The permissions the user holds in this teamspace."""

    teamspace_id: str
    """The ID of the teamspace."""
