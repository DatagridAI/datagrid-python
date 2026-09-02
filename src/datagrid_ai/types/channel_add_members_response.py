# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .channel_member import ChannelMember

__all__ = ["ChannelAddMembersResponse"]


class ChannelAddMembersResponse(BaseModel):
    data: List[ChannelMember]

    object: Literal["list"]

    has_more: Optional[bool] = None
