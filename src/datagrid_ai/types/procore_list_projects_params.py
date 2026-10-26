# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProcoreListProjectsParams"]


class ProcoreListProjectsParams(TypedDict, total=False):
    page: int
    """1-based page number. Values below 1 are treated as 1."""

    per_page: int
    """Items per page. Values above 100 are clamped to 100."""
