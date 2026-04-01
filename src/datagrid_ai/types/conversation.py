# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Conversation"]


class Conversation(BaseModel):
    """The `conversation` object represents a conversation with an AI agent."""

    id: str
    """The conversation identifier, which can be referenced in the API endpoints."""

    created_at: datetime
    """The ISO string for when the conversation was created."""

    object: Literal["conversation"]
    """The object type, which is always `conversation`."""

    updated_at: datetime
    """The ISO string for when the conversation was last updated."""

    agent_ids: Optional[List[str]] = None
    """Array of agent IDs currently assigned to this conversation."""

    name: Optional[str] = None
    """The name of the conversation."""

    participated_agent_ids: Optional[List[str]] = None
    """Array of agent IDs that have previously responded in this conversation.

    This list only grows and is never cleared when agents are reassigned.
    """
