# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ConversationUpdateParams"]


class ConversationUpdateParams(TypedDict, total=False):
    agent_ids: SequenceNotStr[str]
    """Replace the list of agents assigned to this conversation.

    Pass an empty array to clear all agent assignments.
    """

    name: str
    """Update the conversation name."""
