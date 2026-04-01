# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .search_result_item import SearchResultItem

__all__ = ["SearchSearchResponse", "Credits"]


class Credits(BaseModel):
    """Credit consumption for this search.

    When present, `consumed` reflects the actual variable cost of the retrieval work performed for this request. `null` when the billing write fails or the request is aborted before billing completes.
    """

    consumed: float
    """The number of credits consumed by the operation."""


class SearchSearchResponse(BaseModel):
    credits: Optional[Credits] = None
    """Credit consumption for this search.

    When present, `consumed` reflects the actual variable cost of the retrieval work
    performed for this request. `null` when the billing write fails or the request
    is aborted before billing completes.
    """

    data: List[SearchResultItem]
    """An array containing the found search items."""

    object: Literal["list"]
