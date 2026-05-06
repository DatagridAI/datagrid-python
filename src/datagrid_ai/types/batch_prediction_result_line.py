# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .problem_details import ProblemDetails

__all__ = ["BatchPredictionResultLine"]


class BatchPredictionResultLine(BaseModel):
    """One NDJSON result line for a submitted batch item."""

    batch_id: str
    """The batch prediction id."""

    custom_id: str
    """The caller-defined item id from the create request."""

    error: Optional[ProblemDetails] = None
    """
    Problem details when `status` is `errored`, `canceled`, or `expired`; otherwise
    `null`.
    """

    object: Literal["batch_prediction.result"]
    """The object type, which is always `batch_prediction.result`."""

    output: Optional[Dict[str, builtins.object]] = None
    """The model output when `status` is `succeeded`; otherwise `null`."""

    status: Literal["succeeded", "errored", "canceled", "expired"]
    """Terminal status for an individual result line."""
