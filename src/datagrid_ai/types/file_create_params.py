# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    file: Required[FileTypes]

    expires_after: Optional[int]
    """
    The number of seconds after creation when the file will expire and be
    automatically deleted. Must be a positive integer, maximum 6 days (518400s). If
    not provided, the file will not expire.
    """
