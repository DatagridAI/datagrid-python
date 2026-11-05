# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .consumption_breakdown import ConsumptionBreakdown

__all__ = ["ConsumptionBreakdownList"]


class ConsumptionBreakdownList(BaseModel):
    data: List[ConsumptionBreakdown]
    """Consumption breakdown rows for this page."""

    first_id: Optional[str] = None
    """Opaque cursor for the first row on this page, or null when the page is empty."""

    has_more: bool
    """Whether additional rows exist after this page."""

    last_id: Optional[str] = None
    """Opaque cursor for the last row on this page, or null when the page is empty."""

    object: Literal["list"]
    """The object type, always 'list'."""
