# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["UserCreditConsumption"]


class UserCreditConsumption(BaseModel):
    action: str
    """Human-readable action or service label."""

    created_at: datetime
    """When the consumption occurred."""

    credits: int
    """Credits consumed by this row."""

    object: Literal["user_credit_consumption"]
    """Object type discriminator."""

    organization: str
    """Consumer organization (teamspace) name."""

    user: str
    """Display name of the user who incurred the consumption."""

    credit_source: Optional[str] = None
    """Labelled source of the credits (for example a recurring invoice)."""

    resource: Optional[str] = None
    """Optional resource associated with the consumption."""

    resource_type: Optional[str] = None
    """Optional resource type associated with the consumption."""
