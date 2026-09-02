# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ChannelCreateParams"]


class ChannelCreateParams(TypedDict, total=False):
    name: Required[str]
    """Channel name. Names longer than 50 characters are truncated."""

    description: Optional[str]
