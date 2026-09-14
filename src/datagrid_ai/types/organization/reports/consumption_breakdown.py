# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ConsumptionBreakdown"]


class ConsumptionBreakdown(BaseModel):
    action: str
    """Human-readable action or service label."""

    created_at: datetime
    """When the consumption occurred."""

    credits: float
    """Credits consumed by this row.

    Fractional — the row is a sum of decimal ledger amounts.
    """

    object: Literal["consumption_breakdown"]
    """Object type discriminator."""

    organization: str
    """Consumer organization (teamspace) name."""

    credit_source: Optional[str] = None
    """Labelled source of the credits (for example a recurring invoice)."""

    resource: Optional[str] = None
    """Optional resource associated with the consumption."""

    resource_type: Optional[str] = None
    """Optional resource type associated with the consumption."""
