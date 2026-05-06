# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    enabled: bool
    """Enable or disable webhook delivery."""

    events: List[
        Literal[
            "knowledge.processing.completed",
            "batch_prediction.completed",
            "batch_prediction.failed",
            "batch_prediction.expired",
            "batch_prediction.cancelled",
        ]
    ]
    """Updated set of event type subscriptions.

    Currently delivered events include `knowledge.processing.completed`,
    `batch_prediction.completed`, `batch_prediction.failed`,
    `batch_prediction.expired`, and `batch_prediction.cancelled`.
    """

    url: str
    """Updated HTTPS destination URL."""
