# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .user_memory import UserMemory

__all__ = ["UserListResponse"]


class UserListResponse(BaseModel):
    data: List[UserMemory]
    """
    An array containing the actual response elements, paginated by any request
    parameters.
    """

    object: Literal["list"]

    has_more: Optional[bool] = None
    """Whether or not there are more elements available after this set.

    If false, this set comprises the end of the list.
    """
