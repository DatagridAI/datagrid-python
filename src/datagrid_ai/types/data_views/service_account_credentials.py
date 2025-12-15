# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ServiceAccountCredentials"]


class ServiceAccountCredentials(BaseModel):
    """The credentials for a service account."""

    object: Literal["service_account_credentials"]
    """The object type, which is always `service_account_credentials`."""

    private_key: str
    """The private key for the service account in JSON format."""

    type: Optional[Literal["gcp"]] = None
    """The type of service account credentials, currently only `gcp` is supported."""
