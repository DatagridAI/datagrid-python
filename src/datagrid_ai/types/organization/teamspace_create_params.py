# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TeamspaceCreateParams"]


class TeamspaceCreateParams(TypedDict, total=False):
    access: Required[Literal["open", "closed"]]
    """Open teamspaces allow all organization members to join without admin approval.

    Access for users who join this way is limited to conversations with agents in
    this teamspace.

    Closed teamspaces require admin approval to join.
    """

    name: Required[str]
    """The name of the teamspace"""
