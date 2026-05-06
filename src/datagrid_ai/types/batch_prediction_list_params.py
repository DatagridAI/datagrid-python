# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BatchPredictionListParams"]


class BatchPredictionListParams(TypedDict, total=False):
    after: str
    """Opaque cursor returned by a previous list call."""

    limit: int
    """The maximum number of batch predictions to return, between 1 and 100."""

    status: Literal[
        "validating", "failed", "in_progress", "finalizing", "completed", "expired", "cancelling", "cancelled"
    ]
    """Optional filter by batch prediction status."""
