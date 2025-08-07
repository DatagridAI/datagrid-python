# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectionCreateParams"]


class ConnectionCreateParams(TypedDict, total=False):
    connector_id: Required[str]
    """The connector ID for the third-party service to connect to."""
