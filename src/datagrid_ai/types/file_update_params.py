# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FileUpdateParams"]


class FileUpdateParams(TypedDict, total=False):
    expires_after: int
    """Seconds from now until the file expires.

    Only applies to temporary files. Max 6 days (518400s). Omitted leaves expiration
    unchanged.
    """
