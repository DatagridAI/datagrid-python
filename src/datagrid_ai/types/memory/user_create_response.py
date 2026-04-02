# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .user_memory import UserMemory

__all__ = ["UserCreateResponse", "UserCreateResponseCredits"]


class UserCreateResponseCredits(BaseModel):
    """Credit consumption for this user-memory creation.

    `consumed` reflects the billed embedding work for the request. `null` when the billing write fails after the memory is successfully created.
    """

    consumed: float
    """The number of credits consumed by the operation."""


class UserCreateResponse(UserMemory):
    credits: Optional[UserCreateResponseCredits] = None
    """Credit consumption for this user-memory creation.

    `consumed` reflects the billed embedding work for the request. `null` when the
    billing write fails after the memory is successfully created.
    """
