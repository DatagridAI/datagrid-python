# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ChannelCreateMessageParams"]


class ChannelCreateMessageParams(TypedDict, total=False):
    content: Required[str]

    file_ids: Optional[SequenceNotStr[str]]
