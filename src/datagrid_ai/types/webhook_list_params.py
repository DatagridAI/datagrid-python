# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WebhookListParams"]


class WebhookListParams(TypedDict, total=False):
    cursor: str
    """A pagination cursor returned by a previous list call."""

    limit: int
    """The maximum number of webhook subscriptions to return."""
