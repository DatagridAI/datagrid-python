# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Secret"]


class Secret(BaseModel):
    """
    The `Secret` object represents a securely stored secret that can be referenced in converse API calls.
    """

    id: str
    """The secret identifier, which can be referenced in the converse API."""

    created_at: str
    """The date and time the secret was created"""

    name: str
    """The name of the secret"""

    object: Literal["secret"]
    """The object type, which is always `secret`."""
