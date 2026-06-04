# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .problem_details import ProblemDetails
from .batch_prediction_request_counts import BatchPredictionRequestCounts

__all__ = ["BatchPrediction"]


class BatchPrediction(BaseModel):
    """The `batch_prediction` object represents an asynchronous batch prediction job."""

    id: str
    """The id of the batch prediction."""

    cancelled_at: Optional[datetime] = None
    """ISO timestamp when the batch reached `cancelled`, or `null` otherwise."""

    cancelling_at: Optional[datetime] = None
    """ISO timestamp when cancellation was requested, or `null` otherwise."""

    completed_at: Optional[datetime] = None
    """ISO timestamp when the batch reached `completed`, or `null` otherwise."""

    completion_window: Literal["24h"]
    """Requested completion window."""

    created_at: datetime
    """ISO timestamp when the batch was created."""

    error: Optional[ProblemDetails] = None
    """
    Batch-level terminal error details for `failed`, `cancelled`, or `expired`
    batches; otherwise `null`.
    """

    expired_at: Optional[datetime] = None
    """ISO timestamp when the batch reached `expired`, or `null` otherwise."""

    expires_at: datetime
    """ISO timestamp when the batch completion window expires."""

    failed_at: Optional[datetime] = None
    """ISO timestamp when the batch reached `failed`, or `null` otherwise."""

    finalizing_at: Optional[datetime] = None
    """ISO timestamp when the batch entered `finalizing`, or `null` if it has not."""

    in_progress_at: Optional[datetime] = None
    """ISO timestamp when the batch entered `in_progress`, or `null` if it has not."""

    metadata: Optional[Dict[str, str]] = None
    """Optional metadata map with up to 16 entries.

    Metadata keys must be 64 characters or fewer and values must be 512 characters
    or fewer.
    """

    model: Literal[
        "gemini-2.5-flash",
        "gemini-2.5-flash-lite",
        "gemini-3.1-flash-lite",
        "gemini-2.5-pro",
        "anthropic.claude-haiku-4-5-20251001-v1:0",
        "anthropic.claude-sonnet-4-5-20250929-v1:0",
        "amazon.nova-2-lite-v1:0",
    ]
    """LLM model to use for every item in the batch."""

    object: Literal["batch_prediction"]
    """The object type, which is always `batch_prediction`."""

    request_counts: BatchPredictionRequestCounts
    """The sum of processing, succeeded, errored, canceled, and expired equals total."""

    results_url: Optional[str] = None
    """Relative URL for the NDJSON results stream once the batch is terminal.

    This becomes `null` after retained result lines are cleaned up.
    """

    status: Literal[
        "validating", "failed", "in_progress", "finalizing", "completed", "expired", "cancelling", "cancelled"
    ]
    """Current batch lifecycle state.

    Terminal states are `completed`, `failed`, `expired`, and `cancelled`.
    """
