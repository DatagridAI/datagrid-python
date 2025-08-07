# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Connector"]


class Connector(BaseModel):
    id: str
    """The unique identifier for the connector."""

    name: str
    """The display name of the connector."""

    object: Literal["connector"]
    """The object type, which is always `connector`."""
