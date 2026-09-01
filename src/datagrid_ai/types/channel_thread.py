# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChannelThread"]


class ChannelThread(BaseModel):
    id: str

    channel_id: str

    created_at: datetime

    object: Literal["thread"]

    updated_at: datetime

    name: Optional[str] = None

    root_message_id: Optional[str] = None
