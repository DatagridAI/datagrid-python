# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SummaryListParams"]


class SummaryListParams(TypedDict, total=False):
    limit: int
    """The limit on the number of objects to return, ranging between 1 and 1000."""

    next: str
    """A cursor to use in pagination to continue a query from the previous request.

    This is automatically added when the request has more results to fetch.
    """

    record_type: Literal["row", "table", "file", "page"]
    """Which summary variant to return.

    `row` (default) returns one summary per source row. `table` returns the
    table-level summary. `file` returns file-level overviews. `page` returns page
    extraction bodies. Matches `record_type` on each Summary in the response.
    """
