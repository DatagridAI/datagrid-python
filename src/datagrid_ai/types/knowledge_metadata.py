# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["KnowledgeMetadata", "NavigationItem"]


class NavigationItem(BaseModel):
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


class KnowledgeMetadata(BaseModel):
    id: str
    """The unique identifier of the knowledge."""

    name: str
    """The name of the knowledge."""

    navigation_item: NavigationItem
    """The navigation item of the knowledge."""

    object: Literal["knowledge_metadata"]
    """The object type, which is always `knowledge_metadata`."""

    url: str
    """The url of the knowledge."""
