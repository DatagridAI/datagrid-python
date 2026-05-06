# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BatchPredictionRequestCounts"]


class BatchPredictionRequestCounts(BaseModel):
    """The sum of processing, succeeded, errored, canceled, and expired equals total."""

    canceled: int
    """Items that were cancelled before completion."""

    errored: int
    """Items that ended with an error."""

    expired: int
    """Items that did not finish before the completion window elapsed."""

    processing: int
    """Items that are still pending or processing."""

    succeeded: int
    """Items that completed with a valid output."""

    total: int
    """Total number of submitted items."""
