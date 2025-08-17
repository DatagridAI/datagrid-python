# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["TeamspaceInvite", "Permissions"]


class Permissions(BaseModel):
    role: Literal["admin", "member", "agents-only", "agent-specific"]
    """The role to assign to the user in the teamspace.

    Available roles: admin, member, agents-only, agent-specific
    """

    agent_ids: Optional[List[str]] = None
    """
    The IDs of the agents that the user has access to, if the role is agent-specific
    """


class TeamspaceInvite(BaseModel):
    id: str
    """The ID of the invite. Only present if the invite is pending."""

    email: str
    """The email address of the user invited"""

    permissions: Permissions
    """Represents the permissions assigned to a user in a teamspace"""

    status: Literal["pending", "accepted"]
    """Whether the user has accepted the invite"""

    accepted_at: Optional[datetime] = None
    """The date and time the user accepted the invite.

    Only present if the invite is accepted.
    """
