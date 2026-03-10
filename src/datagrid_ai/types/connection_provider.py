# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectionProvider"]


class ConnectionProvider(BaseModel):
    """
    The `ConnectionProvider` object represents custom OAuth credentials for a connector. When creating a connection with a connection provider, the specified client ID and secret will be used instead of the default credentials.
    """

    id: str
    """The connection provider identifier."""

    client_id: str
    """The OAuth client ID to use for this connector."""

    client_secret_id: str
    """
    The ID of the secret containing the OAuth client secret to use for this
    connector.
    """

    connector_id: str
    """The connector ID this provider is configured for."""

    created_at: datetime
    """The date and time the connection provider was created."""

    name: str
    """The name of the connection provider."""

    object: Literal["connection_provider"]
    """The object type, which is always `connection_provider`."""

    updated_at: datetime
    """The date and time the connection provider was last updated."""
