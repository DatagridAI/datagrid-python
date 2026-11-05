# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SearchSearchAIParams"]


class SearchSearchAIParams(TypedDict, total=False):
    query: Required[str]
    """The natural language search query.

    The AI will search your indexed knowledge and generate an answer.
    """

    display_type: Optional[Literal["dataset", "document", "image", "channel"]]
    """
    Product-facing grouping of one result card, aligned with the result tabs in the
    Datagrid web app. Derived from the card's structure and media type: tables and
    records are `dataset`, files with an `image/*` media type are `image`, other
    files and pages are `document`, and channels are `channel`.
    """

    limit: Optional[int]
    """Maximum number of search results to consider when generating the answer."""

    offset: Optional[int]
    """
    Number of results to skip before the returned page, for paginating search
    results. Combine with `skip_ai_generation: true` to fetch subsequent pages
    without regenerating the AI answer. Honored when paginated search is enabled for
    the teamspace (Gen Search phase 3).
    """

    record_types: Optional[List[Literal["rows", "tables", "files", "pages", "cells"]]]
    """
    Optional filter to restrict search to specific record types (rows, tables,
    files, pages, cells).
    """

    skip_ai_generation: Optional[bool]
    """
    When true, returns the requested page of search results without generating an AI
    answer (`answer` is null and `sources` is empty). Cannot be combined with
    streaming. Honored when paginated search is enabled for the teamspace (Gen
    Search phase 3).
    """
