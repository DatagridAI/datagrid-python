# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChannelMember", "Actor"]


class Actor(BaseModel):
    id: str

    type: Literal["user", "agent"]

    email: Optional[str] = None

    name: Optional[str] = None


class ChannelMember(BaseModel):
    id: str

    actor: Actor

    channel_id: str

    created_at: datetime

    object: Literal["channel.member"]
