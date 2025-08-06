# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TeamspacePatchParams"]


class TeamspacePatchParams(TypedDict, total=False):
    access: Literal["open", "closed"]
    """Open teamspaces allow all organization members to join without admin approval.

    Access for users who join this way is limited to conversations with agents in
    this teamspace.

    Closed teamspaces require admin approval to join.
    """

    name: str
    """The new name of the teamspace"""
