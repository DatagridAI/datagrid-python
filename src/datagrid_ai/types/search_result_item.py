# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .search_result_resource import SearchResultResource

__all__ = ["SearchResultItem"]


class SearchResultItem(BaseModel):
    content: List[str]
    """Text snippets relevant to the search query."""

    object: Literal["search_result_item"]
    """The object type, which is always `search_result_item`."""

    resource: SearchResultResource
    """The resource that matched the search query."""

    score: float
    """The score of the item, between 0 and 1."""

    updated_at: datetime
    """The date and time the item was last updated."""

    summary: Optional[str] = None
    """The summary of the item."""

    title: Optional[str] = None
    """The title of the item."""
