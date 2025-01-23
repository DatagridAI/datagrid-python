# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConverseResponse", "Content"]


class Content(BaseModel):
    text: str


class ConverseResponse(BaseModel):
    agent_id: str
    """The ID of the agent used for the converse."""

    content: List[Content]
    """Contents of the converse response."""

    conversation_id: str
    """The ID of the agent conversation."""

    object: Literal["conversation.message"]
