# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChannelAddMembersParams", "Actor"]


class ChannelAddMembersParams(TypedDict, total=False):
    actors: Required[Iterable[Actor]]


class Actor(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["user", "agent"]]
