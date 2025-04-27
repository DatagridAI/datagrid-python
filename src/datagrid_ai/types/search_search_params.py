# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SearchSearchParams"]


class SearchSearchParams(TypedDict, total=False):
    query: Required[str]

    limit: int
    """The limit on the number of objects to return, ranging between 1 and 100."""

    next: str
    """A cursor to use in pagination to continue a query from the previous request.

    This is automatically added when the request has more results to fetch.
    """
