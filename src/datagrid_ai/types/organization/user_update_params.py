# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    role: Required[Literal["admin", "member"]]
    """The role to assign to the user in the organization.

    Available roles: admin, member
    """
