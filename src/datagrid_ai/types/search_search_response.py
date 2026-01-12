# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .search_result_item import SearchResultItem

__all__ = ["SearchSearchResponse"]


class SearchSearchResponse(BaseModel):
    data: List[SearchResultItem]
    """An array containing the found search items."""

    object: Literal["list"]

    next: Optional[str] = None
    """Cursor for fetching the next page of results."""
