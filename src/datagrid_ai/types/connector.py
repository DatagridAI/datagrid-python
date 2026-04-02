# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Connector", "OAuthAppSettings"]


class OAuthAppSettings(BaseModel):
    """Connector's OAuth app settings requirements."""

    redirect_uri: str
    """The OAuth redirect URI that must be configured in your OAuth app settings"""

    scopes: Optional[List[str]] = None
    """The OAuth scopes that must be granted when configuring your OAuth app."""


class Connector(BaseModel):
    """
    The `connector` object represents an available connector that can be used to connect to a third-party service.
    """

    id: str
    """The unique identifier for the connector."""

    name: str
    """The display name of the connector."""

    object: Literal["connector"]
    """The object type, which is always `connector`."""

    oauth_app_settings: Optional[OAuthAppSettings] = None
    """Connector's OAuth app settings requirements."""
