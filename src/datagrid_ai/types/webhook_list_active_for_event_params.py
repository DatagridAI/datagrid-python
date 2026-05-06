# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookListActiveForEventParams"]


class WebhookListActiveForEventParams(TypedDict, total=False):
    event_type: Required[
        Literal[
            "knowledge.processing.completed",
            "batch_prediction.completed",
            "batch_prediction.failed",
            "batch_prediction.expired",
            "batch_prediction.cancelled",
        ]
    ]
    """
    The event type to filter by, for example `knowledge.processing.completed` or
    `batch_prediction.completed`.
    """
