# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SearchTreeResult", "Credits"]


class Credits(BaseModel):
    """Credit consumption for this search.

    When present, `consumed` reflects the actual variable cost of the retrieval work performed for this request. `null` when the billing write fails or the request is aborted before billing completes.
    """

    consumed: float
    """The number of credits consumed by the operation."""


class SearchTreeResult(BaseModel):
    """
    Hierarchical search results grouped by source (datasets, files, pages) with navigation items.
    """

    credits: Optional[Credits] = None
    """Credit consumption for this search.

    When present, `consumed` reflects the actual variable cost of the retrieval work
    performed for this request. `null` when the billing write fails or the request
    is aborted before billing completes.
    """

    data: List[object]
    """Tree nodes representing search results grouped by source.

    Each node contains the matched content, metadata, score, and child nodes for
    hierarchical display.
    """

    has_more: bool
    """Whether more results are available beyond this page.

    Use the `next` cursor to fetch additional results.
    """

    nav_items: List[object]
    """
    Navigation items providing quick links to the datasets, tables, and files that
    matched the query. Each item includes a name, emoji, URL, and type.
    """

    object: Literal["search_tree"]
    """The object type, always `search_tree`."""

    query: str
    """The original search query."""

    next: Optional[str] = None
    """Pagination cursor (numeric offset as string).

    Pass this value as the `next` query parameter to `/search/tree` to fetch the
    next page.
    """
