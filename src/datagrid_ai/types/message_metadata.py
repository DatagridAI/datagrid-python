# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessageMetadata", "Conversation", "ConversationNavigationItem"]


class ConversationNavigationItem(BaseModel):
    id: str
    """The id of the navigation item."""

    item_type: str
    """The type of the navigation item."""

    name: str
    """The name of the navigation item."""

    object: Literal["navigation_item_metadata"]
    """The object type, which is always `navigation_item_metadata`."""

    url: str
    """The url of the navigation item."""

    emoticon: Optional[str] = None
    """The emoticon of the navigation item."""

    source_media_type: Optional[str] = None
    """The media type of the navigation item if known."""


class Conversation(BaseModel):
    id: str
    """The id of the conversation."""

    name: str
    """The name of the conversation."""

    navigation_item: ConversationNavigationItem
    """The navigation item of the conversation."""

    object: Literal["conversation_metadata"]
    """The object type, which is always `conversation_metadata`."""

    url: str
    """The url of the conversation."""


class MessageMetadata(BaseModel):
    id: str
    """The id of the message."""

    author_id: str
    """The identifier of the message author (either a user ID or agent ID)."""

    author_type: Literal["user", "agent"]
    """Indicates whether the author is a user or an agent."""

    conversation: Conversation
    """The conversation that the message belongs to."""

    object: Literal["message_metadata"]
    """The object type, which is always `message_metadata`."""

    url: str
    """The url of the message."""

    author_name: Optional[str] = None
    """The pretty name of the author of the message."""
