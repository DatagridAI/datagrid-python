# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RedirectURLResponse"]


class RedirectURLResponse(BaseModel):
    """The `redirect_url` object represents a redirect url for a connection."""

    object: Literal["redirect_url"]

    redirect_url: str
    """The redirect url for a connection."""
