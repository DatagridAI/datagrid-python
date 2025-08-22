# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InviteCreateParams", "Permissions"]


class InviteCreateParams(TypedDict, total=False):
    email: Required[str]
    """The email address of the user to invite"""

    permissions: Optional[Permissions]
    """The permissions to assign to the user in the teamspace"""


class Permissions(TypedDict, total=False):
    role: Required[Literal["admin", "member", "agents-only", "agent-specific"]]
    """The role to assign to the user in the teamspace.

    Available roles: admin, member, agents-only, agent-specific
    """

    agent_ids: Optional[List[str]]
    """
    The IDs of the agents that the user has access to, if the role is agent-specific
    """
