# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ProblemDetails"]


class ProblemDetails(BaseModel):
    status: int

    title: str

    type: str

    detail: Optional[str] = None

    instance: Optional[str] = None
