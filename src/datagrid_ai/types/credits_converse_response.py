# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CreditsConverseResponse"]


class CreditsConverseResponse(BaseModel):
    consumed_for_conversation: float
    """The number of credits consumed for the entire conversation."""

    consumed_for_message: float
    """
    The number of credits consumed during this specific converse call for the
    message.
    """
