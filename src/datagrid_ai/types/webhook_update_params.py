# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    enabled: bool
    """Enable or disable webhook delivery."""

    events: SequenceNotStr[str]
    """Updated set of event type subscriptions."""

    url: str
    """Updated HTTPS destination URL."""
