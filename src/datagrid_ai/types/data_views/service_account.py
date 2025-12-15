# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ServiceAccount"]


class ServiceAccount(BaseModel):
    """
    The `service_account` object represents a service account for accessing data views.
    """

    id: str
    """The service account identifier."""

    created_at: datetime
    """The ISO string for when the service account was created."""

    email: str
    """The email address of the service account."""

    object: Literal["service_account"]
    """The object type, which is always `service_account`."""

    type: Literal["gcp"]
    """The type of service account, currently only `gcp` is supported."""
