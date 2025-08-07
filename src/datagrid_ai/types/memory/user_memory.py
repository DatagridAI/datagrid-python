# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["UserMemory"]


class UserMemory(BaseModel):
    id: str
    """The ID of the user memory."""

    agent_id: str
    """The agent ID of the user memory."""

    context: List[str]
    """The context of the user memory."""

    created_at: str
    """The created at of the user memory."""

    memory: List[str]
    """The memory of the user memory."""

    object: Literal["user_memory"]
    """The object type, which is always `user_memory`."""

    updated_at: str
    """The updated at of the user memory."""

    user_id: str
    """The user ID of the user memory."""

    user_prompt: str
    """The user prompt of the user memory."""
