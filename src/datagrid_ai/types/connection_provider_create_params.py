# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectionProviderCreateParams"]


class ConnectionProviderCreateParams(TypedDict, total=False):
    client_id: Required[str]
    """The OAuth client ID to use for this connector."""

    client_secret: Required[str]
    """The OAuth client secret to use for this connector."""

    connector_id: Required[str]
    """The connector ID this provider is configured for."""

    name: Required[str]
    """The name of the connection provider."""
