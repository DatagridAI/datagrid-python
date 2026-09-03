# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .user_credit_consumption import UserCreditConsumption

__all__ = ["UserCreditConsumptionList"]


class UserCreditConsumptionList(BaseModel):
    data: List[UserCreditConsumption]
    """User credit consumption rows for this page."""

    first_id: Optional[str] = None
    """Opaque cursor for the first row on this page, or null when the page is empty."""

    has_more: bool
    """Whether additional rows exist after this page."""

    last_id: Optional[str] = None
    """Opaque cursor for the last row on this page, or null when the page is empty."""

    object: Literal["list"]
    """The object type, always 'list'."""
