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

    limit: Optional[int]
    """Maximum number of search results to consider when generating the answer."""

    record_types: Optional[List[Literal["rows", "tables", "files", "pages", "cells"]]]
    """
    Optional filter to restrict search to specific record types (rows, tables,
    files, pages, cells).
    """
