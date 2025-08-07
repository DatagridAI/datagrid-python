# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CreditsReport"]


class CreditsReport(BaseModel):
    consumed: float
    """The number of credits consumed in the current billing period."""

    remaining: float
    """The number of unused credits remaining for the current billing period."""

    total: float
    """The initial total number of credits for the current billing period."""
