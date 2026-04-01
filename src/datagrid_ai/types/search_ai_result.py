# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .ai_source import AISource
from .search_tree_result import SearchTreeResult

__all__ = ["SearchAIResult", "Credits"]


class Credits(BaseModel):
    """Credit consumption for this search.

    When present, `consumed` reflects the actual variable cost of the retrieval work performed for this request. `null` when the billing write fails or the request is aborted before billing completes.
    """

    consumed: float
    """The number of credits consumed by the operation."""


class SearchAIResult(BaseModel):
    """AI-generated answer with source citations and the underlying search results."""

    answer: str
    """AI-generated natural language answer based on the search results.

    Contains numbered citations like [1], [2] that reference entries in the
    `sources` array.
    """

    credits: Optional[Credits] = None
    """Credit consumption for this search.

    When present, `consumed` reflects the actual variable cost of the retrieval work
    performed for this request. `null` when the billing write fails or the request
    is aborted before billing completes.
    """

    object: Literal["search_ai_result"]
    """The object type, always `search_ai_result`."""

    search_results: SearchTreeResult
    """The full search tree results used to generate the answer.

    Useful for displaying raw results alongside the AI summary.
    """

    sources: List[AISource]
    """Sources cited in the answer, ordered by citation index.

    Each source links back to the original data in your teamspace.
    """
