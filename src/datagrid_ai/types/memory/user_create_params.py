# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    agent_id: Required[str]
    """The agent ID of the user memory."""

    memory: Required[str]
    """The memory of the user memory."""

    context: Optional[str]
    """The context of the user memory."""

    user_prompt: Optional[str]
    """The user prompt of the user memory."""
