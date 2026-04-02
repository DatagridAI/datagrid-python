# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConnectionProviderUpdateParams"]


class ConnectionProviderUpdateParams(TypedDict, total=False):
    client_id: str
    """The OAuth client ID to use for this connector."""

    client_secret: str
    """The OAuth client secret to use for this connector."""

    name: str
    """The name of the connection provider."""
