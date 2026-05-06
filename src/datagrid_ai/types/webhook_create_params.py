# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    events: Required[
        List[
            Literal[
                "knowledge.processing.completed",
                "batch_prediction.completed",
                "batch_prediction.failed",
                "batch_prediction.expired",
                "batch_prediction.cancelled",
            ]
        ]
    ]
    """List of event types to subscribe to.

    Currently delivered events include `knowledge.processing.completed`,
    `batch_prediction.completed`, `batch_prediction.failed`,
    `batch_prediction.expired`, and `batch_prediction.cancelled`.
    """

    url: Required[str]
    """HTTPS destination URL for webhook deliveries."""
