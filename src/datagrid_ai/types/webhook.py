# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Webhook"]


class Webhook(BaseModel):
    """The `webhook` object represents an outbound webhook subscription."""

    id: str
    """The webhook identifier."""

    created_at: datetime
    """The ISO string for when the webhook was created."""

    enabled: bool
    """Whether delivery is enabled for this webhook."""

    events: List[
        Literal[
            "knowledge.processing.completed",
            "batch_prediction.completed",
            "batch_prediction.failed",
            "batch_prediction.expired",
            "batch_prediction.cancelled",
        ]
    ]
    """The subscribed event types.

    Currently delivered events include `knowledge.processing.completed`,
    `batch_prediction.completed`, `batch_prediction.failed`,
    `batch_prediction.expired`, and `batch_prediction.cancelled`.
    """

    object: Literal["webhook"]
    """The object type, which is always `webhook`."""

    updated_at: datetime
    """The ISO string for when the webhook was last updated."""

    url: str
    """The destination URL for webhook deliveries."""
