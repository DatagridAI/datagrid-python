# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SearchSearchParams"]


class SearchSearchParams(TypedDict, total=False):
    query: Required[str]
    """The search query to run against knowledge.

    Must contain at least one non-whitespace character after trimming.
    """

    knowledge_ids: SequenceNotStr[str]
    """Optional list of knowledge IDs to scope the search to."""

    limit: int
    """The limit on the number of objects to return, ranging between 1 and 100."""

    next: str
    """A cursor to use in pagination to continue a query from the previous request.

    This is automatically added when the request has more results to fetch.
    """

    record_types: List[Literal["rows", "tables", "files", "pages", "cells"]]
    """Filter results by record type in the vector database."""
