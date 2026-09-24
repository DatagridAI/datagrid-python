# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SearchSearchTreeParams"]


class SearchSearchTreeParams(TypedDict, total=False):
    query: Required[str]
    """The natural language search query."""

    display_type: Literal["dataset", "document", "image", "channel"]
    """Filter results to one display type (dataset, document, image, or channel).

    Applied before pagination, so pages cover the full filtered result pool. When
    omitted, all display types are returned. Honored when paginated search is
    enabled for the teamspace (Gen Search phase 3).
    """

    limit: int
    """The limit on the number of objects to return, ranging between 1 and 100."""

    next: str
    """A cursor to use in pagination to continue a query from the previous request.

    This is automatically added when the request has more results to fetch.
    """

    record_types: List[Literal["rows", "tables", "files", "pages", "cells"]]
    """Filter results by record type in the vector database.

    When omitted, all record types are searched.
    """
