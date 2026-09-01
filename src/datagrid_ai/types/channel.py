# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Channel"]


class Channel(BaseModel):
    id: str

    created_at: datetime

    description: Optional[str] = None

    name: str

    object: Literal["channel"]

    teamspace_id: str

    type: Literal["channel"]

    updated_at: datetime
