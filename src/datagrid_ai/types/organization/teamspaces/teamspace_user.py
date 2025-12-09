# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["TeamspaceUser", "Permissions"]


class Permissions(BaseModel):
    """The permissions assigned to the user in the teamspace"""

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


class TeamspaceUser(BaseModel):
    """Represents a user in a teamspace"""

    id: str
    """The unique identifier of the user"""

    email: str
    """The email address of the user"""

    first_name: str
    """The first name of the user"""

    last_name: str
    """The last name of the user"""

    permissions: Permissions
    """The permissions assigned to the user in the teamspace"""
